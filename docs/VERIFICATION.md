# Verifying the Lean formalization

Everything in `lean/` is checkable from a clean clone of this repository alone. This page says how,
and — as important — what a successful check does and does not certify.

## Build (one kernel)

```bash
cd lean
lake exe cache get     # fetches Mathlib at the pinned commit and its prebuilt .olean files
lake build             # builds all 14 modules; prints every `#print axioms` line
```

`lean/lake-manifest.json` is committed and pins Mathlib (tag v4.34.0-rc2, commit `85e3a25`) and every
transitive dependency, so no `lake update` is needed — running one would re-resolve and could drift.

Toolchain: `lean4:v4.34.0-rc2` (`lean/lean-toolchain`; [elan](https://github.com/leanprover/elan)
installs it automatically). The library has **116 theorems across 14 modules**.

A successful build prints, for every theorem, a line such as

```
'QuantumFluids.CompactBoson.bkt_not_selfDual' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The permitted footprint is exactly `{propext, Classical.choice, Quot.sound}` (some theorems use fewer).
**Any other axiom, or any `sorry`, is a failure.** (Namespaces still read `QuantumFluids.*` — the
modules were extracted unchanged from the origin programme so that statements and footprints match its
published record exactly; renaming them would have changed every theorem's identity.)

## Keep the audit honest

```bash
python3 scripts/regen_axiom_audit.py --check   # exits non-zero if any theorem lacks its audit line
```

The audit blocks at the bottom of each `.lean` file are *generated*, never hand-written: a hand-kept list
drifted once in the origin programme (12 theorems had never been audited), and a generator does not.

## Second kernel (Comparator + nanoda)

A single kernel accepting a proof rests on one implementation of type theory. Comparator exports each
module's proof terms and re-checks them with an independent kernel (nanoda), and confirms the exported
closure is exactly the listed theorems and their dependencies.

```bash
python3 scripts/make_comparator_challenges.py            # regenerates lean/ComparatorChallenges/*
cd lean
lake env comparator ComparatorChallenges/CompactBoson.json   # repeat per module
```

Comparator, `lean4export`, `nanoda_bin` and `landrun` must be on `PATH`; install instructions are in the
[Comparator repository](https://github.com/leanprover/comparator). The challenge files are *generated*
from the solutions, so "same statement" holds by construction; the independent content of a pass is
that two kernels accept the proofs, with only the permitted axioms, over exactly the stated closure. Run
it without network or privileges (the origin programme used
`systemd-run --user --property=RestrictAddressFamilies=~AF_UNIX`).

Status: **all 14 modules accepted by both kernels, re-run in this repository** on 2026-09-27 (`LEDGER.md`,
SCT-005), matching the origin programme's record; negative controls fail as they must. Re-running
Comparator yourself is how you confirm it rather than trusting either record.

## Negative controls

For each module, deliberately false variants must *fail* — a check that cannot fail certifies nothing.
Examples recorded in the origin programme: `RCFTDuality` — claiming `S² = 𝟙` (instead of `2·𝟙`) or
`det S = 1` fails; `LevelRankDuality` — the box statement with `a, b` left unswapped fails to
typecheck; `CompactBoson` — "BKT at the self-dual radius" fails; `SectorDuality` — "duality squared is
the identity at N = 3" fails. Adding a negative control for your own contribution is expected (see
`../CONTRIBUTING.md`).

## What a pass certifies, and what it does not

> **A clean footprint certifies the proof, never the statement.**

Every module's docstring states what it does *not* prove. The kernel checks that the stated theorem
follows from the definitions; it cannot check that the stated theorem is the right physics:

| Module | What is proved | What is *not* proved (supplied as prose, from the literature) |
|---|---|---|
| `RCFTDuality` | a 2×2 integer matrix squares to `2·𝟙` | that this matrix is su(2)₁'s Kac–Peterson S-matrix |
| `LevelRankDuality` | the Young-diagram box-transpose bijection | S,T-matrix / Verlinde-formula preservation |
| `SectorDuality` | ℤ_N Fourier duality is a bijection; its square is not the identity | the anomaly argument for which fixed points are forced |
| `ChargeLattice` | the discriminant's SL(2,ℤ)-invariance | that a real black hole's entropy is this function |
| `CompactBoson` | the dimensions and radii; `2√2 ≠ √2` | that a superfluid *is* a compact boson (the dictionary is physics input) |
| `DualLength` | its algebra and floor | any physical significance — **retracted** in the origin programme (AM–GM, weaker than Onsager's bound, dimensionally forced) |

Whether each statement is the right one remains a human — or agent — audit. That audit is exactly
what `CONTRIBUTING.md` invites.
