# v10 candidate: alpha compatibility correction

## Status

`correction_possible_pre_audit`

This is not claimed as a new discovery, a refutation of the Erdos--Straus conjecture, or a new Egyptian-fraction construction.

## Claim for audit

In arXiv:2511.07465v1, the square-free factor `alpha` in the ED2 parametrization and the lattice quantity `gcd(g,b'+c')` are used under the same symbol and are explicitly asserted to be consistent in Theorem 9.21(I). Under the displayed definitions, the assertion `delta=alpha*d'^2` is false for the valid primitive ED2 row

```text
P=37, delta=5, b=5, c=10, A=10,
g=5, b'=1, c'=2,
alpha_sf=5, d_sf=1,
alpha_lat=1, d_lat=5.
```

The ED2 and unit-fraction identities are exact, but `alpha_lat*d_lat^2=25`, not `delta=5`.

The failure extends algebraically to the family `P=8t-3`, `b=t`, `c=2t`, `delta=t`, `A=2t`; for prime `P>3`, `alpha_lat=1`, `d_lat=t`, and the claimed value is `t^2`. Under the natural reading `g=gcd(b,c)` inherited from §5, the additional displayed conditions `gcd(b',g)=gcd(c',g)=1` in Theorem 9.21(I) hold when `t` is odd; P=37 is in this restricted subfamily. Resolving whether that natural reading is the author's intended one is itself part of the audit.

## Classification

- Mathematical status: explicit correction candidate for v1 notation/compatibility claim.
- Novelty claim: false/not made.
- ESC status: unchanged; every displayed family row is a valid decomposition.
- Known structure: the `P=8t-3` decomposition is a standard congruence/Type-II-shaped identity and is not presented as new.
- Audit target: whether the paper intended two distinct `g`/`alpha` systems and whether Theorem 9.21 can be repaired by an explicit compatibility hypothesis or a restricted quantifier.

## Reproducibility

```text
python work/goal-iteration-10-alpha/v10_scan.py
python work/goal-iteration-10-alpha/verify_v10.py
```

The independent verifier reports `imports_scan=false` and `failures=[]`.
