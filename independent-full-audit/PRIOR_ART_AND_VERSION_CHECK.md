# 版・訂正・先行研究の確認

確認日: 2026-08-10

## 版の状態

- [arXiv abstract page](https://arxiv.org/abs/2511.07465) の Submission history は v1（2025-11-07）の一件のみだった。
- arXiv の related DOI は [10.5281/zenodo.17062748](https://doi.org/10.5281/zenodo.17062748) である。
- Zenodo API で concept record `17062747` の全版を照会した結果、record `17062748` の一件のみだった。したがって、確認時点で同一 Zenodo concept 内に後続版はない。
- 後発の関連一般化 [Zenodo record 18229826](https://zenodo.org/records/18229826) は見つかったが、2511.07465 の corrigendum として登録された資料ではない。本監査ではその別論文の数学内容を監査していない。

確認できた範囲では、arXiv v2、同一 Zenodo concept の改訂版、明示的 corrigendum は存在しない。

## 補正式の先行研究

次の式・語句を組み合わせて検索した。

- `alpha=gcd(g,b'+c')`
- `d'=g/alpha`
- `b'+c'`, diagonal period, Erdős–Straus, ED2
- arXiv ID、題名、著者名と correction/corrigendum

この限定検索では、監査で導出した

`alpha_lat=d_sf gcd(alpha_sf,P)`,

`d_lat=alpha_sf/gcd(alpha_sf,P)`

を独立に述べる先行資料は確認できなかった。ただし、これは新規性証明ではない。MathSciNet、zbMATH、専門家による引用追跡、非英語文献、未索引資料まで網羅していない。

直接関連する査読済み文献として、Marc Chamberland, *The Erdős–Straus Conjecture and the Structure of Primes*, [INTEGERS 26 (2026), A42](https://math.colgate.edu/~integers/aa42/aa42.pdf) を確認した。同論文は 2026-02-25 受理、2026-04-03 公開で、Type II 解が存在するための別形式の iff 条件を Theorem 1 で与える。その一方、すべての素数がその条件を満たすという部分は Conjecture 2 として明示的に未解決のまま残す。この文献に本監査の `alpha_lat, d_lat` の完全に同じ式は見つからなかったが、Type II 構造定理という広い主題の新規性は既に狭い。

[Erdős Problems #242](https://www.erdosproblems.com/242) も 2026 年の確認時点で問題を Open と表示している。2026 年にも解決を主張する arXiv preprint は存在するため、「主張がある」ことと「数学界で解決済みと確認された」ことは分けた。

## 出版レベルの暫定評価

補正式そのものは一行の gcd 計算で導け、近接する Type II iff 文献もあるため、単独の研究論文としては内容が小さい可能性が高い。一方、原論文の中心依存経路に対する複数の厳密反例、最小修正、再現可能な監査をまとめた訂正・批判的技術ノートには学術的価値があり得る。

外部提出前に必要なのは、より広い先行研究調査、原著者版の再確認、人間の数論研究者による独立査読である。
