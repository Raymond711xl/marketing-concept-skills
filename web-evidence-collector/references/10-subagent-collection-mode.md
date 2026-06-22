# Subagent Collection Mode

Use this file when collection is broad enough that platform-first subagents would improve evidence cleanliness, vertical depth, or cross-checking.

## Principle

Prefer platform-first splitting. Each subagent searches deeply within one platform or source family. Material attributes are handled inside the platform shard.

Example:

- A video-platform subagent collects video ads, short videos, visible metrics, captions, and related landing pages from YouTube, Bilibili, Douyin, or TikTok.
- A social-platform subagent collects Xiaohongshu, Weibo, Zhihu, Bilibili, WeChat public account, forum, or search-lead evidence.
- A PR/news subagent collects press releases, media coverage, interviews, controversy, awards, and reputation events.

## When To Recommend

Recommend subagent mode when any condition is true:

- More than three platforms are in scope.
- More than three material categories are requested.
- Depth is deep or exhaustive.
- Target evidence volume is more than 25 items.
- The task includes multiple campaigns, competitors, sub-themes, or product lines.
- The task includes several source forms at once: social, video, visual materials, news, reports, and official pages.

Do not force subagent mode for small tasks. If light collection is enough, collect sequentially.

## Consent Rule

Before starting subagents, ask for explicit approval from the user or controller:

```text
This collection spans multiple platforms/material types. I recommend subagent collection mode to keep platform evidence cleaner and more vertical. It will use more tokens. Should I proceed with subagents?
```

If approval is not given, collect sequentially and keep the shard plan as an internal organization method.

## Default Platform Shards

| Shard | Scope | Material Focus | Prefix |
| --- | --- | --- | --- |
| Official / brand-owned | Official site, campaign page, press room, owned accounts | landing page, official visuals, launch facts, owned claims | OFF |
| News / PR / industry media | News, trade media, PR wires, interviews, awards, controversy | PR, reputation, media framing | NEW |
| Video platforms | YouTube, Bilibili, Douyin, TikTok, Vimeo, embedded official videos | TVC, campaign film, short video, visible metrics | VID |
| Social platforms | Xiaohongshu, Weibo, Zhihu, Bilibili community, WeChat public account, forums | social leads, public reactions, UGC traces | SOC |
| Visual / campaign archives | Image search, creative archives, case pages, design platforms | poster, KV, landing page, packaging, event visual | VIS |
| Reports / PDFs / market context | Public reports, white papers, filings, public PDFs | report facts, category context, public numbers | RPT |

Use hybrid splitting when a platform shard is too large. Example: split `SOC-XHS`, `SOC-WEIBO`, `SOC-BILI`, or split `VID-YOUTUBE`, `VID-BILI`.

## Subagent Task Packet

Give each subagent a self-contained task:

```markdown
Use $web-evidence-collector to collect one evidence shard.

## Shard Task
- Shard ID:
- Target brand / campaign / event:
- Platform / source scope:
- Material focus:
- Time range:
- Geography / language:
- Target count:
- Required source levels:
- Access boundaries:
- Output prefix:

## Output Required
Return only:
1. Shard Brief
2. Search Log
3. Evidence Pool Shard
4. Gaps And Restrictions

Do not make strategy conclusions. Keep quotes short. Preserve source trails.
```

## Evidence Shard Format

```markdown
# Evidence Shard: [Shard Name]

## Shard Brief

- Shard ID:
- Scope:
- Platforms:
- Categories:
- Target count:
- Actual count:
- Search date:

## Search Log

| Query | Platform/source | Result |
| --- | --- | --- |

## Evidence Pool Shard

### Evidence [PREFIX]-001
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
- Related evidence:
- Linkage status:
- Metric / count:
- Limitation / restriction:

## Gaps And Restrictions

- 
```

## Merge Rules

After subagents return:

1. De-duplicate by URL, citation, asset title, and campaign/material identity.
2. Preserve separate evidence items when one campaign appears in different channels or material forms.
3. Normalize IDs and keep shard prefixes.
4. Merge campaign/message labels conservatively.
5. Mark related evidence links as `confirmed`, `likely`, or `tentative`.
6. Lower confidence for search-only or access-limited evidence.
7. Add a source skew and platform skew note if one shard dominates.

## Cross-Checking

Use subagents for cross-validation:

- Official claim -> verify through news/PR or campaign page.
- News claim -> trace to official page or independent second source.
- Social lead -> treat as signal unless supported by source spread.
- Visual asset -> link to official/case/archive source where possible.
- Video metric -> record access date because counts are volatile.

The final merged output must still be one unified Markdown handoff using `references/09-output-template.md`.
