# Regression Samples

Use these samples when checking that normalization remains lossless and
strategy-boundary-safe.

## Sample Input

```markdown
## Evidence Pool

### Evidence V-01
- Evidence ID: V-01
- Source type: brand-owned
- Source name: Brand campaign landing page
- Date: 2026-05-01
- URL or citation: https://example.com/campaign
- Raw quote:
- Observation: Hero page uses a full-bleed blue KV, a single product bottle, and the visible line "每天轻一点".
- Summary: Campaign landing page foregrounds lightness and product visibility.
- Topic tag: 视觉轻盈
- Audience: urban young women
- Confidence: high
- Category: visual
- Material type: landing page
- Screenshot status: captured
- Brand hard data type: slogan
- Needs user confirmation: yes

### Evidence A-02
- Evidence ID: A-02
- Source type: event feedback
- Source name: Pop-up visitor notes
- Date: 2026-05-03
- URL or citation: user-provided event notes
- Raw quote: "排队很长，但拍照点很好看。"
- Observation: Feedback mentions queue friction and photo-friendly installation.
- Summary: Offline activation created visual sharing value but had operational friction.
- Topic tag: 快闪体验
- Audience: pop-up visitors
- Confidence: medium
- Category: offline activation
- Material type: event feedback

### Evidence C-03
- Evidence ID: C-03
- Source type: competitor
- Source name: Competitor launch post
- Date: 2026-04-21
- URL or citation: https://example.com/competitor-launch
- Raw quote: "我们主打高效自律。"
- Observation: Competitor frames product as a high-performance lifestyle aid.
- Summary: Competitor owns an efficiency-oriented message frame.
- Topic tag: 竞品效率叙事
- Audience: category observer
- Confidence: medium
- Category: competitor
- Brand hard data type: competitor distinction

### Evidence R-04
- Evidence ID: R-04
- Source type: review
- Source name: ecommerce review export
- Date: 2026-05-04
- URL or citation: review-export.csv row 18
- Raw quote: "没有广告说得那么轻，味道有点腻。"
- Observation: Review contradicts the lightness claim.
- Summary: Consumer review challenges the lightness message.
- Topic tag: 轻盈反证
- Audience: buyer
- Confidence: medium
- Category: review
```

## Expected Cleaned Evidence Checks

The cleaned output must preserve:

- `Evidence ID: V-01`, `A-02`, `C-03`, and `R-04`
- `Observation` for each item
- Contradiction between `V-01` and `R-04`
- Brand hard-data lead from `V-01`
- Competitor distinction lead from `C-03`
- Source separation: brand-owned, event feedback, competitor, review

## Expected Evidence Pattern Inventory Excerpt

```markdown
### Pattern: "轻盈" message is visible but not fully validated

- Evidence support: V-01, R-04
- What the evidence shows: Brand-owned landing page uses lightness wording, while one buyer review disputes the sensory claim.
- Source / channel / material structure: Brand-owned landing page vs ecommerce review.
- Contradictions or caveats: Consumer-side validation is mixed and thin.
- Confidence: medium
```

This is allowed because it describes evidence structure. Do not write a human
truth or cultural tension.

## Expected Strategy Readiness Pack Excerpt

```markdown
| Item | Candidate | Status | Evidence ID | Confidence | Notes / user confirmation needed |
| --- | --- | --- | --- | --- | --- |
| Brand truth candidate | "每天轻一点" may be a campaign slogan or lightness claim | reported | V-01 | high | Brand should confirm whether this is official brand truth, campaign line, or only page copy. |
| Proof edge | Photo-friendly installation supports shareability, but queue friction weakens experience proof | reported | A-02 | medium | Needs more event evidence. |
| Brand behavior | Offline pop-up created visible participation and photo point | reported | A-02 | medium | Operational behavior includes queue friction. |
| Competitor distinction | Competitor uses efficiency/self-discipline framing | reported | C-03 | medium | Needs broader competitor sample. |
```

## Regression Checklist

- [ ] Cleaned Evidence Pool keeps every original Evidence ID.
- [ ] Cleaned Evidence Pool keeps or adds Observation.
- [ ] Contradictory evidence is visible in pattern inventory.
- [ ] Brand hard information is preserved but not upgraded to strategy.
- [ ] Strategy Readiness Pack includes Evidence ID and Confidence for each row.
- [ ] Missing or weak evidence is marked as missing / caveat / collector task.
