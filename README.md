# Instagram Daily Trends

Every day, we find what's trending on Instagram in fashion, home decor, and beauty — and paint it as a painterly animation.

## Today's Animation · 2026-11-13

![Today's animation](assets/latest.gif)

> In the animation: her long wavy hair sways softly, the candle flames on the mantel flicker, the fairy lights on the maximalist tree and the garland twinkle, snow falls slowly outside the window, and the glitter on her eyelids sparkles. The grain and brushstroke texture of the illustration is preserved all the way through — never smoothed out, never recolored. HD video version: [assets/latest.mp4](assets/latest.mp4). Still illustration: [assets/2026-11-13.png](assets/2026-11-13.png).

## Today's Trends

### 👗 Fashion — Let him pick the dress — 'help me choose' reels take over party season

A 35K-like reel plays 'Letting my husband pick my dress for a holiday party' — a metallic bronze pleated gown with a deep V and side cutouts ('struck gold,' 'Studio 54'), a black sparkly strapless gown with a thigh-high slit, and a burgundy velvet strapless mermaid dress with a bow; he picks the black one. A 14K-like reel presents three Windsor Holiday Party options — a black strapless mini with a white bow and puffy skirt, a floor-length burgundy sparkly gown with a deep V, and a black off-the-shoulder mini with a sheer train — and asks viewers to vote. A 7.5K-like 'Holiday Dress Round Up' models eight dresses, from a light-blue feather halter mini and a black sparkly halter mini to a navy off-the-shoulder mermaid gown, a gold sequined mini, a red feather mini, satin bubble-skirt dresses in black and red, and a white feather sleeveless mini. A 6.6K-like reel turns to Meta AI for a 70s-themed Las Vegas wedding guest look and lands on a lime-green sequin halter mini with gold platform heels and gold jewelry. A 4K-like 'help me pick my festive dress' reel tries an emerald green sequined gown with a black velvet bodice, a black sleeveless maxi with a sheer overlay, and a burgundy sequined midi with a thigh slit. A 3.4K-like carousel closes the night out in Manila — dark teal velvet, sequined dresses and midi skirts with slits at a mirrored-wall venue.

### 🛋️ Home Decor — Maximalist Christmas trees take over — 5,000 lights, 1,000 ornaments, and 'collected, not coordinated'

A 65K-like reel documents a 'dream maximalist Christmas tree' — four days, 5,000 lights and 1,000 ornaments, vintage shiny Brite balls, Santa figures, reindeer, snowmen and glittery poinsettias packed onto a pre-lit tree under a star topper. A 35K-like reel starts the season with three friends assembling a tall artificial tree in a gold-and-white theme — oversized reflective gold baubles, gold bells, poinsettias and a star topper, plus garlands, nutcrackers and bottle-brush trees. A 17K-like carousel names the 'CHRISTMAS TREE TRENDS 2026': metallic lametta tinsel, paper chains, 'collected, not coordinated' maximalism, alternative trees, and DIY decorations. A 14K-like reel leans traditional — deep red velvet ribbons, burgundy berries, cream and gold baubles, pinecones and warm white lights under a large gold star, 'All I Want This Year is a Traditional Christmas.' A 14K-like Anthropologie/terrain carousel tours trees in red-and-white striped bows, pastel ornaments and a bright pink-themed tree. A 13K-like family tour opens on a flocked white tree with gold ornaments, red velvet bows and red berries, the family in matching teal reindeer pajamas.

### 💄 Beauty — Snowy fairy eyes and champagne glam on a drugstore budget

A 28K-like tutorial builds a 'bright beautiful snowy fairy angel' eye — a soft brown base, white concealer cut into a new lid shape, white eyeshadow packed across the lid and inner corner, Fenty Diamond Bomb pressed on top for a snowy sparkle. A 14K-like clip pairs a close-up makeup application with an Emporio Armani 'POWER OF YOU' perfume moment in front of a lit Christmas tree, fur coat on. A 7.9K-like 'Champagne Glam on a Drugstore Budget' tutorial runs a full face on e.l.f., L'Oreal, CoverGirl and Maybelline, finishing with body shimmer and a velcro roller. A 7.8K-like tutorial layers a green-and-pink duochrome shadow with dark glitter, silver metallic inner corners and KIKO MILANO mascara for a dramatic glittery eye. A 7.8K-like unboxing opens the e.l.f. 'Express Your E.L.F.' Advent Calendar — 24 doors of palettes, balms, serums and lip oils. A 7.6K-like clip pitches the Kiko Milano Twist & Twinkle Holiday Edition 3D Extreme Lip Gloss as the $16 'extra' for holiday parties.

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

- [2026-11-13](data/2026-11-13.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-13.gif) · [Video](assets/2026-11-13.mp4)
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
