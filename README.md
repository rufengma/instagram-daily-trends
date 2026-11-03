# Instagram Daily Trends

Every day, we find what's trending on Instagram in fashion, home decor, and beauty — and paint it as a painterly animation.

## Today's Animation · 2026-11-03

![Today's animation](assets/latest.gif)

> In the animation: her hair sways softly, fireplace and wood-stove flames flicker, chandelier light shimmers, candle flames dance, and steam drifts up from her coffee mug. The grain and brushstroke texture of the illustration is preserved all the way through — never smoothed out, never recolored. HD video version: [assets/latest.mp4](assets/latest.mp4). Still illustration: [assets/2026-11-03.png](assets/2026-11-03.png).

## Today's Trends

### 👗 Fashion — Statement-coat layering — fur cuffs, belted coats, leopard

Statement outerwear is doing the talking in fall layering: a viral NYC street montage cycles through a burgundy cropped jacket with large fur cuffs over wide-leg jeans, a long brown belted coat, a black fringed coat, and a leopard-print peplum jacket, while luxury lookbooks pile on long coats, capes, trench coats and fur accents over layered knits, with designer totes and gloves to finish.

### 🛋️ Home Decor — Cozy autumn-evening living rooms — candlelight, chandeliers, wood stoves

Post-Halloween living rooms settle into warm evening coziness: tufted sofas with chunky knit throws and dark green pillows, lit fireplaces under gold-framed mirrors, crystal chandeliers, candles and fairy lights, wood-burning stoves, and coffee tables styled with dried hydrangeas and eucalyptus. Slow evening tours lean into lamp and candlelight rather than seasonal kitsch.

### 💄 Beauty — Fall makeup diaries — skin tints, cream blush, plum and burgundy

Fall makeup diaries keep it wearable: affordable base routines built on gripping primer, skin tint and liquid contour, cream blush blended with a sponge, softly lined eyes and mascara — then a bolder turn for fall and winter with deep plum and burgundy eyeshadow, flushed blush, and dark glossy burgundy lips.

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

- [2026-11-03](data/2026-11-03.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-03.gif) · [Video](assets/2026-11-03.mp4)
- [2026-11-02](data/2026-11-02.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-02.gif) · [Video](assets/2026-11-02.mp4)
- [2026-11-01](data/2026-11-01.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-01.gif) · [Video](assets/2026-11-01.mp4)
- [2026-10-31](data/2026-10-31.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-31.gif) · [Video](assets/2026-10-31.mp4)
- [2026-10-30](data/2026-10-30.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-30.gif) · [Video](assets/2026-10-30.mp4)
- [2026-10-29](data/2026-10-29.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-29.gif) · [Video](assets/2026-10-29.mp4)
