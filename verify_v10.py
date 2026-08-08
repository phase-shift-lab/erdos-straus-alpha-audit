"""Independent verifier for the v10 alpha-compatibility candidate.

The verifier intentionally does not import v10_scan.py or any earlier code.
It recomputes the prime family, the ED2 identities, the squarefree data, and
the lattice quantities using separate routines.
"""

from fractions import Fraction
from math import gcd
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
failures = []


def check(condition, label, detail=None):
    if not condition:
        failures.append({"label": label, "detail": detail})


def prime_flags(limit):
    flags = [True] * (limit + 1)
    flags[0] = False
    flags[1] = False
    for p in range(2, limit + 1):
        if flags[p] and p * p <= limit:
            multiple = p * p
            while multiple <= limit:
                flags[multiple] = False
                multiple += p
    return flags


def factor_squarefree(n):
    kernel = 1
    root = 1
    q = 2
    remainder = n
    while q * q <= remainder:
        exponent = 0
        while remainder % q == 0:
            remainder //= q
            exponent += 1
        if exponent % 2 == 1:
            kernel *= q
        root *= q ** (exponent // 2)
        q += 1
    if remainder > 1:
        kernel *= remainder
    return kernel, root


def verify_family_integer_identity(t):
    P = 8 * t - 3
    b = t
    c = 2 * t
    delta = t
    A = 2 * t
    check(4 * b * c - b - c == P * delta, "family_ED2_identity", {"t": t})
    check((4 * b - 1) * (4 * c - 1) == 4 * P * delta + 1, "family_product_identity", {"t": t})
    check(Fraction(4, P) == Fraction(1, A) + Fraction(1, b * P) + Fraction(1, c * P), "family_fraction", {"t": t})
    check(A < b * P < c * P, "family_order", {"t": t, "P": P})
    return P, b, c, delta, A


def verify_family_prime(P):
    t = (P + 3) // 8
    P0, b, c, delta, A = verify_family_integer_identity(t)
    check(P0 == P, "family_parameter_recovery", {"P": P, "P0": P0})
    g = gcd(b, c)
    bp = b // g
    cp = c // g
    alpha_lat = gcd(g, bp + cp)
    d_lat = g // alpha_lat
    alpha_sf, d_sf = factor_squarefree(delta)
    check(g == t and bp == 1 and cp == 2, "family_normalization", {"P": P, "g": g, "bp": bp, "cp": cp})
    check(alpha_lat == 1, "family_lattice_alpha", {"P": P, "t": t, "alpha_lat": alpha_lat})
    check(delta == t and d_lat == t, "family_lattice_d", {"P": P, "delta": delta, "d_lat": d_lat})
    check(delta != alpha_lat * d_lat * d_lat, "family_incompatibility", {"P": P, "delta": delta, "predicted": alpha_lat * d_lat * d_lat})
    return {
        "P": P,
        "t": t,
        "b": b,
        "c": c,
        "delta": delta,
        "A": A,
        "g": g,
        "bp": bp,
        "cp": cp,
        "alpha_squarefree": alpha_sf,
        "d_square": d_sf,
        "alpha_lattice": alpha_lat,
        "d_lattice": d_lat,
        "delta_from_lattice": alpha_lat * d_lat * d_lat,
        "fraction_ok": True,
    }


def direct_ed2_rows(primes, bound):
    rows = []
    for P in primes:
        if P % 4 != 1:
            continue
        for b in range(1, bound + 1):
            for c in range(b, bound + 1):
                numerator = 4 * b * c - b - c
                if numerator <= 0 or numerator % P:
                    continue
                delta = numerator // P
                if delta <= 0 or b * c % delta:
                    continue
                A = b * c // delta
                if A > b * P:
                    continue
                if Fraction(4, P) != Fraction(1, A) + Fraction(1, b * P) + Fraction(1, c * P):
                    failures.append({"label": "direct_fraction", "detail": {"P": P, "b": b, "c": c}})
                    continue
                g = gcd(b, c)
                bp, cp = b // g, c // g
                alpha_lat = gcd(g, bp + cp)
                d_lat = g // alpha_lat
                rows.append({
                    "P": P,
                    "b": b,
                    "c": c,
                    "delta": delta,
                    "A": A,
                    "alpha_lattice": alpha_lat,
                    "d_lattice": d_lat,
                    "consistent": delta == alpha_lat * d_lat * d_lat,
                })
    return rows


def main():
    limit = 1_000_000
    flags = prime_flags(limit)
    family_primes = [p for p in range(5, limit + 1, 8) if flags[p] and p > 5]
    family_records = [verify_family_prime(p) for p in family_primes]
    theorem_I_family_records = [r for r in family_records if r["t"] % 2 == 1]
    check(len(family_records) > 1000, "family_scan_nontrivial", len(family_records))
    check(all(not r["fraction_ok"] is False for r in family_records), "family_fraction_all")
    check(all(r["delta"] != r["delta_from_lattice"] for r in family_records), "family_all_mismatch")
    check(len(theorem_I_family_records) > 1000, "theorem_I_family_scan_nontrivial", len(theorem_I_family_records))
    check(all(r["delta"] != r["delta_from_lattice"] for r in theorem_I_family_records), "theorem_I_family_all_mismatch")

    for t in range(1, 10001):
        verify_family_integer_identity(t)

    P37 = verify_family_prime(37)
    check(P37["b"] == 5 and P37["c"] == 10 and P37["delta"] == 5 and P37["A"] == 10, "P37_exact_row", P37)
    check(P37["alpha_squarefree"] == 5 and P37["d_square"] == 1, "P37_squarefree_view", P37)
    check(P37["alpha_lattice"] == 1 and P37["d_lattice"] == 5, "P37_lattice_view", P37)
    check(P37["delta_from_lattice"] == 25, "P37_predicted_delta", P37)
    check(gcd(P37["bp"], P37["g"]) == 1 and gcd(P37["cp"], P37["g"]) == 1, "P37_theorem_I_gcd_conditions", P37)
    check(P37["b"] <= P37["c"] and P37["b"] * P37["c"] % P37["delta"] == 0, "P37_order_and_divisibility", P37)
    check(P37["A"] <= P37["b"] * P37["P"], "P37_A_bound", P37)

    P29_template = {
        "P": 29,
        "alpha": 1,
        "d": 2,
        "bp": 2,
        "cp": 4,
    }
    P29_g = P29_template["alpha"] * P29_template["d"]
    P29_b = P29_g * P29_template["bp"]
    P29_c = P29_g * P29_template["cp"]
    check((4 * P29_g * P29_template["bp"] - 1) * (4 * P29_g * P29_template["cp"] - 1) == 4 * 29 * 4 + 1, "P29_template_product")
    check(gcd(P29_template["bp"], P29_template["cp"]) != 1, "P29_nonprimitive_displayed_example")
    check(gcd(P29_b, P29_c) != P29_g, "P29_g_reset_mismatch", {"g_displayed": P29_g, "gcd_bc": gcd(P29_b, P29_c)})

    small_primes = [p for p in range(2, 201) if flags[p]]
    direct_rows = direct_ed2_rows(small_primes, 120)
    direct_mismatches = [r for r in direct_rows if not r["consistent"]]
    check(len(direct_rows) > 0, "direct_ED2_rows_nonempty")
    check(len(direct_mismatches) > 0, "direct_ED2_mismatch_nonempty")

    result = {
        "version": "v10-alpha-verifier-1",
        "imports_scan": False,
        "failures": failures,
        "scope": {
            "family_prime_limit": limit,
            "family_condition": "prime P == 5 mod 8, P > 5",
            "symbolic_integer_t": 10000,
            "direct_ED2": "P <= 200, b <= c <= 120",
        },
        "family": {
            "prime_count": len(family_records),
            "mismatch_count": sum(1 for r in family_records if r["delta"] != r["delta_from_lattice"]),
            "theorem_I_displayed_gcd_subfamily_count": len(theorem_I_family_records),
            "theorem_I_displayed_gcd_subfamily_mismatch_count": sum(1 for r in theorem_I_family_records if r["delta"] != r["delta_from_lattice"]),
            "first": family_records[:10],
            "last": family_records[-3:],
        },
        "P37": P37,
        "P29": {
            "displayed_template": P29_template,
            "b": P29_b,
            "c": P29_c,
            "gcd_b_c": gcd(P29_b, P29_c),
        },
        "direct_ED2": {
            "row_count": len(direct_rows),
            "mismatch_count": len(direct_mismatches),
            "first_mismatches": direct_mismatches[:10],
        },
        "iff_checked": {
            "family_identity": "For t>=1: 4*t*(2*t)-t-2*t = t*(8*t-3).",
            "fraction_identity": "4/(8t-3)=1/(2t)+1/(t(8t-3))+1/(2t(8t-3)).",
            "lattice_values": "g=t,b'=1,c'=2, alpha_lat=gcd(t,3), d_lat=t/alpha_lat.",
            "prime_reduction": "For prime P=8t-3>3, alpha_lat=1, hence delta_from_lattice=t^2.",
        },
        "assessment": {
            "candidate_status": "correction_possible_pre_audit",
            "novelty_claim": False,
            "not_ESC_refutation": True,
            "not_ESC_solution": True,
            "audit_needed": True,
        },
    }
    out = ROOT / "v10_verification.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(out), "imports_scan": result["imports_scan"], "failures": failures, "family": result["family"]["prime_count"], "mismatches": result["family"]["mismatch_count"], "direct": result["direct_ED2"]}, ensure_ascii=False, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
