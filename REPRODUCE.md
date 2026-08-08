# Reproduce the audit

The scripts use the Python standard library only. Run them from the
repository root.

## Environment

The supported preparation environment is Python 3.11 on Windows or Linux.
The code uses no third-party Python package. Record the actual Python version
when publishing a release:

```powershell
python --version
```

## Commands

```powershell
python .\v10_scan.py
python .\verify_v10.py
python .\sol-audit\independent_verify_sol_v10.py
```

`v10_scan.py` regenerates `v10_scan.json`.
`verify_v10.py` regenerates `v10_verification.json`.
The independent Sol verifier recomputes the audit and prints a JSON report;
it does not import either v10 scan script.

## Release acceptance conditions

The following fields are the contract, not merely the process exit code:

```text
v10_verification.json:
  imports_scan=false
  failures=[]

independent verifier report:
  imports_scan=false
  failures=[]
  v10_sha.all_ok=true
```

The independent verifier can print a report while returning a successful
process status, so inspect the JSON fields. A non-empty `failures` list is a
failed verification gate.

Before the LF-output fix, a Windows-generated working tree could report:

```text
failures=["v10_sha:v10_scan.json", "v10_sha:v10_verification.json"]
v10_sha.all_ok=false
```

The generators now explicitly write LF line endings. If this failure appears
again, inspect the raw file bytes and the complete `git diff` before changing
the manifest. A public tag or DOI still requires the contract to pass in a
fresh clone and CI.

## Fresh-clone check

For a release candidate, clone the exact commit into a new directory, run the
three commands above, and confirm that the generated files are deterministic:

```powershell
git diff --check
git status --short --branch
```

After intentional regeneration, review the complete diff and the v10
manifest. Do not silently update a SHA-protected artifact or manifest.

## Interpretation

The checks establish only the recorded arithmetic identities and bounded
enumerations. They do not establish the Erdős–Straus conjecture, invalidate
the paper as a whole, or establish priority.
