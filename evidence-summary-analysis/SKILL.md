---
name: evidence-summary-analysis
description: Summarize, normalize, classify, and prepare an evidence pool produced by research, competitive research, visual research, social listening, campaign research, interviews, comments, reviews, or user-provided materials. Use when the user needs sourced material organized into evidence patterns, category summaries, visual/material observations, campaign evidence summaries, evidence gaps, or a structured handoff for a downstream strategy or insight skill. This skill consumes evidence; it does not perform open web research, create insight themes, infer human truths, make cultural judgments, or make final brand strategy decisions.
---

# Evidence Summary Analysis

Use this skill to turn a collected evidence pool into a clear, traceable summary layer. The job is to organize sourced material, label evidence patterns, and make the handoff clean enough that a downstream strategy skill can work from it confidently.

This skill sits between research collection and strategy:

```text
web-evidence-collector -> evidence-summary-analysis -> insight-strategy
```

## Language And Market Defaults

- Default to Chinese for working communication and user-facing output.
- If the user writes in English, requests English deliverables, or specifies an overseas market, adapt the working language and summary style accordingly.
- For Chinese brands, Chinese categories, Chinese campaigns, or China-market strategy work, interpret evidence inside Chinese network, platform, media, and consumer-language context.
- Use overseas or English-language framing when the evidence package or controller task names overseas markets, international competitors, global platforms, English campaigns, or cross-border context.
- Keep shared evidence schema field names stable in English so downstream skills can consume the cleaned evidence pool.
- Preserve source wording in its original language, especially raw quotes, slogans, post titles, and short visible phrases. Add Chinese explanation when useful, but do not replace the original source trail.

## Boundary

Do:

- Normalize messy research notes into a usable evidence pool.
- Classify evidence by source type, category, material type, topic tag, audience label, confidence, and evidence value.
- Summarize evidence across video, offline activation, marketing, PR, and visual materials.
- Extract repeated evidence patterns, category contrasts, material patterns, source skews, and evidence gaps.
- Preserve source trails and short raw quotes.
- Produce a structured handoff for downstream strategy or insight work.

Do not:

- Perform open web research unless the user explicitly asks this skill to help with a light missing-evidence note. Ask for `web-evidence-collector` when fresh external research is needed.
- Bypass login, paywalls, anti-bot controls, private groups, or platform restrictions.
- Copy full articles, full reports, full comment threads, or full social posts.
- Treat brand-owned claims as consumer truth.
- Create insight themes, human truths, motive inferences, cultural tensions, strategic recommendations, positioning, Big Idea, brand strategy, or campaign strategy. Those belong to `insight-strategy` or later strategy/concept skills.

## Input Contract

Accept any of these inputs:

- Evidence pool from `web-evidence-collector`
- Competitive design or visual research output
- Brand campaign research notes
- Market or competitor research digest
- Social listening initial wash
- Interview notes, comments, reviews, survey open ends, event feedback, or user-provided screenshots

If the input is not already structured, normalize it into the evidence pool schema below before analysis.

## Evidence Pool Schema

Use the downstream-compatible core fields first. Add optional fields when available.

```markdown
## Evidence Pool

### Evidence 1
- Evidence ID:
- Source type: news / report / brand-owned / competitor / social / review / interview / event feedback / survey / forum / customer service / search result / user provided / other
- Source name:
- Date:
- URL or citation:
- Raw quote:
- Summary:
- Topic tag:
- Audience:
- Confidence: high / medium / low / speculative
- Category: video / offline activation / marketing / PR / visual / market / competitor / social / report / other
- Source level: L1 / L2 / L3 / L4 / L5 / L6 / L7 / L8
- Publisher / platform:
- Author / account:
- Access date:
- Brand / event:
- Campaign / message:
- Channel:
- Material type: video ad / TVC / short video / poster / KV / landing page / packaging / product page / event photo / social post / article / report / comment / review / other
- Visual material:
- Screenshot status: captured / public image linked / not accessible / user needed / not applicable
- Key fact:
- Evidence value:
- Limitation / restriction:
```

Required for downstream strategy:

- `source_type`
- `source_name`
- `date`
- `url_or_citation`
- `raw_quote`
- `summary`
- `topic_tag`
- `audience`
- `confidence`

If required fields are missing, preserve the item but mark the missing fields clearly.

## Source Level Handling

Use source levels to preserve collection constraints:

| Level | Source | Handling |
| --- | --- | --- |
| L1 | Official sites, government pages, public company filings, brand press releases | Summarize directly, keep links, use short quotes only. |
| L2 | News articles, public reports, industry media | Extract facts, viewpoints, dates, and publication context. |
| L3 | Public PDFs, white papers, report excerpts | Summarize key numbers and cite page/file when available. |
| L4 | Search snippets, aggregators, news indexes | Treat as leads; do not treat as final facts unless traced. |
| L5 | Ecommerce reviews, App Store reviews, public forums | Use small representative quotes; avoid bulk copying. |
| L6 | Xiaohongshu, Weibo, Douyin, Zhihu, Bilibili, TikTok, Instagram, and similar dynamic or login-prone platforms | Use public pages only. When access is limited, keep one short key phrase, a link, and a restriction note. |
| L7 | Paywalled reports, member-only pages, private communities, logged-in content | Do not auto-collect. Analyze only user-provided screenshots, excerpts, or authorized exports. |
| L8 | Explicitly blocked or prohibited content | Do not collect. Keep only link metadata or user-authorized material. |

## Volume Selection

When users request category summaries, allow them to choose category count and item volume.

Categories:

- Video
- Offline activation
- Marketing
- PR
- Visual materials

Default output volume:

| Category | Light | Standard default | Deep |
| --- | --- | --- | --- |
| Video | 1-2 items | 3 items | 6-10 items |
| Offline activation | 1-2 items | 3 items | 6-10 items |
| Marketing | 3 items | 5 items | 8-12 items |
| PR | 3 items | 5 items | 8-12 items |
| Visual materials | 3 items | 5 items | 8-12 items |

If the user does not specify volume, say:

```text
I will use the standard default: Video 3, Offline activation 3, Marketing 5, PR 5, Visual materials 5 where evidence exists. I will mark missing categories as evidence gaps.
```

If evidence is thinner than the requested volume, output what exists and list the missing evidence needed.

## Workflow

### 1. Clarify Scope

Identify:

- Target brand, campaign, event, product, industry, or competitor set
- Time range
- Geography or platform scope
- Requested categories
- Requested output volume
- Downstream use: internal briefing, creative reference, strategy input, pitch proposal, competitive audit, or evidence handoff

If enough context is already present, proceed without asking.

### 2. Normalize Evidence

Convert inputs into evidence items. Preserve raw wording where useful, but keep quotes short. Add source labels and confidence.

Separate:

- Fact: what the source directly says or shows
- Observation: what can be seen in the material
- Inference: only low-level source or material implications, not motive, human truth, cultural meaning, or strategic meaning
- Unknown: what is missing or unverified

### 3. Audit Evidence Coverage

Before summarizing, check:

- Are there enough items for the requested categories?
- Are sources diverse or dominated by one platform?
- Are brand-owned sources separated from third-party and consumer sources?
- Are dates and URLs traceable?
- Are visual or social materials accessible, restricted, or user-needed?
- Are any claims based only on search snippets or weak evidence?

Continue with caveats if the evidence is thin.

### 4. Category Summary

Summarize only categories requested by the user, or all available categories when unspecified.

#### Video

For video ads, TVCs, short videos, livestream clips, and campaign films, extract:

- Title or asset name
- Source and link
- Core message or slogan
- Script/narrative structure
- Main audience
- Visual style and craft cues
- Product role
- Platform/channel
- Evidence-supported performance indicators, if any
- Reusable pattern
- Evidence gap

#### Offline Activation

For pop-ups, exhibitions, retail events, stunts, roadshows, installations, campus activities, and community events, extract:

- Event mechanism
- Location and time
- Participation path
- Spatial/visual device
- Interactive mechanic
- Social sharing trigger
- Online amplification
- Audience role
- Reusable pattern
- Evidence gap

#### Marketing

For promotions, launches, collaborations, ecommerce moments, KOL/KOC, UGC, private traffic, membership, and platform mechanics, extract:

- Marketing mechanism
- Target audience
- Offer, hook, or participation incentive
- Channel mix
- Content format
- Conversion or engagement path
- Partner or creator role
- Reusable pattern
- Evidence gap

#### PR

For press releases, media coverage, public issues, awards, controversies, CEO statements, social debates, and reputation moments, extract:

- News angle
- Message frame
- Speaker or institution
- Media/source spread
- Public response indicators
- Risk or controversy
- Reputation effect
- Reusable pattern
- Evidence gap

#### Visual Materials

For posters, KVs, landing pages, packaging, product pages, social visuals, event visuals, and screenshots, extract:

- Material type
- Source and screenshot status
- Composition and hierarchy
- Color, typography, imagery, and brand asset usage
- Message and CTA
- Platform adaptation
- Visual consistency across touchpoints
- Reusable pattern
- Evidence gap

When social platforms cannot be fully accessed, include one short key phrase, the link, the platform, and a note such as:

```text
Full social content requires platform access; use the link for manual verification.
```

### 5. Evidence Pattern Inventory

After category summaries, synthesize:

- Repeated messages
- Explicit audience labels found in the evidence
- Common material formats
- Observable channel logic
- Strongest proof points
- Weak or unverified claims
- Contradictory evidence items
- Source concentration and skew
- Patterns worth handing to `insight-strategy`

Keep the inventory evidence-bound. Do not name insight themes, infer motives, produce human truths, make cultural judgments, or jump directly to strategy.

### 6. Output Handoff

End with a downstream handoff containing:

- Cleaned evidence pool
- Category summary tables
- Evidence pattern inventory
- Evidence gaps
- Confidence notes
- Strategy handoff notes clearly labeled as evidence-only, not insight

## Output Template

Use this structure unless the user asks for another format:

```markdown
# Evidence Summary Analysis: [Topic]

## 1. Scope

- Target:
- Time range:
- Geography/platform:
- Requested categories:
- Requested volume:
- Evidence count:
- Main source types:

## 2. Evidence Coverage Check

| Area | Status | Notes |
| --- | --- | --- |
| Source diversity | strong / medium / weak | |
| Date traceability | strong / medium / weak | |
| URL/citation traceability | strong / medium / weak | |
| Brand-owned vs third-party separation | clear / mixed / weak | |
| Social/platform restrictions | none / some / significant | |
| Visual evidence coverage | strong / medium / weak | |

## 3. Category Summaries

### Video

| Item | Source | Message | Audience | Pattern | Confidence |
| --- | --- | --- | --- | --- | --- |

### Offline Activation

| Item | Source | Mechanism | Audience | Pattern | Confidence |
| --- | --- | --- | --- | --- | --- |

### Marketing

| Item | Source | Mechanism | Channel | Pattern | Confidence |
| --- | --- | --- | --- | --- | --- |

### PR

| Item | Source | News angle | Response/risk | Pattern | Confidence |
| --- | --- | --- | --- | --- | --- |

### Visual Materials

| Item | Material type | Source | Visual observation | Screenshot status | Confidence |
| --- | --- | --- | --- | --- | --- |

## 4. Evidence Pattern Inventory

### Pattern 1: [Name]

- Evidence support:
- What the evidence shows:
- What remains uncertain:
- Confidence:

## 5. Evidence Gaps

| Gap | Why it matters | Suggested collector task |
| --- | --- | --- |

## 6. Downstream Strategy Handoff

### Strong evidence patterns

- 

### Weak evidence patterns / collection leads

- 

### Evidence-only handoff notes

- 

## 7. Cleaned Evidence Pool

### Evidence 1
- Source type:
- Source name:
- Date:
- URL or citation:
- Raw quote:
- Summary:
- Topic tag:
- Audience:
- Confidence:
- Category:
- Source level:
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
- Limitation / restriction:
```

## Quality Rules

- Keep every major summary traceable to evidence IDs, source names, or URLs.
- Do not fabricate quotes, links, dates, metrics, campaign names, or platform reactions.
- Do not turn a single vivid example into a broad market truth.
- Do not treat brand-owned messaging as audience belief.
- Preserve minority or contradictory evidence when it may matter.
- Mark uncertain items as low or speculative rather than smoothing them away.
- Do not explain why people feel something, what culture wants, or what the brand should choose; pass the evidence pattern to `insight-strategy`.
- Use short quotes only; summarize the rest.
- For restricted social content, provide links and short key phrases instead of copying full content.

## Handoff Discipline

For downstream strategy skills, output a clean evidence pool plus concise summary. Avoid burying the evidence under a long essay.

Preferred handoff order:

1. Evidence coverage check
2. Category summaries
3. Evidence pattern inventory
4. Evidence gaps
5. Cleaned evidence pool

If the user asks for a quick version, provide only:

- Top evidence patterns
- Category summary table
- Evidence gaps
- Cleaned evidence pool
