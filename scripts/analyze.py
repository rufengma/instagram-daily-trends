"""Emotion analysis for instagram-daily-mood.

Reads data/raw/<date>.json (posts with a 'summary' text field) and writes
data/<date>.json with the emotion distribution.

Model (default): j-hartmann/emotion-english-distilroberta-base, a 7-way
emotion classifier (anger, disgust, fear, joy, neutral, sadness, surprise)
trained on English text. Inference is done directly with
AutoTokenizer + AutoModelForSequenceClassification (no pipeline API),
so it works across transformers versions.

Valence rollup (documented, fixed):
  positive = joy
  negative = anger + sadness + fear + disgust
  neutral  = neutral + surprise   (surprise is valence-ambiguous)

Usage:
  python analyze.py --date 2026-10-29 [--model <hf-id>] [--raw data/raw]
"""
import argparse
import json
from collections import Counter
from pathlib import Path

import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

EMOTIONS = ["anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"]
DEFAULT_MODEL = "j-hartmann/emotion-english-distilroberta-base"
MAX_CHARS = 1200  # keep well under the model's 512-token window


def classify(texts, model_id):
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForSequenceClassification.from_pretrained(model_id)
    model.eval()
    id2label = {int(k): v for k, v in model.config.id2label.items()}
    results = []
    with torch.no_grad():
        for text in texts:
            clipped = (text or "")[:MAX_CHARS]
            inputs = tokenizer(clipped, return_tensors="pt", truncation=True, max_length=512)
            logits = model(**inputs).logits
            probs = torch.softmax(logits, dim=-1)[0].tolist()
            scores = {id2label[i]: round(float(p), 4) for i, p in enumerate(probs)}
            dominant = max(scores, key=scores.get)
            results.append({"scores": scores, "dominant": dominant})
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--raw", default="data/raw")
    parser.add_argument("--out", default="data")
    args = parser.parse_args()

    raw_path = Path(args.raw) / f"{args.date}.json"
    posts = json.loads(raw_path.read_text(encoding="utf-8"))
    texts = [p.get("summary", "") for p in posts]
    results = classify(texts, args.model)

    for post, res in zip(posts, results):
        post["emotion_scores"] = res["scores"]
        post["dominant_emotion"] = res["dominant"]

    n = len(posts)
    mean_scores = {
        emo: round(sum(p["emotion_scores"][emo] for p in posts) / n, 4) for emo in EMOTIONS
    }
    dominant_counts = Counter(p["dominant_emotion"] for p in posts)
    distribution = {
        emo: {
            "mean_score": mean_scores[emo],
            "dominant_count": dominant_counts.get(emo, 0),
            "share": round(dominant_counts.get(emo, 0) / n, 4),
        }
        for emo in EMOTIONS
    }
    overall_dominant = max(mean_scores, key=mean_scores.get)
    rollup = {
        "positive": round(mean_scores["joy"], 4),
        "negative": round(
            mean_scores["anger"] + mean_scores["sadness"] + mean_scores["fear"] + mean_scores["disgust"], 4
        ),
        "neutral": round(mean_scores["neutral"] + mean_scores["surprise"], 4),
    }
    topic_counts = Counter(p.get("topic", "unknown") for p in posts)

    out = {
        "date": args.date,
        "model": args.model,
        "method": "transformer",
        "sample_size": n,
        "dominant_emotion": overall_dominant,
        "emotion_distribution": distribution,
        "valence_rollup": rollup,
        "topics": dict(topic_counts),
        "posts": posts,
    }
    out_path = Path(args.out) / f"{args.date}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"analyzed {n} posts -> {out_path}")
    print(f"dominant: {overall_dominant} (mean score {mean_scores[overall_dominant]})")
    print("mean scores:", mean_scores)
    print("topics:", dict(topic_counts))


if __name__ == "__main__":
    main()
