# Collection Workflow

Use this workflow for each collection request.

## 0. Probe Capabilities

Before claiming that collection has started, identify the available capability classes from `references/02-source-taxonomy-and-platforms.md`.

- Record what is available, what will be used, and what is unavailable or restricted.
- Use generic capability labels, not environment-specific tool names.
- If no live access exists, stop the live-collection branch and produce a `Source Plan`, `Gaps and Restrictions`, and `User Materials Needed`.
- Mark planned searches `not executed`. Do not fabricate search logs or Evidence Pool items.
- If user-provided files, links, screenshots, or exports can be inspected, collect only those real inputs and mark the overall result `partially collected`.

## 1. Scope

Create a brief working scope:

- Controller task packet, if provided
- Target brand, campaign, event, product, market, or competitor set
- Time range and geography
- Requested categories and depth
- Known links, screenshots, exports, or seed keywords
- Downstream destination: evidence-summary-analysis or user review. The collector hands its Evidence Pool to evidence-summary-analysis; it does not perform or bypass the later strategy stage.

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

If capability limits prevent execution, preserve this section as `Source Plan` and label every row `not executed`.

## 2.5 Subagent Decision

Before collecting, apply the broad-task test in `references/10-subagent-collection-mode.md`. Recommend subagent mode only when the request is genuinely broad across multiple dimensions.

Default split is platform-first:

- Official / brand-owned sources
- News / PR / industry media
- Video platforms
- Social platforms
- Visual / campaign archive sources
- Reports / PDFs / market context

Inside each platform shard, collect relevant material categories such as visual, video, offline activation, marketing, and PR.

Start subagents only after explicit user or controller approval. If approved but subagents are unavailable, keep the same shard IDs, source scopes, and target counts, then collect the shards sequentially and report `unavailable - sequential fallback`.

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

- A unique, stable `Evidence ID` assigned once
- Source trail: source name, URL or citation, date, access date
- `Raw quote`, `Observation`, and `Summary` as separate fields
- One concise factual summary
- Category and material type
- Confidence and source level
- Screenshot status or platform restriction
- Related campaign/message if visible

Keep each item focused on a single fact, material, quote, or observation.

Every core field in `references/04-evidence-pool-contract.md` must be present. Do not leave core fields blank. For visual or other non-verbal evidence, use `Raw quote: not available` and write a concrete factual `Observation`. For text-only evidence with no useful visual observation, use `Observation: not applicable - text-only source`.

## 5. Verify And De-Duplicate

- De-duplicate repeated syndicated news by keeping the strongest original or earliest source.
- Do not count the same article reposted across multiple sites as multiple independent facts.
- Keep separate items when the same campaign appears in different material forms, such as video, offline event, landing page, and PR article.
- If a claim appears only in L4 search snippets, mark it as a lead and lower confidence.
- Never renumber an `Evidence ID` after assignment. When duplicate items are merged, retain the canonical ID, list discarded aliases in `Merged from evidence IDs`, and preserve every contributing `Shard ID` and `Shard source scope`.

## 6. Link Related Evidence

When evidence belongs to the same campaign, message, hashtag, event, or launch window, assign a shared `Campaign / message` label and add `Related evidence`.

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

Run `references/11-regression-checklist.md` before handoff. Confirm that the actual output preserves stable IDs, visual observations, Brand Hard Data provenance, restricted-platform caveats, and truthful no-access downgrade behavior.

Default to the compact frontstage handoff in `references/09-output-template.md`. Keep full query plans, shard logs, statistics, repetition snapshots, and the complete Evidence Pool in the backend dossier. If the frontstage output links to or summarizes the dossier, do not truncate or rewrite the backend Evidence Pool.
