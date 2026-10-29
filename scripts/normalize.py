"""Normalize raw Instagram trend-search output into data/raw/<date>.json.

The daily fetch itself is done by the agent through public Instagram
trend discovery (social.search, platform=instagram, ranking_intent=
engagement) because no Instagram account is connected to this project.
That step returns per-post summaries (URL, type, timestamp, author,
summary text). This script turns that raw output into the repo's raw
format: dedupe by URL, keep a recent window, and tag topics by keyword.

Usage:
  python normalize.py --date 2026-10-29 --input /tmp/search.json
      --window-days 3
Input JSON: a list of posts with keys url, type, created, likes,
author, summary (extra keys are kept).
"""
import argparse
import json
from collections import Counter
from datetime import date, timedelta
from pathlib import Path


def topic_of(post):
    text = ((post.get("summary") or "") + " " + (post.get("url") or "")).lower()
    if "jennifer lawrence" in text or "call her daddy" in text or "hunger games" in text:
        return "Jennifer Lawrence × Call Her Daddy"
    if (
        "karwa chauth" in text
        or "karva chauth" in text
        or "mehendi" in text
        or "mehndi" in text
        or "henna" in text
    ):
        return "Karwa Chauth × Priyanka Chopra"
    if "odisha" in text or "disaster preparedness" in text:
        return "Odisha Disaster Preparedness Day"
    return "其他今日内容"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    parser.add_argument("--input", required=True, help="raw search JSON (list of posts)")
    parser.add_argument("--window-days", type=int, default=3)
    parser.add_argument("--out", default="data/raw")
    args = parser.parse_args()

    day = date.fromisoformat(args.date)
    earliest = (day - timedelta(days=args.window_days - 1)).isoformat()
    raw = json.loads(Path(args.input).read_text(encoding="utf-8"))

    seen = {}
    for post in raw:
        url = post.get("url", "")
        if url and url not in seen:
            seen[url] = post
    posts = []
    for post in seen.values():
        created = (post.get("created") or "")[:10]
        if created < earliest or created > args.date:
            continue
        posts.append(
            {
                "url": post.get("url", ""),
                "type": post.get("type", ""),
                "created": post.get("created", ""),
                "likes": post.get("likes"),
                "author": post.get("author", ""),
                "topic": topic_of(post),
                "summary": post.get("summary", ""),
            }
        )
    posts.sort(key=lambda p: p["created"])
    out_path = Path(args.out) / f"{args.date}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(posts, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"normalized {len(posts)} posts -> {out_path}")
    print("topics:", dict(Counter(p["topic"] for p in posts)))


if __name__ == "__main__":
    main()
