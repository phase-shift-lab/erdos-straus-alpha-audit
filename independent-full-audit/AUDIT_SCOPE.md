# 独立全体監査の範囲

## 監査対象

- 一次資料: E. Dyachenko, *Constructive Proofs of the Erdős–Straus Conjecture for Prime Numbers of the Form P ≡ 1 (mod 4)*, [arXiv:2511.07465v1](https://arxiv.org/html/2511.07465v1)
- 版の固定: arXiv v1、2025-11-07 提出
- 監査日: 2026-08-10
- 中心命題: Theorem 9.21 の「すべての素数 P ≡ 1 (mod 4) に ED2 表現が存在する」という無条件主張
- 新候補: `paper-candidate-pre-audit/` の Section 7 と Section 9 のパラメータ橋渡し補正式

## 読んだ依存範囲

中心命題の真偽判定に必要な次の経路を対象とした。

1. Section 7 の ED2 恒等式・平方因子パラメータ化・掲載数値例
2. Section 8 の分母の P-倍数分類
3. Sections 9.1–9.12 の格子密度、アフィン類、非線形 ED2 条件、存在・計算量主張
4. Lemmas 9.22–9.24、Proposition 9.25、Corollary 9.26 から Theorem 9.21 への格子被覆経路
5. Appendix C の正規化・列挙経路
6. Appendix D の逆検査・有限被覆経路
7. arXiv と Zenodo における後続版・訂正の有無

これは中心定理と、その無条件性を支えると明記された全経路の監査である。一方、ED1 の全補題、全数表の再計算、実装が提示されていない大規模計算の再現、論文全行の文章校閲は対象外とした。

## 独立性

- SHA 保護された v10、`sol-audit/`、`paper-candidate-pre-audit/` は入力専用とした。
- 既存の検証 Python を import していない。
- 既存の `verification.json` 等を数学的証拠として読んでいない。
- 独立検証器は Python 標準ライブラリ、整数演算、`fractions.Fraction` のみを使う。
- 一次資料の定義から式を再導出し、反例を新規に構成した。

## 判定語

- **証明済み**: 一般式の導出が閉じており、有限計算に依存しない。
- **反例確認**: 命題の全仮定を満たし結論を破る厳密な整数例がある。
- **未証明**: 記載経路に欠落があるが、命題そのものの偽を示してはいない。
- **有限検算**: 実装・例の検査であり、一般証明の代用ではない。

## 非実施事項

著者への連絡、外部公開、issue/PR 作成、commit、push、査読済みとの表示は行っていない。
