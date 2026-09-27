# Contributing: discussion, proof, and collaboration

This repository is built to be argued with. Scientists and AI agents are both invited to check,
extend, and contest the theory. What makes a contribution welcome is not whether it agrees with the
theory but whether it meets the evidence standard below — a well-sourced argument that a verdict is
*wrong* is worth more than an unsourced one that it is right.

## Ways to take part

| You want to... | Do this | Label |
|---|---|---|
| Ask a question or discuss an idea | Open a GitHub Discussion (or an issue if Discussions is off) | `question` |
| Propose a new case for the table | Issue using the *case proposal* template | `case-proposal` |
| Argue that an existing verdict is wrong | Issue using the *challenge a verdict* template | `challenge` |
| Formalise something in Lean | Issue first, then a PR | `formalization` |
| Reproduce, or fail to reproduce, a numerical result | Issue with your environment and outputs | `reproduction` |
| Report an error in a paper, citation, or number | Issue — errors are fixed and recorded, never silently | `erratum` |

## The evidence standard (applies to everyone, human or agent)

1. **Literature gate.** Every citation must be verified — DOI against Crossref, or arXiv ID against
   the source — *before* it is written down. Say which you did. A citation you have not verified is
   not a citation.
2. **Check dependencies, not analogy.** A shared mathematical structure between two systems licenses
   no claim about their physics unless a real dependency connects them. This is the theory's own
   thesis, applied to itself.
3. **Classify honestly.** A candidate case returns one of the four verdicts, or "the literature does
   not settle this," or "not an instance" (no duality / no self-map). Do not force a case into the
   taxonomy by analogy with earlier cases. See `docs/TRAINING_GUIDE.md`, Module 8.
4. **Pre-register new experiments.** State the prediction and the pass/fail criterion *before*
   running. Report failed criteria as failed; do not reinterpret them after the fact. (The foundation
   paper reports its own failed thermometer clause — that is the standard.)
5. **Report negative results with the same weight as positive ones.** An exclusion, a
   non-reproduction, or a retraction is a contribution, not a defect.
6. **Numbers must be computed or read from a real file**, never typed in as if computed. State which.

## Contributing Lean

- Build against the pinned Mathlib (`lean/lakefile.lean`); do not bump the pin in a content PR.
- **Footprint:** only `propext`, `Classical.choice`, `Quot.sound`. No `sorry`, no `admit`, no new axioms.
- Run `python3 scripts/regen_axiom_audit.py` so every theorem gets its generated `#print axioms` line;
  run it with `--check` before opening a PR; CI (`.github/workflows/ci.yml`) runs it too.
- **Negative controls:** include at least one deliberately false variant that fails (describe it in
  the PR; do not commit it as a theorem).
- **Docstring must state what is *not* proved.** The kernel certifies the proof, never the statement;
  the reader must be able to see where the Lean stops and the physics prose begins.
- **Search Mathlib first.** If Mathlib already proves it (as with `ModularGroup.stabilizer_I` for
  Montonen–Olive), cite it; do not re-prove it. If nothing checkable exists beyond what is already
  proved, integrate the case as prose — no token theorems.
- Run Comparator on your module if you can (`docs/VERIFICATION.md`); say whether you did.

## Contributing numerics or notebooks

- Notebooks must execute top to bottom from a fresh clone (`notebooks/README.md`).
- State which results are recomputed live and which are replotted from archived files.
- New data: record source, licence, retrieval date, and an authenticity check (e.g. a known landmark).
- Long computations may be opt-in cells, but the default path must run and must not fake their output.

## For AI agents

AI agents are first-class collaborators here, under the same evidence standard plus four rules:

1. **Declare yourself.** An agent-authored issue, comment, or PR says so in its first line, with the
   agent/model name and whether a human reviewed it before posting.
2. **Show the evidence trail.** Include the tool calls or commands you ran and their outputs (the MCP
   server in `mcp-server/` returns structured, citable results for exactly this purpose).
3. **`ran: false` is not a pass.** If a check did not run (missing toolchain, timeout, network), say so;
   never report an unrun check as passing. The MCP server marks this explicitly on every result.
4. **Never fabricate a citation, a theorem name, or a number.** If you cannot verify it, say you could
   not. An agent that says "I could not verify this DOI" is doing its job; one that invents a plausible
   DOI is not.

The MCP server (`mcp-server/`) lets an agent look up a case, fetch its theorem statements, re-run the
kernel check, and re-run a numerical landmark — see `mcp-server/CO_DEPLOYMENT.md` for using it
alongside the rusty-SUNDIALS numerical server and the Agora-LeanMaster Lean tooling in one environment.

## Review

Every PR is reviewed for the evidence standard first and the conclusion second. A PR that changes a
verdict in `docs/CASE_TABLE.md` must update the papers' corresponding text or open an erratum for it,
so the table, the papers, and the MCP server's case data never disagree.

## Conduct

Argue with claims, not people. Be specific. Assume good faith, and earn it by showing your sources.

## Licence of contributions

Code contributions are accepted under MIT; paper and documentation contributions under CC BY 4.0
(see `NOTICE`). By contributing you confirm you have the right to license your contribution this way.
