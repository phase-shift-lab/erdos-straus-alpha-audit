# Erdős–Straus Alpha-Compatibility Audit

This repository contains a reproducible, scope-limited audit of a
parameter-compatibility assertion in Dyachenko,
[arXiv:2511.07465v1](https://arxiv.org/abs/2511.07465).

The audit concerns the connection between two quantities written with the
same `alpha` notation:

- the square-free factor in the ED2 parametrization,
  `delta = alpha_sf * d_sf^2`; and
- the lattice quantity `alpha_lat = gcd(g, b' + c')`, with
  `d_lat = g / alpha_lat`.

## Current classification

`correction_confirmed_pre_publication_scope_unverified`

The independent audit confirms that, under the displayed definitions in
version 1, the claimed compatibility
`delta = alpha_lat * d_lat^2` fails for valid ED2 decompositions. This is a
technical correction candidate concerning the paper's notation and parameter
bridge.

This repository does **not** claim:

- a new solution of the Erdős–Straus conjecture;
- a counterexample to the conjecture;
- a resolution of the conjecture;
- a correction of the entire paper; or
- literature-wide priority or publication-level novelty.

## Full-audit extension

The `independent-full-audit/` package extends the preliminary parameter audit
to the central ED2 proof route in arXiv:2511.07465v1. It records exact
counterexamples to Lemma 9.24 and Proposition 9.25, a false positive for the
affine-density argument, the corrected parameter bridge, and the remaining
gaps in Appendices C and D.

Its conclusion is deliberately narrow: the v1 proof route does not establish
Theorem 9.21. It is not a disproof of Theorem 9.21, the Erdős–Straus
conjecture, or the entire source paper. The full report remains a public
preprint-level audit artifact requiring human mathematical review.

See [`independent-full-audit/FULL_AUDIT_REPORT.md`](independent-full-audit/FULL_AUDIT_REPORT.md),
[`independent-full-audit/SOURCE_DEPENDENCY_MAP.md`](independent-full-audit/SOURCE_DEPENDENCY_MAP.md),
and [`independent-full-audit/REPRODUCE.md`](independent-full-audit/REPRODUCE.md).

## Public release status

The repository is Public on GitHub and contains the preliminary,
scope-limited release `v0.1.0-audit`. Public-facing material is separated
into the following files:

- [`PUBLIC_SUMMARY.md`](PUBLIC_SUMMARY.md): concise result and claim boundary.
- [`REPRODUCE.md`](REPRODUCE.md): reproduction commands and release gate.
- [`LIMITATIONS.md`](LIMITATIONS.md): mathematical, computational, and
  publication limitations.
- [`AI_DISCLOSURE.md`](AI_DISCLOSURE.md): AI-use disclosure and independent
  verification boundary.
- [`CITATION.cff`](CITATION.cff): citation metadata.
- [`LICENSE`](LICENSE) and [`LICENSE-DOCS.md`](LICENSE-DOCS.md): code and
  documentation licensing.
- [`.github/workflows/verify.yml`](.github/workflows/verify.yml): CI checks.
- [`independent-full-audit/`](independent-full-audit/): source-wide central
  proof-route audit, exact counterexamples, and independent verifier.
- [`paper-candidate-pre-audit/`](paper-candidate-pre-audit/): read-only input
  package for the parameter-bridge candidate used by the full audit.

## Small exact witness

The following row satisfies the displayed arithmetic conditions and gives a
valid Egyptian-fraction decomposition:

```text
(P, delta, b, c, A) = (17, 4, 2, 10, 5)
4bc - b - c = 68 = 17 * 4
4/17 = 1/5 + 1/34 + 1/170
```

With `g = gcd(b,c) = 2` and `(b',c') = (1,5)`:

```text
square-free parameters: (alpha_sf, d_sf) = (1, 2)
lattice parameters:     (alpha_lat, d_lat) = (2, 1)
alpha_lat * d_lat^2 = 2 != delta = 4
```

Here the natural gcd interpretation and the constructed scale both give
`g = 2`, so the discrepancy is not resolved by the ambiguity in the meaning
of `g`.

The independently checked `P=37` row is retained as a second example. The
full calculation and the general family are in
[`TECHNICAL_NOTE.md`](TECHNICAL_NOTE.md).

## Reproduction

The scripts use only the Python standard library. Run them from the
repository root:

```powershell
python .\v10_scan.py
python .\verify_v10.py
python .\sol-audit\independent_verify_sol_v10.py
python .\independent-full-audit\independent_verify_full_audit.py
```

The release gate is based on recorded fields, not only process exit codes:

```text
v10_verification.json:
  imports_scan=false
  failures=[]

independent verifier:
  imports_scan=false
  failures=[]
  v10_sha.all_ok=true

full audit verifier:
  imports_scan=false
  failures=[]
  input_integrity.unchanged_since_start=true
```

The independent verifier does not import `v10_scan.py` or `verify_v10.py` and
rechecks the v10 input hashes from the manifest. The generators explicitly
write UTF-8 with LF line endings so that the protected JSON outputs are
deterministic across supported environments.

## Repository map

- [`TECHNICAL_NOTE.md`](TECHNICAL_NOTE.md): concise English note for an
  independent mathematical reader.
- [`README.ja.md`](README.ja.md): Japanese companion orientation.
- [`EXPLORATION_V10_ALPHA.md`](EXPLORATION_V10_ALPHA.md): definitions,
  symbolic family, scan design, and limits.
- [`v10_scan.py`](v10_scan.py) / [`v10_scan.json`](v10_scan.json): construction
  scan and recorded output.
- [`verify_v10.py`](verify_v10.py) /
  [`v10_verification.json`](v10_verification.json): non-importing verification
  pass.
- [`sol-audit/`](sol-audit/): independent re-audit and verifier.
- [`SHA256SUMS_V10.txt`](SHA256SUMS_V10.txt): integrity manifest for the
  protected v10 inputs.

## Scope and remaining uncertainty

The preliminary audit establishes a reproducible mismatch in the displayed
parameter connection. The full audit additionally identifies failures in the
central ED2 existence route and its stated rescue paths. It does not establish
that every unrelated ED1 argument or every lemma in the source fails, and it
does not prove that the theorem statement itself is false.

The full audit contains a bounded check of the arXiv/Zenodo version state and
nearby Type II literature. It is not a comprehensive priority search and has
not received independent human confirmation. A DOI, formal paper submission,
author notification, or claim of publication-level novelty remains a separate
step.

The primary source is [Dyachenko, arXiv:2511.07465v1](https://arxiv.org/abs/2511.07465).
A reviewer is invited to identify any misreading in the `P=17` calculation or
in the interpretation of Theorem 9.21(I).
