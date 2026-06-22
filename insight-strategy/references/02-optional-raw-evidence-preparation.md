# Optional Raw Evidence Preparation

Use this only when the user provides raw comments, reviews, open-ended survey
answers, event feedback, support logs, or a rough monitoring export that needs
conversion into an evidence pool. Skip this step when the user already provides
a structured evidence pool.

## Supported Data

The optional adapter is designed for:

- Excel (`.xls`, `.xlsx`, `.xlsm`) when supported by local Python packages
- CSV (`.csv`)
- TSV (`.tsv`)
- TXT (`.txt`)

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

Do not treat the output as the final insight. It is the material for Level 1.

## Command

```bash
python scripts/prepare_raw_evidence.py input.csv output.md --source "小红书" --brand "品牌名" --stopwords "额外停用词1,额外停用词2"
```

## Output

The output Markdown should include:

1. Dataset overview
2. Top signal words
3. Need and tension marker scan
4. Raw voice excerpts
5. Evidence pool draft
6. Known limitations

After this file is produced, enter `03-level1-fact-layer.md`.
