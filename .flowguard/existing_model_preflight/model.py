"""FlowGuard ExistingModelPreflight for layered research evidence upgrades.

Function block contract:
  SearchExistingModels(Input x State) -> Set(Output x State)
  DecideBoundary(Input x State) -> Set(Output x State)
  RouteDownstream(Input x State) -> Set(Output x State)
"""

from __future__ import annotations

from flowguard import (
    DuplicateBoundaryRisk,
    ExistingModelPreflight,
    ExistingOwnershipSnapshot,
    ModelContextHit,
    REUSE_DECISION_NEW_BOUNDARY,
    REUSE_DECISION_REUSE_EXISTING,
    review_existing_model_preflight,
)


SEARCH_PATHS = (
    "README.md",
    "PLAN.md",
    "docs/guard-family-basis.md",
    "docs/history-ledger.md",
    "docs/implementation-roadmap.md",
    "openspec/changes/add-research-investigation-workflow-skill",
    "openspec/changes/upgrade-investigation-depth-contract",
    "openspec/changes/integrate-sourceguard-discovery-loop",
    "openspec/changes/strengthen-research-source-and-citation-quality",
    "openspec/changes/add-research-reasoning-atlas",
    "openspec/changes/strengthen-layered-research-evidence-contract",
    ".flowguard",
    "<CODEX_HOME>/skills/sourceguard",
    "<CODEX_HOME>/skills",
)


def correct_preflight() -> ExistingModelPreflight:
    return ExistingModelPreflight(
        "layered-research-evidence-existing-model-preflight",
        "Strengthen source portfolios, key-claim ledgers, semantic-fit checks, and layered Guard use without duplicating Guard-family engines or forcing one fixed artifact genre.",
        mode="full",
        existing_modeled_system=True,
        model_search_performed=True,
        search_paths=SEARCH_PATHS,
        relevant_models=(
            ModelContextHit(
                "research-investigation-workflow",
                model_path="<CODEX_HOME>/skills/research-investigation-workflow; skills/research-investigation-workflow",
                evidence_id="research-workflow-skill-20260602",
                evidence_tier="skill_guidance_checked",
                responsibilities=("workflow orchestration", "source portfolio contract", "key-claim/key-number ledger contract", "layered Guard handoff order", "semantic source-fit closure gate", "genre-adaptive reader artifact contract", "History Ledger handoff"),
                function_blocks=("PlanLayeredResearchContract", "RouteLedgersToGuards", "SynthesizeReaderArtifact", "RecordHistoryPostflight"),
                state_owned=("research_plan_card", "layered_contract_status", "source_portfolio_status", "key_claim_ledger_status", "semantic_source_fit_status", "final_quality_gate"),
                side_effects_owned=("write_history_ledger", "write_reader_artifact"),
                public_entrypoints=("<CODEX_HOME>/skills/research-investigation-workflow",),
                validation_evidence=("quick_validate.py research-investigation-workflow",),
                rationale="The workflow skill owns orchestration and final artifact contract, but delegates source search, trace reconstruction, and argument audit to existing Guard owners.",
            ),
            ModelContextHit(
                "sourceguard-workflows",
                model_path="<CODEX_HOME>/skills/sourceguard; <local-source-repo>/SourceGuard_20260531",
                evidence_id="sourceguard-command-surface-20260531",
                evidence_tier="command_surface_checked",
                responsibilities=("source discovery", "candidate sources", "evidence anchors", "source portfolio class coverage", "key-number provenance search", "bridge-evidence search", "source lineage", "access gaps", "post-draft source-gap review"),
                function_blocks=("BuildBeliefState", "ScoreSearchActions", "RecordObservation", "ReviewSourcePortfolioCoverage", "PlanNumericProvenanceSearch", "ExportHandoffBundle"),
                state_owned=("belief_state", "source_candidate_registry", "source_gap_frontier", "search_action_frontier", "source_portfolio", "key_number_provenance_frontier", "source_lineage_map"),
                side_effects_owned=("write_sourceguard_state", "write_sourceguard_handoff_exports"),
                public_entrypoints=("python -m sourceguard",),
                validation_evidence=("python -m sourceguard --help",),
                rationale="SourceGuard owns discovery planning, source portfolios, numeric provenance, and bridge-evidence gaps but does not own event reconstruction, argument audit, or process closure.",
            ),
            ModelContextHit(
                "traceguard-workflows",
                model_path="<CODEX_HOME>/skills/traceguard",
                evidence_id="traceguard-command-surface-20260531",
                evidence_tier="command_surface_checked",
                responsibilities=("case evidence", "layered leads", "events", "competing storylines", "causal/effect-chain state", "counterfactual traces", "confounder ledgers", "scope-transfer warnings", "gaps", "contradictions", "safe wording boundaries"),
                function_blocks=("BuildLayeredTraceModel", "EvaluateTrace", "ReviewExecutionChain", "ReviewEffectChain", "ReviewCompetingStorylines", "ReviewCounterfactualTrace", "ExportLogicGuardBundle"),
                state_owned=("case_library", "gap_ledger", "contradiction_ledger", "execution_chain_status", "effect_chain_status", "scope_transfer_warnings", "competing_storyline_set", "counterfactual_trace_set", "confounder_ledger"),
                side_effects_owned=("write_traceguard_case_library",),
                public_entrypoints=("python -m traceguard",),
                validation_evidence=("python -m traceguard --help",),
                rationale="TraceGuard owns evidence-to-storyline and execution-chain boundaries but does not own final argument audit or Codex skill orchestration.",
            ),
            ModelContextHit(
                "logicguard-workflows",
                model_path="<CODEX_HOME>/skills/logicguard",
                evidence_id="logicguard-command-surface-20260531",
                evidence_tier="command_surface_checked",
                responsibilities=("source preservation", "hierarchical artifact-unit argument modeling", "genre-adaptive artifact synthesis", "claim audit", "semantic source-fit audit", "citation consistency audit", "source registry audit", "conclusion tournament", "steelman opposition", "robustness tests"),
                function_blocks=("PreserveSource", "ModelHierarchicalArgument", "SynthesizeGenreAdaptiveArtifact", "AuditClaim", "AuditSemanticSourceFit", "AuditCitationConsistency", "RunConclusionTournament", "StressTestConclusion"),
                state_owned=("source_library", "argument_model", "hierarchical_artifact_model", "claim_to_source_matrix", "semantic_source_fit", "citation_registry", "conclusion_tournament", "steelman_opposition_map"),
                side_effects_owned=("write_logicguard_source_library",),
                public_entrypoints=("run_logicguard.py",),
                validation_evidence=("run_logicguard.py --help",),
                rationale="LogicGuard owns formal support, final-claim structure, and citation consistency but does not own messy case memory or source search ranking.",
            ),
            ModelContextHit(
                "flowguard-development-process-flow",
                model_path=".flowguard/development_process_flow/model.py",
                evidence_id="flowguard-package-0.40.4-schema-1.0",
                evidence_tier="package_import_checked",
                responsibilities=("process order", "evidence freshness", "closure safety"),
                function_blocks=("ReviewDevelopmentProcess",),
                state_owned=("artifact_versions", "validation_evidence", "closure_status"),
                side_effects_owned=("write_flowguard_logs",),
                public_entrypoints=("python -m flowguard",),
                validation_evidence=("python -c import flowguard; print(flowguard.SCHEMA_VERSION)",),
                rationale="FlowGuard owns lifecycle safety for this implementation and stays separate from research report content rules.",
            ),
        ),
        ownership_snapshot=ExistingOwnershipSnapshot(
            function_block_owners=(
                ("BuildBeliefState", "sourceguard-workflows"),
                ("ScoreSearchActions", "sourceguard-workflows"),
                ("ReviewSourcePortfolioCoverage", "sourceguard-workflows"),
                ("PlanNumericProvenanceSearch", "sourceguard-workflows"),
                ("BuildLayeredTraceModel", "traceguard-workflows"),
                ("ReviewExecutionChain", "traceguard-workflows"),
                ("ReviewEffectChain", "traceguard-workflows"),
                ("ReviewCompetingStorylines", "traceguard-workflows"),
                ("ReviewCounterfactualTrace", "traceguard-workflows"),
                ("ModelHierarchicalArgument", "logicguard-workflows"),
                ("AuditSemanticSourceFit", "logicguard-workflows"),
                ("AuditCitationConsistency", "logicguard-workflows"),
                ("RunConclusionTournament", "logicguard-workflows"),
                ("StressTestConclusion", "logicguard-workflows"),
                ("PlanLayeredResearchContract", "research-investigation-workflow"),
                ("RouteLedgersToGuards", "research-investigation-workflow"),
                ("ReviewDevelopmentProcess", "flowguard-development-process-flow"),
            ),
            state_owners=(
                ("belief_state", "sourceguard-workflows"),
                ("source_gap_frontier", "sourceguard-workflows"),
                ("source_portfolio", "sourceguard-workflows"),
                ("key_number_provenance_frontier", "sourceguard-workflows"),
                ("source_lineage_map", "sourceguard-workflows"),
                ("case_library", "traceguard-workflows"),
                ("execution_chain_status", "traceguard-workflows"),
                ("effect_chain_status", "traceguard-workflows"),
                ("scope_transfer_warnings", "traceguard-workflows"),
                ("competing_storyline_set", "traceguard-workflows"),
                ("counterfactual_trace_set", "traceguard-workflows"),
                ("source_library", "logicguard-workflows"),
                ("hierarchical_artifact_model", "logicguard-workflows"),
                ("semantic_source_fit", "logicguard-workflows"),
                ("citation_registry", "logicguard-workflows"),
                ("conclusion_tournament", "logicguard-workflows"),
                ("steelman_opposition_map", "logicguard-workflows"),
                ("layered_contract_status", "research-investigation-workflow"),
                ("source_portfolio_status", "research-investigation-workflow"),
                ("key_claim_ledger_status", "research-investigation-workflow"),
                ("semantic_source_fit_status", "research-investigation-workflow"),
                ("artifact_versions", "flowguard-development-process-flow"),
            ),
            side_effect_owners=(
                ("write_sourceguard_state", "sourceguard-workflows"),
                ("write_traceguard_case_library", "traceguard-workflows"),
                ("write_logicguard_source_library", "logicguard-workflows"),
                ("write_history_ledger", "research-investigation-workflow"),
                ("write_reader_artifact", "research-investigation-workflow"),
                ("write_flowguard_logs", "flowguard-development-process-flow"),
            ),
            public_entrypoint_owners=(
                ("python -m sourceguard", "sourceguard-workflows"),
                ("python -m traceguard", "traceguard-workflows"),
                ("run_logicguard.py", "logicguard-workflows"),
                ("<CODEX_HOME>/skills/research-investigation-workflow", "research-investigation-workflow"),
                ("python -m flowguard", "flowguard-development-process-flow"),
            ),
            responsibility_owners=(
                ("source-discovery planning", "sourceguard-workflows"),
                ("source portfolio coverage", "sourceguard-workflows"),
                ("key-number provenance search", "sourceguard-workflows"),
                ("evidence-to-storyline", "traceguard-workflows"),
                ("competing storyline review", "traceguard-workflows"),
                ("counterfactual trace review", "traceguard-workflows"),
                ("execution-chain boundary", "traceguard-workflows"),
                ("effect-chain boundary", "traceguard-workflows"),
                ("claim-to-support audit", "logicguard-workflows"),
                ("semantic source-fit audit", "logicguard-workflows"),
                ("hierarchical artifact modeling", "logicguard-workflows"),
                ("citation consistency audit", "logicguard-workflows"),
                ("conclusion tournament audit", "logicguard-workflows"),
                ("layered research contract orchestration", "research-investigation-workflow"),
                ("reader artifact contract", "research-investigation-workflow"),
                ("process freshness", "flowguard-development-process-flow"),
            ),
        ),
        reuse_decision=REUSE_DECISION_REUSE_EXISTING,
        downstream_routes=("development_process_flow",),
        proposed_new_boundaries=("research-investigation-workflow layered evidence contract extension",),
        rationale=(
            "Existing Guard-family workflows already own source discovery, trace reconstruction, argument audit, and process "
            "freshness. The layered evidence upgrade extends the existing research workflow orchestration boundary with source "
            "portfolio, key-claim ledger, semantic-fit, effect-chain, and genre-adaptive closure gates while delegating direct "
            "source planning, layered trace reconstruction, and hierarchical argument audit to existing owners."
        ),
    )


def broken_parallel_engine_preflight() -> ExistingModelPreflight:
    return ExistingModelPreflight(
        "research-investigation-workflow-broken-parallel-engine",
        "Create one new engine that stores source portfolios, key claims, source discovery, evidence, sources, traces, semantic-fit audits, conclusion tournaments, process records, citation audit, and reusable run memory together.",
        mode="full",
        existing_modeled_system=True,
        model_search_performed=True,
        search_paths=SEARCH_PATHS,
        relevant_models=correct_preflight().relevant_models,
        ownership_snapshot=correct_preflight().ownership_snapshot,
        reuse_decision=REUSE_DECISION_REUSE_EXISTING,
        downstream_routes=("development_process_flow",),
        proposed_new_boundaries=("combined-research-reasoning-engine",),
        duplicate_risks=(
            DuplicateBoundaryRisk(
                "state",
                "belief_state",
                "sourceguard-workflows",
                proposed_owner_id="combined-research-reasoning-engine",
            ),
            DuplicateBoundaryRisk(
                "state",
                "branch_source_frontier",
                "sourceguard-workflows",
                proposed_owner_id="combined-research-reasoning-engine",
            ),
            DuplicateBoundaryRisk(
                "state",
                "source_portfolio",
                "sourceguard-workflows",
                proposed_owner_id="combined-research-reasoning-engine",
            ),
            DuplicateBoundaryRisk(
                "state",
                "case_library",
                "traceguard-workflows",
                proposed_owner_id="combined-research-reasoning-engine",
            ),
            DuplicateBoundaryRisk(
                "state",
                "competing_storyline_set",
                "traceguard-workflows",
                proposed_owner_id="combined-research-reasoning-engine",
            ),
            DuplicateBoundaryRisk(
                "state",
                "effect_chain_status",
                "traceguard-workflows",
                proposed_owner_id="combined-research-reasoning-engine",
            ),
            DuplicateBoundaryRisk(
                "state",
                "source_library",
                "logicguard-workflows",
                proposed_owner_id="combined-research-reasoning-engine",
            ),
            DuplicateBoundaryRisk(
                "state",
                "conclusion_tournament",
                "logicguard-workflows",
                proposed_owner_id="combined-research-reasoning-engine",
            ),
            DuplicateBoundaryRisk(
                "state",
                "semantic_source_fit",
                "logicguard-workflows",
                proposed_owner_id="combined-research-reasoning-engine",
            ),
            DuplicateBoundaryRisk(
                "state",
                "citation_registry",
                "logicguard-workflows",
                proposed_owner_id="combined-research-reasoning-engine",
            ),
            DuplicateBoundaryRisk(
                "responsibility",
                "process freshness",
                "flowguard-development-process-flow",
                proposed_owner_id="combined-research-reasoning-engine",
            ),
        ),
        rationale="This would duplicate existing Guard-family ownership and collapse memory layers.",
    )


def run_checks():
    return (
        review_existing_model_preflight(correct_preflight()),
        review_existing_model_preflight(broken_parallel_engine_preflight()),
    )
