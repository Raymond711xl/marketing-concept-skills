# Evidence Pool Contract

This schema is the handoff bridge into `evidence-summary-analysis` first, then `insight-strategy`.

Normal downstream order:

```text
web-evidence-collector -> evidence-summary-analysis -> insight-strategy
```

Do not skip `evidence-summary-analysis` unless the user explicitly overrides the workflow.

## Required Core Fields

Keep these fields first in every item:

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

If `Raw quote` is unavailable, use `Observation` for visual, video, or event evidence. Do not fabricate quotes.

## Collector Extension Fields

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

## Confidence Rules

- High: L1-L2 source, clear date and URL, direct evidence, or repeated evidence across source types.
- Medium: credible source but partial context, or repeated evidence with limited source diversity.
- Low: thin evidence, platform access limits, unclear date, limited trace, or only one weak source.
- Speculative: useful lead but not confirmed; pass downstream only with caveat.

## Item Quality

Good evidence item:

- Traceable
- Dated or clearly marked as date unknown
- Focused on one fact/material/quote/observation
- Separated from inference
- Labeled with source level and confidence

Bad evidence item:

- No source trail
- Broad paragraph mixing several claims
- Full article copied into raw quote
- Brand claim treated as audience truth
- Search result treated as final fact
