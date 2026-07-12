---
name: evidence-summary-analysis
description: Summarize, normalize, classify, and prepare an evidence pool produced by web-evidence-collector, messy notes, structured evidence pools, competitive research, visual research, social listening, campaign research, interviews, comments, reviews, screenshots, or user-provided materials. Use when sourced material needs evidence-pattern summaries, category summaries, frontstage content strips, Strategy Readiness Pack, cleaned Evidence Pool, or a compact handoff for downstream strategy. This skill consumes evidence; it does not perform open web research, create insight themes, infer human truths, make cultural judgments, or make strategy decisions.
---

# Evidence Summary Analysis

Use this skill to turn collected material into a clean, traceable summary layer.

Normal bundle flow:

```text
web-evidence-collector -> evidence-summary-analysis -> insight-strategy
```

When run by `concept-strategy-controller`, this skill is part of the default
Evidence Preparation stage. Do not ask the user to separately approve summary
unless the controller explicitly selected audit mode.

## Language And Field Rules

- Default to Chinese for working communication and user-facing output.
- Preserve source wording in its original language for `Raw quote`, slogans,
  titles, post text, and visible phrases.
- Keep Markdown handoff field labels in stable Title Case, such as `Evidence ID`,
  `Raw quote`, `Observation`, `Confidence`, and `Strategy Readiness Pack`.
- Do not switch between Title Case labels and snake_case labels inside Markdown
  output. If a machine export is requested, use the mapping in
  `references/01-evidence-pool-schema.md`.
- Preserve `Evidence ID` from input to cleaned output. If missing, assign a
  stable ID and mark that it was assigned during normalization.
- Preserve or add `Observation`, especially for visual, offline activation,
  landing page, packaging, video, and screenshot evidence.

## Boundary

Do:

- Normalize messy material into a cleaned Evidence Pool.
- Preserve source trails, `Evidence ID`, `Raw quote`, `Observation`, source
  labels, dates, URLs/citations, confidence, and limitations.
- Summarize evidence across visual, video, offline activation, marketing, PR,
  social, report, market, and competitor material.
- Extract evidence patterns: repeated material, source, channel, wording,
  visual, activation, PR-angle, or platform structures directly visible in the
  evidence.
- Produce frontstage content strips, evidence coverage, evidence gaps, category
  summaries, Strategy Readiness Pack, and compact downstream handoff.

Do not:

- Perform open web research or pretend fresh research was completed.
- Bypass login, paywalls, anti-bot controls, private groups, or platform
  restrictions.
- Copy full articles, full reports, full comment threads, or full social posts.
- Treat brand-owned claims as consumer truth.
- Create insight themes, human truths, motive inferences, cultural tensions,
  strategic recommendations, positioning, Idea Platform, brand strategy, Big
  Idea, or campaign strategy.

## Reference Map

Read these files as needed:

- `references/01-evidence-pool-schema.md` - required fields, naming convention,
  source levels, confidence, `Evidence ID`, `Observation`, and cleaned Evidence
  Pool contract.
- `references/02-category-and-volume-rules.md` - category extraction rules and
  light / standard / deep output volume.
- `references/03-output-templates.md` - coverage check, content strips,
  Strategy Readiness Pack, full handoff, quick output, and collector task
  template.
- `references/04-regression-samples.md` - regression examples for preserving
  `Evidence ID`, `Observation`, contradictory evidence, and brand hard-data
  leads.

## Input Adaptation

Accept:

- Collector output from `web-evidence-collector`
- Messy notes, links, pasted excerpts, screenshots, exported comments, interview
  notes, campaign notes, and social listening drafts
- Structured Evidence Pool or cleaned Evidence Pool
- User-provided files or citations with traceable source trails

If the input is structured, preserve the structure and normalize field names.
If the input is messy, convert it into Evidence Pool items before summarizing.

If fresh external evidence is missing, do not research from this skill. Output a
collector task using `references/03-output-templates.md`, including target,
missing categories, source priorities, and required fields.

## Workflow

### 1. Scope And Readiness

Identify:

- Target brand, campaign, event, product, industry, or competitor set
- Time range and geography/platform scope
- Requested categories and volume
- Downstream destination: user review, controller, `insight-strategy`, or audit
- Whether evidence is collector output, messy notes, or an existing Evidence Pool

If enough context is present, proceed. Ask only when missing scope blocks
normalization.

### 2. Normalize Evidence

Read `references/01-evidence-pool-schema.md`.

Normalize into cleaned Evidence Pool items. Keep required fields first and do
not drop collector fields. Required preservation:

- `Evidence ID`
- `Source type`
- `Source name`
- `Date`
- `URL or citation`
- `Raw quote`
- `Observation`
- `Summary`
- `Topic tag`
- `Audience`
- `Confidence`

Separate:

- `Fact`: what the source directly says
- `Observation`: what the material directly shows
- `Low-level source/material inference`: only direct material or source
  implication, not motive/culture/strategy
- `Unknown`: missing or unverified information

### 3. Audit Coverage

Check:

- Source diversity and source-level spread
- Date and URL/citation traceability
- Brand-owned vs third-party vs audience/source separation
- Visual, video, offline activation, marketing, PR, social, report, market, and
  competitor coverage
- Brand hard-data leads: brand philosophy, vision, slogan, chronology, founder
  statement, product proof, service proof, brand behavior, competitor
  distinction
- Contradictory evidence and missing categories
- Platform restrictions and user-needed materials

Continue with caveats if thin. Mark weak packages as exploratory.

### 4. Produce Frontstage Content Strips

Use compact strips for controller display:

- `来源覆盖内容条`
- `强证据模式内容条`
- `品牌硬信息内容条`
- `证据缺口内容条`
- `进入策略判断内容条`

Keep strips evidence-bound. Do not infer human truths or cultural tensions.

### 5. Category Summaries

Read `references/02-category-and-volume-rules.md`.

Summarize only requested categories, or all available categories when
unspecified. Use category fields for visual, video, offline activation,
marketing, PR, social, report, market, and competitor evidence.

If evidence is thinner than requested volume, output available items and mark
missing items as evidence gaps.

### 6. Evidence Pattern Inventory

Inventory observable patterns only:

- Repeated messages or phrases
- Explicit audience labels found in sources
- Common material formats
- Observable channel logic
- Visual or activation mechanisms
- PR angles and media/source spread
- Strong proof points and weak/unverified claims
- Contradictory evidence
- Source concentration and skew

Do not name insight themes, infer motives, produce human truths, make cultural
judgments, or recommend strategy.

### 7. Strategy Readiness Pack

Read `references/03-output-templates.md`.

Before handoff, create a Strategy Readiness Pack. Each candidate must include:

- Candidate text
- Status: `confirmed` / `reported` / `inferred` / `missing`
- Evidence ID
- Confidence
- Notes or user confirmation needed

Required rows:

- Brand truth candidate
- Proof edge
- Brand behavior
- Competitor distinction

This pack is not strategy. It is the hard-data bridge for `insight-strategy`.

### 8. Output Handoff

Use `references/03-output-templates.md`.

Default handoff order:

1. Frontstage content strips
2. Evidence coverage check
3. Category summaries
4. Evidence Pattern Inventory
5. Strategy Readiness Pack
6. Evidence gaps
7. Cleaned Evidence Pool

Quick output must still include a usable `Cleaned Evidence Pool` section. If the
pool is too long and the environment allows file output, provide a clear file
path or file-entry label and state that it contains `Evidence ID`, `Observation`,
traceability fields, and confidence.

## Quality Gates

- Every major summary traces back to `Evidence ID`, source name, or URL/citation.
- Collector core fields enter the cleaned Evidence Pool without loss.
- `Observation` exists for visual, activity, landing page, packaging, video, or
  screenshot evidence even when `Raw quote` is empty.
- Strategy Readiness Pack candidates all have status, Evidence ID, and
  Confidence, or are explicitly marked `missing`.
- Contradictory evidence is preserved, not smoothed away.
- Restricted social content uses short key phrases plus links, not full copied
  content.
- If fresh evidence is missing, output collector tasks rather than filling gaps
  with unsupported claims.
