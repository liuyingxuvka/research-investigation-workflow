"""FlowGuard ExistingModelPreflight for research-investigation-workflow.

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
    ".flowguard",
    "<CODEX_HOME>/skills",
)


def correct_preflight() -> ExistingModelPreflight:
    return ExistingModelPreflight(
        "research-investigation-workflow-existing-model-preflight",
        "Create an orchestration skill for TraceGuard, LogicGuard, FlowGuard, and a run-history ledger.",
        mode="full",
        existing_modeled_system=True,
        model_search_performed=True,
        search_paths=SEARCH_PATHS,
        relevant_models=(
            ModelContextHit(
                "traceguard-workflows",
                model_path="<CODEX_HOME>/skills/traceguard",
                evidence_id="traceguard-command-surface-20260531",
                evidence_tier="command_surface_checked",
                responsibilities=("case evidence", "events", "traces", "gaps", "contradictions"),
                function_blocks=("BuildTraceModel", "EvaluateTrace", "ExportLogicGuardBundle"),
                state_owned=("case_library", "gap_ledger", "contradiction_ledger"),
                side_effects_owned=("write_traceguard_case_library",),
                public_entrypoints=("python -m traceguard",),
                validation_evidence=("python -m traceguard --help",),
                rationale="TraceGuard owns evidence-to-storyline work but does not own Codex skill orchestration.",
            ),
            ModelContextHit(
                "logicguard-workflows",
                model_path="<CODEX_HOME>/skills/logicguard",
                evidence_id="logicguard-command-surface-20260531",
                evidence_tier="command_surface_checked",
                responsibilities=("source preservation", "argument modeling", "artifact synthesis", "claim audit"),
                function_blocks=("PreserveSource", "ModelArgument", "SynthesizeArtifact", "AuditClaim"),
                state_owned=("source_library", "argument_model", "artifact_plan"),
                side_effects_owned=("write_logicguard_source_library",),
                public_entrypoints=("run_logicguard.py",),
                validation_evidence=("run_logicguard.py --help",),
                rationale="LogicGuard owns formal support and final-claim structure but does not own messy case memory.",
            ),
            ModelContextHit(
                "flowguard-development-process-flow",
                model_path=".flowguard/development_process_flow/model.py",
                evidence_id="flowguard-package-0.39.1-schema-1.0",
                evidence_tier="package_import_checked",
                responsibilities=("process order", "evidence freshness", "closure safety"),
                function_blocks=("ReviewDevelopmentProcess",),
                state_owned=("artifact_versions", "validation_evidence", "closure_status"),
                side_effects_owned=("write_flowguard_logs",),
                public_entrypoints=("python -m flowguard",),
                validation_evidence=("python -c import flowguard; print(flowguard.SCHEMA_VERSION)",),
                rationale="FlowGuard owns lifecycle safety for this implementation.",
            ),
        ),
        ownership_snapshot=ExistingOwnershipSnapshot(
            function_block_owners=(
                ("BuildTraceModel", "traceguard-workflows"),
                ("ModelArgument", "logicguard-workflows"),
                ("ReviewDevelopmentProcess", "flowguard-development-process-flow"),
            ),
            state_owners=(
                ("case_library", "traceguard-workflows"),
                ("source_library", "logicguard-workflows"),
                ("artifact_versions", "flowguard-development-process-flow"),
            ),
            side_effect_owners=(
                ("write_traceguard_case_library", "traceguard-workflows"),
                ("write_logicguard_source_library", "logicguard-workflows"),
                ("write_flowguard_logs", "flowguard-development-process-flow"),
            ),
            public_entrypoint_owners=(
                ("python -m traceguard", "traceguard-workflows"),
                ("run_logicguard.py", "logicguard-workflows"),
                ("python -m flowguard", "flowguard-development-process-flow"),
            ),
            responsibility_owners=(
                ("evidence-to-storyline", "traceguard-workflows"),
                ("claim-to-support audit", "logicguard-workflows"),
                ("process freshness", "flowguard-development-process-flow"),
            ),
        ),
        reuse_decision=REUSE_DECISION_NEW_BOUNDARY,
        downstream_routes=("development_process_flow",),
        proposed_new_boundaries=("research-investigation-workflow skill orchestration",),
        rationale=(
            "Existing Guard-family workflows own reasoning subdomains, but no existing skill owns the cross-run "
            "research orchestration and History Ledger boundary. A new thin orchestration skill is justified if it "
            "delegates reasoning work instead of replacing it."
        ),
    )


def broken_parallel_engine_preflight() -> ExistingModelPreflight:
    return ExistingModelPreflight(
        "research-investigation-workflow-broken-parallel-engine",
        "Create one new engine that stores evidence, sources, process records, and reusable run memory together.",
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
                "case_library",
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
