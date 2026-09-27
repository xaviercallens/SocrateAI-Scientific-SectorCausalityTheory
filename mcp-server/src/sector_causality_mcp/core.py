"""Pure logic behind the MCP tools, kept free of any MCP dependency so it can be tested directly.

Honesty conventions (every tool result follows them):
- `ran`: whether the underlying check actually executed. `ran: false` never means "passed"; it means
  the check did not happen, and `reason` says why.
- A clean Lean axiom footprint certifies a *proof*, never that the *statement* is the right physics.
- Case verdicts are transcriptions of the papers; `check_cases_against_paper` re-derives them from the
  paper's own Table 1 so a transcription error is detectable rather than silently served.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

PKG_DIR = Path(__file__).resolve().parent

CRITERION = (
    "A self-dual point pins a physical transition if and only if the two sectors it exchanges are "
    "simultaneously critical and the fixed-point set is discrete. On a continuous moduli space with "
    "enhanced symmetry, the self-dual point is a point like any other, and any transition present sits "
    "where one sector crosses its own threshold -- not at the duality's fixed locus. When both dual "
    "sectors are populated and compete energetically, the self-dual point can be a preferred equilibrium "
    "rather than a transition. In every case, the duality relabels the sectors; the sector acts."
)
CRITERION_SOURCE = "papers/sector_thesis.tex, keybox 'The criterion.' (Section 1)"

PAPER_VERDICT_TO_KEY = {
    "Forced": "forced",
    "Not forced": "not_forced",
    "Constraint": "constraint",
    "Organisation": "organisation",
    "Preferred equilibrium": "preferred_equilibrium",
    "Open question": "open_question",
    "Not a duality": "excluded_not_a_duality",
    "No self-map": "excluded_no_self_map",
}

PAPERS = [
    {
        "file": "papers/sector_thesis.pdf",
        "source": "papers/sector_thesis.tex",
        "title": "When does self-duality cause physics? A machine-checked criterion, tested across sixteen "
                 "candidate physical systems, an interventional experiment, and real cosmological data",
        "role": "foundation paper (standalone statement of the theory)",
        "doi": "10.5281/zenodo.22985863",
        "doi_kind": "concept DOI of this paper's own dedicated Zenodo record (resolves to latest version)",
    },
    {
        "file": "papers/duality_sector.pdf",
        "source": "papers/duality_sector.tex",
        "title": "Duality is a structure; the sector is the cause",
        "role": "technical report with six dated addenda (full case-by-case arguments)",
        "doi": "10.5281/zenodo.22855581",
        "doi_kind": "concept DOI of the SocrateAI-Scientific-QuantumFluids software/companion archive",
    },
    {
        "file": "papers/cosmology_sectors.pdf",
        "source": "papers/cosmology_sectors.tex",
        "title": "Sectors in the sky",
        "role": "cosmological extension (wave dark matter, dark energy, K3 charge lattice, CMB test)",
        "doi": "10.5281/zenodo.22855581",
        "doi_kind": "concept DOI of the SocrateAI-Scientific-QuantumFluids software/companion archive",
    },
]


def repo_root() -> Path:
    """Repository root: $SCT_REPO_ROOT, else two levels above this package's `src/` directory."""
    env = os.environ.get("SCT_REPO_ROOT")
    if env:
        return Path(env).resolve()
    return PKG_DIR.parents[2]


def lean_dir() -> Path:
    env = os.environ.get("SCT_LEAN_DIR")
    return Path(env).resolve() if env else repo_root() / "lean"


# --------------------------------------------------------------------------------------------------
# Cases
# --------------------------------------------------------------------------------------------------

def load_cases(path: Path | None = None) -> dict:
    return json.loads((path or PKG_DIR / "cases.json").read_text())


def list_cases(data: dict | None = None) -> list[dict]:
    data = data or load_cases()
    return [{"id": c["id"], "name": c["name"], "verdict": c["verdict"], "why": c["why"]} for c in data["cases"]]


def get_case(query: str, data: dict | None = None) -> dict | None:
    """Exact id match first, then case-insensitive substring match on id or name (unique only)."""
    data = data or load_cases()
    q = query.strip().lower()
    for c in data["cases"]:
        if c["id"].lower() == q:
            return c
    hits = [c for c in data["cases"] if q in c["id"].lower() or q in c["name"].lower()]
    return hits[0] if len(hits) == 1 else None


def parse_paper_table(tex: str) -> list[tuple[str, str]]:
    """(case, verdict) rows of the paper's Table 1 (label tab:cases), in order, as written in LaTeX."""
    m = re.search(r"\\begin\{tabular\}.*?\\end\{tabular\}", tex, re.S)
    if not m or "tab:cases" not in tex[m.end():m.end() + 600]:
        raise ValueError("Table 1 (tab:cases) not found in the paper source")
    rows = []
    for line in m.group(0).splitlines():
        line = line.strip()
        if "&" not in line or line.startswith("\\textbf{Case}"):
            continue
        cells = [c.strip() for c in line.rstrip("\\").split(" & ")]
        if len(cells) >= 2:
            rows.append((cells[0], cells[1]))
    return rows


def check_cases_against_paper(data: dict | None = None, paper: Path | None = None) -> dict:
    """Compare every served verdict with the paper's own Table 1. Returns mismatches, missing, extra."""
    data = data or load_cases()
    paper = paper or repo_root() / "papers" / "sector_thesis.tex"
    if not paper.exists():
        return {"ran": False, "reason": f"paper source not found at {paper}"}
    rows = parse_paper_table(paper.read_text())
    table = {case: verdict for case, verdict in rows}
    served = {c["paper_case"]: c for c in data["cases"]}
    mismatches = []
    for case, verdict in table.items():
        c = served.get(case)
        if c is None:
            continue
        expected = PAPER_VERDICT_TO_KEY.get(verdict)
        if c["verdict"] != expected or c["paper_verdict"] != verdict:
            mismatches.append({"case": case, "paper": verdict, "served": c["verdict"]})
    missing = [case for case in table if case not in served]
    extra = [case for case in served if case not in table]
    return {
        "ran": True,
        "paper": str(paper),
        "rows_in_paper": len(rows),
        "cases_served": len(data["cases"]),
        "mismatches": mismatches,
        "missing_from_server": missing,
        "not_in_paper": extra,
        "consistent": not (mismatches or missing or extra),
    }


# --------------------------------------------------------------------------------------------------
# Lean theorem parsing
# --------------------------------------------------------------------------------------------------

@dataclass
class Theorem:
    name: str          # fully qualified (namespace-prefixed)
    short_name: str
    module: str
    kind: str          # theorem | lemma
    statement: str     # declaration text up to (not including) the top-level `:=`
    docstring: str
    line: int


_OPEN = "([{⟨⦃"
_CLOSE = ")]}⟩⦄"
_DECL = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(theorem|lemma)\s+([^\s(:{\[]+)")


def find_toplevel_walrus(text: str) -> int:
    """Index of the first `:=` at bracket depth 0, or -1. A named argument such as `(N := N)` is inside
    brackets and is skipped; this is the bug this project's own challenge generator once had."""
    depth = 0
    i = 0
    while i < len(text):
        ch = text[i]
        if text.startswith("--", i):
            nl = text.find("\n", i)
            i = len(text) if nl < 0 else nl
            continue
        if ch in _OPEN:
            depth += 1
        elif ch in _CLOSE:
            depth = max(0, depth - 1)
        elif depth == 0 and text.startswith(":=", i):
            return i
        i += 1
    return -1


def parse_lean_file(path: Path) -> list[Theorem]:
    src = path.read_text()
    lines = src.splitlines(keepends=True)
    offsets = [0]
    for ln in lines:
        offsets.append(offsets[-1] + len(ln))
    module = path.stem
    scopes: list[tuple[str, str]] = []   # (kind, name) for namespace/section, to resolve `end X`
    out: list[Theorem] = []
    pending_doc = ""
    i = 0
    while i < len(lines):
        raw = lines[i]
        s = raw.strip()
        if s.startswith("/--"):
            j = i
            buf = [raw]
            while "-/" not in lines[j] or (j == i and lines[j].strip() == "/--"):
                j += 1
                if j >= len(lines):
                    break
                buf.append(lines[j])
            doc = "".join(buf).strip()
            pending_doc = doc[3:-2].strip() if doc.endswith("-/") else doc[3:].strip()
            i = j + 1
            continue
        if s.startswith("/-"):
            depth = s.count("/-") - s.count("-/")
            j = i
            while depth > 0 and j + 1 < len(lines):
                j += 1
                depth += lines[j].count("/-") - lines[j].count("-/")
            i = j + 1
            continue
        mns = re.match(r"^(namespace|section)\s*(\S*)", s)
        if mns:
            scopes.append((mns.group(1), mns.group(2)))
            i += 1
            continue
        mend = re.match(r"^end\b\s*(\S*)", s)
        if mend and scopes:
            scopes.pop()
            i += 1
            continue
        md = _DECL.match(raw)
        if md:
            kind, short = md.group(1), md.group(2)
            rest = src[offsets[i]:]
            k = find_toplevel_walrus(rest)
            stmt = rest[:k] if k >= 0 else rest.split("\n\n", 1)[0]
            ns = ".".join(n for kd, n in scopes if kd == "namespace" and n)
            full = f"{ns}.{short}" if ns else short
            out.append(Theorem(full, short, module, kind, stmt.strip(), pending_doc, i + 1))
            pending_doc = ""
            i += 1
            continue
        if s and not s.startswith("--") and not s.startswith("@["):
            pending_doc = ""  # a docstring belongs only to the declaration immediately after it
        i += 1
    return out


def all_theorems(ldir: Path | None = None) -> list[Theorem]:
    ldir = ldir or lean_dir()
    out: list[Theorem] = []
    for p in sorted(ldir.glob("*.lean")):
        if p.name in ("lakefile.lean", "SectorCausality.lean"):
            continue
        out.extend(parse_lean_file(p))
    return out


def search_theorems(query: str, ldir: Path | None = None, limit: int = 25) -> list[dict]:
    q = query.lower()
    hits = []
    for t in all_theorems(ldir):
        hay = f"{t.name} {t.module} {t.docstring} {t.statement}".lower()
        if all(tok in hay for tok in q.split()):
            hits.append({"name": t.name, "module": t.module, "kind": t.kind, "line": t.line,
                         "docstring": t.docstring[:300]})
    return hits[:limit]


def get_theorem(name: str, ldir: Path | None = None) -> dict | None:
    ths = all_theorems(ldir)
    for t in ths:
        if t.name == name:
            return asdict(t)
    short = [t for t in ths if t.short_name == name or t.name.endswith("." + name)]
    return asdict(short[0]) if len(short) == 1 else None


# --------------------------------------------------------------------------------------------------
# Kernel verification
# --------------------------------------------------------------------------------------------------

def verify_module(module: str, ldir: Path | None = None, timeout: int = 900) -> dict:
    """Run `lake env lean <module>.lean`. Reports errors, `sorry` warnings and the `#print axioms`
    footprint. Returns ran=False (with the reason) when the toolchain or the built Mathlib cache is
    absent, instead of pretending."""
    ldir = ldir or lean_dir()
    caveat = ("A clean footprint certifies that the proof checks with the listed axioms. It does not "
              "certify that the statement is the right physics; that remains a human audit.")
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", module):
        return {"ran": False, "reason": f"invalid module name {module!r}", "caveat": caveat}
    f = ldir / f"{module}.lean"
    if not f.exists():
        return {"ran": False, "reason": f"no such module {f}", "caveat": caveat}
    lake = shutil.which("lake") or str(Path.home() / ".elan" / "bin" / "lake")
    if not Path(lake).exists():
        return {"ran": False, "reason": "lake (Lean toolchain) not found on PATH or in ~/.elan/bin",
                "caveat": caveat}
    mathlib_build = ldir / ".lake" / "packages" / "mathlib" / ".lake" / "build"
    if not mathlib_build.exists():
        return {"ran": False,
                "reason": f"Mathlib build cache not found ({mathlib_build}); run `lake exe cache get` "
                          "in the lean directory first (lake-manifest.json pins every dependency)",
                "caveat": caveat}
    try:
        p = subprocess.run([lake, "env", "lean", f.name], cwd=ldir, capture_output=True, text=True,
                           timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"ran": False, "reason": f"timed out after {timeout}s", "caveat": caveat}
    out = p.stdout + p.stderr
    errors = [ln for ln in out.splitlines() if ": error" in ln]
    sorries = [ln for ln in out.splitlines() if "declaration uses 'sorry'" in ln]
    axioms = {}
    for m in re.finditer(r"'([^']+)' depends on axioms: \[([^\]]*)\]", out):
        axioms[m.group(1)] = [a.strip() for a in m.group(2).split(",") if a.strip()]
    no_axioms = re.findall(r"'([^']+)' does not depend on any axioms", out)
    for n in no_axioms:
        axioms[n] = []
    standard = {"propext", "Classical.choice", "Quot.sound"}
    nonstandard = {n: ax for n, ax in axioms.items() if set(ax) - standard}
    return {
        "ran": True,
        "module": module,
        "exit_code": p.returncode,
        "errors": errors,
        "sorry_warnings": sorries,
        "axioms": axioms,
        "nonstandard_axioms": nonstandard,
        "clean": p.returncode == 0 and not errors and not sorries and not nonstandard and bool(axioms),
        "caveat": caveat,
    }


# --------------------------------------------------------------------------------------------------
# Reproductions (bounded, seconds)
# --------------------------------------------------------------------------------------------------

def run_reproduction(name: str, timeout: int = 60) -> dict:
    from . import reproductions
    if name not in reproductions.REGISTRY:
        return {"ran": False, "reason": f"unknown reproduction {name!r}",
                "available": sorted(reproductions.REGISTRY)}
    try:
        p = subprocess.run([sys.executable, "-m", "sector_causality_mcp.reproductions", name],
                           capture_output=True, text=True, timeout=timeout,
                           env={**os.environ, "PYTHONPATH": str(PKG_DIR.parent)})
    except subprocess.TimeoutExpired:
        return {"ran": False, "reason": f"timed out after {timeout}s", "name": name}
    if p.returncode != 0:
        return {"ran": False, "reason": "reproduction subprocess failed", "stderr": p.stderr[-2000:],
                "name": name}
    return json.loads(p.stdout)
