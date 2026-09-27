# Data

Everything the notebooks read. Nothing here needs to be downloaded again.

| path | what | provenance |
|---|---|---|
| `planck2018_tt_full/COM_PowerSpect_CMB-TT-full_R3.01.txt` | Planck 2018 TT power spectrum: ℓ, D_ℓ, −dD_ℓ, +dD_ℓ (μK²) | Planck Legacy Archive (https://pla.esac.esa.int), product COM_PowerSpect_CMB-TT-full_R3.01; checked against Aghanim et al. 2020 (A&A 641, A6): low-ℓ plateau and first-peak amplitude D_220 ≈ 6373 μK². Copied unmodified from the origin repository's `data/external/planck2018_tt_full/`. |
| `results/intervention_r2/I_<base>_<arm>.json` | per-block observables (condensate fraction, temperature, vortex count, coherence exponent η, …) of every arm of the energy-matched intervention | copied unmodified from SocrateAI-Scientific-QuantumFluids `data/generated/pgpe/r2/`; the multi-MB final-field `.npy` snapshots were deliberately not copied |
| `results/intervention_r2/r2_verdicts.json`, `r2_energy_budget.json`, `r2_controls.json` | the pre-registered verdicts, energy budget and controls of that round | same origin, `data/generated/pgpe/` |
| `results/torus_r4/r4_verdicts.json` | round-4 torus test verdicts (B1–B5) | same origin, `data/generated/pgpe/` |
| `results/cmb/python_bound_table_interp_vs_exact.csv` | the 2σ bound on r across (β/H★, z̄_pt), interpolated and exact spectra, with KTW's Eq. 15 | transcribed from the origin repository's `docs/designs/CMB_CASCADE_REPRODUCTION.md` (produced by `exploration/cmb/cmb_bound.py`); notebook 03 recomputes four of these points live and matches them |
| `results/cmb/rust_fisher_grid_pr57.csv` | full exact-spectrum grid with Planck bars and with the cosmic-variance floor | copied from the description of rusty-SUNDIALS PR #57 (`crates/qf-cmb-cascade`, `examples/fisher_grid.rs`) |

Origin repository: https://github.com/xaviercallens/SocrateAI-Scientific-QuantumFluids
