/-
# SectorCausality — the machine-checked backbone of "Duality is a structure; the sector is the cause"

    import SectorCausality

brings in every module below. Extracted from SocrateAI-Scientific-QuantumFluids (the research
programme this theory grew out of) into this standalone repository so the theory is self-contained:
this package pins its own Mathlib revision and depends on nothing else. Built against Lean 4.34.0-rc2
and Mathlib `85e3a25` (tag v4.34.0-rc2). Every theorem carries a `#print axioms` line and the whole
set is re-checked by Comparator against two independent kernels (see `../docs/VERIFICATION.md`).

**What this library is.** Verification infrastructure for a criterion, not new mathematics: every
theorem here is either elementary or a direct instantiation of an existing Mathlib theorem to a new
physical reading. The value is that the distinction the theory draws -- between a duality (a proved,
checkable reindexing of a "sector") and the sector itself (what actually does causal work) -- is
stated precisely enough for a kernel to check it.

| module | the case, and what is proved |
|---|---|
| `CompactBoson` | T-duality of the free boson stated on its winding/momentum sectors: a reindexing that preserves the sector sum; the self-dual radius `R=√2` is a different point from the vortex-marginality radius `2√2` (BKT is not self-dual) |
| `SectorDuality` | the finite-cyclic-group ($\mathbb Z_N$) case, built on Mathlib's own `ZMod.dft`/`ZMod.dft_dft`: the duality is a bijection of sector-weighted data; for $N\geq2$ its square is not the identity |
| `RCFTDuality` | the su(2) level-1 rational-CFT modular $S$-matrix: $S^2=2\cdot\mathbf 1$ (the Verlinde relation), symmetric, $\det=-2$ |
| `LevelRankDuality` | the finite combinatorial skeleton of level-rank duality $U(N)_K\leftrightarrow U(K)_N$: a Young diagram fits an $a\times b$ box iff its transpose fits a $b\times a$ box |
| `ChargeLattice` | Moore's K3$\times T^2$ dyon discriminant, $\mathrm{SL}(2,\mathbb Z)$-invariant; the Bousso--Polchinski flux lattice and Kaloper's discretely-evanescent dark energy; a documentation note on where the discriminant does and does not generalise to 4D-lifted D1-D5-P-KK dyons |
| `Fricke` | the Fricke involution normalises Mathlib's own $\Gamma_0(N)$; its axis action is the `DualLength` involution -- group theory only |
| `QHFricke` | the Fricke element fixes the quantum-Hall critical orbit but sends every plateau off the odd-denominator class |
| `TopologicalProtection` | winding is conserved by every continuous evolution avoiding a phase slip; a change of winding forces a slip; an XY-ring energy barrier |
| `ScaleResolvedWinding` | discrete Stokes: the winding read at an enclosing scale is the net charge inside it, so a bound pair is invisible from outside |
| `ContinuumWinding` | the sampled principal-branch loop sum equals the topological degree of the continuum phase, for every fine-enough sampling |
| `SectorTemperature` | the inverse temperature of a state mixing two sectors is their mediant, not their average -- equal energy does not imply equal temperature once a conserved label exists |
| `VortexWinding`, `QuantizedCirculation`, `DualLength` | prerequisites the modules above build on |
-/
import VortexWinding
import QuantizedCirculation
import DualLength
import Fricke
import QHFricke
import TopologicalProtection
import ScaleResolvedWinding
import ContinuumWinding
import SectorTemperature
import CompactBoson
import ChargeLattice
import SectorDuality
import RCFTDuality
import LevelRankDuality
