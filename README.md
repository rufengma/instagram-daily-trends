# Instagram Daily Trends

Every day, we find what's trending on Instagram in fashion, home decor, and beauty — and paint it as a painterly animation.

## Today's Animation · 2026-11-02

![Today's animation](assets/latest.gif)

> In the animation: her hair sways softly, fireplace and candle flames flicker, chandelier light shimmers, and steam drifts up from her coffee cup. The grain and brushstroke texture of the illustration is preserved all the way through — never smoothed out, never recolored. HD video version: [assets/latest.mp4](assets/latest.mp4). Still illustration: [assets/2026-11-02.png](assets/2026-11-02.png).

## Today's Trends

### 👗 Fashion — Layered fall outfits, just add layers — lace peeking under sweaters

November layering is all about the details: sheer lace tops peeking out at the neckline and wrists under oversized sweaters and argyle knits, brown suede jackets over flared jeans, and knee-high boots to finish. One viral styling trick layers an oversized top over a striped long-sleeve shirt, tying the shirt at the waist for an asymmetrical skirt effect in three colorways, while a "just add layers" London lookbook pairs the same suede-and-argyle formula with a tote and sunglasses.

### 🛋️ Home Decor — Warm-lit evening living rooms, chandeliers and fireplaces

Evening living rooms glow without going overboard on pumpkins: light-colored sectionals with brown and cream pillows and chunky knit throws, lit fireplaces topped with gold-framed mirrors, crystal chandeliers, and candles and dried hydrangeas and eucalyptus on coffee tables. Slow panning tours at night show the same formula — warm lamp and candlelight, dark wood beams and coffee tables, gallery walls — with one creator proudly noting "not a pumpkin in sight" for a more refined fall look.

### 💄 Beauty — Toasty fall makeup, warm and sun-kissed

Toasty fall makeup is the warm, sun-kissed look beginners are copying: hydrating skincare first, bronzer placed high on cheekbones, temples and forehead and blended into the hairline, terracotta and toasted-teddy blush with pumpkin-and-cinnamon undertones, brown eyeshadow tapped on the lids, tightlined eyes, faux freckles, and glossy nude lips. A 180K-like full-face tutorial follows the same soft-glam grammar — primer, satin foundation, color-correcting concealer, liquid blush, smoky eyes with winged liner, and lip gloss on top.

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

- [2026-11-02](data/2026-11-02.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-02.gif) · [Video](assets/2026-11-02.mp4)
- [2026-11-01](data/2026-11-01.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-01.gif) · [Video](assets/2026-11-01.mp4)
- [2026-10-31](data/2026-10-31.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-31.gif) · [Video](assets/2026-10-31.mp4)
- [2026-10-30](data/2026-10-30.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-30.gif) · [Video](assets/2026-10-30.mp4)
- [2026-10-29](data/2026-10-29.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-29.gif) · [Video](assets/2026-10-29.mp4)
