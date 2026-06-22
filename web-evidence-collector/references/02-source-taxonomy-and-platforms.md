# Source Taxonomy And Platforms

Use source levels to preserve reliability and access constraints.

## Source Levels

| Level | Source | Collection Handling |
| --- | --- | --- |
| L1 | Official sites, government pages, public company filings, brand press releases, official campaign pages | Use as strong factual evidence. Summarize directly, keep links, use short quotes only. |
| L2 | News articles, public reporting, industry media, trade publications | Extract facts, viewpoints, dates, publication context, and media frame. |
| L3 | Public PDFs, white papers, report excerpts, annual reports, decks the user has rights to provide | Summarize key points and cite file/page when available. Do not copy large excerpts. |
| L4 | Search snippets, news aggregators, directory pages, platform search results | Treat as leads. Try to trace to L1-L3 or accessible L5-L6 pages before using as fact. |
| L5 | Ecommerce reviews, App Store reviews, public forums, public comment pages | Use small representative quotes. Avoid bulk copying and preserve sampling limitations. |
| L6 | Xiaohongshu, Weibo, Douyin, Zhihu, Bilibili, TikTok, Instagram, YouTube comments, WeChat public account pages, and similar dynamic or login-prone platforms | Use public pages, official APIs, platform search, or user exports when available. If access is limited, preserve one short key phrase, link, platform, and restriction note. |
| L7 | Paywalled reports, member-only pages, private communities, logged-in content, private groups | Do not auto-collect. Use only user-authorized screenshots, exports, or excerpts. |
| L8 | Explicitly blocked, technically restricted, or prohibited content | Do not collect. Keep only link metadata and reason if useful. |

## Source Type Labels

Use one of:

```text
brand-owned, official, news, report, competitor, social, review, forum, video platform, ecommerce, app store, event feedback, survey, interview, search result, user provided, other
```

## Platform Coverage

Prefer official or authorized access paths:

- Search engines: public web search, news search, image search, video search.
- Brand-owned: official websites, press rooms, campaign pages, investor pages, brand social accounts.
- Video: YouTube, Bilibili, Douyin public pages, Vimeo, official embedded videos, ad archives where available.
- Social: Xiaohongshu, Weibo, Douyin, Zhihu, Bilibili, WeChat public account articles, TikTok, Instagram, X, LinkedIn, Facebook, Reddit when public.
- Campaign and creative archives: Ads of the World, Campaign Asia, The Drum, WARC summaries where public, SocialBeta, Digitaling, Meihua, award pages where public.
- Reports: government reports, annual reports, industry white papers, public PDF summaries.
- Reviews: ecommerce pages, App Store, Google Play, public forum threads.

## API-First Rule

When official APIs, platform exports, or user-authorized connectors are available, prefer them over browser scraping. Record:

- API or export name
- Query or filter used
- Collection date
- Known coverage limits

Do not claim API coverage if no API is actually available in the environment. If an API is unavailable, use public pages, search snippets as leads, or ask the user for platform exports/screenshots.

## Reliability Notes

- Separate brand-owned claims from third-party reporting and audience evidence.
- Treat social evidence as signal, not representative truth, unless the dataset and sampling method are known.
- Treat counts shown on dynamic platforms as volatile; record the access date.
