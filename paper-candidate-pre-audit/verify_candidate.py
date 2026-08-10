"""Independent pre-audit verifier for the ED2 compatibility candidate.

This file intentionally has no project-local imports. It uses a separate
trial-division prime test, direct ED2 enumeration, exact Fraction checks,
symbolic-family instantiations, and source-table rows.
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


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    q = 3
    while q * q <= n:
        if n % q == 0:
            return False
        q += 2
    return True


def squarefree_factor(n):
    kernel = 1
    root = 1
    q = 2
    remainder = n
    while q * q <= remainder:
        exponent = 0
        while remainder % q == 0:
            remainder //= q
            exponent += 1
        if exponent & 1:
            kernel *= q
        root *= q ** (exponent // 2)
        q += 1
    if remainder > 1:
        kernel *= remainder
    return kernel, root


def verify_template_row(P, alpha, d, bp, cp, label, require_primitive=True):
    g = alpha * d
    b = g * bp
    c = g * cp
    delta = alpha * d * d
    A = alpha * bp * cp
    s = bp + cp
    alpha_lat = gcd(g, s)
    d_lat = g // alpha_lat
    h = gcd(alpha, P)
    check(4 * b * c - b - c == P * delta, label + ":ed2", (P, alpha, d, bp, cp))
    check(
        Fraction(4, P)
        == Fraction(1, A) + Fraction(1, b * P) + Fraction(1, c * P),
        label + ":fraction",
        (P, alpha, d, bp, cp),
    )
    if require_primitive:
        check(gcd(bp, cp) == 1, label + ":primitive", (P, bp, cp))
    check(A <= b * P <= c * P, label + ":order", (P, A, b * P, c * P))
    check(
        alpha_lat == d * h,
        label + ":alpha_formula",
        {"actual": alpha_lat, "expected": d * h},
    )
    check(
        d_lat == alpha // h,
        label + ":d_formula",
        {"actual": d_lat, "expected": alpha // h},
    )
    check(
        g // gcd(g, s) == alpha // h,
        label + ":diagonal_period",
        {"actual": g // gcd(g, s), "expected": alpha // h},
    )
    check(
        (delta == alpha_lat * d_lat * d_lat) == (d == alpha // h),
        label + ":iff",
        {
            "delta": delta,
            "lattice": alpha_lat * d_lat * d_lat,
            "d": d,
            "rhs": alpha // h,
        },
    )
    return {
        "P": P,
        "alpha": alpha,
        "d": d,
        "b_prime": bp,
        "c_prime": cp,
        "g": g,
        "b": b,
        "c": c,
        "delta": delta,
        "A": A,
        "alpha_lat": alpha_lat,
        "d_lat": d_lat,
        "gcd_alpha_P": h,
        "source_gcd_conditions": gcd(bp, g) == 1 and gcd(cp, g) == 1,
        "compatible": delta == alpha_lat * d_lat * d_lat,
    }


def direct_rows(P_limit=400, bc_limit=180):
    rows = []
    for P in range(5, P_limit + 1):
        if P % 4 != 1 or not is_prime(P):
            continue
        for b in range(1, bc_limit + 1):
            for c in range(b, bc_limit + 1):
                numerator = 4 * b * c - b - c
                if numerator <= 0 or numerator % P:
                    continue
                delta = numerator // P
                if delta <= 0 or b * c % delta:
                    continue
                A = b * c // delta
                if A > b * P:
                    continue
                alpha, d = squarefree_factor(delta)
                g = gcd(b, c)
                if g != alpha * d:
                    continue
                bp = b // g
                cp = c // g
                row = verify_template_row(P, alpha, d, bp, cp, "direct")
                row["source_gcd_conditions"] = gcd(bp, g) == 1 and gcd(cp, g) == 1
                rows.append(row)
    return rows


def main():
    incompatible = []
    for t in range(1, 5000):
        P = 8 * t - 3
        if not is_prime(P):
            continue
        row = verify_template_row(P, t, 1, 1, 2, "incompatible_family")
        incompatible.append(row)
        if t > 1:
            check(not row["compatible"], "incompatible_family_mismatch", row)

    incompatible_alpha3 = []
    for u in range(0, 5000):
        P = 132 * u + 109
        if not is_prime(P):
            continue
        row = verify_template_row(P, 3, 1, 1, 12 * u + 10, "incompatible_alpha3")
        incompatible_alpha3.append(row)
        check(not row["compatible"], "incompatible_alpha3_mismatch", row)
        check(row["source_gcd_conditions"], "incompatible_alpha3_source_gcd", row)

    compatible = []
    for t in range(0, 5000):
        P = 60 * t + 37
        if not is_prime(P):
            continue
        row = verify_template_row(P, 2, 2, 1, 8 * t + 5, "compatible_family")
        compatible.append(row)
        check(row["compatible"], "compatible_family_expected", row)

    rows = direct_rows()
    check(len(rows) > 0, "direct_rows_nonempty", len(rows))
    check(
        all(r["alpha_lat"] == r["d"] * r["gcd_alpha_P"] for r in rows),
        "direct_alpha_formula_all",
    )
    check(
        all(r["d_lat"] == r["alpha"] // r["gcd_alpha_P"] for r in rows),
        "direct_d_formula_all",
    )
    check(
        all(r["compatible"] == (r["d"] == r["alpha"] // r["gcd_alpha_P"]) for r in rows),
        "direct_iff_all",
    )

    p37 = verify_template_row(37, 2, 2, 1, 5, "P37_compatible")
    check(p37["compatible"], "P37_compatible_row", p37)
    check(
        p37["delta"] == 8 and p37["alpha_lat"] == 2 and p37["d_lat"] == 2,
        "P37_values",
        p37,
    )

    source_rows = [
        (2521, 1, 3, 4, 161),
        (2521, 2, 7, 2, 159),
        (2521, 11, 1, 2, 29),
        (3529, 1, 1, 5, 186),
        (3529, 1, 2, 3, 307),
        (3529, 1, 13, 3, 296),
        (3529, 2, 5, 4, 111),
        (3529, 5, 2, 1, 181),
        (3529, 13, 3, 4, 17),
        (3529, 17, 4, 2, 26),
        (3529, 26, 5, 1, 34),
    ]
    source_checked = []
    for P, alpha, d, bp, cp in source_rows:
        source_checked.append(
            verify_template_row(
                P, alpha, d, bp, cp, "source_table", require_primitive=False
            )
        )
    check(
        source_checked[0]["delta"] == 9 and not source_checked[0]["compatible"],
        "source_P2521_row1",
        source_checked[0],
    )
    check(
        source_checked[1]["delta"] == 98 and not source_checked[1]["compatible"],
        "source_P2521_row2",
        source_checked[1],
    )
    check(
        source_checked[3]["compatible"],
        "source_P3529_row1_boundary",
        source_checked[3],
    )

    result = {
        "version": "paper-candidate-pre-audit-verifier-1",
        "imports_scan": False,
        "standard_library_only": True,
        "failures": failures,
        "scope": {
            "direct_prime_limit": 400,
            "direct_bc_limit": 180,
            "incompatible_family_t": "1..4999, prime P=8t-3",
            "incompatible_alpha3_u": "0..4999, prime P=132u+109",
            "compatible_family_t": "0..4999, prime P=60t+37",
        },
        "counts": {
            "direct_template_rows": len(rows),
            "incompatible_family_prime_rows": len(incompatible),
            "incompatible_alpha3_prime_rows": len(incompatible_alpha3),
            "compatible_family_prime_rows": len(compatible),
            "direct_compatible_rows": sum(1 for r in rows if r["compatible"]),
            "direct_incompatible_rows": sum(1 for r in rows if not r["compatible"]),
        },
        "P37_compatible": p37,
        "first_incompatible_family": incompatible[:8],
        "first_incompatible_alpha3": incompatible_alpha3[:8],
        "first_compatible_family": compatible[:8],
        "first_direct_rows": rows[:8],
        "source_table_rows": source_checked,
        "criterion": {
            "alpha_lat": "gcd(alpha*d,b_prime+c_prime) = d*gcd(alpha,P)",
            "d_lat": "alpha/gcd(alpha,P)",
            "compatibility_iff": "d = alpha/gcd(alpha,P)",
            "diagonal_period": "g/gcd(g,b_prime+c_prime) = alpha/gcd(alpha,P)",
        },
    }
    out = ROOT / "verification.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "output": str(out),
                "imports_scan": False,
                "failures": failures,
                "counts": result["counts"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
