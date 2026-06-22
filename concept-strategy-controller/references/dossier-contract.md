# Backstage Dossier Contract

Use this reference whenever the controller needs to preserve project memory, hand work to a downstream skill, show the user the material base, resume a paused stage, or return to an earlier stage.

The backstage dossier is the complete structured memory of the project. It may be long. The frontstage output should remain short.

By default, the controller should export or maintain a Markdown dossier for real projects, while showing only the relevant portion in the conversation. Exporting a dossier means writing structured project memory to a file; it does not mean printing the whole dossier into chat.

## Two Output Layers

### Frontstage Output

Use this for user-facing progress:

- Current conclusion
- Content strips for the current stage
- Evidence brief box when evidence preparation finishes
- Why it matters
- Key evidence or reasoning
- Confidence
- Gaps
- Decision options
- Suggested next action

Keep it short enough for the user to decide whether to continue, deepen, return, or revise.

### Backstage Dossier

Use this for downstream work and user inspection:

- User original brief
- Project startup packet
- Working brief
- Controller interpretation
- Evidence pool
- Cleaned evidence pool
- Source coverage and restrictions
- Evidence preparation brief
- Brand hard data track
- Category summaries
- Evidence pattern inventory
- Strategy readiness pack
- Insight map
- Strategy candidates
- Idea Platform records
- Concept records
- Open questions and caveats

Compression should reduce reading burden, not remove evidence, uncertainty, source trails, or strategic caveats.

## Dossier Template

```markdown
# Backstage Dossier: [Working Title]

## 0. User Original Brief

## 1. Project Startup Packet

## 2. Controller Interpretation

- Current route:
- Current stage:
- Stage goal:
- Assumptions:
- Constraints:
- Open questions:

## 3. Evidence Base

### Evidence Preparation Brief

- Mode: default / audit
- Brief status:
- Full evidence pool file:
- User confirmation status:

### Source Coverage

### Brand Hard Data Track

- Brand philosophy / vision:
- Slogan / brand claim:
- Brand chronology:
- Founder or leadership statement:
- Product proof:
- Service / experience proof:
- Brand behavior:
- Competitor distinction:
- Confirmation status:

### Evidence Pool

### Gaps And Restrictions

## 4. Evidence Summary

### Frontstage Content Strips

- Source coverage strip:
- Strong evidence pattern strip:
- Brand hard data strip:
- Evidence gap strip:
- Strategy readiness strip:

### Category Summaries

### Evidence Pattern Inventory

### Strategy Readiness Pack

- Brand truth candidates:
- Proof edge candidates:
- Brand behavior evidence:
- Competitor distinction:
- User confirmation needed:
- Recommended next step:

### Cleaned Evidence Pool

## 5. Insight Strategy

### Level 1 - Fact Layer

### Level 2 - Motive Inference

### Level 3 - Cultural Judgment

### Level 4 - Strategic Decision

## 6. Idea Platform Records

### Idea Platform 1

- Statement:
- Cultural tension answered:
- Brand truth used:
- Proof edge:
- Why the brand can own it:
- Emotional charge:
- Strategic implications:
- Risks / weak assumptions:
- Validation needed:

## 7. Concept Records

### Concept 1

- Concept name:
- One-sentence concept:
- Human / cultural tension:
- Brand belief:
- Audience role:
- Proof mechanism:
- Expression territory:
- Must stay consistent:
- Must avoid:
- Confidence:
- Open questions:

## 8. Decision Log

| Date / turn | Decision | Reason | Impact |
| --- | --- | --- | --- |

## 9. Next Options

- Continue:
- Deepen:
- Return:
- Stop:
```

## Dossier Export Rules

- Default export location: `dossiers/[project-slug]/backstage-dossier.md`.
- If no project slug exists, create one from the working title.
- Do not print the full dossier in chat unless the user asks to view it.
- Update only changed sections when possible.
- Do not overwrite a materially different previous dossier without preserving a dated copy, such as `backstage-dossier-YYYYMMDD-HHMM.md`.
- If filesystem export is unavailable on a platform, keep the dossier as structured chat memory and offer a copyable Markdown block only when requested.

## Downstream Handoff Packet

Whenever handing work to a specialist skill, send this packet:

```markdown
## Downstream Handoff Packet

### User Original Brief

### Controller Interpretation

- Current route:
- Current stage:
- Task goal:
- What to do:
- What not to do:
- Desired output depth:

### Relevant Backstage Dossier

### Specific Task
```

Never send only a short summary when original user input or complete evidence exists.

## Update Rules

- Add new evidence to the evidence base, not to strategy sections.
- Add cleaned and summarized material to evidence summary, not directly to insights.
- Add brand hard data candidates to `Brand Hard Data Track` and mark whether they are user-supplied, publicly collected, or still need confirmation.
- Add evidence-preparation content strips and the evidence brief box to frontstage sections, not as a substitute for the full evidence pool.
- Add Level 1-4 thinking only after `insight-strategy` or a focused strategy pass.
- Mark provisional strategy when brand truth, proof edge, brand behavior, or competitor difference are thin.
- Keep contradictory evidence visible.
- Keep source IDs or source names attached to major claims.
