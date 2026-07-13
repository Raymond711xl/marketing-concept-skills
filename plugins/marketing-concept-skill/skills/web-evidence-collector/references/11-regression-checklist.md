# Minimum Regression Checklist

Run this checklist before handing a collection dossier to `evidence-summary-analysis`. These are behavioral test cases, not evidence fixtures. Never copy placeholder text from this file into a live Evidence Pool.

## Case 1: Public Official Source

Scenario: An official site, press release, filing, campaign page, or official public account is accessible.

Pass when:

- The evidence item has a stable, non-empty `Evidence ID`.
- `Source type`, `Source name`, `Date`, and `URL or citation` identify the actual source.
- A short `Raw quote` is preserved when useful; no long copyrighted passage is copied.
- `Observation` and `Summary` remain separate from the quote.
- `Confidence` reflects direct access and source quality.
- A brand-owned claim is labeled as a claim, not audience truth.

## Case 2: Restricted Dynamic Social Source

Scenario: A Xiaohongshu, Weibo, Douyin, Zhihu, Bilibili, WeChat, or similar page is discoverable but full content requires login, is unstable, or cannot be inspected.

Pass when:

- The item contains only a real visible short phrase, title, metadata trace, link, or result citation.
- `Limitation / restriction` states what was not accessible.
- `Screenshot status` is `not accessible` or `user needed` when appropriate.
- `Confidence` is lowered unless another source corroborates the lead.
- No login, paywall, CAPTCHA, anti-bot control, or access restriction was bypassed.
- If no real trace exists, the source appears only in `Source Plan` or `Gaps and Restrictions`, not as an evidence item.

## Case 3: Visual Observation Without A Quote

Scenario: A poster, KV, packaging image, landing page, screenshot, event photo, thumbnail, or video frame has no useful visible wording.

Pass when:

- `Raw quote` is `not available`.
- `Observation` gives a concrete factual visual description and is not blank.
- `Summary` explains the evidence value without repeating or replacing `Observation`.
- Source, citation, date status, screenshot status, and Confidence remain present.
- The item does not infer audience emotion, human truth, positioning, or cultural tension.

## Case 4: Brand Hard Data Candidate

Scenario: Public material suggests a philosophy, vision, slogan, chronology, founder statement, product proof, service proof, brand behavior, or competitor distinction.

Pass when:

- The candidate has a corresponding item in the Evidence Pool.
- The `Brand Hard Data Track` row cites the exact source `Evidence ID`.
- The row includes `Candidate status`, `Confidence`, and `Needs user confirmation`.
- Public candidates absent from the user's official brief use `Needs user confirmation: yes`.
- Brand self-description remains separate from consumer or audience evidence.

## Case 5: No Live Collection Capability

Scenario: No public search, page inspection, browser, authorized connector, official interface, or authorized export is available, and the user supplied no inspectable material.

Pass when the output includes:

```text
Collection status: not collected - capability unavailable
Evidence items: 0
```

It must also include:

- A `Source Plan` labeled `not executed`
- `Gaps and Restrictions`
- `User Materials Needed`
- No simulated URLs, citations, quotes, dates, metrics, search logs, screenshots, or Evidence Pool items

If real user-provided material is available, process only that material, set `Collection status: partially collected`, and label each item `Source type: user provided`.

## Lossless Handoff Check

Before completion, verify:

- Every actual item contains all 11 `Evidence Pool v1` core fields with exact names.
- Every `Evidence ID` is unique and unchanged from capture through merge.
- Every visual evidence item retains `Observation` when `Raw quote` is unavailable.
- No frontstage compression changed or deleted the backend Evidence Pool.
- Duplicate merges retain canonical IDs, alias IDs, shard IDs, and shard source scopes.
- Every Brand Hard Data candidate points to an existing Evidence ID.
- The handoff notice explicitly tells `evidence-summary-analysis` not to delete, rename, merge, or overwrite core fields.
- The output contains no human truth, cultural tension, positioning, Idea Platform, Concept, or strategic recommendation.
- Any controller/user `Primary Research Lens`, `Supporting Research Lens`, `Delivery Mode`, and `Lens adaptation note` remain unchanged in the collection brief and downstream handoff.
- Research Lens affects source priority only; material `Category` values remain evidence-form labels and are not renamed to match the lens.
