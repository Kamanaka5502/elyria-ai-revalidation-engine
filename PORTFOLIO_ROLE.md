# Portfolio Role — Elyria AI Revalidation Engine

## Control Dimension: Changed Conditions and Approval Freshness

This repository is a supporting proof surface within the **Elyria Systems Pre-Execution Governance** portfolio.

It establishes that AI approval is not permanent. Material changes in model, prompt, data, retrieval, tools, access, policy, environment, or use case can invalidate the standing that previously allowed a system to operate.

```text
ADMIT       → prior approval remains valid
HOLD        → evidence is incomplete
REVALIDATE  → changed conditions require renewed review
REFUSE      → continued use must stop
```

## How to Navigate the Portfolio

1. **Start with the flagship runnable proof surface:** [Elyria Admission Runtime](https://github.com/Kamanaka5502/elyria-admission-runtime)
2. **Review the full portfolio hierarchy:** [Elyria Systems — Portfolio Start Here](https://github.com/Kamanaka5502/Samantha-Revita-Elyria-Systems/blob/main/PORTFOLIO_START_HERE.md)
3. **Then return here** to inspect stale approval detection, change triggers, evidence requirements, and revalidation outcomes.

## Relationship to the Flagship Runtime

```text
Elyria Admission Runtime
    → resolves whether a proposed movement may bind now

AI Revalidation Engine
    → determines whether earlier approval is still valid after the
      conditions supporting that approval have changed
```

> **Pre-Execution Governance category:** Continued operation is admitted only while the approval basis remains current.
