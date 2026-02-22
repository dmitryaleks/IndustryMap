# Chapter 16: Foundries, IDMs & the AI Boom

> The companies profiled throughout this book -- the wafer polishers, photoresist formulators, CMP slurry makers, and probe card assemblers -- do not exist in isolation; they exist because a handful of chipmakers spend tens of billions of dollars every year converting raw silicon into finished semiconductors, and understanding these demand engines is essential to understanding why Japan's hidden dominance matters.

## Introduction

Every chapter of this book has traced the semiconductor supply chain from the bottom up. We started with raw silicon ingots in Chapter 4, worked through patterning, deposition, etch, planarization, and test, and arrived at advanced packaging in Chapter 15. At each stage, we identified Japanese companies that hold monopoly or oligopoly positions in critical process steps. But we have not yet addressed the fundamental question: who buys all of this?

The answer is a surprisingly small group of companies. The global semiconductor industry generates over 60 trillion yen in annual revenue, yet the vast majority of advanced chip production flows through just seven entities: TSMC, Samsung Electronics, Intel, SK Hynix, Micron, Kioxia, and -- as the demand anchor that shapes capital expenditure decisions for all of the above -- NVIDIA. These seven companies collectively account for the bulk of all wafer fabrication capacity at advanced nodes. They are the customers that the 62 Japanese companies profiled in this book depend on. When TSMC raises its annual capital expenditure from 4 trillion to 8 trillion yen, that increase ripples backward through every tier of the supply chain -- more silicon wafers from Shin-Etsu, more CMP slurry from Fujimi, more EUV mask blanks from HOYA, more coater/developers from Tokyo Electron, more ultrapure water systems from Organo.

This chapter reverses the lens. Instead of looking upstream from the process step to the supplier, we look downstream from the supplier to the customer. We examine the business models that define the industry -- foundry, IDM, and fabless -- and explain why each model creates different demand patterns for the Japanese supply chain. We profile the seven demand engines individually, using the supply chain graph to quantify each company's dependence on Japanese suppliers. And we trace how the AI capital expenditure supercycle, driven by NVIDIA's insatiable appetite for advanced chips and high-bandwidth memory, is propagating demand signals backward through every node in this book's supply chain map.

---

## Business Models: Foundry, IDM, and Fabless

The semiconductor industry is organized around three fundamental business models. Understanding the distinctions is essential for grasping how demand flows through the supply chain and why different chipmakers create different patterns of dependency on Japanese companies.

### The Integrated Device Manufacturer (IDM)

The oldest model is the Integrated Device Manufacturer, or IDM. An IDM designs its own chips and manufactures them in its own fabrication facilities. For most of the semiconductor industry's history, this was the only model. Companies like Intel, Texas Instruments, Motorola, and Toshiba (now Kioxia) designed processors and memory chips, then fabricated them in their own fabs using their own equipment and their own process recipes.

The IDM model has a compelling logic: vertical integration gives a company complete control over both the design and the manufacturing. Process engineers and chip designers can collaborate directly, optimizing the chip design for the specific characteristics of the fab's process technology. Intel's dominance of the PC microprocessor market from the 1980s through the 2010s was built on this model -- its chip designers and process engineers worked in tight feedback loops that competitors could not replicate.

But the IDM model carries enormous capital requirements. A single leading-edge fab costs upward of 2 trillion yen to build and equip. The equipment must be replaced or upgraded every few years as process nodes advance. Only companies with massive and consistent revenue streams can afford to sustain this level of investment. As a result, the number of IDMs capable of manufacturing at leading-edge nodes has collapsed from dozens in the 1990s to essentially two today: Intel and Samsung.

Samsung is a special case -- a hybrid IDM that both manufactures its own memory and logic chips (most notably the Exynos mobile processors used in its Galaxy smartphones) and operates a foundry business that manufactures chips for external customers. This dual identity creates complex incentives: Samsung's foundry clients are aware that they are sharing a fab with Samsung's own products, which creates potential conflicts over capacity allocation and technology priorities.

### The Foundry Model

The foundry model emerged in 1987 when Morris Chang founded TSMC on a radical premise: a company that manufactured chips but designed none of its own. TSMC's sole business was to fabricate chips designed by other companies, using process technology that TSMC developed and maintained. The foundry would compete not on chip design but on manufacturing excellence -- yield, cost, reliability, and time to market.

The foundry model fundamentally altered the economics of the semiconductor industry. Before TSMC, a company that wanted to sell a custom chip had to either build its own fab (prohibitively expensive) or negotiate access to an IDM's excess capacity (unreliable and fraught with intellectual property concerns). TSMC offered a clean alternative: a dedicated manufacturing partner with no competing chip designs, no incentive to steal customers' IP, and a relentless focus on process technology leadership.

Today, TSMC dominates the foundry market with approximately 62-65 percent global share by revenue. At advanced nodes -- defined as 7 nanometers and below, where AI chips, mobile processors, and high-performance computing chips are manufactured -- TSMC's share exceeds 90 percent. Samsung Foundry holds a distant second place, and Intel Foundry Services, launched as part of Intel's IDM 2.0 strategy, is attempting to build a third-party foundry business essentially from scratch.

### The Fabless Model

The third model, fabless, emerged as a natural complement to the foundry. A fabless company designs chips but owns no fabrication facilities. It outsources all manufacturing to foundries (primarily TSMC) and focuses entirely on chip architecture, circuit design, and software ecosystems.

NVIDIA is the archetype of the fabless model. Jensen Huang's company designs the world's most advanced AI accelerators -- the H100, H200, Blackwell, and forthcoming Rubin architectures -- but does not manufacture a single transistor. Every NVIDIA GPU is fabricated by TSMC, tested on Advantest equipment, diced by DISCO saws, and packaged on Ibiden substrates using SK Hynix's HBM memory stacks. NVIDIA's market capitalization of 518.3 trillion yen -- the second most valuable company in the world -- is built entirely on intellectual property and software, with physical production delegated to a network of suppliers.

Other major fabless companies include AMD, Qualcomm, Broadcom, MediaTek, and Apple's chip design division. The fabless model's advantage is capital efficiency: the company can invest all of its resources in design and software rather than splitting investment between design and manufacturing. The disadvantage is dependency -- a fabless company is entirely at the mercy of its foundry partner for capacity, yield, and process technology access.

### Why the Model Matters for Japan

The distinction between foundry, IDM, and fabless matters enormously for Japan's supply chain position. A foundry like TSMC consumes equipment, materials, and chemicals from hundreds of suppliers because its entire business is manufacturing. In our supply chain graph, TSMC has 40 incoming supplier edges -- more than almost any other node. Samsung, as an IDM with both memory and foundry operations, has even more: 44 incoming supplier edges. These are the companies that write the purchase orders for Tokyo Electron coater/developers, Shin-Etsu wafers, Stella Chemifa hydrofluoric acid, and Daifuku cleanroom automation systems.

A fabless company like NVIDIA, by contrast, has only 4 incoming supplier edges in our graph: TSMC (chip manufacturing), SK Hynix (HBM memory), Ibiden (FC-BGA substrates), and Leeno Industrial (test components). NVIDIA creates demand indirectly -- its GPU designs dictate the process technology that TSMC must develop, which in turn dictates the equipment and materials that TSMC must purchase from Japanese suppliers. But the purchase orders flow through TSMC, not through NVIDIA.

This is why the foundries and IDMs are the true demand engines of the supply chain. They are the converting nodes -- the companies that transform raw materials and equipment into finished semiconductors. Japan's 62 companies are overwhelmingly suppliers to these converting nodes.

---

## The AI Capex Supercycle

Before profiling the individual demand engines, it is necessary to understand the macroeconomic force reshaping the entire semiconductor supply chain: the artificial intelligence capital expenditure supercycle.

### The Scale of AI Investment

The numbers are staggering. Global AI-related capital expenditure is projected to exceed 50 trillion yen in 2026, an increase of 50-60 percent year over year. The five largest AI investors -- Microsoft, Amazon, Google, Meta, and Oracle -- have collectively committed to spending more than 40 trillion yen on data center infrastructure in 2026 alone. The vast majority of this spending flows to NVIDIA GPUs (approximately 39 percent of total AI capex goes directly to GPU procurement), the TSMC fabs that manufacture those GPUs, and the memory companies that supply the HBM stacks bonded alongside them.

NVIDIA itself projects 2026 revenue of approximately 75 trillion yen (roughly $500 billion), representing 71 percent earnings growth over the prior year. The company reports a $500 billion order backlog. These are not speculative projections -- they reflect binding commitments from hyperscale cloud providers that have bet their competitive futures on AI infrastructure.

### How the Supercycle Ripples Backward

The AI capex supercycle creates demand through a chain of amplifying dependencies. The sequence runs as follows:

**Tier 0 -- End demand.** Hyperscale cloud providers (Microsoft, Amazon, Google, Meta) need AI compute capacity. They order NVIDIA GPUs and AI server systems.

**Tier 1 -- Chip design.** NVIDIA designs Blackwell and Rubin GPU architectures. Each GPU die requires TSMC's most advanced process nodes (3nm, transitioning to 2nm). Each GPU package requires 6-8 HBM memory stacks from SK Hynix or Samsung. Each GPU sits on an FC-BGA substrate from Ibiden.

**Tier 2 -- Chip manufacturing.** TSMC allocates its most advanced fab capacity to NVIDIA production. To meet demand, TSMC raises its annual capex to approximately 8.5 trillion yen ($56 billion) in 2026. Samsung and Intel increase memory and foundry capex in parallel. SK Hynix expands HBM production capacity.

**Tier 3 -- Equipment and materials.** TSMC's capex flows to equipment and materials suppliers. Tokyo Electron receives orders for coater/developers, CVD chambers, and etch tools. ASML ships additional EUV scanners. SCREEN delivers wet cleaning stations. Advantest provides test equipment. Shin-Etsu and SUMCO ramp wafer production. Fujimi and Fuso Chemical increase CMP slurry output. HOYA produces more EUV mask blanks. Organo installs additional ultrapure water systems.

**Tier 4 -- Component and chemical suppliers.** The Tier 3 equipment and materials companies, in turn, increase orders to their own suppliers. Gun Ei Chemical produces more photoresist resins. Stella Chemifa refines more ultra-high-purity hydrofluoric acid. PILLAR manufactures more fluororesin fittings for wet bench tools. Marumae machines more aluminum chamber components. Rorze builds more wafer transfer robots.

The amplification effect at each tier is substantial. A single NVIDIA Blackwell GPU requires approximately 60 billion transistors, manufactured using 70-80 lithography steps, 20-30 CMP planarization steps, dozens of deposition and etch cycles, and an FC-BGA substrate with twenty or more wiring layers. Multiply that by the millions of GPUs NVIDIA ships annually, and the throughput demands on every supplier in this chain become enormous.

This is why the AI supercycle is not merely good for a few Japanese semiconductor equipment companies. It is good for the entire supply chain, from the silicon crystal grower to the fluororesin fitting maker to the ultrapure water system integrator. The ripple effect is structural, not incidental.

---

## Company Profiles

### Taiwan Semiconductor Manufacturing Company Limited (2330.TW) -- The World's Foundry

**Founded:** 1987 | **HQ:** Hsinchu, Taiwan | **Market Cap:** 288.8 trillion yen ($1.5 trillion)

Morris Chang founded TSMC in 1987 on the principle that semiconductor manufacturing could be a standalone business. Nearly four decades later, that principle has produced the most consequential industrial company of the twenty-first century. TSMC commands approximately 62-65 percent of the global foundry market by revenue and over 90 percent of the advanced-node market at 7 nanometers and below. Every major AI chip -- NVIDIA's Blackwell, Apple's M4, AMD's MI300, Qualcomm's Snapdragon -- is manufactured in TSMC's fabs.

The financial profile reflects this dominance. TSMC reported revenue of approximately 18.1 trillion yen in the latest fiscal year, growing 31.6 percent year over year. Operating margin stands at 54.0 percent -- an extraordinary figure for a capital-intensive manufacturer, and evidence of the pricing power that comes with monopoly-level market share at advanced nodes. ROE of 38.8 percent demonstrates efficient capital allocation despite annual capex of 8 trillion yen or more. TSMC's January 2026 revenue of NT$401 billion represented 37 percent year-over-year growth, with HPC (high-performance computing) chips -- the category that includes AI accelerators -- accounting for 58 percent of total revenue.

TSMC's 2026 capital expenditure plan of approximately 8.5 trillion yen ($56 billion) represents the largest single-year investment in semiconductor manufacturing history. This spending flows overwhelmingly to equipment and materials from the companies profiled in earlier chapters of this book.

**Key Financials:**

| Metric | Value |
|--------|-------|
| Market Cap | 288.8 trillion yen |
| PER | 31.9x |
| PBR | 9.9x |
| Revenue (FY) | 18,097.5 billion yen |
| Revenue Growth | +31.6% YoY |
| Operating Margin | 54.0% |
| ROE | 38.8% |
| Dividend Yield | 1.42% |
| Analyst Consensus | 49 Buy / 43 Hold / 0 Sell |

**TSMC's Japanese Supply Chain: 40 Incoming Supplier Edges**

TSMC's position in our supply chain graph reveals the depth of its dependence on Japanese companies. Of TSMC's 40 incoming supplier edges, 38 originate from Japanese companies. The remaining two come from ASML (Netherlands, EUV lithography) and Leeno Industrial (South Korea, test components). This means that 95 percent of TSMC's mapped supply chain relationships run through Japan.

The full list of Japanese suppliers to TSMC in our database illustrates the breadth of this dependency:

| Supplier | Category | Chapter |
|----------|----------|---------|
| Shin-Etsu Chemical | Silicon wafers | Ch 4 |
| SUMCO | Silicon wafers | Ch 4 |
| Tokyo Electron | Coater/developers, etch, CVD | Ch 9 |
| SCREEN Holdings | Wafer cleaning | Ch 10 |
| Fujimi | CMP slurry | Ch 11 |
| Fuso Chemical | CMP slurry | Ch 11 |
| HOYA | Photomask blanks | Ch 7 |
| Advantest | Test equipment | Ch 13 |
| Lasertec | EUV mask inspection | Ch 7 |
| Toyo Gosei | Photoresist materials (PAGs) | Ch 8 |
| Resonac | Semiconductor materials | Ch 8/11 |
| Nippon Sanso | Specialty gases | Ch 5 |
| Tokyo Ohka Kogyo | Photoresist (25% world share) | Ch 8 |
| JSR | EUV photoresist | Ch 8 |
| Ebara | CMP systems, vacuum pumps | Ch 11 |
| NGK Insulators | Ceramic electrostatic chucks | Ch 12 |
| Niterra | IC package substrates | Ch 12/15 |
| FUJIFILM | CMP slurry, photoresist | Ch 8/11 |
| Rorze | Wafer handling systems | Ch 12 |
| Stella Chemifa | 12-nine purity HF acid | Ch 5 |
| Kanto Denka Kogyo | Specialty fluorine gases | Ch 5 |
| Sumitomo Chemical | Photoresist | Ch 8 |
| Toppan | EUV photomasks | Ch 7 |
| Ibiden | High-end FC-BGA substrates | Ch 15 |
| Dai Nippon Printing | Photomask production | Ch 7 |
| Nikon | i-line/KrF steppers | Ch 6 |
| Canon | i-line/KrF steppers | Ch 6 |
| Organo | Ultrapure water systems | Ch 5 |
| Nomura Micro Science | Ultrapure water systems | Ch 5 |
| NHK Spring | HDD suspension (50% share) | Ch 13 |
| Daifuku | Cleanroom AMHS | Ch 12 |
| MEC Company | PCB surface treatment | Ch 15 |
| Nagase | Electronic chemicals | Ch 8 |
| Shibaura Mechatronics | Plasma processing equipment | Ch 9 |
| Samco | Plasma CVD equipment | Ch 9 |
| Tazmo | Coater/developer equipment | Ch 9 |
| Tokyo Seimitsu | Probing, dicing, CMP equipment | Ch 11/13/14 |
| PILLAR | Fluororesin fittings | Ch 10 |

This table is, in effect, a cross-reference to the entire book. Every process chapter -- from Chapter 4 (silicon wafers) to Chapter 15 (advanced packaging) -- contains companies that supply TSMC. A disruption to any one of these suppliers would affect TSMC's ability to produce chips, and by extension, would affect every fabless company that depends on TSMC for manufacturing.

The concentration is particularly acute in certain categories. Organo holds 100 percent of TSMC's ultrapure water treatment contracts for advanced nodes (10nm and below). HOYA supplies over 75 percent of TSMC's EUV photomask blanks. Lasertec is the sole source for EUV mask inspection. These are not relationships that can be diversified away.

#### Investment Perspective

TSMC scores 62.8 in our evaluation framework, ranking seventh overall. The score reflects a perfect moat score (B = 25/25) -- the highest possible rating for market share, switching costs, technological differentiation, and supply chain centrality. Growth metrics are equally strong (C = 15/15), reflecting 31.6 percent revenue growth and 54 percent operating margins. The score is held back by a stretched valuation (A = 8.8/30, reflecting PBR of 9.9x and PER of 31.9x) and minimal price discount to the 52-week high (D = 2.0/10).

The investment thesis for TSMC is straightforward: the company is a monopoly at the most critical node in the semiconductor supply chain, with pricing power, secular demand growth driven by AI, and no credible challenger at advanced nodes. The risk is geopolitical -- TSMC's fabs are concentrated in Taiwan, and cross-strait tensions with China represent the single largest tail risk in the global semiconductor supply chain. TSMC is mitigating this through geographic diversification (fabs in Arizona, Japan, and Germany), but Taiwan will remain the center of advanced manufacturing for the foreseeable future.

---

### Samsung Electronics Co., Ltd. (005930.KS) -- The IDM Colossus

**Founded:** 1969 | **HQ:** Suwon, South Korea | **Market Cap:** 42.1 trillion yen ($877 billion)

Samsung Electronics is the most diversified semiconductor company in the world and the largest by total semiconductor revenue. It operates simultaneously as an IDM (designing and manufacturing its own memory chips and mobile processors), a foundry (manufacturing chips for external customers), and a consumer electronics conglomerate (smartphones, displays, appliances). This sprawling scope makes Samsung both the most capable and the most conflicted participant in the semiconductor supply chain.

In memory, Samsung is the undisputed global leader. It holds approximately 40 percent of the DRAM market and a comparable share of NAND flash, making it the single largest customer for memory-focused equipment and materials. Samsung's memory fabs in Pyeongtaek, South Korea -- the largest semiconductor fabrication complex in the world -- consume vast quantities of the equipment and chemicals profiled in this book.

In foundry, Samsung is TSMC's primary challenger, though the gap is wide. Samsung Foundry offers 3nm GAA (Gate-All-Around) process technology, the first commercial implementation of GAA transistors, which represents a genuine technical accomplishment. However, Samsung's foundry yield rates have historically lagged TSMC's, and Samsung's dual identity as both foundry and IDM creates trust issues with potential customers who compete with Samsung's own products. The Tesla AI chip deal -- valued at approximately $16.5 billion -- represents Samsung Foundry's most significant external win and a validation of its technical capabilities at advanced nodes.

Samsung's HBM4 development is of particular importance. The company is racing to achieve NVIDIA certification for its HBM4 memory products, which would break SK Hynix's current dominance of the HBM supply chain for NVIDIA's next-generation Rubin platform. Mass production of HBM4 commenced in February 2026, though certification remains pending. The outcome of this competition will determine whether SK Hynix maintains its 70 percent share of HBM for NVIDIA or whether Samsung recaptures a meaningful portion of this high-margin market.

**Key Financials:**

| Metric | Value |
|--------|-------|
| Market Cap | 42.1 trillion yen |
| PER | 29.3x |
| PBR | 1.14x |
| Revenue (FY) | 33,099 billion yen |
| Revenue Growth | +2.6% YoY |
| Operating Margin | 9.51% |
| ROE | 8.33% |
| Dividend Yield | 2.5% |
| Analyst Consensus | 33 Buy / 1 Hold / 1 Sell |

**Samsung's Japanese Supply Chain: 44 Incoming Supplier Edges**

Samsung has more incoming supplier edges than any other company in our database -- 44 in total, exceeding even TSMC's 40. This reflects Samsung's dual identity as both a logic/foundry manufacturer and a memory producer, requiring equipment and materials for both categories.

Of Samsung's 44 incoming supplier edges, 34 originate from Japanese companies. The remaining 10 come from South Korean suppliers (SEMES, SEMICS, WONIK IPS, EO Technics, KCTech, Techwing, Leeno Industrial, HANA Micron, SFA Semicon) and ASML (Netherlands). Japan's share of Samsung's mapped supply chain is 77 percent -- lower than TSMC's 95 percent, reflecting the deeper Korean domestic equipment ecosystem that has developed to serve Samsung and SK Hynix.

The Japanese suppliers to Samsung overlap extensively with those supplying TSMC, with the addition of Kokusai Electric (batch deposition, critical for memory manufacturing), Aval Data (test equipment components), and several others. Notable shared dependencies include Shin-Etsu and SUMCO for wafers, Tokyo Electron for deposition, HOYA for photomask blanks, Stella Chemifa for HF, and Lasertec for EUV mask inspection.

The Korean suppliers represent a domestication trend worth noting. Companies like SEMES (Samsung's captive equipment subsidiary), WONIK IPS (deposition equipment), and KCTech (CMP equipment and slurry) have been developing capabilities that partially substitute for Japanese suppliers. However, for the most critical process steps -- EUV-related technologies, ultra-high-purity chemicals, and advanced test equipment -- Japanese suppliers remain irreplaceable.

#### Investment Perspective

Samsung scores 60.2 in our evaluation framework. The valuation dimension is favorable (A = 16.2/30), reflecting PBR of 1.14x -- a deep discount to the G3 peer median of 2.11x. The moat score is strong (B = 19/25), reflecting Samsung's dominant memory market share and moderate foundry position. Growth metrics are weak (C = 6.0/15), penalized by anemic 2.6 percent revenue growth and sub-10 percent operating margins -- a reflection of the memory downcycle's lingering effects and the drag from consumer electronics divisions. The catalyst dimension is strong (D = 6.0/10 and E = 9.0/10), with 33 out of 35 analysts rating Samsung a buy and significant capacity expansion underway.

Samsung's stock sits well below its 52-week high (57,000 KRW versus the 52-week high of 88,800 KRW), representing a 36 percent drawdown that provides a potential entry point for investors willing to underwrite the memory recovery thesis and the HBM4 certification catalyst.

---

### Intel Corporation (INTC) -- The IDM in Transformation

**Founded:** 1968 | **HQ:** Santa Clara, California | **Market Cap:** 15.8 trillion yen ($234 billion)

Intel's story is one of the most consequential in semiconductor history -- and one of the most cautionary. For thirty years, Intel was the undisputed leader in semiconductor manufacturing. Its fabs consistently led the industry in transistor density and performance. The "Intel Inside" brand was synonymous with computing itself. But beginning in approximately 2015, Intel stumbled. Its 10nm process technology was delayed repeatedly, while TSMC advanced from 16nm to 7nm to 5nm to 3nm on schedule. By the early 2020s, Intel found itself in the unfamiliar position of being a laggard in manufacturing technology -- a situation that would have been inconceivable a decade earlier.

Intel's response is the IDM 2.0 strategy, announced by CEO Pat Gelsinger in 2021 and currently being executed under his successor. The strategy has two components. First, Intel is investing aggressively to regain process technology leadership through what it calls "five nodes in four years" -- an unprecedented acceleration of its manufacturing roadmap, targeting the Intel 18A node as the vehicle for returning to competitiveness with TSMC. Second, Intel is building a third-party foundry business, Intel Foundry Services, to compete with TSMC and Samsung for external customers.

The execution challenges are immense. Intel's latest fiscal year showed revenue declining 2.0 percent year over year, with an operating margin of negative 4.19 percent. The company reported negative earnings per share of -$0.06, driven by the massive capital expenditures required for its transformation. The U.S. CHIPS Act provides some relief -- Intel has been awarded $8.5 billion in direct subsidies and up to $11 billion in loans -- but the fundamental question remains whether Intel can close a multi-year gap with TSMC while simultaneously transforming its business model.

Intel's relationship with Japanese suppliers is deep. Intel has the largest installed base of Lasertec EUV mask inspection systems in the world -- 14 units -- reflecting its heavy investment in EUV-enabled process technology for the Intel 18A node and beyond. Tokyo Electron, Shin-Etsu, SUMCO, HOYA, Kokusai Electric, and Fuso Chemical are all confirmed suppliers.

**Key Financials:**

| Metric | Value |
|--------|-------|
| Market Cap | 15.8 trillion yen |
| PER | N/A (negative earnings) |
| PBR | 1.32x |
| Revenue (FY) | 8,071.2 billion yen |
| Revenue Growth | -2.0% YoY |
| Operating Margin | -4.19% |
| ROE | -18.9% |
| Dividend Yield | 0.55% |
| Analyst Consensus | 4 Buy / 34 Hold / 7 Sell |

**Intel's Japanese Supply Chain: 28 Incoming Supplier Edges**

Intel has 28 incoming supplier edges in our graph, of which 25 originate from Japanese companies. This 89 percent Japan share is comparable to TSMC's 95 percent and reflects the fact that, for leading-edge logic manufacturing, there is no viable alternative to the Japanese equipment and materials ecosystem.

Intel's suppliers include the same core group that serves TSMC: Shin-Etsu and SUMCO for wafers, Tokyo Electron for deposition, Lasertec for EUV mask inspection, HOYA for photomask blanks, Kokusai Electric for batch deposition, Fujimi and Fuso Chemical for CMP slurry, and Stella Chemifa for ultra-high-purity HF. The overlap underscores a crucial point: regardless of which company "wins" the foundry race, the Japanese supply chain wins. Whether TSMC, Samsung, or Intel builds the next leading-edge fab, they will all buy from the same Japanese suppliers.

#### Investment Perspective

Intel scores 57.5 in our evaluation framework. The score is distorted by the valuation dimension (A = 22.5/30), which is inflated because Intel's negative earnings make PER-based comparisons meaningless, and the pro-rata rescaling of the single available sub-dimension (PBR discount) produces an artificially high number. The moat score is moderate (B = 16/25), reflecting Intel's still-significant but eroding market position. Growth metrics are among the worst in our database (C = 3.0/15), reflecting revenue declines and negative margins. The catalyst dimension is mixed: Intel has strong policy tailwinds from the CHIPS Act (E3 = 3/3) but weak analyst consensus (only 4 out of 45 analysts rate it a buy).

Intel represents a high-risk, high-reward thesis: if Intel 18A succeeds and Intel Foundry Services attracts major customers, the company's manufacturing assets and CHIPS Act subsidies could make it one of the great turnaround stories in semiconductor history. If the transformation fails, Intel's relevance to this supply chain map will diminish significantly. Either way, Intel's capex during the transformation period generates substantial demand for Japanese equipment and materials.

---

### SK Hynix Inc. (000660.KS) -- The HBM Champion

**Founded:** 1983 | **HQ:** Icheon, South Korea | **Market Cap:** 19.0 trillion yen ($452 billion)

SK Hynix is, by almost any measure, the single greatest beneficiary of the AI revolution among memory semiconductor companies. The company holds over 50 percent of the global market for High Bandwidth Memory -- the vertically stacked DRAM technology that is essential to every AI accelerator produced by NVIDIA, AMD, and other GPU designers. HBM has transformed SK Hynix from a commodity memory maker subject to brutal cyclical swings into a structural growth story with a direct line to the highest-growth segment of the semiconductor industry.

The HBM opportunity is enormous. Each NVIDIA H100 GPU requires six HBM3 stacks. Each Blackwell GPU requires even more HBM capacity. The forthcoming Rubin platform, expected in the second half of 2026, will use HBM4 -- and SK Hynix is projected to capture 70 percent of HBM4 supply for the Rubin platform, according to UBS estimates. This is not a commodity memory business; this is a near-monopoly position in the highest-margin segment of the memory industry, with demand visibility extending years into the future.

The financial results reflect this transformation. SK Hynix reported revenue of approximately 7.3 trillion yen in the latest fiscal year, an extraordinary 102 percent year-over-year increase. Operating margin reached 35 percent -- a level unheard of in the memory industry outside of peak-cycle quarters. PER of 5.59x and ROE of 31.1 percent together tell the story of a company generating enormous earnings relative to its market valuation.

SK Hynix's direct relationship with NVIDIA is the demand anchor. NVIDIA is SK Hynix's largest customer for HBM products, and this relationship is captured explicitly in our supply chain graph: CMP-0020 (SK Hynix) supplies CMP-0028 (NVIDIA) with HBM memory. The supply chain then extends further -- each HBM stack requires thermocompression bonding from Hanmi Semiconductor (CMP-0072, which holds 71 percent market share in TC bonders for HBM), EUV-stealth dicing from EO Technics, and wafer probing from Tokyo Seimitsu and SEMICS.

**Key Financials:**

| Metric | Value |
|--------|-------|
| Market Cap | 19.0 trillion yen |
| PER | 5.59x |
| PBR | 2.95x |
| Revenue (FY) | 7,280.9 billion yen |
| Revenue Growth | +102.0% YoY |
| Operating Margin | 35.0% |
| ROE | 31.1% |
| Dividend Yield | 0.26% |
| Analyst Consensus | 34 Buy / 2 Hold / 1 Sell |

**SK Hynix's Japanese Supply Chain: 22 Incoming Supplier Edges**

SK Hynix has 22 incoming supplier edges in our graph (excluding one competitor edge from Samsung). Of these, 13 originate from Japanese companies, representing 59 percent of the total. The remaining suppliers include Korean companies (Hanmi Semiconductor, KCTech, Techwing, SEMICS, WONIK IPS, EO Technics, HANA Micron) and ASML.

The lower Japanese share (59 percent versus TSMC's 95 percent) reflects two factors. First, Korea's domestic semiconductor equipment ecosystem is more developed than Taiwan's, particularly in memory-specific tools. Second, memory manufacturing uses a somewhat different process mix than logic manufacturing -- for example, batch deposition (Kokusai Electric's specialty) is more prevalent in memory fabs, while the EUV-related tools that are disproportionately Japanese play a smaller role in memory (which adopted EUV later than logic).

Japanese suppliers to SK Hynix include: Shin-Etsu and SUMCO (silicon wafers), Tokyo Electron (deposition equipment), Advantest (test equipment), Kokusai Electric (batch deposition), HOYA (photomask blanks), Nippon Sanso (specialty gases), Stella Chemifa (ultra-high purity HF), Nomura Micro Science (ultrapure water systems), Ebara (CMP systems), Tokyo Seimitsu (probing, dicing equipment), and PILLAR (fluororesin fittings).

#### Investment Perspective

SK Hynix scores 73.0 in our evaluation framework -- the third-highest score in the entire database of 74 companies, behind only Gun Ei Chemical (78.9) and PILLAR Corporation (72.0). This is a remarkable result for a large-cap memory company, and it reflects the unusual combination of structural growth, dominant market position, and deep valuation that the AI-driven HBM cycle has created.

The valuation dimension is strong (A = 20.0/30): PER of 5.59x represents a deep discount to the G3 Semiconductors & Memory peer median of 29.3x, and earnings yield is among the highest in the database. The moat dimension is excellent (B = 21/25), driven by HBM market leadership (B1 = 8/10), very high switching costs (B2 = 5/5), and strong technology differentiation (B3 = 4/5). Growth metrics are perfect (C = 15/15), reflecting 102 percent revenue growth, 35 percent operating margins, 31 percent ROE, and maximum AI exposure.

The key risk is cyclicality. Memory has historically been the most volatile segment of the semiconductor industry, with boom-bust cycles that can compress margins from 35 percent to negative in a single year. HBM's structural demand from AI may moderate this cyclicality, but investors must assess whether the current margin profile is sustainable or whether it represents a peak. The stock's position near its 52-week high (249,000 KRW versus 248,500 KRW) leaves limited margin of safety for timing.

---

### Micron Technology, Inc. (MU) -- America's Memory Maker

**Founded:** 1978 | **HQ:** Boise, Idaho | **Market Cap:** 17.2 trillion yen ($469 billion)

Micron Technology is the only U.S.-based manufacturer of DRAM and NAND flash memory. In an industry dominated by Korean and, historically, Japanese competitors, Micron has survived through a combination of technical capability, acquisition (Micron's 2013 acquisition of Elpida Memory, the bankrupt Japanese DRAM maker, was a defining strategic move), and, increasingly, the benefits of being a domestic supplier in an era of semiconductor nationalism.

Micron holds approximately 20-25 percent of the global DRAM market and a comparable share of NAND flash, placing it third behind Samsung and SK Hynix in both categories. The company's product portfolio spans data center, PC, graphics, networking, automotive, industrial, and mobile markets, sold under the Micron and Crucial brands.

Micron's HBM ambitions are notable. While SK Hynix leads the HBM market, Micron has been investing aggressively in HBM development and has secured qualification for its HBM3E products with at least one major customer. Micron's advantage is its strong relationship with U.S.-based hyperscalers and the geopolitical tailwind of being a domestic supplier in an era when governments are actively seeking to reduce dependence on Asian memory supply chains.

Revenue in the latest fiscal year was approximately 3.8 trillion yen, growing 61.6 percent year over year -- a rate that reflects recovery from the memory downcycle and growing demand for AI-related memory products. Operating margin of 22.4 percent and ROE of 22.55 percent indicate a business operating well above its mid-cycle profitability.

**Key Financials:**

| Metric | Value |
|--------|-------|
| Market Cap | 17.2 trillion yen |
| PER | 24.6x |
| PBR | 2.88x |
| Revenue (FY) | 3,816.7 billion yen |
| Revenue Growth | +61.6% YoY |
| Operating Margin | 22.4% |
| ROE | 22.55% |
| Dividend Yield | 0.45% |
| Analyst Consensus | 26 Buy / 2 Hold / 0 Sell |

**Micron's Japanese Supply Chain: 12 Incoming Supplier Edges**

Micron has 12 incoming supplier edges in our graph (excluding one competitor edge from Samsung). Of these, 9 originate from Japanese companies (75 percent), with the remainder from Hanmi Semiconductor (TC bonders for HBM), Powertech Technology (memory packaging), and ASML. The Japanese suppliers include: Shin-Etsu and SUMCO (silicon wafers), Advantest (test equipment), Kokusai Electric (batch deposition), Nippon Sanso (specialty gases), Stella Chemifa (ultra-high purity HF), Ebara (CMP systems), and Tokyo Seimitsu (probing, dicing equipment).

Micron's lower total supplier edge count compared to TSMC or Samsung reflects its narrower product focus (memory only, no logic or foundry) and the fact that Micron's fab operations are concentrated in fewer locations with a more standardized equipment set.

#### Investment Perspective

Micron scores 57.5 in our evaluation framework. PER of 24.6x versus the G3 peer median of 29.3x earns a moderate valuation discount (A1 = 8/12). Revenue growth of 61.6 percent and ROE of 22.55 percent both align closely with G3 medians, resulting in solid but not exceptional growth scores. The primary risk dimension (F = 4/10) reflects forex sensitivity and geopolitical uncertainty. Nearly all 28 analysts covering Micron rate it a buy (E1 = 4/5), suggesting strong consensus around the memory recovery thesis.

---

### Kioxia Holdings Corporation (285A.T) -- Japan's Last Chipmaker

**Founded:** 2017 (as Toshiba Memory Corporation) | **HQ:** Minato-ku, Tokyo | **Market Cap:** 7.97 trillion yen

Kioxia occupies a unique position in this book: it is the only Japanese company among the seven demand engines profiled in this chapter. It is, in effect, Japan's last remaining major chipmaker -- the sole Japanese company that manufactures semiconductor devices at scale for the global market. Every other Japanese company in our database is a supplier to chipmakers rather than a chipmaker itself. This makes Kioxia both a national champion and a symbol of how Japan's semiconductor industry has evolved from chip production to supply chain dominance.

Kioxia's origins lie in Toshiba's invention of flash memory in 1987. Fujio Masuoka, a Toshiba engineer, developed the concept of flash memory and produced the first working prototypes, creating what would become one of the most important semiconductor technologies of the modern era. Toshiba's flash memory business grew into a global leader, pioneering the NAND flash architecture that underlies virtually all solid-state storage today.

The corporate history since then has been turbulent. In 2017, a financial crisis at Toshiba forced the sale of its memory division, which was reconstituted as Toshiba Memory Corporation and subsequently renamed Kioxia in 2019. A consortium led by Bain Capital acquired the business, and Kioxia completed its initial public offering on the Tokyo Stock Exchange in December 2024 -- a long-delayed event that had been attempted and postponed multiple times.

Today, Kioxia is the world's third-largest NAND flash supplier with approximately 14 percent market share, behind Samsung and SK Hynix. Its product portfolio centers on BiCS FLASH (3D NAND technology), SSDs for enterprise and consumer markets, UFS and e-MMC for mobile and automotive applications, and XL-FLASH storage class memory. Revenue for the latest fiscal year was approximately 1.7 trillion yen, growing 58.5 percent year over year as the NAND market recovered from a severe downcycle. Operating margin stands at 17.86 percent and ROE at 21.61 percent.

**Key Financials:**

| Metric | Value |
|--------|-------|
| Market Cap | 7.97 trillion yen |
| PER | 65.46x |
| PBR | 1.34x |
| Revenue (FY) | 1,706.5 billion yen |
| Revenue Growth | +58.5% YoY |
| Operating Margin | 17.86% |
| ROE | 21.61% |
| Foreign Ownership | 51.0% |
| Analyst Consensus | 9 Buy / Target: 26,525 yen |

**The Western Digital Joint Venture**

Kioxia's most distinctive structural feature is its manufacturing joint venture with Western Digital, which dates back to 2000 when Western Digital's predecessor (SanDisk) partnered with Toshiba to share the enormous capital costs of NAND flash fabrication. The joint venture operates two major fabrication complexes: the Yokkaichi plant in Mie Prefecture and the newer Kitakami plant in Iwate Prefecture. Under the JV arrangement, Kioxia and Western Digital jointly invest in fab construction and equipment, then split the wafer output proportionally to their investment share. Each company develops its own firmware and controller technology, competes independently in the market, but shares the same physical wafers.

This arrangement has profound economics. NAND flash fabrication is among the most capital-intensive manufacturing processes in the semiconductor industry. A single NAND fab can cost over 1.5 trillion yen to build and equip. By sharing these costs, Kioxia and Western Digital each invest roughly half of what they would need independently, dramatically improving the return on capital for both parties. The JV also provides supply stability -- neither partner can be cut off from production by the other, since both are co-investors in the same facilities.

The strategic risk of the JV is dependence. Kioxia and Western Digital are bound together in a relationship that neither can easily exit. Periodic tensions have arisen, including Western Digital's aborted attempt to merge with Kioxia in 2023 and subsequent disputes over technology sharing. The relationship is captured in our supply chain graph as a partner edge: CMP-0023 (Western Digital) and CMP-0014 (Kioxia) share a bidirectional partnership for the Yokkaichi/Kitakami JV.

**NAND Economics and the AI Connection**

NAND flash memory is not a direct AI accelerator component in the same way that HBM DRAM is. AI training models run primarily on GPU compute and HBM memory, not on NAND storage. However, Kioxia benefits from the AI cycle indirectly through several channels.

First, the massive AI models generated by training must be stored somewhere. Each new generation of large language models produces checkpoints and training artifacts measured in petabytes, and the data centers that store these artifacts use enterprise SSDs built on Kioxia (and Samsung, and Micron) NAND. Second, AI inference -- the deployment of trained models to serve user queries -- requires fast storage for model weights and caching, creating SSD demand. Third, the general data center buildout driven by AI investment increases demand for all forms of data center storage.

Apple's reported agreement to pay Kioxia a 2x price increase for Q1 2026 NAND supply is indicative of tightening supply-demand conditions. After a brutal downcycle in 2022-2023 that pushed the entire NAND industry into losses, the market is recovering, and Kioxia's position as the third-largest supplier gives it pricing power as capacity tightens.

**Kioxia's Supply Chain Position: 5 Incoming Edges**

Kioxia has only 5 incoming edges in our graph, the fewest of any demand engine profiled in this chapter. These include Stella Chemifa (supplier of ultra-high purity HF), Kokusai Electric (batch deposition equipment), Western Digital (JV partner), Tokyo Ohka Kogyo (photoresist), and Tokyo Seimitsu (probing and dicing equipment). The low edge count reflects Kioxia's more limited representation in our database rather than a genuinely smaller supply chain -- in reality, Kioxia's fabs use the full range of equipment and materials from the same Japanese suppliers that serve TSMC and Samsung. Future iterations of the database will likely expand Kioxia's mapped relationships substantially.

#### Investment Perspective

Kioxia scores 44.8 in our evaluation framework -- the lowest score among the seven demand engines profiled in this chapter. The primary drag is valuation: PER of 65.46x is deeply unattractive relative to the G3 peer median of 29.3x, earning a zero on the PER discount sub-dimension. PBR of 1.34x is reasonable, providing some offset (A3 = 6/12). The moat score (B = 12/25) reflects Kioxia's moderate market share (14 percent, behind Samsung and SK Hynix) and its position as a third player in a three-company oligopoly -- meaningful, but not dominant.

The 51 percent foreign ownership rate for a recently IPO'd Japanese company is notable. Nine analysts rate Kioxia a buy with an average price target of 26,525 yen, representing approximately 30 percent upside from the current price of 20,485 yen. The thesis for Kioxia is cyclical recovery: if the NAND market continues to tighten and prices rise, Kioxia's earnings will expand dramatically from the current depressed base, compressing the PER toward more reasonable levels. The risk is that the NAND cycle reverses again before earnings fully recover.

---

### NVIDIA Corporation (NVDA) -- The Demand Anchor

**Founded:** 1993 | **HQ:** Santa Clara, California | **Market Cap:** 518.3 trillion yen ($4.65 trillion)

NVIDIA is the gravitational center of the AI semiconductor universe. With 85-90 percent market share in AI accelerators, a CUDA software ecosystem that has become the de facto standard for AI development, and a product roadmap (Blackwell, Rubin, and beyond) that extends visibility for years, NVIDIA is the company whose decisions propagate demand signals through the entire supply chain mapped in this book.

The scale of NVIDIA's dominance is difficult to overstate. Revenue in the latest fiscal year reached approximately 19.8 trillion yen, growing 114 percent year over year. Operating margin stands at 58.84 percent. ROE is 107.36 percent -- a figure that would be dismissed as an error if it did not reflect the company's extraordinary capital efficiency as a fabless designer. NVIDIA's market capitalization of 518.3 trillion yen makes it the second most valuable company in the world, with potential to become the first to reach the $5 trillion mark.

NVIDIA's product cycle is the metronome of the AI supply chain. The Hopper architecture (H100, H200) drove the first wave of AI infrastructure spending in 2023-2024. The Blackwell architecture (B100, B200, GB200) is driving the current wave in 2025-2026. The Rubin architecture, expected in the second half of 2026, will drive the next wave. Each generation demands more advanced process technology from TSMC, more HBM capacity from SK Hynix, more FC-BGA substrates from Ibiden, and -- cascading backward through the supply chain -- more of everything from every Japanese supplier in this book.

**Key Financials:**

| Metric | Value |
|--------|-------|
| Market Cap | 518.3 trillion yen |
| PER | 47.48x |
| PBR | 37.32x |
| Revenue (FY) | 19,836 billion yen |
| Revenue Growth | +114.0% YoY |
| Operating Margin | 58.84% |
| ROE | 107.36% |
| Dividend Yield | 0.03% |
| Analyst Consensus | 39 Buy / 1 Hold / 1 Sell |

**NVIDIA's Supply Chain: 4 Incoming Edges**

NVIDIA's graph profile is the inverse of TSMC's. Where TSMC has 40 incoming supplier edges, NVIDIA has only 4: TSMC (chip manufacturing), SK Hynix (HBM memory), Ibiden (AI server IC substrates, 50 percent or more of NVIDIA's supply), and Leeno Industrial (test components). This minimal direct supply chain is the defining characteristic of the fabless model: NVIDIA owns no fabs, runs no deposition chambers, pours no CMP slurry.

But NVIDIA's indirect demand footprint is the largest of any company in our database. Every NVIDIA GPU that ships requires TSMC to activate its entire 40-supplier chain. Every HBM stack bonded onto an NVIDIA GPU requires SK Hynix to activate its 22-supplier chain. Every FC-BGA substrate beneath an NVIDIA GPU requires Ibiden to source materials from Resonac, MEC Company, and others. NVIDIA does not buy photoresist from Tokyo Ohka Kogyo or wafers from Shin-Etsu directly, but its product decisions determine how much photoresist and how many wafers the entire industry consumes.

This is why we describe NVIDIA as the demand anchor rather than a demand engine. NVIDIA does not consume materials and equipment; it generates the demand that causes others to consume them. Understanding this distinction is essential for supply chain investors: NVIDIA's financial results are a leading indicator for the Japanese semiconductor supply chain, but the direct financial beneficiaries are the companies one, two, and three tiers removed from NVIDIA in the supply chain.

#### Investment Perspective

NVIDIA scores 57.2 in our evaluation framework. The score is held down by an extremely stretched valuation (A = 1.2/30) -- PER of 47.48x and PBR of 37.32x leave virtually no valuation discount to extract. The moat score is perfect (B = 25/25), matching TSMC's rating and reflecting NVIDIA's monopoly market share, maximum switching costs (the CUDA ecosystem), the highest technology differentiation, and the highest supply chain centrality. Growth metrics are also perfect (C = 15/15).

The investment thesis for NVIDIA in the context of this book is not about buying NVIDIA stock. It is about recognizing that NVIDIA's dominance sustains elevated semiconductor equipment and materials demand for 3-5 years. NVIDIA is the demand-side anchor of the entire supply chain thesis that this book describes. Every investment perspective in Chapters 4 through 15 -- every thesis about Gun Ei Chemical's photoresist resins, PILLAR's fluororesin fittings, Fuso Chemical's CMP slurry, Organo's ultrapure water systems -- implicitly depends on NVIDIA continuing to drive AI capex at the current trajectory or higher.

As a USD-listed mega-cap, NVIDIA represents a fundamentally different risk/return profile from the small- and mid-cap Japanese names that are the primary focus of this book's investment framework. The alpha opportunity for supply chain investors is not in NVIDIA itself but in the undervalued Japanese companies that supply the companies that supply NVIDIA.

---

## Competitive Landscape

The seven companies profiled in this chapter compete across two distinct domains: logic/foundry and memory.

### Logic and Foundry

The foundry market is effectively a monopoly. TSMC holds over 90 percent of advanced-node production and approximately 62-65 percent of the total foundry market by revenue. Samsung Foundry is the only meaningful competitor, with perhaps 10-15 percent of the foundry market, though its share at advanced nodes is much lower. Intel Foundry Services is a nascent entrant with negligible external revenue.

The competitive dynamics are unusual. TSMC's dominance is self-reinforcing: because TSMC produces more wafers at each node, it achieves higher yields faster, which allows it to offer lower prices and better delivery times, which attracts more customers, which produces more wafers, which accelerates learning further. Samsung's inability to close the yield gap at 3nm -- despite being the first to ship GAA transistors -- illustrates how difficult it is to challenge this virtuous cycle.

Intel's ambition to become the world's second-largest foundry by 2030 is theoretically possible -- Intel has the engineering talent, the fab infrastructure, and the CHIPS Act funding. But the path from negative operating margins to competitive foundry services requires years of flawless execution, and Intel's track record in the 2015-2023 period does not inspire confidence. The market appears to agree: only 4 out of 45 analysts rate Intel a buy.

### Memory

The memory market is an oligopoly with three participants: Samsung (approximately 40 percent DRAM share), SK Hynix (approximately 30 percent), and Micron (approximately 25 percent). In NAND, Kioxia and Western Digital add two more players, though Kioxia's 14 percent share puts it in the number three or four position depending on cycle dynamics.

The competitive dynamics in memory have been transformed by HBM. Traditional DRAM is a commodity -- buyers can substitute between Samsung, SK Hynix, and Micron products with relative ease, and pricing is driven by supply-demand balance rather than differentiation. HBM is fundamentally different. Qualifying an HBM product with a customer like NVIDIA requires months of testing and validation. SK Hynix's 50-plus percent HBM market share and its projected 70 percent share of HBM4 for the Rubin platform represent a structural competitive advantage that Samsung and Micron will find extremely difficult to erode in the near term.

This HBM dominance is why SK Hynix scores 73.0 in our framework -- third overall and far above any other large-cap semiconductor company. The combination of deep valuation (PER 5.59x), structural growth (102 percent revenue growth), and market leadership in the highest-demand product category is rare.

---

## Supply Chain Connections

The supply chain connections mapped in this chapter complete the circuit that runs through the entire book. The flow is:

**Japanese suppliers (Chapters 4-15)** sell to **demand engines (this chapter)** which manufacture chips purchased by **end customers (hyperscalers, OEMs, consumers)**.

### Upstream: Who Feeds the Demand Engines

Every process chapter in this book describes suppliers to the companies profiled here:

- **Chapter 4 (Silicon Wafers):** Shin-Etsu and SUMCO supply wafers to all five chipmakers (TSMC, Samsung, Intel, SK Hynix, Micron). No wafers, no chips.
- **Chapter 5 (UPW & Gases):** Organo provides 100 percent of TSMC's advanced-node ultrapure water. Stella Chemifa's 12-nine HF is used by all five chipmakers. Kanto Denka's fluorine gases are in every etch chamber.
- **Chapters 6-8 (Patterning):** HOYA's EUV mask blanks, Lasertec's inspection tools, TOK and JSR's photoresists -- all flow to TSMC, Samsung, and Intel.
- **Chapters 9-11 (Building the Chip):** Tokyo Electron's coater/developers, Kokusai Electric's batch deposition, SCREEN's wet cleaning, Ebara's CMP systems, Fujimi and Fuso Chemical's slurries -- the core process equipment and materials.
- **Chapter 12 (Infrastructure):** Daifuku's AMHS, Rorze's robots, PILLAR's fittings, NGK's ceramic chucks -- the invisible infrastructure that keeps every fab running.
- **Chapters 13-15 (Back-End):** Advantest's testers, Tokyo Seimitsu's probers, DISCO's dicing saws, Ibiden's substrates -- the final stages before chips reach end customers.

### Downstream: Where the Chips Go

The demand engines profiled here ship their products to the companies that define the AI era:

- TSMC ships processors to Apple (20 percent or more of revenue), NVIDIA, AMD, Qualcomm, MediaTek, and Broadcom.
- Samsung ships memory to data center operators, HBM to NVIDIA (pending certification of HBM4), and mobile processors to its own smartphone division.
- SK Hynix ships HBM directly to NVIDIA -- the most critical single edge in the entire AI supply chain.
- Intel ships CPUs to PC OEMs and data center operators.
- Micron ships memory to data center operators, PC OEMs, and automotive companies.
- Kioxia ships NAND flash and SSDs to Apple and data center operators.
- NVIDIA ships GPUs to Microsoft, Amazon, Google, Meta, and CoreWeave.

### Cross-References to Earlier Chapters

Readers interested in the supply chain dependencies described here are encouraged to trace them backward:

- For the TSMC-Organo relationship (100 percent of advanced-node UPW): see Chapter 5.
- For the SK Hynix-Hanmi Semiconductor relationship (71 percent HBM TC bonder share): see Chapter 15.
- For the NVIDIA-Ibiden relationship (50 percent or more of AI server substrates): see Chapter 15.
- For the common dependencies on Shin-Etsu and SUMCO wafers: see Chapter 4.
- For the common dependencies on Lasertec EUV mask inspection: see Chapter 7.

---

## The Demand Dependency Matrix

The following matrix summarizes the incoming supplier edge counts for each demand engine, segmented by supplier origin:

| Company | Total Supplier Edges | From Japan | From Korea | From Other | Japan % |
|---------|---------------------|-----------|-----------|-----------|---------|
| Samsung Electronics | 44 | 34 | 9 | 1 (ASML) | 77% |
| TSMC | 40 | 38 | 1 | 1 (ASML) | 95% |
| Intel | 28 | 25 | 1 | 2 (ASML, other) | 89% |
| SK Hynix | 22 | 13 | 8 | 1 (ASML) | 59% |
| Micron | 12 | 9 | 2 | 1 (ASML) | 75% |
| Kioxia | 5 | 4 | 0 | 1 (WD, USA) | 80% |
| NVIDIA | 4 | 1 (Ibiden) | 2 | 1 (TSMC, Taiwan) | 25% |

Several patterns emerge from this matrix:

**Japan dominates the supply chain for every chipmaker.** Even SK Hynix, with the deepest Korean domestic supply chain of any chipmaker, sources 59 percent of its mapped suppliers from Japan. TSMC's 95 percent Japan share is remarkable for a Taiwanese company -- it reflects the near-total absence of a Taiwanese semiconductor materials and equipment industry.

**ASML is the lone non-Japanese, non-Korean universal supplier.** Every chipmaker except Kioxia and NVIDIA has a direct ASML edge, reflecting the Dutch company's EUV lithography monopoly. ASML is the only non-Asian company that appears as a supplier to all major chipmakers.

**Samsung has the most diverse supply chain.** Samsung's 9 Korean supplier edges reflect a deliberate strategy to develop domestic alternatives, including captive subsidiaries like SEMES. However, for the most critical process steps, Japanese suppliers remain irreplaceable.

**NVIDIA's minimal direct footprint magnifies its indirect impact.** NVIDIA's 4 direct edges understate its true supply chain footprint by orders of magnitude. Every GPU NVIDIA ships activates TSMC's full 40-supplier chain plus SK Hynix's 22-supplier chain plus Ibiden's substrate supply chain.

---

## Key Takeaways

- **Three business models define the semiconductor industry.** Foundries (TSMC) manufacture for others, IDMs (Samsung, Intel, SK Hynix, Micron, Kioxia) design and manufacture their own chips, and fabless companies (NVIDIA) design chips but outsource all manufacturing. The foundry and IDM models are the direct customers of Japan's supply chain.

- **Japan supplies 59-95 percent of the mapped supply chain for every major chipmaker.** TSMC's 40 incoming supplier edges include 38 from Japan. Samsung's 44 edges include 34 from Japan. Even SK Hynix, with the strongest Korean domestic ecosystem, sources 59 percent of its mapped suppliers from Japan. Regardless of which company builds the next leading-edge fab, Japanese suppliers win.

- **The AI capex supercycle amplifies demand through four tiers.** End demand from hyperscalers flows to NVIDIA (chip design), then to TSMC and memory makers (chip manufacturing), then to equipment and materials companies (Tier 3), and finally to component and chemical suppliers (Tier 4). Each tier amplifies the demand signal, creating structural growth for the entire Japanese supply chain.

- **SK Hynix is the standout investment among the demand engines.** With a score of 73.0 (third overall), PER of 5.59x, 102 percent revenue growth, and 50 percent or more HBM market share, SK Hynix combines structural growth, market dominance, and deep valuation in a way that no other large-cap semiconductor company matches.

- **Kioxia is Japan's last chipmaker -- and it matters.** As the only Japanese company among the seven demand engines, Kioxia represents the final link between Japan's semiconductor manufacturing heritage and its current supply chain dominance. The Western Digital JV provides capital efficiency, and NAND recovery provides cyclical upside, but Kioxia's strategic significance extends beyond its financial profile.

---

*Data sources: CMP-0017 (TSMC), CMP-0018 (Samsung Electronics), CMP-0019 (Intel), CMP-0020 (SK Hynix), CMP-0021 (Micron), CMP-0014 (Kioxia), CMP-0028 (NVIDIA), graph.json (321 edges), evaluation_progress.json (74 scored companies)*
