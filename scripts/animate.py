"""Animate a daily illustration into a GIF for instagram-daily-mood.

Motion: a slow zoom-in with a gentle pan, floating decorative shapes
(hearts / stars / sparkles) drifting upward, and a bottom banner with
the date and the day's dominant emotion.

Usage:
  python animate.py --image assets/2026-10-29.png --date 2026-10-29
      --emotion joy --out assets/2026-10-29.gif [--also-latest assets/latest.gif]

Chinese overlay text uses a CJK font when one is available on the
system (Noto Sans/Serif CJK); the daily banner is English-only so it
renders everywhere without a CJK font.
"""
import argparse
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

EMOTION_EN = {
    "joy": "Joy",
    "anger": "Anger",
    "sadness": "Sadness",
    "fear": "Fear",
    "surprise": "Surprise",
    "disgust": "Disgust",
    "neutral": "Neutral",
}

FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/noto/NotoSansCJKsc-Regular.otf",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansCJKsc-Regular.otf",
    "/usr/share/fonts/opentype/noto/NotoSerifCJKsc-Bold.otf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]
CJK_FONTS = [p for p in FONT_CANDIDATES if "CJK" in p]


def load_font(size):
    """Return (font, has_cjk). Prefer a CJK font so Chinese renders."""
    for path in FONT_CANDIDATES:
        try:
            return ImageFont.truetype(path, size), ("CJK" in path)
        except OSError:
            continue
    return ImageFont.load_default(), False


def draw_heart(draw, cx, cy, r, fill):
    draw.polygon(
        [
            (cx, cy + r * 0.9),
            (cx - r, cy - r * 0.2),
            (cx - r * 0.5, cy - r * 0.9),
            (cx, cy - r * 0.3),
            (cx + r * 0.5, cy - r * 0.9),
            (cx + r, cy - r * 0.2),
        ],
        fill=fill,
    )


def draw_star(draw, cx, cy, r, fill):
    points = []
    for i in range(10):
        angle = -math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.45
        points.append((cx + rad * math.cos(angle), cy + rad * math.sin(angle)))
    draw.polygon(points, fill=fill)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--emotion", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--also-latest", default="")
    parser.add_argument("--frames", type=int, default=24)
    parser.add_argument("--duration", type=int, default=110)
    args = parser.parse_args()

    base = Image.open(args.image).convert("RGB")
    width, height = base.size
    font_big, has_cjk = load_font(max(28, width // 22))
    font_small, _ = load_font(max(20, width // 32))

    name = EMOTION_EN.get(args.emotion, args.emotion)
    banner_main = f"{args.date} · {name.upper()}"
    banner_sub = f"Dominant emotion: {args.emotion}"

    random.seed(29)
    floaters = []
    for _ in range(14):
        floaters.append(
            {
                "x": random.uniform(0.05, 0.95),
                "y": random.uniform(0.15, 0.95),
                "r": random.uniform(8, 20),
                "speed": random.uniform(0.004, 0.011),
                "shape": random.choice(["heart", "star", "dot"]),
                "alpha": random.randint(120, 200),
            }
        )

    frames = []
    for i in range(args.frames):
        t = i / args.frames
        # Slow zoom-in (1.00 -> 1.08) with a gentle downward pan.
        zoom = 1.0 + 0.08 * t
        crop_w, crop_h = int(width / zoom), int(height / zoom)
        left = int((width - crop_w) * 0.5)
        top = int((height - crop_h) * (0.35 + 0.15 * t))
        frame = base.crop((left, top, left + crop_w, top + crop_h)).resize((width, height), Image.LANCZOS)
        overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        for f in floaters:
            y = (f["y"] - f["speed"] * i) % 1.0
            x = f["x"] + 0.01 * math.sin(i * 0.35 + f["r"])
            px, py = int(x * width), int(y * height)
            col = (255, 255, 255, f["alpha"])
            if f["shape"] == "heart":
                draw_heart(draw, px, py, int(f["r"]), col)
            elif f["shape"] == "star":
                draw_star(draw, px, py, int(f["r"]), col)
            else:
                draw.ellipse([px - f["r"] // 2, py - f["r"] // 2, px + f["r"] // 2, py + f["r"] // 2], fill=col)
        frame = Image.alpha_composite(frame.convert("RGBA"), overlay).convert("RGB")
        # Bottom banner.
        draw = ImageDraw.Draw(frame, "RGBA")
        band_h = int(height * 0.16)
        draw.rectangle([0, height - band_h, width, height], fill=(0, 0, 0, 140))
        for text, font, y_off in [(banner_main, font_big, 0.06), (banner_sub, font_small, 0.52)]:
            bbox = draw.textbbox((0, 0), text, font=font)
            tw = bbox[2] - bbox[0]
            draw.text(((width - tw) // 2, height - band_h + int(band_h * y_off)), text, font=font, fill=(255, 255, 255))
        frames.append(frame)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=args.duration, loop=0)
    if args.also_latest:
        latest = Path(args.also_latest)
        latest.parent.mkdir(parents=True, exist_ok=True)
        frames[0].save(latest, save_all=True, append_images=frames[1:], duration=args.duration, loop=0)
    print(f"wrote {out_path} ({args.frames} frames, cjk={has_cjk})")


if __name__ == "__main__":
    main()
