# Ledger

Every claim this repository makes, its status, and where its verification record lives. Statuses are
copied from the origin programme's ledger
([SocrateAI-Scientific-QuantumFluids `LEDGER.md`](https://github.com/xaviercallens/SocrateAI-Scientific-QuantumFluids/blob/master/LEDGER.md)),
where the full evidence for each entry is recorded. Claims made *in this repository* after the move are
recorded below as `SCT-nnn`.

**Rules.** A claim's status only changes with evidence. Retractions are never deleted: the status
becomes RETRACTED with the reason. "Verified" always states its scope — the mathematics, a reading, or
a pre-registered measurement — because a machine-checked proof never certifies the physics prose around
it.

## Inherited claims (origin programme)

### The criterion and its cases

| Origin ID | Status | Claim | Here |
|---|---|---|---|
| CLAIM-045 | VERIFIED (mathematics; the generalisation is a reading, stated as such) | Compact-boson T-duality stated on sectors; `Δ_e·Δ_m = ¼`; BKT (`2√2`) is not the self-dual point (`√2`); the criterion extracted from Ising, string-gas, SIT, QH | `lean/CompactBoson.lean`; DS §2–3 |
| CLAIM-037 | VERIFIED (gate verdicts + group theory) | BKT ≠ self-dual point; the Fricke element is not a Hall symmetry | `lean/QHFricke.lean`, `lean/Fricke.lean` |
| CLAIM-052 | VERIFIED (mathematics; explicitly not the anomaly argument) | ℤ_N sector duality is a bijection whose square is not the identity | `lean/SectorDuality.lean` |
| CLAIM-053 | VERIFIED (mathematics; not the affine-Lie-algebra identification) | RCFT / Verlinde su(2)₁: `S² = 2·𝟙`; self-dual radius on a continuous line → not forced | `lean/RCFTDuality.lean`; DS Add. 2 |
| CLAIM-054 | VERIFIED (finite combinatorics only) | Level-rank duality's Young-diagram box bijection; ν = ½ → constraint, not cause | `lean/LevelRankDuality.lean`; DS Add. 2 |
| CLAIM-047 | VERIFIED (mathematics; cosmological reading stated as a reading) | K3×T² dyon discriminant is SL(2,ℤ)-invariant; flux-lattice and discharge dynamics | `lean/ChargeLattice.lean`; CS |
| CLAIM-055 | VERIFIED (discriminant transfers; class number does not) | The D1-D5-P-KK sequel reuses the discriminant; Strominger–Vafa is out of scope | `lean/ChargeLattice.lean` docstring |
| CLAIM-057 | VERIFIED (Seiberg, prose only) / EXCLUDED (topological superconductors) | Seiberg duality → not forced; the tenfold way is a classification, not a duality | DS Add. 3 |
| CLAIM-059 | VERIFIED (Montonen–Olive, via Mathlib) / EXCLUDED (3D Ising, AdS/CFT) | S-duality → not forced; two structural mismatches | DS Add. 4 |
| CLAIM-060 | RESEARCHED, PARTIAL — question explicitly left open | Calabi–Yau mirror symmetry: T-duality thread extended; no citable self-mirror example | DS Add. 5 |
| CLAIM-062 | VERIFIED (Potts) / DEEPENED (level-rank N = K) | Potts/random-cluster → forced, for every q ≥ 1; level-rank's N = K poses no self-dual question | DS Add. 6 |

### Is the sector a cause?

| Origin ID | Status | Claim | Here |
|---|---|---|---|
| CLAIM-039 | VERIFIED (mathematics) | Winding conserved without a slip; a slip is forced to change it; XY-ring barrier; discrete Stokes; sampled loop sum = degree | `lean/TopologicalProtection.lean`, `ScaleResolvedWinding.lean`, `ContinuumWinding.lean` |
| CLAIM-040 | **VERIFIED IN PART** — composite causal claim **not** made as worded; post-hoc reading stated as such | Energy-matched intervention: topology 15–60× more effective than phonons; **the thermometer clause failed** (vortex arm 5–16% colder) | FP §3; notebook 02 |
| CLAIM-042 | VERIFIED (combinatorics) | Mixed-sector inverse temperature is a mediant, not an average | `lean/SectorTemperature.lean` |
| CLAIM-043 | PROPOSAL + external tests (one PASS, three FAIL as written) | Topological sectors carry their own temperature (Onsager two-temperature picture) | origin programme `sector_temperature` paper |
| CLAIM-038 | VERIFIED IN PART (one amendment wrong, corrected post hoc) | BKT heating ladder; `η·n_s·λ² = 1` to 12–27% | origin programme |

### Cosmology and real data

| Origin ID | Status | Claim | Here |
|---|---|---|---|
| CLAIM-049 | CONFIRMED (3 of 4 pass; B2 fails a threshold, not a direction) | On a torus, density is blind to an imposed sector (1–4%) while injected pairs move it 21–118% | CS; notebook 02 |
| CLAIM-051 | CONFIRMED (on a recalibrated statistic) | B2 recalibrated per injected vortex; agrees across seeds to 8% | origin programme |
| CLAIM-048 | **FAIL / INCONCLUSIVE** (honest negative) | Round-3 finite-size ladder at L = 128: admission failure; the comparison is void, not positive | origin programme |
| CLAIM-058 | VERIFIED (independent reproduction) | Koren–Tsai–Wang's CMB bound reproduced from its equations and Planck 2018 data | notebook 03 |
| CLAIM-061 | VERIFIED, **quantitative basis corrected** (SCT-002) | Exact bubble-time spectrum: worst case within ×3.16; a TT-only successor tightens the bound by at most ~1.4× | notebook 03 |

### Retracted in the origin programme, relevant here

| Origin ID | Status | What was withdrawn |
|---|---|---|
| R2 (CLAIM-024) | **RETRACTED (significance)** | Any claim that the dual length `ℓ(k) = ε²/(ħ²c²k³)` or its floor is a new result: its bound is AM–GM, weaker than Onsager's, and dimensionally forced. `lean/DualLength.lean` is kept only as a prerequisite of `Fricke.lean` (the axis action); the group theory stands, the physics claim does not. |

### Publications

| Origin ID | Status | What |
|---|---|---|
| CLAIM-063 | PUBLISHED | Foundation paper `papers/sector_thesis.pdf` on its own dedicated DOI, concept [10.5281/zenodo.22985863](https://doi.org/10.5281/zenodo.22985863) |
| CLAIM-056 | PUBLISHED | Origin-programme archive v1.14.0 (all companion papers), [10.5281/zenodo.22980872](https://doi.org/10.5281/zenodo.22980872); concept [10.5281/zenodo.22855581](https://doi.org/10.5281/zenodo.22855581) |

## Claims made in this repository

| ID | Status | Date | Claim / event |
|---|---|---|---|
| SCT-001 | VERIFIED (one kernel, this repo) | 2026-09-27 | Theory moved to its dedicated repository. `lean/` extracts the 14 theory-relevant modules unchanged from the origin programme. `lake build` from this repository alone: **succeeded (8792 jobs), 116 audited theorems, 0 `sorry`, 0 errors**; footprints: 105 × `{propext, Classical.choice, Quot.sound}`, 8 × `{propext, Quot.sound}`, 1 × `{propext}` — all within the standard three. `scripts/check_build_log.py` enforces this in the CI workflow (parked in `ci/` until the publishing token has the `workflow` scope — see `ci/README.md`; it joins Lean's wrapped footprint lines; a line-based grep falsely flagged two long names) and fails on four planted defects (a bad axiom inside a wrapped footprint, a `sorry`, a missing theorem, an extra axiom). `regen_axiom_audit.py --check` passes. Comparator challenges regenerate identically apart from the source path in each header. **Not yet done here:** re-running Comparator's second kernel in this repository rather than inheriting the origin programme's record (`docs/VERIFICATION.md`). |
| SCT-002 | **ERRATUM** (conclusion unchanged, quantitative basis corrected) | 2026-09-27 | The foundation paper as archived at 10.5281/zenodo.22985879, and CLAIM-061 in the origin programme, said Planck's TT error bars are "within about 15% of the cosmic-variance floor for ℓ ≈ 5–50." That came from nine sampled multipoles. Building `notebooks/03_cmb_cascade_reproduction.ipynb`, a scan of every multipole (f_sky = 0.7) gave: **1.23–1.95 for 2 ≤ ℓ < 5; 0.96–1.13 for 5 ≤ ℓ < 30; 0.83–1.84 for 30 ≤ ℓ ≤ 50** (the floor there is estimated from the measured, noisy spectrum; 1.03–1.42 against a smoothed one). Re-checked independently from `data/planck2018_tt_full/` before this entry was written. Since the bound on r scales as √σ, the worst ratio still allows at most ~1.4× tightening, so "no meaningful gain from a TT-only successor" stands. Corrected in `papers/sector_thesis.tex` (abstract, §5, with an erratum footnote), `docs/TRAINING_GUIDE.md`, `docs/CASE_TABLE.md`, and in the origin repository. The archived v2 PDF is not silently changed; the correction is carried by the next archived version. |
