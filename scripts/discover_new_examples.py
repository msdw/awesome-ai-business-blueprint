#!/usr/bin/env python3
"""Discover new AI business examples from public sources."""
import sys
import json
import argparse
import datetime
import time
from pathlib import Path
from urllib.request import urlopen, Request

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

HN_SEARCH_API = "https://hn.algolia.com/api/v1"


def fetch_json(url):
    try:
        req = Request(url, headers={"User-Agent": "awesome-ai-blueprint/1.0"})
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"  Fetch error: {e}", file=sys.stderr)
        return None


def discover_from_hn(mode):
    print("\n[HN] Searching for AI business examples...")
    candidates = []
    days = 7 if mode == "weekly" else 1
    from_ts = int((datetime.datetime.utcnow() - datetime.timedelta(days=days)).timestamp())

    for kw in ["Show HN AI SaaS", "Show HN AI service", "Ask HN AI business"]:
        url = f"{HN_SEARCH_API}/search?query={kw.replace(' ', '+')}&numericFilters=created_at_i>{from_ts}&hitsPerPage=10"
        data = fetch_json(url)
        if not data:
            continue
        for hit in data.get("hits", []):
            points = hit.get("points", 0)
            if points < 15:
                continue
            title = hit.get("title", "")
            story_url = hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID')}"
            candidates.append({
                "id": f"candidate_hn_{hit.get('objectID', '')}",
                "name": title,
                "description": f"From HN: {title}",
                "category": "ai_saas",
                "industries": ["software_dev"],
                "target_users": ["developer"],
                "blueprint_stage_relevance": ["step_10"],
                "business_model": "subscription_saas",
                "outcome": "Candidate — needs review",
                "lessons": ["Candidate — needs review"],
                "tags": ["b2b"],
                "source": story_url,
                "status": "candidate",
                "_meta": {"points": points, "source": "hacker_news"}
            })
            print(f"  {title[:70]} ({points} pts)")
        time.sleep(0.5)
    return candidates


def save_candidates(candidates, dry_run):
    if not candidates:
        print("No candidates found")
        return
    print(f"Found {len(candidates)} candidates")
    if dry_run:
        return

    import yaml
    path = DATA / "examples.yaml"
    data = {}
    if path.exists():
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
    existing_ids = {e["id"] for e in data.get("examples", [])}
    new = [c for c in candidates if c["id"] not in existing_ids]
    if not new:
        print("All candidates already exist")
        return
    data.setdefault("examples", []).extend(new)
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    print(f"Added {len(new)} new candidates")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["weekly", "daily"], default="weekly")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    print(f"=== Discovering new examples (mode={args.mode}) ===")
    candidates = discover_from_hn(args.mode)
    save_candidates(candidates, args.dry_run)
    print("Done")


if __name__ == "__main__":
    main()
