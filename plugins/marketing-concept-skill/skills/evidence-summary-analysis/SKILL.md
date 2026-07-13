---
name: evidence-summary-analysis
description: Summarize, normalize, classify, and prepare an evidence pool produced by web-evidence-collector, messy notes, structured evidence pools, competitive research, visual research, social listening, campaign research, interviews, comments, reviews, screenshots, or user-provided materials. Use when the user asks for 证据摘要, 资料整理, 资料清洗, 调研资料归纳, 证据分类, 客户版研究报告, or when sourced material needs evidence-pattern summaries, category summaries, a selected Research Lens, frontstage content strips, a client-facing evidence report, Strategy Readiness Pack, cleaned Evidence Pool, or a compact handoff for downstream strategy. This skill consumes evidence; it does not perform open web research, create insight themes, infer human truths, make cultural judgments, or make strategy decisions.
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
- Organize the same evidence through a selected `Research Lens` without
  discarding unrelated items from the cleaned Evidence Pool.
- Produce frontstage content strips, evidence coverage, evidence gaps, category
  summaries, lens summaries, Strategy Readiness Pack, and compact downstream
  handoff.

Do not:

- Perform open web research or pretend fresh research was completed.
- Bypass login, paywalls, anti-bot controls, private groups, or platform
  restrictions.
- Copy full articles, full reports, full comment threads, or full social posts.
- Treat brand-owned claims as consumer truth.
- Present consumer evidence as a consumer insight, a single dated signal as a
  trend, or call a case successful without credible outcome evidence.
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
- `references/05-research-lens-and-delivery-modes.md` - canonical Research Lens
  values, Chinese request aliases, lens-specific modules, selection rules, and
  Delivery Mode contracts. Read whenever a lens or presentation mode must be
  selected, inferred, or rendered.

## Input Adaptation

Accept:

- Collector output from `web-evidence-collector`
- Messy notes, links, pasted excerpts, screenshots, exported comments, interview
  notes, campaign notes, and social listening drafts
- Structured Evidence Pool or cleaned Evidence Pool
- User-provided files or citations with traceable source trails
- A user or controller request naming one or more `Research Lens` values or a
  `Delivery Mode`

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
- `Primary Research Lens` and any `Supporting Research Lens`
- `Delivery Mode`
- Downstream destination: user review, controller, `insight-strategy`, or audit
- Whether evidence is collector output, messy notes, or an existing Evidence Pool

If enough context is present, proceed. Ask only when missing scope blocks
normalization.

Read `references/05-research-lens-and-delivery-modes.md` when the user names a
report direction, asks for a client-ready report, or leaves lens/mode selection
implicit. Keep material `Category` and `Research Lens` separate. Use one primary
lens by default; add supporting lenses only when requested or clearly necessary.

### 2. Normalize Evidence

Read `references/01-evidence-pool-schema.md`.

Normalize into cleaned Evidence Pool items. Keep required fields first and do
not drop collector fields. Preserve collector traceability extensions such as
`Brand hard data status`, `Shard ID`, `Shard source scope`, and
`Merged from evidence IDs` whenever present. Required core preservation:

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

These five strip names are a shared frontstage contract with
`concept-strategy-controller`; keep the names exactly stable. Keep strips
evidence-bound. Do not infer human truths or cultural tensions.

### 5. Category Summaries

Read `references/02-category-and-volume-rules.md`.

Summarize only requested categories, or all available categories when
unspecified. Use category fields for visual, video, offline activation,
marketing, PR, social, report, market, and competitor evidence.

If evidence is thinner than requested volume, output available items and mark
missing items as evidence gaps.

### 6. Research Lens Summary

Before the pattern inventory, produce a `Research Lens Summary` using
`references/05-research-lens-and-delivery-modes.md`. The lens changes grouping
and emphasis, not evidence status. Every lens finding must cite Evidence IDs,
Confidence, and contradictions or limitations.

For requests phrased as industry strategy, consumer insight, platform trend,
public sentiment, or successful case research, use the evidence-only adapters
in the reference. Do not supply the strategic, motivational, cultural, trend,
sentiment, or success claim unless the evidence contract permits it.

### 7. Evidence Pattern Inventory

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

### 8. Strategy Readiness Pack

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

### 9. Output Handoff

Use `references/03-output-templates.md`.

Default handoff order:

1. Scope, `Research Lens`, and `Delivery Mode`
2. Frontstage content strips
3. Evidence coverage check
4. Category summaries
5. Research Lens Summary
6. Evidence Pattern Inventory
7. Strategy Readiness Pack
8. Evidence gaps
9. Cleaned Evidence Pool

Apply the selected `Delivery Mode` from
`references/05-research-lens-and-delivery-modes.md`. Delivery Mode controls the
visible presentation, not evidence retention. Every mode must preserve a
complete cleaned pool in the output or provide its explicit file entry. Keep
the Strategy Readiness Pack available for downstream handoff even when a
client-facing body hides internal handoff terminology.

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
- Research Lens findings remain evidence-only and cite Evidence IDs and
  Confidence.
- Delivery Mode changes presentation only; it does not remove the cleaned
  Evidence Pool, source trail, caveats, or downstream handoff artifacts.
- Restricted social content uses short key phrases plus links, not full copied
  content.
- If fresh evidence is missing, output collector tasks rather than filling gaps
  with unsupported claims.
