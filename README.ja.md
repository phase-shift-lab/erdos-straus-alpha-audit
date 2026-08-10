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

## 全体監査の追加

`independent-full-audit/` には、論文 v1 の中心 ED2 証明経路を対象にした
独立全体監査を収録しています。Lemma 9.24 / Proposition 9.25 の厳密反例、
アフィン格子密度の偽陽性、補正されたパラメータ橋、Appendix C/D の残る欠落を
記録しています。

結論は限定的です。v1 の証明経路では Theorem 9.21 は証明されていませんが、
Theorem 9.21 自体、Erdős–Straus 予想、論文全体の反証を主張するものではありません。
査読前の監査成果であり、第三者の数学的確認が必要です。

詳細は [`independent-full-audit/FULL_AUDIT_REPORT.md`](independent-full-audit/FULL_AUDIT_REPORT.md)、
再現手順は [`independent-full-audit/REPRODUCE.md`](independent-full-audit/REPRODUCE.md) を参照してください。

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
python .\independent-full-audit\independent_verify_full_audit.py
```

独立 verifier の期待値は次です。

```text
imports_scan=false
failures=[]
v10_sha.all_ok=true
```

全体監査 verifier では、さらに `input_integrity.unchanged_since_start=true`
を確認します。

## 残る不確実性

全体監査では、表示されたパラメータ接続に加えて、中心 ED2 存在経路と Appendix C/D
の問題を確認しています。ただし、論文中の無関係な全経路が失敗することや、定理自体が
偽であることまでは示していません。改訂版、著者訂正、広範な先行研究、人間による確認は
別途必要です。

第三者からの確認では、P=17の計算または Theorem 9.21(I) の読み方に誤りがないかを指摘してもらうことを想定しています。
