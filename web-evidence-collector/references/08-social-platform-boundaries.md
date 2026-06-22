# Social Platform Boundaries

Use this file for Xiaohongshu, Weibo, Douyin, Zhihu, Bilibili, WeChat public account, Tieba, TikTok, Instagram, YouTube, X, Reddit, and other dynamic platforms.

## Operating Rules

- Use official APIs, authorized exports, platform search, public pages, or user-provided screenshots/exports when available.
- Do not bypass login, anti-bot systems, CAPTCHAs, paywalls, private groups, or technical access restrictions.
- Do not copy full posts, full threads, full comment sections, or large batches of user content.
- Use short key phrases and links for restricted or dynamic content.
- Mark platform evidence as signal, not representative truth, unless sampling is known.

## Platform Handling

| Platform Type | Preferred Path | Fallback |
| --- | --- | --- |
| Search engines | Public search result leads | Trace to original source where possible |
| Xiaohongshu | Official/API/export if available, public search leads, user screenshots | One short phrase + link + user-needed note |
| Weibo | Public posts, official account pages, API/export if available | Short key phrase + link |
| Douyin / TikTok | Public video page or official account, API/export if available | Link + visible metadata + user-needed note |
| Zhihu | Public question/article pages | Short quote only; note login limits |
| Bilibili | Public video pages, comments if publicly visible | Link + visible title/metrics/date |
| WeChat public account | Public article URLs, search leads, user exports | Short quote only; note if access unstable |
| Tieba / forums | Public thread pages | Representative short quote, no bulk copying |
| Instagram / X / Facebook / LinkedIn | Public posts and official APIs if available | Link + short visible phrase |

## Social Lead Item

Use this structure:

```markdown
### Evidence N
- Evidence ID:
- Source type: social
- Source name:
- Source level: L6
- Date:
- URL or citation:
- Raw quote: "[one short key phrase only]"
- Observation:
- Summary:
- Topic tag:
- Audience:
- Confidence:
- Publisher / platform:
- Author / account:
- Access date:
- Brand / event:
- Campaign / message:
- Channel:
- Material type: social post / comment / video page / hashtag / search result
- Screenshot status: captured / public image linked / not accessible / user needed
- Metric / count:
- Limitation / restriction:
```

## User-Needed Note

Use this wording when a platform requires manual verification:

```text
Full social content requires platform access or user-provided export. This evidence preserves a short visible phrase, link, platform, and access limitation for manual verification.
```
