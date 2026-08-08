# Project instructions

## Scope

This repository contains a reproducible mathematical audit, not a claim to solve the Erdős–Straus conjecture. Preserve the distinction between a verified arithmetic correction and a novelty claim.

## Before editing

- Check `git status --short --branch`.
- Read `AI_CONTEXT.md` and the relevant artifact before changing it.
- Do not alter SHA-protected v10 files unless the task explicitly names that change.
- Prefer small, reversible edits and explicit file paths.

## After editing

- Run the relevant Python verifier from the repository root.
- Confirm `imports_scan=false` and `failures=[]` when the verifier reports those fields.
- Check `git diff --check` and `git status`.
- Report changed files, commands, results, and remaining uncertainty.

## External actions

Do not delete, publish, create issues or pull requests, or push to GitHub unless the current user request explicitly authorizes that action. Keep the repository Private by default.
