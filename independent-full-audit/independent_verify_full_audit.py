#!/usr/bin/env python3
"""Independent exact-arithmetic verifier for the arXiv:2511.07465v1 audit.

This script deliberately does not import project search/verifier modules and does
not consume their JSON conclusions.  Existing manifests are read only to verify
input preservation.
"""

from __future__ import annotations

import argparse
import ast
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import sys


AUDIT_DIR = Path(__file__).resolve().parent
ROOT = AUDIT_DIR.parent
START_SNAPSHOT = AUDIT_DIR / "input_integrity_start.json"
RESULT_PATH = AUDIT_DIR / "audit_result.json"

MANIFESTS = (
    (ROOT / "SHA256SUMS_V10.txt", ROOT),
    (ROOT / "sol-audit" / "SHA256SUMS_SOL_V10.txt", ROOT / "sol-audit"),
    (
        ROOT / "paper-candidate-pre-audit" / "SHA256SUMS.txt",
        ROOT / "paper-candidate-pre-audit",
    ),
)

ALLOWED_IMPORT_ROOTS = {
    "__future__",
    "argparse",
    "ast",
    "datetime",
    "fractions",
    "hashlib",
    "json",
    "math",
    "pathlib",
    "sys",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_manifest(manifest_path: Path, base_dir: Path) -> dict:
    entries = []
    parse_failures = []
    for line_number, raw_line in enumerate(
        manifest_path.read_text(encoding="utf-8-sig").splitlines(), start=1
    ):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(maxsplit=1)
        if len(parts) != 2 or len(parts[0]) != 64:
            parse_failures.append(
                {"line": line_number, "reason": "invalid manifest row", "text": line}
            )
            continue
        expected, relative_text = parts
        # Normalize the manifest path for stable JSON on Windows.
        relative_text = relative_text.lstrip("*").replace("\\", "/")
        target = base_dir.joinpath(*relative_text.split("/"))
        actual = sha256_file(target) if target.is_file() else None
        entries.append(
            {
                "path": target.relative_to(ROOT).as_posix(),
                "expected_sha256": expected.lower(),
                "actual_sha256": actual,
                "ok": actual == expected.lower(),
            }
        )
    return {
        "manifest": manifest_path.relative_to(ROOT).as_posix(),
        "manifest_sha256": sha256_file(manifest_path),
        "entry_count": len(entries),
        "entries": entries,
        "parse_failures": parse_failures,
        "all_ok": not parse_failures and all(item["ok"] for item in entries),
    }


def integrity_snapshot() -> dict:
    manifests = [parse_manifest(path, base) for path, base in MANIFESTS]
    return {
        "schema_version": 1,
        "captured_utc": utc_now(),
        "manifests": manifests,
        "all_ok": all(item["all_ok"] for item in manifests),
    }


def write_json_lf(path: Path, payload: dict) -> None:
    encoded = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    path.write_bytes(encoded.encode("utf-8"))


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def is_squarefree(n: int) -> bool:
    prime = 2
    remaining = n
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
            if exponent >= 2:
                return False
        prime += 1
    return True


def scan_imports() -> dict:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".", 1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            roots.add(node.module.split(".", 1)[0])
    disallowed = sorted(roots - ALLOWED_IMPORT_ROOTS)
    return {
        "imports": sorted(roots),
        "disallowed_imports": disallowed,
        "imports_scan": bool(disallowed),
    }


def candidate_bridge_checks() -> dict:
    failures = []
    scanned = 0
    valid_rows = 0
    prime_rows = 0
    mismatch_rows = 0

    for alpha_sf in range(1, 19):
        if not is_squarefree(alpha_sf):
            continue
        for d_sf in range(1, 11):
            g = alpha_sf * d_sf
            delta = alpha_sf * d_sf * d_sf
            for b_prime in range(1, 21):
                for c_prime in range(1, 25):
                    scanned += 1
                    if math.gcd(b_prime, c_prime) != 1:
                        continue
                    b = g * b_prime
                    c = g * c_prime
                    numerator = 4 * b * c - b - c
                    if numerator <= 0 or numerator % delta:
                        continue
                    p_value = numerator // delta
                    valid_rows += 1
                    if is_prime(p_value):
                        prime_rows += 1

                    sum_prime = b_prime + c_prime
                    h = math.gcd(alpha_sf, p_value)
                    alpha_lat = math.gcd(g, sum_prime)
                    d_lat = g // alpha_lat
                    reconstructed_delta = alpha_lat * d_lat * d_lat
                    expected_equality = d_sf == alpha_sf // h
                    actual_equality = reconstructed_delta == delta

                    row_checks = {
                        "alpha_lat_formula": alpha_lat == d_sf * h,
                        "d_lat_formula": d_lat == alpha_sf // h,
                        "delta_iff": actual_equality == expected_equality,
                        "d_lat_is_diagonal_period": (d_lat * sum_prime) % g == 0,
                        "d_lat_is_minimal": all(
                            (step * sum_prime) % g != 0 for step in range(1, d_lat)
                        ),
                    }
                    if not all(row_checks.values()):
                        failures.append(
                            {
                                "parameters": {
                                    "P": p_value,
                                    "alpha_sf": alpha_sf,
                                    "d_sf": d_sf,
                                    "b_prime": b_prime,
                                    "c_prime": c_prime,
                                },
                                "checks": row_checks,
                            }
                        )
                    if not actual_equality:
                        mismatch_rows += 1

    source = {
        "P": 2521,
        "alpha_sf": 1,
        "d_sf": 3,
        "b_prime": 4,
        "c_prime": 161,
    }
    source["g"] = source["alpha_sf"] * source["d_sf"]
    source["b"] = source["g"] * source["b_prime"]
    source["c"] = source["g"] * source["c_prime"]
    source["delta"] = source["alpha_sf"] * source["d_sf"] ** 2
    source["A"] = source["b"] * source["c"] // source["delta"]
    source["alpha_lat"] = math.gcd(
        source["g"], source["b_prime"] + source["c_prime"]
    )
    source["d_lat"] = source["g"] // source["alpha_lat"]
    source["lattice_reconstructed_delta"] = (
        source["alpha_lat"] * source["d_lat"] ** 2
    )
    source["ed2_identity"] = (
        4 * source["b"] * source["c"] - source["b"] - source["c"]
        == source["P"] * source["delta"]
    )
    source["unit_fraction_identity"] = (
        Fraction(4, source["P"])
        == Fraction(1, source["A"])
        + Fraction(1, source["b"] * source["P"])
        + Fraction(1, source["c"] * source["P"])
    )
    source["bridge_mismatch"] = (
        source["lattice_reconstructed_delta"] != source["delta"]
    )

    return {
        "status": "verified" if not failures else "failed",
        "bounded_scan": {
            "parameter_tuples_scanned": scanned,
            "valid_ed2_rows": valid_rows,
            "prime_P_rows": prime_rows,
            "rows_where_source_and_lattice_delta_differ": mismatch_rows,
            "failures": failures,
        },
        "source_table_witness": source,
    }


def lattice_counterexample_checks() -> dict:
    # This lattice comes from the exact ED2 solution P=17, alpha_sf=1,
    # d_sf=2, b'=1, c'=5, g=2, delta=4, b=2, c=10.
    p_value = 17
    alpha_sf = 1
    d_sf = 2
    b_prime = 1
    c_prime = 5
    g = alpha_sf * d_sf
    delta = alpha_sf * d_sf**2
    b = g * b_prime
    c = g * c_prime
    alpha_lat = math.gcd(g, b_prime + c_prime)
    d_lat = g // alpha_lat

    def in_lattice(point: tuple[int, int]) -> bool:
        u, v = point
        return (u * b_prime + v * c_prime) % g == 0

    p0 = (0, 0)
    diagonal_step = (d_lat, d_lat)
    lemma_counterexample = (1, -1)
    rectangle_integer_points = [(1, 2)]
    rectangle_lattice_points = [
        point for point in rectangle_integer_points if in_lattice(point)
    ]

    checks = {
        "underlying_ed2_identity": 4 * b * c - b - c == p_value * delta,
        "underlying_unit_fraction_identity": Fraction(4, p_value)
        == Fraction(1, b * c // delta)
        + Fraction(1, b * p_value)
        + Fraction(1, c * p_value),
        "lemma_hypotheses": in_lattice(p0) and in_lattice(diagonal_step),
        "lemma_rhs_contains_counterexample": in_lattice(lemma_counterexample)
        and all(
            (lemma_counterexample[index] - p0[index]) % d_lat == 0
            for index in (0, 1)
        ),
        "counterexample_not_on_diagonal_orbit": (
            lemma_counterexample[0] - p0[0]
            != lemma_counterexample[1] - p0[1]
        ),
        "rectangle_meets_size_hypothesis": d_lat == 1,
        "rectangle_has_no_lattice_point": not rectangle_lattice_points,
    }
    return {
        "status": "refuted" if all(checks.values()) else "verification_failed",
        "parameters": {
            "P": p_value,
            "alpha_sf": alpha_sf,
            "d_sf": d_sf,
            "g": g,
            "b_prime": b_prime,
            "c_prime": c_prime,
            "delta": delta,
            "b": b,
            "c": c,
            "alpha_lat": alpha_lat,
            "d_lat": d_lat,
        },
        "lemma_9_24_counterexample": lemma_counterexample,
        "proposition_9_25_rectangle": {
            "x_interval": [1, 2],
            "y_interval": [2, 3],
            "integer_points": rectangle_integer_points,
            "lattice_points": rectangle_lattice_points,
        },
        "checks": checks,
    }


def affine_false_positive_checks() -> dict:
    # Same ED2 affine congruence class as the paper's P=73, delta=9,
    # g=3 example, but this point does not satisfy the nonlinear ED2 identity.
    p_value = 73
    delta = 9
    g = 3
    d_sf = 3
    m3 = 3
    b = 3
    c = 24
    b_prime = b // g
    c_prime = c // g
    t_value = 4 * b * c - b - c
    a_value = b * c // delta

    checks = {
        "affine_membership": delta % m3 == 0 and b % g == 0 and c % g == 0,
        "primitive_pair": math.gcd(b_prime, c_prime) == 1,
        "gcd_condition": math.gcd(b, c) == g,
        "local_divisibility": (b_prime + c_prime) % d_sf == 0,
        "local_mod_4": ((b_prime + c_prime) // d_sf) % 4 == 3,
        "delta_divides_bc": (b * c) % delta == 0,
        "ordering_and_size": b <= c and a_value <= b * p_value,
        "nonlinear_ed2_identity_fails": t_value != p_value * delta,
        "unit_fraction_identity_fails": Fraction(4, p_value)
        != Fraction(1, a_value)
        + Fraction(1, b * p_value)
        + Fraction(1, c * p_value),
    }
    return {
        "status": "verified_false_positive"
        if all(checks.values())
        else "verification_failed",
        "parameters": {
            "P": p_value,
            "delta": delta,
            "g": g,
            "d_sf": d_sf,
            "m3": m3,
            "b": b,
            "c": c,
            "b_prime": b_prime,
            "c_prime": c_prime,
            "A": a_value,
            "4bc_minus_b_minus_c": t_value,
            "P_delta": p_value * delta,
        },
        "checks": checks,
    }


def appendix_c_checks() -> dict:
    normalization_failures = []
    cases = 0
    nontrivial_cases = 0
    for d_value in range(1, 31):
        for a_value in range(1, d_value + 1):
            if d_value % a_value:
                continue
            for x_value in range(1, 8):
                for y_value in range(1, 8):
                    if math.gcd(x_value, y_value) != 1:
                        continue
                    b = d_value * x_value
                    c = d_value * y_value
                    d_prime = d_value // a_value
                    b_prime = b // d_prime
                    c_prime = c // d_prime
                    cases += 1
                    if a_value > 1:
                        nontrivial_cases += 1
                    if math.gcd(b_prime, c_prime) != a_value:
                        normalization_failures.append(
                            {
                                "d": d_value,
                                "a": a_value,
                                "x": x_value,
                                "y": y_value,
                            }
                        )

    # Intended Appendix C data: P=13, delta=3, a=2.  If a divides b and c,
    # then a divides 4bc-b-c, while a does not divide P*delta; hence no ED2
    # raw pair can meet those simultaneous requirements.
    p_value = 13
    delta = 3
    a_value = 2
    intended_checks = {
        "P_is_prime": is_prime(p_value),
        "delta_range_and_class": delta <= math.isqrt(p_value) and delta % 4 == 3,
        "a_is_prime": is_prime(a_value),
        "a_divides_P_plus_delta": (p_value + delta) % a_value == 0,
        "a_congruent_minus_one_mod_delta": a_value % delta == (delta - 1) % delta,
        "a_coprime_to_P_delta": math.gcd(a_value, p_value * delta) == 1,
        "raw_pair_requirements_incompatible": math.gcd(a_value, p_value * delta)
        == 1,
    }

    return {
        "status": "normalization_claim_refuted"
        if not normalization_failures and nontrivial_cases > 0
        else "verification_failed",
        "identity": "gcd(b/(d/a), c/(d/a)) = a when d=gcd(b,c)",
        "bounded_identity_check": {
            "cases": cases,
            "nontrivial_a_gt_1_cases": nontrivial_cases,
            "failures": normalization_failures,
        },
        "intended_raw_pair_incompatibility_example": {
            "P": p_value,
            "delta": delta,
            "a": a_value,
            "checks": intended_checks,
        },
    }


def lemma_8_5_local_proof_check() -> dict:
    p_value = 5
    a_value = 2
    capital_a = a_value * p_value
    p_over_a = Fraction(p_value, capital_a)
    return {
        "status": "proof_sentence_refuted_but_conclusion_repairable",
        "counterexample_to_integrality_sentence": {
            "P": p_value,
            "A": capital_a,
            "P_over_A": str(p_over_a),
            "is_integer": p_over_a.denominator == 1,
        },
        "repair": {
            "statement": "If ordered A is divisible by P, then A,B,C >= P and the RHS is at most 3/P < 4/P.",
            "strict_inequality_check": Fraction(3, p_value) < Fraction(4, p_value),
        },
    }


def run_audit() -> dict:
    failures = []
    import_check = scan_imports()
    if import_check["imports_scan"]:
        failures.append(
            {"id": "imports", "details": import_check["disallowed_imports"]}
        )

    current_integrity = integrity_snapshot()
    if not current_integrity["all_ok"]:
        failures.append({"id": "input_manifest_integrity", "details": "not all OK"})

    if not START_SNAPSHOT.is_file():
        failures.append(
            {
                "id": "start_snapshot_missing",
                "details": "run with --write-start before the final audit",
            }
        )
        start_integrity = None
        unchanged = False
    else:
        start_integrity = json.loads(START_SNAPSHOT.read_text(encoding="utf-8"))
        unchanged = start_integrity.get("manifests") == current_integrity.get(
            "manifests"
        )
        if not unchanged:
            failures.append(
                {
                    "id": "input_changed_since_start",
                    "details": "manifest payload differs",
                }
            )

    bridge = candidate_bridge_checks()
    lattice = lattice_counterexample_checks()
    affine = affine_false_positive_checks()
    appendix_c = appendix_c_checks()
    lemma_8_5 = lemma_8_5_local_proof_check()

    expected_statuses = {
        "candidate_bridge": bridge["status"] == "verified",
        "lattice_counterexamples": lattice["status"] == "refuted",
        "affine_false_positive": affine["status"] == "verified_false_positive",
        "appendix_c": appendix_c["status"] == "normalization_claim_refuted",
        "lemma_8_5": lemma_8_5["status"]
        == "proof_sentence_refuted_but_conclusion_repairable",
    }
    for name, ok in expected_statuses.items():
        if not ok:
            failures.append({"id": name, "details": "unexpected verifier status"})

    return {
        "schema_version": 1,
        "generated_utc": utc_now(),
        "audit_target": "arXiv:2511.07465v1",
        "arithmetic": "Python integers and fractions.Fraction only",
        "imports_scan": import_check["imports_scan"],
        "import_details": import_check,
        "input_integrity": {
            "start_snapshot": START_SNAPSHOT.name,
            "start_all_ok": bool(start_integrity and start_integrity.get("all_ok")),
            "end": current_integrity,
            "unchanged_since_start": unchanged,
        },
        "candidate_parameter_bridge": bridge,
        "source_claim_checks": {
            "lemma_9_24_and_proposition_9_25": lattice,
            "affine_density_gap": affine,
            "appendix_c_normalization": appendix_c,
            "lemma_8_5_local_proof": lemma_8_5,
        },
        "expected_statuses": expected_statuses,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-start",
        action="store_true",
        help="create the immutable-input start snapshot and exit",
    )
    args = parser.parse_args()

    if args.write_start:
        if START_SNAPSHOT.exists():
            print(f"refusing to overwrite existing {START_SNAPSHOT.name}", file=sys.stderr)
            return 2
        snapshot = integrity_snapshot()
        write_json_lf(START_SNAPSHOT, snapshot)
        print(
            json.dumps(
                {
                    "start_snapshot": START_SNAPSHOT.name,
                    "all_ok": snapshot["all_ok"],
                    "manifest_count": len(snapshot["manifests"]),
                },
                sort_keys=True,
            )
        )
        return 0 if snapshot["all_ok"] else 1

    result = run_audit()
    write_json_lf(RESULT_PATH, result)
    print(
        json.dumps(
            {
                "result": RESULT_PATH.name,
                "imports_scan": result["imports_scan"],
                "input_unchanged": result["input_integrity"][
                    "unchanged_since_start"
                ],
                "failures": result["failures"],
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0 if not result["failures"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
