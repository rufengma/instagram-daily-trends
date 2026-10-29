# Instagram Daily Trend Mood

Every day, we analyze the emotions in Instagram's most popular trends and paint them as a painterly animation.

## Today's Animation · 2026-10-29

![Today's animation](assets/latest.gif)

> In the animation: wind moves her hair, waves roll, clouds drift slowly, lantern light flickers. The grain and brushstroke texture of the illustration is preserved all the way through — never smoothed out, never recolored. HD video version: [assets/latest.mp4](assets/latest.mp4). Still illustration: [assets/2026-10-29.png](assets/2026-10-29.png).

## Today's Dominant Emotion: Joy 🎉

On 2026-10-29, Instagram's trending topics were overall **joy**-led: mean joy score 0.52, and 28 of 45 trend posts (62%) had joy as their dominant emotion.

## Today's Emotion Distribution

| Emotion | Mean Score | Dominant Posts | Share |
| --- | --- | --- | --- |
| Joy | 0.5215 | 28 | 62.2% |
| Neutral | 0.2185 | 9 | 20.0% |
| Disgust | 0.1126 | 4 | 8.9% |
| Anger | 0.0728 | 3 | 6.7% |
| Fear | 0.0356 | 1 | 2.2% |
| Surprise | 0.0240 | 0 | 0% |
| Sadness | 0.0150 | 0 | 0% |

Valence rollup: positive 0.5215 (joy) / negative 0.2360 (anger + sadness + fear + disgust) / neutral 0.2425 (neutral + surprise; surprise has no fixed valence, counted as neutral).

## Today's Top Trends

| Trend | Posts |
| --- | --- |
| Karwa Chauth × Priyanka Chopra (Bollywood star celebrating Karwa Chauth, henna festivities) | 29 |
| Jennifer Lawrence × Call Her Daddy (podcast jokes, Hunger Games return, working after motherhood) | 16 |

Sample: 45 trend posts, from the 2026-10-27 to 2026-10-29 trend window.

## How It Works, Every Day

1. **Discover trends**: find the day's hot topics and posts through public Instagram trend discovery, ranked by engagement.
2. **Emotion analysis**: score every post with a 7-way emotion transformer model (`j-hartmann/emotion-english-distilroberta-base`) and aggregate into the day's emotion distribution.
3. **Illustration**: generate one painterly illustration for the day's dominant emotion and top trends (grain, loose brushstrokes, muted blue-green palette).
4. **Animation**: turn the illustration into a 10-second animation (wind, waves, clouds, light all moving) and embed it at the top of the README as an autoplaying GIF, with the HD video linked alongside.
5. **Archive**: the day's data is saved as `data/YYYY-MM-DD.json`; the illustration and animation as `assets/YYYY-MM-DD.png` / `.mp4` / `.gif`.

## Data Notes (Please Read First)

- **Data source**: public Instagram trend discovery. No Instagram account is connected. This project is not affiliated with Instagram / Meta.
- **What is analyzed**: model scores are based on post descriptions (search-result summaries), not full raw captions. The sample is recent posts under trending topics, not a platform-wide census — it reflects the mood of hot trends, not of all users.
- **Illustration and animation**: both AI-generated. The illustration style reference is a private image and is not included in this repo.
- **Emotions are model inferences**: scores are what the model infers from text, not self-reported feelings. Treat it as a trend sketch, not a precise poll.

## Repo Structure

```
instagram-daily-mood/
├── README.md                  # Today's animation + today's mood (updated daily)
├── assets/
│   ├── latest.gif             # Latest day's animation (autoplaying)
│   ├── latest.mp4             # Latest day's animation (HD video)
│   ├── YYYY-MM-DD.gif         # Each day's animation
│   ├── YYYY-MM-DD.mp4         # Each day's animation (HD video)
│   └── YYYY-MM-DD.png         # Each day's illustration
├── data/
│   ├── YYYY-MM-DD.json        # Each day's emotion distribution + per-post scores
│   └── raw/YYYY-MM-DD.json    # Each day's raw trend posts
└── scripts/
    ├── normalize.py           # Raw search results → data/raw
    ├── analyze.py             # Transformer emotion analysis → data
    ├── animate.py             # GIF utility (fallback; daily output is video → GIF)
    └── run_daily.py           # Daily analysis orchestration
```

## Archive

- [2026-10-29](data/2026-10-29.json) — Dominant emotion: Joy · Animation: [GIF](assets/2026-10-29.gif) · [Video](assets/2026-10-29.mp4)
