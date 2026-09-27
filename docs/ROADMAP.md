# Roadmap: extension, falsification, observation, communication

Written 2026-09-27. A plan, not a promise: every direction below is ranked by what it would add to
the evidence, and every one carries its own kill criterion. Nothing here is claimed as done unless
`LEDGER.md` says so. The ranking follows an external-style assessment of the theory made on the same
day (summarised in §0), whose central advice was: *make the theory able to fail, and make it predict
something not already known.*

---

## 0. Where the theory stands — honestly

**What is solid.** One criterion applied consistently to sixteen candidate cases (twelve verdicts,
one open question, three correctly excluded); a Lean skeleton of 116 theorems, built on GitHub's own
CI and re-checked by a second kernel; three executed reproduction notebooks; an independently
reproduced cosmological bound against real Planck data.

**What is genuinely new.** Not the mathematics of any single duality. The new parts are:
1. The **interventionist test** of whether a topological sector is a *cause*: an energy-matched,
   pre-registered comparison (topology 15–60× more effective per unit energy than phonons), with its
   own failed criterion reported.
2. The **systematic taxonomy**, where "not an instance" and "the literature does not settle this" are
   first-class outcomes rather than silent omissions.
3. The **verification discipline** itself: machine-checked skeletons, stated scope limits, errata.

**What a referee will say is already known**, and the roadmap must answer:
- Duality as a Fourier transform on the sector group is Savit (1980).
- *Why* some self-dual points are forced is already explained by 't Hooft anomalies in the
  non-invertible-symmetry literature (Aasen–Mong–Fendley; Choi–Córdova–Hsin–Lam–Shao;
  Kaidi–Ohmori–Zheng; Shao's lectures). The criterion's "forced" half is close to a restatement of
  anomaly matching.
- "Self-dual points on conformal manifolds are not transitions" is standard lore.
- Most verdicts are *readings* of existing literature. The strongest empirical result lives in a
  two-dimensional classical-field model.

The consequence for positioning: present SCT as **a precise, checked, tested unifying criterion
plus a reusable causal-testing method**, not as new physics. The roadmap's job is to change that
sentence by producing one genuinely new, falsifiable prediction.

---

## 1. Falsification programme

A theory that cannot fail certifies nothing, the same rule as a Lean negative control. Below, each part
of SCT is stated with what would refute it. A refutation is a result, and would be recorded as one.

| # | Part of the theory | It is **falsified** by | Status |
|---|---|---|---|
| F1 | "Forced" direction: discrete fixed points exchanging inequivalent gapped sectors pin a transition | A self-dual point on a discrete fixed-point set, exchanging two inequivalent gapped sectors, that is demonstrably **not** a transition (no non-analyticity, no phase change) | No counterexample known. Potts/random-cluster, **proved** for every q ≥ 1, strengthens it. |
| F2 | "Not forced" direction: continuous moduli never force a transition at the self-dual point | A transition located **at** a self-dual point on a continuous moduli space, whose position is explained by the self-duality rather than by a sector threshold that happens to coincide with it | Four cases consistent (BKT, RCFT, Seiberg, Montonen–Olive). The Montonen–Olive global-form caveat (SU(N) ↔ PSU(N) at τ = i) is the nearest thing to a live threat. |
| F3 | Taxonomy completeness: every duality with a self-map falls into one of the four verdicts | A duality with a genuine self-map and fixed locus that fits none of forced / not forced / constraint / organisation | Calabi–Yau is *open*, not a misfit: no self-mirror example exists to test. |
| F4 | Causal claim: the sector, not the energy, is the difference-maker | An energy-matched intervention, in a regime where the sector is well defined (no phase slips during the measurement window), where topology's effect is **not** larger than the control's within uncertainty | One system tested (2D projected GPE, three bases): consistent. **The thermometer clause failed**: the causal claim is made without it. |
| F5 | Sector-blindness of density observables (the dark-matter transplant) | A density-only statistic that reads an imposed net winding at matched core content | Round 4 torus: blind at 1–4% against a 21–118% pair signal. One geometry, one resolution. |
| F6 | The cosmological reading makes no number up | Any cosmological parameter "derived" from the toy simulations | None exists, none is claimed; guarded by the checklist in `TRAINING_GUIDE.md` Module 8. |

**Rule for every direction below:** write the prediction and the pass/fail threshold *before* running
it, and record it as a pre-registration in `LEDGER.md` (the origin programme's pre-registration
format carries over).

---

## 2. Research directions

Ranked within each track by evidential value per unit effort. Each direction lists its **deliverable**,
**kill criterion**, and **effort** (S ≤ 1 week, M ≤ 1 month, L = months, requires collaborators).

### Track A — Formal: turn the criterion from prose into a theorem

**A1 (highest value). Formalise the anomaly side of "forced" for finite cyclic groups.** *(M)*
The referee objection above says "forced" *is* anomaly matching. Meet it head-on: state in Lean the
classification the forcing argument runs on. The pinned Mathlib already has group cohomology in general
degree (`groupCohomology`) and a dedicated `RepresentationTheory/Homological/GroupCohomology/FiniteCyclic`
file for cyclic groups (checked 2026-09-27). Target: the ℤ_N anomaly group (degree-3 cohomology of ℤ_N
with U(1)-valued coefficients, ≅ ℤ_N) as a theorem, with `SectorDuality`'s gauging map shown to act on it.
- *Deliverable:* `lean/AnomalyZN.lean`, plus a docstring stating exactly where the Lean stops. The
  physics step, "a nonzero mixed anomaly forbids a trivially gapped phase", stays prose unless it can
  be reduced to a finite statement.
- *Kill criterion:* if the coefficient bookkeeping (U(1) as a representation over ℤ) cannot be
  expressed with existing Mathlib API within the effort bound, record what is missing and stop.

**A2. The criterion as a decision procedure on a finite model class.** *(M)* For ℤ_N clock/Potts-type
models with a finite set of couplings, state the verdict as a function of (fixed-point set discrete?,
sectors inequivalent?). Prove the Ising and q-state Potts instances return "forced", and that a continuous
family returns "not forced".
- *Kill criterion:* if "inequivalent gapped sectors" cannot be given a finite, checkable definition for
  the class, the criterion is not yet a theorem. Say so, and keep it as prose.

**A3. Blueprint and dependency graph.** *(S)* Generate a Lean Blueprint (prose claim → declaration)
and a declaration graph for `lean/`, following the tooling of the sibling Agora-LeanMaster programme.
Its `leangraph` accepts a root/target and has not yet been tried on this repository.
- *Deliverable:* a browsable map that makes "where the Lean stops" visible.

**A4. Close the inherited-verification gap.** *(S, running)* Comparator's second kernel re-run *in this
repository* for all 14 modules (9/14 accepted when this was written), recorded as `SCT-003`.

### Track B — Numerical: strengthen the causal claim where it is weakest

**B1 (highest value). Dose-response for the intervention.** *(M)* Causal claims are strengthened by
dose-response. Vary the injected winding charge (1, 2, 4, 8 pairs) at matched energy, and vary the
energy at fixed charge.
- *Prediction to pre-register:* the effect scales with topological charge at fixed energy, not with
  energy at fixed charge.
- *Kill criterion:* if the effect tracks energy rather than charge, F4 fails for this system, and the
  paper's causal section is revised.

**B2. Repair the failed thermometer clause.** *(M)* Pre-register a two-thermometer measurement: the
phonon bath temperature, and the vortex-gas temperature via the calibrated point-vortex estimator. This
tests the mediant prediction of `SectorTemperature` directly, instead of reading it post hoc.
- *Kill criterion:* if the two temperatures do not separate as predicted, the "sector carries its own
  temperature" reading is withdrawn.

**B3. Three dimensions: helicity and linked vortex rings.** *(L)* Repeat the energy-matched protocol
in 3D GPE with linked versus unlinked vortex rings of equal energy. Helicity is the 3D topological
invariant. The Rust `qf-pgpe` engine in rusty-SUNDIALS is the natural base, extended to 3D.
- *Kill criterion:* if linking makes no energy-matched difference, SCT's causal claim is recorded as
  2D-specific.

**B4. Close the round-3 finite-size question (C2).** *(S, running)* The L = 128 rerun with doubled
equilibration is in progress in the origin programme. Its admission result decides whether the
finite-size ladder comparison is void or restored.

**B5. The cosmological bound, from toy statistic to likelihood.** *(L)* Replace the reproduced 3-bin χ²
with a real Planck likelihood (CAMB/CLASS module for the phase-transition signal, plus a sampler). The
Rust port makes the forward model fast. The bottleneck is implementing the new physics in a Boltzmann
code: weeks, not days, regardless of hardware.

### Track C — Observation and experiment: where the theory meets data it has not seen

**C1 (highest value). A laboratory matched-arm experiment in a ring condensate.** *(L, needs a lab)*
Atomtronic rings already imprint and read quantised persistent currents (Eckel et al., *Nature* 506,
200 (2014), [10.1038/nature12958](https://doi.org/10.1038/nature12958)).
- *Proposal:* imprint winding W in one arm, and deposit the same energy as non-topological excitation
  in the other. Compare condensate fraction, coherence, and current decay.
- *Pre-registered prediction:* per unit energy, the sector arm's effect exceeds the control's. The
  current decays in discrete phase-slip steps, not continuously.
- *First step (S):* a one-page proposal with the numerical predictions from B1, sent as a question, not
  a claim, to groups already doing ring-condensate work. Mapping the classical-field numbers to an
  experiment's parameters is itself a derivation to do *before* contact.

**C2. Rotating superfluids and vortex-cluster data.** *(M)* Public vortex-position data (Gauthier et
al. 2019, already used in the origin programme) supports sector-level statistics without new
experiments. Extend the Onsager-dipole analysis to a pre-registered, sector-versus-pairs discrimination
on those data.

**C3. Late-time discrete dark energy: find a channel that beats cosmic variance.** *(M, research question)*
The reproduction shows no temperature-only CMB successor can help: Planck is within about 13% of the
cosmic-variance floor for 5 ≤ ℓ < 30, and the bound tightens at most ~1.4×. So the observational question
is which *other* channel could. One candidate to examine, **unverified and possibly swamped by noise**:
- *Idea:* the transition's redshift perturbation δz₀ is imprinted on *every* photon crossing the
  first-encounter surface. Sources beyond z_pt would then share the CMB's large-angle δz₀ pattern.
  That suggests a cross-correlation between the CMB temperature map and a low-ℓ map of galaxy-redshift
  residuals for sources beyond z_pt.
- *First step:* a literature gate (has this been proposed?), then an order-of-magnitude estimate. At the
  current bound δz₀ ~ 10⁻⁵–10⁻⁴, while peculiar velocities give ~10⁻³ per galaxy with correlated
  large-scale structure.
- *Kill criterion:* if the peculiar-velocity field's low-ℓ variance exceeds the signal for any
  realistic survey, record the channel as closed.

Other channels to scope the same way: kSZ, the CMB dipole (both already used against the single-bubble
model), 21-cm intensity mapping. Spectral distortions and pulsar timing arrays probe *earlier*
transitions, not the late-time ones considered here — do not conflate.

**C4. Hunt for an F1/F2 counterexample in the literature.** *(M, ideal for AI agents)* Systematically
search lattice-model and CFT literature for self-dual points that break the criterion: exactly the
falsifiers of §1. A found counterexample is the most valuable single contribution anyone can make.

### Track D — Theory extension: a genuinely new prediction

**D1 (the priority the assessment named). One new, testable prediction.** *(L)* The theory so far
*classifies known results*. It needs one prediction nobody has made. The candidates with the clearest
route are B1 (dose-response, numerical, in reach), C1 (laboratory, needs a partner), and C3
(observational, needs a channel that survives its kill criterion). Whichever of these first produces a
pre-registered, quantitative, falsifiable statement becomes the headline of the next paper version.

**D2. Beyond groups: fusion-category sectors.** *(L)* Non-invertible symmetries replace sector *groups*
with fusion categories. Restate the criterion for sectors labelled by simple objects of a fusion
category, and check it on the Fibonacci / Ising categories. Level-rank duality's own case already shows
the trap: labels can close up while physics does not.

**D3. The open and caveated items.**
- **Calabi–Yau:** stays open until a citable, physically distinguished self-mirror threefold is found.
  Search, do not guess.
- **Montonen–Olive:** decide whether the SU(N) ↔ PSU(N) global-form exchange at τ = i changes the verdict.
- **N = K level-rank:** documented. No further action unless new literature appears.

---

## 3. Communication roadmap

Staged so that each audience meets the version of the claim it can check.

| Phase | Audience | Deliverable | Venue / channel | Gate before moving on |
|---|---|---|---|---|
| **P0 (now)** | Anyone landing on the repo | This repository, training guide, notebooks, MCP server | GitHub | CI green; Comparator 14/14 recorded; foundation paper v3 archived with the erratum |
| **P1 (weeks)** | Experts, cheaply | The sharpest single question, *"When does a self-dual point pin a phase transition?"*, posed without claiming priority | Physics StackExchange / MathOverflow; Lean Zulip (the formalization) | A written **priority and positioning audit**: which parts of SCT are Savit / anomaly matching / lore, and which are new. Required before P2. |
| **P2 (1–3 months)** | Formal-methods community | "Machine-checked skeletons for a physics criterion: what the kernel certifies and what it cannot" | CPP / ITP-style venue or workshop; Lean community blog | The formalization claims survive Zulip feedback |
| **P2** | Philosophy of physics | The interventionist causal argument (energy-matched, pre-registered, with its failed clause) | Philosophy-of-physics journal (e.g. BJPS, SHPMP) | B1 dose-response pre-registered, ideally run |
| **P3 (3–6 months)** | Physicists | A **perspective** paper, not a "new results" letter: the criterion, the taxonomy with exclusions, the causal method, and the positioning audit on page one | arXiv (physics.hist-ph, cross-listed to hep-th / cond-mat.stat-mech; **an endorser is needed**, as the author has no prior arXiv record) | Positioning audit done; D1 either achieved or honestly stated as not yet |
| **P4 (6–12 months)** | Experimentalists | The C1 proposal with numerical predictions | Direct contact with ring-condensate groups, as a question | B1 numbers in hand |

**Communication principles (non-negotiable).**
- Lead with what cannot be dismissed as known: the formalization, the matched-arm causal test, and the
  honest exclusions and errata. Address the Savit and generalized-symmetries overlap on page one.
- Engage the generalized-symmetries researchers as *readers*, by citing their work accurately. Never
  claim priority over anomaly matching.
- Every public claim links to a ledger entry, and every number to a notebook or a Lean theorem.
- Errata are published like results: SCT-002 is the model.

**An explorable explainer (optional, P1–P2).** An interactive page walking a reader through
"here is a self-dual point: is it forced?" on the worked cases. The compact-boson radius plot would be
live, and each verdict would link to its Lean theorem and paper paragraph.

---

## 4. Collaboration: what scientists and AI agents can pick up now

Tasks are sized for one contributor. Agents should use the MCP server (`mcp-server/`) and follow
`CONTRIBUTING.md`: declare yourself, show the evidence trail, and treat `ran: false` as not a pass.

| Task | Track | Size | Good for |
|---|---|---|---|
| Hunt for F1/F2 counterexamples in lattice and CFT literature | C4 | M | agents, theorists |
| Priority and positioning audit (Savit, anomaly matching, lore) | P1 | M | agents, historians of physics |
| Run LeanGraph / Blueprint on `lean/` | A3 | S | Lean users |
| Order-of-magnitude estimate for the C3 cross-correlation channel | C3 | S | cosmologists |
| Pre-register B1 dose-response (write the thresholds only) | B1 | S | anyone |
| Attempt `AnomalyZN.lean` on Mathlib's `FiniteCyclic` group cohomology | A1 | M | Lean + physics |
| Reproduce a notebook on your machine and file a reproduction report | P0 | S | everyone |

---

## 5. Milestones and decision gates

| When | Milestone | Decision it triggers |
|---|---|---|
| Days | CI green on GitHub; Comparator 14/14 in this repo (`SCT-003`); foundation paper v3 archived | P0 complete; P1 may start |
| 2–4 weeks | Positioning audit written; B1 pre-registered; A3 map published | If the audit finds the criterion *fully* subsumed by anomaly matching, reframe SCT around the causal method and the taxonomy only |
| 1–3 months | B1 run; A1 attempted; C3 order-of-magnitude done | If B1 fails (effect tracks energy), revise the causal section before any P3 submission |
| 3–6 months | Perspective paper on arXiv; formal-methods submission | Go/no-go on C1 outreach depends on B1 |
| 6–12 months | C1 proposal circulated; D1 prediction stated or honestly not yet | The next paper version's headline is whichever prediction survived |

**Standing rule.** A direction that hits its kill criterion is closed and recorded, not quietly dropped.
Three of sixteen candidate cases were excluded, one left open, and one numerical claim corrected in
public. That record is the theory's credibility, and every item on this roadmap is meant to extend it.
