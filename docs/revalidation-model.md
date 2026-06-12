# Revalidation Model

## Core Rule

```text
Prior AI approval remains valid only while the conditions that justified approval remain materially unchanged.
```

Revalidation is required when a material change may alter risk, authority, access, grounding, safety, compliance, operational consequence, or business use.

---

## Decision States

| Decision | Meaning |
|---|---|
| ADMIT | Prior approval remains valid. |
| HOLD | Change evidence is incomplete. |
| REVALIDATE | Material change requires renewed review. |
| REFUSE | Continued use must stop because a critical boundary changed. |

---

## Revalidation Questions

1. What changed?
2. Who owns the change?
3. Which approval record is being relied upon?
4. Did the change alter model behavior, prompt behavior, data access, tool access, source authority, policy scope, environment, or business use?
5. Does monitoring still capture the right evidence?
6. Is continued use allowed before review completes?

---

## Operating Principle

AI governance is not complete when a system is approved. Governance continues across the lifecycle whenever the system, context, authority, or consequence surface changes.
