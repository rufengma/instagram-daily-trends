# Instagram Daily Trends

Every day, we find what's trending on Instagram in fashion, home decor, and beauty — and paint it as a painterly animation.

## Today's Animation · 2026-11-05

![Today's animation](assets/latest.gif)

> In the animation: her hair sways softly, the fireplace and candle flames flicker, lamplight shimmers, and steam drifts up from her coffee mug. The grain and brushstroke texture of the illustration is preserved all the way through — never smoothed out, never recolored. HD video version: [assets/latest.mp4](assets/latest.mp4). Still illustration: [assets/2026-11-05.png](assets/2026-11-05.png).

## Today's Trends

### 👗 Fashion — November fur trim and animal print — fur-trimmed coats, pencil mini skirts

November belongs to fur trim and animal print: a November 2026 trends roundup spotlights matching fur-trimmed capes and skirts plus animal-print coats with fur trim — a fur scarf tied at the waist works as the no-buy version — while a New York fall-fashion segment (60K likes) shows a tiger-print faux-fur coat over a pink dress, a bold red power suit and cobalt blue, and a style-predictions carousel forecasts striped socks with ballet flats and vintage L.L.Bean fleeces.

### 🛋️ Home Decor — The November decor flip and Thanksgiving tables — cozy holiday styling, gold/burgundy/sage

November 1 flips the house from fall to cozy holiday: one 11K-like reel swaps autumn styling for Christmas touches overnight, a fall decorating finale layers sequin runners, pampas grass, a lit fall tree and a plush pumpkin on the sofa, and a Thanksgiving table tour builds three looks on one small table — Classic Gold, Rich Burgundy and Modern Sage — around a fruit-and-flower centerpiece.

### 💄 Beauty — Toasty fall glam — warm brown eyes, cream blush, glossy brown lips

Fall glam turns toasty: a 'Toasty Fall Girl Glam' routine builds a warm look with foundation, concealer, cream blush, warm brown eyeshadow and false lashes, a soft autumn routine pairs a liquid base with cream blush, powder bronzer and shimmery winged liner, and a fall lip-combo tutorial cycles through brown liner-and-gloss pairings, while an 8.2K-like autumn makeup tutorial layers pink cream blush with bronzer and false lashes.

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

- [2026-11-05](data/2026-11-05.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-05.gif) · [Video](assets/2026-11-05.mp4)
- [2026-11-04](data/2026-11-04.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-04.gif) · [Video](assets/2026-11-04.mp4)
- [2026-11-03](data/2026-11-03.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-03.gif) · [Video](assets/2026-11-03.mp4)
- [2026-11-02](data/2026-11-02.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-02.gif) · [Video](assets/2026-11-02.mp4)
- [2026-11-01](data/2026-11-01.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-01.gif) · [Video](assets/2026-11-01.mp4)
- [2026-10-31](data/2026-10-31.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-31.gif) · [Video](assets/2026-10-31.mp4)
- [2026-10-30](data/2026-10-30.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-30.gif) · [Video](assets/2026-10-30.mp4)
- [2026-10-29](data/2026-10-29.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-29.gif) · [Video](assets/2026-10-29.mp4)
