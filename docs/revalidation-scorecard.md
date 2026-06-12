# Revalidation Scorecard

## Purpose

The Revalidation Scorecard provides a buyer-facing way to evaluate whether an AI system's prior approval remains valid after change.

---

## Scoring Model

| Domain | Score | Notes |
|---|---:|---|
| Approval record clarity | 0-5 | Is the prior approval documented and traceable? |
| Change ownership | 0-5 | Is an accountable change owner assigned? |
| System ownership | 0-5 | Is an accountable system owner assigned? |
| Change classification | 0-5 | Is the change type clearly identified? |
| Boundary impact | 0-5 | Are critical control boundaries evaluated? |
| Monitoring status | 0-5 | Is evidence capture active? |
| Model/prompt impact | 0-5 | Were behavioral changes assessed? |
| Data/source impact | 0-5 | Were data and retrieval source changes assessed? |
| Tool/access impact | 0-5 | Were action and permission changes assessed? |
| Policy/use-case impact | 0-5 | Were governance and business-use changes assessed? |

Maximum score: 50

---

## Readiness Bands

| Score | Readiness Band | Decision Guidance |
|---:|---|---|
| 45-50 | Approval likely current | ADMIT if no critical blocker exists. |
| 35-44 | Review with conditions | HOLD until gaps are closed. |
| 20-34 | Revalidation likely required | REVALIDATE unless evidence resolves risk. |
| 0-19 | High-risk / uncontrolled | REFUSE or stop continued use pending review. |

---

## Critical Blockers

Any of the following should override the numeric score:

- missing approval record
- missing change owner
- missing system owner
- regulated data boundary changed
- production write boundary changed
- identity or privilege boundary changed
- financial or legal consequence boundary changed
- monitoring inactive where required

---

## Executive Summary Template

```text
This AI system is currently [ADMIT / HOLD / REFUSE / REVALIDATE].
The primary revalidation drivers are [model, prompt, data, source, tool, access, policy, environment, or business-use changes].
The required next steps are [remediation items].
```
