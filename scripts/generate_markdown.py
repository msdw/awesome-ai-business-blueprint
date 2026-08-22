#!/usr/bin/env python3
"""Generate browseable index pages from YAML data."""
import sys
import argparse
import yaml
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
EXAMPLES_DIR = ROOT / "examples"

HEADER = "<!-- AUTO-GENERATED — do not edit manually. Run: python scripts/generate_markdown.py -->\n\n"

# Pages that --check found out of date. main() exits non-zero when this is not
# empty, so a data change committed without regenerating its pages fails the gate
# instead of passing silently.
STALE = []

# Set from --force: generate-pages.yml passes it so a page is rewritten even
# when unchanged, which is what makes the auto-commit step deterministic.
FORCE = False


def load_yaml(path):
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def write_page(path, content, check_only):
    path.parent.mkdir(parents=True, exist_ok=True)
    full = HEADER + content
    if not FORCE and path.exists() and path.read_text(encoding="utf-8") == full:
        return False
    if check_only:
        STALE.append(path)
        print(f"  WOULD WRITE: {path.relative_to(ROOT)}")
        return True
    path.write_text(full, encoding="utf-8")
    print(f"  WROTE: {path.relative_to(ROOT)}")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--force", action="store_true",
                        help="Rewrite every page even when its content is unchanged")
    args = parser.parse_args()

    global FORCE
    FORCE = args.force

    print(f"=== {'Checking' if args.check else 'Generating'} Markdown pages ===")

    data = load_yaml(DATA / "examples.yaml")
    examples = [e for e in (data or {}).get("examples", []) if e.get("status") == "accepted"] if data else []
    print(f"Loaded {len(examples)} accepted examples")

    if examples:
        # Group by blueprint stage
        by_stage = defaultdict(list)
        for ex in examples:
            for stage in ex.get("blueprint_stage_relevance", ["other"]):
                by_stage[stage].append(ex)

        lines = ["# Examples by Blueprint Stage\n\n"]
        for stage in sorted(by_stage):
            lines.append(f"## {stage.replace('-', ' ').title()}\n\n")
            for ex in by_stage[stage]:
                lines.append(f"- [{ex['name']}](../data/examples.yaml) — {ex.get('description','')[:100].strip()}\n")
            lines.append("\n")
        write_page(EXAMPLES_DIR / "by-stage.md", "".join(lines), args.check)

        # Index
        idx_lines = ["# All Examples\n\n"]
        for ex in examples:
            idx_lines.append(f"- [{ex['name']}](../data/examples.yaml)\n")
        write_page(EXAMPLES_DIR / "index.md", "".join(idx_lines), args.check)

    if args.check and STALE:
        print(f"\n{len(STALE)} page(s) out of date — run: python scripts/generate_markdown.py")
        sys.exit(1)

    print("\nDone")


if __name__ == "__main__":
    main()
