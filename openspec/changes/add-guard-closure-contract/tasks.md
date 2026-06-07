## 1. Closure Helper

- [x] Add `scripts/research_closure_check.py`.
- [x] Update research skill closure guidance.

## 2. Validation

- [x] Run helper smoke checks.
- [x] Run existing helper checks or focused tests.
- [x] Run FlowGuard project audit after edits.

## 3. Sync

- [x] Sync installed research-investigation-workflow skill folder.
- [x] Record verification evidence and remaining gaps.

## Verification Evidence

- Research helper `py_compile` checks: passed.
- `python skills/research-investigation-workflow/scripts/research_closure_check.py --json`: partial report smoke passed with next actions.
- `python .flowguard/guard_closure_contract/run_checks.py`: passed.
- `python -m flowguard project-audit --root .`: passed with FlowGuard 0.40.12.
- Installed skill hash check: source and local `.codex/skills` copies match.
