# Change Evidence and Auditability

## Purpose

Revalidation decisions must be reconstructable. The enterprise should be able to prove what changed, who owned the change, what prior approval was relied on, and why continued use was admitted, held, refused, or routed back to review.

---

## Required Evidence

| Evidence | Purpose |
|---|---|
| Approval record ID | Links the system to its prior approval. |
| Change summary | Describes what changed. |
| Change owner | Identifies accountable owner. |
| System owner | Identifies operating owner. |
| Change class | Model, prompt, data, source, tool, access, policy, environment, or use-case change. |
| Boundary impact | Indicates whether critical control boundaries changed. |
| Monitoring status | Confirms evidence capture is active. |
| Decision record | Preserves ADMIT / HOLD / REFUSE / REVALIDATE outcome. |

---

## Audit Rule

```text
A revalidation decision is not complete unless the change, approval state, owner, decision, and required remediation can be reconstructed later.
```
