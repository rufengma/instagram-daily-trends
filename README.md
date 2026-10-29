# Instagram 每日趋势情绪

每天分析 Instagram 最流行趋势里的情绪，用一段油画质感动画把它画出来。

## 今日动画 · 2026-10-29

<video src="assets/latest.mp4" poster="assets/2026-10-29.png" controls autoplay loop muted width="100%"></video>

> 动画里：风吹动头发、海浪起伏、云缓慢漂移、灯光微微闪烁；动画全程保留插画的颗粒与笔触质感，不磨平、不改色。打不开视频的话，[点这里直接打开](assets/latest.mp4)，静态插画在 [assets/2026-10-29.png](assets/2026-10-29.png)。

## 今日主导情绪：喜悦 🎉

2026-10-29，Instagram 热门趋势整体是**喜悦**主导：平均喜悦分数 0.52，45 条趋势帖子里有 28 条（62%）的主导情绪是喜悦。

## 今日情绪分布

| 情绪 | 平均分数 | 主导帖数 | 占比 |
| --- | --- | --- | --- |
| 喜悦 joy | 0.5215 | 28 | 62.2% |
| 平静 neutral | 0.2185 | 9 | 20.0% |
| 厌恶 disgust | 0.1126 | 4 | 8.9% |
| 愤怒 anger | 0.0728 | 3 | 6.7% |
| 恐惧 fear | 0.0356 | 1 | 2.2% |
| 惊讶 surprise | 0.0240 | 0 | 0% |
| 悲伤 sadness | 0.0150 | 0 | 0% |

效价归类：正向 0.5215（喜悦）/ 负向 0.2360（愤怒+悲伤+恐惧+厌恶）/ 中性 0.2425（平静+惊讶，惊讶效价不定，计入中性）。

## 今日热门趋势

| 趋势话题 | 帖数 |
| --- | --- |
| Karwa Chauth × Priyanka Chopra（宝莱坞明星过 Karwa Chauth、henna 庆祝） | 29 |
| Jennifer Lawrence × Call Her Daddy（播客玩笑、《饥饿游戏》回归、当妈后的工作方式） | 16 |

样本：45 条趋势帖子，取自 2026-10-27～10-29 的趋势周期。

## 每天怎么运作

1. **发现趋势**：通过公开 Instagram 趋势发现（按互动热度排序）找到当天热门话题下的帖子。
2. **情绪分析**：用 7 类情绪 transformer 模型（`j-hartmann/emotion-english-distilroberta-base`）给每条帖子打分，汇总成当日情绪分布。
3. **插画**：按当日主导情绪和热门趋势生成一张油画质感插画（颗粒、松散笔触、蓝绿色调）。
4. **动画**：把插画做成一段 10 秒动画（风、海浪、云、灯光都在动），嵌在 README 顶部。
5. **归档**：当日数据存为 `data/YYYY-MM-DD.json`，插画和动画存为 `assets/YYYY-MM-DD.png` / `.mp4`。

## 数据说明（请先读）

- **数据来源**：公开 Instagram 趋势发现，未连接任何 Instagram 账号；本项目与 Instagram / Meta 无关。
- **分析对象**：模型打分依据的是帖子内容描述（搜索结果摘要），不是原始 caption 全文；样本是趋势话题下的近期帖子，不是全站普查，结果反映的是热门趋势的情绪，不是全体用户的情绪。
- **插画与动画**：均为 AI 生成；插画风格参考图为私人图片，未收入本仓库。
- **情绪是模型推断**：分数是模型对文本的推断，不是用户自报的情绪，看看趋势就好，别当精确民调。

## 仓库结构

```
instagram-daily-mood/
├── README.md                  # 今日动画 + 今日情绪（每天更新）
├── assets/
│   ├── latest.mp4             # 最新一天的动画
│   ├── YYYY-MM-DD.mp4         # 每天的动画
│   └── YYYY-MM-DD.png         # 每天的插画原图
├── data/
│   ├── YYYY-MM-DD.json        # 每天的情绪分布 + 逐条帖子打分
│   └── raw/YYYY-MM-DD.json    # 每天的原始趋势帖子
└── scripts/
    ├── normalize.py           # 原始搜索结果 → data/raw
    ├── analyze.py             # transformer 情绪分析 → data
    ├── animate.py             # GIF 工具（备用；日常输出以视频为主）
    └── run_daily.py           # 每日分析编排
```

## 往期归档

- [2026-10-29](data/2026-10-29.json) — 主导情绪：喜悦 · 动画：[assets/2026-10-29.mp4](assets/2026-10-29.mp4)
