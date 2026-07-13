# Optional Raw Evidence Preparation

Use this only when the user provides raw comments, reviews, open-ended survey
answers, event feedback, support logs, or a rough monitoring export that needs
conversion into an evidence pool. Skip this step when the user already provides
a structured evidence pool.

## Supported Data

The optional adapter is designed for:

- CSV (`.csv`), TSV (`.tsv`), and TXT (`.txt`) with Python's standard library;
  no third-party dependency is required. TXT may be a delimited table or one
  comment per non-empty line.
- Excel `.xlsx` and `.xlsm` only when the optional `openpyxl` package is
  installed.
- Legacy binary `.xls` is not supported by `openpyxl`. Convert it to `.xlsx`,
  `.csv`, or `.tsv` first.

The data should contain at least one text column. Common text-column aliases:
`comment`, `comments`, `content`, `text`, `message`, `review`, `评论`, `内容`,
`留言`, `评价`, `正文`.

Optional fields:

- Like/upvote count
- Source/platform
- Date
- User/audience segment

## Purpose

This step is mechanical preparation, not strategy. It should produce:

- High-frequency words and repeated signals
- Language markers related to need, pressure, desire, or tension
- Representative raw voices
- Deduplicated quote bank
- A first-pass evidence pool

The adapter loads the bundled, self-authored stopwords, emotion taxonomy,
motive taxonomy, synonym map, tension domains, platform slang, and coding tags
from `assets/lexicons/`. These matches are reading aids only.

Do not treat the output as the final insight. It is the material for Level 1.

## Command

Resolve the command from the directory containing this Skill's `SKILL.md`.
Do not assume the caller is in the plugin root:

```bash
python3 <insight-strategy-skill-dir>/scripts/prepare_raw_evidence.py \
  input.csv output.md --source "小红书" --source-type social --brand "品牌名" \
  --stopwords "额外停用词1,额外停用词2"
```

The script locates bundled lexicons relative to its own file, so it can be
invoked from any working directory. Relative input and output paths remain
relative to the caller's current directory.

Optional dependencies:

- `jieba`: used for richer Chinese tokenization when available. With the
  default `--tokenizer auto`, absence falls back to a standard-library phrase
  scanner. Use `--tokenizer jieba` to require it or `--tokenizer stdlib` for a
  deterministic no-dependency run.
- `openpyxl`: required only for `.xlsx` and `.xlsm`. If absent, the script exits
  with a conversion/install instruction; CSV, TSV, and TXT remain available.

## Output

The output Markdown should include:

1. Dataset overview
2. Top signal words
3. Bundled lexicon load summary
4. Emotion, motive, synonym, tension-domain, and platform-slang scans
5. Raw voice excerpts with `RAW-###` Evidence IDs
6. Evidence Pool v1 draft with all 11 core fields in canonical order
7. Known limitations

After this file is produced, enter `03-level1-fact-layer.md`.
