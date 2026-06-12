from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from elyria_revalidation_engine import evaluate_revalidation

EXAMPLES_DIR = ROOT / "examples"
OUTPUT_DIR = ROOT / "sandbox" / "outputs"
OUTPUT_FILE = OUTPUT_DIR / "sandbox-results.json"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results = []

    for scenario_path in sorted(EXAMPLES_DIR.glob("*.json")):
        scenario = json.loads(scenario_path.read_text(encoding="utf-8"))
        decision = evaluate_revalidation(scenario)
        results.append({"file": scenario_path.name, **decision})
        print(f"{scenario_path.name}: {decision['outcome']}")

    OUTPUT_FILE.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
