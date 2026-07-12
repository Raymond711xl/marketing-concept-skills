# Input Package Contract

An input package is the bridge between upstream coordination/research and this
insight strategy skill. It can be assembled from a client brief, public brand
information, competitor research, raw consumer material, and an evidence pool.

This skill should not wait until Level 4 to discover basic brand facts. Brand
context belongs at the start.

## Recommended Package

Include what is available:

- `brief`: task, business problem, communication objective, audience, market,
  constraints, and success criteria
- `brand_context`: brand/product name, what it does, current positioning,
  public claims, channels, tone, known audience relationship
- `brand_facts`: brand truth hypotheses, product proof, brand behavior, history,
  founder belief, service proof, experience proof, and audience proof
- `competitor_context`: key competitors or substitutes, their claims, category
  conventions, and visible differentiation
- `strategy_readiness_pack`: upstream evidence-summary bridge for Level 4,
  including brand truth candidates, proof edge candidates, brand behavior
  evidence, competitor distinction, and user-confirmation needs
- `evidence_pool`: sourced evidence items from research, social platforms,
  interviews, reviews, reports, news, or event feedback

Do not require every field for every task. Use what exists, but be honest about
what its absence means.

## Evidence Item Fields

Each evidence item should contain as many of these fields as possible:

- `source_type`: news, report, brand-owned, competitor, platform-comment,
  review, interview, event feedback, survey, forum, customer service, or other
- `source_name`: publication, platform, company, interviewee group, or dataset
- `date`: publication, collection, or interview date if known
- `url_or_citation`: URL, file name, page, interview ID, or other trace
- `raw_quote`: original wording, observation, or data point
- `summary`: concise meaning of the item
- `topic_tag`: initial topic label
- `insight_lens`: need, pain-point, driver, barrier, risk, opportunity, or
  other analysis lens
- `matched_keywords`: important words, phrases, claims, or language markers
- `audience`: who the evidence represents
- `confidence`: high, medium, low, or speculative

## Acceptance Check

Before analysis, check:

- What brief and brand context are already available?
- What public or research-derived brand facts are already in the package?
- Is there a Strategy Readiness Pack from evidence summary?
- What competitor or category context is already available?
- Is there enough evidence to support at least 4-6 themes?
- Are sources diverse enough, or dominated by one platform or viewpoint?
- Are raw quotes or traceable observations present?
- Are dates recent enough for the user's question?
- Are brand-owned claims separated from consumer or third-party evidence?

## Trace ID Normalization

Preserve upstream IDs. Before Level 1, assign local IDs to any supplied item
that lacks one:

- `BR-###`: brief facts or user-stated constraints
- `BF-###`: brand, product, service, history, or brand-behavior facts
- `CP-###`: competitor or category facts
- `E###`: structured evidence-pool items when upstream IDs are absent
- `RAW-###`: rows created by the raw-evidence adapter

Keep the source citation beside every local ID. An ID is an index, not proof by
itself. Do not allow Level 4 or a Message House Foundation to cite only a
summary without a traceable source item.

## Readiness Outcomes

- `Ready`: traceable evidence can support Level 1 and the Strategy Readiness
  Pack contains usable brand and competitor facts.
- `Partial`: analysis can proceed, but evidence spread or Level 4 hard data is
  thin. Carry the gap into a Provisional strategy and Concept Package.
- `Unavailable`: no traceable evidence or supplied material can support Level
  1. Stop before insight generation and return the missing-input list.

If evidence is thin, continue only with visible caveats. If the package is
missing source trails, mark the work as exploratory. If brand facts are thin,
do not stop the whole workflow; carry the gap forward and decide at Level 4
whether the strategic output must remain provisional.

## Compatible Inputs

Treat these as valid evidence pools after light normalization:

- Competitive research outputs
- Platform monitoring or raw-evidence preparation reports
- News or report digests
- Interview notes with quotes
- Open-ended survey responses
- Comment/review exports
- Event feedback summaries

Do not perform open web research from this skill. Ask the user to run the
research skill first when fresh external evidence is needed.

## Brand Facts Handling

Levels 1-3 can usually proceed from the evidence pool. Level 4 uses the brand
context, brand facts, and Strategy Readiness Pack already present in the input
package.

Do not perform new information intake during Level 4. If Level 4 reveals that
the package lacks brand truth, product proof, repeated brand behavior, audience
proof, or competitor difference, do not treat this as a sudden hard stop. Mark
the strategy provisional and recommend rollback to:

- brief clarification,
- brand-material collection,
- competitor research, or
- evidence-pool expansion.

Prefer this wording: "The strategy can proceed as provisional; final approval
requires user confirmation or additional evidence for [specific hard-data gap]."
