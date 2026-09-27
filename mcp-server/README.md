# sector-causality-mcp

A [Model Context Protocol](https://modelcontextprotocol.io) server (stdio, official Python `mcp` SDK ≥ 2.0)
that lets scientists and AI agents query, check and reproduce the Sector Causality Theory directly: the
case table, the criterion, the Lean theorems, kernel verification, the papers, and fast landmark
reproductions.

## Tools

| Tool | Returns |
|---|---|
| `criterion()` | the criterion, verbatim from `papers/sector_thesis.tex` |
| `list_cases()` | the sixteen candidate cases: id, verdict, one-line reason, plus the verdict vocabulary |
| `get_case(name)` | one case in full: the paper's own verdict wording, citations (DOI/arXiv), Lean modules, caveats |
| `check_consistency()` | re-derives every verdict from the paper's Table 1 and reports any mismatch with what the server serves |
| `search_theorems(query)` | Lean theorems in `lean/` matching all keywords (name, module, docstring, statement) |
| `get_theorem(name)` | a theorem's full statement (up to the top-level `:=`), module, line and docstring |
| `verify_theorem(module)` | runs `lake env lean <module>.lean`: errors, `sorry` warnings, `#print axioms` footprint |
| `list_papers()` | the papers with titles, roles and DOIs |
| `list_reproductions()` / `reproduce(name)` | bounded (seconds) landmark checks run in a subprocess |

Reproductions available: `cmb_correlator_zero` (the exact bubble-time correlator at r→0 equals π²/6),
`compact_boson_tduality` (sector sum invariant under R → 2/R; Δₑ·Δₘ = 1/4; √2 vs 2√2),
`rcft_su2_level1` (S² = 2·1, symmetric, det −2), `potts_self_dual` (the random-cluster self-dual point is
a fixed point of the duality; q = 2 reproduces the Kramers–Wannier Ising point),
`levelrank_box_transpose` (transpose maps the a×b box bijectively onto the b×a box). Standard library only.

## Honesty conventions

- **`ran`** on every check: `ran: false` means it did not execute (toolchain missing, Mathlib cache not
  built, timeout, unknown name) and says why. It is never a pass.
- **A clean axiom footprint certifies a proof, not that the statement is the right physics.** Every
  `verify_theorem` result carries that caveat.
- **Verdicts are transcriptions of the paper, and checkable as such.** `check_consistency` parses the
  paper's own Table 1, so a transcription error in `cases.json` is detectable rather than silently served.
- **Reproductions compare against independently fixed values** (a closed form, a published number), not
  against numbers this code produced earlier; where a reproduction only illustrates a theorem already
  proved in Lean, it says so.
- Theorem statements are cut at the first **top-level** `:=`, so a named argument such as
  `ZMod.dft (N := N)` inside a signature does not truncate it (a bug this project's own Comparator
  challenge generator once had).

## Install and run

```bash
cd mcp-server
python3 -m venv .venv && . .venv/bin/activate      # or: uv venv && uv pip install -e ".[test]"
pip install -e ".[test]"
sector-causality-mcp                                # speaks MCP on stdin/stdout
```

Register with Claude Code (run this yourself; nothing here edits your settings):

```bash
claude mcp add sector-causality -- /path/to/SocrateAI-Scientific-SectorCausalityTheory/mcp-server/.venv/bin/sector-causality-mcp
```

With an editable install (`pip install -e`) the server finds the repository from its own location; a
regular (non-editable) install cannot, so set `SCT_REPO_ROOT` (as `mcp-config.example.json` does).
Override with `SCT_REPO_ROOT` (repository root) or
`SCT_LEAN_DIR` (a Lean project directory, e.g. to verify against another checkout). `verify_theorem` needs
the Lean toolchain (`elan`/`lake`) and a built Mathlib cache in `lean/` (`cd lean && lake exe cache get`);
without them it returns `ran: false` with the reason.

## Tests

```bash
pytest                          # 25 tests + 1 opt-in slow kernel test
SCT_SLOW=1 pytest -k verify_real_module          # real kernel check of RCFTDuality (~1 min)
SUNDIALS_MCP_BIN=/path/to/rusty-SUNDIALS/target/release/sundials-mcp pytest -k interop
```

Every "it works" test is paired with a planted-defect control that must fail: a wrong verdict and a
missing case are caught by `check_consistency`; a 1% error planted in the correlator, a wrong duality map,
and an identity in place of the transpose each make their reproduction fail; a theorem file with a named
argument `:=` must parse to the full statement; a module without a Mathlib cache must report `ran: false`.
`tests/test_stdio_e2e.py` drives the real server through the official MCP client over stdio.

As of 2026-09-27: 26 passed, 1 skipped (the slow kernel test, which passes when enabled — `RCFTDuality`
checks clean with `{propext, Classical.choice, Quot.sound}`), including the interop test against
rusty-SUNDIALS' `sundials-mcp`.

## Co-deployment

See [`CO_DEPLOYMENT.md`](CO_DEPLOYMENT.md) for running this server together with rusty-SUNDIALS'
`sundials-mcp` and alongside the Agora-LeanMaster Lean tooling, and
[`mcp-config.example.json`](mcp-config.example.json) for a two-server client configuration.

Licence: MIT.
