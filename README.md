# Instagram Daily Trends

Every day, we find what's trending on Instagram in fashion, home decor, and beauty — and paint it as a painterly animation.

## Today's Animation · 2026-11-14

![Today's animation](assets/latest.gif)

> In the animation: her long wavy hair sways softly, the candle flames on the mantel flicker, the fairy lights and tree lights twinkle, snow falls slowly outside the window, the tiny train circles the Christmas village at the tree's base, and the glitter on her eyelids sparkles. The grain and brushstroke texture of the illustration is preserved all the way through — never smoothed out, never recolored. HD video version: [assets/latest.mp4](assets/latest.mp4). Still illustration: [assets/2026-11-14.png](assets/2026-11-14.png).

## Today's Trends

### 👗 Fashion — Camel overcoats and pinstripe tailoring lead the fall lookbook wave

A 220K-like carousel presents an Ami Paris Fall/Winter lookbook — a male model in a long camel overcoat over a brown pinstripe three-piece suit with an unbuttoned red-and-white striped shirt and black boots, posed at a bright white colonial-style building; the set closes with a handwritten card from the runway and a close-up of the garments. A 21K-like carousel models Tommy Hilfiger fall outfits around New York — a black pantsuit with a burgundy blouse, a tan coat with a fur collar, a varsity jacket over a white blouse with a plaid midi skirt, and a maroon varsity jacket with plaid wide-leg pants. A 17K-like reel cycles through fall/winter layering looks — a plaid shirt-dress with a grey cable-knit sweater, a cream off-the-shoulder cable-knit sweater dress with a grey plaid coat and knee-high boots, a mint-green fuzzy peplum cardigan, a brown ribbed midi dress under a faux-fur wrap coat, and a cream Fair Isle sweater with a tweed cape. An 18K-like carousel builds three fall-winter outfits around a black-and-white houndstooth fringed coat-dress with bright red stilettos, a black faux-leather top with a tiger-stripe midi skirt, and a monochromatic bright-red faux-leather ensemble with a beret. A 13K-like carousel styles a coordinated maroon look — a ribbed cropped knit cardigan with fringe cuffs, matching stirrup leggings, burgundy leather gloves and a black Dior saddle bag. A 13K-like carousel documents a SpaceNK Christmas getaway party — matching red Santa-print pajamas, burgundy party outfits, a shiny silver puffer over a red knit romper, and a long fitted burgundy dress.

### 🛋️ Home Decor — It's dark by 5pm — maximalist Christmas lights go up early

A 190K-like reel tours a cozy maximalist Christmas home — a woman on a step ladder tops a huge tree covered in multicolor lights and vintage-style ornaments, with the on-screen line "It's dark by 5pm because you're supposed to have your christmas lights up"; the camera pans across pink striped curtains, garlands with colored bulbs, a dining table with reindeer figurines and gingerbread decor, and a garland-draped kitchen. A 59K-like reel unpacks holiday decor from a storage bin in white Christmas pajamas — pinecones, gold-wrapped ornaments, brass bells, black metal reindeer, wooden trees and greenery garlands — building a coffee-table centerpiece, a mantel garland with bells, stockings, a wreath on a round mirror and miniature lit ceramic houses. A 36K-like reel pushes through a doorway framed in dense silver tinsel garland covered in ornaments, bows and candy canes into a room with a brightly lit tree, a greenery-draped mantel and rainbow ceiling streamers, captioned "It's tiiiiime!" A 35K-like reel documents a 14-hour vintage tree build with about 1,000 ornaments, 95% thrifted, adding colorful C9 lights by hand and a Christopher Radko Disney nutcracker ornament. A 25K-like reel presents a "Creative Holiday Edit" tree in checkered pajamas — red baubles, black-and-white checkered ornaments, a yellow traffic light, a red stop sign, a Woody doll and a plush Mickey, topped with a sign reading "THE CREATIVE." A 24K-like reel centers on a tree with red bows and white-and-gold ornaments above an illuminated miniature Christmas village on a snowy mat, a train circling past tiny lit houses, a windmill and figurines, while two cats wander through the scene.

### 💄 Beauty — Hooded-eye holiday glam and Christmas makeup hacks

An 80K-like tutorial builds holiday eye makeup for hooded eyes — a folded cotton round as a shield while dark purple shadow from a Morphe palette defines the crease, then a shimmery pink shade on the lid, finished with mascara for a soft smoky purple eye with winged liner, glossy nude lips and gold hoops. A 41K-like "GRWM FOR DIWALI" tries Indian makeup for the first time — warm-toned eyeshadow, gel winged liner, shimmery highlighter on the lids and brown lip liner with gloss, paired with a sari sent by a friend. A 35K-like reel shares "2 Holiday Makeup Hacks for Hooded Eyes" — a cotton pad shield for a clean dark-purple edge, then tape at the outer corner to map the crease with reddish-brown shadow and a shimmery silver-green lid. A 30K-like reel demos "3 easy christmas makeup hacks" — a Santa hat stamped on the forehead with an eyelash curler dipped in red liquid lipstick, bauble dots on the cheek drawn with a green pen, and a snowflake etched into red blush with a toothpick dipped in micellar water. A 27K-like transformation tutorial walks through a soft-glam look — liquid foundation and concealer, pink blush, contour and eyeshadow from a multi-pan palette, winged liner, mascara, lip liner and gloss. An 18K-like clip applies a deep berry lipstick from a gold case with a red gem detail, captioned "deep berry lips for winter >>."

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

- [2026-11-14](data/2026-11-14.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-14.gif) · [Video](assets/2026-11-14.mp4)
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
