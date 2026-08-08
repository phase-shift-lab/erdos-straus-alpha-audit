# v10: ED2 における alpha 二重定義の独立監査

## 0. 判定

本パッケージの暫定状態は `correction_possible_pre_audit` である。これは新しい Erdos--Straus 分解の発見、Erdos--Straus 予想の反証、または予想の解決を意味しない。

一次資料 v1 は、同じ `alpha` 記号を少なくとも次の二つの役割で使っている。

1. §7.2 / Lemma 7.2（PDF p.16）: `delta = alpha_sf*d_sf^2` の平方自由部分 `alpha_sf`。
2. Theorem 9.21(I)--(III)（PDF pp.27--28）: `alpha_lat = gcd(g,b'+c')`、`d_lat = g/alpha_lat`。

さらに Theorem 9.21(I) は、後者が前者と「consistent」で `delta = alpha*d'^2` になると明記する。P=37 の正の primitive ED2 行でこの等式が破れるため、少なくとも v1 の記号接続またはその追加主張には訂正が必要である。

## 1. 一次資料からの定義再導出

対象は [Dyachenko, arXiv:2511.07465v1](https://arxiv.org/abs/2511.07465) の本文だけとした。

- PDF p.16, Lemma 7.2: `g := gcd(b,c)`, `b=g b'`, `c=g c'` の後に、`delta=alpha*d'^2`（`alpha` square-free）を置き、さらに `g := alpha*d'` と書く。
- PDF p.17, Theorem 7.3: `alpha,d'` と `g=alpha*d'` による因数分解で「all solutions」を記述すると述べる。primitive 条件 `gcd(b',c')=1` も列挙される。
- PDF p.24, §9.6: §7.2 の構造として、square-free `alpha`、`g=alpha*d'`、`delta=alpha*d'^2` を再使用する。
- PDF p.27, Theorem 9.21(I): `alpha := gcd(g,b'+c')`、`d':=g/alpha` と定義し、「Theorem 7.3 の parametrization と consistent」で `delta=alpha*d'^2` と記す。
- PDF pp.27--28, Theorem 9.21(III)--Proposition 9.25: 同じ gcd 由来の `alpha,d'` を格子の対角周期に使う。

HTML版でも、§5 は `g=gcd(b,c)`、`b'=b/g,c'=c/g` と記し（HTML lines 230--249）、Lemma 7.2 は先に `g:=gcd(b,c)` と置いた後に `g:=alpha*d'` と書く（HTML lines 805--843）。Theorem 9.21(I) は `gcd(b,c)=d` と書いた直後に `g_b=gcd(b,g), g_c=gcd(c,g)` を使い、`alpha=gcd(g,b'+c')` として「consistent」と述べる（HTML lines 1466--1481）。このため v10 では、`g` の意図が canonical gcd か constructed scale かも監査対象に含めた。

したがって、曖昧さを避けるため、本監査では記号を次のように分離した。

```text
alpha_sf, d_sf   : delta = alpha_sf*d_sf^2, alpha_sf square-free
g                : canonical gcd(b,c), when the preceding normalization is used
b', c'           : b/g, c/g
alpha_lat        : gcd(g,b'+c')
d_lat            : g/alpha_lat
```

`delta = alpha_lat*d_lat^2` は lattice 定義から自動的には出ず、独立した compatibility condition として扱う。

## 2. 明示的な反例族

任意の整数 `t>=1` に対し、

```text
P = 8t - 3,
b = t, c = 2t, delta = t, A = 2t
```

と置くと、整数恒等式は

```text
4bc-b-c = 8t^2-3t = t(8t-3) = P*delta,
A = bc/delta = 2t,
```

であり、分数恒等式も

```text
4/P = 1/(2t) + 1/(tP) + 1/(2tP)
```

となる。`P` が素数で `P=8t-3>3` なら `P≡5 (mod 8)` かつ、正値・順序 `2t<tP<2tP` が成立する。

canonical gcd 正規化では

```text
g = gcd(t,2t) = t,
b' = 1, c' = 2,
alpha_lat = gcd(t,3) = 1,
d_lat = t.
```

最後の `gcd(t,3)=1` は、もし `3|t` なら `3|P=8t-3` となり、素数 `P>3` に反することから従う。したがって `t>1` の全素数族行で

```text
delta = t != t^2 = alpha_lat*d_lat^2.
```

Theorem 9.21(I) の追加表示条件 `gcd(b',g)=gcd(c',g)=1` まで要求する場合は、§5 の `g=gcd(b,c)` を自然に引き継いで `b'=1,c'=2,g=t` と読むので、`t` を奇数に制限すればよい。P=37 (`t=5`) はこの条件を満たし、`gcd(b',c')=1`、順序、`delta|bc`、`A<=bP` もすべて成立する。したがって本候補の直接反例は、偶数 t の表示上の不適合に依存しない。偶数 t を含む全素数族のスキャン結果は、基礎 ED2 恒等式に対する補助的な数値観察として別に扱う。

これは有限計算だけに依存しない。この族が Theorem 7.3 の square-free primitive template にも文字どおり入る場合は、`t` が square-free のときである。その場合 `alpha_sf=t,d_sf=1,g=t,b'=1,c'=2` となる。具体的には `P=13 (t=2)`、`P=37 (t=5)`、`P=101 (t=13)` などが該当する。従って、P=37 の失敗は非平方自由または非primitiveな選択では救済できない。

## 3. P=37 の完全な数値検証

```text
P = 37
(delta,b,c,A) = (5,5,10,10)
4bc-b-c = 185 = 37*5
(4b-1)(4c-1) = 19*39 = 741 = 4*37*5+1
g = gcd(5,10) = 5
(b',c') = (1,2), gcd(b',c')=1
(alpha_sf,d_sf) = (5,1)
(alpha_lat,d_lat) = (gcd(5,3), 5) = (1,5)
alpha_lat*d_lat^2 = 25 != delta=5
4/37 = 1/10 + 1/185 + 1/370
```

この行は正の分母を持つ有効な ED2 分解であり、格子パラメータの取り違えだけが失敗している。分解自体を反証する例ではない。

## 4. P=29 の補助的な g 再代入問題

本文 p.17 の worked example は `alpha=1,d'=2,b'=2,c'=4,g=2,b=4,c=8,delta=4` と書く。しかしこの表示では `gcd(b',c')=2`、`gcd(b,c)=4` であり、表示された `g=alpha*d'=2` は canonical `gcd(b,c)` ではない。これは P=37 の反例に依存しない補助証拠であり、§7.2 の「先に gcd と置いた g を後で scale として再代入する」記法を分離すべき理由になる。ただし、本パッケージの主候補は primitive な P=37 行で確定している。

## 5. 探索枝と判定

16件以上の仮説を `v10_hypotheses.json` に記録した。枝は次の四つである。

- A: 一次資料の記号・定義接続（A01--A05）
- B: `P=8t-3` 明示族の恒等式・素数条件・境界（B01--B06）
- C: テンプレート生成、直接 ED2 列挙、P=37/P=29 の独立検査（C01--C06）
- D: 記号分離、互換条件、定理への影響範囲、訂正候補（D01--D06）

### 実行結果

`v10_scan.py` は次を実行した。

| 対象 | 範囲 | 件数 | `delta != alpha_lat*d_lat^2` |
|---|---:|---:|---:|
| 明示族 | 素数 `P<=1,000,000`, `P≡5 mod 8`, `P>5` | 19,622 | 19,622 |
| うち Theorem 9.21(I) gcd条件も満たす行 | 同上、`t` odd | 9,815 | 9,815 |
| square-free template | `P<=2,000`, `alpha<=12`, `d<=12`, `b'<=30` | 845 | 599 |
| 直接 ED2 列挙 | `P<=200`, `b<=c<=250` | 80 | 57 |
| 有効行の重複除去後 | 上記の合併 | 20,468 | — |

`verify_v10.py` は別実装で次を再計算した。

- 素数族 19,622件、全件で分数恒等式・整数恒等式・順序・格子不整合を確認。Theorem 9.21(I) の表示 gcd 条件を満たす奇数 t の9,815件でも全件で不整合を確認。
- `t=1..10,000` の素数でない整数パラメータも恒等式だけを検査。
- 直接 ED2 列挙 `P<=200,b<=c<=120` で73行、うち51行が格子互換条件を満たさない。
- P=37 と本文 P=29 例を個別検査。
- `imports_scan=false`, `failures=[]`。

有限スキャンは無限性の根拠ではない。無限族については上の整数恒等式と、素数行での `3∤t` の推論を別に記録した。

## 6. 暫定的な修正案

最小の安全な修正は、本文全体で記号を分けることである。

1. `alpha_sf,d_sf` を square-free decomposition 専用にする。
2. `alpha_lat,d_lat` を格子周期専用にする。
3. `delta=alpha_lat*d_lat^2` は定義から削除し、必要なら追加仮定として明示する。
4. `g` が `gcd(b,c)` なのか、構成された scale `alpha_sf*d_sf` なのかを各節で固定し、再代入しない。
5. Theorem 7.3 の「all solutions」は、primitive normalization と上記 compatibility を含む正確な量化へ書き直す。

この修正で Proposition 9.25 の格子誤りや Theorem 9.21 の存在主張が自動的に救済されるとは主張しない。そこは別監査である。

## 7. 残る不確実性

- v1 の `g` が意図的に「構成 scale」として再定義された可能性はある。しかしその場合でも、Theorem 9.21(I) の `delta=alpha*d'^2` を導くための compatibility 証明が本文に必要である。
- Theorem 9.21 の lattice 条件がどの `g,b',c'` を実際に量化しているかは、PDFの記号崩れも含めて著者または最終監査で確認すべきである。
- これは訂正候補の再現可能性を示すものであり、既刊文献にないことや査読論文としての新規性を証明するものではない。

## 8. 停止点

本 goal は Sol 監査前で停止する。`PRE_SOL_HANDOFF.md` に監査項目を整理し、既存 v2--v9、`outputs/`、既存 SHA マニフェストは変更しない。
