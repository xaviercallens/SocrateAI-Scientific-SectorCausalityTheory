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
| CLAIM-065 | CONFIRMED (admission failure was an equilibration artefact) / **FAIL, robust** (C1) / not bracketed (C2) | The L = 128 rerun with doubled equilibration: admission 2/6 → 5/6 (previously admitted runs unchanged); the finite-size offset η·K − 1 still **grows** with L at every energy (ratio 2.50), now shown not to be a selection artefact; magnitude uncertain, interpretation open; one run still unphysical (not a trapped winding sector) | origin programme, `PGPE_R3_RESULTS.md` Part C2 |
| CLAIM-058 | VERIFIED (independent reproduction) | Koren–Tsai–Wang's CMB bound reproduced from its equations and Planck 2018 data | notebook 03 |
| CLAIM-061 | VERIFIED, **quantitative basis corrected** (SCT-002) | Exact bubble-time spectrum: worst case within ×3.16; a TT-only successor tightens the bound by at most ~1.4× | notebook 03 |

### Retracted in the origin programme, relevant here

| Origin ID | Status | What was withdrawn |
|---|---|---|
| R2 (CLAIM-024) | **RETRACTED (significance)** | Any claim that the dual length `ℓ(k) = ε²/(ħ²c²k³)` or its floor is a new result: its bound is AM–GM, weaker than Onsager's, and dimensionally forced. `lean/DualLength.lean` is kept only as a prerequisite of `Fricke.lean` (the axis action); the group theory stands, the physics claim does not. |

### Publications

| Origin ID | Status | What |
|---|---|---|
| CLAIM-063 | PUBLISHED | Foundation paper `papers/sector_thesis.pdf` on its own dedicated DOI, concept [10.5281/zenodo.22985863](https://doi.org/10.5281/zenodo.22985863); v3 archived from this repository (SCT-006) |
| CLAIM-056 | PUBLISHED | Origin-programme archive v1.14.0 (all companion papers), [10.5281/zenodo.22980872](https://doi.org/10.5281/zenodo.22980872); concept [10.5281/zenodo.22855581](https://doi.org/10.5281/zenodo.22855581) |

## Claims made in this repository

| ID | Status | Date | Claim / event |
|---|---|---|---|
| SCT-001 | VERIFIED (one kernel, this repo) | 2026-09-27 | Theory moved to its dedicated repository. `lean/` extracts the 14 theory-relevant modules unchanged from the origin programme. `lake build` from this repository alone: **succeeded (8792 jobs), 116 audited theorems, 0 `sorry`, 0 errors**; footprints: 105 × `{propext, Classical.choice, Quot.sound}`, 8 × `{propext, Quot.sound}`, 1 × `{propext}` — all within the standard three. `scripts/check_build_log.py` enforces this in CI (`.github/workflows/ci.yml`; it joins Lean's wrapped footprint lines; a line-based grep falsely flagged two long names) and fails on four planted defects (a bad axiom inside a wrapped footprint, a `sorry`, a missing theorem, an extra axiom). `regen_axiom_audit.py --check` passes. Comparator challenges regenerate identically apart from the source path in each header. Comparator's second kernel was then re-run here: see SCT-005. |
| SCT-002 | **ERRATUM** (conclusion unchanged, quantitative basis corrected) | 2026-09-27 | The foundation paper as archived at 10.5281/zenodo.22985879, and CLAIM-061 in the origin programme, said Planck's TT error bars are "within about 15% of the cosmic-variance floor for ℓ ≈ 5–50." That came from nine sampled multipoles. Building `notebooks/03_cmb_cascade_reproduction.ipynb`, a scan of every multipole (f_sky = 0.7) gave: **1.23–1.95 for 2 ≤ ℓ < 5; 0.96–1.13 for 5 ≤ ℓ < 30; 0.83–1.84 for 30 ≤ ℓ ≤ 50** (the floor there is estimated from the measured, noisy spectrum; 1.03–1.42 against a smoothed one). Re-checked independently from `data/planck2018_tt_full/` before this entry was written. Since the bound on r scales as √σ, the worst ratio still allows at most ~1.4× tightening, so "no meaningful gain from a TT-only successor" stands. Corrected in `papers/sector_thesis.tex` (abstract, §5, with an erratum footnote), `docs/TRAINING_GUIDE.md`, `docs/CASE_TABLE.md`, and in the origin repository. The archived v2 PDF is not silently changed; the correction is carried by v3 (SCT-006). |
| SCT-003 | DONE | 2026-09-27 | **CI active and green on GitHub.** First run (commit 787afe5): Lean build on GitHub's runner succeeded (8792 jobs) and `check_build_log.py` reported *116 audited theorems; footprints within [Classical.choice, Quot.sound, propext]* — an independent machine confirming SCT-001; notebooks and audit jobs passed; the MCP-server job **failed** on a real test bug (`test_verify_without_mathlib_cache_does_not_pretend` assumed a Lean toolchain was installed; on a runner without one the server correctly returned `ran: false`, for the other reason). Fixed by two hermetic tests (commit 90a5cd2); second run: all four jobs green. |
| SCT-004 | PLANNED | 2026-09-27 | `docs/ROADMAP.md`: falsifiers F1–F6 for each part of the theory, research tracks A (formal: anomaly side of "forced" via Mathlib's `FiniteCyclic` group cohomology), B (dose-response, thermometer repair, 3D helicity), C (ring-condensate matched-arm experiment, a channel that beats cosmic variance for late-time transitions), D (one genuinely new prediction), and a staged communication plan gated on a priority and positioning audit. Nothing in it is claimed as done. |
| SCT-005 | VERIFIED (two kernels, this repo) | 2026-09-27 | Comparator re-run **in this repository** on all 14 modules (`systemd-run --user --property=RestrictAddressFamilies=~AF_UNIX`, no network): **14/14 accepted by both nanoda and the Lean default kernel**, each reporting "Your solution is okay!" (VortexWinding, QuantizedCirculation, DualLength, Fricke, QHFricke, TopologicalProtection, ScaleResolvedWinding, ContinuumWinding, SectorTemperature, CompactBoson, ChargeLattice, SectorDuality, RCFTDuality, LevelRankDuality; 247–829 s each). The theory's two-kernel record no longer rests on the origin programme's runs. As always: this certifies the proofs and their axiom closure, not that each statement is the right physics. |
| SCT-006 | PUBLISHED | 2026-09-27 | Foundation paper **v3** archived from this repository on its dedicated concept DOI [10.5281/zenodo.22985863](https://doi.org/10.5281/zenodo.22985863): version DOI [10.5281/zenodo.22992255](https://doi.org/10.5281/zenodo.22992255) (supersedes v2, 10.5281/zenodo.22985879). New in v3: Potts/random-cluster as a third "forced" case (16 candidates, 12 verdicts); the SCT-002 erratum in the abstract, §5, and a footnote quoting the superseded wording; the formalization stated precisely as 116 theorems / 14 modules (two-kernel re-check SCT-005); this repository as the theory's home. Published only after SCT-005 passed. Verified via the Zenodo API: one file (`sector_thesis.pdf`, 471,456 bytes), resource type preprint, related identifiers include both repositories, and the concept DOI resolves to the latest version. |
