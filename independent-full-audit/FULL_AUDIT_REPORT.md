# arXiv:2511.07465v1 独立全体監査報告

## 結論

**査読相当の判定は `REJECT AS PROOF / major mathematical revision required` である。**

Theorem 9.21 の無条件存在証明は成立していない。決定的なのは次の三点である。

1. Lemma 9.24 と Proposition 9.25 は、全仮定を満たす小さな厳密反例を持つ。
2. 固定指数アフィン格子の正密度は、非線形 ED2 等式を満たす点の存在を意味しない。
3. Appendix C は正規化式が代数的に誤り、Appendix D は全 P の被覆を明示的に条件付きとしている。

一方、`paper-candidate-pre-audit/` のパラメータ橋渡し補正式は一般式として正しい。しかしこれは Theorem 9.21 を修復しない。Erdős–Straus 予想も、P ≡ 1 (mod 4) に対する中心命題の真偽も、この監査では決着していない。

## 記号の分離

原文は `alpha` と `d'` を別の役割で再利用するため、ここでは次のように分ける。

- `alpha_sf, d_sf`: Section 7 の `delta = alpha_sf d_sf^2`、`g = alpha_sf d_sf`
- `alpha_lat := gcd(g, b' + c')`
- `d_lat := g / alpha_lat`: Lemma 9.22 の最小正対角周期

この分離なしに両者を同一視すると、原文の Theorem 9.21(I) の不整合を見落とす。

## F1 — Critical: Lemma 9.24 と Proposition 9.25 は偽

一次資料の [Lemmas 9.22–9.24 と Proposition 9.25](https://arxiv.org/html/2511.07465v1) は

`L = {(u,v) in Z^2 : u b' + v c' = 0 (mod g)}`

に対し、対角周期 `(d_lat,d_lat)` と各座標の合同条件だけで一つの対角軌道を特徴づけ、辺長がともに `d_lat` 以上の長方形は必ず L と交わるとする。

厳密反例は次である。

- `P=17, alpha_sf=1, d_sf=2, g=2, b'=1, c'=5`
- `delta=4, b=2, c=10, A=5`
- `4bc-b-c=68=P delta`
- `4/17 = 1/5 + 1/34 + 1/170`
- `alpha_lat=gcd(2,6)=2`, `d_lat=1`
- `L={(u,v):u+5v=0 (mod 2)}={(u,v):u+v is even}`

Lemma 9.24 について `p0=(0,0)` とすると、`d_lat=1` なので右辺の座標合同条件は L の全点を許す。しかし `(1,-1)` は L に属し、対角軌道 `{(m,m):m in Z}` には属さない。

Proposition 9.25 について

`R=[1,2) x [2,3)`

は高さ・幅がともに `1=d_lat` だが、唯一の整数点 `(1,2)` は L に属さない。よって `L intersect R` は空である。

原証明の誤りは、横座標と縦座標の合同類代表を独立に選んだ後、横座標から決めた一つのシフト整数 `m` が縦座標にも同時に合うと仮定した点にある。

正しい対角軌道の特徴づけは、例えば

`p0 + Z(d_lat,d_lat) = {(u,v): u-v=u0-v0 and u=u0 (mod d_lat)}`

である。一般の格子点を保証する粗い修正なら、一方の辺長を `g` 以上、他方を `1` 以上にできる。ただし、それでも得られるのは格子点だけであり、非線形 ED2 解ではない。

## F2 — Critical: 格子密度から ED2 解の存在は出ない

[Theorems 9.1–9.2 と Remark 9.4](https://arxiv.org/html/2511.07465v1) を合わせて読むと、Theorem 9.1 が数えるのは固定指数の合同類であり、Remark 9.4 自身も非線形恒等式

`(4b-1)(4c-1)=4P delta+1`

の解存在には外部入力が必要だと認めている。その外部入力は後段でも無条件には供給されていない。

必要条件だけを満たす偽陽性は容易に得られる。

- `P=73, delta=9, g=3, d_sf=3, m3=3, b=3, c=24`
- `b'=1, c'=8`, `gcd(b',c')=1`
- アフィン合同、`gcd(b,c)=g`、`d_sf | (b'+c')`、商の mod 4 条件、`delta | bc`、順序・A の範囲条件を満たす
- しかし `4bc-b-c=261` に対し `P delta=657`

したがって、アフィン類の正密度は真の ED2 解の正密度・非空性・定数平均探索時間のいずれも与えない。非線形等式を「追加条件」として残すなら同値性は循環的であり、その条件を外すなら偽陽性が残る。

## F3 — Major: Section 7 と Lemma 9.22 のパラメータ橋渡し

ED2 の仮定

`g=alpha_sf d_sf`, `delta=alpha_sf d_sf^2`, `b=g b'`, `c=g c'`

のもと、`S=b'+c'` と置く。`4bc-b-c=P delta` を `g` で割ると

`S=d_sf(4 alpha_sf b'c' - P)`

だから、`h=gcd(alpha_sf,P)` として

`alpha_lat = gcd(g,S) = d_sf h`,

`d_lat = g/alpha_lat = alpha_sf/h`.

従って

`delta = alpha_lat d_lat^2  iff  d_sf = alpha_sf/gcd(alpha_sf,P)`.

これは有限観察ではなく一般証明である。原文 Table 2 の最初の `P=2521` 行は

- `alpha_sf=1, d_sf=3, b'=4, c'=161`
- `g=3, delta=9, b=12, c=483, A=644`
- `alpha_lat=3, d_lat=1`
- `alpha_lat d_lat^2=3 != 9`

となり、掲載された正しい ED2 解自身が Theorem 9.21(I) の「consistent」という同一視を破る。

独立有限検算では 57,600 パラメータ組を走査し、8,712 件の ED2 整数行（うち `P` が素数の行 2,088 件）で補正式に失敗はなかった。これは実装確認であり、一般性は上の導出が担う。

## F4 — Major: Appendix C の正規化は成立しない

[Lemma C.1](https://arxiv.org/html/2511.07465v1) は

`d=gcd(b,c), a|d, d'=d/a, b'=b/d', c'=c/d'`

から `gcd(b',c')=1` とする。しかし定義だけで

`gcd(b',c') = d/(d/a) = a`

であり、`a=1` でない限り 1 にはならない。

さらに Appendix C で意図される素数 `a` が `P delta` と互いに素で、同時に `a|b,c` なら、`a` は `4bc-b-c` を割るが `P delta` を割らないため ED2 等式と矛盾する。例 `P=13, delta=3, a=2` は `a|(P+delta)` と `a=-1 (mod delta)` を満たすが、この同時要件を満たす raw ED2 pair は存在しない。

Lemma C.2 が示すのは有限列挙の停止だけであり、出力が一件以上あることではない。Proposition C.3 と Remark C.4 はそれぞれヒューリスティック・条件付きである。

## F5 — Major: Appendix D は無条件性を回復しない

Appendix D の逆点検査は、与えられた候補が ED2 恒等式を満たすかの厳密な iff 検査として有用である。しかし [Remark D.18](https://arxiv.org/html/2511.07465v1) は、すべての P に対する固定有限リストの存在保証を「conditional covering scheme」に対応させている。

また D.15.1 の Examples D.43–D.44 は、具体的な被覆データではなく「指定し、検証せよ」という未充填の指示である。D.17 の要約も有限被覆を条件付きと明記する。よって Appendix D は候補検査を与えるが、全 P に対する候補の存在を与えない。

## F6 — Minor: Lemma 8.5 の証明文は誤りだが修復可能

[Lemma 8.5](https://arxiv.org/html/2511.07465v1) は `A=aP` なら `P/A` が整数だと扱うが、実際は `P/A=1/a` であり一般に整数ではない。

ただし結論は別の一行で救える。分母を `A<=B<=C` と並べ、A が P の倍数なら三分母はすべて P 以上なので、右辺は高々 `3/P<4/P` で矛盾する。これは中心定理の破断原因ではない。

## 下流影響

- Lemma 9.24 と Proposition 9.25 の反例により、Corollary 9.26 から Theorem 9.21 へ進む明示的な無条件格子経路は使えない。
- パラメータ橋渡しだけ直しても、非線形集合の非空性は証明されない。
- Appendix C の修正だけでも同様である。
- Appendix D は条件付き被覆を実際に構成・検証しない限り無条件証明にならない。
- 論文中の個々の掲載 ED2 分解が正しいこととは両立する。有限個の正しい例は全 P の存在証明ではない。

## 採録可能性と必要修正

現在形の中心定理を保った採録は推奨できない。最低限、次が必要である。

1. Lemma 9.24、Proposition 9.25、Corollary 9.26 を撤回または正しい命題に置換する。
2. Section 7 と Section 9 の同名パラメータを分離し、上記 gcd 補正式を反映する。
3. アフィン合同類ではなく、非線形 ED2 集合が各 P で非空であることを新しい無循環の論証で示す。
4. Appendix C の raw pair、`a`、`alpha`、正規化を定義から作り直す。
5. Appendix D を使うなら、全剰余類を覆う具体的有限データと機械検証を提示する。
6. 修正版全体を独立検証し、中心定理・計算量・有限実験を別々に主張する。

独立した査読済み文献として Chamberland, *The Erdős–Straus Conjecture and the Structure of Primes*, [INTEGERS 26 (2026), A42](https://math.colgate.edu/~integers/aa42/aa42.pdf) がある。同論文は Type II 解の存在を素数の構造表示との iff に落とす一方、全素数がその表示を持つことは Conjecture 2 として残す。これは、Type II の構造的パラメータ化と全素数での存在証明を分離すべきことの外部確認にもなっている。

## 最終分類

| 対象 | 判定 |
|---|---|
| パラメータ橋渡し補正式 | **証明済み** |
| Lemma 9.24 | **反例により偽** |
| Proposition 9.25 | **反例により偽** |
| Theorem 9.2 / Corollary 9.3 の ED2 解保証 | **提示論証では未証明** |
| Appendix C の正規化 | **代数的に誤り** |
| Appendix D の全 P 被覆 | **条件付き・具体被覆なし** |
| Theorem 9.21 の命題自体 | **この監査では真偽未決、v1 では未証明** |
| Erdős–Straus 予想 | **影響なし、未解決のまま** |
| 補正式単独の新規性 | **未確定。初等的で単独論文には弱い可能性** |
| 監査・訂正ノートとしての価値 | **技術ノート候補。外部先行研究確認と人間査読が必要** |
