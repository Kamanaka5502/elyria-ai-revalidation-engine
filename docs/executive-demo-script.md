# Executive Demo Script

## Purpose

This script supports a concise buyer, hiring-panel, or executive walkthrough of the Elyria AI Revalidation Engine.

---

## Opening

```text
AI approval is not permanent.

A system may be approved today and become stale tomorrow because the model, prompt, data, source, tool, access policy, governance policy, deployment environment, or business use changed.

The Elyria AI Revalidation Engine gives enterprises a repeatable way to detect when prior approval remains valid, when evidence is incomplete, when renewed review is required, and when continued use must stop.
```

---

## Walkthrough Path

1. Start with `README.md` and explain stale approval risk.
2. Open `docs/why-and-how.md` and show the core problem: approved does not mean still approved.
3. Open `docs/revalidation-trigger-catalog.md` and show change triggers.
4. Open `docs/approval-freshness-model.md` and show current, stale, invalidated, and expired states.
5. Open `src/elyria_revalidation_engine/engine.py` and explain the decision order.
6. Open `examples/` and show ADMIT, HOLD, REVALIDATE, and REFUSE scenarios.
7. Open `sandbox/outputs/sample-sandbox-results.json` and show sample results.
8. Open `reports/sample-revalidation-readiness-report.md` and show executive output.
9. Close with `docs/production-readiness-checklist.md`.

---

## Close

```text
The value is approval freshness. This gives the enterprise a disciplined way to decide when AI can continue operating, when evidence must be completed, when review must be reopened, and when changed systems must stop before stale approval creates real consequence.
```
