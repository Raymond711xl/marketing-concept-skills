# Output Template

Use the default frontstage handoff unless the user/controller asks for the full backend dossier, subagents were used and need audit, or downstream processing needs the complete file.

## Default Frontstage Handoff

Use this compact Markdown structure for normal user/controller display.

```markdown
# Web Evidence Collection: [Topic]

## 1. Collection Readiness

- Status: ready / partial / thin / blocked
- Collection status: collected / partially collected / not collected - capability unavailable
- Available capabilities:
- Capabilities used:
- Unavailable or restricted capabilities:
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

### Capability Downgrade: Source Plan

Include this subsection only when collection is partial or not collected because capabilities are unavailable.

| Planned source / platform | Planned query or material | Execution status | User material needed |
| --- | --- | --- | --- |
| | | not executed / partially executed | |

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

Include one row per actual candidate. Put absent hard-data types in `Gaps And Restrictions`.

| Hard data type | Candidate evidence | Source Evidence ID(s) | Source / URL | Candidate status | Confidence | Needs user confirmation |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | user-provided official / public official candidate / independently corroborated / conflicting / incomplete | | yes / no / unknown |

## 5. Key Campaign / Competitor Linkage

| Campaign / message | Linkage status | Related evidence IDs | Channels represented | Missing channels |
| --- | --- | --- | --- | --- |

## 6. Gaps And Restrictions

| Gap / restriction | Why it matters | Suggested next action |
| --- | --- | --- |

## 7. Evidence Pool Handoff

- Evidence pool: included below / stored in backend dossier / not created - capability unavailable
- Evidence Pool schema: Evidence Pool v1
- Handoff preservation: preserve Evidence ID and all core field names and values; keep Observation even when Raw quote is unavailable
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
- Collection status: collected / partially collected / not collected - capability unavailable
- Available capabilities:
- Capabilities used:
- Unavailable or restricted capabilities:

## 2. Depth And Query Plan

| Category | Target volume | Query / source strategy | Execution status | Notes |
| --- | ---: | --- | --- | --- |
| Visual | | | executed / partial / not executed | |
| Video | | | executed / partial / not executed | |
| Offline activation | | | executed / partial / not executed | |
| Marketing | | | executed / partial / not executed | |
| PR | | | executed / partial / not executed | |
| Social | | | executed / partial / not executed | |
| Reports / context | | | executed / partial / not executed | |

### Capability Downgrade: User Materials Needed

Include only when collection is partial or not collected.

| Missing source/platform | Why live collection was not possible | Link, screenshot, export, or file requested |
| --- | --- | --- |
| | | |

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

- Platforms / source range:
- Categories:
- Target count:
- Actual count:
- Search date:
- Search log:
- Gaps / restrictions:
- Evidence IDs produced:
- Evidence IDs merged as duplicates:

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

Include one row per actual candidate. Every source Evidence ID must exist in section 13.

| Hard data type | Candidate evidence | Source Evidence ID(s) | Source / URL | Source type | Candidate status | Confidence | Needs user confirmation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | user-provided official / public official candidate / independently corroborated / conflicting / incomplete | | yes / no / unknown |

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

Handoff preservation: Evidence Pool v1. Preserve Evidence ID and all core field names and values. Keep Observation even when Raw quote is unavailable.

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
- Brand hard data status:
- Related evidence:
- Linkage status:
- Metric / count:
- Limitation / restriction:
- Shard ID:
- Shard source scope:
- Merged from evidence IDs:
```

## Output Rule

- The frontstage handoff is for reading and controller display.
- The backend dossier is for audit, continuation, and downstream skill processing.
- The Evidence Pool is the core result and must be preserved even when the frontstage layer is compact.
- Core Evidence Pool fields must never be omitted, renamed, or left blank in an actual evidence item. Use explicit missing values from `references/04-evidence-pool-contract.md`.
- A visual evidence item with no source wording must use `Raw quote: not available` and retain a concrete `Observation`.
- Frontstage compression may hide or link to the backend dossier; it must not truncate, summarize over, or discard the backend Evidence Pool.
- When no real evidence was collected, do not print an empty `### Evidence 1` block. Instead write `Evidence items: 0` and `Status: not collected - capability unavailable`, followed by the source plan, gaps, and user materials needed.
- The next skill is `evidence-summary-analysis`. This collector ends at the Evidence Pool handoff and does not route directly to `insight-strategy`.
