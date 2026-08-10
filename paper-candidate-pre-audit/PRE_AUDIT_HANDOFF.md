# Pre-audit handoff

## Stop state

    candidate_status=paper_level_candidate_pre_audit
    independent_final_audit=false
    external_publication=false
    author_contact=false

This handoff deliberately stops before the final independent audit. It is not a publication, priority, acceptance, or no-prior-art assertion.

## Candidate to audit

The candidate is the exact ED2 square-free/lattice compatibility criterion:

    alpha_lat = d*gcd(alpha,P)
    d_lat = alpha/gcd(alpha,P)
    delta = alpha_lat*d_lat^2  iff  d=alpha/gcd(alpha,P)

The hypotheses and source boundary are recorded in HYPOTHESES.json. The self-contained proof is in PROOF_DRAFT.md. The proposed paper structure is in PAPER_OUTLINE.md.

The candidate is a correction to a parameter bridge, not a solution or refutation of the Erdős–Straus conjecture. The P = 2521 source-table row is a displayed structural check; the unit-fraction identity remains exact.

## Reproduction

From the package directory, run:

    python verify_candidate.py

Acceptance fields for this pre-audit package are:

    imports_scan=false
    failures=[]

The verifier uses only the Python standard library, performs its own prime test and direct enumeration, and does not import the exploratory generator, v10 verifier, or sol-audit.

Observed pre-audit run on 2026-08-09:

    exit_code=0
    imports_scan=false
    failures=[]
    direct_template_rows=134
    direct_compatible_rows=44
    direct_incompatible_rows=90
    compatible_family_prime_rows=1631
    incompatible_alpha3_prime_rows=1347

## Priority audit attacks

1. Re-derive the theorem from the exact quantifiers and variable bindings in the source’s Theorem 7.3, Lemma 7.2, Theorem 9.21(I), Lemma 9.22, and Proposition 9.25. Check whether a prime, square-free, coprime, or ordering hypothesis was silently omitted from this package.
2. Recompute every displayed source-table row from the source version and verify that the P = 2521 row is transcribed correctly, including b, c, delta, A, and all gcd conditions.
3. Determine whether the source uses d′ as a newly rebound lattice period rather than the constructed scale. If so, state the minimum notation or quantifier repair and check every downstream use.
4. Verify that the lattice diagonal period is the least positive t with g dividing t(b′+c′), and compare it with any Smith-normal-form or lattice-index convention used by the source.
5. Check all primitive, source-gcd, positivity, denominator-order, and exact unit-fraction conditions in both arithmetic-progression families. Do not treat a bounded prime scan as proof of infinitude; use the stated Dirichlet condition only after checking the progression gcd.
6. Search later arXiv versions, corrigenda, MathSciNet, zbMATH, Crossref, and the wider lattice/congruence literature for an equivalent gcd or diagonal-period theorem.
7. Apply a known-equivalence audit to the explicit families and test whether the theorem is an elementary corollary already implicit in a standard congruence-kernel lemma.
8. Audit the source proof downstream before saying that any theorem is false. The current package supports only a parameter-bridge correction candidate.

## Evidence inventory

- CANDIDATE.md: claim boundary and source-level impact.
- PROOF_DRAFT.md: theorem, proof, exact diagonal period, and two structural families.
- PAPER_OUTLINE.md: paper-centre proposal and non-claims.
- PRELIMINARY_PRIOR_ART.md: checked sources, searches, and unresolved novelty boundary.
- HYPOTHESES.json: machine-readable hypotheses and statuses.
- RESEARCH_LOG.md: chronological exploration record.
- verify_candidate.py and verification.json: independent reproducibility pair.
- SHA256SUMS.txt: package integrity manifest generated from the files after verification.

## Explicitly not started

- The final independent mathematical audit.
- Any external publication, repository write, author contact, issue, pull request, commit, or push.
- A claim that the source is wholly false.
- A claim that the candidate is a confirmed new discovery or accepted paper result.
