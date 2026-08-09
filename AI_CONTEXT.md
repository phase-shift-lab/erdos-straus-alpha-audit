# AI context: Erdős–Straus alpha-compatibility audit

## Project identity

- Local root: `C:\AI\projects\math\erdos-straus-alpha-audit`
- GitHub remote: `https://github.com/phase-shift-lab/erdos-straus-alpha-audit`
- Default branch: `main`
- Repository visibility: Public
- Purpose: reproducibly audit the compatibility between the square-free `alpha,d'` parameters and the lattice parameters in Dyachenko, arXiv:2511.07465v1.

## Current status

The v10 candidate is classified as:

`correction_confirmed_pre_publication_scope_unverified`

The independent Sol audit confirms a parameter-compatibility failure as written in the v1 text. P=17 and P=37 are valid Egyptian-fraction decompositions, but the lattice reconstruction does not equal `delta` under the displayed definitions. This is not an Erdős–Straus proof, disproof, solution, or literature-wide novelty claim.

The primary evidence is in `sol-audit/SOL_AUDIT_V10.md`. The v10 artifact integrity is recorded in `SHA256SUMS_V10.txt` and rechecked by `sol-audit/independent_verify_sol_v10.py`.

## Public-release status

The repository is Public and contains the preliminary, scope-limited GitHub release `v0.1.0-audit`. The public-facing materials are `PUBLIC_SUMMARY.md`, `REPRODUCE.md`, `LIMITATIONS.md`, `AI_DISCLOSURE.md`, `CITATION.cff`, `LICENSE`, `LICENSE-DOCS.md`, and `.github/workflows/verify.yml`.

The v10 generators explicitly write UTF-8 with LF line endings. The released verifier contract reports `imports_scan=false`, `failures=[]`, and `v10_sha.all_ok=true`. A fresh-clone and CI run remain required for any future release candidate, and no DOI or peer-reviewed-result claim should be made until human mathematical review and the remaining literature checks are complete.

## Reproduction

Run from the repository root:

```powershell
python .\v10_scan.py
python .\verify_v10.py
python .\sol-audit\independent_verify_sol_v10.py
```

Expected independent-verifier conditions:

```text
imports_scan=false
failures=[]
v10_sha.all_ok=true
```

The scripts use the Python standard library only. The scan and verifier regenerate JSON outputs; check `git diff` and the SHA manifest after changing or rerunning them.

## Collaboration rules

1. Treat the v10 audit files as the current record. Do not rewrite their mathematical claims or SHA-protected contents without an explicit task.
2. Keep claims precise: call the result a correction candidate or audit result, never a new ESC discovery or resolution.
3. Before changing files, state the scope and run the smallest relevant verifier afterward.
4. Do not delete files, publish externally, open issues/PRs, or push commits unless the current task explicitly requests it.
5. Put volatile experiments, raw experiments, and large private data outside the tracked artifact set or under ignored directories.
6. Use `README.md` for human-facing orientation, this file for cross-LLM context, and `AGENTS.md` for Codex-specific execution rules.

## Source and uncertainty

The primary source is [arXiv:2511.07465v1](https://arxiv.org/abs/2511.07465). A revised version, author correction, broad priority search, and publication-level novelty have not been established by this repository.
