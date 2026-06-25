# Man Ce｜Marketing Concept Skill

[中文](README.md)｜English

The first half of proposal writing, paced slowly with AI.

Version: 0.7.9  
Status: Draft / Alpha  
License: MIT

Man Ce is a Chinese-first skill bundle for brand strategy and marketing concept development. It helps users move from a rough brief to evidence preparation, insight strategy, Idea Platform, and finally a discussable Concept.

Version `0.7.9` upgrades the `insight-strategy` layer around Insight Reality: fact reading, motive inference, cultural tension, strategic decision, model comparison, and Message House development after the Idea Platform.

## Core Flow

```text
Brief
  -> Evidence Collection
  -> Evidence Summary
  -> Insight Strategy
  -> Idea Platform
  -> Concept
```

Man Ce covers the first half of proposal work. Copywriting, visual design, KV, scripts, proposal decks, and execution assets after Concept are outside the current system.

## Skills

- `concept-strategy-controller`: front-stage controller. It reads the brief, chooses the route, compresses stage progress, and maintains the backstage dossier.
- `web-evidence-collector`: collects public web evidence, platform signals, competitor material, brand-owned facts, campaign links, and evidence gaps.
- `evidence-summary-analysis`: cleans, classifies, and summarizes evidence patterns into a Strategy Readiness Pack.
- `insight-strategy`: turns prepared evidence into human truths, cultural tensions, brand truth, proof edge, Idea Platform candidates, and Concept-ready strategy.

## Good For

- Starting brand or campaign strategy research from zero.
- Organizing links, screenshots, notes, comments, reports, or messy research.
- Extracting evidence patterns from competitors, social platforms, PR, videos, and visual materials.
- Deriving audience motives, cultural tensions, brand stance, and Idea Platform.
- Turning an Idea Platform into a discussable Concept and Message House.
- Pausing, deepening, revising, or returning to a specific stage.

## Not For

- Jumping straight to final advertising copy without evidence or strategy.
- Producing final copywriting, visual design, KV, scripts, proposal pages, or execution assets.
- Bypassing logins, paywalls, anti-bot controls, private groups, or platform restrictions.
- Treating brand-owned claims as consumer truth.

## Language And Market Defaults

- Default working language and user-facing output: Chinese.
- For China-market work, prioritize Chinese web context, Chinese search queries, and Chinese platforms.
- Switch or adapt to English / overseas research when the brief specifies English deliverables, overseas markets, international competitors, global platforms, or cross-border context.
- Preserve original source wording where possible.
- Keep shared schema fields in English where they work as handoff contracts, such as `Evidence Pool`, `Confidence`, `Raw quote`, `Insight Map`, and `Idea Platform Record`.

## Insight Reality Strategy Model

`insight-strategy` works through a four-level ladder:

```text
Level 1: Fact Layer
Level 2: Motive Inference
Level 3: Cultural Judgment
Level 4: Strategic Decision
```

The default governing logic is:

```text
Idea Platform = Cultural Tension x Brand Truth x Proof Edge
```

A strong Idea Platform is not a slogan. It must connect a real cultural tension, a credible brand truth, and a proof edge the brand can demonstrate through product, service, behavior, channel, or content.

## Strategy Models Library

Version `0.7.9` adds an optional model-selection library for Level 4. It can compare routes such as Default Idea Platform, Ogilvy Big Ideal, Ogilvy positioning triangle, 3C, The Butterfly, USP / SMP / ESP, Challenger Brand, Cultural Branding, Golden Circle, Brand Key, Jobs To Be Done, and Get / To / By / So.

These models are derivation routes, not separate outputs. Every route is normalized back into the shared `Idea Platform Record`.

## Message House

After an Idea Platform is selected, Man Ce can develop Concepts through a Message House:

```text
Idea Platform
  -> Concept A -> Message House
  -> Concept B -> Message House
  -> Concept C -> Message House
```

Each Concept has:

- `Roof`: the single core message or claim.
- `Pillars`: 2-3 supporting messages.
- `Foundation`: evidence, product proof, brand behavior, examples, or source material.

If the Roof cannot be supported by Pillars and Foundation, the Concept should remain provisional or be revised.

## Stage Commands

Use explicit stage commands instead of `@` mentions:

- `进入：证据采集`
- `进入：证据摘要`
- `进入：策略洞察`
- `进入：Idea Platform`
- `进入：Concept`
- `查看：资料池`
- `回退到：证据摘要`
- `继续`

## Output Layers

- `Frontstage Output`: short, decision-oriented responses shown in chat.
- `Backstage Dossier`: structured project memory containing brief, evidence, summaries, insights, strategy candidates, Idea Platform records, Concept records, and open questions.

For real projects, the controller should export or maintain a Markdown dossier by default, but it should not print the whole dossier into chat unless the user asks to view it.
