# Instagram Daily Trends

Every day, we find what's trending on Instagram in fashion, home decor, and beauty — and paint it as a painterly animation.

## Today's Animation · 2026-11-11

![Today's animation](assets/latest.gif)

> In the animation: her long wavy hair sways softly, the candle flames flicker, the fairy lights on the flocked tree and the pink tree in the doorway twinkle, snow falls slowly outside the window, and the glitter on her eyelids sparkles. The grain and brushstroke texture of the illustration is preserved all the way through — never smoothed out, never recolored. HD video version: [assets/latest.mp4](assets/latest.mp4). Still illustration: [assets/2026-11-11.png](assets/2026-11-11.png).

## Today's Trends

### 👗 Fashion — Sequin party season rolls on — black sequin minis, velvet wraps, and a 'put down the sequins' backlash

Sequin party season rolls on, with velvet as its softer twin — and one voice pushing back. A 2.9K-like reel walks a black sequined mini-dress with a plunging V-neck and high side slit under a long black coat through golden-hour smoke, shot like a perfume ad. A 2.5K-like carousel answers 'What to wear for the party season' with six looks: a dark velvet wrap blazer with wide-leg jeans, a bronze velvet wrap dress, a leopard coat over a bright red ruched top, a burgundy puff-sleeve dress with knee-high boots, a navy cap-sleeve top with white lace trim, and a silver sequin fit-and-flare mini. A 1.9K-like 20-slide carousel runs through holiday outfit ideas — a long black sequined gown, a sheer black lace top, a strapless burgundy velvet mini, a red turtleneck with sequin shorts, a black velvet jumpsuit, a red satin fringe mini and an emerald velvet wrap jumpsuit — plus a glitter stick for legs 'like Barbie'. A 1.1K-like reel from a New York hotel room tries on plus-size party picks: a red sequin mini, burgundy sequin wide-leg pants, a navy velvet fit-and-flare dress and a silver sequin asymmetric midi skirt. The counterpoint comes in a 49-like guide advising viewers to 'put down the sequins' for a black velvet blazer with feather-trim cuffs, wide-leg trousers and patent heels. A 42-like 'Styling Sequins' guide mixes black sequin separates over a white shirt, a silver sequin midi skirt, and burgundy sequin wide-leg trousers with a fuzzy grey sweater.

### 🛋️ Home Decor — Dark by 5pm, lights up — cozy Christmas tours, flocked trees, and a break from beige

Dark by 5pm, lights up: cozy Christmas home tours take over. A 15K-like evening tour opens on the line 'It's dark by 5:00pm because you're supposed to have your Christmas lights up' — a lit tree with red bows and plaid ornaments, a mantel of village houses and candles, stockings, and two children in pajamas watching a snowy movie under blankets. A 13K-like cinematic walkthrough tours an opulent home in whites, blacks and golds, with fresh garlands strung with warm fairy lights and several trees in cream ribbons and gold and silver ornaments. A 2.6K-like flocked-tree setup dresses the tree in red, green and gold ornaments and plaid baubles with personalized family ornaments, declaring the creator is 'tired of the beige aesthetic' and leaning into 1990s Christmas nostalgia. A 1.8K-like Virginia home carousel layers greenery and dried orange slices, copper pans, a tabletop tree and a nutcracker vignette — 'creating the backdrop to our memories'. A 1.2K-like snap-transition montage reveals a different decorated tree in every room: a pink tree in the bedroom, red-and-gold on the landing, burgundy in the dining room, a flocked green-and-gold tree, and a navy-blue, gold and white tree in the foyer. A 500-like tour leans opulent — red velvet throws, gold reindeer, a crystal chandelier. A 340-like guide builds a Hallmark-style cozy home with red chandelier shades, chunky knit throws, wreaths with long red ribbons and poinsettias.

### 💄 Beauty — Glitter goes everywhere — frosty lilac eyes, peppermint pink, and gingerbread face paint

Glitter goes everywhere this holiday season. A 15K-like reel markets a 'HOLIDAY GLOW-UP ESSENTIAL GLINT GLITTER' — an iridescent glitter gel dabbed under the eyes, worn with leopard-print nails, a red lip and winged liner. A 2.3K-like Marc Jacobs holiday glam tutorial builds an icy smoky eye with star-shaped palettes, 'Joystick Blush' and a red 'Love Muscle' lipstick. A 1.2K-like vlog paints a whole gingerbread house on one cheek — white icing lines, red and green details — ahead of a gingerbread-making party. A 700-like 'Peppermint Sugar Eyes' tutorial blends bright pink into the crease, presses silver glitter onto the lid, adds a sharp wing and finishes with a berry-red matte lip. A 550-like look offers frosty lilac eyeshadow as the alternative to metallics: a lavender stick layered with purple glitter, silver inner corners and black mascara. A 310-like soft winter look pairs a lavender-purple shadow with rosy cheeks and glossy lips. A 220-like Hourglass demo shows the Scattered Light Glitter Eyeshadow in 'Ray' blended onto the lid for a holiday eye.

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

- [2026-11-11](data/2026-11-11.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-11.gif) · [Video](assets/2026-11-11.mp4)
- [2026-11-10](data/2026-11-10.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-10.gif) · [Video](assets/2026-11-10.mp4)
- [2026-11-09](data/2026-11-09.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-09.gif) · [Video](assets/2026-11-09.mp4)
- [2026-11-08](data/2026-11-08.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-08.gif) · [Video](assets/2026-11-08.mp4)
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
