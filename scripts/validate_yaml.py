#!/usr/bin/env python3
"""Validate all YAML data files against required schema."""
import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

REQUIRED_EXAMPLE_FIELDS = [
    "id", "name", "description", "category", "industries",
    "target_users", "blueprint_stage_relevance", "business_model",
    "outcome", "lessons", "tags", "source", "status"
]

REQUIRED_STEP_FIELDS = [
    "id", "order", "title", "file", "objective",
    "key_questions", "deliverables", "common_mistakes"
]

VALID_STATUSES = {"candidate", "needs_review", "accepted", "rejected", "duplicate", "deprecated"}
REGULATED_INDUSTRIES = {"legal", "healthcare", "finance", "insurance"}

ERRORS = []
WARNINGS = []


def error(msg):
    ERRORS.append(msg)
    print(f"  ERROR: {msg}", file=sys.stderr)


def warn(msg):
    WARNINGS.append(msg)
    print(f"  WARN:  {msg}")


def load_yaml(path):
    try:
        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        error(f"YAML parse error in {path.name}: {e}")
        return None
    except FileNotFoundError:
        error(f"File not found: {path}")
        return None


def validate_blueprint_steps(path):
    print(f"\nValidating {path.name}...")
    data = load_yaml(path)
    if not data:
        return
    steps = data.get("blueprint_steps", [])
    seen_ids = set()
    for i, step in enumerate(steps):
        prefix = f"step[{i}] id={step.get('id', '?')}"
        sid = step.get("id")
        if sid in seen_ids:
            error(f"{prefix}: duplicate id '{sid}'")
        seen_ids.add(sid)
        for field in REQUIRED_STEP_FIELDS:
            if field not in step:
                error(f"{prefix}: missing required field '{field}'")
    print(f"  Checked {len(steps)} blueprint steps")


def validate_examples(path):
    print(f"\nValidating {path.name}...")
    data = load_yaml(path)
    if not data:
        return
    examples = data.get("examples", [])
    seen_ids = set()
    for i, ex in enumerate(examples):
        prefix = f"examples[{i}] id={ex.get('id', '?')}"
        eid = ex.get("id")
        if eid in seen_ids:
            error(f"{prefix}: duplicate id '{eid}'")
        seen_ids.add(eid)
        for field in REQUIRED_EXAMPLE_FIELDS:
            if field not in ex:
                error(f"{prefix}: missing required field '{field}'")
        status = ex.get("status")
        if status and status not in VALID_STATUSES:
            error(f"{prefix}: invalid status '{status}'")
        industries = ex.get("industries", [])
        if any(ind in REGULATED_INDUSTRIES for ind in industries):
            if not ex.get("compliance_notes"):
                warn(f"{prefix}: regulated industry — compliance_notes recommended")
    print(f"  Checked {len(examples)} examples")


def validate_taxonomy(path, key):
    print(f"\nValidating {path.name}...")
    data = load_yaml(path)
    if not data:
        return set()
    items = data.get(key, [])
    print(f"  Found {len(items)} entries")
    return {item.get("id") for item in items if "id" in item}


def main():
    print("=== Validating YAML schemas ===")

    for fname, key in [
        ("business_models.yaml", "business_models"),
        ("industries.yaml", "industries"),
        ("customer_segments.yaml", "customer_segments"),
        ("channels.yaml", "channels"),
        ("tags.yaml", "tags"),
    ]:
        p = DATA / fname
        if p.exists():
            validate_taxonomy(p, key)

    if (DATA / "blueprint_steps.yaml").exists():
        validate_blueprint_steps(DATA / "blueprint_steps.yaml")

    if (DATA / "examples.yaml").exists():
        validate_examples(DATA / "examples.yaml")

    print(f"\n=== Summary ===\n  Errors: {len(ERRORS)}  Warnings: {len(WARNINGS)}")
    if ERRORS:
        print("\nFAILED", file=sys.stderr)
        sys.exit(1)
    else:
        print("\nPASSED")


if __name__ == "__main__":
    main()
