"""Tests for the Sector Causality MCP server. Every "it works" test is paired with a planted-defect
control showing the check can fail -- a test that can only pass is not evidence."""
import collections
import copy
import json
import os
import re
from pathlib import Path

import pytest

from sector_causality_mcp import core, reproductions

LEAN = core.lean_dir()
HAVE_LEAN_SOURCES = LEAN.exists() and any(LEAN.glob("*.lean"))
PAPER = core.repo_root() / "papers" / "sector_thesis.tex"


# ---------------------------------------------------------------- cases vs. the paper -----------

@pytest.mark.skipif(not PAPER.exists(), reason="paper source not present")
def test_cases_consistent_with_paper_table():
    r = core.check_cases_against_paper()
    assert r["ran"] and r["rows_in_paper"] == 16
    assert r["consistent"], r


@pytest.mark.skipif(not PAPER.exists(), reason="paper source not present")
def test_planted_wrong_verdict_is_detected():
    data = copy.deepcopy(core.load_cases())
    potts = next(c for c in data["cases"] if c["id"] == "potts")
    potts["verdict"] = "not_forced"                      # planted defect
    r = core.check_cases_against_paper(data)
    assert not r["consistent"]
    assert [m["case"] for m in r["mismatches"]] == [potts["paper_case"]]


@pytest.mark.skipif(not PAPER.exists(), reason="paper source not present")
def test_planted_missing_case_is_detected():
    data = copy.deepcopy(core.load_cases())
    data["cases"] = [c for c in data["cases"] if c["id"] != "calabi_yau_mirror"]   # planted defect
    r = core.check_cases_against_paper(data)
    assert not r["consistent"] and r["missing_from_server"] == ["Calabi--Yau mirror symmetry"]


def test_verdict_distribution():
    counts = collections.Counter(c["verdict"] for c in core.load_cases()["cases"])
    assert counts == {"forced": 3, "not_forced": 4, "constraint": 2, "organisation": 2,
                      "preferred_equilibrium": 1, "open_question": 1,
                      "excluded_not_a_duality": 1, "excluded_no_self_map": 2}


def test_every_case_is_well_formed():
    data = core.load_cases()
    ids = [c["id"] for c in data["cases"]]
    assert len(ids) == len(set(ids)) == 16
    for c in data["cases"]:
        assert c["verdict"] in data["verdict_vocabulary"]
        assert core.PAPER_VERDICT_TO_KEY[c["paper_verdict"]] == c["verdict"]
        assert c["citations"], c["id"]
        for cit in c["citations"]:
            assert re.match(r"^(doi:10\.\d{4,}/\S+|arXiv:\S+)$", cit["id"]), cit


@pytest.mark.skipif(not HAVE_LEAN_SOURCES, reason="lean/ not present")
def test_referenced_lean_modules_exist():
    for c in core.load_cases()["cases"]:
        for m in c["lean_modules"] + c["related_lean_modules"]:
            assert (LEAN / f"{m}.lean").exists(), (c["id"], m)


def test_get_case_lookup():
    assert core.get_case("potts")["verdict"] == "forced"
    assert core.get_case("Calabi")["verdict"] == "open_question"
    assert core.get_case("zzz-no-such-case") is None


# ---------------------------------------------------------------- Lean parsing ------------------

def test_toplevel_walrus_skips_named_arguments():
    s = "theorem t (N : ℕ) : f (ZMod.dft (N := N) (E := ℂ)) = g := by simp"
    k = core.find_toplevel_walrus(s)
    assert s[k:].startswith(":= by simp")
    naive = s.index(":=")                                # the bug this guards against
    assert naive < k and s[:naive].endswith("(N ")


def test_parse_named_argument_theorem(tmp_path):
    f = tmp_path / "Fixture.lean"
    f.write_text(
        "import Mathlib\n\nnamespace A.B\n\n/-- The doc. -/\n"
        "theorem bij (N : ℕ) [NeZero N] :\n"
        "    Function.Bijective (ZMod.dft (N := N) (E := ℂ) : (ZMod N → ℂ) → (ZMod N → ℂ)) :=\n"
        "  (ZMod.dft (N := N) (E := ℂ)).toEquiv.bijective\n\nend A.B\n")
    [t] = core.parse_lean_file(f)
    assert t.name == "A.B.bij" and t.docstring == "The doc."
    assert t.statement.endswith("(ZMod N → ℂ) → (ZMod N → ℂ))")
    assert "(N := N) (E := ℂ)" in t.statement


def test_sections_do_not_enter_names_and_docstrings_do_not_leak(tmp_path):
    f = tmp_path / "Fixture.lean"
    f.write_text(
        "/-\n  header with the word theorem in it\n-/\nimport Mathlib\nnamespace X\nsection S\n"
        "/-- belongs to the def -/\ndef d : ℕ := 1\n\n"
        "theorem t1 : d = 1 := rfl\nend S\n"
        "private theorem t2 : (1 : ℕ) = 1 := rfl\nend X\ntheorem t3 : True := trivial\n")
    ts = {t.name: t for t in core.parse_lean_file(f)}
    assert set(ts) == {"X.t1", "X.t2", "t3"}
    assert ts["X.t1"].docstring == ""                     # the def's docstring must not attach to t1


@pytest.mark.skipif(not HAVE_LEAN_SOURCES, reason="lean/ not present")
def test_parsed_theorems_match_axiom_audit_exactly():
    parsed = {t.name for t in core.all_theorems()}
    audited = set()
    for p in LEAN.glob("*.lean"):
        audited |= set(re.findall(r"^#print axioms (\S+)", p.read_text(), re.M))
    assert parsed == audited and len(parsed) >= 116


@pytest.mark.skipif(not HAVE_LEAN_SOURCES, reason="lean/ not present")
def test_search_and_get_theorem():
    hits = core.search_theorems("self dual radius")
    assert any(h["name"].endswith("selfDual_radius") for h in hits)
    t = core.get_theorem("QuantumFluids.CompactBoson.bkt_not_selfDual")
    assert t and t["module"] == "CompactBoson" and "2 * Real.sqrt 2" in t["statement"]
    assert core.get_theorem("no_such_theorem_anywhere") is None


# ---------------------------------------------------------------- kernel verification -----------

def test_verify_rejects_bad_module_name():
    r = core.verify_module("../etc/passwd")
    assert r["ran"] is False and "invalid" in r["reason"]


def test_verify_without_toolchain_does_not_pretend(tmp_path, monkeypatch):
    """No lake anywhere (empty PATH, HOME without ~/.elan): ran=False, never a pass."""
    (tmp_path / "Foo.lean").write_text("theorem foo : True := trivial\n")
    empty = tmp_path / "emptybin"
    empty.mkdir()
    monkeypatch.setenv("PATH", str(empty))
    monkeypatch.setenv("HOME", str(tmp_path))
    r = core.verify_module("Foo", ldir=tmp_path)
    assert r["ran"] is False and "toolchain" in r["reason"]
    assert "not certify that the statement is the right physics" in r["caveat"]


def test_verify_without_mathlib_cache_does_not_pretend(tmp_path, monkeypatch):
    """A lake exists but the Mathlib cache does not: ran=False, and lake is never invoked.
    Hermetic: a stub `lake` records any invocation, so the test does not depend on whether the
    machine running it has a real Lean toolchain (CI runners do not)."""
    (tmp_path / "Foo.lean").write_text("theorem foo : True := trivial\n")
    bindir = tmp_path / "bin"
    bindir.mkdir()
    marker = tmp_path / "lake_was_invoked"
    stub = bindir / "lake"
    stub.write_text(f"#!/bin/sh\ntouch {marker}\n")
    stub.chmod(0o755)
    monkeypatch.setenv("PATH", str(bindir))
    r = core.verify_module("Foo", ldir=tmp_path)
    assert r["ran"] is False and "Mathlib build cache" in r["reason"]
    assert not marker.exists(), "lake must not run when the Mathlib cache is missing"
    assert "not certify that the statement is the right physics" in r["caveat"]


@pytest.mark.skipif(os.environ.get("SCT_SLOW") != "1", reason="slow kernel check; set SCT_SLOW=1")
def test_verify_real_module_with_kernel():
    r = core.verify_module("RCFTDuality")
    assert r["ran"] and r["clean"], r
    assert set(r["axioms"]) == {f"QuantumFluids.RCFTDuality.{n}" for n in
                                ("su2Level1_S_sq", "su2Level1_S_symm", "su2Level1_S_det")}


# ---------------------------------------------------------------- reproductions -----------------

@pytest.mark.parametrize("name", sorted(reproductions.REGISTRY))
def test_reproduction_passes_in_subprocess(name):
    r = core.run_reproduction(name)
    assert r["ran"] and r["passed"], r


def test_unknown_reproduction_reports_ran_false():
    r = core.run_reproduction("not_a_reproduction")
    assert r["ran"] is False and "cmb_correlator_zero" in r["available"]


def test_planted_defect_correlator_fails(monkeypatch):
    real = reproductions._single
    monkeypatch.setattr(reproductions, "_single", lambda t, r: 1.01 * real(t, r))   # 1% planted error
    assert reproductions.cmb_correlator_zero()["passed"] is False


def test_planted_defect_potts_fails(monkeypatch):
    monkeypatch.setattr(reproductions, "_rc_dual", lambda p, q: (q * (1 - p) / p) / (2 + q * (1 - p) / p))
    assert reproductions.potts_self_dual()["passed"] is False


def test_planted_defect_levelrank_fails(monkeypatch):
    monkeypatch.setattr(reproductions, "_transpose", lambda lam: tuple(lam))            # identity, not transpose
    assert reproductions.levelrank_box_transpose()["passed"] is False


def test_reproduction_output_is_json_serialisable():
    for name in reproductions.REGISTRY:
        json.dumps(reproductions.run(name), default=str)
