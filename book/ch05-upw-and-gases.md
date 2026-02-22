# Chapter 5: Ultrapure Water & Specialty Gases

> Every advanced semiconductor fab consumes millions of liters of water per day and dozens of specialty gases per process step -- and impurities measured in parts per trillion can destroy an entire production lot.

## Introduction

A modern semiconductor fabrication plant is, at its core, a temple of purity. The transistors etched into a silicon wafer at the 3-nanometer node are roughly fifteen atoms wide. At this scale, a single stray particle of sodium, a molecule of dissolved silica, or a trace of metal ion in the wrong place at the wrong time does not merely degrade performance -- it kills the chip. The manufacturing environment must be controlled to levels of cleanliness that exceed anything else in industrial history, and the two most fundamental inputs to that environment are water and gas.

Water is the semiconductor industry's universal solvent. A 300-millimeter fab performing advanced logic manufacturing uses between 30,000 and 50,000 cubic meters of ultrapure water per day -- enough to supply a small city. This water is used in nearly every step of the process: rinsing wafers after chemical-mechanical planarization, diluting etchants to precise concentrations, cleaning photoresist residue after development, and flushing wet processing tools between batches. But the water that enters a fab bears no resemblance to the water that comes from a municipal tap. Semiconductor-grade ultrapure water -- referred to throughout the industry as UPW -- must meet purity standards so extreme that measuring the impurities requires specialized instrumentation capable of detecting individual atoms. The specification for leading-edge UPW is a resistivity of 18.2 megaohm-centimeters (the theoretical maximum for pure water at 25 degrees Celsius), with total organic carbon below 1 part per billion, dissolved metals below 1 part per trillion, and particle counts in the single digits per liter at the 10-nanometer size threshold.

Specialty gases are equally critical. The deposition, etching, and doping steps that build up the layers of a semiconductor device each require specific gaseous precursors delivered at extraordinarily high purity. Silane (SiH4) is decomposed to deposit silicon dioxide insulating layers. Tungsten hexafluoride (WF6) provides the tungsten that fills contact vias. Nitrogen trifluoride (NF3) cleans the deposition chambers between runs. Fluorine-based gases such as carbon tetrafluoride (CF4), hexafluoroethane (C2F6), and octafluorocyclobutane (C4F8) etch specific materials with atomic-level selectivity. And at the extreme end of the purity spectrum sits hydrofluoric acid -- not a gas in its final application but a product of fluorine chemistry -- whose role in oxide etching and wafer cleaning makes it perhaps the single most strategically important chemical in the entire semiconductor supply chain.

Japan dominates both of these domains. The country's three largest UPW system providers -- Organo Corporation, Kurita Water Industries, and Nomura Micro Science -- together control over eighty percent of the global semiconductor UPW market. In specialty gases, Nippon Sanso Holdings ranks among the world's top three suppliers of electronics-grade gases, while Kanto Denka Kogyo produces over fifteen types of specialty fluorine gases from proprietary electrolysis technology that competitors cannot easily replicate. And in ultra-high-purity hydrofluoric acid, the Stella Chemifa and Morita Chemical duopoly represents one of the tightest supply bottlenecks in the entire industry: only these two Osaka-based companies can produce HF at twelve-nine purity -- 99.9999999999 percent pure -- the grade required for etching features at the most advanced process nodes.

This chapter examines the science behind these purity requirements, profiles the key Japanese companies that meet them, and explains why their positions are among the most structurally defensible in the semiconductor supply chain.

---

## The Science of Ultrapure Water

### Why Water, and Why So Pure?

Water's role in semiconductor manufacturing is both ancient and irreplaceable. The silicon dioxide that forms the basis of transistor gate insulators, the metal interconnect layers that carry signals across a chip, and the photoresist patterns that define circuit geometries must all be cleaned, rinsed, or developed using water at some point in the process. A single leading-edge logic wafer undergoes hundreds of wet processing steps. The total water consumption of the global semiconductor industry exceeds 250 billion liters per year, a figure that is growing rapidly as new fabs come online to meet AI-driven demand.

The purity imperative arises from physics. A transistor gate at the 3-nanometer node is composed of perhaps a few hundred atoms of carefully doped silicon and hafnium oxide. If a single atom of sodium, potassium, or iron is deposited on that gate during a rinse step, it will alter the electrical threshold voltage, causing the transistor to switch at the wrong voltage or, worse, to fail entirely. At the 7-nanometer node, semiconductor-grade UPW specifications required total metallic impurities below 10 parts per trillion. At 3 nanometers and below, the industry is pushing toward sub-1 part per trillion specifications -- that is, fewer than one impurity atom per trillion water molecules. To put this in physical terms, one part per trillion is equivalent to a single drop of ink dissolved in twenty Olympic swimming pools. Finding and removing that drop is the job of the ultrapure water system.

### The UPW Purification Train

Converting municipal source water into semiconductor-grade UPW is a multi-stage process that typically involves the following sequence:

**Pre-treatment.** Raw water from rivers, reservoirs, or wells is first treated with coagulants to remove suspended solids, then passed through multimedia filters. This stage reduces turbidity and removes the bulk of organic matter.

**Reverse osmosis (RO).** Water is forced through semi-permeable membranes at high pressure. Modern RO membranes reject 99.5 percent or more of dissolved salts, organics, and particles. Leading-edge fabs use double-pass or even triple-pass RO systems to achieve progressively higher rejection rates.

**Electrodeionization (EDI).** After RO, remaining ionic impurities are removed by EDI modules, which use ion exchange resins and an applied electric field to continuously regenerate the resin beds without chemical dosing. Organo's proprietary D2EDI (double-pass electrodeionization) system is specifically designed for semiconductor-grade purification.

**UV oxidation.** Ultraviolet light at 185 nanometers and 254 nanometers is used to break down trace organic compounds that survive RO and EDI. The UV system oxidizes organics to carbon dioxide and water, reducing total organic carbon (TOC) to sub-ppb levels.

**Ion exchange polishing.** The final stage passes water through nuclear-grade mixed-bed ion exchange resin columns. These columns remove the last traces of ionic contamination, bringing resistivity to the theoretical maximum of 18.18 megaohm-centimeters.

**Ultrafiltration (UF).** Point-of-use ultrafilters with pore sizes below 10 nanometers remove any particles or colloids that may have been introduced by the resin beds or distribution piping.

The entire system must be constructed from materials that do not leach impurities into the water -- high-purity PFA (perfluoroalkoxy) piping, PVDF (polyvinylidene fluoride) valves, and electropolished stainless steel tanks. The distribution loop that carries UPW from the purification plant to the individual process tools must maintain constant recirculation at controlled temperature and flow rate to prevent bacterial growth and recontamination. A single stagnant zone in the piping can breed bacteria that release organic compounds, ruining the water quality and forcing a costly system shutdown and decontamination cycle.

### The Scale Challenge

The economics of UPW production are dominated by scale. A large 300-millimeter logic fab operating at full capacity requires a UPW system capable of producing 10,000 to 15,000 cubic meters per hour -- a flow rate comparable to a medium-sized municipal water treatment plant, but at purity levels roughly a million times higher. Building such a system requires an investment of tens of billions of yen and a lead time of 1.5 to 2 years. Once installed, the system generates ongoing revenue through chemical consumables (ion exchange resins, RO membranes, UV lamp replacements), maintenance services, and increasingly, water recycling operations that recover and re-purify spent UPW to reduce consumption.

Water scarcity is becoming a strategic factor in fab siting decisions. TSMC's Arizona fabs operate in a desert climate where freshwater is scarce and expensive. Taiwan itself experiences periodic droughts that have forced TSMC to truck water to its fabs. Semiconductor companies are investing heavily in UPW recycling -- recovering 85 to 95 percent of process wastewater for re-purification -- and the companies that design and operate these recycling systems hold an increasingly valuable position in the supply chain.

---

## The Specialty Gas Landscape

### Bulk Gases vs. Specialty Gases

The gases used in semiconductor manufacturing fall into two categories. Bulk gases -- nitrogen, oxygen, argon, hydrogen, and helium -- are consumed in enormous volumes for atmospheric control, purging, and as carrier gases. A leading-edge fab may consume hundreds of thousands of cubic meters of nitrogen per day to maintain the inert atmosphere in its cleanroom and process tools. These bulk gases are typically supplied by on-site air separation units operated by industrial gas companies under long-term contracts.

Specialty gases, sometimes called electronic-grade gases, are consumed in much smaller volumes but at far higher purity and at significantly higher prices. These include:

- **Etch gases:** Carbon tetrafluoride (CF4), hexafluoroethane (C2F6), octafluorocyclobutane (C4F8), sulfur hexafluoride (SF6), nitrogen trifluoride (NF3), chlorine (Cl2), boron trichloride (BCl3), and hydrogen bromide (HBr). Each gas etches specific materials with different selectivity profiles, and the choice of etch gas determines the shape, depth, and smoothness of the features being cut.

- **Deposition gases:** Silane (SiH4), dichlorosilane (SiH2Cl2), tetraethyl orthosilicate (TEOS), tungsten hexafluoride (WF6), trimethylaluminum (TMA), and various metal-organic precursors for ALD (atomic layer deposition). These decompose in CVD and ALD chambers to deposit thin films of silicon dioxide, silicon nitride, tungsten, aluminum oxide, and other materials atom by atom.

- **Doping gases:** Phosphine (PH3), arsine (AsH3), diborane (B2H6), and boron trifluoride (BF3). These introduce controlled concentrations of dopant atoms into silicon to create the p-type and n-type regions that form transistors.

- **Chamber cleaning gases:** NF3, CF4, and ClF3 are used to clean deposition chambers between runs by converting residual films into volatile fluoride or chloride compounds that can be pumped away.

### Purity Requirements for Specialty Gases

The purity requirements for specialty gases have tightened with each process node shrinkage. At the 7-nanometer node, most etch and deposition gases must meet SEMI Grade 5 specifications: total impurities below 10 parts per million (ppm), with individual metallic impurities below 1 part per billion (ppb). At 3 nanometers and below, fabs increasingly demand custom specifications that exceed published SEMI standards, with metallic impurities below 100 parts per trillion (ppt) and moisture content below 50 ppb.

Achieving these purity levels requires specialized manufacturing processes. Fluorine-based gases, for example, are typically produced by electrochemical fluorination -- passing an electric current through anhydrous hydrogen fluoride to generate fluorine gas, which is then reacted with carbon-containing precursors under carefully controlled conditions. The electrolysis technology itself is a critical differentiator. Companies that have mastered large-scale fluorine electrolysis with consistent purity can produce a wide portfolio of fluorinated gases from a common manufacturing platform, while competitors without this capability must license or import the fluorine feedstock at higher cost and lower quality control.

### Hydrofluoric Acid: The Crown Jewel of Semiconductor Chemistry

Hydrofluoric acid occupies a unique position in semiconductor chemistry. It is the only common acid that dissolves silicon dioxide, the fundamental dielectric material in semiconductor devices. This property makes HF indispensable for two critical process steps:

**Oxide etching.** When circuit patterns are defined by photolithography, HF-based solutions selectively remove exposed silicon dioxide while leaving underlying silicon or metal layers intact. The etching rate, uniformity, and selectivity depend critically on HF concentration and purity.

**Wafer cleaning.** The standard RCA cleaning sequence, used universally in semiconductor manufacturing since the 1970s, includes a dilute HF step (typically 1:100 or 1:200 HF:water) to remove native oxide and metallic contamination from the wafer surface. At advanced nodes, this cleaning step must not introduce any new contamination, which means the HF itself must be essentially free of dissolved metals.

The purity scale for electronic-grade HF is measured in "nines" -- the number of nines after the decimal point in the purity percentage. Consumer-grade HF might be 99 percent pure (two nines). Industrial-grade HF used in glass etching is typically four to five nines (99.99-99.999 percent). Semiconductor-grade HF at the mature nodes (28nm and above) requires nine to ten nines. And at the most advanced nodes -- 7nm, 5nm, 3nm, and the forthcoming 2nm generation -- the industry demands twelve-nine purity: 99.9999999999 percent. At this level, the HF contains fewer than one impurity atom per trillion molecules.

Producing HF at twelve-nine purity requires mastery of the entire production chain: sourcing high-purity fluorite (CaF2), reacting it with sulfuric acid under contamination-free conditions, distilling the crude HF multiple times to remove volatile impurities, and then subjecting the distillate to a proprietary final purification step that removes the last traces of arsenic, boron, sodium, iron, and other metals to sub-ppt levels. The know-how to achieve this has been accumulated over a century of fluorine chemistry, and it cannot be reverse-engineered from published literature. This is why only two companies in the world can do it.

---

## Company Profiles

### Organo Corporation (6368.T) -- Ultrapure Water Systems for the World's Most Advanced Fabs

**Founded:** 1946 | **HQ:** Tokyo, Japan | **Market Cap:** 770 billion yen

Organo Corporation is the world's second-largest provider of ultrapure water systems for semiconductor manufacturing, with an estimated 20 to 30 percent global market share. But raw market share figures understate Organo's strategic significance. The company's defining competitive advantage is its relationship with TSMC, the world's largest and most advanced contract chipmaker: Organo supplies 70 to 80 percent of all TSMC water treatment plants, and one hundred percent of TSMC's UPW installations at the 10-nanometer node and below.

This last figure bears repeating. Every wafer that TSMC manufactures at its most advanced process nodes -- the chips inside Apple's latest iPhones, NVIDIA's AI accelerators, AMD's data center processors, and Qualcomm's mobile SoCs -- is rinsed, cleaned, and processed using ultrapure water produced by Organo systems. There is no alternative supplier for these installations. The switching cost is not merely financial; it is existential. Replacing a UPW system at a running fab would require shutting down production for months, requalifying every process recipe with new water chemistry, and accepting the risk that the replacement system might introduce contaminants that were absent in the original. No fab manager would take that risk.

Organo was founded in 1946 and became a subsidiary of Tosoh Corporation (4042.T), a major chemical company, which has held approximately 44 percent of Organo's shares since 1955. This parent relationship provides strategic benefits -- Tosoh produces ion exchange resins through its Tosoh Bioscience division, a key consumable input for UPW systems -- while constraining Organo's free float to approximately 54 percent of outstanding shares.

The company's product portfolio extends well beyond UPW system construction. Organo manufactures its own ORLITE brand ion exchange resins (the DS series for semiconductor-grade purification, the DRY series for organic solvent purification), D2EDI electrodeionization modules, and specialty chemical recovery systems including HF acid recovery, TMAH (tetramethylammonium hydroxide) recovery, rare metal recovery, and NMP (N-methyl-2-pyrrolidone) solvent recycling via membrane separation. These capabilities position Organo not just as a system builder but as a full-service water and chemical management provider for semiconductor fabs.

Organo operates approximately 100 semiconductor UPW plants across eight countries. TSMC accounts for roughly 14 percent of Organo's total revenue in FY2025/3, with the remainder coming from other semiconductor fabs, pharmaceutical companies, power plants, and food and beverage operations (including sugar refinery decolorization). The geographic revenue split is approximately 60 percent Japan, 17 percent Taiwan, 13 percent China, and 10 percent rest of world.

The growth trajectory is extraordinary. Organo's current expansion pipeline directly mirrors TSMC's global fab buildout: UPW and wastewater treatment systems for TSMC's JASM fab in Kumamoto, Japan (Phase 1 operational December 2024, Phase 2 targeted for end of 2027); the TSMC Arizona fab in the United States, where Organo USA Inc. (established in 2021) opened a dedicated Arizona office to serve this project and pursue other American semiconductor customers; and the TSMC ESMC fab in Dresden, Germany, where Organo is executing water treatment projects for TSMC's European expansion.

Beyond TSMC, Organo has secured the UPW contract for Rapidus, Japan's national project to manufacture 2-nanometer-class chips at a new fab in Chitose, Hokkaido. In a strategically significant move, Organo will not merely build but own and operate the water purification facility at the Rapidus site -- a recurring-revenue model that locks in long-term cash flows and represents an evolution toward annuity-like income streams.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 27.1x |
| PBR | 5.85x |
| EPS | 613.06 yen |
| ROE | 21.7% |
| Revenue (FY2025/3) | 163.3 billion yen (+8.6% YoY) |
| Operating Profit (FY2025/3) | 31.1 billion yen (+38.0% YoY) |
| Operating Margin | 19.1% |
| Foreign Ownership | 22.5% |
| FY2026/3 Revenue Guidance | 175 billion yen |
| FY2026/3 Order Guidance | 185 billion yen (+22.3% YoY) |

Organo's financial profile reflects the quality of the business. Its 19.1 percent operating margin significantly exceeds the G1 Semiconductor Equipment peer group median of 14.9 percent, and its 21.7 percent ROE is nearly three times the peer average. Revenue growth at 8.6 percent appears modest, but this is an artifact of project-based accounting: large UPW installations have lead times of 1.5 to 2 years and recognize revenue on a percentage-of-completion basis. The order pipeline of 185 billion yen -- 22.3 percent above the prior year -- provides visibility into revenue growth through FY2028. The stock has risen approximately 134 percent over the past twelve months, reflecting the market's belated recognition of Organo as a pure-play TSMC infrastructure proxy.

#### Investment Perspective

Organo holds one of the most extraordinary customer lock-ins in the semiconductor supply chain. The 100 percent share of TSMC's advanced-node UPW installations creates a flywheel: every new TSMC fab anywhere in the world generates near-automatic revenue for Organo. The company's moat score of B=24 out of 25 in the evaluation framework reflects this position -- monopoly-grade market share at TSMC, extreme switching costs (requalification of UPW chemistry takes months and risks yield loss), and decades of accumulated purification expertise.

The primary catalyst is the foreign ownership gap. At 22.5 percent foreign ownership against an expected level of 45 percent or more for a company with near-maximum moat scores, there is roughly 22.5 percentage points of potential institutional buying as global semiconductor fund managers recognize Organo as one of the most direct plays on TSMC's expansion. Additional catalysts include TSMC fab ramp-ups across Kumamoto, Arizona, and Dresden; the Rapidus build-own-operate model, which could be replicated at future fab projects; and the broader AI-driven capex boom that drives demand for every advanced fab, and hence for every Organo UPW system.

The valuation concern is real. At 5.85x PBR -- an extreme premium of 2.35x the G1 peer median of 2.49x -- Organo is the most expensive stock by price-to-book in its peer group. The stock trades near its all-time high and above the average analyst price target of 16,250 yen. TSMC concentration risk is significant: while TSMC represents only 14 percent of total revenue, it constitutes 70 to 80 percent of Organo's semiconductor UPW business. Geopolitical risk from Greater China exposure (approximately 30 percent of revenue) and Tosoh's 44 percent controlling stake, which limits minority shareholder influence, are additional considerations. This is a case of "right company, expensive price" -- the business quality is exceptional, but position sizing should reflect the stretched valuation. The evaluation framework assigns Organo a composite score of 60.0 out of 100.

---

### Nomura Micro Science Co., Ltd. (6254.T) -- The Korean Semiconductor Market's UPW Specialist

**Founded:** 1969 | **HQ:** Kanagawa, Japan | **Market Cap:** 92 billion yen

Where Organo is synonymous with TSMC, Nomura Micro Science has built its UPW franchise around the Korean semiconductor ecosystem. Samsung Electronics and SK Hynix -- the world's dominant DRAM and NAND flash manufacturers -- are Nomura Micro Science's anchor customers. This geographic specialization gives Nomura a clear lane in what is effectively an oligopolistic market.

Nomura Micro Science was founded in 1969 as a pure-play ultrapure water equipment company, and it has maintained that focus for over half a century. Unlike Organo, which serves pharmaceutical, power, and food industries alongside semiconductors, Nomura Micro Science is more narrowly specialized in semiconductor-grade water treatment. This specialization has produced deep expertise in the specific water chemistry requirements of memory fabs, which differ from logic fabs in their heavier use of wet etching processes for high-aspect-ratio 3D NAND channel formation.

The company holds an estimated 10 to 15 percent share of the global semiconductor UPW market, making it the third-largest player behind Kurita Water Industries (35 to 45 percent) and Organo (20 to 30 percent). Together, these three Japanese companies control over 80 percent of the global market -- a concentration that underscores just how deeply Japanese technology is embedded in the most fundamental input to chip manufacturing.

Nomura Micro Science has been an early mover in geographic expansion, establishing operations in Korea before expanding to Taiwan, China, and the United States. The company's water recycling technology is a particular strength, increasingly valuable as fabs face tightening water availability constraints. Record revenues in FY2025 reflect the continued buildout of memory fab capacity by Samsung and SK Hynix, driven by surging demand for HBM (High Bandwidth Memory) used in AI accelerator systems.

The company reported revenue of 73 billion yen in the latest fiscal year, though this figure reflects a -44 percent year-over-year decline from an unusually strong prior year that included large project completions. Operating margin stands at 14.1 percent, consistent with the capital-intensive nature of UPW system delivery projects. ROE of 15.2 percent demonstrates solid capital efficiency.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 34.13x |
| PBR | 2.49x |
| EPS | 100.8 yen |
| ROE | 15.22% |
| Revenue (Latest FY) | 73.02 billion yen |
| Operating Margin | 14.07% |
| Dividend Yield | 2.03% |

The stock has experienced significant volatility, trading between a 52-week low of 1,541 yen and a high of 5,680 yen -- a range that reflects the project-driven nature of UPW revenue and the market's difficulty in assigning a stable multiple to a business with lumpy order flow. Two analysts cover the stock, both with Hold ratings and an average target of 3,315 yen against a current price of 2,428 yen. The evaluation framework assigns Nomura Micro Science a composite score of 44.2 out of 100, reflecting the combination of moderate moat strength (B=11 versus Organo's B=24) and a revenue decline in the latest fiscal year.

---

### Nippon Sanso Holdings Corporation (4091.T) -- Japan's Industrial Gas Champion

**Founded:** 1910 | **HQ:** Tokyo, Japan | **Market Cap:** 2.35 trillion yen

Nippon Sanso Holdings is Japan's largest industrial gas company and ranks among the world's top three suppliers of electronics-related gases. It is part of the Mitsubishi Chemical Group, giving it access to one of Japan's largest chemical conglomerates for both technology development and market access. The company supplies bulk gases (nitrogen, oxygen, argon, hydrogen) and specialty electronic gases to semiconductor fabs globally, including TSMC, Samsung, and Intel.

The semiconductor gas business sits within Nippon Sanso's broader industrial gas operations, which generated revenue of approximately 1.33 trillion yen in the latest fiscal year. The company's scale is its primary competitive advantage: operating on-site air separation units at major fab complexes requires enormous capital investment and multi-year supply contracts, creating a natural barrier to entry that favors the largest players. Nippon Sanso competes globally against Linde (Germany/USA), Air Liquide (France), and Air Products (USA) -- the so-called "Big Three" of industrial gases -- but holds particular strength in the Japanese domestic market and across East Asian semiconductor production zones.

Nippon Sanso's strategic position is expanding alongside the new fab construction cycle. The company is developing ultra-high-purity air separation equipment for new fab projects and is supplying gases for the Rapidus pilot line in Chitose, Hokkaido. As each new leading-edge fab requires both bulk gas supply infrastructure and specialty gas delivery systems, Nippon Sanso benefits from the same global fab buildout that drives Organo's UPW pipeline.

The company's semiconductor-specific gas portfolio includes high-purity nitrogen (the single largest volume gas consumed in a fab), ultra-high-purity argon for sputtering processes, specialty gas mixtures for etching and deposition, and carrier gases for CVD and epitaxy. While individual specialty gases are often sourced from niche producers like Kanto Denka Kogyo, Nippon Sanso's role as the bulk gas infrastructure provider makes it an indispensable partner for every fab -- no cleanroom can operate without a continuous supply of inert gas to maintain its atmosphere.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 22.2x |
| EPS | 264.38 yen |
| ROE | 11.92% |
| Revenue (Latest FY) | 1,330 billion yen (+4.5% YoY) |
| Operating Margin | 13.38% |
| Dividend Yield | 1.1% |

Nippon Sanso's financial profile reflects the characteristics of the industrial gas business: steady but unspectacular revenue growth (4.5 percent), moderate operating margins (13.4 percent), and strong competitive positioning driven by scale and long-term contracts rather than proprietary technology. The PER of 22.2x sits at a premium to the G2 Semiconductor Materials peer median of 17.0x, reflecting the market's appreciation of the company's defensive revenue streams and Mitsubishi Chemical Group parentage. The evaluation framework assigns Nippon Sanso a composite score of 38.8 out of 100, reflecting solid moat characteristics (B=14) but limited valuation upside and moderate growth prospects.

---

### Kanto Denka Kogyo Co., Ltd. (4047.T) -- The Fluorine Gas Portfolio

**Founded:** 1938 | **HQ:** Tokyo, Japan | **Market Cap:** 59.4 billion yen

Kanto Denka Kogyo is a specialty chemical company whose strategic significance to the semiconductor industry derives from a single core capability: proprietary fluorine electrolysis technology. While most specialty gas producers can manufacture three to four types of fluorinated gases, Kanto Denka Kogyo produces over fifteen -- a portfolio breadth that is unmatched in the industry and that flows directly from its mastery of the electrochemical generation of fluorine gas.

Fluorine is the most electronegative element on the periodic table and among the most reactive. Handling it safely at industrial scale requires specialized equipment, rigorous safety protocols, and decades of accumulated process knowledge. Kanto Denka Kogyo, a member of the Furukawa Group (one of Japan's oldest industrial conglomerates, tracing its origins to the copper mining business established by Furukawa Ichibei in 1877), has been refining its fluorine chemistry capabilities for nearly nine decades.

The company's product portfolio includes etch gases used in both dielectric and conductor etching (CF4, C2F6, C4F8, SF6, NF3, and others), chamber cleaning gases, and specialty fluorine compounds used in doping and surface treatment. Each of these gases must be produced at electronic grade -- typically SEMI Grade 5 or higher -- with metallic impurities in the parts-per-billion range and moisture content controlled to sub-ppm levels.

Kanto Denka Kogyo supplies TSMC, Samsung, Intel, and other major fabs directly. The company's competitive moat lies not in any single gas product but in the breadth of its fluorine gas portfolio and the reliability of its supply. A fab that sources multiple etch and cleaning gases from a single qualified supplier reduces its procurement complexity and qualification burden compared to sourcing each gas from a different vendor. This portfolio effect creates meaningful switching costs that individual gas producers cannot replicate.

The company has announced a 400 billion yen investment program for capacity expansion, signaling management's expectation that semiconductor-driven demand for fluorine gases will grow substantially over the coming years. This investment is large relative to the company's 59.4 billion yen market capitalization, indicating a transformative expansion rather than incremental growth.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 25.6x |
| PBR | 0.87x |
| EPS | 33.4 yen |
| ROE | -4.74% |
| Revenue (Latest FY) | 61.2 billion yen (+10.6% YoY) |
| Dividend Yield | 1.53% |

Kanto Denka Kogyo's financial profile presents a mixed picture. Revenue growth of 10.6 percent is solid, and the PBR of 0.87x -- a discount to book value -- suggests the market is skeptical of the company's ability to generate adequate returns on equity. That skepticism is grounded in recent results: ROE of -4.74 percent reflects operating losses or write-downs that weighed on profitability. The stock trades near its 52-week high of 1,130 yen at 1,035 yen, with one analyst covering the name with a Buy rating and a target of 1,300 yen. The evaluation framework assigns Kanto Denka Kogyo a composite score of 49.0, reflecting strong moat characteristics (B=14) and meaningful capacity expansion catalysts (E=9), offset by poor current profitability and limited data coverage. The company's 400 billion yen capex program, if executed successfully, could significantly rerate the stock -- but execution risk on an investment of that magnitude relative to the current market cap is substantial.

---

### Stella Chemifa Corporation (4109.T) -- The Twelve-Nine HF Duopoly

**Founded:** 1916 | **HQ:** Osaka, Japan | **Market Cap:** 68.63 billion yen

Stella Chemifa operates in one of the tightest duopolies in the global semiconductor supply chain. Together with privately held Morita Chemical Industries, also based in Osaka, Stella is one of only two companies on earth that can produce hydrofluoric acid at twelve-nine purity -- 99.9999999999 percent. This is not marketing language. The global electronic-grade HF market has fewer than fifteen capable producers, and the top five control approximately 70 percent of supply, but at the very highest purity tier -- the grade required for etching at 7-nanometer and below -- the market narrows to a two-player duopoly that supplies over 90 percent of Japanese domestic demand and dominates the global ultra-high-purity segment.

Stella Chemifa was founded in 1916 in Osaka and has spent more than a century refining its fluorine chemistry capabilities. The production of twelve-nine HF begins with fluorite ore (calcium fluoride, CaF2), the primary raw material, which is reacted with sulfuric acid to produce crude hydrofluoric acid. This crude product is then subjected to multiple rounds of fractional distillation and proprietary purification steps that progressively remove dissolved metals, silicon, arsenic, boron, and other contaminants until the final product contains fewer than one impurity atom per trillion. The know-how required to achieve this level of purification has been developed iteratively over a hundred years and cannot be replicated through laboratory research alone -- it requires direct manufacturing experience with fluorine chemistry at industrial scale, sophisticated analytical instrumentation capable of measuring sub-ppt impurity levels, and deep understanding of the contamination sources at each stage of the production chain.

The company's client list reads as a directory of the global semiconductor industry. Stella Chemifa supplies ultra-high-purity HF to TSMC, Samsung Electronics, Intel, SK Hynix, Micron Technology, Kioxia, SMIC, Hua Hong Semiconductor, UMC, and GlobalFoundries -- ten major fab operators spanning five countries. When the company states in Japanese-language industry sources that it supplies "almost all domestic semiconductor manufacturers," this is not exaggeration. It is a description of a supply chain position that is as close to universal coverage as any materials company achieves.

Stella Chemifa operates through two business segments: High-Purity Chemicals (86 percent of consolidated sales) and Transportation. Within the chemicals segment, semiconductor applications account for approximately 70 percent of revenue, with the balance split between energy and battery materials (roughly 15 percent, and growing fastest) and optical and general chemicals (roughly 15 percent). The company operates factories in Sakai and Izumi-Otsu (both in Osaka Prefecture) and Kitakyushu (Fukuoka Prefecture), with international manufacturing through subsidiaries in Singapore (Jurong Island) and China (Zhejiang province, through a 55 percent-owned joint venture, Zhejiang Blue Star Chemical, and a subsidiary, Quzhou BDX New Chemical Materials).

Beyond semiconductors, Stella Chemifa manufactures LiPF6 (lithium hexafluorophosphate), the critical electrolyte salt in lithium-ion batteries. The supply chain runs: Stella Chemifa produces LiPF6, which Mitsubishi Chemical formulates into Sol-Rite brand battery electrolyte, which Panasonic uses in battery cell production, which ultimately powers Tesla and other electric vehicles. This creates exposure to the EV megatrend without requiring dedicated capital expenditure. The energy and battery segment roughly doubled in FY2025/3 and represents the company's fastest-growing division.

Additional niche businesses include the production of fluoride compounds for optical lenses (used in stepper lenses for lithography equipment and consumer camera lenses), enriched boron-10 for nuclear fuel storage, and BF3 (boron trifluoride) gas -- of which Stella is Japan's sole manufacturer -- used as a catalyst in organic synthesis. The subsidiary Stella Pharma Corporation pursues BNCT (Boron Neutron Capture Therapy), a novel cancer treatment modality that leverages the company's boron chemistry expertise.

The raw material supply chain presents both a risk and a strategic consideration. Fluorite, the essential feedstock for HF production, is predominantly sourced from China, which produces over 60 percent of the world's supply. Stella has diversified its procurement to include European and Mexican sources -- Orbia/Mexichem operates the world's largest fluorite mine in San Luis Potosi, Mexico, and MINERSA Group supplies from Spain and South Africa -- but Chinese supply chain disruption remains a structural risk.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 21.62x |
| PBR | 1.39x |
| EPS | 244.83 yen |
| ROE | 6.5% |
| Revenue (FY2025/3) | 36.29 billion yen (+19.2% YoY) |
| Operating Profit (FY2025/3) | 4.34 billion yen (+59.4% YoY) |
| Operating Margin | 12.0% |
| Foreign Ownership | 25.93% |
| Dividend Yield | 3.21% |

The financial trajectory shows strong recovery. FY2025/3 revenue grew 19.2 percent year-over-year with operating profit surging 59.4 percent, reflecting both volume growth from the semiconductor upcycle and operating leverage on the relatively fixed cost base of chemical production. ROE at 6.5 percent has recovered from an anomalous 0.3 percent in FY2024/3, which was depressed by a one-time 2.3 billion yen impairment charge. The company's fourth Medium-Term Management Plan targets ROE of 8 percent or above by FY2028/3 and a total shareholder return ratio exceeding 100 percent over three years through a combination of dividends and share buybacks. The dividend yield of 3.21 percent is generous for a semiconductor materials company. The Q3 FY2026/3 operating profit progress rate of 88.9 percent strongly suggests the company's conservative full-year guidance is ripe for upward revision.

#### Investment Perspective

Stella Chemifa is a "moat first, valuation second" investment story. The moat score of B=25 out of 25 -- a perfect score -- reflects the company's position in a genuine duopoly with no viable substitutes at the highest purity tier. Requalification of ultra-pure chemicals at a semiconductor fab takes 12 to 18 months per customer, creating switching costs that are measured not in dollars but in lost production time. The 2019 episode, when Japan imposed export restrictions on HF, photoresist, and fluorinated polyimide shipments to South Korea, provided a live demonstration of the irreplaceability of Japanese ultra-high-purity chemicals: Samsung and SK Hynix were unable to find alternative twelve-nine HF sources and spent years attempting to build supply chain diversification that remains incomplete.

The foreign ownership gap is a structural catalyst. At 25.9 percent foreign ownership against an expected 45 percent or more for a company with maximum moat scores, there is roughly 19 percentage points of potential institutional buying as global funds discover this name. Additional catalysts include the global fab buildout (TSMC Arizona, Kumamoto, Dresden; Intel Ohio and Germany; Samsung Taylor, Texas; Rapidus Chitose; Micron Hiroshima expansion), guidance revisions as Q3 progress rates virtually guarantee upward adjustments, and the LiPF6 battery electrolyte optionality.

The risks are equally clear. Chinese electronic-grade HF producers, particularly Do-Fluoride New Materials (002407.SZ), have reportedly reached UP-SSS (G5) grade -- the highest purity classification -- potentially threatening the Stella/Morita duopoly over the medium term. Fluorite sourcing dependency on China (60 percent or more of global supply) is a structural vulnerability. ROE of 6.5 percent remains below the company's own cost of equity. And with the stock having rallied 42 percent over the past year, the PER of 21.62x now sits at a 27 percent premium to the G2 Materials peer median of 17.0x, indicating the market has partially priced in the moat. The evaluation framework assigns Stella Chemifa a composite score of 60.5 out of 100.

---

## Competitive Landscape

### Ultrapure Water: A Three-Player Japanese Oligopoly

The global semiconductor UPW market is effectively controlled by three Japanese companies. Kurita Water Industries (6370.T) holds the largest share at an estimated 35 to 45 percent, followed by Organo at 20 to 30 percent and Nomura Micro Science at 10 to 15 percent. Together they account for over 80 percent of the global market.

Kurita is the primary competitive threat to Organo. It is larger, with broader geographic diversification, stronger standardized equipment offerings, and more aggressive pricing. Kurita's strength lies in North America and Europe, where its brand recognition and service infrastructure give it advantages that Organo is only now beginning to build through its US and European TSMC expansion projects. However, Kurita has not been able to displace Organo at TSMC's advanced nodes -- a testament to the depth of Organo's relationship and the extreme risk-aversion that governs UPW supplier selection at leading-edge fabs.

The competitive landscape shifted in December 2025 when Ecolab (ECL) acquired Ovivo's Electronics UPW business for 1.8 billion dollars, creating a well-capitalized American competitor with approximately 500 million dollars in semiconductor UPW revenue. Xylem's 2023 acquisition of Evoqua for 7.5 billion dollars added another substantial Western competitor. Veolia of France co-dominates the broader global UPW market. DuPont Water Solutions offers competing MEGA technology for semiconductor applications.

Despite this consolidation among Western competitors, the Japanese oligopoly remains entrenched at the leading edge. The reason is straightforward: UPW system qualification at an advanced fab is a 1.5 to 2 year process involving extensive water chemistry testing, tool compatibility verification, and yield correlation analysis. Once a UPW system is qualified and production is running, the cost of switching -- both financial and in terms of yield risk -- far exceeds any savings that a new entrant might offer. The installed base advantage is self-reinforcing: each new qualified installation builds the reference base that wins the next project.

Nomura Micro Science occupies a distinct niche. Its Samsung and SK Hynix relationships give it a defensible position in the Korean memory manufacturing ecosystem that neither Organo nor Kurita can easily contest. The Korean market preferences are well-established: Samsung works with Nomura, TSMC works with Organo, and this geographic segmentation of the oligopoly appears stable.

Emerging Chinese competitors -- Hangzhou Ouquan, Shenzhen Jianghui Environmental Protection Technology, and Shenzhen Hongsen Environmental Protection Technology -- are beginning to appear in the domestic Chinese market, potentially threatening the Japanese oligopoly's position at Chinese fabs (SMIC, Hua Hong). However, these companies lack the track record and qualification history needed to win business at the most advanced nodes, and the Chinese fab ecosystem itself remains several generations behind the leading edge.

### Specialty Gases: Scale Players and Niche Specialists

The specialty gas market is more fragmented than UPW, with competition occurring along two axes: bulk gas infrastructure (dominated by the global Big Three of Linde, Air Liquide, and Air Products, plus Nippon Sanso as the fourth major player) and niche fluorine gases (where Kanto Denka Kogyo, Showa Denko (now Resonac), and various regional specialists compete).

Nippon Sanso's competitive position is strongest in the Japanese domestic market and across East Asian semiconductor production zones, where its Mitsubishi Chemical Group parentage provides procurement advantages and customer relationships. In global markets, Nippon Sanso competes primarily on the basis of its electronics gas portfolio breadth and its ability to provide integrated bulk-plus-specialty gas supply solutions.

Kanto Denka Kogyo's competitive advantage is its fluorine electrolysis platform, which supports the production of over fifteen specialty gases versus the three to four that most competitors can produce. This breadth creates a portfolio moat: fabs prefer to consolidate their fluorine gas procurement with a single qualified supplier, and Kanto Denka's catalog is the deepest available.

### Hydrofluoric Acid: The Two-Firm Ceiling

The competitive dynamics of the ultra-high-purity HF market are unique in the semiconductor supply chain. At the twelve-nine purity tier, competition is effectively limited to Stella Chemifa and Morita Chemical Industries. This is not a market share battle in the conventional sense -- it is a capability ceiling that only two organizations have reached.

Below the twelve-nine tier, competition is broader. Daikin Industries (6367.T) produces high-purity HF leveraging its vertical integration in fluorine chemicals and fluorspar resources. Honeywell (HON) and Solvay (SOLB.BR) are identified as leading global producers. In China, Do-Fluoride New Materials (002407.SZ) has reportedly achieved UP-SSS (G5) grade quality and is expanding capacity aggressively. Other Chinese producers including Jiangyin Jianghua Microelectronics Materials, Zhejiang Kaiheng Electronic Materials, Shaowu Fluoride, and Yingpeng Group are building out electronic-grade HF capacity.

The Chinese competitive threat is the most significant strategic risk to the Stella/Morita duopoly. If Chinese producers can consistently manufacture and deliver twelve-nine grade HF at scale, the pricing power and market share of the Japanese duopoly would erode. However, the qualification barrier remains formidable: even if a Chinese producer demonstrates twelve-nine quality in the laboratory, achieving consistent production at that level and passing the multi-month qualification process at a leading-edge fab are substantially different challenges. Japanese producers benefit from their decades-long track record and the extreme risk-aversion of fab operators when it comes to changing wet chemistry suppliers.

---

## Supply Chain Connections

### Upstream Dependencies

The companies in this chapter sit at the beginning of the semiconductor manufacturing value chain, requiring inputs that are largely commodity or near-commodity:

**For UPW systems:** The primary inputs are RO membranes (likely sourced from DuPont/FilmTec, Toray Industries, or Nitto Denko/Hydranautics), ion exchange resins (Organo manufactures its own ORLITE brand; Tosoh's Bioscience division is also a source), ultrafilter membranes (Pall Corporation, a Danaher subsidiary), and construction materials including high-purity PFA piping and PVDF valves. The fluororesin fittings discussed in Chapter 10 -- dominated by PILLAR Corporation (CMP-0042) -- are a critical component in UPW distribution piping, creating a direct upstream link from the wet cleaning chapter to this one.

**For specialty gases:** The primary inputs are atmospheric air (for bulk gas production via air separation), fluorite ore and sulfuric acid (for fluorine-based gas production), and various hydrocarbon and halogenated precursors. Nippon Sanso's Mitsubishi Chemical Group relationship provides integrated access to many of these feedstocks.

**For ultra-high-purity HF:** Fluorite (CaF2) is the essential raw material. Stella Chemifa sources from China (over 60 percent of global supply), Europe (MINERSA Group in Spain/South Africa), and Mexico (Orbia/Mexichem). Sulfuric acid, a commodity chemical, is the other key input.

### Downstream Customers

The supply chain graph from the IndustryMap database reveals the following edges for this chapter's companies:

**Organo (CMP-0052):** Supplies ultrapure water systems to TSMC (CMP-0017), Samsung (CMP-0018), SMIC (CMP-0066), and Hua Hong Semiconductor (CMP-0070). The TSMC relationship is the defining edge: Organo's 100 percent share of TSMC's advanced-node UPW is one of the most concentrated supplier dependencies in the entire graph.

**Nomura Micro Science (CMP-0053):** Supplies ultrapure water systems to TSMC (CMP-0017), Samsung (CMP-0018), and SK Hynix (CMP-0020). The Samsung and SK Hynix edges are the primary relationships, establishing Nomura's Korean market focus.

**Nippon Sanso (CMP-0032):** Supplies specialty gases to TSMC (CMP-0017), Samsung (CMP-0018), Intel (CMP-0019), SK Hynix (CMP-0020), and Micron (CMP-0021). The five-fab coverage reflects the universal requirement for industrial gas supply at every semiconductor fab.

**Kanto Denka Kogyo (CMP-0045):** Supplies specialty fluorine gases to TSMC (CMP-0017), Samsung (CMP-0018), and Intel (CMP-0019). The three-fab coverage reflects the company's focus on the largest and most advanced fab operators.

**Stella Chemifa (CMP-0044):** Supplies twelve-nine purity HF acid to TSMC (CMP-0017), Samsung (CMP-0018), Intel (CMP-0019), SK Hynix (CMP-0020), and Micron (CMP-0021), plus Kioxia (CMP-0014), SMIC (CMP-0066), Hua Hong (CMP-0070), UMC (CMP-0102), and GlobalFoundries (CMP-0106). With ten fab-operator edges, Stella Chemifa has the densest customer graph in this chapter and one of the densest in the entire supply chain database.

### Connections to Other Chapters

The materials covered in this chapter feed directly into virtually every subsequent process step in the book:

- **Chapter 4 (Silicon Wafers):** Wafer polishing and cleaning require both UPW and dilute HF solutions.
- **Chapters 6-8 (Lithography, Photomasks, Photoresist):** Photoresist development and post-exposure bake cleaning consume large volumes of UPW. Photomask cleaning uses specialty chemicals including HF-based solutions.
- **Chapter 9 (Deposition):** CVD and ALD processes consume specialty gases as precursors and chamber cleaning agents. The fluorine-based gases from Kanto Denka Kogyo are direct inputs to deposition tool operation.
- **Chapter 10 (Etching & Cleaning):** The most direct downstream connection. Wet etching uses dilute HF, and wet cleaning uses UPW in massive quantities. The SCREEN Holdings cleaning tools discussed in Chapter 10 are fed by the UPW systems discussed here.
- **Chapter 11 (CMP):** Post-CMP cleaning is one of the largest consumers of UPW in a fab, as slurry residues must be completely removed from the wafer surface.
- **Chapter 12 (Fab Infrastructure):** UPW distribution piping and gas delivery systems are part of the fab infrastructure that enables process tools to operate.

---

## Key Takeaways

- **Ultrapure water is the semiconductor industry's most consumed material by volume.** A leading-edge 300mm fab uses 30,000 to 50,000 cubic meters per day at a purity level of fewer than 1 part per trillion metallic impurities. Three Japanese companies -- Kurita, Organo, and Nomura Micro Science -- control over 80 percent of the global semiconductor UPW market.

- **Organo's TSMC lock-in is one of the most extraordinary supplier relationships in the supply chain.** With 100 percent of TSMC's advanced-node UPW installations, Organo benefits automatically from every new TSMC fab anywhere in the world -- Kumamoto, Arizona, Dresden, and beyond. The switching cost is effectively infinite at a running fab.

- **The twelve-nine HF duopoly is an irreplaceable bottleneck.** Only Stella Chemifa and Morita Chemical Industries can produce hydrofluoric acid at the purity level required for sub-7nm etching and cleaning. Japan's 2019 export restrictions proved this in real time: Korean fabs could not find alternative sources. This is the definition of structural supply chain leverage.

- **Specialty fluorine gases require mastery of fluorine electrolysis.** Kanto Denka Kogyo's ability to produce over fifteen types of fluorinated gases from a proprietary electrolysis platform creates a portfolio moat that individual gas producers cannot replicate. The company's 400 billion yen expansion program signals management confidence in sustained demand growth.

- **Water scarcity and geopolitics are emerging risk factors.** As fabs are built in water-scarce regions (Arizona, Taiwan during droughts), UPW recycling technology becomes strategically valuable. Meanwhile, fluorite sourcing from China (60 percent of global supply) creates a raw material dependency that even the Japanese duopoly cannot fully mitigate. Chinese EG-HF producers are closing the quality gap, representing a medium-term threat to the Stella/Morita pricing power.

---

*Data sources: CMP-0052 (Organo Corporation), CMP-0053 (Nomura Micro Science), CMP-0032 (Nippon Sanso Holdings), CMP-0045 (Kanto Denka Kogyo), CMP-0044 (Stella Chemifa), graph.json, evaluation_progress.json*
