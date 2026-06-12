from elyria_revalidation_engine import evaluate_revalidation


def base_scenario():
    return {
        "scenario_id": "TEST-001",
        "name": "Base Test Scenario",
        "approval_record_id": "APR-TEST-001",
        "system_owner": "AI Platform Team",
        "change_owner": "Release Manager",
        "change_summary": "No material change.",
        "monitoring_required": True,
        "monitoring_active": True,
    }


def test_no_material_change_admits():
    result = evaluate_revalidation(base_scenario())
    assert result["outcome"] == "ADMIT"
    assert "PRIOR_APPROVAL_REMAINS_VALID" in result["reason_codes"]


def test_missing_evidence_holds():
    scenario = base_scenario()
    scenario.pop("change_owner")
    result = evaluate_revalidation(scenario)
    assert result["outcome"] == "HOLD"
    assert "CHANGE_EVIDENCE_INCOMPLETE" in result["reason_codes"]


def test_material_change_revalidates():
    scenario = base_scenario()
    scenario["model_changed"] = True
    result = evaluate_revalidation(scenario)
    assert result["outcome"] == "REVALIDATE"
    assert "MATERIAL_CHANGE_REQUIRES_REVALIDATION" in result["reason_codes"]


def test_critical_boundary_change_refuses():
    scenario = base_scenario()
    scenario["identity_or_privilege_boundary_changed"] = True
    result = evaluate_revalidation(scenario)
    assert result["outcome"] == "REFUSE"
    assert "CRITICAL_CONTROL_BOUNDARY_CHANGED" in result["reason_codes"]
