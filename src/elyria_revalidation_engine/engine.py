"""Public-safe Elyria AI Revalidation Engine.

This module evaluates whether prior AI approval remains valid after a change event.
It intentionally avoids private Elyria Systems runtime internals.
"""

from __future__ import annotations

from .schema import (
    ADMIT,
    HOLD,
    REFUSE,
    REVALIDATE,
    critical_boundary_changes,
    material_changes,
    missing_required_evidence,
)


def evaluate_revalidation(scenario: dict) -> dict:
    """Evaluate an AI change scenario.

    Returns a public-safe decision object with:
    - outcome
    - reason_codes
    - required_remediation
    - evidence
    """
    reasons: list[str] = []
    remediation: list[str] = []

    missing = missing_required_evidence(scenario)
    material = material_changes(scenario)
    critical = critical_boundary_changes(scenario)

    if missing:
        reasons.append("CHANGE_EVIDENCE_INCOMPLETE")
        remediation.append("Complete required ownership, approval, and change evidence before continued use.")
        return _decision(HOLD, reasons, remediation, scenario, material, critical, missing)

    if critical:
        reasons.append("CRITICAL_CONTROL_BOUNDARY_CHANGED")
        remediation.append("Stop continued use until critical boundary change is reviewed and explicitly reapproved.")
        return _decision(REFUSE, reasons, remediation, scenario, material, critical, missing)

    if material:
        reasons.append("MATERIAL_CHANGE_REQUIRES_REVALIDATION")
        remediation.append("Route the AI system back through revalidation before continued production movement.")
        return _decision(REVALIDATE, reasons, remediation, scenario, material, critical, missing)

    if scenario.get("approval_expired") is True:
        reasons.append("APPROVAL_EXPIRED")
        remediation.append("Renew approval record before continued use.")
        return _decision(REVALIDATE, reasons, remediation, scenario, material, critical, missing)

    if scenario.get("monitoring_required") is True and scenario.get("monitoring_active") is not True:
        reasons.append("MONITORING_REQUIRED_BUT_NOT_ACTIVE")
        remediation.append("Activate monitoring and evidence capture before continued use.")
        return _decision(HOLD, reasons, remediation, scenario, material, critical, missing)

    reasons.append("PRIOR_APPROVAL_REMAINS_VALID")
    return _decision(ADMIT, reasons, remediation, scenario, material, critical, missing)


def _decision(
    outcome: str,
    reasons: list[str],
    remediation: list[str],
    scenario: dict,
    material: list[str],
    critical: list[str],
    missing: list[str],
) -> dict:
    return {
        "scenario_id": scenario.get("scenario_id"),
        "scenario_name": scenario.get("name"),
        "outcome": outcome,
        "reason_codes": reasons,
        "required_remediation": remediation,
        "evidence": {
            "approval_record_id": scenario.get("approval_record_id"),
            "system_owner": scenario.get("system_owner"),
            "change_owner": scenario.get("change_owner"),
            "material_changes_detected": material,
            "critical_boundary_changes_detected": critical,
            "missing_required_evidence": missing,
        },
    }
