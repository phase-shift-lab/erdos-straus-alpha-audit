# Public summary: alpha-compatibility audit

## Status

This is a preliminary, scope-limited audit of the ED2 parameter bridge in
Dyachenko, [arXiv:2511.07465v1](https://arxiv.org/abs/2511.07465). It is not a
proof or disproof of the Erdős–Straus conjecture.

The current project classification is:

```text
correction_confirmed_pre_publication_scope_unverified
```

The repository records a reproducible parameter-compatibility correction
candidate. It does not claim a new Erdős–Straus solution, a refutation of the
conjecture, a correction of the whole paper, or literature-wide novelty.

## Full-audit result

The 2026-08-10 full-audit package follows the central ED2 existence route in
the v1 source. It verifies, with exact arithmetic, that:

- Lemma 9.24 and Proposition 9.25 have explicit counterexamples;
- affine-lattice density contains points that fail the nonlinear ED2 identity;
- the square-free/lattice parameter bridge has the corrected gcd formula;
- Appendix C's normalization claim is algebraically inconsistent; and
- Appendix D supplies conditional checking machinery, not an unconditional
  covering for every P.

The narrow conclusion is that the v1 proof route does not establish
Theorem 9.21. This is not a disproof of the theorem statement, the
Erdős–Straus conjecture, or the whole paper. The detailed report and verifier
are in [`independent-full-audit/`](independent-full-audit/).

## Main result

For the displayed definitions in the v1 text, the square-free parameters and
the lattice parameters can give different reconstructions of `delta`, even
when the Egyptian-fraction identity and the displayed arithmetic conditions
hold.

| P | delta | b | c | A | fraction | square-free `(alpha,d')` | lattice `(alpha,d')` | lattice reconstruction |
|---:|---:|---:|---:|---:|---|---|---|---:|
| 17 | 4 | 2 | 10 | 5 | `4/17` | `(1,2)` | `(2,1)` | 2 != 4 |
| 37 | 5 | 5 | 10 | 10 | `4/37` | `(5,1)` | `(1,5)` | 25 != 5 |

For example:

```text
4/17 = 1/5 + 1/34 + 1/170
4/37 = 1/10 + 1/185 + 1/370
```

The independent audit also records the identity

```text
P = 8t - 3,  delta = t,  b = t,  c = 2t,  A = 2t
```

and derives the corresponding lattice reconstruction for prime `P > 3`.
The identity is an arithmetic audit result; finite computation is not being
used to infer an infinite prime theorem. Any infinitude statement for a
specified prime subfamily requires the stated number-theoretic theorem.

## What is verified

- The displayed P=17 and P=37 fractions are checked by exact integer and
  `Fraction` arithmetic.
- The ED2 and product identities are checked independently of the original
  scan code.
- The square-free and lattice parameter calculations are recomputed by a
  standard-library-only verifier that does not import `v10_scan.py` or
  `verify_v10.py`.
- The direct enumeration and the explicit family have bounded, recorded
  scopes. They are reproducibility evidence, not a proof of the
  Erdős–Straus conjecture.

## Current release gate

The `v0.1.0-audit` release passed the verifier contracts. The independent
verifier reports:

```text
imports_scan=false
failures=[]
v10_sha.all_ok=true

full-audit verifier:
  imports_scan=false
  failures=[]
  input_integrity.unchanged_since_start=true
```

An earlier Windows run exposed a line-ending sensitivity in the generated
JSON files. The two generators now write UTF-8 with LF line endings, and the
v10 manifest plus independent verifier expectations have been reconciled to
that deterministic representation. Future release candidates must rerun the
same gate from a fresh clone and in CI.

See [REPRODUCE.md](REPRODUCE.md) for the exact commands and
[LIMITATIONS.md](LIMITATIONS.md) for the scope boundaries.

## Source and prior-art boundary

The primary source audited here is [Dyachenko, arXiv:2511.07465v1](https://arxiv.org/abs/2511.07465).
The full audit records a bounded arXiv/Zenodo version check and nearby Type II
literature, but not a comprehensive priority search, independent human
confirmation, or publication-level novelty. The source PDF is linked, not
redistributed.
