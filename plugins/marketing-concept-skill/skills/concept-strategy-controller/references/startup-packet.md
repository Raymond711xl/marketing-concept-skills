# Project Startup Packet

Use this reference when starting a new Concept Strategy Controller project, receiving a fresh brief, or returning to the beginning because the current direction is unclear.

The startup packet is a lightweight shared entrance for all later stages. It is not a final brief, proposal, report, or strategy.

## Purpose

The packet should:

- Preserve the user's original wording.
- Establish the user workspace, project slug, dossier path, and entry mode before routing.
- Clarify the working target and desired endpoint.
- Diagnose whether the project starts from zero research, messy materials, a structured evidence pool, existing insight, or an existing Idea Platform / Concept.
- Identify Level 4 hard-data needs early, especially brand philosophy, vision, slogan, chronology, founder statements, product proof, service proof, brand behavior, and competitor distinction.
- Make missing inputs visible without blocking unnecessarily.
- Give downstream skills enough context to work without re-asking broad intake questions.

Project recovery is not a new startup. When the user provides `恢复项目：<dossier path>`, follow the recovery protocol in `dossier-contract.md` and preserve the dossier's original startup packet.

## Template

```markdown
## Project Startup Packet

- User original brief:
- Working title:
- Project slug:
- User workspace root:
- Dossier path: dossiers/[project-slug]/backstage-dossier.md
- Entry mode: new project / direct stage / reverse audit
- Brand / product / category:
- Market / geography / language:
- Business problem:
- Communication objective:
- Target audience:
- Current known materials:
- Existing evidence status: none / messy / structured / analyzed
- Evidence preparation mode: default / audit
- Brand hard data status: supplied / public candidates needed / user confirmation needed / unknown
- Brand hard data leads: philosophy / vision / slogan / chronology / founder statement / product proof / service proof / brand behavior / competitor distinction
- Priority platforms or source types:
- Forbidden sources or constraints:
- Desired endpoint: evidence / insight strategy / Idea Platform / Concept
- Current task boundary:
- Recommended route:
- Output language:
- Missing inputs:
- Controller notes:
```

## Filling Rules

- Do not invent missing information.
- Keep empty or uncertain fields visible instead of smoothing them away.
- If a field is missing, explain what later stage it may affect.
- Keep `User original brief` as close to the user's wording as possible.
- Resolve `Dossier path` from the user's current project workspace, never from the installed skill or plugin directory.
- Use Chinese as the default output language unless the user asks otherwise.
- Keep route names and structural labels stable enough for downstream handoff.
- Treat `Existing evidence status: none` as a routing signal, not a reason to stop. When the object, problem, and basic market scope are clear, hand off to `web-evidence-collector` in the same turn and keep non-blocking gaps as assumptions or pending confirmations.

## Starting Point Diagnosis

Use these labels:

| Evidence status | Meaning | Recommended route |
| --- | --- | --- |
| `none` | User has only a question, brand, market, or loose brief | Evidence collection first |
| `messy` | User has links, notes, screenshots, exports, or unstructured research | Evidence summary first |
| `structured` | User has a usable evidence pool, listening report, or research handoff | Insight strategy first |
| `analyzed` | User already has themes, insights, Idea Platform, or Concept | Focused strategy / reverse audit |

## First Response Checklist

The first response should include:

1. `Brief 快照`
2. `起点判断`
3. `推荐路径`
4. `证据准备模式`
5. `如何介入`
6. `当前需要补充的信息`

Include this intervention explanation in the first response:

```text
你可以随时输入阶段指令来单独深入讨论，例如「进入：证据摘要」「进入：策略洞察」「进入：Idea Platform」「进入：Concept」「查看：资料池」。总控会暂停推进，把用户原话、当前判断和完整资料池一起带入该环节，不会只转发压缩摘要。已有项目可以用「恢复项目：<dossier path>」继续。
```

Ask at most three questions. If the missing information is not blocking, state a default and proceed.

When brand hard data is missing, do not ask the user to define abstract brand truth. Ask whether official materials exist, such as brand book, website, slogan, chronology, founder statement, campaign archive, product proof, service proof, or competitor list. If not supplied, mark them as public collection leads and proceed.
