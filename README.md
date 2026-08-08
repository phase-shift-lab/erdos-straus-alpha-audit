# Erdős–Straus alpha-compatibility audit

Dyachenko, arXiv:2511.07465v1 の ED2 パラメータ表示について、平方自由分解側の `alpha,d'` と格子側の `gcd(g,b'+c')` が同一の量として接続されている箇所を、整数計算・`Fraction`・独立 verifier で再検査した記録です。

## 結論の範囲

このリポジトリは、次の分類で保全しています。

`correction_possible_pre_audit` / Sol再監査後: `correction_confirmed_pre_publication_scope_unverified`

P=17 と P=37 では、単位分数分解自体は正しい一方、論文の表示どおりに計算した格子側の再構成値が `delta` と一致しません。P=17 は、指定した有限範囲で確認した最小の厳密例です。

これは新しい Erdős–Straus 解、予想の反証、予想の解決、または査読論文レベルの新規性を主張するものではありません。論文 v1 の記号・パラメータ互換性と証明経路に対する、再現可能な技術的訂正候補です。

## 主な数値例

P=37, `delta=5, b=5, c=10, A=10`:

```text
4/37 = 1/10 + 1/185 + 1/370
g = gcd(5,10) = 5, (b',c') = (1,2)
alpha_squarefree = 5, d_square = 1
alpha_lattice = gcd(5,1+2) = 1, d_lattice = 5
alpha_lattice*d_lattice^2 = 25 != delta = 5
```

Sol再監査では、より小さい P=17 の例も独立に確認しています。

```text
4/17 = 1/5 + 1/34 + 1/170
(delta,b,c,A) = (4,2,10,5)
alpha_squarefree = 1, d_square = 2
alpha_lattice = 2, d_lattice = 1
alpha_lattice*d_lattice^2 = 2 != delta = 4
```

## 再現方法

依存パッケージはなく、Python標準ライブラリだけを使います。リポジトリのルートで実行してください。

```powershell
python .\v10_scan.py
python .\verify_v10.py
python .\sol-audit\independent_verify_sol_v10.py
```

`verify_v10.py` は `v10_scan.py` を import せず、`imports_scan=false` と `failures=[]` を含む `v10_verification.json` を再生成します。Sol側の独立 verifier も探索器を import せず、v10成果物のSHA256を再照合します。

## ファイル構成

- `EXPLORATION_V10_ALPHA.md`: 探索設計、定義、恒等式、棄却・限界
- `v10_scan.py` / `v10_scan.json`: 族・テンプレート・直接ED2行の走査
- `verify_v10.py` / `v10_verification.json`: 独立検証器と結果
- `v10_candidate.md` / `v10_candidate.json`: 訂正候補の主張と分類
- `PRIOR_ART_V10.md`: 一次資料と既知構造の照合
- `PRE_SOL_HANDOFF.md`: Sol監査前の引き継ぎ記録
- `SHA256SUMS_V10.txt`: v10成果物の完全性マニフェスト
- `sol-audit/`: gpt-5.6-sol/high による独立再監査と、その verifier

## 一次資料

- [Dyachenko, arXiv:2511.07465v1 (abstract)](https://arxiv.org/abs/2511.07465)
- [Dyachenko, arXiv:2511.07465v1 (HTML)](https://arxiv.org/html/2511.07465v1)
- [Dyachenko, arXiv:2511.07465v1 (PDF)](https://arxiv.org/pdf/2511.07465)

本リポジトリは v1 に対するローカル監査記録です。改訂版、著者訂正、広範な先行研究、出版優先権は未確認です。論文への連絡や公開投稿の前に、別の数学者による内容確認と最新版・先行性の確認が必要です。
