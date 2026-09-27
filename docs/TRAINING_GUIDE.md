# Training guide: Sector Causality Theory

A guided path through the theory for a physicist, a mathematician, a student, or an AI agent meeting it
for the first time. Each module states one idea, points to where it is proved (Lean), reproduced
(notebook), and argued (paper), and ends with a short exercise. Answers are at the end.

**Prerequisites.** Undergraduate statistical mechanics and some familiarity with the idea of a phase
transition. No string theory, no Lean, and no cosmology are assumed; each is introduced where needed.
**Time.** Modules 0–4 are the core (about three hours with the notebooks). Modules 5–8 are for those
who want to check, extend, or contest the theory.

---

## Module 0 — The thesis in one sentence

> **A duality is a structure; the sector is the cause.**

A *duality* is an exact map between two descriptions of the same physics. A *self-dual point* is a
place where that map sends the theory to itself. The theory makes one claim about when such a point
matters physically, and one claim about what does the work when something happens:

1. **The criterion.** A self-dual point is forced to be physically distinguished **if and only if** it
   exchanges two *inequivalent* sectors on a *discrete* fixed-point set. On a *continuous* moduli space
   with enhanced symmetry — or when self-duality only constrains a fixed point without producing one —
   it is not.
2. **The causal claim.** When something physical happens (a transition, a proliferation, an
   annihilation), it is the **sector** — a conserved or topological label — that crosses a threshold. The
   duality only relabels which sector is which.

Read: `papers/sector_thesis.pdf`, §1 and the boxed criterion.

**Exercise 0.** In your own words, why is "the duality is exact" compatible with "the duality causes
nothing"?

---

## Module 1 — What is a sector?

A **sector** is a label that sorts configurations or theories into classes that no continuous change
can connect without passing through something singular. The simplest example: the winding number `W`
of a phase field around a loop, the number of times the phase wraps around the circle. You cannot
change `W` by smoothly deforming the field; you need a *phase slip* (a point where the field vanishes).

What this project proves about sectors (all in `lean/`, all re-checked by two independent kernels):

| Fact | Lean module | In words |
|---|---|---|
| Winding is conserved without a slip | `TopologicalProtection` | Every continuous evolution avoiding a phase slip keeps `W`; changing `W` forces a slip |
| The slip costs energy | `TopologicalProtection` | On an XY ring of at least ten sites the slip crosses a positive barrier; the bound fails at exactly nine (checked) |
| What you see depends on scale | `ScaleResolvedWinding` | The winding read around a loop is the net charge inside it: a vortex–antivortex pair is invisible from outside |
| The numerical detector is right | `ContinuumWinding` | The sampled, principal-branch loop sum equals the continuum topological degree for every fine-enough sampling |
| Circulation is quantised | `QuantizedCirculation` | Circulation is `W · κ`, `κ = h/m`; no fraction of a quantum |

A sector can also be a *discrete label that is not a winding* — a gauge-group rank `N_c`, a set of
Young diagrams, a lattice of charges `(p, q)` — or a *continuous* parameter (a radius, a coupling
constant). Whether the sector set is discrete or continuous turns out to decide the verdict (Module 3).

Hands-on: `notebooks/02_interventional_experiment.ipynb`, the live winding demo (inject a pair, draw a
loop around one vortex and then both).

**Exercise 1.** A loop encloses a vortex (`+1`) and an antivortex (`−1`) placed close together. What
winding does it read? What does a loop enclosing only the vortex read? Which Lean module says so?

---

## Module 2 — What is a duality? (A Fourier transform on the sector group)

In every clean case examined here, the duality is literally Fourier analysis on the group of sectors
(Savit, *Rev. Mod. Phys.* 52, 453 (1980)):

- **The compact boson.** Sectors are pairs `(n, w) ∈ ℤ²` (momentum, winding). T-duality `R ↦ 2/R`
  swaps them. `lean/CompactBoson.lean` proves this is a *reindexing* of the sector lattice that leaves
  the sector sum invariant (with no convergence hypothesis), and that `Δ_e · Δ_m = 1/4` for every `R`.
- **ℤ_N sectors.** `lean/SectorDuality.lean` builds on Mathlib's own discrete Fourier transform
  (`ZMod.dft`, `ZMod.dft_dft`): the duality is a bijection of sector-weighted data, and for `N ≥ 2` its
  square is **not** the identity — the duality is not an ordinary symmetry.
- **Rational CFT.** `lean/RCFTDuality.lean`: for su(2) level 1, the modular `S`-matrix is (up to
  normalisation) the Hadamard matrix, `S² = 2·𝟙` — the Verlinde relation `S² = C`.

The mathematics is elementary. That is the point: its elementariness is what makes the distinction
between *structure* (the reindexing) and *cause* (the sector) sharp enough to check.

Hands-on: `notebooks/01_criterion_compact_boson.ipynb` computes the sector sum on both sides of
`R ↦ 2/R` and shows they agree.

**Exercise 2.** If a duality is a bijection on sector labels, why can it not by itself *create* a
phase transition?

---

## Module 3 — The self-dual point, and the four verdicts

A self-dual point is a fixed point of the duality map. Applying the criterion to a case returns one of
four verdicts:

| Verdict | When | Paradigm case |
|---|---|---|
| **Forced** | Discrete fixed-point set; the two exchanged sectors are inequivalent and gapped, so they must meet there | Ising (Kramers–Wannier): `T_c` at `sinh 2K = 1` exactly |
| **Not forced** | Continuous moduli space; the fixed point has extra symmetry but nothing happens there | Compact boson: `R = √2` is an ordinary point on a line of CFTs |
| **Constraint, not cause** | Self-duality, *if* the critical point is self-dual, pins a number; dynamics causes the transition | Superconductor–insulator transition: a universal resistance |
| **Organisation, not cause** | The duality organises a diagram; a different mechanism does the causing | Quantum Hall: Γ₀(2) organises the plateau diagram; Laughlin's gauge argument causes quantisation |

The decisive contrast is Ising versus the compact boson. In Ising the order and disorder phases are
exchanged and ℤ₂ has one symmetric point, so the phases are forced to meet there. For the compact
boson the actual transition (Berezinskii–Kosterlitz–Thouless) sits where the vortex operator becomes
marginal, at `R = 2√2` — a threshold on **one sector** — and not at the self-dual radius `√2`.
`CompactBoson.lean` proves `√2 ≠ 2√2` together with the dimensions that locate each.

Hands-on: `notebooks/01_criterion_compact_boson.ipynb` plots `Δ_e`, `Δ_m` against `R` with both radii
marked, next to Ising's `sinh 2K = 1`.

**Exercise 3.** Why would it be a mistake to look for the BKT transition at the self-dual radius?

---

## Module 4 — Is the sector really a cause? An interventional test

Modules 1–3 establish a *correlation*-level criterion. Whether a sector is a *cause* is a different
question, answered in the interventionist sense of Woodward and Pearl: intervene on the sector, hold
everything else fixed, and see whether the outcome changes.

**The experiment** (pre-registered; `papers/sector_thesis.pdf` §3; the source programme's
`causal_topology` paper). A projected Gross–Pitaevskii classical field (a 2D Bose gas) is equilibrated
on three independent bases. From each, the *same energy* is injected two ways, at fixed particle
number and momentum: as four vortex–antivortex pairs (a sector intervention), or as phonons (control).

**The result.** Condensate fraction falls by **0.49–0.73** in the vortex arm and by **at most 0.035** in
the phonon arm; the coherence exponent `η` grows **9–44×** against **at most 1.2×**. The same energy,
delivered as topology, is **15–60× more effective**.

**What failed, and why that is reported.** The pre-registered composite claim included a thermometer
clause: the vortex arm read **5–16% colder**, the wrong sign to explain the effect by heating. The
claim is therefore *not* made in full; the failure is recorded, not reinterpreted. The reading that
survives — the injected vortex configuration is a subsystem with its own temperature, weakly coupled to
the bath — has a machine-checked core: `lean/SectorTemperature.lean` proves the inverse temperature of
a state mixing two sectors is their **mediant**, not their average, so equal energy does not imply equal
temperature once a conserved label exists.

Hands-on: `notebooks/02_interventional_experiment.ipynb` replots the archived results (the
multi-hour simulations are not rerun) and runs the live winding demo.

**Exercise 4.** Why must the control arm receive the *same energy*? What would a larger effect in an
unmatched comparison fail to establish?

---

## Module 5 — The case gallery: sixteen candidates, twelve verdicts

The full table with evidence and citations is in [`CASE_TABLE.md`](CASE_TABLE.md). The pattern to
notice:

- **Only three of sixteen are "forced"**: Ising, SO(3) Yang–Mills at θ = π (anomaly-forced), and the
  q-state Potts model's random-cluster self-dual point (proved critical for every `q ≥ 1` by Beffara and
  Duminil-Copin, whether the transition is continuous or first-order — self-duality fixes *where*, not
  *what kind*).
- **The modal verdict is "not forced"**: the compact boson, RCFT, Seiberg duality (`N_c = N_f/2` in the
  conformal window), and Montonen–Olive S-duality (`τ = i` in 𝒩 = 4 super Yang–Mills — Mathlib itself
  already proves the stabiliser of `τ = i` is `{±1, ±S}`).
- **Three candidates are not instances of the criterion at all**, and saying so is part of the theory:
  topological superconductors (a K-theory *classification*, not a duality), three-dimensional Ising
  duality (maps the spin model to a *different* theory, a ℤ₂ gauge theory — no self-map), and AdS/CFT
  (an equivalence at every coupling, no involution with a fixed locus).
- **One is an explicit open question**: Calabi–Yau mirror symmetry is literally T-duality on a torus
  fibration (Strominger–Yau–Zaslow), but it generically relates *two different* manifolds, and no
  citable physically-distinguished self-mirror threefold exists to ask the question of.
- **A lesson from inside an integrated case**: level-rank duality's own self-dual point `N = K`. The
  Young-diagram labels close up (a square box is fixed by transpose), but the physics does not
  (Hsin–Seiberg: `SU(N)_N` relates to its level-reversal, not to itself). *Labels closing up is not
  physics closing up.*

**Exercise 5.** Why is "not a duality" a different outcome from "not forced"? Why does the difference
matter for the theory's credibility?

---

## Module 6 — Into cosmology, and against real data

The criterion transfers, without new machinery, to three cosmological questions
(`papers/cosmology_sectors.pdf`):

- **K3 as a charge lattice.** A black hole's dyonic charges `(p, q)` on K3×T² fix its entropy through
  an SL(2,ℤ)-invariant discriminant (`lean/ChargeLattice.lean`); the attractor mechanism makes the K3
  geometry an **output** of the charges, never an input a physical system could dial.
- **Wave dark matter.** On a torus, a density observable is blind to an imposed sector at the **1–4%**
  level while injected vortex pairs move it by **21–118%** — the sector is invisible to what most surveys
  measure.
- **Dark energy as a walk on a sector lattice.** A discrete cascade (flux discharges) versus a
  continuous roll: the background expansion cannot tell them apart; a completed first-order transition
  leaves a CMB signature a roll cannot.

**We built the test, not only cited it.** `notebooks/03_cmb_cascade_reproduction.ipynb` independently
reproduces Koren–Tsai–Wang's published CMB bound (arXiv:2509.07076) from its equations and Planck's
own 2018 data: worst-case agreement within a factor of **3.16** across the grid, with an honestly
reported trade-off at high transition rates. A forecast built on it shows Planck's error bars are within
about **13%** of the cosmic-variance floor for `5 ≤ ℓ < 30` (where the signal peaks for most transition
rates) and within a factor of two everywhere up to `ℓ = 50`; since the bound scales as the square root of
the error bar, even a perfect temperature measurement tightens it by at most about **1.4×** — no
temperature-only successor can meaningfully help. (An earlier statement, "within ~15% for ℓ ≈ 5–50,"
rested on nine sampled multipoles; the notebook's full scan corrected it — see `LEDGER.md`, SCT-002. It is
a good example of why the notebooks recompute rather than quote.) It runs on one CPU core; a GPU adds
nothing to this calculation. The
pure-Rust port in rusty-SUNDIALS runs the full 22-point forecast grid in about nine minutes.

**What is never claimed.** No cosmological number is derived. No mapping exists from this project's
toy superfluid simulations to a real transition rate or Hubble scale, and none is proposed — building
one by analogy would be exactly the failure this programme exists to prevent.

**Exercise 6.** Why does "the attractor makes K3 an output of the charges" rule out using K3 geometry
to *select* a cosmological parameter?

---

## Module 7 — Reading the Lean, and what a check does and does not certify

Every theorem is stated in Lean 4 against a pinned Mathlib and ends with a generated
`#print axioms` line. Build: `cd lean && lake update && lake exe cache get && lake build`
(see [`VERIFICATION.md`](VERIFICATION.md)).

Three habits this project enforces, and that you should too:

1. **Axiom footprint.** Only `propext`, `Classical.choice`, `Quot.sound` are permitted. Anything else
   (or a `sorry`) is a failure.
2. **Two kernels.** Comparator re-checks each module's exported proof terms with a second, independent
   kernel (nanoda), so acceptance does not rest on one implementation of type theory.
3. **Negative controls.** For each module, deliberately false variants must *fail*. A check that cannot
   fail certifies nothing.

**The most important caveat.** *A clean footprint certifies the proof, never the statement.* Every
module's docstring says what it does **not** prove. `RCFTDuality` proves a 2×2 integer matrix identity;
that this matrix *is* the su(2)₁ Kac–Peterson S-matrix is representation theory, supplied as prose.
`LevelRankDuality` proves the Young-diagram box bijection, not S,T-matrix preservation. Whether a
statement is the *right* statement remains a human (or agent) audit.

**A retraction worth knowing about.** `lean/DualLength.lean` is included only as a prerequisite of
`Fricke.lean` (its axis action). The *physical* significance once claimed for the dual length was
withdrawn in the source programme: its bound is AM–GM, weaker than the known Onsager bound, and
dimensionally forced (see the source repository's `RETRACTIONS.md`, R2). The group theory stands; the
physics claim does not.

**Exercise 7.** `RCFTDuality.su2Level1_S_sq` passes both kernels with the standard axioms. Does that
prove su(2)₁'s modular S-matrix squares to the charge conjugation? What exactly does it prove?

---

## Module 8 — Extending the theory: the contribution checklist

To propose a new case (a human or an AI agent — see [`../CONTRIBUTING.md`](../CONTRIBUTING.md)):

1. **Literature gate first.** Read the primary sources. Verify every DOI/arXiv ID (Crossref or the
   source itself) before writing it down.
2. **Identify the triad.** What is the sector? What is the duality? Is there a self-map, and a fixed
   point of it? If there is no self-map, stop: the case is "not an instance" (like AdS/CFT).
3. **Discrete or continuous?** Classify the fixed-point set. Check whether the exchanged sectors are
   inequivalent and gapped.
4. **Return one verdict** — or say plainly that the literature does not settle it (like Calabi–Yau).
   Do not force a case into the taxonomy by analogy with earlier cases.
5. **Search Mathlib before assuming anything is (or is not) formalisable.** `YoungDiagram.transpose`,
   `ZMod.dft`, and `ModularGroup.stabilizer_I` were found this way. If nothing checkable exists beyond
   what is already proved, integrate as prose — do not write a token theorem.
6. **Check dependencies, not analogy.** A shared structure between two systems licenses nothing about
   their physics unless a real dependency connects them.

**Exercise 8.** Someone proposes that a self-dual point in a neural-network loss landscape "causes"
generalisation, because the loss is invariant under a weight-space involution. Walk through the
checklist. Where does it fail first?

---

## How this programme relates to Agora-LeanMaster

[SocrateAI-Scientific-Agora-LeanMaster](https://github.com/xaviercallens/SocrateAI-Scientific-Agora-LeanMaster)
is a sibling Lean programme (Double Field Theory, Mathieu moonshine arithmetic, a dual-scale string
cosmology proposal) by the same author. Two things are worth taking from it, and one thing is worth
keeping separate:

- **Take its tooling as a model.** It has a Lean Blueprint (an interactive map from prose claims to
  Lean declarations) and a dependency graph of its declarations. The same presentation would suit this
  repository's fourteen modules; see `mcp-server/CO_DEPLOYMENT.md` for how an agent in the same
  environment can use its blueprint and graph alongside this repository's server.
- **Take its audit habit.** Its own README records an audit that narrowed several headline claims to
  what the Lean actually states — the same discipline as Module 7's caveat.
- **Keep the physics separate.** This programme explicitly *excluded* identifying a superfluid's
  dual-length involution with K3×T² mirror symmetry: the K3 geometry is an output of charges, and a
  superfluid has no such charges. Shared mathematics (T-duality, the Fricke involution) is structure, not
  a physical link — which is, after all, the thesis.

---

## Answers

**0.** Exactness is a property of the map between descriptions; causation is a property of what
changes when you intervene. A bijection of labels changes no physical content — it renames it.

**1.** Zero from outside the pair; `+1` around the vortex alone. `ScaleResolvedWinding` (discrete
Stokes).

**2.** A bijection preserves everything it maps; a transition requires something to change. The
duality can only tell you which sector is which on either side.

**3.** Because the self-dual radius sits on a line of equivalent fixed points; BKT is the vortex
operator's marginality, a threshold on one sector, at `2√2 ≠ √2`.

**4.** Energy is the confound: without matching it, a larger effect could simply be a larger input.
Matching isolates the *form* the energy takes (topology versus phonons).

**5.** "Not forced" is an answer the criterion gives; "not a duality" means the criterion's question
does not apply. Conflating them would let the theory silently absorb cases it has no business
classifying — the failure mode of formalising an analogy.

**6.** An output cannot be dialled independently of what produces it: the charges fix the moduli.
Treating K3 as a selectable input inverts the dependency.

**7.** It proves that a specific 2×2 integer matrix, squared, equals twice the identity. That this
matrix is su(2)₁'s S-matrix is an identification from affine Lie algebra representation theory,
supplied in the docstring as physics input, not checked by the kernel.

**8.** Step 2 (and the final rule): a loss-invariance involution is a symmetry of a function, not a
duality between two descriptions of a physical system with sectors; and "generalisation" has no
established dependency on that fixed point. It is an analogy, which licenses nothing.
