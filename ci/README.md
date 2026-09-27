# CI workflow — written, tested locally, not yet active

`github-workflows-ci.yml` is this repository's GitHub Actions workflow. It is parked here, rather than
in `.github/workflows/`, because the token used to publish the repository lacked the `workflow`
scope that GitHub requires to create workflow files. **Until it is moved, no CI runs.**

To activate it (owner, once):

```bash
gh auth refresh -h github.com -s workflow      # grants the workflow scope (interactive)
mkdir -p .github/workflows
git mv ci/github-workflows-ci.yml .github/workflows/ci.yml
git commit -m "Activate CI" && git push
```

What it runs, each step already exercised locally before publication:

| Job | What it checks | Local evidence |
|---|---|---|
| `lean` | `lake exe cache get && lake build`, then `scripts/check_build_log.py --expect 116`: standard axioms only, no `sorry`, all 116 theorems audited (wrapped footprint lines handled) | build succeeded (8792 jobs), 116 audited, 0 `sorry`; the checker fails on four planted defects |
| `mcp-server` | `pytest` for the MCP server (case table matches the paper; planted-defect controls) | 25 passed, 2 opt-in skips (27/27 with `SCT_SLOW=1` and a rusty-SUNDIALS binary) |
| `notebooks` | all three notebooks execute top to bottom | each re-executed independently with 0 errors |
| `audit` | `regen_axiom_audit.py --check`, `make_references.py --check` | both pass |
