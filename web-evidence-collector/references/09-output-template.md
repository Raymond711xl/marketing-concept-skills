# Output Template

Use the default frontstage handoff unless the user/controller asks for the full backend dossier, subagents were used and need audit, or downstream processing needs the complete file.

## Default Frontstage Handoff

Use this compact Markdown structure for normal user/controller display.

```markdown
# Web Evidence Collection: [Topic]

## 1. Collection Readiness

- Status: ready / partial / thin / blocked
- Target:
- Scope:
- Collection date:
- Requested categories:
- Requested depth:
- Evidence count:
- Source mix:
- Restricted / user-needed items:
- Linked campaign chains:
- Subagent mode: recommended / approved / declined / not needed / unavailable
- Downstream next step: evidence-summary-analysis

## 2. Evidence Brief Box

- Evidence readiness:
- Source coverage summary:
- Most reliable source groups:
- Brand hard-data candidates:
- Major restrictions:
- Missing evidence:
- Evidence pool status: included below / attached in backend dossier / unavailable

## 3. Source Coverage

| Area | Collected count | Source spread | Strongest source level | Confidence | Notes |
| --- | ---: | --- | --- | --- | --- |
| Visual | | | | | |
| Video | | | | | |
| Offline activation | | | | | |
| Marketing | | | | | |
| PR | | | | | |
| Social | | | | | |
| Reports / context | | | | | |

## 4. Brand Hard Data Track

| Hard data type | Candidate evidence | Source / URL | Confidence | Needs user confirmation |
| --- | --- | --- | --- | --- |
| Brand philosophy / vision | | | | |
| Slogan / brand claim | | | | |
| Brand chronology | | | | |
| Founder / leadership statement | | | | |
| Product proof | | | | |
| Service / experience proof | | | | |
| Brand behavior | | | | |
| Competitor distinction | | | | |

## 5. Key Campaign / Competitor Linkage

| Campaign / message | Linkage status | Related evidence IDs | Channels represented | Missing channels |
| --- | --- | --- | --- | --- |

## 6. Gaps And Restrictions

| Gap / restriction | Why it matters | Suggested next action |
| --- | --- | --- |

## 7. Evidence Pool Handoff

- Evidence pool: included below / stored in backend dossier / not enough evidence
- Core schema compatibility: evidence-summary-analysis
- Do not skip next skill: evidence-summary-analysis should normalize and summarize this pool before insight-strategy
- Recommended next skill: evidence-summary-analysis
```

## Backend Dossier

Use this full structure when the user asks for the full dossier, when collection needs auditability, when subagents were used, or when writing a complete backend handoff.

```markdown
# Web Evidence Collection Backend Dossier: [Topic]

## 1. Collection Brief

- Research topic:
- Target brand / event / competitor set:
- Time range:
- Geography / platform scope:
- Requested categories:
- Requested depth:
- Collection date:
- Downstream destination: evidence-summary-analysis
- Evidence preparation mode: default / audit
- Known inputs used:
- Controller task packet used: yes / no
- Subagent mode: recommended / approved / declined / not needed / unavailable

## 2. Depth And Query Plan

| Category | Target volume | Query / source strategy | Notes |
| --- | ---: | --- | --- |
| Visual | | | |
| Video | | | |
| Offline activation | | | |
| Marketing | | | |
| PR | | | |
| Social | | | |
| Reports / context | | | |

## 3. Subagent Collection Plan

| Shard ID | Split type | Platform / source scope | Material focus | Target count | Output prefix | Status |
| --- | --- | --- | --- | ---: | --- | --- |
| OFFICIAL | platform | official / brand-owned | landing page, press release, visual | | OFF | proposed / running / complete |
| NEWS | platform | news / industry media / PR | PR, campaign coverage | | NEW | proposed / running / complete |
| VIDEO | platform | YouTube / Bilibili / Douyin / TikTok / video pages | video | | VID | proposed / running / complete |
| SOCIAL | platform | Xiaohongshu / Weibo / Zhihu / Bilibili / WeChat / forums | social leads, UGC | | SOC | proposed / running / complete |
| VISUAL | mixed | image search / creative archives / campaign pages | posters, KV, landing pages, packaging | | VIS | proposed / running / complete |
| REPORT | platform | PDFs / white papers / report summaries | reports, market context | | RPT | proposed / running / complete |

## 4. Evidence Shards

### Shard [ID]: [Scope]

- Platforms:
- Categories:
- Target count:
- Actual count:
- Search date:
- Search log:
- Gaps / restrictions:
- Evidence IDs produced:

## 5. Evidence Brief Box

- Evidence readiness: ready / partial / weak
- Source coverage summary:
- Most reliable source groups:
- Brand hard-data candidates:
- Major restrictions:
- Missing evidence:
- Evidence pool status:

## 6. Source Coverage

| Area | Target count | Collected count | Source spread | Strongest source level | Confidence | Notes |
| --- | ---: | ---: | --- | --- | --- | --- |

## 7. Brand Hard Data Track

| Hard data type | Candidate evidence | Source / URL | Source type | Confidence | Needs user confirmation |
| --- | --- | --- | --- | --- | --- |
| Brand philosophy / vision | | | | | |
| Slogan / brand claim | | | | | |
| Brand chronology | | | | | |
| Founder / leadership statement | | | | | |
| Product proof | | | | | |
| Service / experience proof | | | | | |
| Brand behavior | | | | | |
| Competitor distinction | | | | | |

## 8. Campaign Linkage Map

| Campaign / message | Linkage status | Related evidence IDs | Channels represented | Missing channels | Notes |
| --- | --- | --- | --- | --- | --- |

## 9. Collection Statistics

| Metric | Value | Evidence basis |
| --- | ---: | --- |
| Total evidence items | | |
| Source mix | | |
| Brand-owned items | | |
| Third-party media items | | |
| Social lead items | | |
| Visual items | | |
| Video items | | |
| Offline items | | |
| Marketing items | | |
| PR items | | |
| Linked campaign chains | | |
| Standalone items | | |
| Restricted / user-needed items | | |

## 10. Campaign / Message Repetition Snapshot

| Campaign / message | Evidence count | Channels | Brands | Repetition pattern | Completeness |
| --- | ---: | --- | --- | --- | --- |

## 11. Skew And Completeness Check

| Check | Status | Evidence | Risk for downstream analysis | Suggested next collection |
| --- | --- | --- | --- | --- |
| Category balance | | | | |
| Source diversity | | | | |
| Platform diversity | | | | |
| Brand-owned vs third-party split | | | | |
| Social access limits | | | | |
| Visual evidence coverage | | | | |
| Campaign linkage completeness | | | | |

## 12. Gaps And Restrictions

| Gap / restriction | Why it matters | Suggested next action |
| --- | --- | --- |

## 13. Evidence Pool

### Evidence 1

- Evidence ID:
- Source type:
- Source name:
- Date:
- URL or citation:
- Raw quote:
- Observation:
- Summary:
- Topic tag:
- Audience:
- Confidence:
- Source level:
- Category:
- Publisher / platform:
- Author / account:
- Access date:
- Brand / event:
- Campaign / message:
- Channel:
- Material type:
- Visual material:
- Screenshot status:
- Key fact:
- Evidence value:
- Brand hard data type:
- Needs user confirmation:
- Related evidence:
- Linkage status:
- Metric / count:
- Limitation / restriction:
```

## Output Rule

- The frontstage handoff is for reading and controller display.
- The backend dossier is for audit, continuation, and downstream skill processing.
- The Evidence Pool is the core result and must be preserved even when the frontstage layer is compact.
- The normal next skill is `evidence-summary-analysis`; do not jump directly to `insight-strategy` unless the user explicitly overrides the workflow.
