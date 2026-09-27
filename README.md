# Sector Causality Theory

**When does self-duality cause physics? A machine-checked criterion, tested across sixteen candidate
physical systems, an interventional experiment, and real cosmological data.**

[![Foundation paper DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22985863.svg)](https://doi.org/10.5281/zenodo.22985863)
[![Lean 4](https://img.shields.io/badge/Lean-4.34.0--rc2-blue)]()
[![Theorems](https://img.shields.io/badge/theorems-116%20kernel--checked-blue)]()
[![License: MIT](https://img.shields.io/badge/code-MIT-yellow.svg)](LICENSE)
[![License: CC BY 4.0](https://img.shields.io/badge/papers-CC%20BY%204.0-lightgrey.svg)](NOTICE)

## The theory, in one paragraph

Physics is full of self-dual points: places where a symmetry exchanges two descriptions of the same
system and maps it to itself. Some are physically decisive — the Kramers–Wannier point fixes the Ising
critical temperature exactly. Some are not — the free boson's self-dual radius is an ordinary point on
a line of conformal field theories, not a phase boundary. This project states, proves in Lean 4 against
Mathlib with two independent kernels, and tests experimentally, a single criterion that predicts which
is which: **a self-dual point is forced to be physically distinguished if and only if it exchanges two
inequivalent sectors on a discrete fixed-point set**; on a continuous moduli space with enhanced
symmetry, or when self-duality only constrains a fixed point without producing one, it is not. The
duality is always exact; what does causal work, when anything does, is the **sector** it relabels — a
conserved or topological label crossing a threshold, proliferating, annihilating, or being imposed.

This repository is the theory's dedicated home: everything needed to read, check, reproduce, extend,
or contest it lives here, self-contained. It grew out of a broader quantum-fluids research programme
(SocrateAI-Scientific-QuantumFluids) but has outgrown that origin — this is where the theory itself now
lives.

## Start here

| If you want to... | Go to |
|---|---|
| Read the theory in full, as a standalone paper | [`papers/sector_thesis.pdf`](papers/sector_thesis.pdf) — the foundation paper, on its own dedicated DOI |
| Get a guided, no-prerequisites walkthrough | [`docs/TRAINING_GUIDE.md`](docs/TRAINING_GUIDE.md) |
| See every case examined, with its verdict and evidence | [`docs/CASE_TABLE.md`](docs/CASE_TABLE.md) |
| Check the machine-checked mathematics yourself | [`lean/`](lean/) and [`docs/VERIFICATION.md`](docs/VERIFICATION.md) — `cd lean && lake exe cache get && lake build` |
| Reproduce a numerical result | [`notebooks/`](notebooks/) — runnable Jupyter notebooks |
| See the full technical report (six dated addenda) | [`papers/duality_sector.pdf`](papers/duality_sector.pdf) |
| See the cosmological extension | [`papers/cosmology_sectors.pdf`](papers/cosmology_sectors.pdf) |
| Query the theory programmatically (including as an AI agent) | [`mcp-server/`](mcp-server/) |
| See what would falsify the theory, and where it goes next | [`docs/ROADMAP.md`](docs/ROADMAP.md) — falsifiers, research tracks, communication plan, open tasks |
| Contribute, discuss, or contest a claim | [`CONTRIBUTING.md`](CONTRIBUTING.md) |

## What is here, and why it is self-contained

- **`papers/`** — the three core papers (LaTeX source, compiled PDF, and bibliography) of the theory.
  The foundation paper has its own dedicated Zenodo DOI, independent of any software archive, so the
  *theory* is directly citable as a publication in its own right.
- **`lean/`** — the machine-checked mathematical skeleton: fourteen Lean 4 modules, pinned to the exact
  Mathlib revision the papers cite, with no dependency on the QuantumFluids repository this project
  grew out of. `cd lean && lake exe cache get && lake build` reproduces every kernel check from a
  clean clone (the committed `lake-manifest.json` pins every dependency).
- **`notebooks/`** — Jupyter notebooks that reproduce the theory's key numerical claims from first
  principles: the compact-boson sector-sum computation, the energy-matched interventional experiment,
  and the independent CMB-bound reproduction against real Planck data.
- **`data/`** — the real external dataset used (Planck 2018 TT power spectrum) and the key result files
  the notebooks and papers cite, so nothing here depends on re-downloading anything to inspect.
- **`docs/`** — a training guide for newcomers, the full sixteen-case table with links to evidence, and
  the collaboration model for scientists and AI agents.
- **`mcp-server/`** — a Model Context Protocol server exposing the theory's case table, theorem
  statements, and reproduction scripts as tools an AI agent can call directly, for collaborative
  verification and extension work.

## What this theory does not claim

No novelty is claimed in the underlying mathematics of any single duality cited — Kramers–Wannier,
T-duality, Seiberg duality, Montonen–Olive duality, and every other duality discussed are cited, not
reinvented. What is new is the criterion stated precisely enough to be checked by a kernel and tested
by an experiment, and an honest record of where it does, and does not, resolve: of sixteen candidate
cases examined, twelve receive a definite verdict, three are found not to be instances of the criterion
at all, and one — Calabi–Yau mirror symmetry — is left an explicit open question because the literature
does not settle it. See [`papers/sector_thesis.pdf`](papers/sector_thesis.pdf)'s own "what this does
not claim" sections, and `RETRACTIONS.md`-style honesty throughout `docs/CASE_TABLE.md`, for the full
account.

## Related repositories

- **[SocrateAI-Scientific-QuantumFluids](https://github.com/xaviercallens/SocrateAI-Scientific-QuantumFluids)**
  — the origin programme: the full Lean library (257 theorems, 30 modules, including modules outside
  the sector-causality theory proper), the interventional experiment's pre-registrations and raw
  results, and every companion paper.
- **[rusty-SUNDIALS](https://github.com/xaviercallens/rusty-SUNDIALS)** — the pure-Rust numerical
  solvers used for the theory's reproductions (`qf-pgpe`, `qf-cmb-cascade`), with its own MCP server
  for co-deployment with this repository's server (see `mcp-server/README.md`).
- **[SocrateAI-Scientific-Agora-LeanMaster](https://github.com/xaviercallens/SocrateAI-Scientific-Agora-LeanMaster)**
  — a sibling Lean formalization programme (Double Field Theory, Mathieu moonshine, dual-scale string
  cosmology) whose Lean Blueprint and dependency-graph tooling this repository's documentation points
  to as a model; see `docs/TRAINING_GUIDE.md` for how the two programmes relate and differ.

## Citing

The theory: **[10.5281/zenodo.22985863](https://doi.org/10.5281/zenodo.22985863)** (concept DOI,
resolves to the latest version). See `CITATION.cff`.

## Licence

Code (Lean, notebooks, the MCP server): **MIT**. Papers and documentation: **CC BY 4.0**. See `NOTICE`.
