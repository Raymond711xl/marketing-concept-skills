---
name: insight-strategy
description: Transform an evidence pool, Strategy Readiness Pack, research notes, interviews, comments, reviews, competitive findings, campaign brief, or other sourced material into Level 1-4 insight strategy, an Idea Platform, and an evidence-backed Concept Package. Use when the user asks for 洞察策略, 人性洞察, 文化张力, 策略推导, 品牌真相, 概念推导, Big Idea, or wants themes, signals, human truths, cultural tensions, brand truth, strategy routes, Idea Platform candidates, recommended and alternative Concepts, Message Houses, or a dossier-ready insight-to-concept report. This skill consumes prepared evidence and does not perform open web research.
---

# Insight Strategy

Use this skill to turn an already-prepared input package into a complete
insight-to-concept decision. Read the brief, brand context, competitor context,
Strategy Readiness Pack, evidence pool, or raw-evidence report already provided
by the user or upstream research skill; separate fact from inference; then move
from signals to cultural tension, Idea Platform, and Concept Package.

In this system, `Idea Platform` is the formal term for the strategic platform
often called a Big Idea in advertising workflows. Use `Idea Platform` as the
working term because it becomes the foundation for later Concept development.

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
- A cleaned Evidence Pool, Strategy Readiness Pack, Research Lens Summary, and
  evidence gaps from `evidence-summary-analysis`
- A raw-evidence preparation report with high-frequency signals, language
  markers, and raw consumer voices
- Interview notes, comments, reviews, survey open ends, event feedback, or
  other sourced material that includes traceable quotes or observations

If the user only provides raw tabular consumer text, optionally run
`scripts/prepare_raw_evidence.py` and follow
`references/02-optional-raw-evidence-preparation.md` before entering Level 1.
This is an input-adaptation step, not a separate strategy stage.

Before analysis, preserve existing evidence IDs. Assign local trace IDs to
unindexed supplied material: `BR-###` for brief facts, `BF-###` for brand facts,
`CP-###` for competitor facts, and `RAW-###` for adapted raw evidence. Never
leave a major judgment or Message House Foundation supported only by a file name
or an untraceable summary.

Accept upstream Markdown fields in their stable Title Case form, including
`Evidence ID`, `Raw quote`, `Observation`, and `Confidence`. Treat upstream
`Research Lens` as evidence-organization metadata, not as an `Insight lens`,
theme, motive, or strategic conclusion.

## Workflow

Follow the four-level ladder and close with a Concept Package:

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
4. **Level 4: Strategic Decision** - connect cultural tension with brand truth
   and proof edge to derive and select an Idea Platform. Read both
   `references/06-level4-strategic-decision.md` and
   `references/10-strategy-models-library.md`. Treat models only as Level 4
   derivation routes; keep `Cultural Tension x Brand Truth x Proof Edge` as the
   governing logic.
5. **Concept Package** - translate the selected Idea Platform into one
   recommended Concept and 1-2 alternative Concepts, each with a complete
   Message House, evidence support, proof gaps, risks, and Final or Provisional
   status. Use `references/11-concept-and-message-house-guide.md`,
   `assets/templates/concept-record-template.md`, and
   `assets/templates/concept-package-template.md`.

Complete Step 5 by default. Stop at an earlier stage only when the user
explicitly requests a focused pass or Input Readiness is `Unavailable`.

Before finalizing, apply `references/07-evidence-confidence-rules.md`.
For the final deliverable, use `references/08-final-report-template.md`.

## Operating Rules

- Preserve the source trail. Every major claim should trace back to evidence.
- Require Evidence IDs for Level 1 themes, Level 2 human truths, Level 3
  tensions, Level 4 brand truth and proof edge, every Concept Roof and Pillar,
  and every Message House Foundation item.
- Label inference strength honestly: high, medium, low, or speculative.
- Use only the information already in the input package during Level 4. If
  brand truth, product proof, brand behavior, or competitor difference is
  insufficient, mark the strategy provisional and recommend a rollback to brief
  or research instead of inventing missing facts.
- Do not treat high-frequency words as insight by themselves. They are signals,
  not conclusions.
- Keep divergent and convergent thinking separate: expand in Levels 1-3, choose
  in Level 4.
- Treat `Strategy Readiness Pack` as the preferred bridge into Level 4 when it
  exists. If brand hard data is still thin, continue with a provisional
  recommendation and name the upstream collection or user-confirmation gap
  instead of stopping the workflow.
- Use `Unavailable` only when there is no traceable material from which Level 1
  can be formed. Use `Provisional` when analysis is possible but critical
  evidence, brand truth, proof edge, or competitor difference remains weak.
  Use `Final` only when the selected strategy and Concept foundations are
  sufficiently evidenced. Never fill gaps to obtain `Final`.
- Do not perform fresh file intake or open research during Level 4 or Concept
  generation. Carry gaps forward and name a rollback path.

## Resource Map

- `assets/templates/input-package-template.md` - preferred handoff format into
  this skill.
- `assets/templates/brand-facts-pack-template.md` - preferred Level 4 hard-data
  bridge for brand truth, proof, behavior, and competitor distinction.
- `assets/templates/evidence-pool-template.md` - evidence-only handoff format
  from research skills.
- `assets/templates/insight-map-template.md` - working structure for Levels 1-3.
- `assets/templates/human-truth-record-template.md` - one-card structure for a
  Level 2 motive inference.
- `assets/templates/cultural-tension-record-template.md` - one-card structure
  for a Level 3 cultural tension.
- `assets/templates/idea-platform-record-template.md` - one-card structure for
  the Level 4 Idea Platform.
- `assets/templates/concept-record-template.md` - one-card structure for
  each recommended or alternative Concept.
- `assets/templates/concept-package-template.md` - complete recommended and
  alternative Concept package for dossier writeback.
- `references/10-strategy-models-library.md` - Level 4 model-selection library
  for derivation routes and contrast candidates.
- `references/11-concept-and-message-house-guide.md` - Concept and Message
  House workflow after an Idea Platform is selected.
- `assets/templates/evidence-matrix-template.csv` - structured evidence index
  for large research packages.
- `assets/templates/final-strategy-report-template.md` - final report skeleton.
- `assets/lexicons/` - starter lexicons (motive, emotion, topic-tag, synonym,
  platform-slang, and tension-domain CSVs) used only by the optional
  raw-evidence preparation script. See
  `assets/lexicons/README-lexicon-sourcing.md` for rules on expanding them from
  real project corpora without bundling unclear third-party dictionaries.
- `references/09-materials-and-licensing.md` - boundary rules for missing
  templates, proprietary references, and third-party lexicons.

## Development Resources

Do not read `examples/` during normal strategy runs. Those files are
development-only fixtures and can bias live judgment. Read the golden case only
when running regression checks, reviewing expected output shape, or when the
user explicitly asks for a worked example. Use
`scripts/run_regression_checks.py` for the bundled contract checks.
