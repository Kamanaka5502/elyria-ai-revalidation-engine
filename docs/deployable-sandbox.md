# Deployable Sandbox

## Purpose

The sandbox demonstrates public-safe revalidation decisions across representative enterprise AI change scenarios.

---

## Expected Command

```bash
python sandbox/runner.py
```

The executable runner may be added locally or by CI. The documented sandbox behavior is:

1. Load every scenario in `examples/`.
2. Evaluate each scenario through the public-safe decision engine.
3. Emit ADMIT / HOLD / REFUSE / REVALIDATE.
4. Write output to `sandbox/outputs/sandbox-results.json`.

---

## Expected Outcomes

| Scenario | Expected Decision |
|---|---|
| `no-material-change.json` | ADMIT |
| `missing-change-evidence.json` | HOLD |
| `model-and-policy-change.json` | REVALIDATE |
| `critical-access-boundary-change.json` | REFUSE |

---

## Production Adaptation

Production adaptation requires integration with:

- model registry
- prompt registry
- data catalog
- RAG source registry
- tool/action registry
- identity and access systems
- CI/CD release events
- policy management
- logging and evidence store
- incident and review workflow
