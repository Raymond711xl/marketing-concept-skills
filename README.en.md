# Man Ce｜Marketing Concept Skill

[中文](README.md)｜English

The first half of proposal writing, paced slowly with AI.

Version: 0.7.0  
Status: Draft / Alpha  
License: MIT

Man Ce is a Chinese-first skill bundle for brand strategy and marketing concept development. It helps users move from a rough brief to evidence collection, evidence summary, insight strategy, Idea Platform, and finally a discussable Concept.

In this system, `Idea Platform` is the strategic platform before Concept. It is close to what advertising teams often call a Big Idea, but it is not the final creative concept itself.

This project is currently a `0.7.0` draft. It can be used as an internal workflow, but should still be validated on real projects before public release.

## Core Flow

```text
Brief -> Evidence Collection -> Evidence Summary -> Insight Strategy -> Idea Platform -> Concept
```

Man Ce only covers the first half of proposal work. Copywriting, visual design, scripts, proposal decks, and execution assets after Concept are outside the current system.

## Skills

- `concept-strategy-controller`: the front-stage controller. It reads the brief, chooses the route, compresses stage progress, and maintains the backstage dossier.
- `web-evidence-collector`: collects traceable public web evidence and creates an evidence pool.
- `evidence-summary-analysis`: cleans, classifies, and summarizes evidence patterns without making final strategy decisions.
- `insight-strategy`: turns a prepared evidence package into fact-layer themes, human truths, cultural tensions, Idea Platform candidates, and strategic recommendations.

## Good For

- Starting brand or campaign strategy research from zero.
- Organizing links, screenshots, notes, comments, reports, or messy research.
- Extracting evidence patterns from competitors, social platforms, PR, videos, and visual materials.
- Deriving audience motives, cultural tensions, brand stance, and Idea Platform.
- Turning an Idea Platform into a discussable Concept.
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
