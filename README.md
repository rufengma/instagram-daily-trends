# Instagram Daily Trends

Every day, we find what's trending on Instagram in fashion, home decor, and beauty — and paint it as a painterly animation.

## Today's Animation · 2026-11-06

![Today's animation](assets/latest.gif)

> In the animation: her hair sways softly, the fireplace and candle flames flicker, lamplight shimmers, steam drifts up from her coffee mug, and the Christmas tree lights twinkle faintly. The grain and brushstroke texture of the illustration is preserved all the way through — never smoothed out, never recolored. HD video version: [assets/latest.mp4](assets/latest.mp4). Still illustration: [assets/2026-11-06.png](assets/2026-11-06.png).

## Today's Trends

### 👗 Fashion — Faux-fur cropped jackets and the viral "style different fonts" challenge — brown faux fur, zebra print, baroque puffers

Fur keeps dominating the November feed: a carousel posted today (15K likes) pairs a voluminous brown faux-fur cropped jacket with light-wash wide-leg jeans and black-and-white zebra-print pointed shoes; a 17K-like subway reel wears a cropped brown faux-fur coat open over a black lace bralette, and a 7.4K-like carousel centers a leopard-print faux-fur jacket with low-rise jeans. Meanwhile the week's biggest fashion viral (770K likes) is a creator styling nine outfits as typefaces — Times New Roman as a pinstripe suit, Impact as tactical streetwear, Papyrus as bohemian layers, Futura as all-white tech — and Supreme's fall/winter lookbook (28K likes) leans on baroque-print puffers, Fair Isle cardigans and fur trapper hats.

### 🛋️ Home Decor — Christmas decor takes over in early November — red velvet trees, Dollar Tree hauls, Thanksgiving tablescapes

The feed flipped to Christmas fast: a 64K-like carousel centers a tall tree in red velvet ribbons, heart ornaments, red berries and warm white lights with gold reindeer statues at its base, a 44K-like cinematic "Our Home at Christmas" tour layers wreaths, garlands, red taper candles and a chandelier wrapped in greenery, and a 15K-like reel catches a partner who fully decorated the house by November 2. Budget hauls ride along — a 17K-like Dollar Tree roundup of $1.25 pine-tree dinnerware, velvet ribbon trees and $1 velvet ornaments — while Thanksgiving still gets its moment: a 21K-like reel builds a centerpiece from a white-pumpkin vase of hydrangeas and pumpkin candle holders with pinecones and pears.

### 💄 Beauty — Brown lip combos lead the fall glam — espresso lips, cream blush, warm eyes

Brown lips are the defining fall look: a 39K-like tutorial swatches a KIKO Milano brown liner, matte brown lipstick and shimmery gloss as "my brown fall lip combo," and a 29K-like "lip combo for november" layers a MAC pencil with Rhode's Peptide Lip Treatment from a pumpkin-shaped case. Warm glam fills out the rest — a 21K-like warm fall tutorial pairs pink cream blush with a JUDYDOLL eye palette and CANMAKE mascara, a 41K-like routine centers Charlotte Tilbury pink blush with Airbrush setting spray, and a 71K-like GRWM builds a Qawali-night look with defined eyes, rosy cheeks and glossy lips.

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

- [2026-11-06](data/2026-11-06.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-06.gif) · [Video](assets/2026-11-06.mp4)
- [2026-11-05](data/2026-11-05.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-05.gif) · [Video](assets/2026-11-05.mp4)
- [2026-11-04](data/2026-11-04.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-04.gif) · [Video](assets/2026-11-04.mp4)
- [2026-11-03](data/2026-11-03.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-03.gif) · [Video](assets/2026-11-03.mp4)
- [2026-11-02](data/2026-11-02.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-02.gif) · [Video](assets/2026-11-02.mp4)
- [2026-11-01](data/2026-11-01.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-01.gif) · [Video](assets/2026-11-01.mp4)
- [2026-10-31](data/2026-10-31.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-31.gif) · [Video](assets/2026-10-31.mp4)
- [2026-10-30](data/2026-10-30.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-30.gif) · [Video](assets/2026-10-30.mp4)
- [2026-10-29](data/2026-10-29.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-10-29.gif) · [Video](assets/2026-10-29.mp4)
