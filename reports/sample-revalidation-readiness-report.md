# Sample Revalidation Readiness Report

## System Reviewed

```text
Customer Support AI Copilot
```

## Review Purpose

Assess whether prior approval remains valid after reported AI system changes.

---

## Executive Summary

The reviewed system requires **REVALIDATE** because material model and governance policy changes occurred after the original approval record.

Prior approval should not be relied upon for continued production movement until the change is reviewed, evidence is preserved, and the approval record is renewed or amended.

---

## Decision

```text
REVALIDATE
```

---

## Drivers

| Driver | Finding |
|---|---|
| Prior approval record | Present |
| Change owner | Present |
| System owner | Present |
| Model change | Detected |
| Governance policy change | Detected |
| Critical boundary change | Not detected |
| Monitoring | Active |

---

## Required Remediation

1. Re-run model behavior review.
2. Confirm prompt and policy alignment.
3. Validate output behavior against updated governance policy.
4. Update approval record.
5. Preserve revalidation decision evidence.

---

## Production Readiness Note

This report is a public-safe example. Production reporting should integrate with enterprise approval records, model registry, prompt registry, data catalog, access controls, release management, evidence stores, and incident workflows.
