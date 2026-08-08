# Erdős–Straus alpha-compatibility audit

Dyachenko, arXiv:2511.07465v1 の ED2 パラメータ表示について、平方自由分解側の `alpha,d'` と格子側の `gcd(g,b'+c')` が同一の量として接続されている箇所を、整数計算・`Fraction`・独立 verifier で再検査した記録です。

## 結論の範囲

このリポジトリは、次の分類で保全しています。

`correction_possible_pre_audit` / Sol再監査後: `correction_confirmed_pre_publication_scope_unverified`

P=17 と P=37 では、単位分数分解自体は正しい一方、論文の表示どおりに計算した格子側の再構成値が `delta` と一致しません。P=17 は、指定した有限範囲で確認した最小の厳密例です。

これは新しい Erdős–Straus 解、予想の反証、予想の解決、または査読論文レベルの新規性を主張するものではありません。論文 v1 の記号・パラメータ互換性と証明経路に対する、再現可能な技術的訂正候補です。

## 公開準備の状態

現在は、GitHub Public化済みの予備監査リリース状態です。公開用の要約、再現手順、制限事項、AI開示、引用情報、ライセンス、CIを次の資料に分離しています。

- `PUBLIC_SUMMARY.md`: 公開用の結論、主張・非主張、P=17/P=37の表
- `REPRODUCE.md`: 再現コマンドと検証ゲート
- `LIMITATIONS.md`: 数学・先行性・計算・公開範囲の限界
- `AI_DISCLOSURE.md`: AI利用範囲と独立検証の位置づけ
- `CITATION.cff`: 引用情報
- `LICENSE` / `LICENSE-DOCS.md`: コードと文書のライセンス
- `.github/workflows/verify.yml`: v10と独立verifierのCI

Windows実行時のJSON改行コードによるSHA不一致を解消するため、v10の生成器はUTF-8・LF出力を明示しています。`v0.1.0-audit` はfresh cloneとCIで `imports_scan=false`、`failures=[]`、`v10_sha.all_ok=true` を確認したうえで公開しています。

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
- `PUBLIC_SUMMARY.md` / `REPRODUCE.md` / `LIMITATIONS.md`: 公開準備資料
- `CITATION.cff` / `AI_DISCLOSURE.md` / `LICENSE*`: 引用・AI開示・ライセンス
- `AI_CONTEXT.md`: Codex・Claude・他LLMで共有するプロジェクト状態
- `AGENTS.md`: Codex向けのプロジェクト固有ルール
- `.gitattributes`: 共有環境での改行コード規約

## Project layout and multi-LLM workflow

The canonical local root is:

```text
C:\AI\projects\math\erdos-straus-alpha-audit
```

Use `AI_CONTEXT.md` as the cross-LLM source of truth for project status, reproduction commands, and uncertainty. `AGENTS.md` contains only Codex-specific execution rules. Keep volatile experiments and private data outside the tracked artifacts or under the ignored `scratch/` and `private-data/` directories.

The repository is Public on GitHub as of the `v0.1.0-audit` preliminary release. A clean `git status` and the relevant verifier should be checked before future changes. Further public releases, issue/PR creation, and pushes remain separate actions requiring explicit authorization for their task.

## 一次資料

- [Dyachenko, arXiv:2511.07465v1 (abstract)](https://arxiv.org/abs/2511.07465)
- [Dyachenko, arXiv:2511.07465v1 (HTML)](https://arxiv.org/html/2511.07465v1)
- [Dyachenko, arXiv:2511.07465v1 (PDF)](https://arxiv.org/pdf/2511.07465)

本リポジトリは v1 に対するローカル監査記録です。改訂版、著者訂正、広範な先行研究、出版優先権は未確認です。論文への連絡や公開投稿の前に、別の数学者による内容確認と最新版・先行性の確認が必要です。
