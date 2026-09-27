# CI

The workflow is `.github/workflows/ci.yml`. (It was briefly parked in this directory because the token
first used to publish the repository lacked GitHub's `workflow` scope.)

| Job | What it checks |
|---|---|
| `lean` | `lake exe cache get && lake build`, then `scripts/check_build_log.py --expect 116`: standard axioms only, no `sorry`, all 116 theorems audited (Lean's wrapped footprint lines handled) |
| `mcp-server` | `pytest` for the MCP server: the case table matches the paper; planted-defect controls fail as they must |
| `notebooks` | all three reproduction notebooks execute top to bottom (outputs to a scratch dir, not committed) |
| `audit` | `scripts/regen_axiom_audit.py --check` and `scripts/make_references.py --check` |

Each job was exercised locally before the workflow was committed; see `LEDGER.md` (SCT-001) for the
results of the first run on GitHub.
