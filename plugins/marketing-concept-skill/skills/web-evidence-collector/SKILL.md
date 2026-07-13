---
name: web-evidence-collector
description: Collect, verify, and structure public web evidence for brand, campaign, competitor, visual-material, video, offline activation, marketing, PR, social-platform, market, or event research. Use when the user asks for 证据采集, 竞品调研, 品牌调研, 社媒调研, 舆情素材收集, 案头调研, 找资料/收集资料, or when the user or a controller skill needs sourced materials, screenshots or visual leads, short quotes, brand hard-data candidates, platform-based collection shards, campaign linkage mapping, source coverage, evidence gaps, capability-aware collection fallback, an evidence brief, or a lossless Evidence Pool handoff to evidence-summary-analysis. This skill performs collection and evidence control only; it does not produce final strategy, positioning, Idea Platform, Concept, or insight conclusions.
---

# Web Evidence Collector

Use this skill to gather traceable evidence and turn it into a clean evidence pool. The job is to collect enough sourced material for downstream analysis, not to decide strategy.

This skill is the first layer in the workflow:

```text
controller skill -> web-evidence-collector -> evidence-summary-analysis -> insight-strategy
```

## Language And Market Defaults

- Default to Chinese for working communication and user-facing output.
- If the user writes in English, requests English deliverables, or specifies an overseas market, adapt the working language and research scope accordingly.
- For Chinese brands, Chinese categories, Chinese campaigns, or China-market strategy work, prioritize Chinese web context, Chinese search queries, and Chinese platforms before overseas sources.
- Use overseas or English-language sources when the brief names overseas markets, international competitors, global platforms, English campaigns, or cross-border context.
- Keep shared evidence schema field names stable in English so downstream skills can consume the evidence pool.
- Preserve source wording in its original language, especially raw quotes, slogans, post titles, and short visible phrases. Add Chinese explanation when useful, but do not replace the original source trail.

## Boundary

Do:

- Search for public, traceable sources across official, news, report, visual, campaign, video, offline activation, marketing, PR, and social channels.
- Probe available collection capabilities before claiming that collection has started or finished.
- Read the controller task packet when provided; avoid re-running broad front-end intake.
- Preserve any `Primary Research Lens`, `Supporting Research Lens`, and `Delivery Mode` supplied by the controller or user. Use the lens to prioritize source coverage only; do not turn it into an analytical conclusion.
- Ask brief fallback questions only when scope, depth, category, or existing material is too unclear to collect.
- Let the user or controller choose depth and material volume when they cannot predict the likely evidence scale.
- Recommend subagent collection mode only for broad, multi-dimensional requests; start subagents only after explicit user/controller approval.
- Capture links, dates, source names, source levels, short raw quotes, factual summaries, visual observations, screenshot status, and access restrictions.
- Preserve social-platform leads with a short key phrase plus link when full access, screenshots, or quotation is restricted.
- Build a campaign linkage map that connects related video, offline, marketing, PR, visual, and social evidence under the same campaign/message when the evidence supports the link.
- Collect brand hard-data candidates when relevant: brand philosophy, vision, slogan, brand claim, chronology, founder or leadership statements, product proof, service proof, brand behavior, and competitor distinction.
- Output source coverage, collection statistics, skew warnings, gaps, restrictions, and a downstream-compatible Evidence Pool.
- When live collection is unavailable, output a source plan, unresolved gaps, and user-needed materials instead of simulated evidence.

Do not:

- Produce human truths, final insights, cultural tensions, brand strategy, positioning, Idea Platform, Concept, or campaign recommendations.
- Treat brand-owned claims as audience truth.
- Claim that a source, platform, connector, export, screenshot, or search result was accessed when that capability was unavailable.
- Treat search snippets, aggregator pages, or social captions as confirmed facts unless traced to stronger sources.
- Bypass login, paywalls, private groups, CAPTCHAs, anti-bot controls, API access controls, or platform terms.
- Copy full articles, full reports, full comment threads, full social posts, or large copyrighted excerpts.

## Quick Workflow

1. Probe available collection capabilities and choose the highest-fidelity permitted route. Read `references/02-source-taxonomy-and-platforms.md`.
2. Clarify scope, depth, Research Lens, and Delivery Mode. If unclear, read `references/01-intake-and-depth.md`. Default to `General Evidence Overview` and pass through `Frontstage Brief` when no values are supplied.
3. Create a source plan and decide whether broad scope justifies subagent mode. Read `references/03-collection-workflow.md` and `references/10-subagent-collection-mode.md`.
4. Collect by platform-first shards, with material-category focus inside each shard. Read `references/05-material-categories.md` when relevant.
5. Track campaign links and evidence skew. Read `references/06-campaign-linkage-map.md` and `references/07-coverage-and-statistics.md`.
6. Handle social, structured-access, and platform boundaries. Read `references/08-social-platform-boundaries.md`.
7. Output the evidence brief and lossless handoff. Use `references/04-evidence-pool-contract.md` and `references/09-output-template.md`.
8. Run the pre-handoff regression checklist in `references/11-regression-checklist.md`.

## Intake Defaults

If a controller task packet gives enough detail, proceed. If not, ask no more than three concise fallback questions:

- What target should be researched: brand, campaign, event, competitor set, product, or market?
- Which categories, Research Lens, delivery mode, and depth: visual, video, offline activation, marketing, PR, social, reports; general or a named research direction; frontstage, full dossier, or client-facing; light, standard, deep, or exhaustive?
- What is already known or supplied: links, screenshots, platform exports, official brand materials, time range, geography, priority platforms, or forbidden sources?

When the user does not specify depth, state the standard default and proceed unless they object:

```text
I will use standard collection where evidence exists: Visual 5, Video 3, Offline activation 3, Marketing 5, PR 5, Social leads 5-10. I will mark missing categories and platform restrictions.
```

When the request meets the broad-task test in `references/10-subagent-collection-mode.md`, recommend subagent mode before starting, using the consent script defined in that file. That file holds the single canonical copy of the consent wording; do not maintain a second copy here.

## Capability Probe And Downgrade

Before collection, record which capability classes are actually available: authorized connector or export, direct public page access, public web search, browser/page inspection, and user-provided files or screenshots. Use capability classes rather than proprietary tool names. Treat existing user-provided material as privileged input and process it whenever it is in scope and inspectable.

Use the highest-fidelity permitted route for each source:

1. User-authorized connector, official interface, or authorized export
2. Direct public source through page access or browser inspection
3. Public web search, followed by tracing to the original source
4. Search-result lead or user-needed material when direct verification is unavailable

If no live web or platform capability is available, do not simulate collection. Set `Collection status` to `not collected - capability unavailable`, list a `Source Plan`, identify gaps and restrictions, and state exactly which links, screenshots, exports, or files the user should provide. If user-provided material can still be processed, collect only that material and mark the result `partially collected`.

## Output Contract

Always produce a two-layer Markdown handoff: a compact frontstage handoff for the user/controller, and a backend dossier for downstream skills.

### Default Frontstage Handoff

Show this layer by default. Keep it short and readable:

1. `Collection Readiness`
2. `Research Configuration`
3. `Evidence Brief Box`
4. `Source Coverage`
5. `Brand Hard Data Track` when relevant
6. `Key Campaign / Competitor Linkage`
7. `Gaps and Restrictions`
8. `Evidence Pool Handoff`

The `Evidence Brief Box` is the frontstage source summary for controller display. It should include:

- Source coverage in one short paragraph or table
- Primary and supporting Research Lens plus Delivery Mode
- Most reliable source groups
- Major restrictions and missing evidence
- Brand hard-data candidates found
- Evidence pool status and handoff note

Do not place final insights or strategy in the evidence brief.

Compress frontstage statistics to four items only:

- Total evidence items
- Source mix
- Restricted / user-needed items
- Linked campaign chains

Do not expand query plans, subagent task tables, shard search logs, long statistics tables, or repetition tables in the frontstage layer unless the user asks for the full dossier.

### Backend Dossier

Keep the full dossier available for downstream processing. Include these sections when full output is requested, when subagents were used, or when handing files to the next skill:

1. `Collection Brief`
2. `Research Configuration`
3. `Depth and Query Plan`
4. `Subagent Collection Plan` when recommended or used
5. `Evidence Shards` when subagents or platform shards were used
6. `Evidence Brief Box`
7. `Source Coverage`
8. `Brand Hard Data Track` when relevant
9. `Campaign Linkage Map`
10. `Collection Statistics`
11. `Campaign / Message Repetition Snapshot`
12. `Skew and Completeness Check`
13. `Gaps and Restrictions`
14. `Evidence Pool`

The `Evidence Pool` is the core result. Always preserve the complete backend pool for downstream use even when the frontstage handoff is compact. Frontstage compression may hide or link to the pool, but must never truncate, rewrite, or discard it.

Do not skip `evidence-summary-analysis`. The normal downstream order is:

```text
web-evidence-collector -> evidence-summary-analysis -> insight-strategy
```

If the user or controller asks for strategy output, end this skill at the Evidence Pool handoff to `evidence-summary-analysis`. Any later routing belongs to the controller or downstream skills.

The `Evidence Pool` uses the exact `Evidence Pool v1` contract in `references/04-evidence-pool-contract.md`. Every actual evidence item must keep these core fields first and in this spelling:

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

Do not omit or leave core fields blank. Use explicit values such as `not available`, `date unknown`, `audience unknown`, or `not applicable` where permitted. `Evidence ID` must always be unique, non-empty, and stable once assigned. For visual, video, event, packaging, landing-page, or screenshot evidence with no source quote, set `Raw quote` to `not available` and preserve a concrete factual `Observation`.

Then add the collector extension fields when available, such as `Source level`, `Category`, `Publisher / platform`, `Screenshot status`, `Brand hard data type`, `Needs user confirmation`, `Shard ID`, and `Merged from evidence IDs`. The complete extension-field list, allowed values, and ID stability rules live in `references/04-evidence-pool-contract.md`; read it before writing evidence items so items follow `Evidence Pool v1` exactly.

## Handoff Discipline

- Keep each evidence item focused on one fact, observation, quote, or traceable material.
- Carry `Primary Research Lens`, `Supporting Research Lens`, `Delivery Mode`, and `Lens adaptation note` as package metadata into `evidence-summary-analysis`. Do not add them as per-item evidence fields or rename material `Category` values to match a lens.
- Assign an `Evidence ID` once and never renumber it during de-duplication, shard merge, frontstage compression, or downstream handoff.
- Keep `Raw quote`, `Observation`, and `Summary` separate. Use `Observation` for what the source visibly shows, and never drop it because `Raw quote` is unavailable.
- Instruct `evidence-summary-analysis` to preserve every core field without deletion, renaming, translation, merging, or overwriting. It may add normalized fields, but must retain the collector values verbatim.
- For each `Brand Hard Data Track` candidate, include its source `Evidence ID`, candidate status, and `Needs user confirmation`. Keep brand-owned claims separate from audience evidence.
- Use campaign/message labels as collection aids, not strategic conclusions.
- Use brand hard-data labels as evidence aids, not final brand truth. Mark official claims and publicly inferred candidates separately.
- Mark inferred relationships as `tentative` unless multiple sources support the linkage.
- If requested evidence is unavailable, say what was searched, what was found, and what user-provided material would improve coverage.
- Keep the output machine-readable enough for `evidence-summary-analysis` to normalize without re-researching.

## Reference Map

- `references/01-intake-and-depth.md` - intake questions, depth presets, and user-controlled volume.
- `references/02-source-taxonomy-and-platforms.md` - capability routing, no-access downgrade, L1-L8 source levels, and platform coverage.
- `references/03-collection-workflow.md` - search, verification, capture, and evidence-item workflow.
- `references/04-evidence-pool-contract.md` - downstream-compatible schema.
- `references/05-material-categories.md` - collection fields for visual, video, offline, marketing, PR, social, and reports.
- `references/06-campaign-linkage-map.md` - related-evidence chains across channels and campaign/message labels.
- `references/07-coverage-and-statistics.md` - coverage metrics, skew checks, and completeness warnings.
- `references/08-social-platform-boundaries.md` - Xiaohongshu, Weibo, Douyin, Zhihu, Bilibili, WeChat public account, and other dynamic-platform handling.
- `references/09-output-template.md` - final Markdown handoff template.
- `references/10-subagent-collection-mode.md` - platform-first subagent planning, approval, shard prompts, and merge rules.
- `references/11-regression-checklist.md` - minimum cross-platform regression cases and pre-handoff checks.
