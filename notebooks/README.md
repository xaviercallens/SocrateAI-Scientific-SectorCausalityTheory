# Notebooks — reproduce and explain the theory

Three self-contained Jupyter notebooks. Each explains what it computes for a physicist who has not
read the papers, runs from a fresh clone of this repository alone (all data is in `../data/`), and
says plainly which numbers are **recomputed live** and which are **replotted from archived results**.
Every committed notebook contains the outputs of a complete top-to-bottom execution.

| notebook | what it shows | live | replotted | runtime |
|---|---|---|---|---|
| [`01_criterion_compact_boson.ipynb`](01_criterion_compact_boson.ipynb) | The criterion on its two paradigm cases. Compact boson: T-duality is a reindexing of the $(n,w)$ sectors (the sector sum is invariant under $R\mapsto2/R$), the self-dual radius $\sqrt2$ is not the BKT radius $2\sqrt2$, $\Delta_e\Delta_m=1/4$ for all $R$ — *not forced*. Ising: the Kramers–Wannier fixed point is exactly where order appears — *forced*. | everything | — | seconds |
| [`02_interventional_experiment.ipynb`](02_interventional_experiment.ipynb) | Is the sector a *cause*? A winding number read by a loop sum, invisible for a bound pair (live demo on a synthetic field), then the pre-registered energy-matched intervention: the same energy as vortex pairs collapses the condensate and coherence, as phonons does not — and the pre-registered thermometer clause that **failed**. Round 4: a density map sees vortex cores, not the sector. | the winding demo; every headline number is recomputed from the archived per-block files | the per-block simulation outputs (hours of CPU per arm, not rerun) | seconds |
| [`03_cmb_cascade_reproduction.ipynb`](03_cmb_cascade_reproduction.ipynb) | An independent reproduction of Koren–Tsai–Wang's CMB bound on a discrete late-time dark-energy transition, against the real Planck 2018 TT spectrum, with Elor et al.'s exact bubble-statistics spectrum; and why no temperature-only CMB successor can tighten it (the cosmic-variance floor). | correlator landmark, spectrum, $D_\ell$ curves, four bound points (all twelve with `FULL_GRID = True`), the Planck/cosmic-variance ratio at every multipole | the full Python comparison table and the Rust full Fisher grid (rusty-SUNDIALS PR #57) | ~2 min (~5 min with `FULL_GRID`) |

## Run

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r notebooks/requirements.txt
cd notebooks
jupyter lab                     # or, headless:
jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=1200 *.ipynb
```

`sct_style.py` holds the shared plotting style and paths. Figures are written to `figures/`.

## Honesty notes (read before citing a number)

- **02:** recomputed from the archived blocks, the η ratios against the control arm at $e=0.90$
  seed 11 come out ×10.8 (vortex) and ×1.01 (phonon), where the paper's table quotes ×10.9 and ×0.99 —
  a rounding/averaging difference; every condensate number and the I1/I2/I4 verdict values match the
  paper exactly.
- **03:** the origin design document summarised Planck's error bars as "within 15% of the
  cosmic-variance floor" from nine sampled multipoles. Scanning every multipole shows a two-regime
  structure instead: for $5\le\ell<30$ the published bars equal the floor of the measured spectrum to
  within 13%; from $\ell=30$ (Planck's high-$\ell$ likelihood) the bars are smooth in $\ell$ and sit
  1.0–1.4× a smoothed floor. The bound-level conclusion is unchanged: the largest possible tightening
  anywhere on the grid is 1.39× in $r$.
- **03:** the pure-Rust port (rusty-SUNDIALS PR #57) agrees with this notebook's live values to four
  digits except at $\beta/H_\star=10$, where it differs by about 2% (0.003095 vs 0.003156) — different
  quadrature construction.
- No notebook maps the superfluid simulations onto cosmological parameters; no such bridge exists.
