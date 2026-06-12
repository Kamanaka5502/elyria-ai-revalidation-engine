<div align="center">

# Elyria AI Revalidation Engine

## AI Lifecycle Governance · Change Detection · Approval Freshness · Revalidation Control

<img src="assets/ai-revalidation-engine.jpg" alt="Elyria AI Revalidation Engine" width="100%">

![License](https://img.shields.io/badge/license-MIT-1f4f5a?style=for-the-badge)
![AI Governance](https://img.shields.io/badge/AI%20Governance-Revalidation%20Engine-1f4f5a?style=for-the-badge)
![Change Control](https://img.shields.io/badge/Change%20Control-Approval%20Freshness-c9a66b?style=for-the-badge)
![Lifecycle](https://img.shields.io/badge/Lifecycle-Continuous%20Review-5f8fa3?style=for-the-badge)
![Deployable Sandbox](https://img.shields.io/badge/Deployable-Sandbox%20Output-2f6f73?style=for-the-badge)
![Executive Ready](https://img.shields.io/badge/Executive--Ready-Board%20Readable-c9a66b?style=for-the-badge)
![Production Aligned](https://img.shields.io/badge/Production--Aligned-Readiness%20Checklist-62d9ff?style=for-the-badge)

### **Detect when prior AI approval becomes stale before changed systems continue producing enterprise consequence.**

![Decision](https://img.shields.io/badge/Decision-ADMIT%20%7C%20HOLD%20%7C%20REFUSE%20%7C%20REVALIDATE-1f4f5a?style=flat-square)
![Triggers](https://img.shields.io/badge/Triggers-Model%20%7C%20Prompt%20%7C%20Data%20%7C%20Tool%20%7C%20Policy-c9a66b?style=flat-square)
![Evidence](https://img.shields.io/badge/Evidence-Change%20Record%20%7C%20Approval%20State-5f8fa3?style=flat-square)
![Public Safe](https://img.shields.io/badge/Public--Safe-Protected%20Boundary-1f4f5a?style=flat-square)

</div>

---

## Executive Signal

```text
AI approval is not permanent.
```

An AI system may be safe enough to approve today and unsafe tomorrow if the model changes, prompt changes, data source changes, retrieval corpus expands, agent tool permissions change, access policies shift, deployment environment changes, or business use case expands.

The **Elyria AI Revalidation Engine** turns AI change from an informal engineering event into an explicit governance boundary.

---

## Repository Navigation

| Area | Start Here | Outcome |
|---|---|---|
| Executive overview | `README.md` | Understand stale AI approval and revalidation value. |
| Why and how | `docs/why-and-how.md` | Explain the problem, decision path, and enterprise use pattern. |
| Revalidation model | `docs/revalidation-model.md` | Define when approval remains valid or must return to review. |
| Trigger catalog | `docs/revalidation-trigger-catalog.md` | Map model, prompt, data, tool, policy, access, source, and environment changes. |
| Approval freshness | `docs/approval-freshness-model.md` | Determine whether approval is current, stale, invalidated, or expired. |
| Change evidence | `docs/change-evidence-and-auditability.md` | Define what must be recorded to prove revalidation decisions. |
| Production readiness | `docs/production-readiness-checklist.md` | Review production-candidate requirements and deployment boundaries. |
| Deployment modes | `docs/deployment-modes.md` | Use local, workshop, pilot, enterprise, and production-adaptation modes. |
| Architecture diagram | `docs/architecture-diagram.md` | Review the end-to-end revalidation flow. |
| Pilot sandbox | `docs/deployable-sandbox.md` and `sandbox/outputs/sample-sandbox-results.json` | Review public-safe scenario results. |
| Scorecard | `docs/revalidation-scorecard.md` | Assess revalidation readiness and change risk. |
| Demo script | `docs/executive-demo-script.md` | Present the repo to buyers, hiring panels, or executives. |
| Visual system | `docs/design-language.md` and `docs/visual-index.md` | Review the repo palette, decision signals, and buyer scan path. |
| Sample report | `reports/sample-revalidation-readiness-report.md` | Review enterprise-style output. |

---

## Deployable Sandbox Quick Start

This public repo includes a documented sandbox path and sample output for buyer review.

```text
examples/                                   public-safe change scenarios
src/elyria_revalidation_engine/engine.py     public-safe decision engine
sandbox/outputs/sample-sandbox-results.json  sample scenario results
```

Expected scenario path:

```text
no-material-change.json              → ADMIT
missing-change-evidence.json         → HOLD
model-and-policy-change.json         → REVALIDATE
critical-access-boundary-change.json → REFUSE
```

A local runner can be added from the documented pattern in `sandbox/runner.md`. The connector blocked direct upload of the executable runner file, so the live public repo preserves the engine, examples, documented runner behavior, executable tests, and sample output without exposing private runtime machinery.

---

## What This Solves

Most enterprise AI governance programs approve a system at a point in time.

That is not enough.

AI systems change continuously: models are upgraded, prompts are edited, retrieval sources expand, tools are added, permissions shift, policies change, environments move, data contracts change, and use cases widen.

The **Elyria AI Revalidation Engine** provides a public-safe, enterprise-ready reference architecture for detecting when prior approval remains valid, when evidence is incomplete, when renewed review is required, and when continued use must stop.

---

## Decision Model

```text
ADMIT       Prior approval remains valid.
HOLD        Change evidence is incomplete.
REVALIDATE  Change invalidates prior approval and requires renewed review.
REFUSE      Continued use must stop because a critical control boundary changed.
```

---

## Enterprise Architecture Flow

```text
Approved AI system
        ↓
Change event detected
        ↓
Change classified
        ↓
Approval freshness checked
        ↓
Evidence and owner review
        ↓
Risk and boundary evaluation
        ↓
ADMIT / HOLD / REFUSE / REVALIDATE
        ↓
Continued use only if approval remains valid
        ↓
Audit record preserved
```

---

## End-to-End Coverage

| Layer | Enterprise Question | Repository Asset |
|---|---|---|
| Change detection | What changed? | `docs/revalidation-trigger-catalog.md` |
| Approval freshness | Is prior approval still valid? | `docs/approval-freshness-model.md` |
| Governance decision | Should use continue, pause, stop, or return to review? | `docs/revalidation-model.md` |
| Evidence | What proves the decision? | `docs/change-evidence-and-auditability.md` |
| Production readiness | What must be true before production adaptation? | `docs/production-readiness-checklist.md` |
| Sandbox output | What do sample scenarios return? | `sandbox/outputs/sample-sandbox-results.json` |
| Scorecard | How risky is this change? | `docs/revalidation-scorecard.md` |
| Tests | Does the public-safe engine enforce the expected outcomes? | `tests/test_revalidation_engine.py` |
| Report | What does enterprise output look like? | `reports/sample-revalidation-readiness-report.md` |

---

## Public-Safe Components

| Asset | Purpose |
|---|---|
| `src/elyria_revalidation_engine/engine.py` | Public-safe revalidation decision engine. |
| `src/elyria_revalidation_engine/schema.py` | Scenario schema helpers and decision constants. |
| `examples/*.json` | Public-safe AI change scenarios. |
| `sandbox/runner.md` | Documented sandbox runner behavior. |
| `sandbox/outputs/sample-sandbox-results.json` | Pre-generated public-safe sandbox output. |
| `docs/why-and-how.md` | Why this exists and how the engine works. |
| `docs/revalidation-model.md` | Core revalidation decision model. |
| `docs/revalidation-trigger-catalog.md` | Change trigger catalog. |
| `docs/approval-freshness-model.md` | Approval freshness states and rules. |
| `docs/change-evidence-and-auditability.md` | Evidence and audit requirements. |
| `docs/production-readiness-checklist.md` | Production-candidate requirements. |
| `docs/deployment-modes.md` | Local, workshop, pilot, enterprise, and production-adaptation modes. |
| `docs/architecture-diagram.md` | Mermaid architecture diagram. |
| `docs/revalidation-scorecard.md` | Buyer-facing readiness scorecard. |
| `docs/executive-demo-script.md` | 10-minute buyer or hiring-panel demo path. |
| `docs/design-language.md` | Visual identity, palette, badges, and language rules. |
| `docs/visual-index.md` | Executive scan path and visual decision system. |
| `reports/sample-revalidation-readiness-report.md` | Enterprise-style sample report. |
| `tests/test_revalidation_engine.py` | Executable public-safe engine tests. |
| `tests/expected-revalidation-outcomes.md` | Expected public-safe outcomes. |
| `pyproject.toml` | Python project metadata. |
| `requirements.txt` | Local validation dependency list. |
| `LICENSE.md` | MIT license. |
| `SECURITY.md` | Public-safe security policy. |
| `CONTRIBUTING.md` | Public-safe contribution rules. |
| `NOTICE.md` | Public boundary and attribution notice. |

---

## Relationship to the Elyria Enterprise AI Governance Suite

```text
Elyria Enterprise AI Control Plane
= governs enterprise AI movement across the organization.

Elyria Agent Action Boundary
= governs tool-using agents that may touch systems, data, workflows, communications, or operational action.

Elyria RAG Source Authority Gate
= governs retrieval trust: what knowledge AI may retrieve, trust, cite, and use.

Elyria AI Revalidation Engine
= governs when prior approval becomes stale after change.
```

This repository is the change-after-approval layer of the suite.

---

## Public Boundary

This repository is public-safe. It demonstrates architecture surfaces, sandbox logic, examples, tests, and enterprise readiness models, not private Elyria Systems runtime machinery, protected validators, customer-specific builds, commercial proof-corridor internals, credentials, keys, or confidential implementation details.

**Show the architecture. Protect the machinery.**
