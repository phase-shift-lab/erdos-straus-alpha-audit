# Preliminary prior-art and equivalence map

- Search date: 2026-08-09 (Asia/Tokyo)
- Status: preliminary; not a literature-wide novelty certificate
- Candidate classification: preliminary_novelty_not_refuted

## Primary sources checked

1. Dyachenko, arXiv:2511.07465v1, Constructive Proofs of the Erdős–Straus Conjecture for Prime Numbers with P ≡ 1 (mod 4).
   - URL: https://arxiv.org/abs/2511.07465
   - Checked locations: Theorem 7.3 and Lemma 7.2, source HTML around lines 815–843; source Table 2 around lines 950–1001; Theorem 9.21 and Lemma 9.22 around lines 1466–1538.
   - Relevant facts: the ED2 template sets g = alpha d′ and delta = alpha(d′)^2, and the later lattice description defines alpha = gcd(g, b′ + c′) and d′ = g / alpha as consistent. Table 2 supplies displayed rows for an independent bridge check.

2. Bello-Hernández, Benito, Fernández, arXiv:2606.10922v1, A Divisor Parametrization for the Erdős–Straus Conjecture.
   - URL: https://arxiv.org/abs/2606.10922
   - Relevant facts: divisor identities, Type I/II comparison, shifted-cubic language, a finite-parameter congruence-cover obstruction, and translation-invariant modular sieves. The searched text did not state the alpha/lattice criterion used here.

3. Bello-Hernández, Benito, Fernández, arXiv:1010.2035v2, On Egyptian fractions.
   - URL: https://arxiv.org/abs/1010.2035
   - Relevant facts: standard Type I/II parameter relations, finite-parameter cover limitations, and polynomial families. These are equivalence filters for the explicit families, not novelty support.

4. Elsholtz–Tao, Counting the number of solutions to the Erdős–Straus equation on unit fractions, J. Aust. Math. Soc. 94 (2013), 50–105.
   - URL: https://www.cambridge.org/core/product/D13779FD8A48851BDCC9C6E78CD283A1
   - Relevant fact: established solution-counting results; no direct match to the alpha/lattice bridge was found in the checked metadata and text snippets.

5. Bradford, arXiv:2602.11774v1, A solution to the Straus–Erdős conjecture.
   - URL: https://arxiv.org/abs/2602.11774
   - Relevant fact: adjacent Type I/II and gcd-based reductions. It is not used as proof support or acceptance evidence.

6. Ventas, arXiv:2605.04551v1, A Ceiling Continued Fraction Approach to the Erdős–Straus Conjecture: Heuristic finiteness of counterexamples.
   - URL: https://arxiv.org/abs/2605.04551
   - Relevant fact: an adjacent shifted-divisor/FCT construction; it does not state the criterion in this package.

7. Dyachenko, Zenodo record 10.5281/zenodo.18229826, Parametric Algorithms for the k-Modular Analog...
   - URL: https://zenodo.org/records/18229826
   - Relevant fact: an adjacent generalized k-modular framework. Because it is a deposited record rather than a checked peer-reviewed article, it is a prior-art warning, not publication-level validation.

## Exact-expression searches

The following searches were run against current web/arXiv indexes:

- "gcd(g,b'+c')" Erdős Straus
- "alpha = gcd(g" "b' + c'" Erdős Straus
- "delta=alpha" "d'" "Erdos-Straus" lattice
- "affine lattice" "Erdos-Straus" alpha
- "gcd(alpha,P)" "Erdos-Straus"
- "d = alpha" "Erdos-Straus" parametrization
- "alpha d^2" "Erdos-Straus"

The exact criterion was not found in the checked results. This supports only preliminary_novelty_not_refuted. It does not establish priority, absence from the full literature, or absence of a later source correction.

## Known-equivalence filter

- The P = 8t − 3 family from the prior audit is Type-II-shaped and is not a new result.
- The compatible P = 60t + 37 family is a fixed-congruence identity and is not claimed as novel by itself.
- The source-filter-compatible alpha = 3 family is retained as a structural separation witness, not as a standalone priority claim.
- The candidate, if retained after audit, is the exact necessary-and-sufficient correction theorem for the parameter bridge, its lattice-period consequence, and the source-table counterchecks.

## Required next literature checks

- Recheck all later versions and author corrigenda for arXiv:2511.07465.
- Search MathSciNet, zbMATH, Crossref, and journal indexes with the theorem’s invariant formulation, not only the source notation.
- Search lattice-period, Smith-normal-form, and congruence-kernel terminology outside the Erdős–Straus literature.
- Determine whether the result is an elementary corollary already implicit in a standard lattice lemma.
