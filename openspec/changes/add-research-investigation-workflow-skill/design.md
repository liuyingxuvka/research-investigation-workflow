## Context

The project is a planning workspace for a new Codex skill, not a runnable app. The source materials define a thin orchestration layer over existing Guard-family workflows:

- TraceGuard owns messy case evidence, timelines, gaps, contradictions, and claim boundaries.
- LogicGuard owns durable formal source support, argument modeling, report synthesis, and final claim audit.
- FlowGuard owns workflow order, evidence freshness, stale-check review, and closure confidence.
- Research Investigation History Ledger owns cross-run workflow memory and artifact pointers, not factual proof.

The target installed skill path is `%USERPROFILE%\\.codex\\skills\research-investigation-workflow`. A synchronized project copy is useful because this workspace is not currently a Git repository and the installed skill directory is outside the project root.

## Goals / Non-Goals

**Goals:**

- Create an installable Codex skill with required frontmatter, UI metadata, and reference files.
- Keep `SKILL.md` concise and move detailed process guidance into one-level reference files.
- Encode hard boundaries that prevent a future Codex agent from merging TraceGuard Case Library with LogicGuard Source Library or treating history as evidence.
- Include a History Ledger convention for investigation preflight and postflight records.
- Validate the skill with `quick_validate.py` and a manual smoke review against the project acceptance criteria.

**Non-Goals:**

- No UI, database server, background service, or standalone application.
- No new reasoning engine.
- No scripts in version 1 unless validation proves deterministic file operations are needed.
- No duplication of sensitive source content in the History Ledger by default.

## Decisions

1. Install-first with project sync
   - Decision: Create the canonical skill under `%USERPROFILE%\\.codex\\skills`, then mirror it into `skills/research-investigation-workflow` in this project for local review.
   - Rationale: Codex discovers installed skills from the user skill directory, while the project still needs a local synchronized copy.
   - Alternative considered: Only create the project copy. Rejected because it would not satisfy the user's request to sync the installed local version.

2. Reference-first documentation split
   - Decision: Use `SKILL.md` for trigger, quick route, hard gates, and output contract; use `references/*.md` for detailed operational guidance.
   - Rationale: This follows skill-creator progressive disclosure and keeps active context small.
   - Alternative considered: Put the whole workflow in `SKILL.md`. Rejected because it would be harder to load selectively.

3. No version-1 scripts
   - Decision: Do not add History Ledger helper scripts yet.
   - Rationale: The roadmap says scripts are optional later, and the file format should stabilize first.
   - Alternative considered: Add ledger init/search/append scripts now. Deferred to avoid premature tooling around an unsettled schema.

4. Guard-family reuse boundary
   - Decision: The skill instructs future agents to check current TraceGuard, LogicGuard, and FlowGuard command surfaces before claiming implementation or run completion.
   - Rationale: The project explicitly requires reuse of existing workflows and up-to-date command surfaces.
   - Alternative considered: Embed a fixed complete command recipe. Rejected because command surfaces can evolve.

## Risks / Trade-offs

- Installed skill and project copy can drift -> Mitigate by mirroring after edits and comparing file hashes during validation.
- History Ledger may be mistaken for evidence -> Mitigate with repeated hard boundary language and output contract requirements.
- Future agents may overclaim from TraceGuard or LogicGuard diagnostics -> Mitigate by requiring explicit confidence, gaps, assumptions, and claim-boundary sections.
- No scripts means ledger operations remain manual in v1 -> Accept for first version; document future script candidates only as later work in project artifacts, not inside the skill folder.
