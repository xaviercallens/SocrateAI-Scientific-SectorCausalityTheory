# Co-deploying the theory tools in one environment

Three repositories, one agent session. Two of them expose MCP servers; the third provides Lean tooling
used directly from the shell.

| Component | Repository | Interface | What it gives an agent |
|---|---|---|---|
| `sector-causality` | this repository, `mcp-server/` | MCP (Python, stdio) | cases, criterion, Lean theorems, kernel checks, papers, landmark reproductions |
| `sundials` | [rusty-SUNDIALS](https://github.com/xaviercallens/rusty-SUNDIALS), `crates/sundials-mcp` ([PR #58](https://github.com/xaviercallens/rusty-SUNDIALS/pull/58), merged) | MCP (Rust, stdio) | CVODE named problems with known-answer checks; the `qf-pgpe` Gross–Pitaevskii solver; the `qf-cmb-cascade` CMB bound; BAO distances |
| LeanMaster tooling | [SocrateAI-Scientific-Agora-LeanMaster](https://github.com/xaviercallens/SocrateAI-Scientific-Agora-LeanMaster) | shell / browser (**no MCP server**) | a Lean Blueprint (`blueprint/`) and the LeanGraph dependency explorer (`leangraph/`, `graph/index.html`) |

Status of each piece, stated plainly: both MCP servers are built and tested, and the official Python MCP
client has been tested against both (`tests/test_stdio_e2e.py`, `tests/test_interop_rusty_sundials.py`).
`sundials-mcp` is merged into rusty-SUNDIALS `main` (PR #58, with `crates/qf-cmb-cascade` from PR #57 and
`crates/qf-bao-distances` from PR #61). Its tools are `about`, `list_problems`, `solve`, `pgpe_run`,
`cmb_bound` and `bao_distances`. The CMB landmark is available two ways: `sector-causality`'s
`reproduce("cmb_correlator_zero")` (Python) and `sundials`'s `cmb_bound` (Rust: the Koren–Tsai–Wang
2σ bound against the real Planck 2018 TT data, 10–30 s per call under a 120 s worker timeout). Agora-LeanMaster has no MCP server and none is
provided here.

## 1. Build and register both servers

```bash
# the theory server
cd SocrateAI-Scientific-SectorCausalityTheory/mcp-server
python3 -m venv .venv && . .venv/bin/activate && pip install -e .
( cd ../lean && lake exe cache get )          # optional: enables verify_theorem

# the solver server (on rusty-SUNDIALS main)
cd ../../rusty-SUNDIALS && git checkout main && git pull
cargo build --release -p sundials-mcp

# register (Claude Code; other MCP clients: see mcp-config.example.json)
claude mcp add sector-causality -- /path/to/SocrateAI-Scientific-SectorCausalityTheory/mcp-server/.venv/bin/sector-causality-mcp
claude mcp add sundials -- /path/to/rusty-SUNDIALS/target/release/sundials-mcp
```

`mcp-config.example.json` is the same pair in the `mcpServers` format most clients read. Nothing in either
repository writes to your client configuration; registration is always your own step.

Both servers are stdio processes with no network listener and no shared state, so running them side by
side needs nothing beyond both being registered. Each keeps its protocol stream clean independently:
`sector-causality` runs reproductions and Lean in subprocesses; `sundials-mcp` runs every solver in a worker
subprocess whose stdout is routed to stderr (rusty-SUNDIALS' CVODE prints diagnostics to stdout on some
failure paths).

## 2. Using the Agora-LeanMaster tooling alongside

Agora-LeanMaster is a separate Lean formalization programme (Double Field Theory, Mathieu moonshine,
dual-scale string cosmology) on the same Lean toolchain (v4.34.0-rc2). Its tooling is used from the shell:

```bash
cd SocrateAI-Scientific-Agora-LeanMaster
python3 tools/build_blueprint.py        # then open blueprint/web/index.html
python3 -m leangraph.cli --check-dag --out graph/    # then open graph/index.html
```

LeanGraph's CLI takes `--root <lean project>` and `--target <modules…>`, so in principle it can be pointed
at this repository's `lean/` (targets such as `CompactBoson SectorDuality RCFTDuality LevelRankDuality`) to
draw the sector-causality dependency graph. **That has not been tried here**; treat it as a suggestion to
verify, not a supported path. Keep the two programmes' claims separate: a verdict in this theory's case
table does not depend on anything in Agora-LeanMaster, and vice versa.

## 3. Worked session: checking one case end to end

The goal is to check the Montonen–Olive case, then a case with a numerical landmark, the way a sceptical
reader would — reading the claim, the proof, the kernel's verdict and a number.

1. `sector-causality.criterion()` — read the criterion being applied.
2. `sector-causality.check_consistency()` — confirm the server's case table matches the paper's Table 1
   (`consistent: true`). If it does not, stop: the server is serving something the paper does not say.
3. `sector-causality.get_case("montonen")` — verdict `not_forced`; no project Lean file; `mathlib_lemmas`
   names `ModularGroup.S_mul_S_eq`, `ModularGroup.stabilizer_I`, `ModularGroup.stabilizer_ρ` (Mathlib's own
   proofs that τ = i and τ = ρ have enhanced stabilisers); the caveat about global forms at τ = i.
4. `sector-causality.get_case("compact_boson")` — verdict `not_forced`, Lean module `CompactBoson`.
5. `sector-causality.get_theorem("QuantumFluids.CompactBoson.bkt_not_selfDual")` — the exact statement.
6. `sector-causality.verify_theorem("CompactBoson")` — the kernel's verdict and axiom footprint. If it
   returns `ran: false`, the reason says what is missing (usually the Mathlib cache); that is not a pass.
7. `sector-causality.reproduce("compact_boson_tduality")` — the proved statements on concrete numbers.
8. `sundials.pgpe_run({"initial": "plane_wave", "n": 32, "t_end": 1.0})` — the Gross–Pitaevskii solver
   behind the interventional experiment, checked against an exact solution; then
   `sundials.solve({"problem": "robertson"})` for a stiff ODE with an LLNL reference value.

What a clean run establishes, and what it does not: the table matches the paper, the Lean statement checks
with standard axioms, and the landmark numbers match their references. Whether the statement is the right
physics — whether the Lean `bkt_not_selfDual` says what the case table claims about BKT — is the part no
tool certifies; read the statement against the paper yourself.
