# Instagram Daily Trends

Every day, we find what's trending on Instagram in fashion, home decor, and beauty — and paint it as a painterly animation.

## Today's Animation · 2026-11-04

![Today's animation](assets/latest.gif)

> In the animation: her hair sways softly, fireplace flames flicker, candle flames dance, lamplight shimmers, and steam drifts up from her coffee mug. The grain and brushstroke texture of the illustration is preserved all the way through — never smoothed out, never recolored. HD video version: [assets/latest.mp4](assets/latest.mp4). Still illustration: [assets/2026-11-04.png](assets/2026-11-04.png).

## Today's Trends

### 👗 Fashion — Autumn city-to-cabin layering — burgundy coats, camel trenches, cozy knits

Autumn dressing moves from city streets to cozy cabins: a viral New York lookbook cycles through a burgundy coat, camel trench, long gray coat and cream turtleneck with wide-leg pants, while a pastel knit set pairs oversized sweaters, plaid skirts, knee-high socks and teddy-bear-motif scarves and bags for cabin weekends, and a Paris carousel styles a brown cropped leather trench with black pants and pointed heels.

### 🛋️ Home Decor — Fall mantels and dried-botanical styling — pomegranates, eucalyptus, velvet pumpkins

The mantel is the fall focal point: one time-lapse builds a lush, asymmetrical garland of deep red foliage, berries and whole pomegranates over a stone fireplace, a popular home tour styles dried burgundy eucalyptus in a gold vase with velvet pumpkin pillows and brass accents, and a seasonal transformation layers pumpkin candles, dried botanicals and plush pumpkin pillows around a lit fireplace.

### 💄 Beauty — Toasty fall makeup — warm bronzer, terracotta blush, soft brown eyes

Fall makeup turns toasty and warm: a beginner tutorial builds a sun-kissed look with bronzer placed high on the cheekbones, temples and forehead, a toasty reddish-terracotta blush and brown eyeshadow, while a soft fall routine pairs brown liner and a soft wing with cream blush, nude-brown glossy lips and shimmery lids, and a first-fall-look tutorial keeps it soft with cream blush, cafe-toned eyeshadow and a chocolate balm.

## How It Works, Every Day

1. **Discover trends**: find what's currently popular on Instagram in fashion, home decor, and beauty through public trend discovery, ranked by engagement.
2. **Illustration**: paint one illustration that weaves the day's trends into a single scene — painterly style (grain, loose brushstrokes, muted palette).
3. **Animation**: turn the illustration into a 10-second animation (hair, flames, light all moving) and embed it at the top of the README as an autoplaying GIF, with the HD video linked alongside.
4. **Archive**: the day's trends are saved as `data/YYYY-MM-DD.json`; the illustration and animation as `assets/YYYY-MM-DD.png` / `.mp4` / `.gif`.

## Data Notes (Please Read First)

- **Data source**: public Instagram trend discovery. No Instagram account is connected. This project is not affiliated with Instagram / Meta.
- **What this is**: a sketch of what is popular in these three domains right now — not a platform-wide census, and not a ranking of all trends.
- **Illustration and animation**: both AI-generated. The illustration style reference is a private image and is not included in this repo.

## Repo Structure

```
instagram-daily-trends/
├── README.md                  # Today's animation + today's trends (updated daily)
├── assets/
│   ├── latest.gif             # Latest day's animation (autoplaying)
│   ├── latest.mp4             # Latest day's animation (HD video)
│   ├── YYYY-MM-DD.gif         # Each day's animation
│   ├── YYYY-MM-DD.mp4         # Each day's animation (HD video)
│   └── YYYY-MM-DD.png         # Each day's illustration
├── data/
│   └── YYYY-MM-DD.json        # Each day's trends (fashion / home decor / beauty)
└── scripts/
    └── run_daily.py           # Daily pipeline checklist + output verification
```

## Archive

- [2026-11-04](data/2026-11-04.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-04.gif) · [Video](assets/2026-11-04.mp4)
- [2026-11-03](data/2026-11-03.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-03.gif) · [Video](assets/2026-11-03.mp4)
- [2026-11-02](data/2026-11-02.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-02.gif) · [Video](assets/2026-11-02.mp4)
- [2026-11-01](data/2026-11-01.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-01.gif) · [Video](assets/2026-11-01.mp4)
- [2026-10-31](data/2026-10-31.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-31.gif) · [Video](assets/2026-10-31.mp4)
- [2026-10-30](data/2026-10-30.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-30.gif) · [Video](assets/2026-10-30.mp4)
- [2026-10-29](data/2026-10-29.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-29.gif) · [Video](assets/2026-10-29.mp4)
