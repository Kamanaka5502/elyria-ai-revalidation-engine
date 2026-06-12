# Why and How

## Why This Exists

Enterprise AI governance often fails after approval, not before it.

A system receives approval, then the system changes. The model is upgraded. The prompt is revised. A retrieval source is added. A tool permission expands. Access rules shift. A deployment environment changes. A business team uses the system for a broader purpose.

Without revalidation, the enterprise may continue relying on an approval that no longer applies.

---

## The Core Problem

```text
Was approved does not mean is still approved.
```

AI systems are dynamic. Approval must be lifecycle-aware.

---

## How The Engine Works

The public-safe engine evaluates a change scenario and answers four questions:

1. Is the required change evidence complete?
2. Did a critical control boundary change?
3. Did a material system, data, source, policy, access, prompt, model, tool, environment, or business-use change occur?
4. Does prior approval remain valid?

---

## Decision Path

```text
Missing evidence      -> HOLD
Critical boundary     -> REFUSE
Material change       -> REVALIDATE
No material change    -> ADMIT
```

---

## Enterprise Use Pattern

1. Capture a change event.
2. Classify the trigger.
3. Link the change to the prior approval record.
4. Check ownership and evidence.
5. Evaluate boundary impact.
6. Decide ADMIT / HOLD / REFUSE / REVALIDATE.
7. Preserve the decision record.
8. Route remediation if required.

---

## What This Gives Buyers

- a lifecycle control model
- a change-trigger catalog
- a public-safe decision engine
- example scenarios
- production-readiness checklist
- deployment modes
- scorecard
- audit evidence model
- executive demo path

---

## What This Does Not Expose

This repository does not expose private Elyria Systems runtime machinery, protected validators, commercial proof-corridor internals, customer data, credentials, keys, or production secrets.
