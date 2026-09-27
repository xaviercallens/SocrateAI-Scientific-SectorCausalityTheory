#!/usr/bin/env python3
"""Check a `lake build` log: every audited theorem uses only the standard axioms, no `sorry`, no errors.

Lean wraps long `#print axioms` output across lines, e.g.

    info: X.lean:261:0: 'Ns.long_name' depends on axioms: [propext,
     Classical.choice,
     Quot.sound]

so a line-based grep gives false positives. This joins each footprint up to its closing `]` first.

    python3 scripts/check_build_log.py lean/build.log [--expect 116]
Exits non-zero, naming the offender, on any failure.
"""
from __future__ import annotations

import re
import sys

ALLOWED = {"propext", "Classical.choice", "Quot.sound"}
HEAD = re.compile(r"'([^']+)' depends on axioms: \[")
NONE = re.compile(r"'([^']+)' does not depend on any axioms")


def footprints(text: str) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for m in HEAD.finditer(text):
        end = text.index("]", m.end())
        out[m.group(1)] = {a.strip() for a in text[m.end():end].split(",") if a.strip()}
    for m in NONE.finditer(text):
        out[m.group(1)] = set()
    return out


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    text = open(args[0]).read()
    expect = int(args[args.index("--expect") + 1]) if "--expect" in args else None
    problems = []
    if re.search(r"declaration uses 'sorry'", text):
        problems.append("a declaration uses 'sorry'")
    if re.search(r"^error", text, re.M):
        problems.append("the build reported an error")
    fp = footprints(text)
    for name, axioms in sorted(fp.items()):
        bad = axioms - ALLOWED
        if bad:
            problems.append(f"{name} depends on non-standard axioms {sorted(bad)}")
    if expect is not None and len(fp) < expect:
        problems.append(f"only {len(fp)} audited theorems in the log, expected at least {expect}")
    print(f"{len(fp)} audited theorems; footprints within {sorted(ALLOWED)}" if not problems else "")
    if problems:
        sys.exit("FAIL:\n  " + "\n  ".join(problems))


if __name__ == "__main__":
    main()
