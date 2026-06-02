"""FlowGuard ExistingModelPreflight for generic Research Reasoning Atlas upgrades.

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
    ".flowguard",
    "<CODEX_HOME>/skills/sourceguard",
    "<CODEX_HOME>/skills",
)


def correct_preflight() -> ExistingModelPreflight:
    return ExistingModelPreflight(
        "research-reasoning-atlas-existing-model-preflight",
        "Add generic reasoning-atlas depth without duplicating Guard-family engines or hard-coding domain-specific checklists.",
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
                responsibilities=("workflow orchestration", "Research Reasoning Atlas stage order", "generic branch tree", "model-lens selection", "expert-stance map", "reader-facing artifact contract", "History Ledger handoff"),
                function_blocks=("PlanResearchAtlas", "RouteAtlasToGuards", "SynthesizeReaderArtifact", "RecordHistoryPostflight"),
                state_owned=("research_plan_card", "atlas_stage_status", "branch_tree_summary", "model_lens_selection", "expert_stance_map", "final_quality_gate"),
                side_effects_owned=("write_history_ledger", "write_reader_artifact"),
                public_entrypoints=("<CODEX_HOME>/skills/research-investigation-workflow",),
                validation_evidence=("quick_validate.py research-investigation-workflow",),
                rationale="The workflow skill owns generic orchestration and final artifact contract, but delegates source search, trace reconstruction, and argument audit to existing Guard owners.",
            ),
            ModelContextHit(
                "sourceguard-workflows",
                model_path="<CODEX_HOME>/skills/sourceguard; C:/Users/liu_y/Documents/SourceGuard_20260531",
                evidence_id="sourceguard-command-surface-20260531",
                evidence_tier="command_surface_checked",
                responsibilities=("source discovery", "candidate sources", "evidence anchors", "branch-aware search actions", "disconfirming-source priority", "source lineage", "expert/model source discovery", "access gaps", "source-role coverage", "post-draft source-gap review"),
                function_blocks=("BuildBeliefState", "ScoreSearchActions", "RecordObservation", "ReviewSourceRoleCoverage", "PlanBranchAwareSearch", "ExportHandoffBundle"),
                state_owned=("belief_state", "source_candidate_registry", "source_gap_frontier", "search_action_frontier", "source_role_coverage", "branch_source_frontier", "source_lineage_map"),
                side_effects_owned=("write_sourceguard_state", "write_sourceguard_handoff_exports"),
                public_entrypoints=("python -m sourceguard",),
                validation_evidence=("python -m sourceguard --help",),
                rationale="SourceGuard owns source-discovery planning and source-role coverage gaps but does not own event reconstruction, argument audit, or process closure.",
            ),
            ModelContextHit(
                "traceguard-workflows",
                model_path="<CODEX_HOME>/skills/traceguard",
                evidence_id="traceguard-command-surface-20260531",
                evidence_tier="command_surface_checked",
                responsibilities=("case evidence", "events", "competing storylines", "causal-chain state", "counterfactual traces", "confounder ledgers", "red-team storylines", "gaps", "contradictions", "announcement-to-execution chain status", "safe wording boundaries"),
                function_blocks=("BuildTraceModel", "EvaluateTrace", "ReviewExecutionChain", "ReviewCompetingStorylines", "ReviewCounterfactualTrace", "ExportLogicGuardBundle"),
                state_owned=("case_library", "gap_ledger", "contradiction_ledger", "execution_chain_status", "competing_storyline_set", "causal_chain_status", "counterfactual_trace_set", "confounder_ledger"),
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
                responsibilities=("source preservation", "argument modeling", "artifact synthesis", "claim audit", "citation consistency audit", "source registry audit", "conclusion tournament", "steelman opposition", "model lenses as warrants", "expert-role boundaries", "robustness tests"),
                function_blocks=("PreserveSource", "ModelArgument", "SynthesizeArtifact", "AuditClaim", "AuditCitationConsistency", "RunConclusionTournament", "ReviewSteelmanOpposition", "StressTestConclusion"),
                state_owned=("source_library", "argument_model", "artifact_plan", "claim_to_source_matrix", "citation_registry", "conclusion_tournament", "steelman_opposition_map", "model_lens_warrants"),
                side_effects_owned=("write_logicguard_source_library",),
                public_entrypoints=("run_logicguard.py",),
                validation_evidence=("run_logicguard.py --help",),
                rationale="LogicGuard owns formal support, final-claim structure, and citation consistency but does not own messy case memory or source search ranking.",
            ),
            ModelContextHit(
                "flowguard-development-process-flow",
                model_path=".flowguard/development_process_flow/model.py",
                evidence_id="flowguard-package-0.39.3-schema-1.0",
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
                ("PlanBranchAwareSearch", "sourceguard-workflows"),
                ("BuildTraceModel", "traceguard-workflows"),
                ("ReviewExecutionChain", "traceguard-workflows"),
                ("ReviewCompetingStorylines", "traceguard-workflows"),
                ("ReviewCounterfactualTrace", "traceguard-workflows"),
                ("ModelArgument", "logicguard-workflows"),
                ("AuditCitationConsistency", "logicguard-workflows"),
                ("RunConclusionTournament", "logicguard-workflows"),
                ("StressTestConclusion", "logicguard-workflows"),
                ("PlanResearchAtlas", "research-investigation-workflow"),
                ("RouteAtlasToGuards", "research-investigation-workflow"),
                ("ReviewDevelopmentProcess", "flowguard-development-process-flow"),
            ),
            state_owners=(
                ("belief_state", "sourceguard-workflows"),
                ("source_gap_frontier", "sourceguard-workflows"),
                ("source_role_coverage", "sourceguard-workflows"),
                ("branch_source_frontier", "sourceguard-workflows"),
                ("source_lineage_map", "sourceguard-workflows"),
                ("case_library", "traceguard-workflows"),
                ("execution_chain_status", "traceguard-workflows"),
                ("competing_storyline_set", "traceguard-workflows"),
                ("counterfactual_trace_set", "traceguard-workflows"),
                ("source_library", "logicguard-workflows"),
                ("citation_registry", "logicguard-workflows"),
                ("conclusion_tournament", "logicguard-workflows"),
                ("steelman_opposition_map", "logicguard-workflows"),
                ("atlas_stage_status", "research-investigation-workflow"),
                ("branch_tree_summary", "research-investigation-workflow"),
                ("model_lens_selection", "research-investigation-workflow"),
                ("expert_stance_map", "research-investigation-workflow"),
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
                ("branch-aware source discovery", "sourceguard-workflows"),
                ("evidence-to-storyline", "traceguard-workflows"),
                ("competing storyline review", "traceguard-workflows"),
                ("counterfactual trace review", "traceguard-workflows"),
                ("execution-chain boundary", "traceguard-workflows"),
                ("claim-to-support audit", "logicguard-workflows"),
                ("citation consistency audit", "logicguard-workflows"),
                ("conclusion tournament audit", "logicguard-workflows"),
                ("generic Atlas orchestration", "research-investigation-workflow"),
                ("reader artifact contract", "research-investigation-workflow"),
                ("process freshness", "flowguard-development-process-flow"),
            ),
        ),
        reuse_decision=REUSE_DECISION_REUSE_EXISTING,
        downstream_routes=("development_process_flow",),
        proposed_new_boundaries=("research-investigation-workflow Research Reasoning Atlas extension",),
        rationale=(
            "Existing Guard-family workflows already own source discovery, trace reconstruction, argument audit, and process "
            "freshness. The Atlas upgrade extends the existing research workflow orchestration boundary with generic branch, "
            "lens, expert, and final artifact gates while delegating branch-aware source planning, competing/counterfactual "
            "trace reconstruction, and conclusion tournaments to the existing owners. The upgrade is valid only if it stays "
            "generic and avoids domain-specific checklist ownership in the core skills."
        ),
    )


def broken_parallel_engine_preflight() -> ExistingModelPreflight:
    return ExistingModelPreflight(
        "research-investigation-workflow-broken-parallel-engine",
        "Create one new engine that stores Atlas branches, source discovery, evidence, sources, traces, conclusion tournaments, process records, citation audit, and reusable run memory together.",
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
                "atlas_stage_status",
                "research-investigation-workflow",
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
