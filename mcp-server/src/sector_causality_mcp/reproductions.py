"""Bounded, fast (seconds) numerical reproductions of landmark facts the theory relies on.

Standard library only, so an agent can run them anywhere Python runs. Each returns
{ran, name, expected, observed, passed, tolerance, lean_reference, source, note}. `passed` compares the
observed number with a value fixed independently of this code (a closed form, or a published number),
never with a number this same code produced earlier.

Run one:  python -m sector_causality_mcp.reproductions <name>
"""
from __future__ import annotations

import json
import math
import sys
from itertools import combinations


def _simpson(f, a: float, b: float, n: int = 2000) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for k in range(1, n):
        s += (4 if k % 2 else 2) * f(a + k * h)
    return s * h / 3


# --- Elor, Jinno, Kumar, McGehee, Tsai (arXiv:2311.16222), Supplementary Eqs. (S9)-(S16) ---------

def _I_func(t, r):
    return 8 * math.pi * (math.exp(t / 2) + math.exp(-t / 2)
                          + (t * t - (r * r + 4 * r)) / (4 * r) * math.exp(-r / 2))


def _single(t, r):
    I = _I_func(t, r)
    term1 = 2 * math.pi * math.exp(-r / 2) / (r * I)
    term2 = r * r / 4 + r + 2 - t * t / 4
    term3 = math.log(I / (8 * math.pi)) ** 2 - t * t / 4 + math.pi ** 2 / 6
    return term1 * term2 * term3


def _double(t, r):
    I = _I_func(t, r)
    tb = (math.exp(-t / 2 - r / 2) / (2 * r)) * (r + t + 4) * (r - t)
    tc = (math.exp(t / 2 - r / 2) / (2 * r)) * (r - t + 4) * (r + t)
    td = (math.exp(-r) / (16 * r * r)) * ((r + 4) ** 2 - t * t) * (r * r - t * t)
    b1 = 4 - tb - tc + td
    b2 = (math.log(I / (8 * math.pi)) - 1) ** 2 - t * t / 4 + math.pi ** 2 / 6 - 1
    return (16 * math.pi ** 2 / I ** 2) * b1 * b2


def correlator(r: float) -> float:
    r = max(r, 1e-4)
    return _simpson(lambda t: _single(t, r), -r, r) + _simpson(lambda t: _double(t, r), -r, r)


def cmb_correlator_zero() -> dict:
    obs = correlator(1e-4)
    exp = math.pi ** 2 / 6
    tol = 1e-3
    return {
        "expected": exp, "observed": obs, "tolerance": tol, "passed": abs(obs - exp) / exp < tol,
        "lean_reference": None,
        "source": "Elor et al. arXiv:2311.16222 Supp. Eqs. (S9)-(S16); the r->0 value pi^2/6 is a closed "
                  "form the single-bubble term reduces to (the double-bubble term vanishes at r=0).",
        "note": "Landmark used to validate the exact bubble-time spectrum in the CMB reproduction of "
                "Koren-Tsai-Wang arXiv:2509.07076 (notebooks/03, rusty-SUNDIALS crates/qf-cmb-cascade).",
    }


# --- Compact boson T-duality (lean/CompactBoson.lean conventions, alpha' = 2) --------------------

def _dim(R, n, w):
    return n * n / (R * R) + w * w * R * R / 4


def compact_boson_tduality() -> dict:
    R, beta, N = 1.3, 0.7, 30
    def Z(radius):
        return sum(math.exp(-beta * _dim(radius, n, w)) * math.cos(0.37 * n * w)
                   for n in range(-N, N + 1) for w in range(-N, N + 1))
    z1, z2 = Z(R), Z(2 / R)
    prods = [(_dim(r, 1, 0) * _dim(r, 0, 1)) for r in (0.5, 1.0, math.sqrt(2), 2.0, 3.7)]
    sd, bkt = math.sqrt(2), 2 * math.sqrt(2)
    checks = {
        "sector_sum_invariant_under_R_to_2_over_R": abs(z1 - z2) < 1e-10 * abs(z1),
        "electric_times_magnetic_is_quarter_for_all_R": all(abs(p - 0.25) < 1e-12 for p in prods),
        "self_dual_radius_sqrt2_has_equal_dims_one_half":
            abs(_dim(sd, 1, 0) - 0.5) < 1e-12 and abs(_dim(sd, 0, 1) - 0.5) < 1e-12,
        "vortex_marginal_radius_2sqrt2_has_magnetic_dim_2": abs(_dim(bkt, 0, 1) - 2.0) < 1e-12,
        "bkt_radius_differs_from_self_dual_radius": abs(bkt - sd) > 1.0,
    }
    return {
        "expected": {k: True for k in checks}, "observed": {**checks, "Z(R)": z1, "Z(2/R)": z2},
        "tolerance": 1e-10, "passed": all(checks.values()),
        "lean_reference": ["QuantumFluids.CompactBoson.partition_dual",
                           "QuantumFluids.CompactBoson.electric_mul_magnetic",
                           "QuantumFluids.CompactBoson.selfDual_radius",
                           "QuantumFluids.CompactBoson.vortex_marginal_radius",
                           "QuantumFluids.CompactBoson.bkt_not_selfDual"],
        "source": "lean/CompactBoson.lean",
        "note": "Numerical illustration of theorems already proved in Lean (the truncated sum is symmetric "
                "under the swap, so invariance is exact up to rounding). Evidence lives in the proof; this "
                "only shows the proved statements mean what they say on concrete numbers.",
    }


# --- su(2) level-1 modular S-matrix (lean/RCFTDuality.lean) ---------------------------------------

def rcft_su2_level1() -> dict:
    S = [[1, 1], [1, -1]]
    S2 = [[sum(S[i][k] * S[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    det = S[0][0] * S[1][1] - S[0][1] * S[1][0]
    checks = {"S_squared_is_2I": S2 == [[2, 0], [0, 2]], "symmetric": S[0][1] == S[1][0], "det_is_minus_2": det == -2}
    return {
        "expected": {k: True for k in checks}, "observed": {**checks, "S^2": S2, "det": det},
        "tolerance": 0, "passed": all(checks.values()),
        "lean_reference": ["QuantumFluids.RCFTDuality.su2Level1_S_sq", "QuantumFluids.RCFTDuality.su2Level1_S_symm",
                           "QuantumFluids.RCFTDuality.su2Level1_S_det"],
        "source": "lean/RCFTDuality.lean; Verlinde 1988, Fuchs hep-th/9306162",
        "note": "Checks the integer-matrix identity only; that this is the su(2)_1 Kac-Peterson S-matrix is "
                "representation theory supplied as prose.",
    }


# --- Potts / random-cluster self-duality (Beffara-Duminil-Copin 2012) -----------------------------

def _rc_dual(p, q):
    """Random-cluster planar duality: p* defined by  p p* / ((1-p)(1-p*)) = q."""
    x = q * (1 - p) / p
    return x / (1 + x)


def potts_self_dual() -> dict:
    fixed = {}
    for q in (1, 2, 3, 4, 5, 10):
        psd = math.sqrt(q) / (1 + math.sqrt(q))
        fixed[q] = abs(_rc_dual(psd, q) - psd) < 1e-12
    involution = all(abs(_rc_dual(_rc_dual(p, q), q) - p) < 1e-12 for q in (2, 3, 7) for p in (0.1, 0.4, 0.8))
    Kc = math.log(1 + math.sqrt(2)) / 2                  # Ising, sinh(2 Kc) = 1 (Kramers-Wannier)
    p_ising = 1 - math.exp(-2 * Kc)                      # Fortuin-Kasteleyn edge weight of Ising at Kc
    p_sd2 = math.sqrt(2) / (1 + math.sqrt(2))
    checks = {
        "p_sd(q) is a fixed point of the duality for q in {1,2,3,4,5,10}": all(fixed.values()),
        "the duality map is an involution": involution,
        "q=2 self-dual point equals the Kramers-Wannier Ising critical point": abs(p_ising - p_sd2) < 1e-12,
        "Kramers-Wannier: sinh(2 Kc) = 1": abs(math.sinh(2 * Kc) - 1) < 1e-12,
    }
    return {
        "expected": {k: True for k in checks}, "observed": {**checks, "p_sd(2)": p_sd2, "p_Ising(Kc)": p_ising},
        "tolerance": 1e-12, "passed": all(checks.values()),
        "lean_reference": None,
        "source": "Beffara & Duminil-Copin, PTRF 153 (2012), doi:10.1007/s00440-011-0353-8; Kramers & Wannier 1941",
        "note": "Checks the algebra of the self-dual point. That the self-dual point IS the critical point is "
                "the Beffara-Duminil-Copin theorem, cited, not re-proved here.",
    }


# --- Level-rank duality skeleton (lean/LevelRankDuality.lean) -------------------------------------

def _partitions_in_box(a, b):
    """Young diagrams with at most a rows, each of length at most b (weakly decreasing tuples)."""
    out = []
    def rec(prefix, maxpart, rows_left):
        out.append(tuple(prefix))
        if rows_left == 0:
            return
        for part in range(1, maxpart + 1):
            rec(prefix + [part], part, rows_left - 1)
    rec([], b, a)
    return out


def _transpose(lam):
    if not lam:
        return ()
    return tuple(sum(1 for x in lam if x > j) for j in range(lam[0]))


def levelrank_box_transpose() -> dict:
    results = {}
    ok = True
    for a, b in ((2, 3), (3, 4), (4, 4), (5, 2)):
        box_ab, box_ba = set(_partitions_in_box(a, b)), set(_partitions_in_box(b, a))
        image = {_transpose(l) for l in box_ab}
        binom = math.comb(a + b, a)
        good = image == box_ba and len(box_ab) == len(box_ba) == binom
        results[f"{a}x{b}"] = {"count": len(box_ab), "binomial(a+b,a)": binom, "bijection_onto_bxa": good}
        ok = ok and good
    self_conj_4 = sum(1 for l in _partitions_in_box(4, 4) if _transpose(l) == l)
    return {
        "expected": "transpose maps the a x b box bijectively onto the b x a box; |box| = C(a+b, a)",
        "observed": {**results, "self_conjugate_in_4x4": self_conj_4},
        "tolerance": 0, "passed": ok,
        "lean_reference": ["QuantumFluids.LevelRankDuality.inBox_transpose_iff",
                           "QuantumFluids.LevelRankDuality.levelRankRelabeling"],
        "source": "lean/LevelRankDuality.lean; Naculich-Schnitzer 2007, Hsin-Seiberg 2016",
        "note": "Label combinatorics only. At a=b the labels close up (self-conjugate diagrams are fixed points), "
                "but Hsin-Seiberg's own N=K computation relates SU(N)_N to its level reversal, not to itself: "
                "no physical self-duality is implied by these fixed points.",
    }


REGISTRY = {
    "cmb_correlator_zero": cmb_correlator_zero,
    "compact_boson_tduality": compact_boson_tduality,
    "rcft_su2_level1": rcft_su2_level1,
    "potts_self_dual": potts_self_dual,
    "levelrank_box_transpose": levelrank_box_transpose,
}

DESCRIPTIONS = {
    "cmb_correlator_zero": "Exact bubble-time correlator at r->0 equals pi^2/6 (CMB reproduction landmark).",
    "compact_boson_tduality": "Compact-boson sector sum invariant under R -> 2/R; Delta_e*Delta_m = 1/4; sqrt2 vs 2sqrt2.",
    "rcft_su2_level1": "su(2)_1 modular S-matrix: S^2 = 2*1, symmetric, det = -2.",
    "potts_self_dual": "Random-cluster self-dual point is a fixed point of the duality; q=2 reproduces Ising Kc.",
    "levelrank_box_transpose": "Young-diagram transpose is a bijection a x b box -> b x a box (level-rank labels).",
}


def run(name: str) -> dict:
    res = REGISTRY[name]()
    return {"ran": True, "name": name, **res}


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in REGISTRY:
        print(json.dumps({"ran": False, "reason": "usage: reproductions <name>", "available": sorted(REGISTRY)}))
        sys.exit(2)
    print(json.dumps(run(sys.argv[1]), default=str))
