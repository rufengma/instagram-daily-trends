# Instagram Daily Trends

Every day, we find what's trending on Instagram in fashion, home decor, and beauty — and paint it as a painterly animation.

## Today's Animation · 2026-11-07

![Today's animation](assets/latest.gif)

> In the animation: her curly hair sways softly, steam drifts up from her coffee mug, the fireplace flames flicker, the Christmas tree lights twinkle faintly, and the candle on the coffee table glows. The grain and brushstroke texture of the illustration is preserved all the way through — never smoothed out, never recolored. HD video version: [assets/latest.mp4](assets/latest.mp4). Still illustration: [assets/2026-11-07.png](assets/2026-11-07.png).

## Today's Trends

### 👗 Fashion — Burgundy faux fur goes floor-length — oversized coats, leopard print, November outfit montages

A 94K-like carousel leads with a floor-length oversized burgundy faux-fur coat worn over a sheer leopard-print bodysuit, and a 47K-like lookbook styles a light beige faux-fur hooded jacket open over a striped hoodie with pink sweatpants and silver sneakers. A 5.5K-like "NOVEMBER OUTFITS" montage cycles through about 15 layered looks — burgundy leather midi skirt, beige trench coat, burgundy double-breasted coat, fur-collar brown leather coat — past luxury storefronts, while the cropped brown faux-fur jacket over a black lace bralette keeps resurfacing in subway looks.

### 🛋️ Home Decor — Christmas decorating goes full burgundy-and-green — crystal trees, flocked trees, tree guides

A 4.6K-like "Decorate for Christmas with me" reel layers burgundy velvet bows, crystal trees, garland with lights over an arched mirror and stockings under a Santa-painting mantel; an 8.3K-like reel rebuilds a gift display beneath a black marble fireplace, and a 7.2K-like showroom tour assembles a white flocked tree with warm white lights. How-to content keeps pace — a 6.1K-like Michaels guide compares gold tinsel trees and mercury-glass ornaments — while an 11K-like "Dear 2027, I am ready" reel in red plaid pajamas already sets a New Year table.

### 💄 Beauty — "Winterkissed" makeup goes viral — glossy lips, heavy pink blush, shimmery pink eyes

The day's biggest beauty post is a 75K-like "winterkissed makeup" reel — voluminous curled brown hair, glossy lips, heavy pink blush, shimmery pink eyeshadow and winged liner. A 2.6K-like '90s plum tutorial skips bronzer entirely, pairing MERIT mauve cream shadow with a nude-brown liner, Poundcake plum gloss and Gucci berry blush, while a 3K-like fall routine layers Rhode Pocket Bronze with Westman Atelier contour for an everyday warm glow.

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

- [2026-11-07](data/2026-11-07.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-07.gif) · [Video](assets/2026-11-07.mp4)
- [2026-11-06](data/2026-11-06.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-06.gif) · [Video](assets/2026-11-06.mp4)
- [2026-11-05](data/2026-11-05.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-05.gif) · [Video](assets/2026-11-05.mp4)
- [2026-11-04](data/2026-11-04.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-04.gif) · [Video](assets/2026-11-04.mp4)
- [2026-11-03](data/2026-11-03.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-03.gif) · [Video](assets/2026-11-03.mp4)
- [2026-11-02](data/2026-11-02.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-02.gif) · [Video](assets/2026-11-02.mp4)
- [2026-11-01](data/2026-11-01.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-01.gif) · [Video](assets/2026-11-01.mp4)
- [2026-10-31](data/2026-10-31.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-31.gif) · [Video](assets/2026-10-31.mp4)
- [2026-10-30](data/2026-10-30.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-30.gif) · [Video](assets/2026-10-30.mp4)
- [2026-10-29](data/2026-10-29.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-29.gif) · [Video](assets/2026-10-29.mp4)
