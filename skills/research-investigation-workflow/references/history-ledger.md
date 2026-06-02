# Research Investigation History Ledger

The History Ledger stores reusable workflow memory for investigation runs. It is not an evidence database and must not be cited as factual support.

Record reusable investigation strategy, not private report content. When working inside a skill/software repository, keep ledger records local-only and ignored unless the user explicitly asks to publish a sanitized sample.

For substantive investigations, record SourceGuard discovery strategy alongside TraceGuard, LogicGuard, and FlowGuard records. The ledger should remember useful search directions, failed routes, access gaps, and source-role coverage patterns, not private source contents or unverified claims.

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
reasoning_atlas:
  atlas_path: path-or-null
  status: complete-or-partial-or-blocked-or-reduced-or-not-run
  branch_tree:
    support_branches: []
    opposing_branches: []
    alternative_explanations: []
    confounders: []
    scope_or_temporal_branches: []
    stakeholder_branches: []
    falsifiers: []
    future_triggers: []
  debate_matrix_path: path-or-null
  model_lenses:
    - lens_id: lens-id
      lens_type: generic-or-domain-specific
      contribution: branch-or-warrant-or-evidence-need-or-limitation-or-falsifier
      final_use: reasoning-only-or-appendix-or-main-text
  expert_stance_map:
    status: mapped-or-not-needed-or-partial-or-blocked
    stance_families: []
  conclusion_tournaments:
    - claim_id: claim-id
      winner: preferred-or-alternative-or-unresolved-or-downgraded
      allowed_wording: ""
  anti_overfit_check:
    core_rules_generic: true
    domain_specific_items_kept_as_lenses_or_examples: []
sourceguard:
  state_path: path-or-null
  planned_actions: []
  completed_actions: []
  candidate_sources: []
  source_registry_path: path-or-null
  source_registry_status: complete-or-partial-or-blocked-or-not-run
  source_role_coverage:
    claim_origin: complete-or-gap-or-not-run
    direct_or_original_facts: complete-or-gap-or-not-run
    source_statements: complete-or-gap-or-not-run
    scope_boundaries: complete-or-gap-or-not-run
    execution_or_outcome_evidence: complete-or-gap-or-not-run
    context_or_motive_evidence: complete-or-gap-or-not-run
    expert_or_analyst_interpretation: complete-or-gap-or-not-run
    counter_or_limiting_evidence: complete-or-gap-or-not-run
    future_trigger_conditions: complete-or-gap-or-not-run
  source_role_coverage_quality:
    required_roles_checked: []
    important_gaps: []
    downgrade_reason: ""
  access_gaps: []
  handoff_to_traceguard: []
  handoff_to_logicguard: []
traceguard:
  case_library_root: path-or-null
  case_id: case-id-or-null
  model_paths: []
  logic_leads:
    - id: lead-id
      status: confirmed-or-gap-or-hypothesis
      reusable_search_direction: ""
  evidence_role_map:
    claim_origin: ""
    direct_or_original_facts: []
    source_statements: []
    scope_boundaries: []
    execution_or_outcome_evidence: []
    context_or_motive_evidence: []
    expert_or_analyst_interpretation: []
    counter_or_limiting_evidence: []
    future_trigger_conditions: []
  minimum_rounds:
    original_fact: complete-or-gap-or-not-run
    counter_limiting: complete-or-gap-or-not-run
    impact_execution: complete-or-gap-or-not-run
    stakeholder: complete-or-gap-or-not-run
    future_trigger: complete-or-gap-or-not-run
    downgrade_reason: ""
  execution_chains:
    - lead_id: lead-id
      announcement_or_claim: ""
      implementation_evidence: []
      outcome_or_impact_evidence: []
      stakeholder_evidence: []
      counter_delay_or_non_occurrence: []
      status: complete-or-partial-or-gap-or-not-applicable
      safe_wording: ""
      unsafe_wording: ""
  competing_storylines:
    - storyline_id: storyline-id
      status: supported-or-candidate-or-contradicted-or-gap
      safe_wording: ""
      next_evidence_need: ""
  counterfactual_traces:
    - trace_id: trace-id
      proposed_cause: ""
      counterfactual_question: ""
      weakest_link: ""
      claim_impact: ""
  confounder_ledger:
    - confounder: ""
      branch_id: ""
      evidence_status: ""
      claim_impact: ""
  important_gaps: []
logicguard:
  source_library_root: path-or-null
  model_paths: []
  promoted_source_ids: []
  claim_to_source_matrix: path-or-null
  inline_citation_coverage: complete-or-partial-or-not-run
  citation_consistency_audit:
    status: passed-or-partial-or-blocked-or-not-run
    undefined_markers: []
    duplicate_markers: []
    source_role_mismatches: []
    bibliography_only_claims: []
    rerun_required_after_edits: false
  conclusion_tournament_audit:
    status: passed-or-qualified-or-unresolved-or-blocked-or-not-run
    preferred_conclusions: []
    steelman_oppositions: []
    live_alternatives: []
    robustness_notes: []
flowguard:
  closure_status: passed-or-partial-or-blocked-or-downgraded
  stale_checks: []
final_artifacts:
  main_report: path-or-null
  appendix: path-or-null
  final_research_quality_gate:
    research_reasoning_atlas: complete-or-partial-or-blocked-or-reduced
    branch_tree: complete-or-partial-or-blocked-or-reduced
    debate_and_alternatives: complete-or-partial-or-blocked
    model_lenses: selected-and-used-or-not-needed-or-partial-or-decorative-only-blocked
    expert_stance_map: mapped-or-not-needed-or-partial-or-blocked
    conclusion_tournament: passed-or-qualified-or-unresolved-or-blocked
    source_registry: complete-or-partial-or-blocked
    source_role_coverage: complete-or-partial-or-blocked
    minimum_rounds: complete-or-partial-or-blocked-or-downgraded
    execution_or_evidence_chain: complete-or-partial-or-blocked-or-not-applicable
    claim_to_source_matrix: complete-or-partial-or-blocked
    citation_consistency: passed-or-partial-or-blocked
    reader_limitation_placement: passed-or-partial-or-blocked
    allowed_claim_strength: ""
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
sourceguard_states: []
sourceguard_exports: []
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
  sourceguard:
  useful_source_actions:
    - action: ""
      why: ""
  failed_or_low_value_actions:
    - action: ""
      why: ""
  access_gap_patterns:
    - gap: ""
      useful_fallback: ""
  useful_source_role_patterns:
    - role: ""
      useful_source_class: ""
      caveat: ""
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
4. Record SourceGuard planned and completed search actions, failed routes, useful fallback actions, access gaps, and source-role coverage.
5. Record Research Reasoning Atlas status: branch tree, debate matrix, selected lenses, expert stance families, counterfactual questions, and conclusion tournament outcomes.
6. Record source registry status, important source ids, and unresolved source-role gaps without copying sensitive source content.
7. Record reusable logic leads and whether support, limiting evidence, execution evidence, outcome evidence, and stakeholder evidence were found.
8. Record the reusable evidence-role map, minimum investigation round status, checked missing signals, competing-storyline status, execution-chain status, counterfactual trace status, and watchlist triggers.
9. Record unresolved gaps.
10. Record requested versus delivered conclusion strength.
11. Record inline citation coverage, citation consistency audit, claim-to-source matrix pointer, and conclusion-tournament audit when available.
12. Record final research quality gate status.
13. Record FlowGuard closure status and installed/source parity status when the run changed skill behavior.
14. Keep sensitive source content in owning systems, not in the ledger.

If postflight cannot be written, report the blocker and provide the intended record structure in the final appendix.
