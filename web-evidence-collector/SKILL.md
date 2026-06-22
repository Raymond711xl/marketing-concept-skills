---
name: web-evidence-collector
description: Collect, verify, and structure public web evidence for brand, campaign, competitor, visual-material, video, offline activation, marketing, PR, social-platform, market, or event research. Use when the user or a controller skill needs sourced materials, screenshots or visual leads, short quotes, platform-based collection shards, campaign linkage mapping, source coverage, evidence gaps, or a downstream-ready evidence pool for evidence-summary-analysis or insight-strategy. This skill performs collection and evidence control only; it does not produce final strategy, positioning, Big Idea, or insight conclusions.
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
- Read the controller task packet when provided; avoid re-running broad front-end intake.
- Ask brief fallback questions only when scope, depth, category, or existing material is too unclear to collect.
- Let the user or controller choose depth and material volume when they cannot predict the likely evidence scale.
- Recommend subagent collection mode for large, multi-platform, multi-theme, or multi-material requests; start subagents only after explicit user/controller approval.
- Capture links, dates, source names, source levels, short raw quotes, factual summaries, visual observations, screenshot status, and access restrictions.
- Preserve social-platform leads with a short key phrase plus link when full access, screenshots, or quotation is restricted.
- Build a campaign linkage map that connects related video, offline, marketing, PR, visual, and social evidence under the same campaign/message when the evidence supports the link.
- Output source coverage, collection statistics, skew warnings, gaps, restrictions, and a downstream-compatible Evidence Pool.

Do not:

- Produce final insights, cultural tensions, brand strategy, positioning, creative Big Idea, or campaign recommendations.
- Treat brand-owned claims as audience truth.
- Treat search snippets, aggregator pages, or social captions as confirmed facts unless traced to stronger sources.
- Bypass login, paywalls, private groups, CAPTCHAs, anti-bot controls, API access controls, or platform terms.
- Copy full articles, full reports, full comment threads, full social posts, or large copyrighted excerpts.

## Quick Workflow

1. Clarify scope and depth. If unclear, read `references/01-intake-and-depth.md`.
2. Select source levels and platforms. Read `references/02-source-taxonomy-and-platforms.md`.
3. Decide whether subagent collection mode is useful. Read `references/10-subagent-collection-mode.md` when the task spans multiple platforms, themes, or material categories.
4. Collect by platform-first shards, with material-category focus inside each shard. Read `references/03-collection-workflow.md` and, when relevant, `references/05-material-categories.md`.
5. Track campaign links and evidence skew. Read `references/06-campaign-linkage-map.md` and `references/07-coverage-and-statistics.md`.
6. Handle social, API, and access boundaries. Read `references/08-social-platform-boundaries.md`.
7. Output the handoff. Use `references/04-evidence-pool-contract.md` and `references/09-output-template.md`.

## Intake Defaults

If a controller task packet gives enough detail, proceed. If not, ask no more than three concise fallback questions:

- What target should be researched: brand, campaign, event, competitor set, product, or market?
- Which categories and depth: visual, video, offline activation, marketing, PR, social, reports; light, standard, deep, or exhaustive?
- What is already known or supplied: links, screenshots, platform exports, time range, geography, priority platforms, or forbidden sources?

When the user does not specify depth, state the standard default and proceed unless they object:

```text
I will use standard collection where evidence exists: Visual 5, Video 3, Offline activation 3, Marketing 5, PR 5, Social leads 5-10. I will mark missing categories and platform restrictions.
```

When the request is broad, recommend subagent mode before starting:

```text
This collection spans multiple platforms/material types. I recommend subagent collection mode to keep platform evidence cleaner and more vertical. It will cost more tokens. Do you want me to proceed with subagents?
```

## Output Contract

Always end with a Markdown handoff containing:

1. `Collection Brief`
2. `Depth and Query Plan`
3. `Subagent Collection Plan` when recommended or used
4. `Evidence Shards` when subagents or platform shards were used
5. `Source Coverage`
6. `Campaign Linkage Map`
7. `Collection Statistics`
8. `Skew and Completeness Check`
9. `Gaps and Restrictions`
10. `Evidence Pool`

The `Evidence Pool` must keep the downstream core fields first:

- `Source type`
- `Source name`
- `Date`
- `URL or citation`
- `Raw quote`
- `Summary`
- `Topic tag`
- `Audience`
- `Confidence`

Then add collector-specific fields when available:

- `Evidence ID`
- `Source level`
- `Category`
- `Publisher / platform`
- `Author / account`
- `Access date`
- `Brand / event`
- `Campaign / message`
- `Channel`
- `Material type`
- `Visual material`
- `Screenshot status`
- `Key fact`
- `Evidence value`
- `Related evidence`
- `Limitation / restriction`

## Handoff Discipline

- Keep each evidence item focused on one fact, observation, quote, or traceable material.
- Use `Observation`-style wording for visuals when there is no quote.
- Use campaign/message labels as collection aids, not strategic conclusions.
- Mark inferred relationships as `tentative` unless multiple sources support the linkage.
- If requested evidence is unavailable, say what was searched, what was found, and what user-provided material would improve coverage.
- Keep the output machine-readable enough for `evidence-summary-analysis` to normalize without re-researching.

## Reference Map

- `references/01-intake-and-depth.md` - intake questions, depth presets, and user-controlled volume.
- `references/02-source-taxonomy-and-platforms.md` - L1-L8 source levels, platform coverage, and API-first rules.
- `references/03-collection-workflow.md` - search, verification, capture, and evidence-item workflow.
- `references/04-evidence-pool-contract.md` - downstream-compatible schema.
- `references/05-material-categories.md` - collection fields for visual, video, offline, marketing, PR, social, and reports.
- `references/06-campaign-linkage-map.md` - related-evidence chains across channels and campaign concepts.
- `references/07-coverage-and-statistics.md` - coverage metrics, skew checks, and completeness warnings.
- `references/08-social-platform-boundaries.md` - Xiaohongshu, Weibo, Douyin, Zhihu, Bilibili, WeChat public account, and other dynamic-platform handling.
- `references/09-output-template.md` - final Markdown handoff template.
- `references/10-subagent-collection-mode.md` - platform-first subagent planning, approval, shard prompts, and merge rules.
