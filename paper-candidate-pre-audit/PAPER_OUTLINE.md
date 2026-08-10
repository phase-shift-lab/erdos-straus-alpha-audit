# Paper outline — draft only, not a submission

## Working title

The exact square-free/lattice compatibility condition in an ED2 parametrization of the Erdős–Straus equation

## Abstract draft

We analyze a parameter bridge arising in a recent ED2 parametrization of the Erdős–Straus equation. The construction writes g = alpha d, delta = alpha d^2, b = g b′, and c = g c′, while a later lattice description defines alpha_lat = gcd(g, b′ + c′) and d_lat = g / alpha_lat. Assuming only the displayed ED2 identity 4bc − b − c = P delta, we prove the exact identities

    alpha_lat = d gcd(alpha,P),
    d_lat = alpha / gcd(alpha,P).

Consequently, the asserted identification delta = alpha_lat d_lat^2 holds if and only if d = alpha / gcd(alpha,P). For prime P, this reduces to d = alpha unless P divides alpha. We give source-compatible infinite arithmetic-progression families on both sides of the criterion, independently verify the identities by exact integer and rational arithmetic, and check rows displayed in the source’s own numerical table. The result isolates a correction to the parameter bridge and the exact diagonal period of the associated lattice. It does not resolve the Erdős–Straus conjecture, and the status of the correction as a publication-level novelty claim remains subject to independent mathematical audit and broader literature review.

## Main theorem

Use the self-contained statement and proof in PROOF_DRAFT.md. State the constructed-scale hypothesis explicitly and distinguish it from the canonical gcd interpretation. The theorem should be presented for positive integers first; primality and square-freeness enter only in the specialization and in source-specific applications.

## Difference from known results

- The ED2 identity and Type I/II forms are known background.
- The explicit P = 8t − 3 and fixed-congruence families are not claimed as new.
- The proposed contribution is the exact gcd reduction for the lattice bridge, the if-and-only-if compatibility criterion, the exact diagonal period, and the source-level impact/correction boundary.
- Preliminary searches did not find the exact criterion, but this is not a priority certificate.

## Proof structure

1. Normalize the ED2 template and divide the identity by alpha d.
2. Reduce gcd(g, b′ + c′) modulo g to gcd(alpha d, P d).
3. Compute both lattice parameters and compare the reconstructed delta.
4. Identify the minimal diagonal period of the lattice.
5. Give compatible and incompatible prime-progression families, using Dirichlet’s theorem only for the infinitude of prime instances.
6. Audit displayed source rows and explain the minimum notation/quantifier repair.

## Computational role

verify_candidate.py is a support verifier, not a proof. It uses a separate implementation, standard-library exact arithmetic, a direct bounded enumeration, the two structural families, and source-table rows. It does not import the exploratory generator or any protected v10/Sol-audit artifact.

The recorded acceptance fields are imports_scan = false and failures = [].

## Required discussion in a paper

- Precisely state which source implication is invalid as written or requires an additional hypothesis.
- Separate the existence of valid unit-fraction rows from the consistency of the two parameter labels.
- State whether the source proof can be repaired by rebinding notation, by imposing the if-and-only-if condition, or only by changing a later argument.
- Include a complete later-version/corrigendum and literature search before any priority language.
- Treat all explicit families as structural witnesses unless a separate novelty proof survives the known-equivalence filter.

## Non-claims

- No claim that the Erdős–Straus conjecture is solved or refuted.
- No claim that the entire source theorem is false; only the displayed parameter identification is shown to require an extra condition or a notation repair.
- No claim of literature-wide priority, acceptance, or absence of an author correction.
