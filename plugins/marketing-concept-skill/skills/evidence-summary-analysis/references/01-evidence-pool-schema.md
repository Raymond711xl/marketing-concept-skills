# Evidence Pool Schema

Use this contract for both input normalization and cleaned output. The goal is
lossless preparation, not strategy interpretation.

## Field Naming Convention

Markdown output must use stable Title Case labels. Do not mix Title Case and
snake_case in the same handoff.

If a machine export is requested, use this mapping:

| Markdown label | Machine key |
| --- | --- |
| Evidence ID | evidence_id |
| Source type | source_type |
| Source name | source_name |
| Date | date |
| URL or citation | url_or_citation |
| Raw quote | raw_quote |
| Observation | observation |
| Summary | summary |
| Topic tag | topic_tag |
| Audience | audience |
| Confidence | confidence |
| Category | category |
| Source level | source_level |
| Publisher / platform | publisher_platform |
| Author / account | author_account |
| Access date | access_date |
| Brand / event | brand_event |
| Campaign / message | campaign_message |
| Channel | channel |
| Material type | material_type |
| Visual material | visual_material |
| Screenshot status | screenshot_status |
| Key fact | key_fact |
| Evidence value | evidence_value |
| Brand hard data type | brand_hard_data_type |
| Needs user confirmation | needs_user_confirmation |
| Related evidence | related_evidence |
| Linkage status | linkage_status |
| Metric / count | metric_count |
| Limitation / restriction | limitation_restriction |

## Required Core Fields

Keep these fields first in every cleaned evidence item:

```markdown
### Evidence 1
- Evidence ID:
- Source type:
- Source name:
- Date:
- URL or citation:
- Raw quote:
- Observation:
- Summary:
- Topic tag:
- Audience:
- Confidence:
```

Rules:

- Preserve `Evidence ID` from collector input. If missing, assign a stable ID
  such as `E-001` and note the assignment in `Limitation / restriction`.
- Preserve `Observation` when supplied. If missing and the evidence is visual,
  event, page, packaging, video, screenshot, or activity material, add a concise
  observation based only on the visible/source-provided material.
- If `Raw quote` is unavailable, leave it empty or mark `not available`; do not
  fabricate quotes. Use `Observation` for non-text evidence.
- Keep source trails even when evidence is weak.

## Extension Fields

Add these when available:

```markdown
- Source level:
- Category:
- Publisher / platform:
- Author / account:
- Access date:
- Brand / event:
- Campaign / message:
- Channel:
- Material type:
- Visual material:
- Screenshot status:
- Key fact:
- Evidence value:
- Brand hard data type:
- Needs user confirmation:
- Related evidence:
- Linkage status:
- Metric / count:
- Limitation / restriction:
```

## Allowed Values

Source type:

```text
brand-owned / official / news / report / competitor / social / review / forum / video platform / ecommerce / app store / event feedback / survey / interview / search result / user provided / other
```

Category:

```text
visual / video / offline activation / marketing / PR / social / report / market / competitor / other
```

Confidence:

```text
high / medium / low / speculative
```

Screenshot status:

```text
captured / public image linked / not accessible / user needed / not applicable
```

Linkage status:

```text
confirmed / likely / tentative / standalone / unknown
```

Brand hard data type:

```text
brand philosophy / vision / slogan / brand claim / chronology / founder statement / leadership statement / product proof / service proof / brand behavior / competitor distinction / other
```

Needs user confirmation:

```text
yes / no / unknown
```

## Source Levels

| Level | Source | Handling |
| --- | --- | --- |
| L1 | Official sites, government pages, filings, brand press releases | Summarize directly, keep links, use short quotes only. |
| L2 | News articles, public reports, industry media | Extract facts, viewpoints, dates, and publication context. |
| L3 | Public PDFs, white papers, report excerpts | Summarize key numbers and cite page/file when available. |
| L4 | Search snippets, aggregators, news indexes | Treat as leads; do not treat as final facts unless traced. |
| L5 | Ecommerce reviews, App Store reviews, public forums | Use small representative quotes; avoid bulk copying. |
| L6 | Xiaohongshu, Weibo, Douyin, Zhihu, Bilibili, TikTok, Instagram, dynamic/login-prone platforms | Use public pages only; otherwise keep a short phrase, link, and restriction note. |
| L7 | Paywalled reports, member-only pages, private communities, logged-in content | Analyze only user-authorized screenshots, excerpts, or exports. |
| L8 | Explicitly blocked, technically restricted, or prohibited content | Do not collect; keep metadata and reason if useful. |

## Confidence Rules

- High: L1-L2 source, clear date and URL, direct evidence, or repeated evidence
  across source types.
- Medium: credible source but partial context, or repeated evidence with limited
  source diversity.
- Low: thin evidence, platform access limits, unclear date, limited trace, or
  one weak source.
- Speculative: useful lead but unconfirmed; pass downstream only with caveat.

## Cleaned Evidence Pool Template

```markdown
## Cleaned Evidence Pool

### Evidence 1
- Evidence ID:
- Source type:
- Source name:
- Date:
- URL or citation:
- Raw quote:
- Observation:
- Summary:
- Topic tag:
- Audience:
- Confidence:
- Source level:
- Category:
- Publisher / platform:
- Author / account:
- Access date:
- Brand / event:
- Campaign / message:
- Channel:
- Material type:
- Visual material:
- Screenshot status:
- Key fact:
- Evidence value:
- Brand hard data type:
- Needs user confirmation:
- Related evidence:
- Linkage status:
- Metric / count:
- Limitation / restriction:
```
