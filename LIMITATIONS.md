# Scope and limitations

This repository is a reproducible mathematical audit. It is not a claim to
solve the Erdős–Straus conjecture and is not a peer-reviewed publication.

## Mathematical scope

- The main conclusion concerns the compatibility of the displayed
  square-free and lattice parameters in arXiv:2511.07465v1.
- P=17 and P=37 are arithmetic examples of a parameter mismatch under the
  displayed definitions. Their Egyptian-fraction decompositions remain
  valid.
- The explicit `P=8t-3` family is recorded through its algebraic identities.
  Finite scans do not prove infinitude of a prime subfamily.
- The full audit covers the central ED2 existence route and the stated
  Appendix C/D rescue paths. It does not establish that every unrelated ED1
  lemma or every proof route in the source fails.
- The audit identifies proof-route failures and a parameter correction; it does
  not prove that Theorem 9.21 itself is false.

## Literature scope

The following remain outside the bounded literature check in this repository:

- a complete survey of prior art or publication priority;
- independent confirmation by a journal referee or another mathematician;
- whether the source author intended a different meaning for a reused symbol.

The arXiv v1 history and the same Zenodo concept record were checked, and a
nearby 2026 Type II paper was reviewed for context. These checks do not amount
to a comprehensive literature review or a peer-review decision.

The project should therefore use `correction candidate`, `audit result`, and
`scope-limited` wording rather than `new discovery`, `proof`, or `disproof`.

## Computational scope

Every finite result must be accompanied by its exact bounds, Python version,
commit, and generated output. The current independent verifier uses a
different finite range from the original v10 scan, but neither range is a
universal proof.

## Integrity scope

The v10 artifacts and `SHA256SUMS_V10.txt` are treated as a protected set.
The generators now explicitly write deterministic LF output, and the
manifest has been reconciled with that representation. A fresh-clone and CI
run remain required before release.

## Publication scope

The recommended first release is a preliminary public GitHub repository. A
DOI, formal paper submission, author notification, or public forum post is a
separate step and requires a stable release candidate and human review.
