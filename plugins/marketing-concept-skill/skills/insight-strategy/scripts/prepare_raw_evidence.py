#!/usr/bin/env python3
"""Convert raw text rows into an evidence-pool draft.

The adapter performs mechanical preparation only. It loads the license-clean
lexicons bundled with this Skill, preserves raw voice, and never promotes word
frequency or lexicon hits into insight.
"""

from __future__ import annotations

import argparse
import csv
import io
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Callable


SKILL_DIR = Path(__file__).resolve().parents[1]
LEXICON_DIR = SKILL_DIR / "assets" / "lexicons"

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

SOURCE_TYPES = (
    "social",
    "review",
    "ecommerce",
    "forum",
    "event feedback",
    "survey",
    "interview",
    "user provided",
    "other",
)


def read_dict_rows(path: Path, delimiter: str) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", errors="ignore", newline="") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        if not reader.fieldnames:
            return []
        return [
            {str(key or "").strip(): str(value or "") for key, value in row.items()}
            for row in reader
        ]


def read_txt_rows(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig", errors="ignore")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return []

    for delimiter in ("\t", ","):
        if delimiter not in lines[0]:
            continue
        reader = csv.DictReader(io.StringIO(text), delimiter=delimiter)
        rows = [
            {str(key or "").strip(): str(value or "") for key, value in row.items()}
            for row in reader
        ]
        headers = list(rows[0].keys()) if rows else list(reader.fieldnames or [])
        if pick_column(headers, TEXT_COLUMNS):
            return rows

    return [{"text": line} for line in lines]


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"Input file not found: {path}")

    suffix = path.suffix.lower()
    if suffix == ".csv":
        return read_dict_rows(path, ",")
    if suffix == ".tsv":
        return read_dict_rows(path, "\t")
    if suffix == ".txt":
        return read_txt_rows(path)

    if suffix == ".xls":
        raise SystemExit(
            "Legacy .xls files are not supported by openpyxl. Convert the file "
            "to .xlsx, .csv, or .tsv before running this adapter."
        )

    if suffix in {".xlsx", ".xlsm"}:
        try:
            import openpyxl  # type: ignore
        except ImportError as exc:
            raise SystemExit(
                "Reading .xlsx/.xlsm requires the optional dependency openpyxl. "
                "Install openpyxl or export the file as CSV/TSV."
            ) from exc
        workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
        sheet = workbook.active
        values = list(sheet.iter_rows(values_only=True))
        if not values:
            return []
        headers = [str(value or "").strip() for value in values[0]]
        return [
            {
                headers[index]: "" if value is None else str(value)
                for index, value in enumerate(row)
                if index < len(headers) and headers[index]
            }
            for row in values[1:]
        ]

    raise SystemExit(
        f"Unsupported input file type: {suffix or '[no extension]'}. "
        "Use CSV, TSV, TXT, XLSX, or XLSM."
    )


def pick_column(headers: list[str], candidates: list[str]) -> str | None:
    lower_map = {header.lower(): header for header in headers}
    for candidate in candidates:
        if candidate.lower() in lower_map:
            return lower_map[candidate.lower()]
    for header in headers:
        if any(candidate.lower() in header.lower() for candidate in candidates):
            return header
    return None


def load_csv_asset(filename: str) -> list[dict[str, str]]:
    path = LEXICON_DIR / filename
    if not path.exists():
        raise SystemExit(f"Bundled lexicon asset missing: {path}")
    return read_dict_rows(path, ",")


def load_lexicons() -> dict[str, object]:
    stopword_path = LEXICON_DIR / "zh-stopwords.txt"
    if not stopword_path.exists():
        raise SystemExit(f"Bundled lexicon asset missing: {stopword_path}")
    stopwords = {
        line.strip()
        for line in stopword_path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }
    synonym_rows = load_csv_asset("synonym-map.csv")
    return {
        "stopwords": stopwords,
        "emotion": load_csv_asset("emotion-taxonomy.csv"),
        "motive": load_csv_asset("motive-taxonomy.csv"),
        "synonyms": synonym_rows,
        "synonym_map": {
            row["variant"].strip(): row["canonical_term"].strip()
            for row in synonym_rows
            if row.get("variant") and row.get("canonical_term")
        },
        "domains": {
            row["domain"].strip(): row["description"].strip()
            for row in load_csv_asset("tension-domains.csv")
            if row.get("domain")
        },
        "slang": load_csv_asset("platform-slang.csv"),
        "topic_tags": load_csv_asset("topic-tag-taxonomy.csv"),
    }


def select_segmenter(mode: str) -> tuple[Callable[[str], list[str]] | None, str]:
    if mode == "stdlib":
        return None, "stdlib fallback"
    try:
        import jieba  # type: ignore
    except ImportError as exc:
        if mode == "jieba":
            raise SystemExit(
                "--tokenizer jieba requires the optional dependency jieba. "
                "Use --tokenizer auto or --tokenizer stdlib instead."
            ) from exc
        return None, "stdlib fallback (jieba not installed)"
    return lambda text: [word.strip() for word in jieba.cut(text)], "jieba"


def contains_term(text: str, term: str) -> bool:
    return term.casefold() in text.casefold()


def tokenize(
    text: str,
    stopwords: set[str],
    known_terms: set[str],
    synonym_map: dict[str, str],
    segmenter: Callable[[str], list[str]] | None,
) -> list[str]:
    if segmenter is not None:
        words = segmenter(text)
    else:
        words = []
        for term in sorted(known_terms, key=len, reverse=True):
            words.extend([term] * text.casefold().count(term.casefold()))
        words.extend(re.findall(r"[A-Za-z][A-Za-z0-9_-]+", text))
        for chunk in re.findall(r"[\u4e00-\u9fff]{2,8}", text):
            if not any(contains_term(chunk, term) for term in known_terms):
                words.append(chunk)

    normalized = []
    for word in words:
        clean = word.strip()
        if len(clean) < 2 or clean in stopwords:
            continue
        normalized.append(synonym_map.get(clean, clean))
    return normalized


def to_int(value: str) -> int:
    try:
        return int(float(str(value).replace(",", "").strip()))
    except (TypeError, ValueError):
        return 0


def scan_taxonomy(
    comments: list[dict[str, object]],
    rows: list[dict[str, str]],
    label_field: str,
) -> list[dict[str, object]]:
    results = []
    for row in rows:
        term = row.get("term", "").strip()
        if not term:
            continue
        ids = [str(item["id"]) for item in comments if contains_term(str(item["text"]), term)]
        if ids:
            results.append(
                {
                    "term": term,
                    "label": row.get(label_field, "").strip(),
                    "domain": row.get("tension_domain", "").strip(),
                    "weight": row.get("weight", "").strip(),
                    "ids": ids,
                }
            )
    return results


def append_marker_section(
    output: list[str],
    heading: str,
    markers: list[dict[str, object]],
    domains: dict[str, str],
) -> None:
    output.append(f"## {heading}\n")
    if not markers:
        output.append("- No bundled marker hits. This is not evidence that the emotion or motive is absent.")
        output.append("")
        return
    for marker in markers:
        domain = str(marker["domain"])
        description = domains.get(domain, "unmapped domain")
        ids = ", ".join(str(value) for value in marker["ids"])
        output.append(
            f"- {marker['term']}: label={marker['label']}; "
            f"domain={domain} ({description}); weight={marker['weight']}; "
            f"Evidence IDs={ids}"
        )
    output.append("")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Prepare raw comments as a traceable evidence-pool draft."
    )
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    parser.add_argument("--source", default="unknown")
    parser.add_argument(
        "--source-type",
        choices=SOURCE_TYPES,
        default="social",
        help="Evidence Pool v1 source type for the supplied rows",
    )
    parser.add_argument("--brand", default="unknown brand")
    parser.add_argument("--stopwords", default="")
    parser.add_argument(
        "--tokenizer",
        choices=("auto", "jieba", "stdlib"),
        default="auto",
        help="auto uses jieba when installed and otherwise a stdlib fallback",
    )
    args = parser.parse_args()

    input_path = Path(args.input_file).expanduser().resolve()
    output_path = Path(args.output_file).expanduser().resolve()
    rows = read_rows(input_path)
    if not rows:
        raise SystemExit("No rows found.")

    headers = list(rows[0].keys())
    text_col = pick_column(headers, TEXT_COLUMNS)
    like_col = pick_column(headers, LIKE_COLUMNS)
    if not text_col:
        raise SystemExit(f"No text column found. Headers: {headers}")

    lexicons = load_lexicons()
    stopwords = set(lexicons["stopwords"])
    stopwords.update(value.strip() for value in args.stopwords.split(",") if value.strip())
    synonym_map = dict(lexicons["synonym_map"])

    known_terms = {
        row.get("term", "").strip()
        for key in ("emotion", "motive", "slang")
        for row in lexicons[key]
        if row.get("term", "").strip()
    }
    known_terms.update(synonym_map)
    known_terms.update(synonym_map.values())

    segmenter, tokenizer_label = select_segmenter(args.tokenizer)

    seen: set[str] = set()
    comments: list[dict[str, object]] = []
    for row_number, row in enumerate(rows, start=1):
        text = str(row.get(text_col, "")).strip()
        if len(text) < 3 or text in seen:
            continue
        seen.add(text)
        comments.append(
            {
                "id": f"RAW-{len(comments) + 1:03d}",
                "row": row_number,
                "text": text,
                "likes": to_int(str(row.get(like_col, "0"))) if like_col else 0,
            }
        )

    if not comments:
        raise SystemExit("No usable text rows remained after cleaning and deduplication.")

    token_counts: Counter[str] = Counter()
    for item in comments:
        token_counts.update(
            tokenize(
                str(item["text"]),
                stopwords,
                known_terms,
                synonym_map,
                segmenter,
            )
        )

    emotion_hits = scan_taxonomy(comments, list(lexicons["emotion"]), "emotion")
    motive_hits = scan_taxonomy(comments, list(lexicons["motive"]), "motive")

    synonym_hits = []
    for row in list(lexicons["synonyms"]):
        variant = row.get("variant", "").strip()
        ids = [str(item["id"]) for item in comments if variant and contains_term(str(item["text"]), variant)]
        if ids:
            synonym_hits.append((variant, row.get("canonical_term", "").strip(), ids))

    slang_hits = []
    for row in list(lexicons["slang"]):
        term = row.get("term", "").strip()
        ids = [str(item["id"]) for item in comments if term and contains_term(str(item["text"]), term)]
        if ids:
            slang_hits.append((row, ids))

    domain_counts: Counter[str] = Counter()
    for marker in emotion_hits + motive_hits:
        domain_counts[str(marker["domain"])] += len(list(marker["ids"]))

    top_comments = sorted(comments, key=lambda item: int(item["likes"]), reverse=True)[:100]
    top_tokens = token_counts.most_common(25)
    domains = dict(lexicons["domains"])

    output: list[str] = []
    output.append(f"# {args.brand} Raw Evidence Preparation Report\n")
    output.append("## Dataset Overview\n")
    output.append(f"- Source: {args.source}")
    output.append(f"- Input file: {input_path.name}")
    output.append(f"- Raw rows: {len(rows)}")
    output.append(f"- Deduped usable comments: {len(comments)}")
    output.append(f"- Text column: {text_col}")
    output.append(f"- Like column: {like_col or 'not found'}")
    output.append(f"- Tokenizer: {tokenizer_label}\n")

    output.append("## Bundled Lexicon Use\n")
    output.append(f"- Stopwords loaded: {len(stopwords)}")
    output.append(f"- Emotion markers loaded: {len(list(lexicons['emotion']))}")
    output.append(f"- Motive markers loaded: {len(list(lexicons['motive']))}")
    output.append(f"- Synonym mappings loaded: {len(synonym_map)}")
    output.append(f"- Tension domains loaded: {len(domains)}")
    output.append(f"- Platform slang entries loaded: {len(list(lexicons['slang']))}")
    output.append(f"- Topic coding entries loaded: {len(list(lexicons['topic_tags']))}")
    output.append("- Lexicon policy: bundled, self-authored starter assets only\n")

    output.append("## Top Signal Words\n")
    output.append("- Note: frequency is a navigation signal, not an insight or representative market truth.")
    for word, count in top_tokens:
        output.append(f"- {word}: {count}")
    if not top_tokens:
        output.append("- No usable tokens found.")
    output.append("")

    append_marker_section(output, "Emotion Marker Scan", emotion_hits, domains)
    append_marker_section(output, "Motive Marker Scan", motive_hits, domains)

    output.append("## Synonym Normalization Signals\n")
    if synonym_hits:
        for variant, canonical, ids in synonym_hits:
            output.append(f"- {variant} -> {canonical}; Evidence IDs={', '.join(ids)}")
    else:
        output.append("- No bundled synonym variants detected.")
    output.append("")

    output.append("## Tension Domain Marker Summary\n")
    if domain_counts:
        for domain, count in domain_counts.most_common():
            output.append(f"- {domain} ({domains.get(domain, 'unmapped domain')}): {count} marker hits")
    else:
        output.append("- No domain marker hits.")
    output.append("")

    output.append("## Platform Slang Scan\n")
    if slang_hits:
        for row, ids in slang_hits:
            output.append(
                f"- {row.get('term')}: platform={row.get('platform')}; "
                f"normalize_to={row.get('normalize_to')}; "
                f"meaning={row.get('observed_meaning')}; Evidence IDs={', '.join(ids)}"
            )
    else:
        output.append("- No bundled platform-slang entries detected.")
    output.append("")

    output.append("## Coding Reference\n")
    grouped_tags: dict[str, list[str]] = defaultdict(list)
    for row in list(lexicons["topic_tags"]):
        grouped_tags[row.get("tag_type", "untyped")].append(row.get("tag", ""))
    for tag_type, tags in grouped_tags.items():
        output.append(f"- {tag_type}: {', '.join(tag for tag in tags if tag)}")
    output.append("- These are allowed first-pass labels; assign them only after reading each quote.\n")

    output.append("## Raw Voice Excerpts\n")
    for item in top_comments[:30]:
        text = str(item["text"]).replace("\n", " ")
        output.append(
            f"- {item['id']}, source row {item['row']}, likes {item['likes']}: > {text}"
        )
    output.append("")

    output.append("## Evidence Pool Draft\n")
    for item in top_comments[:20]:
        text = str(item["text"]).replace("\n", " ")
        output.append(f"### Evidence {item['id']}")
        output.append(f"- Evidence ID: {item['id']}")
        output.append(f"- Source type: {args.source_type}")
        output.append(f"- Source name: {args.source}")
        output.append("- Date: date unknown")
        output.append(f"- URL or citation: {input_path.name} row {item['row']}")
        output.append(f"- Raw quote: \"{text}\"")
        output.append("- Observation: not applicable - text-only source")
        output.append("- Summary: To be interpreted in Level 1")
        output.append("- Topic tag: to-be-coded")
        output.append("- Audience: audience unknown")
        output.append("- Confidence: medium")
        output.append("")

    output.append("## Limitations\n")
    output.append("- This is mechanical preparation, not Level 1-4 insight or strategy.")
    output.append("- Lexicon hits flag where to read; they do not determine emotion, motive, or tension.")
    output.append("- The stdlib tokenizer is approximate; install optional jieba for richer Chinese segmentation.")
    output.append("- Missing audience, platform, and date metadata should be filled before strategic decisions.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(output), encoding="utf-8")


if __name__ == "__main__":
    main()
