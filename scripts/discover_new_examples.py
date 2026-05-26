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

GITHUB_API = "https://api.github.com"
HN_SEARCH_API = "https://hn.algolia.com/api/v1"


def fetch_json(url):
    try:
        req = Request(url, headers={"User-Agent": "awesome-ai-blueprint/1.0"})
        with urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"  Fetch error: {e}", file=sys.stderr)
        return None


def load_active_sources() -> dict:
    """Load active sources from data/sources.yaml."""
    try:
        import yaml
        sources_path = DATA / "sources.yaml"
        if not sources_path.exists():
            return {"github": [], "hn": []}
        with open(sources_path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        github_queries, hn_queries = [], []
        for src in data.get("sources", {}).values():
            if src.get("status", "active") != "active":
                continue
            if src.get("type") == "github" and "search_query" in src:
                github_queries.append(src["search_query"])
            elif src.get("type") == "hn" and "search_query" in src:
                hn_queries.append(src["search_query"])
        return {"github": github_queries, "hn": hn_queries}
    except Exception as e:
        print(f"  Warning: could not load sources.yaml: {e}", file=sys.stderr)
        return {"github": [], "hn": []}


def discover_from_github(mode):
    print("\n[GitHub] Searching AI business repos...")
    candidates = []
    days = 7 if mode == "weekly" else 1
    since = (datetime.datetime.utcnow() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")

    active = load_active_sources()
    queries = active["github"] if active["github"] else ["ai business framework OR llm business"]
    queries = list(dict.fromkeys(queries))

    seen_repos: set = set()
    for query in queries:
        url = f"{GITHUB_API}/search/repositories?q={query.replace(' ', '+')}+created:>{since}&sort=stars&per_page=10"
        data = fetch_json(url)
        if not data:
            time.sleep(1)
            continue
        for repo in data.get("items", []):
            name = repo.get("full_name", "")
            if name in seen_repos:
                continue
            stars = repo.get("stargazers_count", 0)
            if stars < 30:
                continue
            desc = repo.get("description") or "No description"
            candidates.append({
                "id": f"candidate_gh_{name.replace('/', '_').lower()}",
                "name": repo.get("name", ""),
                "description": desc[:120],
                "category": "ai_saas",
                "industries": ["software_dev"],
                "target_users": ["developer"],
                "blueprint_stage_relevance": ["step_10"],
                "business_model": "subscription_saas",
                "outcome": "Candidate — needs review",
                "lessons": ["Review README and issues"],
                "tags": repo.get("topics", [])[:5] or ["automation"],
                "source": repo.get("html_url", ""),
                "status": "candidate",
                "_meta": {"stars": stars, "source": "github", "query": query,
                          "discovered_at": datetime.datetime.utcnow().isoformat()}
            })
            seen_repos.add(name)
            print(f"  {name} ({stars} stars)")
        time.sleep(0.3)
    return candidates


def discover_from_hn(mode):
    print("\n[HN] Searching for AI business examples...")
    candidates = []
    days = 7 if mode == "weekly" else 1
    from_ts = int((datetime.datetime.utcnow() - datetime.timedelta(days=days)).timestamp())

    active = load_active_sources()
    hn_queries = active["hn"] if active["hn"] else [
        "Show HN AI SaaS", "Show HN AI service", "Ask HN AI business"
    ]
    hn_queries = list(dict.fromkeys(hn_queries))

    seen_ids: set = set()
    for kw in hn_queries:
        url = f"{HN_SEARCH_API}/search?query={kw.replace(' ', '+')}&numericFilters=created_at_i>{from_ts}&hitsPerPage=10"
        data = fetch_json(url)
        if not data:
            continue
        for hit in data.get("hits", []):
            obj_id = hit.get("objectID", "")
            if obj_id in seen_ids:
                continue
            points = hit.get("points", 0)
            if points < 15:
                continue
            title = hit.get("title", "")
            story_url = hit.get("url") or f"https://news.ycombinator.com/item?id={obj_id}"
            candidates.append({
                "id": f"candidate_hn_{obj_id}",
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
                "_meta": {"points": points, "source": "hacker_news", "query": kw,
                          "discovered_at": datetime.datetime.utcnow().isoformat()}
            })
            seen_ids.add(obj_id)
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
    candidates = []
    candidates.extend(discover_from_github(args.mode))
    candidates.extend(discover_from_hn(args.mode))
    save_candidates(candidates, args.dry_run)
    print("Done")


if __name__ == "__main__":
    main()
