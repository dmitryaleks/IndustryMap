# Chapter 9: Deposition -- Layer by Layer

> Modern semiconductors are not carved from a single block of material but built up through hundreds of deposition steps, each adding a precisely controlled film measured in atoms -- and Japanese equipment makers dominate several of the most critical deposition technologies.

## Introduction

A semiconductor chip is, at its most fundamental, a stack of thin films. If you could slice through a modern logic chip at the 3-nanometer node and examine its cross-section under a transmission electron microscope, you would see dozens of distinct layers -- silicon dioxide for insulation, silicon nitride for passivation, tungsten for contacts, copper for interconnect wiring, hafnium oxide for high-k gate dielectrics, tantalum nitride for diffusion barriers, and many more. Each of these layers was deposited with atomic precision, one on top of the other, in a sequence that can involve more than a thousand individual process steps over several months of continuous fabrication.

Deposition is the process of adding material to a wafer surface. It sounds simple. It is not. The challenge is not merely placing material onto a surface but doing so with extraordinary uniformity -- across a 300-millimeter wafer, the thickness of a deposited film may need to vary by less than one percent from center to edge. The film must be chemically pure, structurally sound, and conformal: in a modern 3D NAND flash memory device with over two hundred vertically stacked layers, a deposited film must coat not only flat surfaces but also the walls and bottoms of deep trenches with aspect ratios exceeding 50:1. Achieving this requires some of the most sophisticated vacuum engineering, gas chemistry, and plasma physics in all of manufacturing.

Japan's role in deposition equipment is anchored by Tokyo Electron (TEL), the country's largest semiconductor equipment company and the world's third-largest by revenue. TEL's coater/developer systems dominate the photoresist coating step, and its CVD and thermal processing tools are installed in virtually every major fab worldwide. Alongside TEL, Kokusai Electric has carved out a formidable niche in batch deposition, commanding seventy percent of the global market for batch atomic layer deposition (ALD) equipment -- a technology that has become indispensable for 3D NAND manufacturing. Smaller but technically significant players -- Shibaura Mechatronics in plasma processing, Samco in plasma CVD, and Tazmo in coating equipment -- fill specialized roles that together give Japan an outsized presence in the deposition landscape.

This chapter explains the major deposition techniques, profiles each of these companies, and maps their positions in the semiconductor supply chain.

---

## The Science of Thin Film Deposition

Deposition techniques in semiconductor manufacturing fall into several major categories, each suited to different materials, film properties, and device geometries. Understanding these techniques is essential to appreciating why certain companies have become dominant and why their positions are difficult to challenge.

### Chemical Vapor Deposition (CVD)

Chemical vapor deposition is the workhorse of semiconductor film formation. In a CVD process, gaseous precursor chemicals are introduced into a heated reaction chamber containing the wafer. These gases react on or near the wafer surface to form a solid thin film, with volatile byproducts exhausted from the chamber. The result is a conformal coating that can line complex three-dimensional features.

CVD comes in several important variants:

**Low-Pressure CVD (LPCVD)** operates at reduced pressures, typically between 0.1 and 10 Torr, and at temperatures ranging from 400 to 900 degrees Celsius. The low pressure ensures that gas-phase reactions are minimized and that the film-forming reaction occurs primarily on the wafer surface, producing highly uniform and conformal films. LPCVD is the standard method for depositing silicon nitride (Si3N4), polysilicon, and certain silicon oxide films. It is frequently performed in batch furnaces -- large vertical or horizontal tubes that can process 100 to 200 wafers simultaneously -- which makes it economically attractive for films that do not require wafer-by-wafer process tuning. This is the domain where Kokusai Electric has built its leadership position.

**Plasma-Enhanced CVD (PECVD)** uses an electrical discharge to generate a plasma from the precursor gases, dramatically lowering the temperature required for the chemical reaction. Where LPCVD might require 700 degrees Celsius, PECVD can deposit films at 200 to 400 degrees Celsius, making it compatible with temperature-sensitive device structures such as metal interconnect layers. PECVD is widely used for depositing interlayer dielectrics, silicon nitride passivation films, and low-k dielectric materials. The tradeoff is that plasma-deposited films tend to have lower density and more incorporated hydrogen than their thermal CVD counterparts. Both Tokyo Electron and Samco supply PECVD equipment, with TEL focused on high-volume production tools and Samco serving research and specialty applications.

**Metal-Organic CVD (MOCVD)** uses metal-organic compounds as precursors and is the primary technique for depositing compound semiconductor films such as gallium nitride (GaN) and indium gallium arsenide (InGaAs). MOCVD is more commonly associated with LED and power semiconductor manufacturing than with silicon-based logic and memory, but its importance is growing as the industry explores new channel materials and heterogeneous integration. Japanese companies have a presence here, though the dominant MOCVD equipment suppliers are currently non-Japanese firms such as Aixtron and Veeco.

**High-Density Plasma CVD (HDP-CVD)** combines CVD with a high-density plasma source, enabling simultaneous deposition and sputtering. The sputtering component preferentially removes material from horizontal surfaces and corners, resulting in excellent gap-fill capability. HDP-CVD is commonly used for filling the narrow trenches in shallow trench isolation (STI) structures -- the insulating barriers that separate individual transistors.

### Physical Vapor Deposition (PVD) / Sputtering

Physical vapor deposition, most commonly performed through sputtering, operates on an entirely different principle from CVD. Instead of chemical reactions, PVD physically ejects atoms from a solid target material by bombarding it with energetic ions (typically argon). The ejected atoms travel across a vacuum chamber and condense on the wafer surface to form a thin film.

Sputtering is the dominant method for depositing metal films: aluminum, titanium, tantalum, copper seed layers, and various metal nitride barrier layers (TiN, TaN). It produces dense, high-purity films with excellent adhesion. However, PVD is inherently a line-of-sight process -- atoms travel in straight lines from the target to the wafer, which means that PVD films do not coat the sidewalls of deep features as well as CVD films do. This limitation has led to the development of ionized PVD and collimated PVD techniques that improve step coverage in high-aspect-ratio structures.

The global PVD equipment market is dominated by Applied Materials (United States), though Tokyo Electron and other Japanese equipment makers supply certain PVD modules and compete in selected PVD segments.

### Atomic Layer Deposition (ALD)

ALD represents the pinnacle of deposition precision. Unlike CVD, which delivers all precursors simultaneously, ALD introduces precursor chemicals one at a time in a sequential, self-limiting cycle. In a typical ALD cycle:

1. The first precursor gas is pulsed into the chamber. It chemisorbs onto the wafer surface, forming a single monolayer. Because the reaction is self-limiting -- once every available surface site is occupied, no further adsorption occurs -- the coverage is perfectly conformal and exactly one atomic layer thick.

2. The chamber is purged to remove excess precursor and byproducts.

3. A second precursor (or reactant) gas is pulsed in, reacting with the chemisorbed first precursor to form the desired material. Again, the reaction is self-limiting.

4. The chamber is purged again, completing one ALD cycle.

Each cycle deposits a film approximately 0.5 to 1.5 angstroms thick -- less than the diameter of a single atom in many cases. To build up a film of practical thickness, hundreds or thousands of cycles are repeated. A 50-nanometer film of aluminum oxide (Al2O3), for example, requires roughly 500 ALD cycles.

The self-limiting nature of ALD gives it three critical advantages. First, thickness control: the film thickness is determined solely by the number of cycles, not by gas flow rates, pressure, or temperature, making the process extraordinarily reproducible. Second, conformality: because the reaction saturates every exposed surface site equally, ALD can coat the deepest, narrowest features with perfectly uniform thickness. Third, composition control: by alternating different precursor combinations, engineers can deposit complex multi-component films or nanolaminate structures with atomic-level precision.

These properties have made ALD indispensable at advanced nodes. The high-k gate dielectric films that replaced silicon dioxide in transistors from the 45-nanometer node onward -- typically hafnium oxide (HfO2) -- are deposited by ALD. The conformal barrier layers in copper interconnects use ALD. And most critically for this chapter, the hundreds of alternating oxide and nitride layers in 3D NAND flash memory are increasingly deposited using batch ALD processes. This is where Kokusai Electric's seventy percent market share becomes strategically significant.

### Epitaxy

Epitaxy is a specialized form of deposition in which a crystalline film is grown on top of a crystalline substrate such that the deposited layer continues the crystal structure of the substrate. The term comes from the Greek *epi* (above) and *taxis* (arrangement). In semiconductor manufacturing, epitaxy is used to grow high-quality silicon or silicon-germanium (SiGe) layers with precisely controlled doping profiles.

There are two main types. **Vapor-phase epitaxy (VPE)** uses gaseous precursors such as silane (SiH4) or dichlorosilane (SiH2Cl2) in a CVD-like process, but at conditions chosen to promote single-crystal growth. **Molecular beam epitaxy (MBE)** uses directed beams of atoms or molecules in an ultra-high vacuum environment and provides the finest control over layer thickness and composition, though it is too slow for high-volume manufacturing and is primarily used in research and compound semiconductor production.

Epitaxial silicon films are essential in modern transistor architectures. The strained silicon-germanium (SiGe) channels used in FinFET transistors at the 14-nanometer node and below require epitaxial growth to achieve the precise lattice strain that enhances carrier mobility. At TSMC's 3-nanometer gate-all-around (GAA) node, epitaxial SiGe layers form the sacrificial material in the nanosheet release process -- a step without which the transistor cannot be fabricated.

Tokyo Electron supplies epitaxial growth equipment, alongside Applied Materials, which is the market leader in this segment.

### Coating and Developing: A Special Case

Not all deposition in a semiconductor fab involves vacuum chambers and gas chemistry. The application of photoresist -- the light-sensitive polymer that patterns each layer of the chip -- is performed by a coater/developer system, often called a "track" tool. In this process, a measured quantity of liquid photoresist is dispensed onto the center of a spinning wafer. Centrifugal force spreads the resist into a uniform thin film, typically 50 to 300 nanometers thick for advanced applications. After lithographic exposure, the developer module applies a chemical developer solution to dissolve the exposed (or unexposed, depending on the resist chemistry) portions of the film, transferring the circuit pattern onto the wafer surface.

Coating and developing is not vacuum deposition. It is wet chemistry and precision mechanics. But it is a deposition process in the broadest sense -- it places a critical thin film on the wafer -- and it is one of the most consequential in the entire manufacturing flow, because the uniformity and defect density of the resist film directly determine the quality of the lithographic pattern. A coater/developer that introduces a single particle into the resist film can produce a killer defect that destroys a chip worth thousands of dollars.

Tokyo Electron dominates this market with a global share estimated above ninety percent in advanced coater/developer systems for leading-edge lithography. This is arguably TEL's strongest single product franchise and a position that has proven virtually unassailable for decades.

---

## Company Profiles

### Tokyo Electron Limited (8035.T) -- Japan's Largest Equipment Maker

**Founded:** 1963 | **HQ:** Tokyo, Japan | **Market Cap:** 20.15 trillion yen

Tokyo Electron Limited -- universally known as TEL -- is the dominant Japanese semiconductor equipment company and one of the five companies that collectively shape the global equipment landscape, alongside Applied Materials, ASML, Lam Research, and KLA. With a market capitalization of approximately 20.15 trillion yen (roughly 135 billion US dollars), TEL is not merely a Japanese champion; it is a global heavyweight.

TEL's product portfolio spans nearly the entire front-end manufacturing process. The company supplies coater/developers, thermal processing equipment (including batch and single-wafer CVD), plasma etch systems, single-wafer deposition tools, and wafer cleaning systems. This breadth is both a strategic strength and a reflection of TEL's history: founded in 1963 as a trading company that imported semiconductor equipment from the United States, TEL progressively developed its own technology through licensing agreements, joint ventures, and internal R&D, eventually becoming a world-class manufacturer in its own right.

**Coater/Developer Dominance.** TEL's CLEAN TRACK series of coater/developer systems holds an estimated ninety percent or more of the global market for advanced lithography track tools. Every leading-edge fab operated by TSMC, Samsung, and Intel uses TEL coater/developers. The system is tightly integrated with the lithography scanner -- whether that scanner is an ASML EUV system or a DUV immersion tool -- and the combined "litho cluster" (scanner plus track) is the heartbeat of the patterning module. TEL's dominance here is self-reinforcing: because the track tool must be precisely matched to the scanner's throughput, overlay requirements, and defect specifications, chipmakers have neither the incentive nor the risk tolerance to qualify an alternative supplier. The switching cost is measured not just in dollars but in months of lost production and potential yield degradation.

**CVD and Thermal Processing.** TEL is a leading supplier of batch thermal processing equipment, including LPCVD furnaces and oxidation/diffusion systems. Its Telius series of single-wafer CVD tools competes in the deposition of advanced dielectric and barrier films. In the CVD market, TEL competes directly with Applied Materials and Lam Research, and while it does not hold the dominant global share in all CVD segments, its installed base at major fabs is extensive. TEL supplies CVD and deposition equipment to TSMC (where the supply chain graph records the relationship as "coater/developers, etch, CVD"), Samsung ("deposition equipment"), Intel ("deposition equipment"), SK Hynix ("deposition equipment"), SMIC ("coater/developer, etch, CVD"), and Hua Hong ("deposition equipment").

**Etch Systems.** Though etching is the subject of Chapter 10, it is worth noting here that TEL is a major player in plasma etch, competing with Lam Research for global leadership. TEL's etch systems are installed at all major foundries and memory manufacturers.

**Supply Chain Position.** TEL sits at the center of a dense web of supply chain relationships. Upstream, TEL draws on a network of over 400 suppliers, including Naigai Tech (CMP-0029, which derives eighty percent of its revenue from precision machining parts sold to TEL), Marumae (CMP-0030, aluminum vacuum chambers), Tocalo (CMP-0031, thermal spray coatings for chamber components), NGK Insulators (CMP-0037, ceramic electrostatic chucks), Rorze (CMP-0041, wafer transfer robots), PILLAR Corporation (CMP-0042, mechanical seals and bellows), CKD (CMP-0043, pneumatic valves), Niterra (CMP-0039), and Aval Data (CMP-0054). Downstream, TEL supplies equipment to every major chipmaker: TSMC, Samsung, Intel, SK Hynix, SMIC, Hua Hong, ASE Technology, Amkor Technology, UMC, and GlobalFoundries are all recorded clients in the supply chain graph. TEL's graph centrality score of 5 out of 5 -- the highest in our database -- reflects this extraordinary interconnectedness.

**Financial Profile.** TEL's financial performance reflects its market position. Revenue for the latest fiscal year reached approximately 2.41 trillion yen, representing 32.8 percent year-over-year growth driven by the AI-fueled capital expenditure cycle. The company guided fiscal year 2026 net sales to 2.6 trillion yen, implying continued growth of roughly seven percent. Operating margin stands at 28.7 percent, and return on equity at 27.0 percent -- both metrics that place TEL firmly in the upper tier of semiconductor equipment companies globally. The company maintains an active share buyback program and pays a dividend yielding 1.27 percent.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 29.13x |
| PBR | 5.70x |
| EPS | 1,094 yen |
| ROE | 27.0% |
| Revenue (Latest FY) | 2,410 billion yen |
| Revenue Growth YoY | 32.8% |
| Operating Margin | 28.7% |
| Dividend Yield | 1.27% |
| Foreign Ownership | 59.51% |
| 52-Week Range | 16,560 -- 45,450 yen |

**Analyst Coverage.** TEL is among the most widely followed semiconductor equipment stocks in Asia. Of 22 covering analysts, 16 rate the stock a Buy, 4 a Hold, and 2 a Sell. The average target price of 42,714 yen is modestly below the current trading price of 43,960 yen, suggesting the market has largely priced in the near-term earnings trajectory.

#### Investment Perspective

TEL's evaluation score of 58.8 out of 100 reflects an interesting tension between exceptional business quality and full valuation. The company scores a perfect 5 out of 5 on supply chain centrality (B4) -- the highest in our database -- and its moat score of 22 out of 25 on Dimension B reflects genuine competitive advantages in coater/developers, thermal processing, and etch. Growth metrics are strong (C total: 15 out of 15), with revenue growth of 32.8 percent and operating margin of 28.7 percent both well above peer group medians.

However, the stock's valuation is stretched: the A dimension (valuation) scores only 8.8 out of 30, reflecting a PER of 29.1x that, while not egregious for a company growing at this rate, offers limited margin of safety. PBR at 5.7x is well above the G1 Equipment peer median of 2.49x. Foreign ownership at 59.51 percent is the highest among Japanese equipment companies in our coverage, indicating that institutional discovery is complete -- there is no hidden foreign ownership catalyst waiting to be triggered. China revenue at an estimated 30 percent is the principal risk factor: US export controls could constrain TEL's ability to sell advanced equipment to Chinese customers, with direct revenue and margin impact.

TEL is Japan's most important semiconductor equipment company and a secular compounder tied to the multi-year AI infrastructure buildout. It is not cheap, and it is not undiscovered. It is, however, structurally irreplaceable -- and that counts for a great deal in an industry where switching costs are measured in years and qualification failures can shut down a fab.

---

### Kokusai Electric Corporation (6525.T) -- The Batch Deposition Specialist

**Founded:** 1949 (as part of Hitachi Kokusai Electric) | **HQ:** Tokyo, Japan | **Market Cap:** 1.12 trillion yen

Kokusai Electric occupies one of the most strategically important niches in the deposition equipment market: batch film deposition for memory semiconductors. The company commands an estimated seventy percent of the global market for batch atomic layer deposition (ALD) equipment and thirty-four percent for batch CVD -- positions that make it an indispensable supplier to every major 3D NAND and DRAM manufacturer on earth.

**Corporate History: From Hitachi to KKR and Back to the Market.** Kokusai Electric's path to its current position is one of the more unusual corporate stories in the semiconductor equipment industry. The company originated as Hitachi Kokusai Electric, a subsidiary of the Hitachi conglomerate that manufactured broadcast and communications equipment alongside semiconductor production tools. In 2018, Hitachi sold its semiconductor equipment division to KKR, the American private equity firm, for approximately 257 billion yen.

Under KKR's ownership from 2018 to 2023, Kokusai Electric was restructured as a standalone semiconductor equipment pure play. The company shed non-semiconductor businesses, invested in R&D, and expanded its customer base. In October 2023, KKR brought Kokusai Electric to the Tokyo Stock Exchange in a re-IPO that valued the company at approximately 480 billion yen. The stock has since appreciated substantially, reaching a market capitalization of 1.12 trillion yen. KKR remains a significant shareholder but has been progressively reducing its stake.

The KKR chapter is notable for two reasons. First, it demonstrates that private equity can add genuine value in the semiconductor equipment space -- Kokusai Electric emerged from KKR ownership as a more focused, more profitable company than it was as a Hitachi subsidiary. Second, the overhang of KKR's remaining shareholding is a factor that investors must weigh: as KKR continues to sell, the share supply could pressure the stock price in the near term, even as the underlying business strengthens.

**Why Batch Processing Matters.** To understand Kokusai Electric's competitive position, one must understand why batch processing remains relevant in an industry that has increasingly shifted to single-wafer tools.

Most advanced deposition equipment processes one wafer at a time. Single-wafer tools offer precise control, rapid recipe changes, and the ability to tailor each film to the specific requirements of a complex logic device. For leading-edge logic manufacturing at TSMC or Samsung Foundry, single-wafer CVD and ALD tools from Applied Materials, Lam Research, and Tokyo Electron are the standard.

But memory manufacturing -- particularly 3D NAND -- has different requirements. A 3D NAND device at the 200-plus-layer generation consists of a towering stack of alternating silicon oxide and silicon nitride films, each pair forming one memory layer. The deposition of these alternating layers must be repeated dozens of times, and while each individual film must be uniform and well-controlled, the films themselves are relatively simple in composition. Speed and throughput matter as much as per-wafer tunability.

This is where batch processing excels. A batch furnace can process 100 to 200 wafers simultaneously in a single deposition run. For the repetitive oxide-nitride stacks in 3D NAND, batch CVD and batch ALD offer dramatically lower cost per wafer-pass than single-wafer tools, because the capital cost is amortized across many more wafers per hour. Kokusai Electric's vertical batch furnaces can deposit these films with the uniformity and conformality required by the most advanced 3D NAND architectures, at a throughput that single-wafer tools cannot match economically.

**Product Portfolio.** Kokusai Electric's core products include batch CVD furnaces for depositing silicon oxide, silicon nitride, and polysilicon films; batch ALD systems for atomic-layer-precise deposition of high-k dielectrics and other advanced films; and treatment equipment for post-deposition film quality improvement, including annealing and oxidation. The company also supplies cleaning equipment for its installed base.

**Customer Base.** Kokusai Electric's client list reads like a directory of the world's memory manufacturers. Samsung Electronics, SK Hynix, Micron, and Kioxia are all confirmed customers. TSMC is noted as the number two customer, reflecting the foundry giant's growing use of batch deposition for certain process steps. Intel, SMIC, and CXMT (a major Chinese memory manufacturer) are also served. In the supply chain graph, Kokusai Electric appears as a supplier of "batch deposition" to Samsung (CMP-0018), Intel (CMP-0019), SK Hynix (CMP-0020), Micron (CMP-0021), Kioxia (CMP-0014), and SMIC (CMP-0066) -- six of the most important chipmakers in the world.

**Financial Profile.** Kokusai Electric reported revenue of 238.93 billion yen in its most recent fiscal year, with year-over-year revenue growth of 2.3 percent at the consolidated level. However, the most recent quarterly results tell a more dynamic story: Q2 2025 revenue of 65.42 billion yen represented 33 percent year-over-year growth, and the full calendar year 2024 revenue of approximately 238.93 billion yen represented 32 percent growth. The CEO has projected 20 percent growth in NAND equipment demand and 15 percent growth in DRAM equipment demand, driven by the AI capex cycle and the ongoing transition to higher-layer 3D NAND architectures. Operating margin stands at 21.86 percent, and ROE at 13.4 percent.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 23.46x |
| PBR | 6.39x |
| EPS | 143.35 yen |
| ROE | 13.4% |
| Revenue (Latest FY) | 238.93 billion yen |
| Revenue Growth YoY | 2.3% (FY) / 33% (Q2) |
| Operating Margin | 21.86% |
| Dividend Yield | 0.57% |
| Foreign Ownership | 37.0% |
| 52-Week Range | 1,667 -- 7,120 yen |

**Analyst Coverage.** Of 11 covering analysts, 8 rate Kokusai Electric a Buy, 2 a Hold, and 1 a Sell. The average analyst target price of 5,469 yen implies approximately 21 percent upside from the current price of 4,516 yen, reflecting bullish expectations for the memory equipment cycle.

#### Investment Perspective

Kokusai Electric's evaluation score of 56.5 out of 100 reflects a company with a strong competitive moat (B total: 20 out of 25) and a PER of 23.46x that is below the G1 Equipment peer median of 31.59x, though the PBR of 6.39x is elevated due to the company's capital structure following the KKR-era leveraged buyout. The batch ALD market share of seventy percent is a genuinely defensible position: batch furnaces require years of qualification at memory fabs, and the installed base creates a recurring service revenue stream. With eight out of eleven analysts rating the stock a Buy and a consensus target implying significant upside, the market views Kokusai Electric as a high-conviction memory equipment play.

The primary risks are cyclicality -- memory equipment spending is the most volatile segment of the semiconductor capex cycle -- and customer concentration in memory manufacturers, whose capital expenditure decisions are driven by NAND and DRAM pricing that can swing dramatically. The KKR stake overhang adds near-term uncertainty. However, the structural case is compelling: every additional 3D NAND layer added by Samsung, SK Hynix, Micron, or Kioxia requires more batch deposition passes, and Kokusai Electric is the global standard for this process step.

---

### Shibaura Mechatronics Corporation (6590.T) -- Plasma Processing and Cleaning Specialist

**Founded:** 1939 (as a Toshiba subsidiary) | **HQ:** Yokohama, Japan | **Market Cap:** 125.64 billion yen

Shibaura Mechatronics occupies a distinctive position in the Japanese equipment ecosystem: it is the world leader in single-wafer cleaning equipment for semiconductor front-end processing, while also manufacturing plasma processing equipment including etching, ashing, and surface treatment systems. Originally established as a subsidiary of Toshiba Corporation in 1939, the company has evolved from a general-purpose machinery maker into a focused semiconductor equipment supplier with growing exposure to advanced-node production.

**Core Technologies.** Shibaura Mechatronics' flagship capability is in single-wafer cleaning -- the process of removing particles, organic residues, metal contaminants, and native oxides from wafer surfaces between process steps. In a modern fab, a wafer is cleaned dozens of times during its journey through the manufacturing flow. Shibaura's post-CMP (chemical mechanical planarization) cleaning tools are installed at TSMC and Samsung, where the company is recognized as a leading supplier. Single-wafer cleaning requires precise control of chemical delivery, megasonic energy, and rinse/dry sequences, all performed without introducing additional contamination or damaging delicate device structures.

Beyond cleaning, Shibaura Mechatronics manufactures plasma processing equipment used in deposition-adjacent applications: plasma ashing (the removal of photoresist after etching), plasma surface treatment (modifying film properties through controlled ion bombardment), and plasma-enhanced deposition for certain specialized films. These tools complement the company's cleaning systems and allow it to offer integrated solutions for post-deposition and post-etch processing sequences.

The company also has a significant presence in LCD and flat panel display equipment manufacturing, though the semiconductor business has become the dominant growth driver as AI-driven demand has accelerated.

**Customer Base and Supply Chain.** The supply chain graph records Shibaura Mechatronics as a supplier of "plasma processing equipment" to both TSMC (CMP-0017) and Samsung (CMP-0018). PILLAR Corporation (CMP-0042) supplies fluororesin fittings to Shibaura Mechatronics, reflecting the company's use of wet chemistry in its cleaning processes.

**Financial Profile.** Shibaura Mechatronics stands out among Japanese equipment companies for its combination of growth and apparent undervaluation. Revenue reached 80.9 billion yen in the latest fiscal year, growing 19.8 percent year-over-year. Operating margin at 16.91 percent and ROE at 23.6 percent are both strong metrics. The stock trades at a PER of 12.46x -- less than half the G1 Equipment peer group median of 31.59x -- and a PBR of 1.43x, well below the peer median of 2.49x. The dividend yield of 2.97 percent is among the highest in the semiconductor equipment group.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 12.46x |
| PBR | 1.43x |
| EPS | 832.26 yen |
| ROE | 23.6% |
| Revenue (Latest FY) | 80.9 billion yen |
| Revenue Growth YoY | 19.8% |
| Operating Margin | 16.91% |
| Dividend Yield | 2.97% |
| 52-Week Range | 5,060 -- 11,520 yen |

#### Investment Perspective

Shibaura Mechatronics' evaluation score of 66.2 out of 100 places it fourth among all companies in our coverage, trailing only Gun Ei Chemical (78.9), SK Hynix (73.0), and PILLAR Corporation (72.0). The score is driven by an exceptionally strong valuation dimension (A total: 27.5 out of 30): the PER of 12.46x represents a 61 percent discount to G1 Equipment peers, and the PBR of 1.43x is a 43 percent discount. These are extraordinary valuation gaps for a company that is growing revenue at nearly 20 percent with an ROE of 23.6 percent.

The competitive moat score (B total: 15 out of 25) is moderate, reflecting the fact that Shibaura competes in segments where SCREEN Holdings, Lam Research, and other larger players are also present. However, its leadership in post-CMP single-wafer cleaning and its relationships with TSMC and Samsung provide meaningful switching cost protection. The AI demand tailwind (C4: 2 out of 3) is present but not as direct as for companies whose tools are required at every process step.

The primary risk is limited analyst coverage: no sell-side analysts currently cover the stock, which means institutional discovery has not yet occurred. For investors comfortable with smaller-capitalization Japanese equipment names, this lack of coverage could be viewed as an opportunity rather than a risk -- it is precisely the informational gap that creates the valuation discount.

---

### Samco Inc. (6387.T) -- Plasma CVD Pioneer

**Founded:** 1979 | **HQ:** Kyoto, Japan | **Market Cap:** 33.7 billion yen

Samco is a Kyoto-based semiconductor equipment company that has built its reputation on a singular technical focus: plasma CVD. Founded in 1979, the company introduced Japan's first plasma CVD equipment in 1980 and has since developed a portfolio that also includes dry etching and cleaning systems. With a market capitalization of approximately 33.7 billion yen, Samco is small by the standards of the global equipment industry, but its R&D-driven approach has earned it a position as a trusted supplier to research institutions and specialty semiconductor manufacturers worldwide.

**Technical Focus.** Samco specializes in low-temperature PECVD processes, particularly the deposition of thick dielectric films at temperatures below 200 degrees Celsius. This capability is important for applications where the substrate cannot tolerate high temperatures -- compound semiconductors, MEMS devices, advanced packaging, and certain power semiconductor structures. Samco's thick-film PECVD technology can deposit silicon oxide, silicon nitride, and amorphous silicon films at rates and uniformities that compete with much larger equipment makers in these niche applications.

The company also supplies inductively coupled plasma (ICP) dry etching systems and UV ozone cleaning tools. Its customer base includes both semiconductor production fabs and research facilities at universities and government laboratories, giving Samco diversified demand exposure across production and R&D cycles.

**Supply Chain Position.** The supply chain graph records Samco as a supplier of "plasma CVD equipment" to TSMC (CMP-0017) and "dry etching equipment" to Samsung (CMP-0018). PILLAR Corporation (CMP-0042) supplies fluororesin fittings to Samco, connecting the company into the broader Japanese equipment supply chain.

**Financial Profile.** Samco's small scale is reflected in its revenue of 8.2 billion yen, growing 4.8 percent year-over-year. However, the company's operating margin of 25.1 percent is impressive -- significantly above the G1 Equipment peer median of 14.9 percent -- reflecting the pricing power that comes from specialized, R&D-intensive products sold to customers with low price sensitivity. The PER of 19.7x is below the G1 peer median, though the absence of PBR data and analyst coverage limits the depth of financial analysis available.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 19.7x |
| EPS | 211.28 yen |
| Revenue (Latest FY) | 8.2 billion yen |
| Revenue Growth YoY | 4.8% |
| Operating Margin | 25.1% |
| Dividend Yield | 1.57% |
| 52-Week Range | 1,950 -- 4,435 yen |

Samco's evaluation score of 56.2 out of 100 (Medium confidence) reflects a company with decent valuation metrics and strong margins but limited supply chain centrality (B4: 1 out of 5) and modest AI exposure compared to larger equipment peers. For investors, Samco is best understood as a niche technology play -- a company whose fortunes are tied more to the growth of compound semiconductors, MEMS, and advanced R&D than to the mainline logic and memory capex cycle.

---

### Tazmo Co., Ltd. (6266.T) -- Coating Process Equipment Specialist

**Founded:** 1972 | **HQ:** Okayama, Japan | **Market Cap:** 32.31 billion yen

Tazmo is a coating process equipment manufacturer based in Okayama Prefecture that produces coaters, developers, and lamination/peeling equipment for semiconductor and flat panel display manufacturing. The company's core competency is in thin film formation through liquid coating processes -- the same fundamental technology that underlies TEL's coater/developer franchise, though Tazmo operates at a different scale and in partially different market segments.

**Product Portfolio.** Tazmo's equipment portfolio centers on spin coating systems, slit coating systems, and developer modules for semiconductor and FPD substrates. The company also manufactures clean transport systems that move wafers and substrates through coating process sequences without introducing contamination. Tazmo's technologies are based on decades of expertise in controlling fluid dynamics, film uniformity, and particle generation during liquid coating processes.

While TEL dominates the coater/developer market for leading-edge lithography at the most advanced foundries and IDMs, Tazmo serves a complementary market that includes FPD manufacturing (where substrate sizes are much larger than 300-millimeter wafers), semiconductor coating for mature and specialty nodes, and advanced packaging applications where different resist types and coating requirements create opportunities for specialized equipment.

**Supply Chain Position.** The supply chain graph records Tazmo as a supplier of "coater/developer equipment" to TSMC (CMP-0017) and "coating equipment" to Samsung (CMP-0018). These relationships indicate that Tazmo has qualified its equipment at the world's two largest chipmakers, though the company likely serves more specialized or complementary applications rather than competing head-to-head with TEL in leading-edge lithography track tools.

**Financial Profile.** Tazmo presents one of the most intriguing valuation profiles in this chapter. Revenue reached 35.87 billion yen, growing 27.4 percent year-over-year -- a growth rate that exceeds many larger equipment companies. Operating margin of 19.0 percent is solid. ROE at 16.76 percent is above the G1 peer median. And the stock trades at a PER of just 7.17x -- the lowest in the entire semiconductor equipment group in our coverage, and less than one quarter of the G1 peer median of 31.59x.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 7.17x |
| PBR | 2.05x |
| EPS | 319.66 yen |
| ROE | 16.76% |
| Revenue (Latest FY) | 35.87 billion yen |
| Revenue Growth YoY | 27.4% |
| Operating Margin | 19.0% |
| Dividend Yield | 1.33% |
| 52-Week Range | 1,302 -- 2,960 yen |

Tazmo's evaluation score of 57.5 out of 100 reflects strong valuation marks (A total: 26.2 out of 30) offset by limited competitive moat (B total: 10 out of 25) and low supply chain centrality (B4: 1 out of 5). The company faces the challenge of operating in TEL's shadow in the coater/developer market, and its FPD business introduces cyclicality tied to display industry demand cycles. No sell-side analysts currently cover the stock.

For investors, Tazmo's extreme valuation discount raises the question of whether the market is correctly pricing the company's competitive position or whether a genuine mispricing exists. The revenue growth of 27.4 percent and ROE of 16.76 percent suggest a business that is executing well; the PER of 7.17x suggests the market has limited confidence in the sustainability of those results. The answer likely lies in the mix between semiconductor and FPD revenue: to the extent Tazmo can shift its revenue base toward semiconductor applications, the multiple could expand significantly.

---

## Competitive Landscape

The global deposition equipment market is dominated by a small number of large players, with specialization by technique and end market creating a segmented competitive structure.

**CVD and ALD (Single-Wafer).** Applied Materials (United States) and Lam Research (United States) hold the leading positions in single-wafer CVD and single-wafer ALD for logic manufacturing. Tokyo Electron competes in this space, particularly in thermal CVD and certain PECVD applications. WONIK IPS (South Korea, CMP-0098) supplies PECVD and ALD equipment to Samsung and SK Hynix, representing the Korean domestic equipment ecosystem's growing capabilities. NAURA Technology (China, CMP-0085) is the leading Chinese domestic supplier of etching and deposition equipment, primarily serving SMIC and Hua Hong at mature process nodes.

**Batch CVD and ALD.** Kokusai Electric is the clear global leader in batch ALD (seventy percent share) and a strong second in batch CVD (thirty-four percent share). The primary competitor in batch deposition is the furnace product division of TEL itself, which also supplies batch thermal processing tools. The Korean supplier WONIK IPS has some presence in batch deposition for Samsung's captive supply chain. The Chinese company Hwatsing Technology (CMP-0086) is attempting to develop domestic alternatives, but batch furnace technology requires decades of accumulated know-how in gas dynamics, temperature uniformity, and wafer handling that is extremely difficult to replicate.

**PVD/Sputtering.** Applied Materials dominates the global PVD market. Japanese companies are not primary competitors in mainstream PVD, though TEL and other Japanese firms supply certain sputtering modules and have capabilities in specialized PVD applications.

**Coater/Developer.** TEL's dominance in the coater/developer market is essentially unchallenged at the leading edge. SEMES (South Korea, CMP-0096), a Samsung subsidiary, supplies photo track and cleaning equipment to Samsung's captive fab ecosystem but does not compete meaningfully in the open market. Tazmo serves complementary and specialty applications. No other company has been able to crack TEL's hold on this critical segment.

**Plasma Processing.** Shibaura Mechatronics competes in plasma processing and cleaning equipment, where SCREEN Holdings (CMP-0003) is the dominant player in wet cleaning, and Lam Research and TEL lead in plasma etch. Shibaura's differentiation in single-wafer post-CMP cleaning gives it a defensible position within this broader competitive field.

**Plasma CVD (Specialty).** Samco operates in a niche that partially overlaps with Oxford Instruments (UK) and smaller European and American suppliers of research-grade plasma CVD and etching equipment. Its focus on low-temperature thick-film PECVD for compound semiconductors and MEMS gives it a differentiated market position.

---

## Supply Chain Connections

The deposition equipment companies profiled in this chapter sit at the intersection of upstream component suppliers and downstream chipmakers. Understanding these connections reveals the economic architecture of the Japanese equipment ecosystem.

### Upstream: Who Feeds the Equipment Makers

The companies in this chapter rely on a shared base of Japanese component and subsystem suppliers that appear throughout the equipment ecosystem:

- **Naigai Tech (CMP-0029)** derives approximately eighty percent of its revenue from precision machining parts sold to TEL, making it effectively a TEL-dedicated supplier.
- **Marumae (CMP-0030)** supplies aluminum vacuum chambers to both TEL and SCREEN Holdings -- the critical enclosures within which CVD, etch, and cleaning processes take place.
- **Tocalo (CMP-0031)** applies thermal spray coatings to the internal components of TEL and SCREEN chamber parts, protecting them from the corrosive plasma and chemical environments inside process chambers.
- **NGK Insulators (CMP-0037)** supplies ceramic electrostatic chucks to TEL -- the components that hold wafers in place during processing using electrostatic forces rather than mechanical clamps.
- **Rorze (CMP-0041)** provides wafer transfer robots to both TEL and SCREEN, handling the movement of wafers between process chambers in a cluster tool.
- **PILLAR Corporation (CMP-0042)** supplies fluororesin fittings, mechanical seals, and bellows to TEL, Kokusai Electric, Shibaura Mechatronics, Samco, and CKD -- a ubiquitous presence in any equipment that handles corrosive chemicals or requires ultra-clean fluid paths.
- **CKD (CMP-0043)** supplies pneumatic valves to TEL, SCREEN, and Kokusai Electric, controlling the precise flow of process gases into deposition chambers.
- **Aval Data (CMP-0054)** supplies tester boards and measurement subsystems to TEL.

This supplier ecosystem is characteristic of the Japanese semiconductor supply chain: a web of mid-cap and small-cap companies, each providing a critical but narrow component, all converging on the major equipment OEMs. The implications for investors are significant. A bet on the deposition equipment cycle is, in effect, a bet on this entire network of suppliers.

### Downstream: Who Uses the Equipment

The downstream connections flow from the equipment makers to the chipmakers and are extensively documented in the supply chain graph:

- **TEL** supplies coater/developers, etch, and CVD equipment to TSMC, Samsung, Intel, SK Hynix, SMIC, Hua Hong, ASE, Amkor, UMC, and GlobalFoundries.
- **Kokusai Electric** supplies batch deposition equipment to Samsung, Intel, SK Hynix, Micron, Kioxia, and SMIC.
- **Shibaura Mechatronics** supplies plasma processing equipment to TSMC and Samsung.
- **Samco** supplies plasma CVD equipment to TSMC and dry etching equipment to Samsung.
- **Tazmo** supplies coater/developer equipment to TSMC and coating equipment to Samsung.

### Cross-Chapter Connections

Deposition does not exist in isolation. It is preceded by wafer preparation (Chapter 4), ultrapure water and gas supply (Chapter 5), and lithographic patterning (Chapters 6-8), and it is followed by etching (Chapter 10) and planarization (Chapter 11). The photoresist coating step -- performed by TEL's coater/developer systems -- is the bridge between the lithography world of Chapter 6 and the deposition/etch world of this chapter. After a pattern is exposed and developed, the exposed film is etched, and then the next deposition cycle begins. This deposit-pattern-etch sequence repeats hundreds of times in the fabrication of a modern chip, creating a rhythmic demand for deposition equipment that scales directly with the complexity of the device being manufactured.

The increasing layer counts in 3D NAND memory illustrate this scaling. Samsung's current V-NAND technology stacks over 200 layers, and the industry roadmap extends to 300 and eventually 400 or more layers. Each additional layer requires additional deposition passes. For Kokusai Electric, whose batch furnaces are optimized for exactly these repetitive deposition sequences, the secular trend toward higher layer counts is a direct and powerful growth driver.

---

## Key Takeaways

- **Deposition is the most repetitive step in semiconductor manufacturing**, with a modern chip requiring hundreds of individually deposited thin films. The technique used -- CVD, PVD, ALD, or epitaxy -- depends on the material, the required film properties, and the geometry of the device structure.

- **Tokyo Electron is Japan's most central equipment company**, with supply chain connections to virtually every major chipmaker worldwide. Its coater/developer franchise (estimated ninety percent-plus global share) is arguably the most dominant single product position among the top-five equipment makers, and its CVD and etch businesses make it a full-line competitor to Applied Materials and Lam Research.

- **Kokusai Electric's batch ALD monopoly (seventy percent share) is a high-conviction structural position** tied directly to the 3D NAND layer count trend. The re-IPO following KKR ownership has created a focused pure-play on memory deposition, and the analyst consensus target implies meaningful upside from current levels.

- **Shibaura Mechatronics' valuation discount is the most extreme in this chapter**, with a PER of 12.46x against a peer median of 31.59x, despite revenue growth of 19.8 percent and ROE of 23.6 percent. The lack of analyst coverage and the company's Toshiba-subsidiary heritage may be obscuring a genuine mispricing.

- **The Japanese deposition equipment ecosystem extends well beyond the OEMs.** Component suppliers such as Naigai Tech, Marumae, Tocalo, NGK Insulators, Rorze, PILLAR, CKD, and Aval Data collectively form the industrial backbone that makes Japanese equipment manufacturing possible. Investors analyzing the deposition cycle should consider this extended supply chain, not just the headline equipment companies.

---

*Data sources: CMP-0004 (Tokyo Electron), CMP-0011 (Kokusai Electric), CMP-0059 (Shibaura Mechatronics), CMP-0060 (Samco), CMP-0062 (Tazmo), graph.json (supply chain edges), evaluation_progress.json (scores and investment theses)*
