# PRIOR ART — Sol V10独立監査

## 一次資料

- E. Dyachenko, *Constructive Proofs of the Erdős–Straus Conjecture for Prime Numbers of the Form P ≡ 1 (mod 4)*, arXiv:2511.07465v1, 14 Oct. 2025: <https://arxiv.org/abs/2511.07465>
- HTML本文: <https://arxiv.org/html/2511.07465v1>
- PDF: <https://arxiv.org/pdf/2511.07465v1>

## 独立に照合した箇所

| 箇所 | 本文上の役割 | 監査判断 |
|---|---|---|
| §5 Notation | `g=gcd(b,c)`、`b=b'g,c=c'g`、`alpha,d'` は `delta` の平方自由部・平方部 | Theorem 9.21(I) の未定義 `g` を読む第一候補。 |
| Lemma 7.2 | 冒頭で `g:=gcd(b,c)`、同じ文中で `g:=alpha d'` と再設定 | 両者の一致を仮定しなければ証明中の代入は成立しない。単純な記号上書き以上の前提欠落。 |
| Theorem 7.3 | `delta=alpha d'^2`、`g:=alpha d'` により「all solutions」を表示 | `gcd(b,c)=alpha d'` を満たさない有効ED2解を排除するため、全解性は本文どおりには成立しない。 |
| §7.2, P=29 | `alpha=1,d'=2,g=2,b'=2,c'=4,b=4,c=8` | 分解自体は正しいが、`gcd(b,c)=4`、`gcd(b',c')=2`。主候補とは別の内部不整合。 |
| §9.6 | `g:=alpha d'`, `delta:=alpha d'^2`、後段で `gcd(b,c)=g` | §7の構成スケールと実gcdを同一視している。 |
| Theorem 9.21(I) | `g_b,g_c,b',c'` の後、`alpha=gcd(g,b'+c')`, `d'=g/alpha` とし、Theorem 7.3 と consistent と主張 | P=17とP=37が明示条件を満たしつつ `delta != alpha d'^2`。整合性文は反例を持つ。 |
| Theorem 9.21(III) | 同じ格子由来 `alpha,d'` を対角周期と存在保証に利用 | §7とのパラメータ橋渡しは修正が必要。ただし今回の例は有効な分解なので存在結論そのものの反例ではない。 |

## 既存ローカル記録との区別

`goal-iteration-10-alpha` の探索記録は候補発見・有限走査の由来としてのみ参照した。上表の定義、P=17/P=37/P=29の算術、無限族の恒等式、判定はSol監査で再導出した。v2〜v9のローカル成果は先行文献とは扱わない。

## 先行性の限界

指定されたarXiv v1以外を対象に広範な文献検索、著者の後続版・撤回・修正履歴、第三者による既報訂正の網羅調査は実施していない。したがって「世界初」「未発表」は未確認である。現段階で言えるのは、指定一次資料v1の内部整合性に再現可能な訂正候補があることまでである。

## Dirichlet利用の切り分け

族 `P=8t-3` のうち Theorem 9.21(I) の表示gcd条件を満たすのは `t` が奇数、すなわち `P≡5 (mod 16)` の素数部分族である。この素数部分族の無限性を述べる場合は、`gcd(5,16)=1` に対する算術級数中の素数に関するDirichletの定理を用いる。有限走査から無限性を推論してはいない。
