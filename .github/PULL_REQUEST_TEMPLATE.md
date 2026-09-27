**Agent-authored?** (yes — name/model, human-reviewed? / no)

## What this changes

## Evidence standard checklist
- [ ] Every new citation verified (say how: Crossref / source)
- [ ] Lean: standard axioms only, no `sorry`; `python3 scripts/regen_axiom_audit.py --check` passes
- [ ] Lean: a negative control fails (describe it)
- [ ] Lean: docstring states what is *not* proved
- [ ] Numerics: notebook executes top to bottom; live vs replotted results stated
- [ ] If a verdict changes: `docs/CASE_TABLE.md`, the papers, and `mcp-server` case data all agree
- [ ] Any check that did not run is listed as not run
