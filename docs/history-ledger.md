# Research Investigation History Ledger

## Purpose

The History Ledger is the workflow memory for `research-investigation-workflow`.

It records how past investigations were conducted so future investigations can
reuse useful paths, avoid failed paths, and find related prior artifacts.

It is not an evidence database.

## Difference From Other Libraries

```text
TraceGuard Case Library:
  Stores case evidence and storylines.

LogicGuard Source Library:
  Stores formal reusable source support.

FlowGuard Logs:
  Store process validation and stale-evidence closure.

Research Investigation History Ledger:
  Stores run-level memory, reusable investigation strategy, and artifact links.
```

## Suggested Filesystem Shape

```text
.research-investigation-history/
  index.yaml
  runs/
    2026-05-31-example-topic/
      run.yaml
      summary.md
      linked_artifacts.yaml
      reusable_lessons.yaml
      unresolved_gaps.yaml
```

## Run Record Fields

`run.yaml` should include:

```yaml
run_id: 2026-05-31-example-topic
title: Example investigation
created_at: "2026-05-31T00:00:00Z"
status: completed
topic: example topic
user_goal: deep research report
report_type: research_report
evidence_policy:
  public_search: allowed
  local_search: ask_user
  internal_search: ask_user
  hypothesis_allowed: true
traceguard:
  case_library_root: path-or-null
  case_id: case-id-or-null
  important_gaps: []
logicguard:
  source_library_root: path-or-null
  model_paths: []
  promoted_source_ids: []
flowguard:
  closure_status: passed-or-partial-or-blocked
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
```

## Preflight Behavior

At the start of a new investigation:

1. Search `index.yaml` and run summaries for similar topics, entities, report
   types, or investigation patterns.
2. Return only reusable workflow guidance and artifact pointers.
3. Do not silently import old evidence as truth.
4. Ask or state when old internal material needs permission before reuse.

## Postflight Behavior

At the end of a run:

1. Add or update the run record.
2. Link TraceGuard cases and LogicGuard artifacts by path or id.
3. Record which search paths worked and which failed.
4. Record unresolved gaps.
5. Record whether the report reached the requested conclusion strength.
6. Record privacy labels so future agents know what can be reused.

## Privacy Rule

The ledger may mention internal artifact ids or paths, but should not duplicate
sensitive source content by default. It should point to the owning library or
file instead.

