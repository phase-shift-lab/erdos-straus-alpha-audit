#!/usr/bin/env python3
"""Independent Sol audit verifier for goal-iteration-10-alpha.

This module deliberately does not import v10_scan.py or verify_v10.py.  It uses
only Python's standard library and emits its result as JSON on stdout.
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

EXPECTED_V10_SHA256 = {
    "EXPLORATION_V10_ALPHA.md": "ceb076f821546a90ce72dfdfdffce3c97bcec7adaef45ffd045bfcb50a3b0bee",
    "PRE_SOL_HANDOFF.md": "73758cdc3e84e96dbbaa3f6a7286c0e28adaef4336fe0fe50f8439c35ed16b27",
    "PRIOR_ART_V10.md": "b851b67baf62b73e56dd8b13372f83c765a47d3921f1416da215e26b87188a71",
    "v10_candidate.json": "00b317699fbd470a4477aa2d3e471f4e0e7559cfe88a07c78bf4ffb243bab35c",
    "v10_candidate.md": "b9527b62ee280bec34302cee1b92cebec335e089701202fcbdeed453856c33dd",
    "v10_hypotheses.json": "02f30393a35355a3269a22533c0ced29265694c0b8e28fcaf5575748f5fdcc0d",
    "v10_scan.json": "e6ca80ee63389fa70ca520d8ab2419a9d81d50a275b90e50206b9ea8c6b7dd77",
    "v10_scan.py": "c2489d7150b098be339a0b5accc6c706ac13fe8972d597b52d597106e501b3de",
    "v10_verification.json": "aca4a8d0405efab5017f139d6891249533ff41c857fde552efba4f29c77299f8",
    "verify_v10.py": "d79b2ab5ca3f1a8a27909101b3cb7e428db0ca331308cc4f9ed1e49ff55ffb48",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sieve(limit: int) -> bytearray:
    prime = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        prime[0] = 0
    if limit >= 1:
        prime[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if prime[p]:
            start = p * p
            prime[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return prime


def squarefree_kernel_and_square_part(n: int) -> tuple[int, int]:
    alpha = 1
    d = 1
    q = n
    p = 2
    while p * p <= q:
        e = 0
        while q % p == 0:
            q //= p
            e += 1
        if e:
            if e % 2:
                alpha *= p
            d *= p ** (e // 2)
        p = 3 if p == 2 else p + 2
    if q > 1:
        alpha *= q
    return alpha, d


def evaluate_row(P: int, delta: int, b: int, c: int) -> dict:
    A = b * c // delta if delta > 0 and (b * c) % delta == 0 else None
    g = math.gcd(b, c)
    bp = b // g
    cp = c // g
    alpha_sf, d_sf = squarefree_kernel_and_square_part(delta)
    alpha_lat = math.gcd(g, bp + cp)
    d_lat = g // alpha_lat
    fraction = (
        Fraction(1, A) + Fraction(1, b * P) + Fraction(1, c * P)
        if A is not None
        else None
    )
    return {
        "P": P,
        "delta": delta,
        "b": b,
        "c": c,
        "A": A,
        "prime_mod4": P % 4,
        "ed2_residual": 4 * b * c - b - c - P * delta,
        "product_residual": (4 * b - 1) * (4 * c - 1) - (4 * P * delta + 1),
        "delta_divides_bc": A is not None,
        "ordered": A is not None and A <= b * P <= c * P,
        "fraction": str(fraction) if fraction is not None else None,
        "fraction_ok": fraction == Fraction(4, P),
        "g": g,
        "g_b": math.gcd(b, g),
        "g_c": math.gcd(c, g),
        "b_prime": bp,
        "c_prime": cp,
        "gcd_bprime_cprime": math.gcd(bp, cp),
        "gcd_bprime_g": math.gcd(bp, g),
        "gcd_cprime_g": math.gcd(cp, g),
        "alpha_squarefree": alpha_sf,
        "d_square": d_sf,
        "squarefree_reconstruction": alpha_sf * d_sf * d_sf,
        "g_squarefree_scale": alpha_sf * d_sf,
        "alpha_lattice": alpha_lat,
        "d_lattice": d_lat,
        "lattice_reconstruction": alpha_lat * d_lat * d_lat,
        "compatibility_mismatch": delta != alpha_lat * d_lat * d_lat,
    }


def strict_theorem_I_displayed(row: dict) -> bool:
    return all(
        [
            row["ed2_residual"] == 0,
            row["product_residual"] == 0,
            row["delta_divides_bc"],
            row["ordered"],
            row["gcd_bprime_cprime"] == 1,
            row["gcd_bprime_g"] == 1,
            row["gcd_cprime_g"] == 1,
        ]
    )


def direct_rows(prime: bytearray, p_limit: int, bc_limit: int) -> list[dict]:
    rows: list[dict] = []
    for P in range(5, p_limit + 1, 4):
        if not prime[P]:
            continue
        for b in range(1, bc_limit + 1):
            for c in range(b, bc_limit + 1):
                numerator = 4 * b * c - b - c
                if numerator % P:
                    continue
                delta = numerator // P
                if delta <= 0 or (b * c) % delta:
                    continue
                row = evaluate_row(P, delta, b, c)
                if row["ordered"]:
                    rows.append(row)
    return rows


def main() -> None:
    failures: list[str] = []

    sha_rows = []
    for name, expected in EXPECTED_V10_SHA256.items():
        path = ROOT / name
        actual = sha256(path) if path.is_file() else None
        ok = actual == expected
        sha_rows.append({"file": name, "expected": expected, "actual": actual, "ok": ok})
        if not ok:
            failures.append(f"v10_sha:{name}")

    p37 = evaluate_row(37, 5, 5, 10)
    p37_required = {
        "prime_mod4": 1,
        "ed2_residual": 0,
        "product_residual": 0,
        "delta_divides_bc": True,
        "ordered": True,
        "fraction_ok": True,
        "g": 5,
        "g_b": 5,
        "g_c": 5,
        "b_prime": 1,
        "c_prime": 2,
        "gcd_bprime_cprime": 1,
        "gcd_bprime_g": 1,
        "gcd_cprime_g": 1,
        "alpha_squarefree": 5,
        "d_square": 1,
        "g_squarefree_scale": 5,
        "alpha_lattice": 1,
        "d_lattice": 5,
        "lattice_reconstruction": 25,
        "compatibility_mismatch": True,
    }
    for key, expected in p37_required.items():
        if p37[key] != expected:
            failures.append(f"P37:{key}:{p37[key]}!={expected}")

    p17 = evaluate_row(17, 4, 2, 10)
    if not strict_theorem_I_displayed(p17) or not p17["compatibility_mismatch"]:
        failures.append("P17_not_strict_mismatch")
    if (p17["alpha_squarefree"], p17["d_square"], p17["alpha_lattice"], p17["d_lattice"]) != (1, 2, 2, 1):
        failures.append("P17_parameter_tuple")

    p29 = evaluate_row(29, 4, 4, 8)
    p29_auxiliary = {
        "paper_constructed_g": 2,
        "actual_gcd_b_c": p29["g"],
        "paper_b_prime": 2,
        "paper_c_prime": 4,
        "paper_gcd_bprime_cprime": math.gcd(2, 4),
        "identity_ok": p29["ed2_residual"] == 0 and p29["fraction_ok"],
    }
    if p29_auxiliary != {
        "paper_constructed_g": 2,
        "actual_gcd_b_c": 4,
        "paper_b_prime": 2,
        "paper_c_prime": 4,
        "paper_gcd_bprime_cprime": 2,
        "identity_ok": True,
    }:
        failures.append("P29_auxiliary")

    family_limit = 2_000_000
    prime = sieve(family_limit)
    family_count = 0
    family_mismatch_count = 0
    theorem_I_count = 0
    theorem_I_mismatch_count = 0
    section7_squarefree_primitive_count = 0
    family_exceptions = []
    for P in range(5, family_limit + 1, 8):
        if not prime[P]:
            continue
        t = (P + 3) // 8
        row = evaluate_row(P, t, t, 2 * t)
        family_count += 1
        if t > 1 and row["compatibility_mismatch"]:
            family_mismatch_count += 1
        elif t > 1:
            family_exceptions.append(P)

        # For P=8t-3, b'=1,c'=2,g=t; the two displayed gcds hold iff t is odd.
        if t % 2 == 1:
            theorem_I_count += 1
            if t > 1 and row["compatibility_mismatch"]:
                theorem_I_mismatch_count += 1

        alpha_sf, d_sf = squarefree_kernel_and_square_part(t)
        if alpha_sf * d_sf == t and math.gcd(1, 2) == 1:
            section7_squarefree_primitive_count += 1

        if row["ed2_residual"] or row["product_residual"] or not row["fraction_ok"]:
            failures.append(f"family_identity:P={P}")
            break
        if P > 5 and math.gcd(t, 3) != 1:
            failures.append(f"family_gcd_t_3:P={P}")
            break

    if family_exceptions:
        failures.append(f"family_mismatch_exceptions:{family_exceptions[:5]}")

    # Independent direct ED2 enumeration, with a different range from v10.
    direct = direct_rows(prime, p_limit=349, bc_limit=180)
    strict_mismatches = [r for r in direct if strict_theorem_I_displayed(r) and r["compatibility_mismatch"]]
    strict_mismatches.sort(key=lambda r: (r["P"], r["b"], r["c"], r["delta"]))
    smallest = strict_mismatches[0] if strict_mismatches else None
    if smallest is None or (smallest["P"], smallest["delta"], smallest["b"], smallest["c"]) != (17, 4, 2, 10):
        failures.append("direct_smallest_strict_mismatch_not_P17")

    result = {
        "audit": "independent Sol v10 verification",
        "imports_scan": False,
        "standard_library_only": True,
        "failures": failures,
        "v10_sha": {"all_ok": all(r["ok"] for r in sha_rows), "rows": sha_rows},
        "P37": p37,
        "P37_strict_theorem_I_displayed": strict_theorem_I_displayed(p37),
        "P17_smaller_strict_candidate": p17,
        "P17_strict_theorem_I_displayed": strict_theorem_I_displayed(p17),
        "P29_auxiliary": p29_auxiliary,
        "family": {
            "formula": "P=8t-3, delta=t, b=t, c=2t, A=2t",
            "prime_bound": family_limit,
            "all_prime_rows_including_P5": family_count,
            "mismatches_for_t_gt_1": family_mismatch_count,
            "theorem_I_displayed_gcd_rows_t_odd": theorem_I_count,
            "theorem_I_mismatches_for_t_gt_1": theorem_I_mismatch_count,
            "section7_squarefree_primitive_rows": section7_squarefree_primitive_count,
            "exceptions": family_exceptions,
            "symbolic_residuals": {
                "4bc-b-c-Pdelta": "4t(2t)-t-2t-(8t-3)t = 0",
                "A_delta-bc": "(2t)t-t(2t) = 0",
                "fraction": "1/(2t)+1/(tP)+1/(2tP)=4/P for P=8t-3",
                "lattice_reconstruction": "gcd(t,3)*(t/gcd(t,3))^2; equals t^2 when prime P>3",
            },
        },
        "direct_enumeration": {
            "P_max": 349,
            "b_c_max": 180,
            "valid_ordered_rows": len(direct),
            "strict_displayed_mismatches": len(strict_mismatches),
            "smallest_strict_mismatch": smallest,
        },
        "scope_note": "Finite scans support reproducibility only; the family statement is established by the recorded identities, with infinitude of prime P congruent to 5 mod 16 requiring Dirichlet's theorem.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
