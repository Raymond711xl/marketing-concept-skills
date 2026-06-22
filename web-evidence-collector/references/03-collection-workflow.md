# Collection Workflow

Use this workflow for each collection request.

## 1. Scope

Create a brief working scope:

- Controller task packet, if provided
- Target brand, campaign, event, product, market, or competitor set
- Time range and geography
- Requested categories and depth
- Known links, screenshots, exports, or seed keywords
- Downstream destination: evidence-summary-analysis, insight-strategy, or user review

Do not repeat broad front-end questioning when a controller skill has already supplied the task packet. Ask only for missing information that blocks collection.

## 2. Query Plan

Create a compact query plan before collecting. Include:

- Official queries: brand + campaign/event/product + official / press release / landing page
- News queries: brand/campaign + news / launch / PR / campaign / controversy / activation
- Visual queries: brand/campaign + poster / KV / landing page / packaging / visual / screenshot
- Video queries: brand/campaign + video / TVC / ad / film / short video / YouTube / Bilibili / Douyin
- Offline queries: brand/campaign + pop-up / event / exhibition / roadshow / activation / installation
- Marketing queries: brand/campaign + collaboration / promo / ecommerce / membership / KOL / UGC
- Social queries: platform name + brand/campaign + key slogan / hashtag / event name

## 2.5 Subagent Decision

Before collecting, decide whether to recommend subagent mode. Recommend it when the task spans multiple platforms, themes, or material types, especially for deep or exhaustive collection.

Default split is platform-first:

- Official / brand-owned sources
- News / PR / industry media
- Video platforms
- Social platforms
- Visual / campaign archive sources
- Reports / PDFs / market context

Inside each platform shard, collect relevant material categories such as visual, video, offline activation, marketing, and PR.

Start subagents only after explicit user or controller approval. If subagents are unavailable, output the same shard plan and collect sequentially.

## 3. Collect Strong Sources First

Prefer L1-L3 before L4-L6:

1. Official source or campaign page
2. Press release or owned social announcement
3. Trade/news coverage
4. Public report or case writeup
5. Visual/video/source archive
6. Social leads and public audience traces

## 4. Capture Evidence Item

Each item should preserve:

- Source trail: source name, URL or citation, date, access date
- Short raw quote or observation
- One concise factual summary
- Category and material type
- Confidence and source level
- Screenshot status or platform restriction
- Related campaign/message if visible

Keep each item focused on a single fact, material, quote, or observation.

## 5. Verify And De-Duplicate

- De-duplicate repeated syndicated news by keeping the strongest original or earliest source.
- Do not count the same article reposted across multiple sites as multiple independent facts.
- Keep separate items when the same campaign appears in different material forms, such as video, offline event, landing page, and PR article.
- If a claim appears only in L4 search snippets, mark it as a lead and lower confidence.

## 6. Link Related Evidence

When evidence belongs to the same campaign, message, concept, hashtag, event, or launch window, assign a shared `Campaign / message` label and add `Related evidence`.

Use `tentative` when the connection is inferred from timing or naming but not explicitly confirmed.

## 7. End With Coverage And Gaps

Before output, report:

- Subagent or shard plan used
- Category volume vs target
- Source spread
- Campaign/message repetition
- Channel chain completeness
- Social/platform restrictions
- Missing evidence that would improve downstream analysis
