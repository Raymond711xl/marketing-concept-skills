---
name: insight-strategy
description: Transform an evidence pool, social listening report, research notes, interviews, comments, reviews, competitive findings, or other sourced material into brand insight and strategy. Use when the user wants themes, signals, human truths, cultural tensions, Brand's Best Self, Brand Big IdeaL candidates, strategic recommendations, or an insight-to-strategy report. This skill consumes evidence; it does not perform open web research unless another research skill or the user provides the evidence pool.
---

# Insight Strategy

Use this skill to turn an already-prepared input package into strategy. The
core job is not to collect more information; it is to read the brief, brand
context, competitor context, evidence pool, or listening report already provided
by the user or upstream research skill, separate fact from inference, and climb
from signals to cultural tension to a brand strategy decision.

## Language And Market Defaults

- Default to Chinese for working communication and user-facing output.
- If the user writes in English, requests English deliverables, or specifies an overseas market, adapt the working language and strategic framing accordingly.
- For Chinese brands, Chinese categories, Chinese campaigns, or China-market strategy work, read evidence through Chinese network, platform, media, cultural, and consumer-language context.
- Use overseas or English-language strategic context when the input package names overseas markets, international competitors, global platforms, English campaigns, or cross-border context.
- Keep shared evidence, insight, and strategy field names stable in English when they function as handoff schema.
- Preserve source wording in its original language, especially raw quotes, slogans, post titles, and consumer voices. Add Chinese explanation when useful, but do not replace the original source trail.

## Input Contract

Start with `references/01-input-package-contract.md`. Accept any of these
inputs as the working package:

- A client brief or project brief from a coordination/control skill
- Brand facts from the user, public brand materials, or upstream research
- Competitor difference and category context from upstream research
- A structured evidence pool from a research or competitive-research skill
- A social listening initial-wash report with high-frequency words, emotion
  scan, and raw consumer voices
- Interview notes, comments, reviews, survey open ends, event feedback, or
  other sourced material that includes traceable quotes or observations

If the user only provides raw tabular social comments, optionally run
`scripts/phase1_social_listening_cleaning.py` and follow
`references/02-optional-social-listening-cleaning.md` before entering Level 1.
This is an input-adaptation step, not a separate strategy stage.

## Workflow

Follow the four-level ladder in order:

0. **Input Readiness** - assemble the supplied brief, brand context, competitor
   context, evidence pool, and listening material into one working package. Use
   `references/01-input-package-contract.md`.
1. **Level 1: Fact Layer** - read the evidence and produce themes, signals,
   and raw-voice support. Use `references/03-level1-fact-layer.md`.
2. **Level 2: Motive Inference** - infer emotions, needs, fears, and human
   truths from Level 1. Use `references/04-level2-motive-inference.md`.
3. **Level 3: Cultural Judgment** - synthesize cross-theme cultural tensions
   using What is / What should be / Why now. Use
   `references/05-level3-cultural-judgment.md`.
4. **Level 4: Strategic Decision** - connect cultural tension with Brand's Best
   Self and derive Brand Big IdeaL candidates. Use
   `references/06-level4-strategic-decision.md`.

Before finalizing, apply `references/07-evidence-confidence-rules.md`.
For the final deliverable, use `references/08-final-report-template.md`.

## Operating Rules

- Preserve the source trail. Every major claim should trace back to evidence.
- Label inference strength honestly: high, medium, low, or speculative.
- Use only the information already in the input package during Level 4. If
  Brand's Best Self, product proof, brand history, or competitor difference is
  insufficient, mark the strategy provisional and recommend a rollback to brief
  or research instead of inventing missing facts.
- Do not treat high-frequency words as insight by themselves. They are signals,
  not conclusions.
- Keep divergent and convergent thinking separate: expand in Levels 1-3, choose
  in Level 4.

## Resource Map

- `assets/templates/input-package-template.md` - preferred handoff format into
  this skill.
- `assets/templates/evidence-pool-template.md` - evidence-only handoff format
  from research skills.
- `assets/templates/insight-map-template.md` - working structure for Levels 1-3.
- `assets/templates/final-strategy-report-template.md` - final report skeleton.
- `assets/lexicons/` - starter lexicons used only by the optional social
  listening cleaning script.
