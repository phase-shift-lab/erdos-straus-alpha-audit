# v10 prior-art and source assessment

## Primary source

Dyachenko, *Constructive Proofs of the Erdos-Straus Conjecture for Prime Numbers of the Form P congruent to 1 modulo 4*, [arXiv:2511.07465](https://arxiv.org/abs/2511.07465), v1.

Relevant locations:

- Lemma 7.2, PDF p.16: square-free `alpha` in `delta=alpha*d'^2`, and the `g:=alpha*d'` reset after `g:=gcd(b,c)`.
- Theorem 7.3, PDF pp.16--17: factorization description and the claim that all solutions are described.
- Section 9.6, PDF p.24: square-free `alpha`, `g=alpha*d'`, `delta=alpha*d'^2` are carried into the affine-lattice discussion.
- Theorem 9.21(I)--(III), PDF pp.27--28: `alpha=gcd(g,b'+c')`, `d'=g/alpha`, followed by the statement that this is consistent with `delta=alpha*d'^2`.
- Proposition 9.25, PDF p.28: the separate diagonal-lattice proposition; v10 does not re-audit its geometric proof.

## Exact comparison

The v1 text supports the following comparison:

| Quantity | Source role | v10 notation |
|---|---|---|
| square-free part of `delta` | §7.2, §9.6 | `alpha_sf` |
| square root of square part | §7.2, §9.6 | `d_sf` |
| `gcd(g,b'+c')` | Theorem 9.21(III) | `alpha_lat` |
| `g/alpha` | lattice diagonal period | `d_lat` |

P=37 gives `alpha_sf=5,d_sf=1` and `alpha_lat=1,d_lat=5`, while all ED2 and Fraction identities hold. Therefore the source-level assertion of compatibility is not a consequence of the displayed definitions.

## Known-equivalence filter

The explicit `P=8t-3` family is a standard Type-II-shaped/congruence identity. It is deliberately not proposed as a new solution family. The v10 candidate is only the parameter-definition mismatch and its effect on the stated proof route.

The local v9/sol-audit package, read without modification, also classifies the P=37 decomposition as a known Type II specialization and does not establish literature-wide novelty for a correction. That local record is context, not a primary source or a novelty certificate.

## Scope and uncertainty

No claim is made that no prior corrigendum, author revision, or independent discussion exists outside the supplied v1 source and the local read-only record. The candidate is therefore `correction_possible_pre_audit`, not `novelty_confirmed`.

The central audit question is whether the author intended `g` and `alpha` to be freshly defined construction parameters in each subsection. If so, the notation still needs separation and the compatibility statement needs a proof or an explicit added hypothesis. The v10 evidence does not by itself determine the minimal corrected theorem.
