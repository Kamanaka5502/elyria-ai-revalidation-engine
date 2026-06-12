# Approval Freshness Model

## Purpose

The approval freshness model determines whether a prior AI approval can still be relied upon after change.

---

## Freshness States

| State | Meaning | Decision Guidance |
|---|---|---|
| Current | No material change detected. | ADMIT |
| Evidence incomplete | Change exists but records are incomplete. | HOLD |
| Stale | Material change affects approval assumptions. | REVALIDATE |
| Invalidated | Critical boundary changed. | REFUSE |
| Expired | Approval time window ended. | REVALIDATE |

---

## Approval Record Requirements

A valid approval record should identify:

- approved system
- approved use case
- approved model or model family
- approved prompt scope
- approved data and source boundaries
- approved tool/action scope
- approved user and access scope
- approval owner
- review date
- review cadence
- revalidation triggers

---

## Freshness Rule

```text
Approval is fresh only when the operating system still matches the reviewed system.
```
