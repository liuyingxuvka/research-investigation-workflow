"""FlowGuard DevelopmentProcessFlow for the skill implementation lifecycle.

Function block contract:
  PlanScope(Input x State) -> Set(Output x State)
  WriteSkillArtifacts(Input x State) -> Set(Output x State)
  SyncAndValidate(Input x State) -> Set(Output x State)
  CloseWithEvidence(Input x State) -> Set(Output x State)
"""

from __future__ import annotations

from flowguard import (
    PROCESS_ARTIFACT_CODE,
    PROCESS_ARTIFACT_DOC,
    PROCESS_ARTIFACT_MODEL,
    PROCESS_ARTIFACT_REQUIREMENT,
    PROCESS_ARTIFACT_TEST,
    PROCESS_EVIDENCE_PASSED,
    DevelopmentProcessPlan,
    FreshnessRule,
    ProcessAction,
    ProcessArtifact,
    ProcessEvidence,
    ProofArtifactRef,
    ValidationRequirement,
    review_development_process_flow,
)


def proof_artifact(artifact_id: str, command: str, result_path: str, *covered: str) -> ProofArtifactRef:
    return ProofArtifactRef(
        artifact_id,
        producer_route="development_process_flow",
        command=command,
        result_path=result_path,
        result_status=PROCESS_EVIDENCE_PASSED,
        exit_code=0,
        artifact_fingerprints={result_path: "sha256:recorded-by-command-output"},
        covered_obligation_ids=covered,
    )


def current_artifacts(skill_version: str = "1", project_copy_version: str = "1"):
    return (
        ProcessArtifact(
            "requirements.project-plan",
            PROCESS_ARTIFACT_REQUIREMENT,
            "1",
            path="README.md; PLAN.md; docs/*.md",
            owner="project",
            description="User-approved project plan and Guard-family basis.",
        ),
        ProcessArtifact(
            "requirements.openspec",
            PROCESS_ARTIFACT_REQUIREMENT,
            "2",
            path="openspec/changes/upgrade-investigation-depth-contract",
            owner="openspec",
            upstream_artifact_ids=("requirements.project-plan",),
            description="OpenSpec proposal, design, spec, and task contract for the generalized deep-investigation upgrade.",
        ),
        ProcessArtifact(
            "model.flowguard-preflight",
            PROCESS_ARTIFACT_MODEL,
            "2",
            path=".flowguard/existing_model_preflight/model.py",
            owner="flowguard",
            upstream_artifact_ids=("requirements.project-plan", "requirements.openspec"),
            description="Existing model ownership route decision.",
        ),
        ProcessArtifact(
            "model.flowguard-process",
            PROCESS_ARTIFACT_MODEL,
            "2",
            path=".flowguard/development_process_flow/model.py",
            owner="flowguard",
            upstream_artifact_ids=("requirements.openspec",),
            description="Lifecycle freshness model for implementation and closure.",
        ),
        ProcessArtifact(
            "code.installed-skill",
            PROCESS_ARTIFACT_CODE,
            skill_version,
            path="<CODEX_HOME>/skills/research-investigation-workflow",
            owner="skill-creator",
            upstream_artifact_ids=("requirements.openspec", "model.flowguard-preflight"),
            description="Canonical installed Codex skill.",
        ),
        ProcessArtifact(
            "doc.project-skill-copy",
            PROCESS_ARTIFACT_DOC,
            project_copy_version,
            path="skills/research-investigation-workflow",
            owner="project",
            upstream_artifact_ids=("code.installed-skill",),
            description="Project-local synchronized copy for review.",
        ),
        ProcessArtifact(
            "tests.skill-validator",
            PROCESS_ARTIFACT_TEST,
            "1",
            path="<CODEX_HOME>/skills/.system/skill-creator/scripts/quick_validate.py",
            owner="skill-creator",
            description="Skill metadata validator.",
        ),
    )


def implementation_plan() -> DevelopmentProcessPlan:
    return DevelopmentProcessPlan(
        "research-investigation-workflow-skill-lifecycle",
        require_proof_artifacts=True,
        artifacts=current_artifacts(skill_version="2", project_copy_version="2"),
        actions=(
            ProcessAction(
                "kb-and-command-preflight",
                reads_artifacts=("requirements.project-plan",),
                produced_evidence_ids=("preflight-evidence",),
                description="Predictive KB, skill-creator, command-surface, git, and coordination checks.",
            ),
            ProcessAction(
                "write-openspec-contract",
                reads_artifacts=("requirements.project-plan",),
                writes_artifacts=("requirements.openspec",),
                order_after=("kb-and-command-preflight",),
            ),
            ProcessAction(
                "write-flowguard-models",
                reads_artifacts=("requirements.openspec",),
                writes_artifacts=("model.flowguard-preflight", "model.flowguard-process"),
                produced_evidence_ids=("flowguard-preflight-pass",),
                order_after=("write-openspec-contract",),
            ),
            ProcessAction(
                "write-installed-skill",
                reads_artifacts=("requirements.openspec", "model.flowguard-preflight"),
                writes_artifacts=("code.installed-skill",),
                invalidates_evidence=("skill-validate-pass", "smoke-review-pass", "sync-hash-pass"),
                order_after=("write-flowguard-models",),
            ),
            ProcessAction(
                "sync-project-copy",
                reads_artifacts=("code.installed-skill",),
                writes_artifacts=("doc.project-skill-copy",),
                produced_evidence_ids=("sync-hash-pass",),
                order_after=("write-installed-skill",),
            ),
            ProcessAction(
                "run-validation",
                reads_artifacts=("code.installed-skill", "doc.project-skill-copy", "tests.skill-validator"),
                produced_evidence_ids=("skill-validate-pass", "smoke-review-pass", "openspec-validate-pass"),
                order_after=("sync-project-copy",),
            ),
            ProcessAction(
                "claim-done",
                action_type="claim_done",
                required_validation_ids=(
                    "preflight-current",
                    "flowguard-current",
                    "skill-validator-current",
                    "sync-current",
                    "smoke-review-current",
                    "openspec-current",
                ),
                order_after=("run-validation",),
            ),
        ),
        evidence=(
            ProcessEvidence(
                "preflight-evidence",
                evidence_kind="preflight",
                producer_route="predictive_kb_preflight",
                status=PROCESS_EVIDENCE_PASSED,
                covers_artifacts=("requirements.project-plan",),
                covered_versions={"requirements.project-plan": "1"},
                validation_requirement_ids=("preflight-current",),
                produced_by_action_id="kb-and-command-preflight",
                command="KB search plus command-surface checks",
                proof_artifact=proof_artifact(
                    "artifact:preflight-evidence",
                    "KB search plus command-surface checks",
                    "console:preflight",
                    "preflight-current",
                ),
            ),
            ProcessEvidence(
                "flowguard-preflight-pass",
                evidence_kind="flowguard",
                producer_route="existing_model_preflight",
                status=PROCESS_EVIDENCE_PASSED,
                covers_artifacts=("model.flowguard-preflight", "model.flowguard-process"),
                covered_versions={"model.flowguard-preflight": "2", "model.flowguard-process": "2"},
                validation_requirement_ids=("flowguard-current",),
                produced_by_action_id="write-flowguard-models",
                command="python .flowguard/existing_model_preflight/run_checks.py; python .flowguard/development_process_flow/run_checks.py",
                proof_artifact=proof_artifact(
                    "artifact:flowguard-preflight-pass",
                    "python .flowguard/existing_model_preflight/run_checks.py; python .flowguard/development_process_flow/run_checks.py",
                    "console:flowguard-checks",
                    "flowguard-current",
                ),
            ),
            ProcessEvidence(
                "skill-validate-pass",
                evidence_kind="skill_validation",
                producer_route="skill_creator",
                status=PROCESS_EVIDENCE_PASSED,
                covers_artifacts=("code.installed-skill",),
                verifier_artifacts=("tests.skill-validator",),
                covered_versions={"code.installed-skill": "2", "tests.skill-validator": "1"},
                validation_requirement_ids=("skill-validator-current",),
                produced_by_action_id="run-validation",
                command="python <CODEX_HOME>/skills/.system/skill-creator/scripts/quick_validate.py <CODEX_HOME>/skills/research-investigation-workflow",
                proof_artifact=proof_artifact(
                    "artifact:skill-validate-pass",
                    "quick_validate.py installed skill",
                    "console:quick-validate",
                    "skill-validator-current",
                ),
            ),
            ProcessEvidence(
                "sync-hash-pass",
                evidence_kind="sync_hash",
                producer_route="development_process_flow",
                status=PROCESS_EVIDENCE_PASSED,
                covers_artifacts=("code.installed-skill", "doc.project-skill-copy"),
                covered_versions={"code.installed-skill": "2", "doc.project-skill-copy": "2"},
                validation_requirement_ids=("sync-current",),
                produced_by_action_id="sync-project-copy",
                command="Compare installed and project skill file hashes",
                proof_artifact=proof_artifact(
                    "artifact:sync-hash-pass",
                    "Compare installed and project skill file hashes",
                    "console:sync-hash",
                    "sync-current",
                ),
            ),
            ProcessEvidence(
                "smoke-review-pass",
                evidence_kind="manual_smoke_review",
                producer_route="skill_creator",
                status=PROCESS_EVIDENCE_PASSED,
                covers_artifacts=("code.installed-skill",),
                covered_versions={"code.installed-skill": "2"},
                validation_requirement_ids=("smoke-review-current",),
                produced_by_action_id="run-validation",
                command="Manual acceptance criteria smoke review",
                proof_artifact=proof_artifact(
                    "artifact:smoke-review-pass",
                    "Manual acceptance criteria smoke review",
                    "console:smoke-review",
                    "smoke-review-current",
                ),
            ),
            ProcessEvidence(
                "openspec-validate-pass",
                evidence_kind="openspec_validation",
                producer_route="openspec",
                status=PROCESS_EVIDENCE_PASSED,
                covers_artifacts=("requirements.openspec",),
                covered_versions={"requirements.openspec": "2"},
                validation_requirement_ids=("openspec-current",),
                produced_by_action_id="run-validation",
                command="openspec validate upgrade-investigation-depth-contract --strict",
                proof_artifact=proof_artifact(
                    "artifact:openspec-validate-pass",
                    "openspec validate upgrade-investigation-depth-contract --strict",
                    "console:openspec-validate",
                    "openspec-current",
                ),
            ),
        ),
        validation_requirements=(
            ValidationRequirement(
                "preflight-current",
                required_artifact_ids=("requirements.project-plan",),
                required_evidence_kinds=("preflight",),
                v_model_pair=True,
                command="Run KB and command-surface preflight.",
            ),
            ValidationRequirement(
                "flowguard-current",
                required_artifact_ids=("model.flowguard-preflight", "model.flowguard-process"),
                required_evidence_kinds=("flowguard",),
                v_model_pair=True,
                command="python .flowguard/existing_model_preflight/run_checks.py; python .flowguard/development_process_flow/run_checks.py",
            ),
            ValidationRequirement(
                "skill-validator-current",
                required_artifact_ids=("code.installed-skill",),
                required_evidence_kinds=("skill_validation",),
                v_model_pair=True,
                command="quick_validate.py installed skill",
            ),
            ValidationRequirement(
                "sync-current",
                required_artifact_ids=("code.installed-skill", "doc.project-skill-copy"),
                required_evidence_kinds=("sync_hash",),
                v_model_pair=True,
                command="Compare installed and project skill file hashes.",
            ),
            ValidationRequirement(
                "smoke-review-current",
                required_artifact_ids=("code.installed-skill",),
                required_evidence_kinds=("manual_smoke_review",),
                v_model_pair=True,
                command="Manual acceptance criteria smoke review.",
            ),
            ValidationRequirement(
                "openspec-current",
                required_artifact_ids=("requirements.openspec",),
                required_evidence_kinds=("openspec_validation",),
                v_model_pair=True,
                command="openspec validate upgrade-investigation-depth-contract --strict",
            ),
        ),
        freshness_rules=(
            FreshnessRule(
                "project-plan-invalidates-openspec-and-models",
                upstream_artifact_id="requirements.project-plan",
                invalidates_artifact_ids=(
                    "requirements.openspec",
                    "model.flowguard-preflight",
                    "model.flowguard-process",
                    "code.installed-skill",
                    "doc.project-skill-copy",
                ),
                invalidates_evidence_kinds=(
                    "preflight",
                    "flowguard",
                    "skill_validation",
                    "manual_smoke_review",
                    "sync_hash",
                    "openspec_validation",
                ),
            ),
            FreshnessRule(
                "openspec-invalidates-skill-validation",
                upstream_artifact_id="requirements.openspec",
                invalidates_artifact_ids=(
                    "model.flowguard-preflight",
                    "model.flowguard-process",
                    "code.installed-skill",
                    "doc.project-skill-copy",
                ),
                invalidates_evidence_kinds=("flowguard", "skill_validation", "manual_smoke_review", "sync_hash"),
            ),
            FreshnessRule(
                "existing-preflight-invalidates-skill-boundary",
                upstream_artifact_id="model.flowguard-preflight",
                invalidates_artifact_ids=("code.installed-skill", "doc.project-skill-copy"),
                invalidates_evidence_kinds=("flowguard", "skill_validation", "manual_smoke_review", "sync_hash"),
            ),
            FreshnessRule(
                "installed-skill-invalidates-sync-and-smoke",
                upstream_artifact_id="code.installed-skill",
                invalidates_artifact_ids=("doc.project-skill-copy",),
                invalidates_evidence_kinds=("sync_hash", "manual_smoke_review", "skill_validation"),
            ),
            FreshnessRule(
                "flowguard-model-invalidates-closure",
                upstream_artifact_id="model.flowguard-process",
                invalidates_evidence_kinds=("flowguard",),
            ),
        ),
    )


def broken_stale_plan() -> DevelopmentProcessPlan:
    return DevelopmentProcessPlan(
        "research-investigation-workflow-stale-lifecycle",
        artifacts=current_artifacts(skill_version="2", project_copy_version="1"),
        actions=(
            ProcessAction("run-validation-too-early", produced_evidence_ids=("skill-validate-pass",)),
            ProcessAction("edit-installed-skill-after-validation", writes_artifacts=("code.installed-skill",)),
            ProcessAction("claim-done", action_type="claim_done", required_evidence_ids=("skill-validate-pass",)),
        ),
        evidence=(
            ProcessEvidence(
                "skill-validate-pass",
                evidence_kind="skill_validation",
                producer_route="skill_creator",
                status=PROCESS_EVIDENCE_PASSED,
                covers_artifacts=("code.installed-skill",),
                verifier_artifacts=("tests.skill-validator",),
                covered_versions={"code.installed-skill": "1", "tests.skill-validator": "1"},
                validation_requirement_ids=("skill-validator-current",),
                produced_by_action_id="run-validation-too-early",
                command="quick_validate.py installed skill",
            ),
        ),
        validation_requirements=(
            ValidationRequirement(
                "skill-validator-current",
                required_artifact_ids=("code.installed-skill",),
                required_evidence_kinds=("skill_validation",),
                evidence_ids=("skill-validate-pass",),
                v_model_pair=True,
                command="quick_validate.py installed skill",
            ),
        ),
        freshness_rules=(
            FreshnessRule(
                "installed-skill-invalidates-validation",
                upstream_artifact_id="code.installed-skill",
                invalidates_evidence_kinds=("skill_validation",),
            ),
        ),
    )


def run_checks():
    return review_development_process_flow(implementation_plan()), review_development_process_flow(broken_stale_plan())
