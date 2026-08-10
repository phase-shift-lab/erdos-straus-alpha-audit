# Candidate: exact ED2 square-free/lattice compatibility criterion

## Status

```text
candidate_status=paper_level_candidate_pre_audit
independent_final_audit=false
external_publication=false
author_contact=false
```

This is a pre-audit mathematical candidate, not a confirmed discovery, a proof of the Erdős--Straus conjecture, a refutation, or a publication/priority claim.

## Proposed main result

Let (P,\alpha,d,b',c') be positive integers and define

```text
g = alpha*d
b = g*b'
c = g*c'
delta = alpha*d^2
```

Assume the ED2 identity

```text
4*b*c - b - c = P*delta.
```

Define the lattice quantities

```text
alpha_lat = gcd(g,b'+c')
d_lat = g/alpha_lat.
```

Then, with (h=\gcd(\alpha,P)),

```text
alpha_lat = d*h
d_lat = alpha/h
```

and therefore

```text
delta = alpha_lat*d_lat^2
    iff d = alpha/gcd(alpha,P).
```

For prime (P), this is (d=\alpha) when (P\nmid\alpha), and (d=\alpha/P) when (P\mid\alpha) and (alpha) is square-free.

## Proof summary

Writing (s=b'+c'), the ED2 identity reduces to

```text
4*alpha*d*b'*c' - s = P*d.
```

Thus (s\equiv-Pd\pmod{\alpha d}), so

```text
gcd(alpha*d,s) = gcd(alpha*d,P*d) = d*gcd(alpha,P).
```

Dividing (g=\alpha d) by this gcd gives (d_{\rm lat}=\alpha/\gcd(\alpha,P)). Comparing the resulting lattice reconstruction with (\delta=\alpha d^2) gives the iff condition. The full proof, the exact diagonal-period statement, and family derivations are in `PROOF_DRAFT.md`.

## Why this can be a paper centre

The result is a general necessary-and-sufficient correction to the bridge between two parameter systems in the source ED2/lattice argument. It is not a single witness:

- it gives the exact lattice invariant for every constructed ED2 row;
- it gives an iff condition for when the source's identification is valid;
- it supplies infinite compatible and incompatible prime-progressions;
- it independently checks a source-displayed (P=2521) row satisfying the ED2 and source gcd conditions but failing the bridge;
- it states the minimum notation/quantifier repair and bounds the impact without claiming the entire existence argument is false.

The explicit arithmetic families are treated as structural witnesses and known-equivalence risks, not as standalone novelty claims.

## Source-level impact

The source's Theorem 7.3 template uses the constructed scale (g=\alpha d') and (\delta=\alpha(d')^2). Theorem 9.21(I) then defines a lattice (\alpha=\gcd(g,b'+c')), (d'=g/\alpha), and states consistency with the square-free representation. The criterion above shows that this consistency is an additional condition, not a consequence of the displayed ED2 identity.

For the source's own Table 2 row (P=2521,\alpha=1,d'=3,b'=4,c'=161):

```text
g=3, b=12, c=483, delta=9, A=644
gcd(b',c')=1
gcd(b',g)=gcd(c',g)=1
alpha_lat=gcd(3,165)=3
d_lat=1
alpha_lat*d_lat^2=3 != 9=delta.
```

The original unit-fraction identity remains exact. The result therefore isolates a parameter-bridge failure and does not by itself refute the Erdős--Straus conjecture or every possible repair of the source proof.

## Reproducibility

From this directory:

```powershell
python .\verify_candidate.py
```

Expected recorded fields:

```text
imports_scan=false
failures=[]
```

The verifier is a separate implementation and does not import the exploratory generator or the protected v10/Sol audit.

## Claim boundary

Allowed at this stop: “A theorem-level correction candidate for the ED2 square-free/lattice bridge was fixed in an independently verifiable pre-audit package.”

Not allowed at this stop: “new discovery confirmed,” “Erdős--Straus solved/refuted,” “proof referee-safe,” “no prior art,” or “accepted for publication.”
