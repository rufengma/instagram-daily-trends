# Instagram Daily Trends

Every day, we find what's trending on Instagram in fashion, home decor, and beauty — and paint it as a painterly animation.

## Today's Animation · 2026-10-29

![Today's animation](assets/latest.gif)

> In the animation: her hair sways softly, fireplace and candle flames flicker, chandelier light shimmers. The grain and brushstroke texture of the illustration is preserved all the way through — never smoothed out, never recolored. HD video version: [assets/latest.mp4](assets/latest.mp4). Still illustration: [assets/2026-10-29.png](assets/2026-10-29.png).

## Today's Trends

### 👗 Fashion — Fall outfit vibes: layered autumn dressing

Oversized knit sweaters, turtlenecks, blazers, trench coats and wool coats, wide-leg trousers, pleated midi skirts, loafers, ballet flats and ankle boots — in neutral tones: navy, brown, black, beige, olive.

### 🛋️ Home Decor — Cozy fall living rooms

White sectional sofas, chunky knit blankets, lit candles, chandeliers, wood ceilings and fireplaces; a warm, inviting autumn atmosphere. A second popular thread: moody makeovers with dark fireplaces, cognac leather sofas, Persian-style rugs, brass accents and velvet curtains.

### 💄 Beauty — 2026 soft natural makeup vs 2016 glam

The 2026 look: softer defined brows, breathable "porcelain doll" skin, lifted concealer instead of heavy contour, soft-sculpted blush, glam half-lash, targeted highlight, fuller lips finished with gloss. Nostalgia for 2016 full glam runs alongside it.

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

- [2026-10-29](data/2026-10-29.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-29.gif) · [Video](assets/2026-10-29.mp4)
