# Instagram Daily Trends

Every day, we find what's trending on Instagram in fashion, home decor, and beauty — and paint it as a painterly animation.

## Today's Animation · 2026-11-17

![Today's animation](assets/latest.gif)

> In the animation: her long wavy hair sways softly, the fireplace flames flicker, the Christmas tree lights twinkle, snow falls slowly outside the windows, and the glitter on the vanity lipsticks sparkles. The grain and brushstroke texture of the illustration is preserved all the way through — never smoothed out, never recolored. HD video version: [assets/latest.mp4](assets/latest.mp4). Still illustration: [assets/2026-11-17.png](assets/2026-11-17.png).

## Today's Trends

### 👗 Fashion — Haul season peaks — H&M red bows, Zara sequins, and cozy loungewear

A 59K-like carousel posted today presents a Guess accessories editorial — an all-white tailored suit with a brown leather hobo bag and a two-tone wristwatch, then a black lace maxi dress with sheer leg panels layered under a leopard-print faux-fur coat with a matching mini bag. A 30K-like reel models an H&M party haul — a bright red one-shoulder mini dress with a large bow, a black off-the-shoulder mini, a red high-neck mini with black knee-high boots, a floor-length gold sequin slip dress, a long dark purple satin gown, and a white turtleneck with a brown sequin pencil skirt. A 24K-like Zara try-on haul runs six looks — an oversized grey knit sweater tucked into a silver sequin midi skirt, a white satin wrap blazer mini-dress, a burgundy tweed cropped cardigan with feathered cuffs, a black sequined camisole with a choker tie, a black long-sleeve mini dress with an asymmetrical drape, and a black-and-white plaid cropped jacket with a faux-fur collar. A 25K-like Snidel Home lookbook leans cozy — loungewear and pajamas with teddy bear graphics, a giant red velvet bow over white pajamas, red heart-print pajamas with fairy lights, and a navy sweater with earmuffs. A 14K-like get-ready reel builds a full glam look around a floor-length champagne sequined halter gown — clear heels, dangling crystal earrings, red lipstick, a small silver sequined clutch, and a long white faux-fur coat. A 10K-like reel builds five party outfits around one burgundy lace strapless bustier top — dark purple wide-leg trousers, a black blazer, a black satin asymmetrical midi skirt, black sequin mini shorts, and white wide-leg trousers.

### 🛋️ Home Decor — Deck every room, not just the tree — castle Christmas, ribbon weaving, and plaid kitchens

A 26K-like vlog decorates for Christmas "besides the tree" — ceramic gingerbread houses and a large Santa statue, a fresh wreath and an "OH WHAT FUN" banner, mantel garland with dried orange slices, monogrammed gingham stockings, garland draped across the kitchen cabinets, and a gingerbread village display on the counter. A 26K-like tour shows Highclere Castle at Christmas — a gravel drive lined with potted evergreen trees, a candlelit dining room with a lit tree, a staircase dressed with illuminated garlands and bows, and drawing rooms filled with elaborately decorated trees. A 20K-like reel posted today decorates a tree in red — warm white fairy lights, white snowflake ornaments, crystal bead garlands, and a large white satin bow topper, with a nutcracker and reindeer figurine on the media console. A 12K-like reel reveals "the cutest tree you ever will see" — a flocked tree with plush ornaments (a smiling cloud, a "Milk For Santa" bottle, a gingerbread man), red glass baubles, pinecones and warm white lights, sitting in a white wicker basket. A 10K-like reel decorates a bright kitchen — a red plaid vinyl cover on the fridge, Santa, tree and cardinal ceramic plates on a green wall, greenery garlands with fairy lights and dried orange slices above the sink, and big red ribbons on the cabinet doors so they look like wrapped gifts. A 9K-like tutorial teaches ribbon weaving — a wide metallic gold sheer ribbon looped in a zig-zag into the branches every few inches, with the reassurance that imperfections will not show once the tree is finished.

### 💄 Beauty — Glitter lips win Christmas — before-and-after glam, hooded-eye holidays, and MAC Fizzy Feels

A 62K-like before-and-after reel goes from a messy bun and satin robe to long styled hair, full makeup with blush and lipstick, and a red top. A 50K-like reveal starts in minimal makeup and a pink robe, then lands on heavy eye makeup, blush and shiny glitter lipstick, captioned "GLITTER LIPSTCK IS THE BEST FOR XMAS MAKEUP :)!". An 18K-like tutorial posted today demos "holiday makeup for hooded eyes" — red-pink shadow blended above the crease with a cotton pad as a shield for a lifted winged effect, a shimmery pink lid, and mascara. A 13K-like clip presents Thanksgiving dinner glam — short curly platinum-blonde hair, sharp dark brows, pink-purple eyeshadow, heavy contour and highlight, and glossy lips with a black turtleneck. An 11K-like "sexy winter wonderland" tutorial skips bronzer for a cool-tone contour, layers baby-pink cream blush under a muted pink powder blush, and finishes with a nude lip and a white faux-fur coat. A 7.2K-like review tries MAC's holiday "Fizzy Feels" lipsticks — "Fizzy Bubbles", a light pink glitter, and "Crystal Caviar", a darker brownish-purple glitter — silky with no gritty feel, swatched and worn with matching lip liners.

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

- [2026-11-17](data/2026-11-17.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-17.gif) · [Video](assets/2026-11-17.mp4)
- [2026-11-16](data/2026-11-16.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-16.gif) · [Video](assets/2026-11-16.mp4)
- [2026-11-15](data/2026-11-15.json) — Fashion / Home Decor / Beauty · Animation: [GIF](assets/2026-11-15.gif) · [Video](assets/2026-11-15.mp4)
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
