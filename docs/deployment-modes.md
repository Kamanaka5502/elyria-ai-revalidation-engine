# Deployment Modes

## Purpose

This repository is structured so the AI revalidation model can be reviewed at multiple enterprise maturity levels without exposing private runtime machinery.

---

## Mode 1 — Local Review

Used by architects, governance reviewers, hiring panels, or technical evaluators.

```text
Goal: understand the model and inspect public-safe scenarios.
```

Assets:

- `README.md`
- `docs/revalidation-model.md`
- `docs/revalidation-trigger-catalog.md`
- `examples/*.json`

---

## Mode 2 — Workshop

Used with stakeholders to map where approval can become stale.

```text
Goal: identify revalidation triggers across model, prompt, data, RAG, tool, access, policy, environment, and business-use changes.
```

Assets:

- `docs/revalidation-trigger-catalog.md`
- `docs/approval-freshness-model.md`
- `docs/revalidation-scorecard.md`
- `docs/executive-demo-script.md`

---

## Mode 3 — Pilot Sandbox

Used to test the decision model against public-safe or customer-provided non-sensitive scenarios.

```text
Goal: evaluate ADMIT / HOLD / REFUSE / REVALIDATE behavior before production adaptation.
```

Assets:

- `src/elyria_revalidation_engine/engine.py`
- `src/elyria_revalidation_engine/schema.py`
- `examples/*.json`
- `sandbox/outputs/sample-sandbox-results.json`

---

## Mode 4 — Enterprise Adaptation

Used when integrating with enterprise systems.

Typical integration points:

- model registry
- prompt registry
- data catalog
- RAG source registry
- tool/action registry
- identity and access management
- CI/CD release events
- policy management
- logging and evidence store
- issue/review workflow

---

## Mode 5 — Production-Candidate Control

Used only after organization-specific review.

Required additions:

- authentication and authorization
- durable evidence storage
- security review
- privacy review
- legal/compliance review
- monitoring and alerting
- incident process
- rollback process
- human approval workflow
- integration testing

---

## Boundary

This public repository is a reference architecture and pilot sandbox. It is not a complete production enforcement system by itself.
