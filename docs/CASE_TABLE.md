# The case table: sixteen candidates, twelve verdicts

Every case examined under the criterion, with its verdict, the reason, the primary literature the
verdict rests on (every DOI/arXiv ID verified against Crossref or the source itself before being
written down), the machine-checked Lean module where one exists, and where the full argument lives.

**The criterion.** A self-dual point pins a physical transition if and only if the two sectors it
exchanges are simultaneously critical and the fixed-point set is discrete. On a continuous moduli space
with enhanced symmetry, the self-dual point is a point like any other. When both dual sectors are
populated and compete, it can be a preferred equilibrium. In every case, the duality relabels the
sectors; the sector acts.

Where the argument lives: **FP** = `papers/sector_thesis.pdf` (foundation paper);
**DS** = `papers/duality_sector.pdf` (technical report; §3 is the original criterion, "Add. N" its dated
addenda); **CS** = `papers/cosmology_sectors.pdf`.

## Verdict counts

| Verdict | Count | Cases |
|---|---:|---|
| Forced | 3 | Ising; SO(3) Yang–Mills at θ = π; Potts / random-cluster |
| Not forced | 4 | Compact boson / BKT; RCFT / Verlinde; Seiberg duality; Montonen–Olive S-duality |
| Constraint, not cause | 2 | Superconductor–insulator; particle-vortex / level-rank (FQHE, ν = ½) |
| Organisation, not cause | 2 | Quantum Hall Γ₀(2) / Fricke; K3×T² dyon lattice (+ D1-D5-P-KK sequel) |
| Preferred equilibrium | 1 | String-gas cosmology |
| **Subtotal with a definite verdict** | **12** | |
| Open question (literature does not settle it) | 1 | Calabi–Yau mirror symmetry |
| Not an instance: not a duality | 1 | Topological superconductors / tenfold way |
| Not an instance: no self-map | 2 | 3D Ising / Wegner duality; AdS/CFT |
| **Total candidates examined** | **16** | |

## Cases with a definite verdict

### 1. Ising (Kramers–Wannier) — **Forced**
The order and disorder operators are exchanged by the duality and ℤ₂ has a single symmetric point: the
two inequivalent, gapped phases are forced to meet there, fixing `T_c` at `sinh 2K = 1`.
- Kramers & Wannier, *Phys. Rev.* 60, 252 (1941), [10.1103/PhysRev.60.252](https://doi.org/10.1103/PhysRev.60.252)
- Fradkin & Susskind, *Phys. Rev. D* 17, 2637 (1978), [10.1103/PhysRevD.17.2637](https://doi.org/10.1103/PhysRevD.17.2637)
- Lean: none (cited, not formalised — elementary algebraic fixed point). Where: DS §3, FP §2.

### 2. SO(3) Yang–Mills at θ = π — **Forced**
The self-dual point separates a ℤ₂ topological phase from the trivial phase; a mixed anomaly, not the
duality map itself, forbids a trivially gapped phase there.
- Kaidi, Ohmori & Zheng, *Phys. Rev. Lett.* 128, 111601 (2022), [10.1103/physrevlett.128.111601](https://doi.org/10.1103/physrevlett.128.111601)
- Choi, Córdova, Hsin, Lam & Shao, *Phys. Rev. D* 105, 125016 (2022), [10.1103/physrevd.105.125016](https://doi.org/10.1103/physrevd.105.125016)
- Lean: none. Where: DS Add. 1.

### 3. Potts / random-cluster model (q ≥ 1) — **Forced**
The random-cluster self-dual point `p_sd(q) = √q / (1 + √q)` *is* the critical point, **proved** for every
`q ≥ 1`. Self-duality fixes *where* the transition is, not its order: continuous for `1 ≤ q ≤ 4`,
discontinuous for `q > 4` — both at the same self-dual point.
- Beffara & Duminil-Copin, *Probab. Theory Relat. Fields* 153, 511 (2012), [10.1007/s00440-011-0353-8](https://doi.org/10.1007/s00440-011-0353-8)
- Duminil-Copin, Sidoravicius & Tassion, *Commun. Math. Phys.* 349, 47 (2017), [10.1007/s00220-016-2759-8](https://doi.org/10.1007/s00220-016-2759-8)
- Duminil-Copin, Gagnebin, Harel, Manolescu & Tassion, *Ann. Sci. ÉNS* 54, 1363 (2021), [10.24033/asens.2485](https://doi.org/10.24033/asens.2485)
- Lean: none (consistent with Ising's citation-only treatment). Where: DS Add. 6, FP §2.

### 4. Compact boson / BKT — **Not forced**
T-duality `R ↦ 2/R` reindexes the `(n, w)` sector lattice. The self-dual radius `√2` sits on a
continuous line of fixed points; the BKT transition is at the vortex-marginality radius `2√2`, a
threshold on one sector — not the self-dual point.
- Nelson & Kosterlitz, *Phys. Rev. Lett.* 39, 1201 (1977), [10.1103/PhysRevLett.39.1201](https://doi.org/10.1103/PhysRevLett.39.1201)
- Savit, *Rev. Mod. Phys.* 52, 453 (1980), [10.1103/RevModPhys.52.453](https://doi.org/10.1103/RevModPhys.52.453)
- **Lean: `CompactBoson`** — `dim_dual`, `partition_dual`, `electric_mul_magnetic` (Δ_e·Δ_m = ¼ for every R), `selfDual_radius`, `vortex_marginal_radius`, `bkt_not_selfDual` (2√2 ≠ √2). Where: DS §2, FP §2. Notebook 01.

### 5. Superconductor–insulator transition — **Constraint, not cause**
Boson–vortex duality predicts a universal resistance *if* the critical point is self-dual; vortex or
charge proliferation causes the transition.
- Fisher, *Phys. Rev. Lett.* 65, 923 (1990), [10.1103/PhysRevLett.65.923](https://doi.org/10.1103/PhysRevLett.65.923)
- Fisher & Lee, *Phys. Rev. B* 39, 2756 (1989), [10.1103/PhysRevB.39.2756](https://doi.org/10.1103/PhysRevB.39.2756)
- Lean: none. Where: DS §3.

### 6. Quantum Hall, Γ₀(2) / Fricke — **Organisation, not cause**
Γ₀(2) organises the plateau diagram and the critical points; Laughlin's gauge argument on the Chern
sector causes quantisation; the Fricke element fixes the critical orbit but is not a symmetry of the
plateaux.
- Lütken & Ross, *Phys. Rev. B* 45, 11837 (1992), [10.1103/PhysRevB.45.11837](https://doi.org/10.1103/PhysRevB.45.11837)
- Laughlin, *Phys. Rev. B* 23, 5632 (1981), [10.1103/PhysRevB.23.5632](https://doi.org/10.1103/PhysRevB.23.5632)
- **Lean: `Fricke`, `QHFricke`** — the Fricke element normalises Mathlib's Γ₀(N); it fixes the critical orbit but sends every plateau off the odd-denominator class. Where: DS §3.

### 7. RCFT / Verlinde (su(2) level 1) — **Not forced**
The modular S-matrix acting on primaries is a duality with `S² = C`. The self-dual radius `R = 1`
(û(1) → ŝu(2)₁ enhancement) sits on a continuous line of RCFT fixed points.
- Verlinde, *Nucl. Phys. B* 300, 360 (1988), [10.1016/0550-3213(88)90603-7](https://doi.org/10.1016/0550-3213(88)90603-7)
- Moore & Seiberg, *Commun. Math. Phys.* 123, 177 (1989), [10.1007/BF01238857](https://doi.org/10.1007/BF01238857)
- Pace, Chatterjee & Shao, arXiv:[2412.18606](https://arxiv.org/abs/2412.18606)
- **Lean: `RCFTDuality`** — `su2Level1_S_sq` (S² = 2·𝟙), `su2Level1_S_symm`, `su2Level1_S_det`. *Not proved:* that this matrix is the Kac–Peterson S-matrix (representation theory, supplied as prose). Where: DS Add. 2.

### 8. Particle-vortex / level-rank duality (FQHE, ν = ½) — **Constraint, not cause**
Particle-hole self-conjugacy at ν = ½ forces an exact number (Berry phase π, σ^CF_xy = −½) without being
a transition. Level-rank duality `U(N)_K ↔ U(K)_N` itself is organisation: a proved relabelling of a
finite anyon label set.
- Son, *Phys. Rev. X* 5, 031027 (2015), [10.1103/PhysRevX.5.031027](https://doi.org/10.1103/PhysRevX.5.031027)
- Seiberg, Senthil, Wang & Witten, *Ann. Phys.* 374, 395 (2016), [10.1016/j.aop.2016.08.007](https://doi.org/10.1016/j.aop.2016.08.007)
- Hsin & Seiberg, *JHEP* 09, 095 (2016), [10.1007/JHEP09(2016)095](https://doi.org/10.1007/JHEP09(2016)095)
- Naculich & Schnitzer, *JHEP* 06, 023 (2007), [10.1088/1126-6708/2007/06/023](https://doi.org/10.1088/1126-6708/2007/06/023)
- **Lean: `LevelRankDuality`** — `inBox_transpose_iff`, `levelRankRelabeling` (the Young-diagram box bijection). *Not proved:* S,T-matrix or Verlinde-formula preservation. Where: DS Add. 2.
- **Deepening (DS Add. 6):** at its own fixed point `N = K` the labels close up (a square box is fixed by transpose) but the physics does not — Hsin–Seiberg show `SU(N)_N` relates to its level-reversal, not to itself. No self-dual question arises there.

### 9. K3×T² dyon lattice, and its D1-D5-P-KK sequel — **Organisation, not cause**
A dyon's entropy depends only on the SL(2,ℤ)-invariant discriminant `D(p,q) = (p·q)² − p²q²`; the number of
inequivalent charges at fixed `D` is a class number. The attractor mechanism makes the K3 geometry an
*output* of the charges. The same discriminant governs the 4D-lifted quarter-BPS D1-D5-P-KK degeneracy;
the class-number statement does **not** transfer there, and the original Strominger–Vafa/Callan–Maldacena
formulas sit outside the discriminant framework.
- Moore, arXiv:[hep-th/9807087](https://arxiv.org/abs/hep-th/9807087)
- Sen, *Gen. Rel. Grav.* 40, 2249 (2008), [10.1007/s10714-008-0626-4](https://doi.org/10.1007/s10714-008-0626-4)
- Sen, *JHEP* 09, 045 (2007), [10.1088/1126-6708/2007/09/045](https://doi.org/10.1088/1126-6708/2007/09/045)
- **Lean: `ChargeLattice`** — `disc_sl2`, `disc_sl2_invariant`, `disc_electric_magnetic_swap`, `disc_scale`, `disc_zero_of_parallel`, `area_sl2_invariant`; plus the Bousso–Polchinski flux lattice and Kaloper's discharge. Where: CS §K3.

### 10. Seiberg duality (4D 𝒩 = 1 SQCD) — **Not forced**
Electric SU(N_c) and magnetic SU(N_f − N_c) flow to the same fixed point throughout the conformal window
`3N_c/2 < N_f < 3N_c`; the point `N_c = N_f/2` is not distinguished. No Lean module: the only
formalisable content, `N_c ↦ N_f − N_c`, is a one-line involution.
- Seiberg, *Nucl. Phys. B* 435, 129 (1995), [10.1016/0550-3213(94)00023-8](https://doi.org/10.1016/0550-3213(94)00023-8)
- Intriligator & Seiberg, *Nucl. Phys. B Proc. Suppl.* 45BC, 1 (1996), [10.1016/0920-5632(95)00626-5](https://doi.org/10.1016/0920-5632(95)00626-5)
- Where: DS Add. 3.

### 11. Montonen–Olive S-duality (𝒩 = 4 super Yang–Mills) — **Not forced**
`S: τ ↦ −1/τ` with `T` generates SL(2,ℤ). `τ = i` and `τ = e^{iπ/3}` are points of enhanced discrete
symmetry on a continuous coupling; 𝒩 = 4 SYM is superconformal for every τ. *Open caveat:* at `τ = i`,
`S` maps the theory to itself only after exchanging discrete global forms of the gauge group.
- Montonen & Olive, *Phys. Lett. B* 72, 117 (1977), [10.1016/0370-2693(77)90076-4](https://doi.org/10.1016/0370-2693(77)90076-4)
- Kapustin & Witten, *Commun. Number Theory Phys.* 1, 1 (2007), [10.4310/cntp.2007.v1.n1.a1](https://doi.org/10.4310/cntp.2007.v1.n1.a1)
- **Lean: Mathlib itself** — `ModularGroup.S_mul_S_eq`, `ModularGroup.stabilizer_I`, `ModularGroup.stabilizer_ρ` already prove the needed facts; no project module was needed. Where: DS Add. 4.

### 12. String-gas cosmology — **Preferred equilibrium**
Momentum modes resist contraction, winding modes resist expansion; with both populated the radion is
stabilised at the self-dual radius. The Hagedorn exit is winding annihilation — a sector event.
- Brandenberger & Vafa, *Nucl. Phys. B* 316, 391 (1989), [10.1016/0550-3213(89)90037-0](https://doi.org/10.1016/0550-3213(89)90037-0)
- Where: DS §3.

## The open question

### 13. Calabi–Yau mirror symmetry — **Open question**
Mirror symmetry is literally T-duality on a special Lagrangian T³ fibration — the furthest extension of
this programme's T-duality thread. But it generically relates *two different* manifolds, not a self-map;
the question only becomes literal for a self-mirror threefold, and no citable physically-distinguished
example exists. What *is* established: a rigid Calabi–Yau (`h^{2,1} = 0`) has no smooth mirror at all.
- Strominger, Yau & Zaslow, *Nucl. Phys. B* 479, 243 (1996), [10.1016/0550-3213(96)00434-8](https://doi.org/10.1016/0550-3213(96)00434-8)
- Candelas, Derrick & Parkes, *Nucl. Phys. B* 407, 115 (1993), [10.1016/0550-3213(93)90276-U](https://doi.org/10.1016/0550-3213(93)90276-U)
- Lean: none (Mathlib has no Calabi–Yau content). Where: DS Add. 5.

## Not instances of the criterion

### 14. Topological superconductors / tenfold way — **Not a duality**
A K-theory / Bott-periodicity *classification* of gapped free-fermion phases, not an exchange between
two descriptions. The one real link (the Kitaev chain maps to the transverse-field Ising model by
Jordan–Wigner) is case 1 in fermionic language, not a new case.
- Ryu, Schnyder, Furusaki & Ludwig, *New J. Phys.* 12, 065010 (2010), [10.1088/1367-2630/12/6/065010](https://doi.org/10.1088/1367-2630/12/6/065010)
- Kitaev, *Phys.-Usp.* 44, 131 (2001), [10.1070/1063-7869/44/10S/S29](https://doi.org/10.1070/1063-7869/44/10S/S29)
- Altland & Zirnbauer, *Phys. Rev. B* 55, 1142 (1997), [10.1103/PhysRevB.55.1142](https://doi.org/10.1103/PhysRevB.55.1142)
- Where: DS Add. 3.

### 15. Three-dimensional Ising / Wegner duality — **No self-map**
In d = 3 the duality maps the Ising spin model to a *different* theory (a ℤ₂ lattice gauge theory); there
is no fixed point to ask about.
- Wegner, *J. Math. Phys.* 12, 2259 (1971), [10.1063/1.1665530](https://doi.org/10.1063/1.1665530)
- Where: DS Add. 4.

### 16. AdS/CFT (weak–strong) — **No self-map**
An equivalence between two descriptions at every coupling, with no conjectured involution and no fixed
locus of enhanced symmetry.
- Maldacena, *Adv. Theor. Math. Phys.* 2, 231 (1998), [10.4310/atmp.1998.v2.n2.a1](https://doi.org/10.4310/atmp.1998.v2.n2.a1)
- Where: DS Add. 4.

## Supporting evidence (not cases, but what the criterion stands on)

| Claim | Where | Lean |
|---|---|---|
| A sector can carry an intervention (conserved without a slip; a slip costs energy) | FP §3 | `TopologicalProtection` |
| A bound pair is invisible from any enclosing scale | FP §3 | `ScaleResolvedWinding` |
| The numerical vortex detector reads the true degree | FP §3 | `ContinuumWinding` |
| Energy-matched intervention: topology 15–60× more effective than phonons | FP §3 | (experiment; pre-registered) |
| Mixed-sector temperature is a mediant, not an average | FP §3 | `SectorTemperature` |
| Duality on ℤ_N sectors is a bijection whose square is not the identity | FP §2 | `SectorDuality` |
| Density is blind to an imposed sector (1–4%) while pairs move it 21–118% | FP §5, CS | (experiment; round 4) |
| Independent CMB bound reproduction: within ×3.16; Planck within ~13% of the cosmic-variance floor for 5 ≤ ℓ < 30 and within ×2 up to ℓ = 50, so a TT-only successor tightens the bound by at most ~1.4× | FP §5 | (numerics; notebook 03) |

## How to propose a change to this table

Open an issue with the label `case-proposal` (see [`../CONTRIBUTING.md`](../CONTRIBUTING.md)) following
the checklist in [`TRAINING_GUIDE.md`](TRAINING_GUIDE.md) Module 8. A proposal that a verdict is wrong is
as welcome as a new case; either must cite primary sources, verified.
