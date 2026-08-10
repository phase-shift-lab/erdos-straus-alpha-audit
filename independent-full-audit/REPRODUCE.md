# 再現手順

リポジトリルート `C:\AI\projects\research\erdos-straus-alpha-audit` で実行する。

```powershell
python independent-full-audit\independent_verify_full_audit.py
```

期待する終了コードは 0。標準出力の要点は次のとおり。

```json
{"failures": [], "imports_scan": false, "input_unchanged": true, "result": "audit_result.json"}
```

詳細は `independent-full-audit/audit_result.json` に出力される。確認すべきフィールドは次である。

- `failures=[]`
- `imports_scan=false`
- `input_integrity.unchanged_since_start=true`
- `candidate_parameter_bridge.status="verified"`
- `source_claim_checks.lemma_9_24_and_proposition_9_25.status="refuted"`
- `source_claim_checks.affine_density_gap.status="verified_false_positive"`
- `source_claim_checks.appendix_c_normalization.status="normalization_claim_refuted"`

`input_integrity_start.json` は監査開始時に一度だけ次で作成した。既存ファイルがある場合、検証器は上書きを拒否する。

```powershell
python independent-full-audit\independent_verify_full_audit.py --write-start
```

検証器は既存のプロジェクト Python を import せず、既存 JSON の数学的結論を入力にしない。SHA manifest は入力保全の確認にだけ使う。
