# Evidence Pool Contract

This schema is the handoff bridge into `evidence-summary-analysis` first, then `insight-strategy`.

Normal downstream order:

```text
web-evidence-collector -> evidence-summary-analysis -> insight-strategy
```

The collector always hands actual evidence to `evidence-summary-analysis`; any later routing decision belongs outside this skill.

Schema name: `Evidence Pool v1`

## Required Core Fields

Keep these fields first, in this exact spelling and order, in every actual evidence item:

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

Core-field rules:

- `Evidence ID` must be non-empty, unique within the dossier, and stable after assignment.
- Every core field must be present. Never leave a core field blank.
- Use explicit missing values: `not available`, `date unknown`, `audience unknown`, or `not applicable`.
- If `Raw quote` is unavailable, set it to `not available`. Do not fabricate a quote.
- `Observation` records what is directly visible or materially present. Visual, video, event, packaging, landing-page, and screenshot evidence must retain a concrete `Observation` even when no words are visible.
- For a text-only source with no relevant visual observation, use `Observation: not applicable - text-only source`.
- `Summary` is the collector's concise factual restatement. Keep it separate from both the source wording in `Raw quote` and the direct description in `Observation`.
- `URL or citation` must point to the source or provide a traceable file/page citation. If only a search-result lead is available, cite that lead and state the limitation.

## Stable Evidence IDs

Assign IDs once at capture time:

```text
WEB-001, WEB-002                    single-agent or sequential collection
OFF-001, NEW-001, VID-001           platform/source shards
SOC-XHS-001, SOC-WEIBO-001          split platform shards
```

- Never renumber IDs for presentation, de-duplication, shard merge, or downstream handoff.
- When de-duplicating, retain one canonical evidence item and its original ID.
- Preserve discarded duplicate IDs in `Merged from evidence IDs`.
- Do not reuse an ID for a different source or observation.
- When continuing an existing dossier, continue its existing ID sequence and prefixes instead of restarting at an ID already in use.

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
- Brand hard data status:
- Related evidence:
- Linkage status:
- Metric / count:
- Limitation / restriction:
- Shard ID:
- Shard source scope:
- Merged from evidence IDs:
```

When a collector extension field is present, preserve it through the handoff. Use `not applicable` where an extension is required by a category-specific template but does not apply.

## Lossless Handoff Rules

`evidence-summary-analysis` must not delete, rename, translate, merge, overwrite, or repurpose these core fields:

```text
Evidence ID
Source type
Source name
Date
URL or citation
Raw quote
Observation
Summary
Topic tag
Audience
Confidence
```

It must also preserve these traceability fields when present:

```text
Source level
Publisher / platform
Access date
Screenshot status
Brand hard data type
Needs user confirmation
Brand hard data status
Related evidence
Linkage status
Limitation / restriction
Shard ID
Shard source scope
Merged from evidence IDs
```

Downstream skills may append fields such as `Normalized summary`, `Pattern label`, or `Normalization note`. They must not replace collector values. If a correction is needed, retain the original value and add a correction note that cites the same `Evidence ID`.

Include this notice in the backend handoff:

```text
Handoff preservation: Evidence Pool v1. Preserve Evidence ID and all core field names and values. Keep Observation even when Raw quote is unavailable.
```

## Brand Hard Data Track Contract

Every actual candidate row must contain:

```markdown
| Hard data type | Candidate evidence | Source Evidence ID(s) | Source / URL | Candidate status | Confidence | Needs user confirmation |
| --- | --- | --- | --- | --- | --- | --- |
```

Use only evidence IDs that exist in the Evidence Pool. Do not create empty candidate rows merely to fill every hard-data type. Put absent types in `Gaps and Restrictions`.

Candidate status:

```text
user-provided official / public official candidate / independently corroborated / conflicting / incomplete
```

- Use `Needs user confirmation: yes` for public candidates not supplied or approved by the user.
- Use `Needs user confirmation: no` only when the user provided/confirmed the material or explicitly waived confirmation.
- Use `unknown` when confirmation status cannot be determined.
- Keep official brand self-description as a brand claim or candidate. Never relabel it as consumer belief, audience truth, human truth, or cultural truth.

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

Brand hard data status:

```text
user-provided official / public official candidate / independently corroborated / conflicting / incomplete / not applicable
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
- Blank or renumbered `Evidence ID`
- Visual evidence with an empty or missing `Observation`
- Simulated evidence created because live collection was unavailable
