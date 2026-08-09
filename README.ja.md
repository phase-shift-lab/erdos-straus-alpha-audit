# Erdős–Straus alpha互換性監査

このリポジトリは、Dyachenko, [arXiv:2511.07465v1](https://arxiv.org/abs/2511.07465) におけるパラメータ互換性の主張を、再現可能な整数計算と独立 verifier で監査した記録です。

対象は、同じ `alpha` で表記される次の二つの量の接続です。

- ED2パラメータ表示の平方自由因子 `delta = alpha_sf * d_sf^2`
- 格子側の `alpha_lat = gcd(g, b' + c')` と `d_lat = g / alpha_lat`

## 現在の分類

`correction_confirmed_pre_publication_scope_unverified`

論文v1の表示どおりに計算すると、有効なED2分解に対して `delta = alpha_lat * d_lat^2` が成立しない例を独立に確認しています。これは論文の記号とパラメータ接続に関する技術的な訂正候補です。

これは次を主張するものではありません。

- Erdős–Straus予想の新しい解
- 予想の反例
- 予想の解決
- 世界初、既報なし、または査読論文レベルの新規性

## 小さい厳密例

```text
(P, delta, b, c, A) = (17, 4, 2, 10, 5)
4bc - b - c = 68 = 17 * 4
4/17 = 1/5 + 1/34 + 1/170
```

`g = gcd(b,c) = 2`、`(b',c') = (1,5)` とすると、

```text
平方自由側: (alpha_sf, d_sf) = (1, 2)
格子側:     (alpha_lat, d_lat) = (2, 1)
alpha_lat * d_lat^2 = 2 != delta = 4
```

この例では、`g` を自然な最大公約数と読む場合も構成スケールと読む場合も `g=2` になります。したがって、`g` の曖昧さだけでは不一致を解消できません。

P=37の例と一般族 `P=8t-3` の計算は [`TECHNICAL_NOTE.md`](TECHNICAL_NOTE.md) にまとめています。

## 再現方法

Python標準ライブラリだけで実行できます。リポジトリのルートで次を実行します。

```powershell
python .\v10_scan.py
python .\verify_v10.py
python .\sol-audit\independent_verify_sol_v10.py
```

独立 verifier の期待値は次です。

```text
imports_scan=false
failures=[]
v10_sha.all_ok=true
```

## 残る不確実性

この監査で確認できるのは、表示されたパラメータ接続に再現可能な不整合があることまでです。パラメータを分離すれば存在証明全体を修復できるか、改訂版や著者訂正があるか、広範な先行研究があるかは別途確認が必要です。

第三者からの確認では、P=17の計算または Theorem 9.21(I) の読み方に誤りがないかを指摘してもらうことを想定しています。
