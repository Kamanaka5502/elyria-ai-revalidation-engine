# Expected Revalidation Outcomes

## Purpose

This file documents expected public-safe scenario outcomes for review, testing, and buyer walkthroughs.

---

| Scenario | Expected Decision | Reason |
|---|---|---|
| `no-material-change.json` | ADMIT | Prior approval remains valid. |
| `missing-change-evidence.json` | HOLD | Required change evidence is incomplete. |
| `model-and-policy-change.json` | REVALIDATE | Material model and governance policy changes occurred. |
| `critical-access-boundary-change.json` | REFUSE | Critical identity and production write boundaries changed. |

---

## Validation Rule

```text
A scenario passes when the engine output matches the expected decision and preserves reason codes, remediation, and evidence fields.
```
