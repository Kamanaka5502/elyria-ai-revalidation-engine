# Sandbox Runner

The intended local runner evaluates every JSON file in `examples/` using the public-safe revalidation engine and writes results to `sandbox/outputs/sandbox-results.json`.

Expected execution command:

```bash
python sandbox/runner.py
```

Expected scenario decisions:

```text
no-material-change.json              -> ADMIT
missing-change-evidence.json         -> HOLD
model-and-policy-change.json         -> REVALIDATE
critical-access-boundary-change.json -> REFUSE
```

If an executable runner is added locally, keep it public-safe and avoid credentials, external service calls, customer data, or private runtime machinery.
