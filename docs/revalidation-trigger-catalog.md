# Revalidation Trigger Catalog

## Purpose

This catalog defines common change events that may invalidate prior AI approval.

---

## Trigger Classes

| Trigger | Revalidation Concern |
|---|---|
| Model change | Output behavior, reliability, risk profile, performance, safety alignment, vendor behavior. |
| Prompt change | Instruction hierarchy, refusal behavior, tone, classification, workflow behavior. |
| Data change | Input distribution, quality, lineage, privacy, contract assumptions. |
| RAG source change | Source authority, freshness, access, grounding, citation integrity. |
| Tool change | External action scope, side effects, production write capability. |
| Access policy change | Who may use the system and what data they may reach. |
| Governance policy change | Applicable standards, controls, review obligations, compliance requirements. |
| Deployment environment change | Network, identity, logging, monitoring, region, security posture. |
| Business use change | Different audience, consequence, decision class, regulatory exposure. |

---

## Critical Boundary Changes

Some changes should stop continued use until explicit review completes:

- regulated data boundary changed
- external action boundary changed
- production write boundary changed
- financial or legal consequence boundary changed
- identity or privilege boundary changed

---

## Trigger Rule

```text
A change is material when it can alter what the AI system knows, accesses, decides, exposes, recommends, invokes, or causes.
```
