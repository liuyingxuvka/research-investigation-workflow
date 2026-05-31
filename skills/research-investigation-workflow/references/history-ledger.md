# Research Investigation History Ledger

The History Ledger stores reusable workflow memory for investigation runs. It is not an evidence database and must not be cited as factual support.

Record reusable investigation strategy, not private report content. When working inside a skill/software repository, keep ledger records local-only and ignored unless the user explicitly asks to publish a sanitized sample.

## Default Location

Prefer a project-local root unless the user specifies another location:

```text
.research-investigation-history/
  index.yaml
  runs/
    <run-id>/
      run.yaml
      summary.md
      linked_artifacts.yaml
      reusable_lessons.yaml
      unresolved_gaps.yaml
```

Use a stable run id:

```text
YYYY-MM-DD-short-topic
```

Avoid sensitive names in run ids when the investigation is private.

## Preflight Search

At the start of a new investigation:

1. Check whether the ledger exists.
2. Search `index.yaml`, run summaries, reusable lessons, and unresolved gaps for similar topics, entities, report types, source policies, or methods.
3. Return only workflow guidance and artifact pointers.
4. Label any internal artifact pointers as permission-gated until current access is confirmed.

Preflight output:

```yaml
prior_run_matches: []
reusable_search_directions: []
reusable_artifacts: []
known_gaps: []
privacy_constraints: []
```

If no ledger exists, state that this is a first run and plan to create the ledger during postflight.

## Run Record

`run.yaml` should include:

```yaml
run_id: 2026-05-31-example-topic
title: Example investigation
created_at: "2026-05-31T00:00:00Z"
status: completed
topic: example topic
user_goal: deep research report
report_type: research_report
conclusion_strength_requested: evidence-backed finding
conclusion_strength_delivered: working hypothesis
evidence_policy:
  public_search: allowed
  local_search: ask_user
  internal_search: ask_user
  hypothesis_allowed: true
traceguard:
  case_library_root: path-or-null
  case_id: case-id-or-null
  model_paths: []
  logic_leads:
    - id: lead-id
      status: confirmed-or-gap-or-hypothesis
      reusable_search_direction: ""
  important_gaps: []
logicguard:
  source_library_root: path-or-null
  model_paths: []
  promoted_source_ids: []
  claim_to_source_matrix: path-or-null
  inline_citation_coverage: complete-or-partial-or-not-run
flowguard:
  closure_status: passed-or-partial-or-blocked-or-downgraded
  stale_checks: []
final_artifacts:
  main_report: path-or-null
  appendix: path-or-null
reusable:
  search_directions: []
  useful_queries: []
  failed_queries: []
  lessons: []
privacy:
  contains_internal_references: false
  safe_to_reuse_summary: true
  safe_for_git_or_github: false
```

## Linked Artifacts

Use `linked_artifacts.yaml` for pointers:

```yaml
traceguard_cases: []
traceguard_models: []
logicguard_sources: []
logicguard_models: []
reports: []
appendices: []
flowguard_logs: []
```

Use paths or ids, not copied source content.

## Reusable Lessons

Use `reusable_lessons.yaml` for investigation strategy:

```yaml
worked:
  - direction: ""
    why: ""
failed:
  - direction: ""
    why: ""
logic_leads:
  - lead: ""
    useful_support_route: ""
    useful_limiting_route: ""
    remaining_gap: ""
try_first_next_time: []
avoid_next_time: []
```

## Unresolved Gaps

Use `unresolved_gaps.yaml` for gaps that future runs should know:

```yaml
gaps:
  - id: gap-1
    description: ""
    needed_evidence: ""
    source_class: public-or-local-or-internal-or-permission-gated
    claim_impact: ""
    status: open
```

## Postflight

At the end of a run:

1. Add or update the run directory.
2. Update `index.yaml` with topic, date, status, privacy label, report type, artifact pointers, and reusable keywords.
3. Record useful and failed search directions.
4. Record reusable logic leads and whether support, limiting evidence, and execution evidence were found.
5. Record unresolved gaps.
6. Record requested versus delivered conclusion strength.
7. Record inline citation coverage and claim-to-source matrix pointer when available.
8. Record FlowGuard closure status.
9. Keep sensitive source content in owning systems, not in the ledger.

If postflight cannot be written, report the blocker and provide the intended record structure in the final appendix.
