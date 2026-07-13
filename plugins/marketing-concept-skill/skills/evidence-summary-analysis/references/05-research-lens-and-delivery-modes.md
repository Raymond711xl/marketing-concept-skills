# Research Lens And Delivery Modes

Use this reference to choose how prepared evidence is organized and presented.
`Research Lens` is an analytical viewing frame. `Delivery Mode` is a presentation
contract. Neither changes the underlying Evidence Pool.

## Contents

- Selection Contract
- Research Lens Catalog
- Common Lens Finding Contract
- Lens-specific Modules
- Delivery Modes
- Multi-lens Rules
- Boundary Fallbacks

## Selection Contract

Record these values in output metadata:

```markdown
- Primary Research Lens:
- Supporting Research Lens:
- Delivery Mode:
- Lens adaptation note:
```

Rules:

- Keep `Category` for evidence form and `Research Lens` for research purpose.
- Use one primary lens by default. Add up to two supporting lenses when the user
  requests them or the brief clearly needs them. Honor additional explicit
  selections, but state the expected visible length before rendering them.
- When no lens is specified, use `General Evidence Overview`; infer one named
  lens only when the user's requested report direction is explicit.
- When no mode is specified, use `Frontstage Brief` for normal/controller
  display. Use `Full Evidence Dossier` for explicit full/audit requests and
  `Client-facing Research Report` only for explicit client-facing requests.
- Preserve all evidence in the Cleaned Evidence Pool even when it is not used in
  the visible lens summary.
- If a selected lens lacks evidence, produce a lens-specific collector task. Do
  not fill it with general knowledge or unsupported claims.
- Preserve the user's original report wording in `Lens adaptation note` when it
  maps to an evidence-only canonical lens.

When the user asks to choose rather than naming a direction, present this compact
selection list and allow one primary plus optional supporting lenses:

```text
Research Lens: Brand Assets & Marketing / Industry & Market Evidence /
Consumer Evidence / Competitive Intelligence / Product Facts / Platform Trends /
Issue & Reputation / Campaign Case Studies / Humanities & Technology Context

Delivery Mode: Frontstage Brief / Full Evidence Dossier /
Client-facing Research Report
```

## Research Lens Catalog

| Canonical Research Lens | Chinese request aliases | Evidence-only scope | Required visible module |
| --- | --- | --- | --- |
| General Evidence Overview | 综合调研、资料总览 | Cross-category coverage, patterns, contradictions, gaps | General Evidence Findings |
| Brand Assets & Marketing | 品牌资产与营销研究、品牌营销研究 | Brand hard data, visible assets, messages, campaign behavior, channel deployment | Brand Asset Register + Marketing Deployment Map |
| Industry & Market Evidence | 行业与战略研究、行业研究 | Category facts, players, market structure, policy/report facts, observable changes | Industry Fact And Structure Table |
| Consumer Evidence | 消费者洞察研究、用户研究 | Sourced language, behavior, complaints, usage contexts, stated audience labels | Consumer Evidence Table |
| Competitive Intelligence | 竞品情报研究、竞品研究 | Competitor claims, products, channels, campaigns, visible distinctions | Competitor Comparison Matrix |
| Product Facts | 产品事实研究、产品研究 | Specifications, claims, price, service, proof, third-party validation, contradictions | Product Fact Ledger |
| Platform Trends | 平台趋势研究、平台研究 | Time-stamped formats, mechanics, topics, visible metrics, cross-period changes | Platform Signal Timeline |
| Issue & Reputation | 热点舆情研究、舆情研究、PR 风险研究 | Event timeline, source spread, message frames, response indicators, official response | Issue Timeline And Frame Map |
| Campaign Case Studies | 成功案例研究、营销案例研究 | Stated objective, execution chain, materials, channels, mechanism, supported results | Campaign Case Record |
| Humanities & Technology Context | 人文科技研究、社会文化与科技研究 | Traceable social, institutional, humanities, and technology context signals | Context Signal Map |

Evidence-only adapters:

- Map `行业与战略研究` to `Industry & Market Evidence`. Pass any strategic
  implication request to `insight-strategy`.
- Map `消费者洞察研究` to `Consumer Evidence`. Do not infer motive, Human Truth,
  or cultural tension.
- Use `Platform Trends` only when evidence supports temporal or repeated change.
  Otherwise label the output `Platform Current Signals`.
- Use `Issue & Reputation`; do not claim overall sentiment without a disclosed,
  adequate sample.
- A user may request `成功案例研究`, but label a case `evidence-supported case`
  until results or credible outcome evidence supports success.

## Common Lens Finding Contract

Every lens summary must include:

```markdown
| Finding | Evidence ID | Source spread | Contradiction / limitation | Confidence |
| --- | --- | --- | --- | --- |
```

Write findings as descriptions of sourced material. Avoid advice, causal claims,
audience motives, cultural judgments, positioning, or strategic implications.

## Lens-specific Modules

### General Evidence Overview

- `General Evidence Findings`: use the common finding contract to show the
  strongest cross-category facts, patterns, contradictions, and gaps.

### Brand Assets & Marketing

- `Brand Asset Register`: asset/claim, material or hard-data type, Evidence ID,
  use context, consistency/conflict, Confidence.
- `Marketing Deployment Map`: campaign/message, channel, material/mechanism,
  related Evidence IDs, observable repetition, gap, Confidence.

### Industry & Market Evidence

- `Industry Fact And Structure Table`: fact/signal, period/geography, player or
  institution, Evidence ID, source level, limitation, Confidence.
- Separate reported market facts from one-source forecasts and source opinions.

### Consumer Evidence

- `Consumer Evidence Table`: sourced behavior/language, context, stated audience,
  Evidence ID, source type, counter-evidence, Confidence.
- Describe what people said or did. Do not explain why they think or feel it.

### Competitive Intelligence

- `Competitor Comparison Matrix`: competitor, visible claim/product/behavior,
  channel/material, Evidence ID, difference visible in evidence, Confidence.
- Do not convert visible difference into strategic whitespace or positioning.

### Product Facts

- `Product Fact Ledger`: fact or claim, official/third-party/user-reported status,
  Evidence ID, validation or contradiction, Confidence.
- Keep specifications and proven performance separate from advertising claims.

### Platform Trends

- `Platform Signal Timeline`: date/period, platform signal, format/mechanism,
  metric if visible, Evidence ID, comparison basis, Confidence.
- Require at least two comparable periods or repeated dated evidence before using
  `trend`, `rising`, `declining`, or similar change language.

### Issue & Reputation

- `Issue Timeline And Frame Map`: date, event/source frame, actor, public response
  indicator, official response, Evidence ID, Confidence.
- State sampling limits. Do not generalize a few posts into public opinion.

### Campaign Case Studies

- `Campaign Case Record`: stated objective, audience label, message, execution
  chain, material/channel linkage, mechanism, supported result, Evidence IDs,
  missing proof, Confidence.
- Use `result not available` when outcome evidence is absent.

### Humanities & Technology Context

- `Context Signal Map`: context fact or discourse, domain, institution/source,
  date, Evidence ID, relevance to the research target, limitation, Confidence.
- Relevance must remain descriptive. Cultural tension belongs downstream.

## Delivery Modes

| Canonical Delivery Mode | Chinese request aliases | Visible effect |
| --- | --- | --- |
| Frontstage Brief | 前台简报、快速版、先看摘要 | Compact review with pool/dossier entry |
| Full Evidence Dossier | 完整资料档案、完整调研、审计版 | Full evidence-bound handoff |
| Client-facing Research Report | 框架客户版、客户版、可给客户看、报告版 | Client-readable Markdown report plus evidence index |

### Frontstage Brief

Use for normal controller display or quick review. Show:

1. Research Configuration
2. Frontstage Content Strips
3. Three to five selected-lens findings
4. Key contradictions and evidence gaps
5. Strategy readiness status
6. Explicit Cleaned Evidence Pool or dossier entry

Keep the full Cleaned Evidence Pool and Strategy Readiness Pack backstage.

### Full Evidence Dossier

Use when the user asks for full research, audit, source review, or downstream
handoff. Use the full order in `03-output-templates.md`, including all selected
lens modules, Strategy Readiness Pack, gaps, and Cleaned Evidence Pool.

### Client-facing Research Report

Use only when the user asks for 框架客户版, 客户版, 可给客户看, or a
client-ready report.
Render the visible Markdown body as:

```markdown
# [Target] [Research Lens] Research Report

## Executive Evidence Summary
## Scope And Method
## Key Evidence Findings
## [Selected Lens Module]
## Cross-source Patterns And Contradictions
## Evidence Gaps And Restrictions
## Source Notes And Confidence
## Evidence Index
```

Use readable display titles while retaining Evidence IDs beside every material
finding. Do not hide caveats to make the report sound more decisive. Keep the
Strategy Readiness Pack and full Cleaned Evidence Pool in the backstage handoff;
the visible report must include either an Evidence Index or their explicit file
entry. This mode changes editorial presentation only. It does not create a DOCX,
PDF, PPT, strategic recommendation, Human Truth, or cultural judgment.

## Multi-lens Rules

- Present the primary lens first and supporting lenses after it.
- Reuse Evidence IDs across lenses instead of duplicating Evidence Pool items.
- When one finding belongs to several lenses, keep one factual wording and vary
  only the module context.
- State estimated visible length before rendering more than three lenses.
- Do not activate every lens merely because evidence exists.

## Boundary Fallbacks

When a requested conclusion exceeds this skill, output the closest evidence
module and a downstream note:

| Requested conclusion | Output here | Downstream owner |
| --- | --- | --- |
| Industry strategy or recommendation | Industry & Market Evidence | insight-strategy |
| Consumer insight or Human Truth | Consumer Evidence | insight-strategy |
| Cultural meaning or tension | Context signals only | insight-strategy |
| Strategic competitor whitespace | Competitor evidence matrix | insight-strategy |
| Positioning, Idea Platform, Concept | Strategy Readiness Pack | insight-strategy |
