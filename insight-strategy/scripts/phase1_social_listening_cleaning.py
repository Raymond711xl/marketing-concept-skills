#!/usr/bin/env python3
"""Convert raw social comments into a first-pass evidence pool Markdown file.

This is an optional adapter for Insight Strategy. It performs mechanical
preparation only: reading comments, deduping, token counting, simple emotion
scanning, and raw voice extraction.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


TEXT_COLUMNS = [
    "comment",
    "comments",
    "content",
    "text",
    "message",
    "review",
    "评论",
    "内容",
    "留言",
    "评价",
    "正文",
]

LIKE_COLUMNS = ["like", "likes", "upvotes", "赞", "点赞", "点赞数"]

DEFAULT_EMOTIONS = {
    "焦虑": ("anxiety", "identity", 3),
    "压力": ("pressure", "social_role", 3),
    "孤独": ("loneliness", "emotional_lack", 3),
    "安全感": ("security", "emotional_lack", 3),
    "自由": ("freedom", "lifestyle", 2),
    "松弛": ("relief", "lifestyle", 2),
    "被看见": ("recognition", "identity", 3),
}

DEFAULT_STOPWORDS = {
    "的",
    "了",
    "和",
    "是",
    "我",
    "也",
    "就",
    "都",
    "很",
    "在",
    "有",
    "不",
    "吗",
    "啊",
}


def read_rows(path: Path) -> list[dict[str, str]]:
    suffix = path.suffix.lower()
    if suffix in {".csv", ".tsv", ".txt"}:
        delimiter = "\t" if suffix == ".tsv" else ","
        if suffix == ".txt":
            sample = path.read_text(encoding="utf-8-sig", errors="ignore")[:2048]
            delimiter = "\t" if "\t" in sample else ","
        with path.open("r", encoding="utf-8-sig", errors="ignore", newline="") as f:
            return [dict(row) for row in csv.DictReader(f, delimiter=delimiter)]

    if suffix in {".xlsx", ".xls", ".xlsm"}:
        try:
            import openpyxl  # type: ignore
        except ImportError as exc:
            raise SystemExit("Excel support requires openpyxl in the runtime.") from exc
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        ws = wb.active
        rows = list(ws.iter_rows(values_only=True))
        if not rows:
            return []
        headers = [str(h or "").strip() for h in rows[0]]
        result = []
        for row in rows[1:]:
            result.append({headers[i]: "" if v is None else str(v) for i, v in enumerate(row)})
        return result

    raise SystemExit(f"Unsupported input file type: {suffix}")


def pick_column(headers: list[str], candidates: list[str]) -> str | None:
    lower_map = {h.lower(): h for h in headers}
    for candidate in candidates:
        if candidate.lower() in lower_map:
            return lower_map[candidate.lower()]
    for header in headers:
        if any(candidate.lower() in header.lower() for candidate in candidates):
            return header
    return None


def tokenize(text: str, stopwords: set[str]) -> list[str]:
    try:
        import jieba  # type: ignore

        words = [w.strip() for w in jieba.cut(text)]
    except ImportError:
        words = re.findall(r"[\u4e00-\u9fff]{2,}|[A-Za-z][A-Za-z0-9_-]+", text)
    return [w for w in words if len(w) >= 2 and w not in stopwords]


def to_int(value: str) -> int:
    try:
        return int(float(str(value).replace(",", "").strip()))
    except Exception:
        return 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    parser.add_argument("--source", default="unknown")
    parser.add_argument("--brand", default="unknown brand")
    parser.add_argument("--stopwords", default="")
    args = parser.parse_args()

    input_path = Path(args.input_file)
    rows = read_rows(input_path)
    if not rows:
        raise SystemExit("No rows found.")

    headers = list(rows[0].keys())
    text_col = pick_column(headers, TEXT_COLUMNS)
    like_col = pick_column(headers, LIKE_COLUMNS)
    if not text_col:
        raise SystemExit(f"No text column found. Headers: {headers}")

    stopwords = set(DEFAULT_STOPWORDS)
    stopwords.update(s.strip() for s in args.stopwords.split(",") if s.strip())

    seen: set[str] = set()
    comments: list[dict[str, object]] = []
    for index, row in enumerate(rows, start=1):
        text = str(row.get(text_col, "")).strip()
        if len(text) < 3 or text in seen:
            continue
        seen.add(text)
        comments.append(
            {
                "row": index,
                "text": text,
                "likes": to_int(str(row.get(like_col, "0"))) if like_col else 0,
            }
        )

    token_counts: Counter[str] = Counter()
    emotion_hits: dict[str, list[str]] = defaultdict(list)
    for item in comments:
        text = str(item["text"])
        token_counts.update(tokenize(text, stopwords))
        for term in DEFAULT_EMOTIONS:
            if term in text:
                emotion_hits[term].append(text)

    top_comments = sorted(comments, key=lambda x: int(x["likes"]), reverse=True)[:100]
    top_tokens = token_counts.most_common(25)

    out = []
    out.append(f"# {args.brand} Phase 1 Social Listening Initial Wash\n")
    out.append("## Dataset Overview\n")
    out.append(f"- Source: {args.source}")
    out.append(f"- Input file: {input_path.name}")
    out.append(f"- Raw rows: {len(rows)}")
    out.append(f"- Deduped usable comments: {len(comments)}")
    out.append(f"- Text column: {text_col}")
    out.append(f"- Like column: {like_col or 'not found'}\n")

    out.append("## Top Signal Words\n")
    for word, count in top_tokens:
        out.append(f"- {word}: {count}")
    out.append("")

    out.append("## Emotion And Tension Scan\n")
    for term, hits in emotion_hits.items():
        emotion, domain, weight = DEFAULT_EMOTIONS[term]
        out.append(f"- {term}: emotion={emotion}, domain={domain}, weight={weight}, hits={len(hits)}")
    if not emotion_hits:
        out.append("- No built-in emotion terms detected. Treat this as absence of script hits, not absence of emotion.")
    out.append("")

    out.append("## Raw Voice Excerpts\n")
    for item in top_comments[:30]:
        likes = int(item["likes"])
        row = int(item["row"])
        text = str(item["text"]).replace("\n", " ")
        out.append(f"- Row {row}, likes {likes}: > {text}")
    out.append("")

    out.append("## Evidence Pool Draft\n")
    for i, item in enumerate(top_comments[:20], start=1):
        text = str(item["text"]).replace("\n", " ")
        out.append(f"### Evidence {i}")
        out.append(f"- Source type: social")
        out.append(f"- Source name: {args.source}")
        out.append(f"- Date: unknown")
        out.append(f"- URL or citation: {input_path.name} row {item['row']}")
        out.append(f"- Raw quote: \"{text}\"")
        out.append(f"- Summary: To be interpreted in Level 1")
        out.append(f"- Topic tag: to-be-coded")
        out.append(f"- Audience: unknown")
        out.append(f"- Confidence: medium")
        out.append("")

    out.append("## Limitations\n")
    out.append("- This is mechanical preparation, not final insight.")
    out.append("- Emotion detection uses a small starter lexicon and must be checked against raw voice.")
    out.append("- Missing audience, platform, and date metadata should be filled before strategic decisions.")

    output_path = Path(args.output_file)
    output_path.write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    main()
