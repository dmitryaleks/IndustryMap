# Audiobook Rewrite Guidelines for Agentic LLM

This document provides comprehensive instructions for rewriting the book *Silicon Foundations -- Japan's Hidden Dominance in the Semiconductor Supply Chain* into a format optimized for audiobook narration. The source chapters are written for print/e-book and contain tables, dense numerical data, markdown formatting, and visual structural cues that do not translate to audio. The rewrite agent must transform the text so that a listener -- hearing the words spoken aloud exactly once, without the ability to re-read, glance at a table, or visually scan ahead -- can follow, understand, and retain the material.

---

## 1. Core Principle: Write for the Ear, Not the Eye

Every sentence you produce must pass a single test: **can a listener understand it on first hearing, without seeing it written down?**

Print readers can re-read a dense sentence, glance at a table header to remember a column label, or visually parse a parenthetical with three nested clauses. Audio listeners cannot. They get one pass. If a sentence requires two readings to parse, it fails.

This does not mean dumbing down the content. The target audience -- investors and technology enthusiasts -- is sophisticated. It means restructuring how information is delivered: shorter sentences, more signposting, explicit transitions, natural-language equivalents for visual formatting, and strategic repetition of key terms.

---

## 2. Handling Tables

Tables are the single biggest obstacle in converting this book to audio. The source text uses tables for financial metrics, company comparisons, peer group data, progress tracking, and edge lists. **Tables cannot be narrated as tables.** They must be converted to prose.

### 2.1 Financial Metric Tables

Source (print):
```
| Metric | Value |
|--------|-------|
| PER | 21.5x |
| PBR | 1.8x |
| Revenue Growth | 15.6% |
| Operating Margin | 14.9% |
| Foreign Ownership | 12.3% |
```

Rewrite (audio):
> The company trades at a price-to-earnings ratio of about twenty-two times and a price-to-book of just under two. Revenue has been growing at roughly sixteen percent, with operating margins near fifteen percent. Foreign investors hold about twelve percent of the shares outstanding.

Rules:
- Expand all abbreviations on first use in each chapter: PER becomes "price-to-earnings ratio," PBR becomes "price-to-book ratio," EPS becomes "earnings per share."
- After first use, you may use the abbreviation spoken as letters ("P-E ratio") if the term recurs more than three times in the same chapter.
- Round numbers to human-friendly approximations: 21.5x becomes "about twenty-two times"; 14.9% becomes "near fifteen percent" or "roughly fifteen percent."
- Do not read all metrics in a single run-on sentence. Break them into two or three short sentences grouped logically (valuation metrics together, growth metrics together, ownership metrics together).
- Omit metrics that are not discussed in the surrounding narrative. If a table exists purely as a data reference and the chapter text never interprets the numbers, summarize only the most salient one or two figures.

### 2.2 Comparison Tables (Multiple Companies)

When a table compares several companies across the same metrics, convert to a narrative comparison:

> Among the three wafer producers, Shin-Etsu is the largest by a wide margin, with a market capitalization roughly twenty times that of SUMCO. Both trade at price-to-earnings multiples above thirty, but Shin-Etsu's superior margins -- operating profit near forty percent -- explain its premium. SUMCO, by contrast, operates on thinner margins but offers higher revenue sensitivity to capacity expansions.

Rules:
- Lead with the comparison point, not the data.
- Name no more than three or four companies in a single comparative passage. If the source table has more, group them and narrate in batches.
- Use relative language ("twice as large," "roughly half," "in line with peers") rather than precise side-by-side numbers.

### 2.3 Supply Chain Edge Tables

The source text includes tabular listings of supplier-client relationships. Convert these to narrative chains:

> PILLAR Corporation supplies its fluororesin fittings to nearly every major wet-process equipment maker in Japan, including SCREEN Holdings -- its single largest customer -- as well as Tokyo Electron, Ebara, and Kokusai Electric. Through these equipment makers, PILLAR's products ultimately reach every leading-edge fab operator: TSMC, Samsung, Intel, and SK Hynix among them.

Rules:
- Group suppliers/clients by category (equipment makers, chipmakers, materials companies) rather than listing them in database order.
- Limit any single list read aloud to five names. If more exist, say "among others" or "and several more."
- Emphasize the most important relationships and allow lesser ones to be implied.

### 2.4 Progress and Reference Tables

Tables used for internal tracking (progress tables, session logs, peer group appendix tables) should be **omitted entirely** from the audiobook. They are metadata, not content.

---

## 3. Numbers, Units, and Financial Data

### 3.1 General Number Rules

- **Spell out all numbers** in the rewrite. Write "forty-two percent" not "42%." Write "three hundred millimeters" not "300mm." The narrator will read what is written; numerals on a page are ambiguous in pronunciation.
- **Round aggressively** for audio. Listeners cannot hold "45.9 billion yen" in working memory as well as "roughly forty-six billion yen" or "about forty-six billion yen." Use the word "approximately," "roughly," "about," or "nearly" to signal rounding.
- **Avoid stacking numbers.** Never put more than two numerical facts in a single sentence. If the source has a sentence with three or more numbers, break it into multiple sentences or cut the least important figure.

### 3.2 Currency

- Use "yen" for JPY figures. On first occurrence in each chapter, say "Japanese yen."
- For very large yen figures, use the most intuitive scale: "about nine trillion yen" (not "nine-point-four trillion yen" or "9,400 billion yen").
- When a US dollar equivalent adds context for an international listener, include it parenthetically in natural speech: "roughly forty-six billion yen -- about three hundred million US dollars."
- Do not convert all yen figures to dollars. Use dollar equivalents only when the figure is central to the narrative point being made.

### 3.3 Market Data and Multiples

- "PER of 21.5x" becomes "a price-to-earnings ratio of about twenty-two times."
- "PBR 0.64x" becomes "a price-to-book ratio of just zero-point-six -- well below one, meaning the market values the company at less than its book value."
- When a valuation ratio is meaningful (notably cheap or expensive), explain why in a brief clause rather than leaving the number to speak for itself.

### 3.4 Percentages and Market Shares

- "60%+" becomes "more than sixty percent."
- "Over 70% global market share" becomes "more than seventy percent of the global market."
- When two market share figures together imply dominance (e.g., company A at 42% and company B at 20%), narrate the combined implication: "Together, these two companies control more than sixty percent of the world market."

### 3.5 Dates and Time Periods

- Fiscal years: "FY2025" becomes "fiscal year twenty-twenty-five."
- Founded dates: "Founded in 1916" is fine as-is.
- Historical periods: "the 1990s" is fine as-is.

---

## 4. Ticker Symbols and Company Identifiers

### 4.1 Ticker Symbols

Tickers are visual shorthand. In audio, they are noise unless the listener specifically needs them for stock lookup.

Rules:
- **Omit tickers on first mention** of a company. Introduce companies by full name only: "Shin-Etsu Chemical" not "Shin-Etsu Chemical, ticker four-zero-six-three-dot-T."
- **Include the ticker once per chapter** in a natural aside, if the company is a primary subject of that chapter: "Shin-Etsu Chemical -- listed in Tokyo under the ticker four-zero-six-three -- controls forty-two percent of the global wafer market."
- For companies that appear repeatedly across chapters, include the ticker only in their primary chapter (as listed in the coverage map).
- Never read the ".T" suffix as "dot-T." Say "listed on the Tokyo Stock Exchange" or "traded in Tokyo" instead. For non-Japanese tickers, say the exchange name: "listed on the Korea Exchange" for .KS, "listed in Taipei" for .TW.

### 4.2 CMP Identifiers

CMP-0001, CMP-0024, etc. are internal database identifiers. **Strip them completely** from the audiobook text. They have no meaning to a listener and will be heard as meaningless alphanumeric strings.

### 4.3 File References

References to data files (graph.json, CMP-*.json, evaluation_progress.json) are metadata. **Strip them completely**, including the "Data sources" footer at the end of each chapter.

---

## 5. Structural Formatting

### 5.1 Chapter Headers

Markdown headers (`#`, `##`, `###`) have no audio equivalent. Replace them with vocal signposts:

- `# Chapter 6: Lithography` -- The narrator reads: "Chapter Six. Lithography -- Printing the Circuit."
- `## Introduction` -- Omit the header; just begin the introductory text. The transition is implicit.
- `### Shin-Etsu Chemical` -- Replace with a transitional sentence: "Let us now turn to Shin-Etsu Chemical, the world's largest silicon wafer manufacturer."

Rules:
- Level-1 headers (chapter titles) are spoken as "Chapter [number]. [Title]."
- Level-2 headers become transitional sentences or brief pauses. The narrator should be able to speak the text with a natural breath pause where a section break occurs.
- Level-3 headers (company names, subsections) become transitional phrases woven into the prose.
- Insert a brief signpost sentence before major section transitions: "Having examined the wafer itself, we now turn to the chemicals that pattern it." This replaces the visual white space and heading that a print reader uses to orient themselves.

### 5.2 Blockquotes (Chapter Thesis)

Each chapter opens with a one-sentence thesis in a blockquote. In the audiobook, this becomes the opening line of the chapter, spoken as a declarative statement without any blockquote indication:

Source: `> Japan controls an extraordinary number of critical chokepoints...`

Audio: "Japan controls an extraordinary number of critical chokepoints in the global semiconductor supply chain -- positions that are structural, not incidental -- and most investors do not fully appreciate this dominance."

### 5.3 Bold and Italic

Bold and italic are visual emphasis cues. In audio, emphasis is conveyed by:
- Word choice: "critically," "remarkably," "the key point here is..."
- Sentence structure: place the emphasized idea at the end of the sentence (the stress position) or at the very beginning.
- Do not insert narrator instructions like "[emphasis]" or "[pause]." Write prose that naturally invites vocal emphasis through its rhythm.

### 5.4 Bullet Points and Numbered Lists

Bullets and numbered lists are visual structures. Convert them to prose:

Source:
```
Key takeaways:
- Japan controls 60%+ of the wafer market
- Lasertec is the sole EUV mask inspection supplier
- DISCO holds 70%+ of dicing equipment
```

Audio:
> Three points stand out from this chapter. First, Japan controls more than sixty percent of the global wafer market through Shin-Etsu and SUMCO. Second, Lasertec is the sole supplier of EUV photomask inspection equipment in the world -- a monopoly without substitute. And third, DISCO dominates dicing equipment with more than seventy percent market share.

Rules:
- Use ordinal signposting: "First... Second... Third..." or "The first point... The next... Finally..."
- Limit to five items. If the source has more, consolidate or cut the least important.
- Never say "bullet point" or "dash."

### 5.5 Horizontal Rules and Visual Separators

Markdown `---` separators have no audio equivalent. Replace with a brief transitional sentence or a natural paragraph break. The narrator's pacing and a brief silence will serve the same function.

---

## 6. Sentence Structure and Pacing

### 6.1 Sentence Length

- Target an average sentence length of **fifteen to twenty words** for audio. The print version averages twenty-five to thirty-five. This is the single most impactful change for listener comprehension.
- Break complex sentences at natural clause boundaries. A sentence with a semicolon in print should almost always become two sentences in audio.
- Avoid nested parentheticals. If a sentence has a parenthetical inside a parenthetical, restructure it.

### 6.2 Appositive Clauses

The source text uses heavy appositive structures:

> "Lasertec Corporation (CMP-0006, ticker 6920.T) occupies what may be the most absolute monopoly in the entire semiconductor supply chain."

For audio, front-load or separate the appositive:

> "Lasertec Corporation occupies what may be the most absolute monopoly in the entire semiconductor supply chain. The company, listed in Tokyo, is the sole global supplier of actinic EUV photomask inspection equipment."

### 6.3 Signposting and Transitions

Listeners need more navigational cues than readers. Insert:
- **Forward references:** "We will return to this point in Chapter Twelve, when we examine fab infrastructure."
- **Backward references:** "As we discussed in Chapter Two, lithography is the step that determines minimum feature size."
- **Section transitions:** "That covers the technical process. Now let us look at the companies that dominate it."
- **Summary callbacks:** At the end of a long technical explanation, briefly restate the key point before moving on: "The essential point is this: without angstrom-level flatness, multi-patterning simply does not work. That is why CMP matters."

### 6.4 Repetition for Retention

Print text avoids restating facts because the reader can glance back. Audio must restate key facts strategically:
- Reintroduce a company's role when returning to it after a digression: "Shin-Etsu -- the world's largest wafer maker, as we noted earlier --"
- When a chapter discusses six or more companies, provide a brief verbal recap before the final section: "We have now examined five companies in this space: Shin-Etsu and SUMCO in wafers, Organo in ultrapure water, and Nippon Sanso and Kanto Denka in specialty gases. One more company remains."

---

## 7. Technical Content

### 7.1 Technical Terms

This book is written for a knowledgeable audience, and technical terminology should be preserved -- not simplified away. However, audio requires more contextual scaffolding:

- On first use in each chapter, provide a brief in-line definition or restatement: "chemical mechanical planarization -- often called CMP, the process of polishing a wafer surface to atomic-level flatness."
- On subsequent uses in the same chapter, the abbreviation alone is sufficient.
- For highly specialized terms that a non-engineer listener may not retain (e.g., "novolac resin," "trichlorosilane"), attach a one-clause functional description each time they appear in a new chapter: "novolac resin, the base polymer used in photoresist."

### 7.2 Chemical Formulas and Units

- Do not read chemical formulas as written. "SiO2" becomes "silicon dioxide." "SiHCl3" becomes "trichlorosilane." "HF" becomes "hydrofluoric acid" on first use, then "HF" spoken as "H-F" if repeated frequently.
- "300mm" becomes "three hundred millimeters." Add context if helpful: "three hundred millimeters -- about twelve inches -- in diameter."
- "sub-ppb" becomes "below one part per billion."
- Temperature: "1,425 degrees Celsius" is fine, but avoid stacking multiple temperatures in one sentence.

### 7.3 Analogies and Scale

The source text already uses some excellent analogies (the football-pitch flatness analogy, the city-and-sticker overlay analogy). Preserve these -- they are especially powerful in audio because they give the listener a mental image. Where the source text presents a raw number without an analogy, consider whether one would help the listener grasp the scale. However, do not invent analogies that are not supported by the source text's factual claims.

---

## 8. Company Profiles

Company profile sections in the source text follow a structured template with a header line (company name, ticker, one-line role), a metadata line (Founded, HQ, Market Cap), and several paragraphs. For audio:

### 8.1 Company Introductions

Replace the structured header with a spoken introduction:

Source:
```
### Shin-Etsu Chemical (4063.T) -- World's largest silicon wafer manufacturer
**Founded:** 1926 | **HQ:** Tokyo | **Market Cap:** ~9.4 trillion yen
```

Audio:
> "Let us turn now to Shin-Etsu Chemical, the largest silicon wafer manufacturer in the world. Founded in nineteen twenty-six and headquartered in Tokyo, the company has grown into a chemical conglomerate with a market capitalization of approximately nine trillion yen -- making it one of the most valuable companies in Japan's semiconductor ecosystem."

### 8.2 Investment Perspective Sections

When the source text includes an "Investment Perspective" subsection drawn from evaluation scores and investment theses, narrate it as an analytical aside:

> "From an investment standpoint, Gun Ei Chemical is one of the most compelling names in this study. The company trades at a price-to-book ratio of just zero-point-six -- meaning the market values it at barely more than half its book value. Its overall evaluation score of seventy-nine out of a hundred is the highest in our dataset, reflecting the combination of a near-monopoly position, expanding capacity, and a valuation that appears to significantly understate the company's strategic importance."

---

## 9. Cross-References

### 9.1 Chapter References

- Replace "see Chapter X" with a full spoken reference: "as we will explore in Chapter Eight, on photoresists and chemicals."
- Replace "see Appendix A" with: "the company cards in the appendix provide additional detail."
- Use forward and backward references sparingly -- no more than two or three per chapter. Too many "as we discussed" and "as we will see" phrases break the listening flow.

### 9.2 Internal Data References

- Strip all references to file names, JSON files, CMP IDs, and database identifiers.
- Replace "as recorded in graph.json" with nothing -- the data simply is.
- Replace "see evaluation_progress.json" with "based on our evaluation framework" or similar.

---

## 10. Appendices

Appendices present a particular challenge for audio. They are structured as reference material -- designed to be scanned, not read linearly. The following guidelines apply:

### 10.1 Appendix A (Japanese Company Cards)

Convert each company card into a brief spoken profile of two to three sentences. Group the sixty-two companies by their primary chapter to give the listener a structured tour. Provide a spoken introduction: "This appendix offers a brief profile of each of the sixty-two Japanese companies examined in this book, organized by their role in the semiconductor supply chain."

### 10.2 Appendix B (Global Ecosystem)

Same approach as Appendix A but briefer. One to two sentences per company. Group by country or by role (foundries, memory makers, equipment, etc.).

### 10.3 Appendix C (Supply Chain Edge List)

**Omit entirely** from the audiobook. A spoken list of three hundred twenty-one supply chain edges would be unintelligible and serves no purpose in audio. The relationships are already narrated in the body chapters.

### 10.4 Appendix D (Evaluation Methodology)

Convert to a narrative explanation of the scoring system. Omit the rubric tables and point-allocation grids. Focus on explaining what the six dimensions measure and why the framework exists. Target approximately five to seven minutes of narration (roughly twelve hundred to fifteen hundred words).

### 10.5 Appendix E (Glossary)

Convert to a "key terms" segment with the twenty to thirty most important terms, each defined in a single spoken sentence. Omit terms that are already defined in context in the body chapters. Alphabetical ordering is acceptable for audio since the listener can use chapter navigation to jump to a term.

---

## 11. Pacing Cues for the Narrator

While this rewrite is textual (not a narration script with stage directions), the prose should be written in a way that naturally guides a professional narrator:

- End paragraphs on a complete thought. Do not let paragraphs trail off into a dependent clause.
- Use sentence-final stress positions for key facts: "That company is Lasertec" is more impactful than "Lasertec is that company."
- Vary sentence length rhythmically. Follow a long explanatory sentence with a short declarative one. Follow a list of facts with a single-sentence synthesis.
- Use rhetorical questions sparingly but effectively to re-engage the listener: "So who supplies the chemicals that make all of this possible?"
- Mark chapter endings with a brief, conclusive paragraph that provides a sense of closure and anticipation: "In the next chapter, we move from the wafer surface to the back end of the line -- where tested, diced, and packaged chips finally become the products that power the modern world."

---

## 12. What to Preserve Unchanged

Not everything needs to change. The following elements of the source text should be preserved as-is or with minimal modification:

- **The narrative voice.** The book's tone is authoritative, measured, and analytical. Do not make it conversational, casual, or breathless. The audiobook should sound like a well-informed analyst speaking to a serious audience, not a podcast host.
- **The thesis and argument structure.** Each chapter makes an argument. Preserve its logical arc.
- **Analogies and metaphors.** They are already audio-friendly.
- **Direct factual claims.** Do not soften facts to make them easier to speak. If the book says "sole global supplier," the audiobook says "sole global supplier."
- **Chapter order and scope.** Do not merge or split chapters. The audiobook chapter structure should mirror the book exactly, so that chapter navigation in the audiobook player corresponds to the table of contents.

---

## 13. What to Cut

Some content in the print edition exists for reference and adds no value in audio:

- **Data source footers** at the end of each chapter (e.g., "*Data sources: CMP-0024, CMP-0025, CMP-0009*").
- **Internal tracking metadata** (progress tables, session logs, agent instructions).
- **Redundant cross-reference tables** (the company coverage map, the peer group appendix reference).
- **Appendix C** in its entirety (the edge list).
- **Markdown formatting artifacts** (horizontal rules, HTML-style tags, blockquote markers).

---

## 14. Agent Workflow for Audiobook Rewrite

### 14.1 Per-Chapter Process

1. **Read the source chapter** from `book/[chapter-file].md`.
2. **Read this style guide** in full before beginning any rewrite.
3. **Identify all tables, ticker symbols, CMP IDs, bullet lists, and file references** in the source.
4. **Rewrite the chapter** applying all rules in this document, producing a clean prose manuscript.
5. **Write the audiobook chapter** to `book/audiobook/[chapter-file].md`.
6. **Self-check:** Read the output aloud mentally. Flag any sentence that would confuse a listener hearing it once.

### 14.2 Quality Checklist

Before submitting a rewritten chapter, verify:

- [ ] No tables remain. All tabular data has been converted to prose.
- [ ] No CMP identifiers remain (CMP-0001, etc.).
- [ ] No file references remain (graph.json, evaluation_progress.json, etc.).
- [ ] No markdown formatting remains (bold markers, header markers, horizontal rules).
- [ ] Ticker symbols appear at most once per chapter, in natural speech.
- [ ] All numbers are spelled out.
- [ ] All abbreviations are expanded on first use in the chapter.
- [ ] No sentence exceeds approximately thirty-five words.
- [ ] No paragraph stacks more than three numerical facts without a breathing sentence between them.
- [ ] Section transitions use spoken signposts, not visual headers.
- [ ] The chapter opens with a spoken thesis (converted from the blockquote).
- [ ] The chapter closes with a concluding paragraph that provides closure.
- [ ] Forward and backward chapter references use full chapter titles, not just numbers.

### 14.3 Output Format

- Write in clean, unformatted prose. No markdown, no bold, no italics, no headers.
- Use a single blank line between paragraphs.
- Use "Chapter [Number]. [Title]" as the opening line of each chapter file.
- Use "--" (em dash equivalent) where the source uses them, as the narrator will interpret these as natural pauses.
- Target approximately the same word count as the source chapter, plus or minus fifteen percent. Converting tables to prose may increase count; cutting metadata may decrease it. These effects roughly cancel out.

---

## 15. Sample Rewrite (Excerpt)

### Source (Print)

```markdown
### DISCO (6146.T) -- Global dicing equipment leader

**Founded:** 1937 | **HQ:** Tokyo | **Market Cap:** ~8 trillion yen

DISCO Corporation (CMP-0002) controls over 70% of the global market for
dicing saws and wafer grinders. Together with Tokyo Seimitsu (CMP-0001),
DISCO accounts for approximately 90% of global dicing equipment.

**Key Financials:**
| Metric | Value |
|--------|-------|
| PER | 51.2x |
| PBR | 12.4x |
| Operating Margin | 41.3% |
| Foreign Ownership | 38.7% |
| Analyst Consensus | 12/15 Buy |
```

### Rewrite (Audiobook)

> Let us now turn to DISCO, the undisputed global leader in dicing equipment. Founded in nineteen thirty-seven and headquartered in Tokyo, DISCO has grown into one of the most valuable companies in Japan's semiconductor equipment sector, with a market capitalization of approximately eight trillion yen.
>
> The numbers tell a remarkable story. DISCO controls more than seventy percent of the global market for dicing saws and wafer grinders. When you add its primary competitor, Tokyo Seimitsu, the two Japanese companies together account for roughly ninety percent of all dicing equipment sold worldwide. This is not a competitive market -- it is a duopoly.
>
> The company's valuation reflects this dominance. DISCO trades at a price-to-earnings ratio above fifty times -- expensive by conventional standards, but supported by operating margins above forty percent and strong institutional interest, with nearly forty percent of shares held by foreign investors. Twelve of fifteen covering analysts rate the stock a buy.

---

## 16. Acronym and Abbreviation Clusters

The source text -- particularly Chapters 5 (UPW & Gases), 6 (Lithography), 8 (Photoresist), 9 (Deposition), and 17 (Geopolitics) -- contains passages where eight to fifteen different acronyms appear within a single paragraph. In print, a reader can glance back to recall what "PECVD" stands for. A listener cannot. Acronym clusters are one of the most severe comprehension killers in audio.

### 16.1 The Five-Acronym Rule

No paragraph in the audiobook should introduce more than five new acronyms. If the source paragraph contains more, split it into multiple paragraphs, each introducing a subset, with a bridging sentence between them.

Source:
> "The major deposition techniques include CVD, LPCVD, PECVD, MOCVD, HDP-CVD, PVD, ALD, and MBE, each optimized for different materials and process conditions."

Audio:
> "Several major techniques exist for depositing thin films. The most common is chemical vapor deposition, or CVD, which introduces gaseous precursors that react on the wafer surface. Variations include low-pressure CVD, plasma-enhanced CVD, and metal-organic CVD -- each tuned for different temperatures and materials. Separately, physical vapor deposition, or sputtering, ejects atoms from a solid target onto the wafer. And atomic layer deposition, or ALD, deposits material one atomic layer at a time, offering the finest control of all."

### 16.2 Acronym Pacing

When introducing an acronym for the first time in a chapter, always give the full name first, pause (with a sentence break or em dash), and then give the abbreviation:
- "chemical vapor deposition -- often called CVD" (correct)
- "CVD, which stands for chemical vapor deposition" (acceptable but less natural)
- "CVD (chemical vapor deposition)" (print-only; do not use in audio)

When an acronym has already been introduced in the current chapter and appears in a cluster with other acronyms, use only the abbreviation but slow the pacing by limiting to two or three per sentence:
- "The fab uses CVD for insulating layers, PVD for metal contacts, and ALD for the thinnest barrier films." (three in one sentence -- acceptable)
- "The fab uses CVD for insulating layers, PVD for metal contacts, ALD for barrier films, RIE for etching, and ICP for high-density plasma processing." (five in one sentence -- too many; split)

### 16.3 Regulatory and Policy Acronyms

Chapters 16 and 17 introduce regulatory acronyms (BIS, METI, CHIPS Act, Entity List). Treat these identically to technical acronyms: expand on first use, then use the abbreviation. For "Entity List" and "CHIPS Act," which are proper names rather than abbreviations, no expansion is needed -- but provide a one-clause explanation on first mention: "the Entity List, the US government's registry of restricted foreign organizations."

---

## 17. Chemical Formula Cascades

Several chapters list multiple chemical compounds with their formulas in rapid succession. This is common in Chapters 5, 8, 9, and 10.

### 17.1 The Problem

Source:
> "Etch gases include carbon tetrafluoride (CF4), hexafluoroethane (C2F6), octafluorocyclobutane (C4F8), sulfur hexafluoride (SF6), nitrogen trifluoride (NF3), chlorine (Cl2), boron trichloride (BCl3), and hydrogen bromide (HBr)."

This eight-item list of chemical names, each followed by its formula in parentheses, is unparseable in audio. The listener hears sixteen pieces of information in one sentence and retains zero.

### 17.2 Conversion Strategy

Break chemical cascades into functional groups and omit formulas entirely. The listener does not need the molecular formula -- they need to understand what the chemicals do and why they matter.

Audio:
> "The etching process relies on a family of highly reactive gases, each chosen for its ability to attack a specific material. Fluorine-based gases -- including carbon tetrafluoride and nitrogen trifluoride -- are used to etch silicon dioxide and silicon nitride. Chlorine-based gases handle aluminum and certain metal layers. And hydrogen bromide is the gas of choice for etching pure silicon with high selectivity."

Rules:
- Never list more than three chemical names in a single sentence.
- Omit the molecular formula entirely. Say "carbon tetrafluoride" not "carbon tetrafluoride, C-F-four." The formula adds nothing for the listener.
- Group chemicals by function (etching, deposition, cleaning, doping) rather than listing them alphabetically or in the order they appear in the source.
- For less-known chemicals (tetraethyl orthosilicate, trimethylaluminum), use a functional label instead: "an organosilicon precursor" or "an aluminum-containing compound."

### 17.3 Cleaning Solution Sequences

The RCA cleaning sequence and similar multi-step chemical protocols (SC-1, SC-2, SPM, DHF, piranha) appear in Chapters 5 and 10 with concentration ratios and temperature ranges.

Source:
> "SC-1: A mixture of ammonium hydroxide (NH4OH), hydrogen peroxide (H2O2), and deionized water, typically in a ratio of 1:1:5 to 1:2:7, heated to 65-80 degrees Celsius."

Audio:
> "The first cleaning step, called SC-1, uses a heated alkaline mixture of ammonium hydroxide, hydrogen peroxide, and ultrapure water. It is designed to remove organic contaminants and particles from the wafer surface."

Rules:
- Omit concentration ratios (1:1:5, 3:1, etc.) unless the ratio is the specific point being made. Listeners cannot hold ratio notation in working memory.
- Omit temperature ranges unless they illustrate a point about process difficulty. A listener does not need to know that SC-1 runs at sixty-five to eighty degrees Celsius.
- Replace the chemical purpose with a plain-English functional description.

---

## 18. Long Inline Company Lists

The source text frequently embeds lists of ten to thirty-five company names in flowing prose -- not as tables or bullets, but as comma-separated sequences within a sentence. This occurs in Chapters 3, 10, 12, 13, 14, 15, and 16.

### 18.1 The Problem

Source (Chapter 15):
> "Its client list includes TSMC, Samsung, Intel, SK Hynix, Micron, Kioxia, ASE Technology (the world's largest OSAT), Amkor (number two), JCET (China's largest OSAT), Tongfu Microelectronics, Tianshui Huatian, Powertech Technology, DB HiTek, HANA Micron, Nepes, SFA Semicon, LB Semicon, Nexchip, CR Micro, YMTC, CanSemi, GTA Semiconductor, KYEC, UMC, VSMC, Chipbond, ChipMOS, GlobalFoundries, UTAC, Inari Amertron, Unisem, and MPI Malaysia."

This is thirty-two companies in a single sentence. A listener will lose track after the fifth name.

### 18.2 Conversion Strategy

Apply the **"Five Names, Then Generalize"** rule:

Audio:
> "The company's client list is remarkably broad. It supplies all of the world's leading chipmakers -- TSMC, Samsung, Intel, SK Hynix, and Micron among them. It also supplies the major outsourced assembly houses, including ASE Technology, Amkor, and JCET. Beyond these, it reaches dozens of smaller foundries and packaging companies across Taiwan, Korea, China, Singapore, and Malaysia. In total, more than thirty companies appear as direct customers in the supply chain data."

Rules:
- Name the five most important companies explicitly.
- Characterize the remainder by category, geography, or count.
- End with a summary statement that conveys the scope ("more than thirty direct customers") so the listener grasps the scale even though they did not hear every name.
- Never read more than five company names in a row without a category label or breathing sentence between them.

### 18.3 Country-Grouped Company Lists

When the source groups companies by country within a list (common in Chapters 3, 13, and 17), use geography as the organizing principle in audio:

Audio:
> "In Taiwan, the company counts TSMC, UMC, and several packaging firms among its customers. In South Korea, Samsung, SK Hynix, and a number of smaller OSATs. In China, SMIC and Hua Hong lead the list, followed by more than a dozen domestic foundries and memory makers."

---

## 19. Purity Notation

Purity tiers are a recurring concept across Chapters 4, 5, 8, and 10. The source text uses multiple notations for the same concept: "twelve-nine purity," "99.9999999999%," "sub-ppt," "sub-ppb," "parts per billion," "parts per trillion." These overlap, and a listener can easily confuse them.

### 19.1 Standardized Spoken Convention

Adopt a single, consistent way to express purity in each chapter:

- Use the **"nines" notation spoken as words** as the primary form: "twelve-nine purity" means twelve nines after the decimal point.
- On first use in each chapter, explain the convention: "Twelve-nine purity means the material is ninety-nine point nine-nine-nine-nine-nine-nine-nine-nine-nine-nine-nine-nine percent pure -- twelve nines after the decimal. In practical terms, this means fewer than one impurity atom per trillion."
- On subsequent uses, the shorthand is sufficient: "twelve-nine purity."
- Do not write out the full percentage string (99.9999999999%) in audio text. The narrator would stumble over the repeated nines.

### 19.2 Parts-Per Notation

- "sub-ppb" becomes "below one part per billion."
- "sub-ppt" becomes "below one part per trillion."
- On first use, contextualize: "below one part per trillion -- imagine a single drop of ink dissolved in twenty Olympic swimming pools."
- Do not alternate between ppb, ppt, and nines notation within the same paragraph. Pick one and stick with it for that passage.

---

## 20. Process Sequences

The source text describes many multi-step manufacturing processes as narrative sequences: the Czochralski crystal growth process, the UPW purification train, the damascene copper interconnect process, the dicing-before-grinding sequence, and the wafer test flow. These are not bullet lists in the source, but they are sequential and the listener must follow the order.

### 20.1 Numbering Spoken Steps

When a process has a clear sequence of three or more steps, use explicit verbal numbering:

Audio:
> "The ultrapure water purification process follows six stages. First, the incoming municipal water undergoes pre-treatment to remove large particles and chlorine. Second, reverse osmosis membranes strip out dissolved salts and organics. Third, electrodeionization removes the remaining ions. Fourth, ultraviolet oxidation breaks down residual organic molecules. Fifth, ion-exchange polishing beds capture any ions that survived the earlier stages. And finally, ultrafiltration membranes remove the last particles down to the nanometer scale."

Rules:
- Use "First... Second... Third..." for up to six steps. Beyond six, consolidate steps into groups.
- State the total number of steps before beginning: "The process follows six stages."
- After the sequence, provide a one-sentence summary of the outcome: "The result is water so pure that its resistivity reaches the theoretical maximum -- a benchmark that no natural water source on earth comes close to."

### 20.2 Spatial Process Descriptions

Some processes describe physical/spatial operations that a print reader can visualize from a diagram but a listener must construct mentally. This includes flip-chip bonding, CoWoS interposer assembly, stealth dicing, and the Czochralski crystal pull.

Rules:
- Use directional language explicitly: "from the top down," "from the bottom up," "flipped over so the circuit side faces downward."
- Anchor the description to a familiar object or orientation before introducing the spatial detail: "Picture the wafer lying flat, circuit side up. Now imagine cutting shallow grooves into that top surface..."
- Avoid describing more than one spatial transformation per sentence. "The wafer is flipped" is one sentence. "Then it is ground from the backside" is the next.

---

## 21. Ratio and Selectivity Notation

The source text uses ratio notation frequently in Chapters 9 and 10 to express etch selectivity, chemical mixtures, and process parameters: "100:1 selectivity," "1:1:5 to 1:2:7," "3:1 to 7:1."

### 21.1 Spoken Equivalents

- "100:1" becomes "one hundred to one."
- "1:1:5" becomes "a mixture of one part ammonium hydroxide, one part hydrogen peroxide, and five parts water."
- "3:1 to 7:1" becomes "at ratios ranging from three-to-one up to seven-to-one."
- "±0.5 microns" becomes "plus or minus half a micrometer."

### 21.2 When to Omit Ratios

Omit ratios when they are not central to the narrative point. If the source lists a cleaning solution's ratio as supporting detail but the main point is what the solution removes, drop the ratio and focus on the function. See Section 17.3 for cleaning solution examples.

---

## 22. Company Name Variants and Rebrandings

Several companies in the dataset have undergone name changes, trade under brand names different from their legal names, or are known by multiple names historically. The source text sometimes introduces all variants at once, which overloads the listener.

### 22.1 Examples in the Source

- "Resonac Holdings, formerly Showa Denko K.K. until its January 2023 renaming"
- "Kioxia Holdings, formerly Toshiba Memory Corporation"
- "Tokyo Seimitsu, trading under the brand name ACCRETECH"
- "Toppan Photomask, renamed Tekscend Photomask in November 2024"
- "DISCO Corporation, originally Dai-Ichi Seitosho (First Grinding Company)"

### 22.2 Conversion Strategy

Use the **current, most-recognized name** as the primary form throughout the audiobook. Mention the former name once, in a subordinate clause, only if it is relevant to the company's history narrative:

Audio:
> "Resonac Holdings -- until recently known as Showa Denko -- is the world's largest semiconductor materials supplier outside of silicon wafers."

Rules:
- Do not introduce the old name, the new name, and the brand name all in the same sentence. Pick the name the listener will encounter again and use that.
- If a company has a brand name that differs from its corporate name (ACCRETECH for Tokyo Seimitsu), mention it once in the company's profile section and then never again. Use the corporate name throughout.
- For companies renamed after the events described in the text (e.g., discussing Toshiba Memory in a historical context), use the name appropriate to the period: "The business was then known as Toshiba Memory. It was later renamed Kioxia."

---

## 23. Historical Timelines

Several chapters -- particularly Chapters 6 (Lithography), 8 (Photoresist), 16 (Demand Side), and 17 (Geopolitics) -- contain compressed timeline passages that list five or more dates and events in rapid succession.

### 23.1 The Problem

Source:
> "In the 1980s, Nikon dominated lithography. By 1990, Nikon held approximately fifty percent of the market. ASML was founded in 1984. Between 2002 and 2008, the immersion transition reshaped the industry. By 2006, ASML was shipping production-quality immersion scanners. The first production-worthy EUV system arrived in 2018-2019. By 2025, hundreds of EUV systems had been shipped."

Seven date references in seven sentences. The listener loses the narrative thread because dates alone do not create a story.

### 23.2 Conversion Strategy

Restructure timelines into **era-based narratives** rather than date-by-date chronologies:

Audio:
> "For decades, Nikon was the undisputed leader in lithography. Through the nineteen-eighties and into the early nineties, the Japanese company held roughly half the global market. But a Dutch startup called ASML, founded in nineteen eighty-four, was quietly gaining ground. The turning point came with immersion lithography in the mid-two-thousands. ASML mastered the new technology faster than its rivals and never looked back. By the time extreme ultraviolet lithography entered production around twenty-nineteen, ASML had become a monopolist. Today, hundreds of EUV systems are installed worldwide -- and every one of them is made by ASML."

Rules:
- Group events into eras: "the early years," "the turning point," "the modern era."
- Use no more than three specific year references per paragraph. Replace others with relative time markers: "a decade later," "within a few years," "by the time..."
- Ensure each date reference is attached to a consequence, not just a fact. "ASML was founded in 1984" is a fact. "A Dutch startup called ASML, founded in nineteen eighty-four, was quietly gaining ground" is a narrative.

### 23.3 Regulatory Timelines (Chapter 17)

The geopolitics chapter contains a three-wave export control timeline (October 2022, October 2023, December 2024). These dates matter for the argument. Treat them as a numbered sequence (see Section 20.1):

Audio:
> "US export controls arrived in three waves. The first, in October twenty-twenty-two, restricted the sale of advanced chipmaking equipment to China. The second, a year later in October twenty-twenty-three, tightened the rules and expanded their scope. The third, in December twenty-twenty-four, went further still, adding new entities to the restricted list and closing loopholes that had allowed some trade to continue."

---

## 24. Scoring and Rating Tables

Chapters 17 and 18 introduce evaluation scoring rubrics (Dimension F geopolitical risk scores, the six-dimension A-F framework) presented as tables with numeric scores and grade-level criteria.

### 24.1 Risk Scoring Tables

Source:
```
| Company | F1 | F2 | F3 | F Total |
|---------|----|----|-----|---------|
| Tokyo Seimitsu | 3 | 4 | 2 | 9 |
| Tokyo Electron | 2 | 3 | 3 | 8 |
```

Audio:
> "Among the five case studies, Tokyo Seimitsu scores highest on geopolitical risk with a total of nine out of fifteen, reflecting its heavy China revenue exposure. Tokyo Electron scores eight, one point lower, owing to its somewhat more diversified customer base."

Rules:
- Do not read the sub-dimension scores mechanically ("F-one: three, F-two: four, F-three: two"). Instead, narrate what the scores mean.
- Focus on the total score and the ranking relative to peers. The sub-dimension breakdown can be summarized narratively: "The high score is driven primarily by its China revenue exposure, which accounts for over thirty percent of sales."
- For scoring rubric definitions, narrate the scale endpoints and midpoint only: "The scale runs from zero to five, where zero means no geopolitical exposure and five means critical dependence on restricted markets."

### 24.2 Scoring Rubric Tables

Source (evaluation criteria table):
```
| Exposure Level | Score | Criteria |
|---------------|-------|----------|
| None | 0 | No China revenue |
| Low | 1–2 | <15% China revenue |
| Moderate | 3 | 15–30% China revenue |
| High | 4–5 | >30% China revenue |
```

Audio:
> "The framework assigns a score from zero to five based on China revenue exposure. Companies with no China revenue score zero. Those with less than fifteen percent score one or two. Moderate exposure, between fifteen and thirty percent, earns a three. And companies deriving more than thirty percent of revenue from China score four or five, placing them in the highest-risk category."

---

## 25. Mega-Tables (Large Reference Tables)

Chapter 3 (Supply Chain Map) and Chapter 16 (Demand Side) contain very large tables -- thirty-seven or more rows -- that serve as reference indexes. The TSMC supplier table in Chapter 16, for example, lists thirty-seven Japanese suppliers grouped by category with chapter cross-references.

### 25.1 Conversion Strategy

Do not attempt to narrate mega-tables row by row. Convert them to a **narrative summary with category highlights**:

Audio:
> "TSMC's supply chain draws on Japanese companies across every stage of the manufacturing process. In wafer materials, it relies on Shin-Etsu and SUMCO. In lithography-related supplies, it sources photoresists from Tokyo Ohka Kogyo and JSR, photomask blanks from HOYA, and UV lamps from Ushio. Its process equipment comes from Tokyo Electron, SCREEN Holdings, Ebara, and Kokusai Electric, among others. And in ultrapure water and specialty chemicals, Organo, Stella Chemifa, and Nippon Sanso are critical vendors. In total, more than three dozen Japanese companies supply TSMC directly -- a concentration that underscores the thesis of this book."

Rules:
- State the total count to convey scale ("more than three dozen").
- Name three to five companies per category, selecting the most important.
- End with a thematic statement linking the table's content back to the chapter or book argument.
- Omit the chapter cross-references from the spoken version; the listener will encounter each company in its dedicated chapter regardless.

---

## 26. Defect Modes and Technical Definition Lists

Chapters 10, 11, and 13 introduce sequences of technical terms -- typically defect modes, process variants, or equipment architectures -- where each term is bolded in print and followed by a definition. Examples include CMP defect modes (dishing, erosion, scratches, corrosion), probe card architectures (cantilever, vertical, MEMS), and cleaning sequences (SC-1, SC-2, SPM, DHF).

### 26.1 The Problem

In print, bold formatting visually separates the term from its definition. In audio, the term and definition blend into undifferentiated prose, and the listener cannot tell where one definition ends and the next begins.

### 26.2 Conversion Strategy

Use an explicit **"term-announcement" pattern**:

Audio:
> "CMP can produce several types of defects, each with a distinct cause. The first is called dishing. Dishing occurs when the center of a wide metal feature is polished lower than its edges, creating a concave surface. The second defect is erosion. Erosion happens when areas with a high density of metal patterns are over-polished, lowering the surrounding dielectric surface. A third concern is scratching, caused by oversized abrasive particles in the slurry."

Rules:
- Introduce each term with "The [ordinal] is called [term]" or "Another is [term]."
- Follow immediately with a one-to-two sentence definition.
- Do not introduce more than four terms in a single passage. If the source has more, split into two passages with a bridging sentence.
- Avoid the print pattern of "[term]: [definition]" where the colon carries the structural weight. In audio, the colon is silent.

---

## 27. Yield Calculations and Mathematical Reasoning

Chapter 13 (Wafer Test) contains compound probability calculations that are central to the argument for known-good-die testing.

### 27.1 The Problem

Source:
> "If the yield of each individual die is ninety percent, the probability that both die in a package are good is only eighty-one percent. At ninety percent individual die yield, an eight-chiplet module has a composite yield of just forty-three percent."

The listener must perform mental multiplication (0.9 x 0.9 = 0.81) to verify the claim. Most will not.

### 27.2 Conversion Strategy

Narrate the intuition, not the arithmetic:

Audio:
> "Here is the problem. If you stack two chips in a single package and each chip has a ninety percent chance of being good, the package only has about an eighty percent chance of working -- because both chips must be functional. The math gets worse quickly. With eight chiplets, the odds of all eight being good drops below fifty percent. And with sixteen layers, as in the latest memory stacks, the composite yield falls to roughly forty-four percent. This is why testing every die before assembly is not optional -- it is an economic necessity."

Rules:
- State the input assumption clearly ("each chip has a ninety percent chance of being good").
- Give the result as a rounded figure.
- Explain the directional trend ("the math gets worse quickly") rather than reciting each calculation.
- End with the practical implication ("this is why testing every die before assembly is not optional").
- Do not use formulas or mathematical notation. No "0.9^8 = 0.43."

---

## 28. Geographic and Subsidiary Cascades

Chapters 8, 10, 12, 15, and 17 contain passages that list a company's international subsidiaries with their locations, served customers, and sometimes founding dates.

### 28.1 The Problem

Source:
> "PILLAR Taiwan Co., Ltd. (with a factory in Kaohsiung) serves TSMC and other Taiwanese fabs. PILLAR Korea Co., Ltd. (Seoul) serves Samsung and SK Hynix. PILLAR Shanghai Co., Ltd. and Pillar Technology Chuzhou serve SMIC and Hua Hong. PILLAR America Inc. (Fremont, California and Houston, Texas) serves Intel and other American fabs. A new Malaysia subsidiary, established in October 2025, positions the company for the growing Southeast Asian semiconductor ecosystem."

Five subsidiaries, seven locations, six customers. The listener hears a cascade of proper nouns with no conceptual anchor.

### 28.2 Conversion Strategy

Lead with the strategic point, then support with selective geography:

Audio:
> "PILLAR has followed its customers around the world. The company operates subsidiaries in Taiwan, South Korea, China, the United States, and -- most recently -- Malaysia. Each subsidiary is positioned near major fab clusters: the Taiwan operation serves TSMC, the Korean subsidiary serves Samsung and SK Hynix, and the American offices serve Intel. This global footprint ensures that PILLAR can provide local support wherever chips are manufactured."

Rules:
- State the strategic purpose of the international presence before listing locations.
- Name countries, not cities, unless the city is essential to the argument (e.g., "TSMC's Arizona fab").
- Match each region to its most important customer -- one per region, not an exhaustive list.
- Omit subsidiary legal entity names entirely. "PILLAR Taiwan Co., Ltd." becomes "the Taiwan operation."
- Omit establishment dates for subsidiaries unless they support a narrative about expansion timing.

---

## 29. Hierarchical Category Structures

Chapters 3 (Supply Chain Map) and 12 (Fab Infrastructure) organize content into hierarchical categories -- countries subdivided into segments, or infrastructure functions subdivided into sub-categories. In print, this hierarchy is conveyed through indentation, bolded category headers, and nested lists. In audio, hierarchy is invisible.

### 29.1 Conversion Strategy

Convert hierarchical structures into a **"tour guide" narrative** that announces each level explicitly:

Audio:
> "The companies that support a fab's infrastructure fall into five broad categories. The first is automation and handling -- the systems that move wafers between tools. The second is precision parts and components -- the machined chambers, ceramic chucks, and metal fittings that go inside the tools themselves. Third is chemical distribution -- the sourcing and delivery of the photoresists, etchants, and solvents that the process tools consume. Fourth is test subsystems -- the probe cards, tester boards, and mechanical components that support electrical testing. And fifth is metrology and inspection -- the microscopes and measurement instruments that verify every step of the process."

Rules:
- State the total number of categories before beginning: "five broad categories."
- Name each category with an ordinal ("The first is... The second is...").
- Give each category a one-sentence description.
- After the overview, devote a separate paragraph or passage to each category. Do not try to list all companies under all categories in the overview itself.

---

## 30. Chapter Difficulty and Rewrite Intensity

Not all chapters require the same degree of transformation. The following ranking, from most to least intensive rewrite effort, should guide the agent's time allocation and level of scrutiny.

### Tier 1 -- Heavy Rewrite (highest density of audio-unfriendly patterns)

- **Chapter 3 (Supply Chain Map):** Largest number of tables, most extensive company rosters (110 nodes), highest ticker-symbol density, multiple country-grouped lists.
- **Chapter 5 (UPW & Gases):** Highest chemical formula density, purity notation complexity, specification-heavy passages.
- **Chapter 8 (Photoresist):** Four generations of resist chemistry, PAG and polymer acronym clustering, chemical cascade passages.
- **Chapter 12 (Fab Infrastructure):** Eleven companies introduced in rapid succession, category-hierarchy structure, dense supply chain edge passages.
- **Chapter 16 (Demand Side):** Seven company profiles with repetitive financial table structures, the 37-row TSMC supplier mega-table, revenue figures in multiple currencies.

### Tier 2 -- Moderate Rewrite

- **Chapter 6 (Lithography):** Wavelength comparison sequences (436nm to 13.5nm), historical timeline density, cost-per-wafer comparisons.
- **Chapter 9 (Deposition):** Acronym clusters (CVD variants), chemical formula passages, multiple company profiles with similar structure.
- **Chapter 10 (Etching & Cleaning):** Chemical formula cascades, ratio notation, cleaning sequence protocols.
- **Chapter 11 (CMP):** Multi-material slurry specifications, defect mode definitions, process sequence descriptions.
- **Chapter 13 (Wafer Test):** Yield calculations, probe card architecture descriptions, ATE specification passages.
- **Chapter 15 (Advanced Packaging):** HBM stack descriptions, bandwidth specifications, spatial assembly process descriptions.
- **Chapter 17 (Geopolitics):** Regulatory timeline, risk scoring rubrics, company case studies with export control context.

### Tier 3 -- Lighter Rewrite

- **Chapter 4 (Silicon Wafers):** Fewer companies, well-structured narrative, moderate number of tables.
- **Chapter 7 (Photomasks):** Smaller company count, clear narrative arc, manageable technical density.
- **Chapter 14 (Dicing):** Only two primary companies, straightforward process descriptions.
- **Chapters 1 and 2:** Already narrative-heavy with fewer tables and lists; primarily need formatting cleanup and sentence-length adjustments.
- **Chapter 18 (Investment Framework):** Analytical rather than data-dense; primarily needs scoring table conversion.

---

## 31. Monotony Prevention in Repetitive Structures

The source text profiles sixty-two Japanese companies using an identical template: header, founded/HQ/market-cap line, narrative paragraphs, financial table, investment perspective. When a single chapter profiles five to eight companies in succession (Chapters 5, 8, 9, 12, 15, 16), the repetition -- tolerable in print where the reader can skim -- becomes monotonous in audio.

### 31.1 Vary the Opening

Do not begin every company profile with "Let us now turn to [Company]." Rotate among several patterns:

- "The next company in this story is..."
- "A very different business enters the picture here."
- "[Company] occupies a unique position in this supply chain."
- "We now come to the smallest company in this chapter -- but one of the most strategically important."
- "If [previous company] represents the high-volume end of this market, [next company] represents the opposite extreme."

### 31.2 Vary the Financial Summary

Do not recite the same five metrics in the same order for every company. Instead:
- For one company, lead with valuation: "The stock trades at a price-to-earnings ratio of..."
- For the next, lead with a standout metric: "What makes this company remarkable from an investment standpoint is its operating margin -- above forty percent..."
- For another, use a peer comparison: "Unlike the other companies we have examined in this chapter, this one trades at a significant discount to its peers..."
- Omit financial metrics entirely for companies where the metrics are unremarkable or where the source text does not interpret them.

### 31.3 Vary the Transition Out

Do not end every company section with "Now let us turn to the next company." Instead:
- Connect to the next company thematically: "If Ebara builds the CMP machines, someone must supply the slurry that goes inside them. That company is Fujimi."
- Connect to the supply chain: "Ebara's machines sit at the center of the planarization step. But the performance of those machines depends entirely on the quality of the abrasive slurry -- which brings us to..."
- Occasionally, skip the transition entirely and let a paragraph break serve.

---

This concludes the audiobook rewrite guidelines. Adhere to these rules consistently across all chapters and appendices to produce a manuscript that delivers the same intellectual depth and investment insight as the print edition, through a medium where every word must earn its place in the listener's attention.
