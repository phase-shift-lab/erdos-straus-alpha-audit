# Technical Note: A Parameter-Compatibility Question in arXiv:2511.07465v1

## Purpose

This note presents a narrow, reproducible question about the connection between the ED2 parametrization and the lattice parameters in Dyachenko, [arXiv:2511.07465v1](https://arxiv.org/abs/2511.07465).

It is **not** a claim to solve or refute the Erdős–Straus conjecture. The intended request to a reviewer is simply: please identify any arithmetic or interpretive error in the calculation below.

## 1. Exact witness at P=17

Take

```text
(P, delta, b, c, A) = (17, 4, 2, 10, 5).
```

The ED2 identity is exact:

```text
4bc - b - c = 4*2*10 - 2 - 10 = 68 = 17*4 = P*delta.
```

The associated Egyptian-fraction decomposition is also exact:

```text
4/17 = 1/5 + 1/34 + 1/170.
```

The displayed gcd conditions are satisfied under the natural normalization:

```text
g = gcd(b,c) = 2
b' = b/g = 1
c' = c/g = 5
gcd(b',c') = gcd(b',g) = gcd(c',g) = 1.
```

The square-free decomposition of `delta` is

```text
delta = 4 = alpha_sf * d_sf^2 = 1 * 2^2.
```

The lattice definitions instead give

```text
alpha_lat = gcd(g, b' + c') = gcd(2, 6) = 2
d_lat = g / alpha_lat = 1
alpha_lat * d_lat^2 = 2 != 4 = delta.
```

For this row, the natural gcd and the constructed scale `alpha_sf*d_sf` both equal `2`. Thus the mismatch is not removed by choosing between those two readings of `g`.

## 2. A second exact witness at P=37

The row

```text
(P, delta, b, c, A) = (37, 5, 5, 10, 10)
```

gives

```text
4/37 = 1/10 + 1/185 + 1/370
g = 5, (b',c') = (1,2)
(alpha_sf,d_sf) = (5,1)
(alpha_lat,d_lat) = (1,5)
alpha_lat*d_lat^2 = 25 != 5 = delta.
```

It also satisfies the displayed positivity, ordering, divisibility, and gcd conditions recorded in the audit.

## 3. Symbolic family

For every integer `t >= 1`, set

```text
P = 8t - 3
delta = t
b = t
c = 2t
A = 2t.
```

Then

```text
4bc - b - c = 8t^2 - 3t = t(8t - 3) = P*delta
```

and

```text
4/P = 1/(2t) + 1/(tP) + 1/(2tP).
```

For a prime `P > 3`, one has `g=t`, `(b',c')=(1,2)`, and `gcd(t,3)=1`. Therefore

```text
alpha_lat = 1
d_lat = t
alpha_lat*d_lat^2 = t^2,
```

which differs from `delta=t` whenever `t>1`. This is an algebraic family of valid decompositions, not a new solution family or an Erdős–Straus counterexample.

## 4. What the calculation does and does not establish

The calculation establishes a reproducible failure of the displayed compatibility assertion connecting the square-free and lattice quantities in version 1 of the paper.

It does not establish that:

- the Erdős–Straus conjecture is false or solved;
- the paper's existence conclusion has no alternative proof;
- the issue is new in the literature; or
- a complete repair of the later lattice argument is impossible.

The appropriate current label is **correction candidate; publication scope unverified**.

## 5. Independent verification

The repository includes a non-importing independent verifier using only the Python standard library. The recorded verification conditions are:

```text
imports_scan=false
failures=[]
v10_sha.all_ok=true
```

From the repository root:

```powershell
python .\v10_scan.py
python .\verify_v10.py
python .\sol-audit\independent_verify_sol_v10.py
```

## Question for an independent reader

Is there a misreading or omitted hypothesis in the calculation above, especially in the use of `g`, `alpha`, and `d'` in Theorem 9.21(I)? A brief correction or reference to a later version would be more than sufficient.

## Source and limitations

Primary source: [Dyachenko, arXiv:2511.07465v1](https://arxiv.org/abs/2511.07465).

The repository has not established the status of later versions, author corrections, broad prior art, or publication-level novelty. Those questions are separate from the arithmetic check reported here.
