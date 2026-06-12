"""Public-safe schema helpers for Elyria AI Revalidation Engine."""

ADMIT = "ADMIT"
HOLD = "HOLD"
REFUSE = "REFUSE"
REVALIDATE = "REVALIDATE"

MATERIAL_CHANGE_FIELDS = [
    "model_changed",
    "prompt_changed",
    "data_changed",
    "rag_source_changed",
    "tool_changed",
    "access_policy_changed",
    "governance_policy_changed",
    "deployment_environment_changed",
    "business_use_changed",
]

CRITICAL_BOUNDARY_FIELDS = [
    "regulated_data_boundary_changed",
    "external_action_boundary_changed",
    "production_write_boundary_changed",
    "financial_or_legal_boundary_changed",
    "identity_or_privilege_boundary_changed",
]

REQUIRED_EVIDENCE_FIELDS = [
    "change_owner",
    "system_owner",
    "approval_record_id",
    "change_summary",
]


def missing_required_evidence(scenario: dict) -> list[str]:
    """Return missing evidence fields for a scenario."""
    return [field for field in REQUIRED_EVIDENCE_FIELDS if not scenario.get(field)]


def material_changes(scenario: dict) -> list[str]:
    """Return material changes detected in a scenario."""
    return [field for field in MATERIAL_CHANGE_FIELDS if scenario.get(field) is True]


def critical_boundary_changes(scenario: dict) -> list[str]:
    """Return critical boundary changes detected in a scenario."""
    return [field for field in CRITICAL_BOUNDARY_FIELDS if scenario.get(field) is True]
