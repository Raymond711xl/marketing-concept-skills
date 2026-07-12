# Backstage Dossier Contract

Use this reference whenever the controller needs to preserve project memory, hand work to a downstream skill, show the user the material base, resume a paused stage, or return to an earlier stage.

The backstage dossier is the complete structured memory of the project. It may be long. The frontstage output should remain short. The dossier is also the source of truth for `继续`, focused-stage return, and cross-session project recovery.

By default, the controller should export or maintain a Markdown dossier for real projects, while showing only the relevant portion in the conversation. Exporting a dossier means writing structured project memory to a file; it does not mean printing the whole dossier into chat.

## Contents

- Two Output Layers
- Dossier Template
- Dossier Export Rules
- Project Recovery Protocol
- Downstream Handoff Packet
- Update Rules

## Two Output Layers

### Frontstage Output

Use this for user-facing progress:

- Current conclusion
- Content strips for the current stage
- Evidence brief box when evidence preparation finishes
- Concept card and Message House when Concept finishes
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
- Controller session state
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
- Message House records
- Downstream handoff log
- Open questions and caveats

Compression should reduce reading burden, not remove evidence, uncertainty, source trails, or strategic caveats.

## Dossier Template

```markdown
# Backstage Dossier: [Working Title]

## 0. User Original Brief

## 1. Project Startup Packet

## 2. Controller Session State

- Project slug:
- User workspace root:
- Dossier path:
- Current route:
- Entry mode: new project / direct stage / reverse audit / restored
- Current stage:
- Stage status: not_started / active / waiting_user / handoff_only / completed / provisional
- Stage owner: controller / web-evidence-collector / evidence-summary-analysis / insight-strategy
- Active downstream skill:
- Completed stages:
- Last valid artifact:
- Confirmed decisions:
- Reliable judgments:
- Provisional judgments:
- Pending confirmations:
- Open questions:
- Return stage:
- Next action:
- Last updated:

## 3. Controller Interpretation

- Current route:
- Current stage:
- Stage goal:
- Assumptions:
- Constraints:
- Open questions:

## 4. Evidence Base

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

## 5. Evidence Summary

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

## 6. Insight Strategy

### Level 1 - Fact Layer

### Level 2 - Motive Inference

### Level 3 - Cultural Judgment

### Level 4 - Strategic Decision

## 7. Idea Platform Records

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

## 8. Concept Records

### Concept 1

- Concept name:
- One-line concept:
- Human / cultural tension:
- Brand belief:
- Audience role:
- Proof mechanism:
- Expression territory:
- Must stay consistent:
- Must avoid:
- Risk:
- Confidence:
- Open questions:

#### Message House

- Roof:
- Pillars:
  - Pillar 1:
    - Audience meaning:
    - Support:
  - Pillar 2:
    - Audience meaning:
    - Support:
- Foundation:
- Proof gaps:

## 9. Downstream Handoff Log

| Date / turn | Stage | Canonical skill | Load status | Task boundary | Return status | Artifact |
| --- | --- | --- | --- | --- | --- | --- |

## 10. Decision Log

| Date / turn | Decision | Reason | Impact |
| --- | --- | --- | --- |

## 11. Next Options

- Continue:
- Deepen:
- Return:
- Stop:
```

## Dossier Export Rules

- Resolve the base directory from the user's active project workspace, not from the location of this installed skill.
- Default project directory: `<user-workspace>/dossiers/[project-slug]/`.
- Default dossier file: `<user-workspace>/dossiers/[project-slug]/backstage-dossier.md`.
- If no project slug exists, create one from the working title.
- Never write project dossiers into a plugin installation directory, plugin source folder, Codex/Claude plugin cache, skill cache, or marketplace cache.
- If the process is running from an installation/cache directory, use the platform-provided user workspace. If no user workspace can be resolved, do not write a file.
- Do not print the full dossier in chat unless the user asks to view it.
- Update only changed sections when possible.
- Do not overwrite a materially different previous dossier without preserving a dated copy, such as `backstage-dossier-YYYYMMDD-HHMM.md`.
- If filesystem export is unavailable or no user workspace can be resolved, maintain the same dossier schema as structured conversation memory. State `Dossier storage: conversation_memory` and offer a copyable Markdown block only when requested.

## Project Recovery Protocol

Use this protocol for `恢复项目：<dossier path>`:

1. Read the specified dossier as the project source of truth. Do not create a fresh startup packet.
2. Recover `User Original Brief` first, then `Controller Session State`, `Decision Log`, the latest valid stage artifact, and `Next Options`.
3. Separate recovered information into:
   - `confirmed`: explicitly approved by the user or recorded as a decision.
   - `reliable`: supported by current evidence and not superseded.
   - `provisional`: useful but dependent on thin evidence or unconfirmed brand hard data.
   - `open`: unresolved questions, proof gaps, and pending confirmations.
4. Verify referenced files or artifacts when file access exists. Mark missing references `unavailable`; do not reconstruct them as historical facts.
5. Restore `Current stage`, `Stage status`, `Return stage`, and `Next action`.
6. Present a compact recovery brief with current stage, reliable judgments, pending confirmations, open questions, next action, and dossier path.
7. Append a recovery event to `Decision Log` only after a writable user-workspace dossier is confirmed.

For older dossiers without `Controller Session State`, infer state from the newest stage record, Decision Log, and Next Options. Label every inferred field `inferred` and ask only about ambiguities that would materially change the next action.

## Downstream Handoff Packet

Whenever handing work to a specialist skill, send this packet:

```markdown
## Downstream Handoff Packet

### Handoff Control

- Target stage:
- Canonical downstream skill:
- Downstream skill status: loaded / unavailable / not loaded
- Stage status: active / handoff_only
- Task boundary:
- Return command: 返回总控 / 继续

### User Original Brief

Preserve the user's wording, links, constraints, preferences, doubts, and exclusions. Do not replace this section with a summary.

### Controller Judgment

- Current route:
- Current stage:
- Task goal:
- What to do:
- What not to do:
- Desired output depth:

### Relevant Backstage Dossier

- Dossier path:
- Relevant confirmed decisions:
- Relevant reliable judgments:
- Relevant provisional judgments:
- Required source artifacts or excerpts:
- Open questions and pending confirmations:

### Specific Task

- Required output contract:
- Completion criteria:
- Return artifacts:
```

Never send only a short summary when original user input or complete evidence exists. A handoff is complete only when the canonical downstream skill was loaded and its return artifacts passed the output-contract check. Otherwise keep `Stage status: handoff_only` and do not generate specialist conclusions inside the controller.

Use `loaded` only after the platform has actually opened the canonical skill instructions for the current task. A skill name mentioned in prose, inferred from memory, or copied into the packet is still `not loaded`.

## Update Rules

- Add new evidence to the evidence base, not to strategy sections.
- Add cleaned and summarized material to evidence summary, not directly to insights.
- Add brand hard data candidates to `Brand Hard Data Track` and mark whether they are user-supplied, publicly collected, or still need confirmation.
- Add evidence-preparation content strips and the evidence brief box to frontstage sections, not as a substitute for the full evidence pool.
- Add Level 1-4 thinking only after `insight-strategy` or a focused strategy pass.
- Mark provisional strategy when brand truth, proof edge, brand behavior, or competitor difference are thin.
- Add `Roof`, `Pillars`, `Foundation`, and `Proof gaps` to every completed or provisional Concept record and retain them in the frontstage Concept summary.
- Do not mark a Concept frontstage result complete unless it explicitly displays Concept name, One-line concept, Audience role, Expression territory, Risk, Confidence, Roof, Pillars, Foundation, and Proof gaps.
- Update `Controller Session State` after every route change, user confirmation, downstream return, rollback, and recovery.
- Record every downstream load attempt and result in `Downstream Handoff Log`.
- Keep contradictory evidence visible.
- Keep source IDs or source names attached to major claims.
