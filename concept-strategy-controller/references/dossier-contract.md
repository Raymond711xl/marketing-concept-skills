# Backstage Dossier Contract

Use this reference whenever the controller needs to preserve project memory, hand work to a downstream skill, show the user the material base, resume a paused stage, or return to an earlier stage.

The backstage dossier is the complete structured memory of the project. It may be long. The frontstage output should remain short.

The dossier is not automatically a file. By default, the controller maintains it as structured project memory and shows only the relevant portion in the conversation. When the user asks to view it, show the requested section in chat. When the user asks to export it, create a Markdown file such as `backstage-dossier-[project-name].md`.

## Two Output Layers

### Frontstage Output

Use this for user-facing progress:

- Current conclusion
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
- Category summaries
- Evidence pattern inventory
- Insight map
- Strategy candidates
- Big Idea records
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

### Source Coverage

### Evidence Pool

### Gaps And Restrictions

## 4. Evidence Summary

### Category Summaries

### Evidence Pattern Inventory

### Cleaned Evidence Pool

## 5. Insight Strategy

### Level 1 - Fact Layer

### Level 2 - Motive Inference

### Level 3 - Cultural Judgment

### Level 4 - Strategic Decision

## 6. Big Idea Records

### Big Idea 1

- Statement:
- Cultural tension answered:
- Brand truth used:
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
- Add Level 1-4 thinking only after `insight-strategy` or a focused strategy pass.
- Mark provisional strategy when brand facts, product proof, brand history, or competitor difference are thin.
- Keep contradictory evidence visible.
- Keep source IDs or source names attached to major claims.
