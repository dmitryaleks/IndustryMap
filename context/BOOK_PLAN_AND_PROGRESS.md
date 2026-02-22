# Silicon Foundations — Japan's Hidden Dominance in the Semiconductor Supply Chain

## Book Plan & Progress Tracker

**Version:** 1.0
**Created:** 2026-02-22
**Last Updated:** 2026-02-22

---

## Overview

This book explains how the semiconductor supply chain works and maps key Japanese companies to each stage of the chip manufacturing process. It targets investors and technology enthusiasts who want to understand the fundamentals of the industry — both the technical details and the economics.

The book draws on the IndustryMap project dataset:
- **110 companies** (62 deeply-researched Japanese, 48 global context)
- **321 supply chain edges** (263 supplier, 42 competitor, 4 partner, 12 ecosystem)
- **74 scored companies** with a 6-dimension evaluation framework (A–F, 0–100 scale)
- **12+ investment theses** for the highest-conviction names

**Style:** Educational, with focus on technology, economics, and finance. See `context/BOOK_GUIDELINE.md` for detailed style guidance.

---

## Data Sources

| File | Description |
|------|-------------|
| `data/graph.json` | 110 nodes, 321 edges — the full supply chain graph |
| `data/companies/CMP-*.json` | Individual company detail files (110 total) |
| `evaluation_progress.json` | 74 scored companies, dimension breakdowns, investment theses |
| `context/EVALUATION_FRAMEWORK.md` | Scoring methodology (dimensions A–F) |
| `context/BOOK_GUIDELINE.md` | Style guide for the book |
| `data/database.json` | Legacy company database (supplementary) |

---

## Book Structure

### PART I: FOUNDATIONS (Chapters 1–3)

| Ch | File | Title | Scope | Key CMP Files |
|----|------|-------|-------|---------------|
| 1 | `ch01-introduction.md` | Why Japan Matters | Overview of Japan's hidden dominance: 62 companies controlling critical chokepoints across the semiconductor supply chain. Introduce the book's thesis — that Japan's position is structural, not incidental. Use graph.json statistics to illustrate the density and centrality of Japanese nodes. | graph.json overview, all 110 nodes |
| 2 | `ch02-process-flow.md` | How a Chip Is Made | A technical primer on the chip manufacturing process from raw silicon to packaged IC. No company-specific content — purely educational. Introduces the ~20 major process steps that subsequent chapters map companies to. Establishes vocabulary (lithography, deposition, etch, CMP, dicing, etc.). | None (technical reference) |
| 3 | `ch03-supply-chain-map.md` | The Supply Chain Map | Present the full supply chain graph as a narrative. Walk through the graph structure: nodes by country, edges by type. Explain supplier/competitor/partner/ecosystem relationships. Highlight Japan's centrality metrics. This chapter is the "map legend" for the rest of the book. | graph.json (all 110 nodes, 321 edges) |

### PART II: THE WAFER (Chapters 4–5)

| Ch | File | Title | Scope | Key CMP Files |
|----|------|-------|-------|---------------|
| 4 | `ch04-silicon-wafers.md` | Silicon Wafers — The Foundation of Every Chip | The Czochralski process, 300mm wafer manufacturing, and the Shin-Etsu / SUMCO duopoly (>50% global share). Cover Ferrotec's silicon crystal growth equipment and consumables. Explain why wafer quality is the ultimate constraint on yield. | CMP-0024 (Shin-Etsu), CMP-0025 (SUMCO), CMP-0009 (Ferrotec) |
| 5 | `ch05-upw-and-gases.md` | Ultrapure Water & Specialty Gases | UPW systems (Organo's TSMC monopoly, Nomura Micro Science), specialty gases (Nippon Sanso, Kanto Denka, Stella Chemifa's 12-nine HF). Explain why sub-ppb purity is non-negotiable at advanced nodes. | CMP-0052 (Organo), CMP-0053 (Nomura Micro Science), CMP-0032 (Nippon Sanso), CMP-0045 (Kanto Denka), CMP-0044 (Stella Chemifa) |

### PART III: PATTERNING (Chapters 6–8)

| Ch | File | Title | Scope | Key CMP Files |
|----|------|-------|-------|---------------|
| 6 | `ch06-lithography.md` | Lithography — Printing the Circuit | ASML's EUV monopoly and why Japan still matters: Nikon and Canon in mature nodes (i-line, KrF), Ushio's UV lamp monopoly (75% share), Canon's nanoimprint push. Explain DUV vs EUV physics, overlay accuracy, and throughput economics. | CMP-0026 (ASML), CMP-0050 (Nikon), CMP-0051 (Canon), CMP-0061 (Ushio) |
| 7 | `ch07-photomasks.md` | Photomasks & Inspection | HOYA's EUV blank monopoly, Toppan and DNP as photomask producers, Lasertec's sole-supplier position in EUV mask inspection. Explain how a single mask defect can destroy millions of chips. | CMP-0015 (HOYA), CMP-0006 (Lasertec), CMP-0047 (Toppan), CMP-0049 (DNP) |
| 8 | `ch08-photoresist.md` | Photoresist & Chemicals | TOK and JSR as resist formulators, Gun Ei Chemical and Maruzen Petrochemical as upstream resin monopolists, Toyo Gosei's PAG specialty, Sumitomo Chemical, FUJIFILM's materials platform, Nagase as distributor. Explain the resist-developer-rinse chemical stack. | CMP-0033 (TOK), CMP-0034 (JSR), CMP-0038 (Gun Ei Chemical), CMP-0010 (Toyo Gosei), CMP-0035 (Maruzen Petrochem), CMP-0046 (Sumitomo Chemical), CMP-0040 (FUJIFILM), CMP-0058 (Nagase) |

### PART IV: BUILDING THE CHIP (Chapters 9–11)

| Ch | File | Title | Scope | Key CMP Files |
|----|------|-------|-------|---------------|
| 9 | `ch09-deposition.md` | Deposition — Layer by Layer | Tokyo Electron's coater/developer and CVD dominance, Kokusai Electric's batch deposition niche, Shibaura Mechatronics and Samco in plasma processing, Tazmo in coating. Explain CVD, PVD, ALD, and epitaxy. | CMP-0004 (TEL), CMP-0011 (Kokusai Electric), CMP-0060 (Samco), CMP-0059 (Shibaura Mechatronics), CMP-0062 (Tazmo) |
| 10 | `ch10-etch-and-clean.md` | Etching & Cleaning | SCREEN Holdings' wet cleaning dominance, PILLAR's fluororesin fitting monopoly, CKD's pneumatic valves, Horiba's gas analysis. Explain wet vs dry etch, selectivity, and contamination control. | CMP-0003 (SCREEN), CMP-0042 (PILLAR), CMP-0043 (CKD), CMP-0012 (Horiba) |
| 11 | `ch11-cmp.md` | CMP — Planarization | Ebara's CMP systems, Fujimi and Fuso Chemical's slurry duopoly, Resonac's multi-material platform, FUJIFILM's CMP slurry, Tocalo's thermal spray coatings, Tokyo Seimitsu's CMP equipment. Explain why angstrom-level flatness matters for multi-patterning. | CMP-0036 (Ebara), CMP-0007 (Fujimi), CMP-0013 (Fuso Chemical), CMP-0008 (Resonac), CMP-0040 (FUJIFILM), CMP-0031 (Tocalo), CMP-0001 (Tokyo Seimitsu) |

### PART V: INFRASTRUCTURE (Chapter 12)

| Ch | File | Title | Scope | Key CMP Files |
|----|------|-------|-------|---------------|
| 12 | `ch12-fab-infrastructure.md` | The Factory Behind the Factory | Daifuku's AMHS/OHT systems, Rorze's wafer transfer robots, Naigai Tech and Marumae as precision parts suppliers, NGK Insulators' ceramic electrostatic chucks, Kyocera's semiconductor components, Niterra's IC package substrates, Nagase's chemical distribution, Aval Data and NHK Spring's test subsystems. | CMP-0056 (Daifuku), CMP-0041 (Rorze), CMP-0029 (Naigai Tech), CMP-0030 (Marumae), CMP-0037 (NGK Insulators), CMP-0027 (Kyocera), CMP-0039 (Niterra), CMP-0058 (Nagase), CMP-0054 (Aval Data), CMP-0055 (NHK Spring) |

### PART VI: BACK-END (Chapters 13–15)

| Ch | File | Title | Scope | Key CMP Files |
|----|------|-------|-------|---------------|
| 13 | `ch13-wafer-test.md` | Wafer Test & Probing | Tokyo Seimitsu and Advantest's prober/tester ecosystem, Aval Data's tester boards, NHK Spring's probe card springs. Explain wafer-level testing, known-good-die, and the economics of test. | CMP-0001 (Tokyo Seimitsu), CMP-0005 (Advantest), CMP-0054 (Aval Data), CMP-0055 (NHK Spring) |
| 14 | `ch14-dicing.md` | Dicing & Singulation | DISCO's 80%+ global share in dicing saws, Tokyo Seimitsu as the #2 player, and their competitive dynamics. Explain blade vs laser dicing, stealth dicing, and why singulation quality determines packaging yield. | CMP-0002 (DISCO), CMP-0001 (Tokyo Seimitsu) |
| 15 | `ch15-advanced-packaging.md` | Advanced Packaging — The New Frontier | Ibiden's FC-BGA substrate dominance (50%+ of NVIDIA AI server substrates), Resonac's die-attach and encapsulation, MEC Company's copper surface treatment, Toppan and Niterra in packaging, Hanmi Semiconductor's TC bonders. Explain chiplet architectures, HBM, CoWoS, and why packaging is the new lithography. | CMP-0048 (Ibiden), CMP-0008 (Resonac), CMP-0057 (MEC Company), CMP-0047 (Toppan), CMP-0039 (Niterra), CMP-0072 (Hanmi Semiconductor) |

### PART VII: ECOSYSTEM (Chapters 16–17)

| Ch | File | Title | Scope | Key CMP Files |
|----|------|-------|-------|---------------|
| 16 | `ch16-demand-side.md` | Foundries, IDMs & the AI Boom | TSMC, Samsung, Intel, SK Hynix, Micron as the demand engines. Kioxia and NVIDIA. How AI capex cycles ripple backward through the Japanese supply chain. Explain foundry vs IDM vs fabless business models. | CMP-0017 (TSMC), CMP-0018 (Samsung), CMP-0019 (Intel), CMP-0020 (SK Hynix), CMP-0021 (Micron), CMP-0014 (Kioxia), CMP-0028 (NVIDIA) |
| 17 | `ch17-geopolitics.md` | Geopolitics & Supply Chain Risk | Japan's strategic position in US-China tech rivalry, export control implications, China's domestic substitution efforts vs Japan's entrenched positions. Use Tokyo Seimitsu, TEL, SCREEN, Ferrotec, Organo as case studies of companies navigating geopolitical crosscurrents. | CMP-0001 (Tokyo Seimitsu), CMP-0004 (TEL), CMP-0003 (SCREEN), CMP-0009 (Ferrotec), CMP-0052 (Organo) |

### PART VIII: CONCLUSION & APPENDICES (Chapter 18 + Appendices A–E)

| Ch | File | Title | Scope | Key CMP Files |
|----|------|-------|-------|---------------|
| 18 | `ch18-investment-framework.md` | Investment Framework — Finding Value in the Supply Chain | Present the 6-dimension evaluation framework (A–F). Walk through peer group medians (G1–G4). Highlight the top-10 most undervalued names with full investment thesis summaries. Discuss how to use the scoring system for portfolio construction. | evaluation_progress.json (all 74 scored companies) |
| A | `appendix-a-company-cards.md` | Japanese Company Cards | One-page profiles for all 62 Japanese companies (CMP-0001 through CMP-0062): company name, ticker, industry, description, key financials, suppliers, clients, evaluation score, investment thesis summary (if available). | CMP-0001 through CMP-0062 |
| B | `appendix-b-global-ecosystem.md` | Global Ecosystem Reference | Profiles for all 48 non-Japanese companies (CMP-0063 through CMP-0110): name, country, industry, role in the supply chain, key edges to Japanese companies. | CMP-0063 through CMP-0110 |
| C | `appendix-c-edge-list.md` | Supply Chain Edge List | Complete tabular listing of all 321 edges from graph.json: source, target, type, label. Grouped by edge type. | graph.json |
| D | `appendix-d-evaluation-methodology.md` | Evaluation Scoring Methodology | Full reproduction of the 6-dimension framework: dimension definitions, point allocations, rubrics, peer group medians, formulas. Reference to `EVALUATION_FRAMEWORK.md`. | EVALUATION_FRAMEWORK.md |
| E | `appendix-e-glossary.md` | Glossary of Semiconductor Terms | Definitions for technical terms used throughout the book: lithography, EUV, CMP, CVD, PVD, ALD, OSAT, HBM, CoWoS, etc. | N/A |

---

## Japanese Company Coverage Map (CMP-0001 through CMP-0062)

Every Japanese company must appear in at least one process chapter (Ch 4–17) plus Appendix A.

| CMP ID | Company | Primary Chapter(s) | Also Appears In |
|--------|---------|-------------------|-----------------|
| CMP-0001 | Tokyo Seimitsu | Ch 11, Ch 13, Ch 14 | Ch 17, App A |
| CMP-0002 | DISCO | Ch 14 | App A |
| CMP-0003 | SCREEN Holdings | Ch 10 | Ch 17, App A |
| CMP-0004 | Tokyo Electron | Ch 9 | Ch 17, App A |
| CMP-0005 | Advantest | Ch 13 | App A |
| CMP-0006 | Lasertec | Ch 7 | App A |
| CMP-0007 | Fujimi | Ch 11 | App A |
| CMP-0008 | Resonac Holdings | Ch 11, Ch 15 | App A |
| CMP-0009 | Ferrotec Holdings | Ch 4 | Ch 17, App A |
| CMP-0010 | Toyo Gosei | Ch 8 | App A |
| CMP-0011 | Kokusai Electric | Ch 9 | App A |
| CMP-0012 | Horiba | Ch 10 | App A |
| CMP-0013 | Fuso Chemical | Ch 11 | App A |
| CMP-0014 | Kioxia Holdings | Ch 16 | App A |
| CMP-0015 | HOYA | Ch 7 | App A |
| CMP-0016 | Olympus | Ch 12 | App A |
| CMP-0017 | TSMC | Ch 16 | Ch 3 |
| CMP-0018 | Samsung Electronics | Ch 16 | Ch 3 |
| CMP-0019 | Intel | Ch 16 | Ch 3 |
| CMP-0020 | SK Hynix | Ch 16 | Ch 3 |
| CMP-0021 | Micron | Ch 16 | Ch 3 |
| CMP-0022 | Apple | Ch 16 | — |
| CMP-0023 | Western Digital | Ch 16 | — |
| CMP-0024 | Shin-Etsu Chemical | Ch 4 | App A |
| CMP-0025 | SUMCO | Ch 4 | App A |
| CMP-0026 | ASML | Ch 6 | Ch 3 |
| CMP-0027 | Kyocera | Ch 12 | App A |
| CMP-0028 | NVIDIA | Ch 16 | Ch 3 |
| CMP-0029 | Naigai Tech | Ch 12 | App A |
| CMP-0030 | Marumae | Ch 12 | App A |
| CMP-0031 | Tocalo | Ch 11 | App A |
| CMP-0032 | Nippon Sanso | Ch 5 | App A |
| CMP-0033 | Tokyo Ohka Kogyo | Ch 8 | App A |
| CMP-0034 | JSR | Ch 8 | App A |
| CMP-0035 | Maruzen Petrochemical | Ch 8 | App A |
| CMP-0036 | Ebara | Ch 11 | App A |
| CMP-0037 | NGK Insulators | Ch 12 | App A |
| CMP-0038 | Gun Ei Chemical | Ch 8 | App A |
| CMP-0039 | Niterra | Ch 12, Ch 15 | App A |
| CMP-0040 | FUJIFILM Holdings | Ch 8, Ch 11 | App A |
| CMP-0041 | Rorze | Ch 12 | App A |
| CMP-0042 | PILLAR | Ch 10 | App A |
| CMP-0043 | CKD | Ch 10 | App A |
| CMP-0044 | Stella Chemifa | Ch 5 | App A |
| CMP-0045 | Kanto Denka Kogyo | Ch 5 | App A |
| CMP-0046 | Sumitomo Chemical | Ch 8 | App A |
| CMP-0047 | Toppan Holdings | Ch 7, Ch 15 | App A |
| CMP-0048 | Ibiden | Ch 15 | App A |
| CMP-0049 | Dai Nippon Printing | Ch 7 | App A |
| CMP-0050 | Nikon | Ch 6 | App A |
| CMP-0051 | Canon | Ch 6 | App A |
| CMP-0052 | Organo | Ch 5 | Ch 17, App A |
| CMP-0053 | Nomura Micro Science | Ch 5 | App A |
| CMP-0054 | Aval Data | Ch 12, Ch 13 | App A |
| CMP-0055 | NHK Spring | Ch 12, Ch 13 | App A |
| CMP-0056 | Daifuku | Ch 12 | App A |
| CMP-0057 | MEC Company | Ch 15 | App A |
| CMP-0058 | Nagase | Ch 8, Ch 12 | App A |
| CMP-0059 | Shibaura Mechatronics | Ch 9 | App A |
| CMP-0060 | Samco | Ch 9 | App A |
| CMP-0061 | Ushio | Ch 6 | App A |
| CMP-0062 | Tazmo | Ch 9 | App A |

**Verification:** All 62 Japanese companies (CMP-0001 through CMP-0062) are mapped to at least one process chapter plus Appendix A. Olympus (CMP-0016) appears in Ch 12 (fab infrastructure — precision measurement / microscopy for process control).

---

## Chapter Template

Every chapter follows this standard Markdown structure:

```markdown
# Chapter N: [Title]

> [One-sentence chapter thesis — what the reader will learn]

## Introduction
[2-3 paragraphs setting the stage: why this process step matters,
 what would happen if it failed, and how Japan fits in]

## [Technical Section: The Process]
[Explain the relevant manufacturing step(s) at a level accessible
 to a motivated non-engineer. Use analogies. Include key numbers
 (e.g., "12-nine purity means fewer than 1 impurity atom per
 trillion"). Subsections as needed.]

## [Company Profiles]
[For each key company in this chapter:]

### [Company Name] ([Ticker]) — [One-line role description]

**Founded:** [year] | **HQ:** [city] | **Market Cap:** [¥ or note if private/delisted]

[2-4 paragraphs covering:]
- Brief history and evolution
- Key products/technologies and global market share
- Position in the supply chain (who supplies them, who they supply)
- Competitive dynamics and moat characteristics

**Key Financials** (where available):
| Metric | Value |
|--------|-------|
| PER | [x] |
| PBR | [x] |
| Revenue Growth | [x%] |
| Operating Margin | [x%] |
| Foreign Ownership | [x%] |

[If an investment thesis exists in evaluation_progress.json, include
 a "Investment Perspective" subsection summarizing it.]

## Competitive Landscape
[Map out competitor relationships from graph.json edges.
 Discuss market share dynamics and substitution risks.]

## Supply Chain Connections
[Describe the supplier and client edges relevant to this chapter.
 Reference upstream chapters (who feeds into this step) and
 downstream chapters (who depends on this step's output).]

## Key Takeaways
[3-5 bullet points summarizing the chapter's main insights]

---
*Data sources: [list CMP files referenced]*
```

---

## Agent Instructions for Chapter Generation

### Before Generating Any Chapter

1. **Read this file** (`context/BOOK_PLAN_AND_PROGRESS.md`) to understand the full book structure and identify dependencies.
2. **Read the style guide** (`context/BOOK_GUIDELINE.md`) for tone and audience guidance.
3. **Check the progress table** below to confirm the chapter is PENDING (not already generated).

### Generating a Chapter

1. **Read all CMP files** listed in the chapter's "Key CMP Files" column.
2. **Read graph.json** edges relevant to those companies (filter by source/target matching key CMP IDs).
3. **Read evaluation_progress.json** for scored companies in the chapter — extract scores, dimension breakdowns, and investment theses.
4. **Follow the Chapter Template** above. Adapt section headings to fit the chapter's content naturally, but maintain the overall structure.
5. **Cross-reference** with adjacent chapters to ensure consistent terminology and avoid redundant explanations.
6. **Write the chapter** to `book/[filename]` as specified in the structure table.

### After Generating a Chapter

1. **Update the progress table** below: change status from `PENDING` to `DONE` and record the date and approximate word count.
2. **Log the session** in the Session Log section below.

### Quality Standards

- Target **3,000–6,000 words** per process chapter (Ch 4–17).
- Target **5,000–8,000 words** for Ch 1, Ch 3, Ch 18 (overview/capstone chapters).
- Target **1,500–3,000 words** for Ch 2 (technical primer, no company content).
- Appendix A: ~200–400 words per company card (62 companies = ~15,000–25,000 words total).
- Appendix B: ~100–200 words per company (48 companies = ~5,000–10,000 words total).
- Appendix C: Primarily tabular — all 321 edges.
- Appendix D: Structured methodology reference (~3,000–5,000 words).
- Appendix E: Alphabetical glossary (~100–200 terms, ~2,000–4,000 words).
- All financial figures in JPY unless otherwise noted.
- Use graph.json edge labels for supply chain descriptions.
- Cite CMP file IDs in data source footers.

---

## Generation Phases

Chapters are grouped by dependency. Within each phase, all chapters can be generated in parallel.

| Phase | Chapters | Dependencies | Notes |
|-------|----------|-------------|-------|
| **A** | Ch 01, Ch 02, Ch 03 | None | Foundational — sets vocabulary and framing for all subsequent chapters |
| **B** | Ch 04, Ch 05, Ch 06, Ch 07, Ch 08, Ch 09, Ch 10, Ch 11, Ch 12 | Phase A complete | Process flow chapters — each covers one manufacturing step. All parallelizable. |
| **C** | Ch 13, Ch 14, Ch 15 | Phase A complete | Back-end chapters — parallelizable after Phase A |
| **D** | Ch 16, Ch 17 | Phase A complete | Context/ecosystem chapters — can run after Phase A, but benefit from B/C for cross-references |
| **E** | Ch 18 | Phases A–D complete | Capstone investment chapter — references all prior chapters and all 74 scored companies |
| **F** | App A, App B, App C, App D, App E | None (fully independent) | Appendices can be generated at any time, in any order |

---

## Progress Tracking

| # | Deliverable | File | Status | Date | Words | Notes |
|---|-------------|------|--------|------|-------|-------|
| 1 | Ch 01 — Why Japan Matters | `book/ch01-introduction.md` | DONE | 2026-02-22 | ~5,850 | Phase A |
| 2 | Ch 02 — How a Chip Is Made | `book/ch02-process-flow.md` | DONE | 2026-02-22 | ~4,850 | Phase A |
| 3 | Ch 03 — The Supply Chain Map | `book/ch03-supply-chain-map.md` | DONE | 2026-02-22 | ~7,100 | Phase A |
| 4 | Ch 04 — Silicon Wafers | `book/ch04-silicon-wafers.md` | DONE | 2026-02-22 | ~6,716 | Phase B |
| 5 | Ch 05 — UPW & Gases | `book/ch05-upw-and-gases.md` | DONE | 2026-02-22 | ~7,804 | Phase B |
| 6 | Ch 06 — Lithography | `book/ch06-lithography.md` | DONE | 2026-02-22 | ~6,740 | Phase B |
| 7 | Ch 07 — Photomasks & Inspection | `book/ch07-photomasks.md` | DONE | 2026-02-22 | ~7,136 | Phase B |
| 8 | Ch 08 — Photoresist & Chemicals | `book/ch08-photoresist.md` | DONE | 2026-02-22 | ~7,472 | Phase B |
| 9 | Ch 09 — Deposition | `book/ch09-deposition.md` | DONE | 2026-02-22 | ~7,217 | Phase B |
| 10 | Ch 10 — Etching & Cleaning | `book/ch10-etch-and-clean.md` | DONE | 2026-02-22 | ~8,034 | Phase B |
| 11 | Ch 11 — CMP Planarization | `book/ch11-cmp.md` | DONE | 2026-02-22 | ~7,233 | Phase B |
| 12 | Ch 12 — Fab Infrastructure | `book/ch12-fab-infrastructure.md` | DONE | 2026-02-22 | ~7,353 | Phase B |
| 13 | Ch 13 — Wafer Test & Probing | `book/ch13-wafer-test.md` | DONE | 2026-02-22 | ~7,444 | Phase C |
| 14 | Ch 14 — Dicing & Singulation | `book/ch14-dicing.md` | DONE | 2026-02-22 | ~6,942 | Phase C |
| 15 | Ch 15 — Advanced Packaging | `book/ch15-advanced-packaging.md` | DONE | 2026-02-22 | ~6,851 | Phase C |
| 16 | Ch 16 — Foundries, IDMs & AI Boom | `book/ch16-demand-side.md` | DONE | 2026-02-22 | ~9,390 | Phase D |
| 17 | Ch 17 — Geopolitics & Risk | `book/ch17-geopolitics.md` | DONE | 2026-02-22 | ~6,647 | Phase D |
| 18 | Ch 18 — Investment Framework | `book/ch18-investment-framework.md` | DONE | 2026-02-22 | ~7,800 | Phase E |
| 19 | Appendix A — JP Company Cards | `book/appendix-a-company-cards.md` | PENDING | — | — | Phase F (needs relaunch) |
| 20 | Appendix B — Global Ecosystem | `book/appendix-b-global-ecosystem.md` | DONE | 2026-02-22 | ~5,783 | Phase F |
| 21 | Appendix C — Edge List | `book/appendix-c-edge-list.md` | DONE | 2026-02-22 | ~5,742 | Phase F |
| 22 | Appendix D — Evaluation Methodology | `book/appendix-d-evaluation-methodology.md` | DONE | 2026-02-22 | ~8,252 | Phase F |
| 23 | Appendix E — Glossary | `book/appendix-e-glossary.md` | DONE | 2026-02-22 | ~7,579 | Phase F |

**Summary:** 22 / 23 deliverables complete

---

## Session Log

Record each generation session here for continuity across sessions.

| Session | Date | Deliverables Completed | Notes |
|---------|------|----------------------|-------|
| 0 | 2026-02-22 | Plan file created | Initial plan written and verified. `book/` directory created. |
| 1 | 2026-02-22 | Ch 02 — How a Chip Is Made | Technical primer chapter. ~2,900 words. No company data referenced. Covers full process flow from sand to packaged IC. |
| 2 | 2026-02-22 | Ch 01 — Why Japan Matters | Introduction chapter. ~6,800 words. Covers hidden dominance thesis, 10 monopoly/duopoly examples, investor thesis, historical context (VLSI), AI inflection, book roadmap. Data from graph.json, 12 CMP files, evaluation_progress.json. |
| 3 | 2026-02-22 | Ch 03 — The Supply Chain Map | Graph-as-narrative chapter. ~7,100 words. Full 110-node/321-edge analysis. Nodes by country (8 countries), edge types explained with examples, Japan centrality analysis (86% of supplier edges from JP), TSMC/Samsung dependency tables, top-15 most-connected nodes, top-10 suppliers, five chokepoint categories, process-step coverage matrix, book navigation guide. Data from graph.json, CMP-0001, CMP-0002, CMP-0004, CMP-0006, CMP-0017, CMP-0018, CMP-0042. |
| 4 | 2026-02-22 | Ch 04 — Silicon Wafers | First Phase B process chapter. ~5,200 words. Covers Czochralski process physics, 300mm wafer specs, wafer quality as yield constraint, Shin-Etsu/SUMCO duopoly profiles with full financials, Ferrotec crystal growth enabler profile, competitive landscape (5-company oligopoly table), 10 supply chain edges to major chipmakers, AI demand inflection, geopolitical dimension. Investment perspectives for Shin-Etsu (score 57.5) and SUMCO (score 49.0). Data from CMP-0024, CMP-0025, CMP-0009, graph.json, evaluation_progress.json. |
| 5 | 2026-02-22 | Ch 06 — Lithography | Phase B patterning chapter. ~6,700 words. Covers wavelength physics (436nm i-line through 13.5nm EUV), Rayleigh criterion, immersion lithography, multi-patterning, EUV source physics (tin plasma). Nikon/Canon vs ASML competitive history (VLSI era through EUV lockout). Four company profiles: ASML (EUV monopoly, score 54.8), Nikon (fallen champion, score 43.5), Canon (NIL optionality, score 65.0, rank #5 thesis), Ushio (75% UV lamp monopoly, score 37.6). Competitive landscape (leading-edge monopoly vs mature-node oligopoly). Supply chain connections to Chapters 7-10. Throughput economics section (cost per wafer layer). Data from CMP-0026, CMP-0050, CMP-0051, CMP-0061, graph.json, evaluation_progress.json. |
| 6 | 2026-02-22 | Ch 05 — UPW & Gases | Phase B water/gas chapter. ~5,600 words. Covers UPW purification science (RO, EDI, UV oxidation, ion exchange polishing), specialty gas categories (etch, deposition, doping, cleaning), HF purity ladder (twelve-nine = 99.9999999999%). Five company profiles: Organo (TSMC 100% advanced-node UPW, score 60.0, full investment thesis), Nomura Micro Science (Korean market specialist, score 44.2), Nippon Sanso (Japan's #1 industrial gas, score 38.8), Kanto Denka Kogyo (15+ fluorine gases, score 49.0), Stella Chemifa (12-nine HF duopoly, score 60.5, full investment thesis). Competitive landscape: Japanese UPW oligopoly (80%+ share), Ecolab/Ovivo 2025 acquisition, Chinese EG-HF threat. 20+ supply chain edges mapped. Data from CMP-0052, CMP-0053, CMP-0032, CMP-0045, CMP-0044, graph.json, evaluation_progress.json. |
| 7 | 2026-02-22 | Ch 07 — Photomasks & Inspection | Phase B patterning chapter. ~5,400 words. Photomask anatomy, EUV multilayer blanks, defect types, actinic inspection. HOYA (75%+ EUV blank monopoly), Lasertec (sole EUV inspection, perfect B=25/25, investment thesis), TOPPAN (merchant mask leader, IBM partnership), DNP (mask + nanoimprint, Y300B capex). HOYA-Lasertec-ASML ecosystem triangle. Data from CMP-0015, CMP-0006, CMP-0047, CMP-0049, CMP-0026, graph.json, evaluation_progress.json. |
| 8 | 2026-02-22 | Ch 08 — Photoresist & Chemicals | Phase B patterning chapter. ~5,800 words. Most companies of any chapter (8). Organized by supply chain position: upstream (Gun Ei, Maruzen) -> formulators (TOK, JSR, Sumitomo, FUJIFILM) -> specialty (Toyo Gosei PAGs) -> distribution (Nagase). Technical section: novolac/DNQ (g/i-line), chemically amplified resists (KrF/ArF), metal-oxide EUV resists, PAG mechanism, developer/rinse stack, pattern collapse, RLS trade-off. Gun Ei Chemical featured as book's #1 thesis (78.9/100). Toyo Gosei (62.4, #6) and JSR/JIC acquisition covered. 15+ supply chain edges across 4 tiers. Data from CMP-0033, CMP-0034, CMP-0038, CMP-0010, CMP-0035, CMP-0046, CMP-0040, CMP-0058, graph.json, evaluation_progress.json. |
| 9 | 2026-02-22 | Ch 09 — Deposition | Phase B process chapter. ~5,400 words. Covers CVD variants (LPCVD, PECVD, MOCVD, HDP-CVD), PVD/sputtering, ALD (self-limiting cycle mechanics), epitaxy (VPE, MBE), and coating/developing as special case. Five company profiles: TEL (anchor, 20.15T yen mkt cap, coater/dev 90%+ share, CVD/etch, score 58.8 with full investment thesis), Kokusai Electric (batch ALD 70% share, KKR re-IPO history, memory focus, score 56.5), Shibaura Mechatronics (post-CMP cleaning leader, PER 12.46x deep discount, score 66.2 rank #4), Samco (plasma CVD pioneer, Kyoto R&D, 25.1% OPM, score 56.2), Tazmo (PER 7.17x extreme discount, 27.4% rev growth, score 57.5). Competitive landscape mapping global CVD/PVD/ALD/coating markets including WONIK IPS, NAURA, SEMES. Full upstream supplier web (8 component suppliers to TEL mapped). Data from CMP-0004, CMP-0011, CMP-0059, CMP-0060, CMP-0062, graph.json, evaluation_progress.json. |
| 10 | 2026-02-22 | Ch 14 — Dicing & Singulation | Phase C back-end chapter. ~5,400 words. Blade dicing physics (kerf, chipping, diamond blades), laser dicing (ablation vs stealth), DBG, tape mount, chiplet-era tailwinds. DISCO (70-80% share, 41% OPM, score 46.2), Tokyo Seimitsu (10% dicing + 46% prober, score 61.0). Valuation paradox. Competitors: EO Technics, Guangli/ADT, Shenyang Heyan, CETC. 13 DISCO OSAT supplier edges. Data from CMP-0001, CMP-0002, CMP-0074, CMP-0089, CMP-0091, CMP-0099, graph.json, evaluation_progress.json. |
| 11 | 2026-02-22 | Ch 13 — Wafer Test & Probing | Phase C back-end chapter. ~5,600 words. Probe card tech (cantilever, vertical, MEMS), ATE architecture, wafer-level test flow, KGD yield math, test economics. Tokyo Seimitsu (46% prober share, 65 edges -- most connected node, score 61.0, thesis), Advantest (#1 ATE, 1.07T yen, score 52.2), Aval Data (PER 6.1x, score 57.0), NHK Spring (probe springs, score 54.8). Tokyo Seimitsu-Advantest partnership section. Data from CMP-0001, CMP-0005, CMP-0054, CMP-0055, graph.json, evaluation_progress.json. |
| 12 | 2026-02-22 | Ch 10 — Etching & Cleaning | Phase B etch/clean chapter. ~5,600 words. Covers wet etch chemistry (HF, BHF, piranha, H3PO4), dry/plasma etch (RIE, ICP, ALE), selectivity and anisotropy, cleaning sequences (SC-1, SC-2, SPM, DHF, DIO3), megasonic cleaning physics, cleaning frequency economics. Four company profiles: SCREEN Holdings (wet cleaning dominance, 15K+ units shipped, score 55.5), PILLAR Corporation (90%+ fluororesin fitting monopoly, S-300 de facto standard, Entegris license validation, full investment thesis at score 72.0 -- book's #2 thesis), CKD Corporation (pneumatic valves, deepest PER discount in G1, score 60.0), Horiba (30%+ MFC share, 56% foreign ownership, score 54.8). PILLAR thesis receives extended treatment: foreign ownership gap catalyst (21.28% vs expected 45%), 100-year heritage, 14 client edges, segment structure, 10-year profit CAGR 15.37%. Competitive landscape and nested supply chain connections mapped. Data from CMP-0003, CMP-0042, CMP-0043, CMP-0012, graph.json, evaluation_progress.json. |
| 13 | 2026-02-22 | Ch 11 -- CMP Planarization | Phase B planarization chapter. ~5,800 words. CMP physics, slurry types, pad conditioning, endpoint detection, dishing/erosion. BEOL frequency (20-30 CMP steps/wafer). 7 companies by role: systems (Ebara, Tokyo Seimitsu 61.0 + thesis), consumables (Fujimi, Fuso Chemical 55.8 + thesis, FUJIFILM, Resonac), coatings (Tocalo). Fuso 90% colloidal silica = deepest hidden chokepoint. Data from CMP-0036, CMP-0007, CMP-0013, CMP-0008, CMP-0040, CMP-0031, CMP-0001. |
| 14 | 2026-02-22 | Ch 17 -- Geopolitics & Supply Chain Risk | Phase D ecosystem chapter. ~5,200 words. Japan's position between US and China, three waves of export controls (Oct 2022, Oct 2023, Dec 2024), Japan/METI alignment, China domestic substitution push (NAURA, Huahai Qingke, Changchuan, Heyan, CETC). Five company case studies: Tokyo Seimitsu (34% China revenue, 65 edges, most-connected node, F=4/10), TEL (30% China, 20.15T mkt cap, coater/dev monopoly buffers risk, F=5/10), SCREEN (cleaning less restricted, 15K+ installed base, F=5/10), Ferrotec (unique China manufacturing footprint, bridge vs trap, F=5/10), Organo (TSMC lock-in, 12.6% China but 30% Greater China, F=1/10 lowest due to customer concentration). Full Dimension F framework explanation (F1 forex, F2 concentration, F3 geopolitical). "Japan premium" analysis: qualification timelines, purity requirements, installed base lock-in, ecosystem effect. Investment perspective for each company. Data from CMP-0001, CMP-0003, CMP-0004, CMP-0009, CMP-0052, CMP-0066, CMP-0070, CMP-0085, CMP-0088, CMP-0093, graph.json, evaluation_progress.json, EVALUATION_FRAMEWORK.md. |
| 15 | 2026-02-22 | Appendix D -- Evaluation Methodology | Phase F reference appendix. ~4,800 words. Complete reproduction of 6-dimension scoring framework (A-F, 0-100 scale). All formulas, tier rubrics, special-case rules. Composite score with data confidence modifier. Peer group definitions (G1-G4) with full rosters and Feb 2026 medians. Score interpretation table. Sensitivity analysis scenarios. 18-field data requirements. Scoring worksheet template. Worked examples. Limitations section. Data from EVALUATION_FRAMEWORK.md, evaluation_progress.json. |
| 16 | 2026-02-22 | Appendix E -- Glossary of Semiconductor Terms | Phase F appendix. ~3,800 words. Alphabetical glossary with ~150 entries across 8 categories: process steps (lithography, etching, deposition, CMP, dicing), equipment types (stepper, scanner, coater/developer, prober, ATE), materials (photoresist, slurry, wafer, photomask, HF), technologies (EUV, DUV, ArF, KrF, CVD, PVD, ALD), packaging (flip-chip, CoWoS, HBM, FC-BGA, chiplet, UCIe, TSV), business terms (foundry, IDM, fabless, OSAT, AMHS), financial metrics (PER, PBR, ROE, operating margin, market cap), and acronyms. Each entry includes 1-2 sentence definition and chapter cross-reference. No CMP data files referenced (terminology reference only). |
| 17 | 2026-02-22 | Ch 18 -- Investment Framework | Phase E capstone chapter. ~7,800 words. Complete 6-dimension framework summary (A-F, 0-100 scale) with dimension weights and sub-score rubrics. Four peer group presentations (G1-G4) with median financial metrics tables. Top-10 most undervalued companies with full investment thesis summaries (300-500 words each): Gun Ei Chemical (78.9), SK Hynix (73.0), PILLAR (72.0), Shibaura Mechatronics (66.2), Canon (65.0), Toyo Gosei (62.4), TSMC (62.8), Tokyo Seimitsu (61.0), Stella Chemifa (60.5), Samsung/CKD/Organo (60.0-60.2). Score distribution analysis across all 74 companies with histogram table. Portfolio construction principles: concentration vs diversification, monopolists vs value plays, China exposure management, position sizing by conviction, currency considerations. Limitations section: point-in-time data, forward PER gap, qualitative dimensions, framework rewards undervaluation not quality (DISCO at 46.2 despite 80%+ share), currency effects, sector-specific design, coverage universe boundaries. Data from evaluation_progress.json (all 74 scored companies), EVALUATION_FRAMEWORK.md, graph.json. |

---

## Appendix: Peer Group Reference

For quick reference when writing chapters with financial comparisons.

| Peer Group | Description | PER Median | PBR Median | ROE Median | Rev Growth Median | OPM Median |
|------------|-------------|------------|------------|------------|-------------------|------------|
| G1 | Semiconductor Equipment | 31.59 | 2.49 | 14.65% | 15.6% | 14.9% |
| G2 | Semiconductor Materials | 17.0 | 1.32 | 9.38% | 7.0% | 15.19% |
| G3 | Semiconductors & Memory | 29.3 | 2.11 | 22.55% | 61.6% | 22.4% |
| G4 | Other | 27.7 | 9.9 | 38.8% | 7.7% | 28.0% |

## Appendix: Top-10 Investment Theses (Quick Reference)

| Rank | Company | Score | Key Thesis |
|------|---------|-------|------------|
| 1 | Gun Ei Chemical (4229.T) | 78.9 | Photoresist resin duopoly, PBR 0.64x, capacity expansion ahead of AI demand |
| 2 | PILLAR (6490.T) | 72.0 | 90%+ fluororesin fitting monopoly, PER 32% discount to peers |
| 3 | SK Hynix (000660.KS) | 73.0 | HBM memory leadership, strong AI-driven demand cycle |
| 4 | Shibaura Mechatronics (6590.T) | 66.2 | Plasma processing specialist, growing advanced-node exposure |
| 5 | Canon (7751.T) | 65.0 | Nanoimprint lithography optionality, mature node revenue base |
| 6 | Toyo Gosei (4970.T) | 62.4 | PAG specialist for EUV photoresists, niche monopoly |
| 7 | TSMC (2330.TW) | 62.8 | Foundry monopoly, AI capex beneficiary |
| 8 | Tokyo Seimitsu (7729.T) | 61.0 | Dual prober/CMM leadership, PER discount to equipment peers |
| 9 | Stella Chemifa (4109.T) | 60.5 | 12-nine HF duopoly, foreign ownership gap catalyst |
| 10 | Samsung / CKD / Organo | 60.0–60.2 | Various theses — see Ch 18 for details |
