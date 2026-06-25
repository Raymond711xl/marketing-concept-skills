# Lexicon Sourcing And Licensing

Decision record for the Chinese emotion/motive lexicons used by Insight Strategy.

## Decision (current)

**Use a self-authored, license-clean starter lexicon only.** Do not bundle full
third-party emotion lexicons into the skill. This keeps the skill freely
distributable and avoids inheriting research-only or unclear commercial terms.

The starter lexicons live here:

- `emotion-taxonomy.csv` — surface emotion markers → tension domain (Level 1→2).
- `motive-taxonomy.csv` — underlying need/fear/desire markers (Level 2).
- `tension-domains.csv` — the four tension domains both files map into.
- `zh-stopwords.txt` — basic words removed from raw-evidence token counts.
- `synonym-map.csv` — canonical term mapping for repeated variants.
- `platform-slang.csv` — platform or category language that needs explanation.

These are hand-built, original, and safe to ship and edit. They are starters,
not coverage-complete dictionaries — expand them per project, and always check
matches against raw voice rather than trusting the word list.

## How the starter is meant to grow

- Add terms from real project corpora (e.g. via `prepare_raw_evidence.py` top
  signal words) rather than importing a giant external dictionary at once.
- Keep weights in 1–3. Keep every term mapped to a `tension_domain`.
- A high-frequency word is a signal, not an insight — the lexicon only flags
  where to look.

## Expanding From Real Project Corpora

Use real project language only after checking the raw voice. Do not add a term
just because it is frequent.

Recommended workflow:

1. Run `prepare_raw_evidence.py` or review the upstream evidence pool.
2. Collect repeated phrases, emotional words, platform slang, category terms,
   and confusing variants.
3. For each candidate term, keep 2-3 raw quotes that show its actual meaning.
4. Decide whether the term belongs in:
   - `emotion-taxonomy.csv` for surface emotion markers;
   - `motive-taxonomy.csv` for need, fear, desire, fatigue, or pressure;
   - `synonym-map.csv` for spelling/wording variants;
   - `platform-slang.csv` for platform-specific or category-specific language;
   - `zh-stopwords.txt` for high-frequency noise that should be ignored.
5. Add a short note explaining why the term matters.

Candidate term review table:

| candidate_term | raw_quote_examples | observed_meaning | target_file | tension_domain | weight | action |
|---|---|---|---|---|---:|---|
| 不被催 | "不想再被催着变优秀" | freedom from pressure | motive-taxonomy.csv | social_position | 3 | add |
| 种草 | "被种草但怕踩雷" | platform purchase influence | platform-slang.csv | life_design | 2 | explain |
| 哈哈 | repeated filler | noise | zh-stopwords.txt | n/a | 1 | stopword |

## What The User Can Provide

For stopwords, synonyms, and platform slang, the user does not need to prepare a
perfect dictionary. Any of the following is enough:

- a CSV/XLSX export of comments, reviews, posts, or open-ended survey answers;
- a pasted list of weird repeated words;
- screenshots or notes showing platform slang;
- a short note like "these words are noise in this category";
- a list of terms that should be merged under one canonical phrase.

If the user can structure it, use these columns:

| source | raw_term | example_quote | observed_meaning | suggested_action | notes |
|---|---|---|---|---|---|
| Xiaohongshu comments | 闭眼入 | "这个可以闭眼入" | trust / low-risk purchase | add slang | category-specific |
| Tmall reviews | 回购 | "已经回购三次" | repeat purchase | add synonym or tag | positive signal |
| Survey open end | 啊啊啊 | "啊啊啊真的烦" | emotional filler | stopword maybe | check context |

Suggested actions:

- `stopword`: remove from token counts.
- `synonym`: map to a canonical term.
- `slang`: define platform/category meaning.
- `emotion`: add as surface feeling marker.
- `motive`: add as need, fear, desire, pressure, or fatigue marker.
- `ignore`: do not add; keep as raw context only.

## External options reviewed (NOT bundled)

Kept here so the decision is auditable. Verify license terms again before any
future integration — do not rely on this summary alone.

| Resource | Coverage | License posture (as understood) | Fit |
|---|---|---|---|
| GoEmotions (Google) | 27 emotion categories, **English** | Open, research-friendly | Wrong language; useful only as a *category* reference, not terms |
| NRC Emotion Lexicon | Multilingual emotion/affect | **Free for research; commercial use requires separate license** | Do not bundle; license-gate before any commercial use |
| DLUT 大连理工 情感词汇本体 | Chinese, academic-grade | **Academic use stated; commercial needs contacting authors** | Strong Chinese coverage but license unclear for our workflow |
| NTUSD 台大情感极性词典 | Chinese polarity (pos/neg) | GitHub copies indicate **MIT** | Polarity only (not fine-grained emotion); MIT is permissive if confirmed |

## If we later want broader coverage

Preferred order, lowest legal risk first:

1. Keep expanding the self-authored starter from project corpora.
2. Integrate only a license-clear open set (e.g. NTUSD if MIT is confirmed on the
   specific copy used), recording source + license per term batch.
3. Pursue a commercial Chinese lexicon only if a project demands certified
   coverage — and only after a written license check.

Anything beyond step 1 should also add an entry to the third-tier "Lexicon 授权
记录" so distribution risk stays tracked.
