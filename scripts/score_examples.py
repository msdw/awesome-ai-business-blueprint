#!/usr/bin/env python3
"""Compute composite scores for accepted examples."""
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

WEIGHTS = {
    "pain_intensity": 0.20,
    "willingness_to_pay": 0.15,
    "ai_fit": 0.15,
    "implementation_complexity": 0.10,
    "distribution_difficulty": 0.10,
    "compliance_risk": 0.10,
    "operational_complexity": 0.10,
    "differentiation_potential": 0.10,
}
INVERT = {"implementation_complexity", "distribution_difficulty", "compliance_risk", "operational_complexity"}


def composite(scoring):
    total = 0.0
    for field, weight in WEIGHTS.items():
        val = scoring.get(field, 5)
        if field in INVERT:
            val = 11 - val
        total += val * weight
    return round(total, 2)


def main():
    path = DATA / "examples.yaml"
    if not path.exists():
        print("examples.yaml not found")
        return
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    updated = 0
    for ex in data.get("examples", []):
        if ex.get("scoring"):
            ex["composite_score"] = composite(ex["scoring"])
            updated += 1
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    print(f"Updated {updated} example scores")


if __name__ == "__main__":
    main()
