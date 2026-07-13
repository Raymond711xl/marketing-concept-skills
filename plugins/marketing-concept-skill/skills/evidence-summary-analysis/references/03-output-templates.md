# Output Templates

Use these templates for handoff, quick output, Strategy Readiness Pack, and
collector task fallback. Use `05-research-lens-and-delivery-modes.md` for the
selected Research Lens module and Delivery Mode wrapper.

## Selection Header

```markdown
## Research Configuration

- Primary Research Lens:
- Supporting Research Lens:
- Delivery Mode: Frontstage Brief / Full Evidence Dossier / Client-facing Research Report
- Lens adaptation note:
```

## Evidence Coverage Check

```markdown
## Evidence Coverage Check

| Area | Status | Notes |
| --- | --- | --- |
| Source diversity | strong / medium / weak | |
| Date traceability | strong / medium / weak | |
| URL/citation traceability | strong / medium / weak | |
| Brand-owned vs third-party separation | clear / mixed / weak | |
| Social/platform restrictions | none / some / significant | |
| Visual evidence coverage | strong / medium / weak | |
| Brand hard-data coverage | strong / medium / weak | |
| Contradictory evidence preserved | yes / no / not found | |
```

## Frontstage Content Strips

```markdown
## Frontstage Content Strips

- 来源覆盖内容条:
- 强证据模式内容条:
- 品牌硬信息内容条:
- 证据缺口内容条:
- 进入策略判断内容条:
```

Each strip must be short, evidence-bound, and traceable to Evidence IDs.

## Category Summary Tables

```markdown
## Category Summaries

### Visual Materials

| Item | Evidence ID | Material type | Source | Observation | Screenshot status | Pattern | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |

### Video

| Item | Evidence ID | Source | Message | Observation | Audience | Pattern | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |

### Offline Activation

| Item | Evidence ID | Source | Mechanism | Observation | Audience | Pattern | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |

### Marketing

| Item | Evidence ID | Source | Mechanism | Channel | Pattern | Confidence |
| --- | --- | --- | --- | --- | --- | --- |

### PR

| Item | Evidence ID | Source | News angle | Response/risk | Pattern | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
```

## Evidence Pattern Inventory

```markdown
## Evidence Pattern Inventory

### Pattern 1: [Name]

- Evidence support: [Evidence IDs]
- What the evidence shows:
- Source / channel / material structure:
- Contradictions or caveats:
- Confidence:
```

Do not explain motives, human truths, cultural tensions, or strategy.

## Strategy Readiness Pack

Every candidate must point back to evidence. Use `missing` when the evidence is
absent.

Status values:

```text
confirmed / reported / inferred / missing
```

Template:

```markdown
## Strategy Readiness Pack

| Item | Candidate | Status | Evidence ID | Confidence | Notes / user confirmation needed |
| --- | --- | --- | --- | --- | --- |
| Brand truth candidate | | confirmed / reported / inferred / missing | | high / medium / low / speculative | |
| Proof edge | | confirmed / reported / inferred / missing | | high / medium / low / speculative | |
| Brand behavior | | confirmed / reported / inferred / missing | | high / medium / low / speculative | |
| Competitor distinction | | confirmed / reported / inferred / missing | | high / medium / low / speculative | |

Readiness status: ready / ready with caveats / needs more evidence
```

Status guidance:

- `confirmed`: directly supported by official, traceable, or repeated strong
  evidence.
- `reported`: stated by a news, report, competitor, social, or third-party source.
- `inferred`: low-level source/material inference only; mark the evidence basis
  and avoid strategic interpretation.
- `missing`: no usable evidence; include a collector task or user confirmation
  request.

## Evidence Gaps

```markdown
## Evidence Gaps

| Gap | Why it matters for downstream work | Suggested collector task |
| --- | --- | --- |
```

## Full Handoff Template

```markdown
# Evidence Summary Analysis: [Topic]

## 1. Scope

- Target:
- Time range:
- Geography/platform:
- Requested categories:
- Requested volume:
- Primary Research Lens:
- Supporting Research Lens:
- Delivery Mode:
- Evidence count:
- Main source types:

## 2. Frontstage Content Strips

- 来源覆盖内容条:
- 强证据模式内容条:
- 品牌硬信息内容条:
- 证据缺口内容条:
- 进入策略判断内容条:

## 3. Evidence Coverage Check

[Use coverage table]

## 4. Category Summaries

[Use category tables]

## 5. Research Lens Summary

[Use the selected module from references/05-research-lens-and-delivery-modes.md]

## 6. Evidence Pattern Inventory

[Use pattern inventory]

## 7. Strategy Readiness Pack

[Use readiness pack table]

## 8. Evidence Gaps

[Use evidence gaps table]

## 9. Cleaned Evidence Pool

[Use schema from references/01-evidence-pool-schema.md]
```

## Quick Output Template

Quick output must still include a cleaned pool or clear file entry.

```markdown
## Quick Evidence Summary

- Primary Research Lens:
- Delivery Mode: Frontstage Brief

### Frontstage Content Strips

- 来源覆盖内容条:
- 强证据模式内容条:
- 品牌硬信息内容条:
- 证据缺口内容条:
- 进入策略判断内容条:

### Top Evidence Patterns

- Pattern:
  - Evidence IDs:
  - Confidence:

### Selected Lens Findings

- Finding:
  - Evidence IDs:
  - Contradiction / limitation:
  - Confidence:

### Strategy Readiness Pack

[Use readiness pack table]

### Evidence Gaps

-

### Cleaned Evidence Pool

[Include cleaned evidence items here, or provide a clear file path / file-entry label that contains the cleaned Evidence Pool with Evidence ID, Observation, traceability fields, and Confidence.]
```

## Collector Task Fallback

Use this when fresh evidence is missing. Do not perform research inside this
skill.

```markdown
## Collector Task

- Target:
- Research Lens:
- Missing evidence:
- Missing lens evidence:
- Priority categories:
- Source priorities:
- Required fields:
  - Evidence ID
  - Source type
  - Source name
  - Date
  - URL or citation
  - Raw quote
  - Observation
  - Summary
  - Topic tag
  - Audience
  - Confidence
- Notes:
```
