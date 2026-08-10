# Research log — paper-level candidate before final audit

## 2026-08-09 — setup and baseline

- Read GOAL_PAPER_LEVEL_EXPLORATION_SPEC.md and treated it as the work contract.
- Preserved the protected v10 files and sol-audit/ as read-only.
- Re-ran the protected verifier successfully: imports_scan = false, failures = [], and all ten v10 SHA checks passed.
- Confirmed that exploration writes are limited to work/paper-level-goal/ until the G1–G7 package is ready.

## Iteration 001 — source and equivalence map

- Read the source ED2 definitions, the square-free parameter statement, and the later lattice consistency statement.
- Checked classical Type I/II and divisor-parametrization literature for known-equivalence risks.
- Rejected a bounded identity and the P = 8t − 3 family as insufficient on their own: they are finite evidence or Type-II-shaped structure, not a paper-level candidate.

## Iteration 002 — exact criterion

- Research question: under g = alpha d, what is the exact condition for the lattice quantities to reproduce delta = alpha d^2?
- Derived from ED2:
  alpha_lat = d gcd(alpha,P),
  d_lat = alpha / gcd(alpha,P),
  delta = alpha_lat d_lat^2 if and only if d = alpha / gcd(alpha,P).
- Derived the exact least positive diagonal period of the lattice:
  g / gcd(g,b′ + c′) = alpha / gcd(alpha,P).
- Constructed compatible and incompatible arithmetic-progression families with source gcd filters.
- Independently checked direct bounded rows with exact Fraction arithmetic and checked displayed source-table rows, including the P = 2521 row that fails the bridge while retaining the ED2 identity.
- Corrected two verifier test-design issues before accepting the run: the boundary t = 1 case and a nonprimitive displayed source row.

## Literature and claim decision

- The exact expression search did not refute the criterion in the checked sources.
- No priority, no-prior-art, acceptance, or author-correction claim is made.
- The result is retained as a theorem-level correction candidate because it is all-quantified, has an if-and-only-if condition, gives the exact lattice invariant, and isolates a source-level impact.

## Package decision

The candidate package is now fixed in paper-candidate-pre-audit/. The independent final audit, external publication, and author contact remain false and are intentionally not started. The package is a handoff for a future audit, not a final proof certificate.
