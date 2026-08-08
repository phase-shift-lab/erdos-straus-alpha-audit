"""Independent-in-spirit scan for the alpha compatibility issue.

This file deliberately does not import any earlier exploration package.  It
constructs ED2 rows directly from integer identities, and writes only the
JSON result beside this file.
"""

from fractions import Fraction
from math import gcd, isqrt
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def sieve(limit):
    flags = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        flags[0] = 0
    if limit >= 1:
        flags[1] = 0
    p = 2
    while p * p <= limit:
        if flags[p]:
            flags[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
        p += 1
    return [n for n, flag in enumerate(flags) if flag]


def squarefree_data(n):
    """Return (squarefree_kernel(n), square_part_root(n))."""
    if n <= 0:
        raise ValueError("n must be positive")
    rest = n
    kernel = 1
    root = 1
    p = 2
    while p * p <= rest:
        exponent = 0
        while rest % p == 0:
            rest //= p
            exponent += 1
        if exponent & 1:
            kernel *= p
        root *= p ** (exponent // 2)
        p += 1 if p == 2 else 2
    if rest > 1:
        kernel *= rest
    return kernel, root


def analyze_row(P, b, c, delta, source, template_alpha=None, template_d=None,
                template_bp=None, template_cp=None):
    g_actual = gcd(b, c)
    bp_actual = b // g_actual
    cp_actual = c // g_actual
    alpha_sf, d_sf = squarefree_data(delta)
    if template_alpha is None:
        template_alpha = alpha_sf
    if template_d is None:
        template_d = d_sf
    if template_bp is None:
        template_bp = bp_actual
    if template_cp is None:
        template_cp = cp_actual
    g_template = template_alpha * template_d

    alpha_lat_actual = gcd(g_actual, bp_actual + cp_actual)
    d_lat_actual = g_actual // alpha_lat_actual
    alpha_lat_template = gcd(g_template, template_bp + template_cp)
    d_lat_template = g_template // alpha_lat_template

    numerator = 4 * b * c - b - c
    denominator_identity = (4 * b - 1) * (4 * c - 1)
    rhs_identity = 4 * P * delta + 1
    A_num = b * c
    A_integral = A_num % delta == 0
    A = A_num // delta if A_integral else None
    fraction_ok = Fraction(4, P) == Fraction(1, A) + Fraction(1, b * P) + Fraction(1, c * P) if A else False
    row_valid = (
        P > 2
        and P % 4 == 1
        and b > 0
        and c > 0
        and delta > 0
        and numerator == P * delta
        and denominator_identity == rhs_identity
        and A_integral
        and fraction_ok
    )
    return {
        "P": P,
        "b": b,
        "c": c,
        "delta": delta,
        "A": A,
        "source": source,
        "row_valid": row_valid,
        "ed2_residual": numerator - P * delta,
        "product_residual": denominator_identity - rhs_identity,
        "fraction_ok": fraction_ok,
        "ordered": bool(A and A <= b * P <= c * P),
        "g_actual": g_actual,
        "bp_actual": bp_actual,
        "cp_actual": cp_actual,
        "g_template": g_template,
        "bp_template": template_bp,
        "cp_template": template_cp,
        "alpha_squarefree": alpha_sf,
        "d_square": d_sf,
        "alpha_template": template_alpha,
        "d_template": template_d,
        "alpha_lattice_actual": alpha_lat_actual,
        "d_lattice_actual": d_lat_actual,
        "alpha_lattice_template": alpha_lat_template,
        "d_lattice_template": d_lat_template,
        "delta_from_actual_lattice": alpha_lat_actual * d_lat_actual * d_lat_actual,
        "delta_from_template_lattice": alpha_lat_template * d_lat_template * d_lat_template,
        "actual_lattice_consistent": delta == alpha_lat_actual * d_lat_actual * d_lat_actual,
        "template_lattice_consistent": delta == alpha_lat_template * d_lat_template * d_lat_template,
        "primitive_actual": gcd(bp_actual, cp_actual) == 1,
        "primitive_template": gcd(template_bp, template_cp) == 1,
        "theorem_I_gcd_conditions_actual": (
            gcd(bp_actual, g_actual) == 1
            and gcd(cp_actual, g_actual) == 1
        ),
        "theorem_I_gcd_values_actual": {
            "gcd_bp_g": gcd(bp_actual, g_actual),
            "gcd_cp_g": gcd(cp_actual, g_actual),
        },
        "g_reset_matches_actual": g_template == g_actual,
        "squarefree_template_matches": template_alpha == alpha_sf and template_d == d_sf,
    }


def family_row(P):
    if P % 8 != 5:
        raise ValueError("family requires P == 5 mod 8")
    t = (P + 3) // 8
    alpha, d = squarefree_data(t)
    row = analyze_row(
        P,
        t,
        2 * t,
        t,
        "explicit family P=8t-3, b=t, c=2t",
        template_alpha=alpha,
        template_d=d,
        template_bp=t // (alpha * d),
        template_cp=(2 * t) // (alpha * d),
    )
    row["t"] = t
    row["P_congruence"] = P % 8
    row["family_identity"] = (4 * t * (2 * t) - t - 2 * t) == t * P
    return row


def generated_template_rows(primes, alpha_limit=12, d_limit=12, bp_limit=30):
    rows = []
    squarefree_alphas = [a for a in range(1, alpha_limit + 1) if squarefree_data(a)[1] == 1]
    for P in primes:
        if P % 4 != 1:
            continue
        for alpha in squarefree_alphas:
            for d in range(1, d_limit + 1):
                g = alpha * d
                for bp in range(1, bp_limit + 1):
                    divisor = 4 * g * bp - 1
                    numerator = P * d + bp
                    if numerator % divisor:
                        continue
                    cp = numerator // divisor
                    if cp <= 0 or cp < bp or gcd(bp, cp) != 1:
                        continue
                    delta = alpha * d * d
                    b = g * bp
                    c = g * cp
                    row = analyze_row(
                        P, b, c, delta,
                        "enumerated squarefree template identity",
                        template_alpha=alpha,
                        template_d=d,
                        template_bp=bp,
                        template_cp=cp,
                    )
                    if row["row_valid"]:
                        rows.append(row)
    return rows


def brute_ed2_rows(primes, b_limit=250):
    """Small direct ED2 enumeration, independent of the template equation."""
    rows = []
    for P in primes:
        if P % 4 != 1:
            continue
        for b in range(1, b_limit + 1):
            for c in range(b, b_limit + 1):
                numerator = 4 * b * c - b - c
                if numerator <= 0 or numerator % P:
                    continue
                delta = numerator // P
                if delta <= 0 or (b * c) % delta:
                    continue
                A = (b * c) // delta
                if A > b * P:
                    continue
                row = analyze_row(P, b, c, delta, "direct ED2 enumeration")
                if row["row_valid"] and row["ordered"]:
                    rows.append(row)
    return rows


def dedupe(rows):
    out = []
    seen = set()
    for row in rows:
        key = (row["P"], row["b"], row["c"], row["delta"])
        if key not in seen:
            seen.add(key)
            out.append(row)
    return out


def main():
    family_prime_limit = 1_000_000
    template_prime_limit = 2_000
    brute_prime_limit = 200
    primes_family = sieve(family_prime_limit)
    primes_template = [p for p in primes_family if p <= template_prime_limit]
    primes_brute = [p for p in primes_family if p <= brute_prime_limit]

    family_rows = [family_row(p) for p in primes_family if p % 8 == 5 and p > 5]
    template_rows = generated_template_rows(primes_template)
    brute_rows = brute_ed2_rows(primes_brute)
    all_rows = dedupe(family_rows + template_rows + brute_rows)

    family_mismatches = [r for r in family_rows if r["row_valid"] and not r["actual_lattice_consistent"]]
    family_theorem_I_rows = [
        r for r in family_rows
        if r["row_valid"] and r["ordered"] and r["primitive_actual"] and r["theorem_I_gcd_conditions_actual"]
    ]
    family_theorem_I_mismatches = [r for r in family_theorem_I_rows if not r["actual_lattice_consistent"]]
    family_squarefree_template = [r for r in family_rows if r["squarefree_template_matches"] and r["primitive_template"]]
    template_mismatches = [r for r in template_rows if not r["template_lattice_consistent"]]
    brute_mismatches = [r for r in brute_rows if not r["actual_lattice_consistent"]]
    valid_rows = [r for r in all_rows if r["row_valid"]]

    result = {
        "version": "v10-alpha-scan-1",
        "scope": {
            "family_prime_limit": family_prime_limit,
            "family_prime_condition": "P prime, P == 5 (mod 8), P > 5",
            "template_scan": "P <= 2000, squarefree alpha <= 12, d <= 12, b' <= 30",
            "brute_scan": "P <= 200, b <= c <= 250, direct ED2 equation",
            "read_only_inputs": ["work/goal-iteration-09", "outputs/erdos-straus-discovery", "Fable5 pasted-text.txt"],
        },
        "counts": {
            "family_rows": len(family_rows),
            "family_lattice_mismatches": len(family_mismatches),
            "family_theorem_I_rows": len(family_theorem_I_rows),
            "family_theorem_I_lattice_mismatches": len(family_theorem_I_mismatches),
            "family_squarefree_primitive_rows": len(family_squarefree_template),
            "template_rows": len(template_rows),
            "template_lattice_mismatches": len(template_mismatches),
            "brute_rows": len(brute_rows),
            "brute_lattice_mismatches": len(brute_mismatches),
            "deduped_valid_rows": len(valid_rows),
        },
        "family_first_rows": family_rows[:12],
        "family_first_mismatches": family_mismatches[:12],
        "family_first_theorem_I_rows": family_theorem_I_rows[:12],
        "family_first_theorem_I_mismatches": family_theorem_I_mismatches[:12],
        "squarefree_primitive_examples": family_squarefree_template[:12],
        "template_first_mismatches": template_mismatches[:12],
        "brute_first_mismatches": brute_mismatches[:12],
        "boundary": {
            "P5_t1": family_row(5) if 5 in primes_family else None,
            "P13_t2": family_row(13) if 13 in primes_family else None,
            "P37_t5": family_row(37) if 37 in primes_family else None,
        },
        "claims_supported": [
            "For every integer t >= 1, b=t,c=2t,delta=t,A=2t gives an ED2 identity at P=8t-3.",
            "For prime P=8t-3 > 3, gcd(t,3)=1, so the lattice alpha is 1 and its d is t.",
            "For every prime family row with t>1, delta=t != alpha_lattice*d_lattice^2=t^2.",
            "For the subfamily satisfying Theorem 9.21(I)'s displayed gcd conditions, including P=37, the same mismatch remains.",
            "The squarefree alpha and lattice alpha cannot be identified in the scanned valid rows.",
        ],
        "caveats": [
            "The explicit family is a known Type-II-shaped decomposition; it is evidence of a correction, not a new ESC solution.",
            "Finite scans do not establish any literature-wide novelty claim.",
            "The paper may have intended g as a constructed scale rather than the preceding gcd; the v1 text still states both uses and an explicit consistency assertion.",
        ],
    }
    out = ROOT / "v10_scan.json"
    with out.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps({"output": str(out), "counts": result["counts"], "P37": result["boundary"]["P37_t5"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
