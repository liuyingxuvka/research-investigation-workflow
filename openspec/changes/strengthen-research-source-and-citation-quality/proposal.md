## Why

The previous research-tool comparison showed that the workflow can produce cautious, well-structured reports, but it can still miss high-value source classes and let citation/source mismatches reach the final artifact. This change hardens the existing SourceGuard, TraceGuard, LogicGuard, and research-investigation orchestration contracts so substantive reports cannot claim deep-research quality without source-role coverage, execution-chain review, and citation audit evidence.

## What Changes

- Add a final research quality gate to `research-investigation-workflow` before delivery.
- Add a source registry contract that carries source ids, source roles, support boundaries, and citation eligibility from discovery through final prose.
- Strengthen SourceGuard guidance to perform source-role coverage review and post-draft source-gap review.
- Strengthen TraceGuard guidance to track announcement-to-execution chains and safe wording boundaries for each important lead.
- Strengthen LogicGuard guidance to require citation/source consistency review and claim-to-source audit before final source-backed artifacts are marked complete.
- Add lightweight audit scripts for Markdown source markers and source-role coverage checks.
- Sync source skill folders and installed Codex skill folders after implementation.
- No breaking changes to the Guard-family boundaries: SourceGuard still plans source discovery, TraceGuard still reconstructs evidence chains, and LogicGuard still audits claim support.

## Capabilities

### New Capabilities

- `research-source-and-citation-quality`: Defines source registry, source-role coverage, execution-chain review, citation consistency, and final research quality gates for source-backed investigation artifacts.

### Modified Capabilities

- None. The existing repository specs are change-local; this change introduces a new capability contract for the next quality upgrade.

## Impact

- Affects `skills/research-investigation-workflow/SKILL.md` and its reference files.
- Affects installed `research-investigation-workflow` under the local Codex skills directory.
- Coordinates source and installed skill updates for SourceGuard, TraceGuard, and LogicGuard.
- Adds small deterministic audit helpers under the research workflow skill.
- Requires OpenSpec validation, skill validation, command-surface checks, FlowGuard process evidence, and focused regression prompts before completion.
