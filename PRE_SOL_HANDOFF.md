# Pre-Sol handoff: v10 alpha compatibility candidate

## Stop status

停止点は Sol 監査直前。Sol、sol_review、Terra、fork、外部公開はこの goal では起動していない。既存 v2--v9、`outputs/erdos-straus-discovery/`、`outputs/erdos-straus-research/` は変更していない。

## Candidate status

`correction_possible_pre_audit`

P=37 と `P=8t-3` の ED2 行は有効な単位分数分解を与える。問題は、Dyachenko v1 の §7.2 の square-free `alpha` と Theorem 9.21 の lattice `gcd(g,b'+c')` を同じ記号で接続し、`delta=alpha*d'^2` とする主張である。P=37 では

```text
alpha_sf=5, d_sf=1,
alpha_lat=1, d_lat=5,
delta=5, alpha_lat*d_lat^2=25.
```

これは ESC の反証ではなく、P=37 の分解の反証でもない。

## Audit questions

1. v1 の Lemma 7.2 で `g` を `gcd(b,c)` から `alpha*d'` に再代入する意図を、記号を分けて再構成できるか。
2. Theorem 9.21(I) の `g,b',c'` が canonical gcd normalization を量化しているか、construction scale を量化しているか。
3. `delta=alpha_lat*d_lat^2` を追加仮定にすれば、Theorem 9.21 の格子部分と ED2 逆写像がつながるか。
4. Theorem 7.3 の「all solutions」が実際には restricted primitive template のみを記述していないか。
5. この内部訂正候補に先行する著者修正・v2・査読記録が存在するか。

## Reproduction commands

```text
python work/goal-iteration-10-alpha/v10_scan.py
python work/goal-iteration-10-alpha/verify_v10.py
```

Expected independent result:

```text
imports_scan=false
failures=[]
family prime rows=19622 (P<=1000000, P=5 mod 8, P>5)
family mismatches=19622
Theorem 9.21(I) displayed-gcd subfamily=9815, mismatches=9815
P37: delta=5, lattice prediction=25
```

## Files in this package

- `EXPLORATION_V10_ALPHA.md`: definitions, proof, branches, limits
- `v10_hypotheses.json`: 23 hypotheses with statuses and evidence
- `v10_scan.py`, `v10_scan.json`: construction scan
- `verify_v10.py`, `v10_verification.json`: non-importing independent verification
- `v10_candidate.md`, `v10_candidate.json`: correction candidate, not novelty claim
- `PRIOR_ART_V10.md`: source and known-equivalence assessment
- `PRE_SOL_HANDOFF.md`: this handoff
- `SHA256SUMS_V10.txt`: package integrity manifest

## Non-claims

- No new Erdos--Straus solution method is claimed.
- No refutation or resolution of the Erdos--Straus conjecture is claimed.
- No literature-wide priority or publication-level novelty is claimed before an independent audit.
