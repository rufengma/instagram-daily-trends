"""Daily pipeline checklist and output verification for instagram-daily-trends.

The repo no longer analyzes mood. Each day, the agent:
  1. Discovers what is currently trending on Instagram in fashion,
     home decor, and beauty (public trend discovery, ranked by
     engagement; no account connected).
  2. Paints one painterly illustration weaving the day's trends into
     a single scene (grain and brushstrokes preserved; style
     reference is a private image, never committed).
  3. Animates the illustration image-to-video (gentle motion, fixed
     camera, texture preserved), converts the mp4 to an autoplaying
     GIF with ffmpeg, and saves assets/<date>.png/.mp4/.gif plus
     assets/latest.* copies.
  4. Writes data/<date>.json (trends) and updates README.md in
     English, with the GIF embedded as the primary animation and
     the HD mp4 linked alongside.

Usage:
  python run_daily.py --date 2026-10-29

It verifies that the day's outputs exist and that README.md mentions
the date. It does not generate anything itself.
"""
import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    missing = []
    for rel in [
        f"assets/{args.date}.png",
        f"assets/{args.date}.mp4",
        f"assets/{args.date}.gif",
        f"assets/latest.gif",
        f"assets/latest.mp4",
        f"data/{args.date}.json",
    ]:
        if not (root / rel).exists():
            missing.append(rel)
    readme = (root / "README.md").read_text(encoding="utf-8")
    if args.date not in readme:
        missing.append("README.md mention of date")
    if missing:
        print(f"daily outputs incomplete for {args.date}: missing {', '.join(missing)}")
        sys.exit(1)
    print(f"daily outputs verified for {args.date}: illustration, animation, GIF, data, README")


if __name__ == "__main__":
    main()
