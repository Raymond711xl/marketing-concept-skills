# Controller Task Packet And Depth

Use this file to read the controller task packet or, when no packet exists, ask minimal fallback questions. The front-end or controller skill should handle broad user discovery; this collector should not repeat that full intake.

## Preferred Controller Task Packet

Accept this structure when provided:

```markdown
## Collection Task Packet

- Target:
- Research purpose:
- Time range:
- Geography / language:
- Priority platforms:
- Excluded platforms / sources:
- Categories:
- Depth: light / standard / deep / exhaustive
- Existing materials:
- Downstream destination:
- Subagent mode approved: yes / no / ask user
- Notes:
```

If `Subagent mode approved` is `ask user`, recommend a subagent plan when the task qualifies and ask for approval before spawning.

## Intake Questions

Ask at most three fallback questions only if the task packet or user request is insufficient. Prefer defaults when the answer is not mission-critical.

1. **Target**: What should be researched: brand, campaign, event, competitor set, product, industry, or platform behavior?
2. **Depth and categories**: Which categories should be included: visual, video, offline activation, marketing, PR, social, reports, competitor examples? Which depth: light, standard, deep, or exhaustive?
3. **Existing material and constraints**: Does the user already have links, screenshots, exports, keywords, priority platforms, geography, time range, or sources to avoid?

If the user is unsure, propose a default:

```text
I will start with standard collection across visual, video, offline activation, marketing, PR, and social leads, then mark evidence gaps.
```

## Depth Presets

| Depth | Use When | Target Volume |
| --- | --- | --- |
| Light | Quick orientation, early exploration, small brief | 8-15 total evidence items |
| Standard | Normal pitch, competitor scan, campaign input | 20-35 total evidence items |
| Deep | Proposal, annual campaign, category audit | 40-70 total evidence items |
| Exhaustive | User explicitly wants a large source archive | 70+ items if public sources support it |

## Category Defaults

| Category | Light | Standard | Deep |
| --- | ---: | ---: | ---: |
| Visual materials | 2-3 | 5 | 8-12 |
| Video | 1-2 | 3 | 6-10 |
| Offline activation | 1-2 | 3 | 6-10 |
| Marketing | 3 | 5 | 8-12 |
| PR | 3 | 5 | 8-12 |
| Social leads | 3-5 | 5-10 | 10-20 |
| Reports / market context | 1-2 | 3-5 | 6-10 |

## Scope Rules

- If the user names a single campaign, prioritize evidence that maps the campaign across channels.
- If the user names a single brand, collect representative campaigns and repeated material systems from the selected time range.
- If the user names a category or competitor set, balance direct competitors, adjacent references, and category-leading examples.
- If requested categories are too broad for the chosen depth, keep the requested depth and mark lower-priority categories as gaps.
- If the task spans several platforms, prefer platform-first shards and material-category focus inside each platform.

## Existing Material

Use user-provided links, screenshots, exports, or notes as privileged leads, but still label their source type and confidence. User-provided material is not automatically high-confidence unless it is traceable.
