# Chapter 10: Etching & Cleaning

> Every circuit pattern printed onto a silicon wafer must be carved into the underlying material with atomic precision, and every trace of contamination must be removed between steps -- processes that depend on some of the most corrosive chemicals in industrial use and on a handful of Japanese companies that make it possible to handle them.

## Introduction

A semiconductor fab is, at its core, an elaborate cycle of two operations: adding material and taking it away. The previous chapter described deposition -- the process of building up thin films layer by layer. This chapter covers the complementary half: etching, which selectively removes material to carve circuit patterns, and cleaning, which strips away residues, particles, and contaminants between every major process step.

If deposition is construction, etching is sculpture. After a photoresist pattern has been developed onto a film, an etch step transfers that pattern into the underlying material -- silicon, silicon dioxide, silicon nitride, metal, or any of a dozen other thin films that compose a modern chip. The etch must be precise enough to remove the target material without damaging what lies beneath it, and anisotropic enough to produce vertical sidewalls at dimensions measured in nanometers. At the 3-nanometer node, the tolerance for etch variability across a 300-millimeter wafer is measured in angstroms -- the width of a single atom.

Cleaning is equally critical and far more frequent. A leading-edge logic wafer undergoes more than one thousand individual process steps, and cleaning operations account for roughly thirty to forty percent of them. Every time a film is deposited, patterned, or etched, the wafer surface must be cleaned to remove particles, organic residues, metallic contaminants, and native oxides before the next step can proceed. At advanced nodes, a single particle larger than twenty nanometers on the wafer surface can kill a die. A single metal ion at the parts-per-trillion level can shift threshold voltages and destroy transistor performance. Cleaning is not a glamorous process step, but it is the one that most directly determines fab yield -- and yield is the single most important economic variable in semiconductor manufacturing.

Japan's position in etch and clean is anchored by SCREEN Holdings, the undisputed global leader in wet cleaning equipment, and by a cluster of specialized component suppliers whose products are embedded inside every cleaning tool that ships. PILLAR Corporation makes the fluororesin fittings that carry corrosive chemicals through the tool. CKD Corporation makes the pneumatic valves that control the flow of those chemicals. Horiba makes the mass flow controllers and concentration monitors that measure what is flowing and whether the chemistry is correct. Together, these companies form a supply chain within a supply chain -- invisible, indispensable, and almost entirely Japanese.

---

## The Science of Etching

Etching is the process of selectively removing material from a wafer surface using chemical reactions, physical bombardment, or a combination of both. The field divides into two broad categories: wet etching, which uses liquid chemicals, and dry etching, which uses reactive gases in a plasma state. Each has its domain, its advantages, and its limitations.

### Wet Etching

Wet etching is the older and simpler of the two methods. The wafer is immersed in or sprayed with a liquid chemical that dissolves the target material. The most important wet etchant in semiconductor manufacturing is hydrofluoric acid, or HF. Dilute HF, typically at concentrations of 0.5 to 5 percent, is used to remove silicon dioxide -- the native oxide that forms spontaneously on silicon surfaces and the thermally grown oxide used as a gate dielectric in older process nodes. Buffered HF, or BHF, is a mixture of hydrofluoric acid and ammonium fluoride (NH4F) that provides a more controlled, consistent etch rate. BHF is preferred when the etch depth must be precisely controlled, because the ammonium fluoride acts as a buffer that stabilizes the pH and the etch rate as the HF is consumed.

Other critical wet etch chemistries include piranha solution, a mixture of sulfuric acid (H2SO4) and hydrogen peroxide (H2O2) at ratios typically between 3:1 and 7:1, heated to 120-180 degrees Celsius. Piranha is an extraordinarily aggressive oxidizer used to strip organic residues -- particularly photoresist -- from the wafer surface. The name is apt: piranha solution will dissolve most organic materials on contact. Phosphoric acid (H3PO4) at elevated temperatures is used to etch silicon nitride selectively over silicon dioxide, a chemistry critical in spacer-defined patterning at advanced nodes.

Wet etching has one fundamental limitation: it is isotropic. The liquid etchant attacks the target material equally in all directions -- downward into the film, but also laterally beneath the photoresist mask. This lateral undercutting was acceptable at feature sizes above one micrometer, where a small amount of lateral etch could be tolerated. At modern dimensions, where the target feature width is five nanometers or less, isotropic wet etching cannot produce the vertical sidewalls required. For this reason, wet etching in a modern fab is used primarily for blanket removal of films (stripping an entire oxide layer, for example), cleaning, and specific non-critical etch steps where isotropy is not a concern.

### Dry Etching: Reactive Ion Etching and Beyond

Dry etching -- also called plasma etching -- solved the anisotropy problem. In a dry etch system, a gas or mixture of gases is introduced into a vacuum chamber and energized into a plasma state using radio-frequency (RF) power. The plasma contains reactive radicals, ions, and electrons. The ions are accelerated toward the wafer surface by an electric field, where they strike the surface with enough energy to break chemical bonds (physical sputtering) while the reactive radicals react chemically with the surface material to form volatile compounds that are pumped away.

The most common form of dry etching is Reactive Ion Etching, or RIE. In RIE, the wafer sits on the RF-powered electrode (the cathode), which develops a DC self-bias that accelerates ions perpendicularly toward the wafer surface. Because the ions arrive with a strong directional bias -- nearly vertical -- the etch proceeds preferentially downward rather than laterally. The result is an anisotropic etch profile: vertical sidewalls with minimal undercutting.

More advanced variants include Inductively Coupled Plasma (ICP) etching, where the plasma is generated by a separate RF coil (typically wrapped around the chamber), decoupling the plasma density from the ion energy. This allows independent control of how many ions are generated and how hard they hit the surface -- a critical capability for high-aspect-ratio etching, where deep, narrow trenches must be carved into the wafer without damaging the bottom or bowing the sidewalls. ICP-RIE is the standard configuration for leading-edge logic and memory etch at the 7-nanometer node and below.

### Selectivity and the Etch Stop

The most important concept in etching is selectivity -- the ratio of the etch rate of the target material to the etch rate of the material that must not be removed. When etching a silicon dioxide layer that sits on top of silicon, the etch chemistry must remove SiO2 rapidly while leaving the underlying silicon essentially untouched. A selectivity of 100:1 means the etchant removes the target material one hundred times faster than the material beneath it. At advanced nodes, where films are only a few nanometers thick, selectivities of 200:1 or higher are often required.

Achieving high selectivity requires precise control of gas chemistry, plasma conditions, temperature, and pressure. Fluorine-based chemistries (CF4, CHF3, C4F8) are used for oxide and nitride etching. Chlorine-based chemistries (Cl2, BCl3, HBr) are used for silicon and metal etching. The gas ratios, flow rates, chamber pressure, RF power levels, and wafer temperature must all be tuned to achieve the desired combination of etch rate, selectivity, anisotropy, and surface smoothness. This is where Horiba's mass flow controllers and gas analyzers enter the picture -- if the gas mixture is even slightly off specification, the selectivity collapses and the etch damages the layers it should preserve.

### Atomic Layer Etching

At the most advanced nodes -- 3 nanometers and below -- the industry is moving toward Atomic Layer Etching, or ALE, the inverse of Atomic Layer Deposition. ALE removes material one atomic layer at a time through a two-step cycle: first, a surface modification step that chemically alters exactly one monolayer of the target material; second, a removal step that clears away only the modified layer. ALE can achieve sub-angstrom etch depth control and near-infinite selectivity in principle, though the throughput is low and the process complexity is high. Both Tokyo Electron and Lam Research are developing ALE-capable etch platforms.

---

## The Science of Cleaning

If etching is the sculptor's chisel, cleaning is the surgeon's scrub. Semiconductor cleaning removes five categories of contaminants from the wafer surface: particles (dust, debris, slurry residues), organic residues (photoresist fragments, carbon compounds), metallic contaminants (iron, copper, sodium, aluminum), native oxides (thin SiO2 layers that form within seconds of air exposure), and ionic contaminants (dissolved salts and acids). Each category requires a different chemical approach, and a modern cleaning sequence typically chains multiple steps together.

### The RCA Clean and Its Descendants

The foundation of semiconductor cleaning was established in 1965 by Werner Kern at RCA Laboratories, who developed the two-step cleaning sequence that bears the company's name. The RCA clean consists of two solutions:

**SC-1 (Standard Clean 1):** A mixture of ammonium hydroxide (NH4OH), hydrogen peroxide (H2O2), and deionized water, typically in a ratio of 1:1:5 to 1:2:7, heated to 65-80 degrees Celsius. SC-1 removes organic contaminants through oxidation and particles through a combination of chemical undercutting and electrostatic repulsion. The NH4OH etches the silicon surface very slightly, lifting particles off by removing the material underneath them. SC-1 is sometimes called APM (Ammonia-Peroxide Mixture).

**SC-2 (Standard Clean 2):** A mixture of hydrochloric acid (HCl), hydrogen peroxide (H2O2), and deionized water, typically 1:1:6 to 1:2:8, heated to 65-80 degrees Celsius. SC-2 removes metallic contaminants by dissolving metal ions and forming soluble chloride complexes. This step is critical because even trace metals -- iron at the parts-per-billion level, copper at parts-per-trillion -- can diffuse into the silicon lattice during subsequent high-temperature processes and destroy transistor performance. SC-2 is sometimes called HPM (Hydrochloric acid-Peroxide Mixture).

Modern fabs have evolved well beyond the original RCA recipe, adding and modifying steps to meet the demands of advanced nodes:

**SPM (Sulfuric acid-Peroxide Mixture):** The piranha solution described in the etching section, used at the cleaning stage to strip bulk photoresist after lithography and etch. SPM operates at 120-180 degrees Celsius and generates Caro's acid (H2SO5), one of the strongest oxidizers used in semiconductor manufacturing. A single SPM cycle can remove a micrometer-thick photoresist layer in minutes.

**DHF (Dilute Hydrofluoric acid):** A 0.5 to 1 percent solution of HF in ultrapure water, used to strip native oxide and leave a hydrogen-terminated silicon surface. The DHF step is typically the final step before gate oxide growth, because it produces the cleanest possible silicon surface. This is where Stella Chemifa's twelve-nine purity hydrofluoric acid, discussed in Chapter 5, finds its most critical application: any impurity in the HF will be deposited directly onto the silicon surface that will become the transistor channel.

**Ozonated Water (DIO3):** Ultrapure water saturated with dissolved ozone, used as a less aggressive alternative to SPM for organic removal. DIO3 has the advantage of being a simple, room-temperature process with no chemical waste beyond water and oxygen. It is increasingly used at advanced nodes for light organic cleaning between process steps.

### Megasonic Cleaning

Chemical cleaning alone cannot remove all particles. At advanced nodes, particles as small as 20 nanometers -- roughly the diameter of a virus -- can cause yield-killing defects. Megasonic cleaning supplements chemical action with high-frequency acoustic energy. A transducer generates sound waves at frequencies between 0.7 and 3 megahertz, which propagate through the cleaning liquid and create microscopic pressure oscillations near the wafer surface. These oscillations dislodge particles without the cavitation damage associated with lower-frequency ultrasonic cleaning.

The physics is subtle. At lower frequencies (below 100 kilohertz), acoustic cleaning works through cavitation -- the formation and violent collapse of microscopic bubbles. Cavitation is powerful but destructive: the energy of collapsing bubbles can pit and damage delicate features on the wafer surface. At megasonic frequencies, the wavelength of the sound is comparable to the particle size, and the cleaning mechanism shifts from cavitation to acoustic streaming -- the generation of high-velocity fluid flows near the wafer surface that drag particles off by viscous force. Megasonic cleaning at the right frequency and power level can remove 20-nanometer particles without damaging the sub-10-nanometer features on the wafer.

SCREEN's single-wafer cleaning systems integrate megasonic transducers as standard equipment, and the tuning of the megasonic frequency, power, and sweep pattern to different cleaning chemistries and feature sizes is one of the areas where SCREEN's decades of accumulated process knowledge create a competitive advantage that is difficult to replicate.

### Cleaning Frequency and Economic Impact

The sheer volume of cleaning operations in a modern fab is staggering. A leading-edge logic wafer at the 3-nanometer node passes through the cleaning tool more than 200 times during its fabrication, which spans 60 to 90 days and over 1,000 total process steps. Each cleaning step consumes ultrapure water, specialty chemicals, and tool time. The cleaning step is the most frequently repeated operation in the entire process flow, which is why cleaning equipment represents one of the largest capital expenditure categories in fab construction.

This frequency also explains why SCREEN's market position is so significant. While a fab might require a handful of EUV lithography systems (at 300-400 million dollars each), it requires dozens of cleaning tools. A large-scale logic fab operating at the 3-nanometer node may deploy 80 to 120 cleaning tools. At roughly 200-400 million yen per tool, cleaning equipment can represent 15-25 percent of the total process equipment budget. The installed base economics are equally important: each cleaning tool consumes fluororesin fittings, valves, and seals as consumables, generating a recurring revenue stream for component suppliers like PILLAR and CKD that persists for the 15-20 year operational life of the tool.

---

## SCREEN Holdings (7735.T) -- Global Leader in Wet Cleaning Equipment

**Founded:** 1943 | **HQ:** Kyoto | **Market Cap:** 2,040 billion yen

SCREEN Holdings is the world's number one manufacturer of semiconductor wafer cleaning equipment. The company's Semiconductor Process Equipment (SPE) division, marketed under the SCREEN SPE brand, designs and manufactures single-wafer spin cleaners, batch immersion cleaners, spin scrubbers, and related wet processing systems. Cumulative shipments exceed 15,000 units worldwide, and SCREEN holds the leading global market share in each of its core cleaning equipment categories.

The company was founded in 1943 in Kyoto as Dainippon Screen Manufacturing, originally producing printing plates and graphic arts equipment. The transition to semiconductor equipment began in the 1970s, when SCREEN applied its precision coating and etching expertise from the printing industry to the emerging semiconductor market. The company developed wafer cleaning systems, coater/developers, and direct-write exposure systems. Over the following decades, the cleaning equipment business grew to dominate the company's revenue and profit.

SCREEN's product lineup addresses the full spectrum of wet cleaning needs:

**Single-wafer spin cleaners** are the workhorses of modern cleaning. A single wafer is loaded onto a spinning chuck, and cleaning chemicals are dispensed onto the wafer surface through precisely positioned nozzles while the wafer rotates at controlled speeds. The spinning action provides uniform chemical distribution and centrifugal removal of particles and residues. Single-wafer tools offer superior process uniformity and contamination control compared to batch systems, and they have become the standard for advanced-node cleaning. SCREEN's SU-3300 series single-wafer cleaner is the market-leading platform.

**Batch immersion cleaners** process 25 to 50 wafers simultaneously in chemical baths. While single-wafer tools offer better uniformity, batch tools offer higher throughput for non-critical cleaning steps -- such as pre-diffusion cleans or post-CMP cleans -- where the tighter process control of single-wafer systems is not required. SCREEN maintains a significant position in batch cleaning alongside competitors like Tokyo Electron.

**Spin scrubbers** combine chemical cleaning with physical brush scrubbing, primarily used for post-CMP cleaning to remove slurry particles from the wafer surface. After a CMP step (described in Chapter 11), the wafer surface is covered in abrasive slurry residues that must be completely removed before subsequent processing.

SCREEN's more recent product development extends beyond cleaning into adjacent wet process areas. The **Lemotia** PLP (Panel-Level Packaging) coater addresses the growing advanced packaging market, and the **LeVina** direct-write exposure system offers maskless lithography for specific applications. However, cleaning remains the core franchise.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 22.19x |
| PBR | 3.35x |
| EPS | 930.8 yen |
| ROE | 22.4% |
| Revenue Growth (YoY) | +1.2% |
| Operating Margin | 14.9% |
| Dividend Yield | 1.75% |
| Foreign Ownership | 40.0% |

SCREEN's financial profile reflects the characteristics of a mature market leader in semiconductor equipment. The PER of 22.19x represents a 30 percent discount to the G1 Semiconductor Equipment peer group median of 31.59x, suggesting either undervaluation or the market's assessment of lower growth potential relative to peers. The PBR of 3.35x is modestly above the peer median of 2.49x, reflecting the capital-light nature of equipment design relative to the balance sheet. Operating margin at 14.9 percent is precisely at the G1 peer median, indicating competitive but not exceptional profitability.

Foreign ownership at 40.0 percent is meaningfully above the level typically seen for mid-tier Japanese semiconductor companies, reflecting SCREEN's visibility as a recognized equipment maker with strong analyst coverage -- 7 Buy, 7 Hold, and 1 Sell recommendations among surveyed analysts. The 52-week price range of 7,825 to 21,940 yen indicates significant volatility tied to semiconductor cycle expectations.

SCREEN's competitive moat rests on three pillars. First, the installed base: with over 15,000 cleaning systems shipped, SCREEN has the deepest library of process recipes for specific cleaning applications -- knowledge accumulated over decades that new entrants cannot replicate. Second, integration with the fab ecosystem: cleaning tools must interface seamlessly with upstream and downstream equipment, and SCREEN's long-standing relationships with TSMC, Samsung, Intel, and other leading chipmakers provide the customer intimacy needed to co-develop cleaning processes for each new technology node. Third, R&D partnerships with industry research organizations including imec (Belgium) and IBM ensure that SCREEN's technology roadmap stays aligned with the requirements of future process nodes.

### Investment Perspective

SCREEN's evaluation score of 55.5/100 places it in the middle tier of our coverage universe. The moat score (B=19/25) is strong, reflecting the company's leading market share, high switching costs from process recipe lock-in, and strong chain centrality as a supplier to every major chipmaker. The valuation score (A=12.5/30) is moderate -- the PER discount to peers is meaningful, but the PBR premium and lack of forward PER data limit the upside case. Growth and profitability (C=10.0/15) are solid, with ROE of 22.4 percent and moderate AI exposure through increased cleaning step counts at advanced nodes. The risk-adjusted deduction (F=-5.0) reflects forex sensitivity and geopolitical exposure to China, where SCREEN has significant revenue from mature-node fabs.

The primary investment consideration for SCREEN is its role as a bellwether for cleaning equipment demand. As the dominant player, SCREEN's order trends are a leading indicator for the broader semiconductor cycle. The company benefits from secular tailwinds -- the number of cleaning steps per wafer increases with each new process node, driving tool demand even at constant wafer start volumes -- but also faces cyclical headwinds from the capital expenditure patterns of its major customers.

---

## PILLAR Corporation (6490.T) -- The Hidden Monopoly in Fluororesin Fittings

**Founded:** 1924 | **HQ:** Osaka | **Market Cap:** 185 billion yen

PILLAR Corporation is, by any reasonable measure, the most under-appreciated monopolist in the global semiconductor supply chain. The company holds over ninety percent of the global market for fluororesin fittings used in semiconductor wet cleaning equipment. Its Super 300 (S-300) fitting has become the de facto industry standard -- so dominant that Entegris, the $17 billion American specialty materials company and the world's leading semiconductor fluid handling provider, licenses PILLAR's S-300 technology rather than developing a competing standard. When a competitor of that scale chooses to license rather than compete, it is the ultimate validation of a monopoly position.

### The Century-Long Journey

PILLAR was founded in 1924 in Osaka as Nippon Pillar Packing Co., Ltd., a manufacturer of industrial seals, gaskets, and packing materials for Japan's growing heavy industry. For decades, the company served petrochemical plants, power generation facilities, and shipbuilders -- applications where sealing technology prevented leaks of high-pressure steam, corrosive chemicals, and flammable fluids. This was the domain of mechanical engineering at its most practical: creating reliable seals from materials that could withstand extreme temperatures, pressures, and chemical environments.

The pivot to semiconductors began in the 1980s, as Japan's semiconductor industry expanded and fabs demanded components that could handle the ultra-aggressive chemicals used in wafer cleaning. Hydrofluoric acid, the most critical cleaning and etching chemical, dissolves glass, attacks most metals, and corrodes virtually every common engineering material. The only materials that can withstand prolonged exposure to concentrated HF are fluoropolymers -- specifically polytetrafluoroethylene (PTFE, known commercially as Teflon) and perfluoroalkoxy alkane (PFA). PILLAR's decades of experience in sealing and chemical resistance positioned it perfectly to develop fluororesin fittings, tubing, valves, and pumps for semiconductor wet process equipment.

The company spent the following decades perfecting the purity and precision of these components. Semiconductor-grade fluororesin fittings are not simply tubes and connectors made from fluoropolymer material. They must meet extraordinary cleanliness specifications: the inner surfaces must be free of particles above 0.1 micrometers, the material must not leach metallic contaminants at the parts-per-trillion level, and the dimensional tolerances must ensure leak-free connections even under the thermal cycling that occurs when cleaning chemicals alternate between room temperature and 180 degrees Celsius. PILLAR developed proprietary molding, welding, and surface finishing processes to achieve these standards, and over time those processes became the basis of the S-300 fitting standard.

In June 2024, at its centennial anniversary, the company rebranded from Nippon Pillar Packing Co., Ltd. to PILLAR Corporation -- a deliberate signal that management intended to reposition the company's identity away from its industrial heritage and toward its semiconductor business.

### Why Fluororesin Fittings Matter

The centrality of fluororesin fittings in semiconductor manufacturing becomes clear when one considers the chemical environment inside a wet cleaning tool. A single-wafer spin cleaner cycles through multiple chemical steps in sequence: SPM (sulfuric acid and hydrogen peroxide at 120-180 degrees Celsius), SC-1 (ammonia and hydrogen peroxide at 65-80 degrees Celsius), DHF (dilute hydrofluoric acid at room temperature), SC-2 (hydrochloric acid and hydrogen peroxide at 65-80 degrees Celsius), and ultrapure water rinses between each step. Each of these chemicals is delivered to the wafer through a fluid delivery system consisting of pipes, fittings, valves, filters, pumps, and flow controllers.

The challenge is that these chemicals are among the most corrosive substances in industrial use. Hydrofluoric acid dissolves glass, most ceramics, and many metals. Piranha solution oxidizes organic materials on contact. Even the ultrapure water is aggressively pure -- so devoid of dissolved minerals that it will leach ions from any material it contacts, contaminating itself and, ultimately, the wafer.

Fluororesin -- specifically PFA and PTFE -- is one of the very few materials that can withstand this entire chemical gauntlet without degrading or contaminating the fluids. The carbon-fluorine bond that defines fluoropolymers is one of the strongest in organic chemistry, making these materials virtually inert to chemical attack. But the material alone is not sufficient. The fittings must be manufactured to semiconductor-grade purity, with surface roughness measured in nanometers and extractable metal content below parts per trillion. This is where PILLAR's hundred years of sealing expertise and its decades of semiconductor-specific process development converge.

The S-300 fitting system incorporates PILLAR's proprietary technologies for:
- **Precision injection molding** of PFA resin with controlled crystallinity that minimizes particle shedding
- **High-purity welding** techniques that create particle-free joints between tubing sections
- **Surface finishing** processes that reduce inner surface roughness to minimize fluid turbulence and particle generation
- **Dimensional control** that ensures leak-free connections even after thousands of thermal cycles

The result is a fitting system that has become the industry standard -- not because it was mandated or regulated, but because it works reliably in the most demanding chemical environment in manufacturing.

### The Client Ecosystem

PILLAR serves the semiconductor industry through two channels, creating a web of relationships that is extraordinarily difficult for a competitor to replicate.

The first channel is OEM supply to equipment manufacturers. SCREEN Holdings is PILLAR's largest customer, accounting for 16.6 percent of PILLAR's total revenue (9.65 billion yen in FY2025) and growing from 9 percent in FY2021 -- a reflection of the increasing cleaning intensity at advanced nodes. Tokyo Electron, Ebara Corporation, Shibaura Mechatronics, Kokusai Electric, CKD Corporation, and Samco all embed PILLAR's fluororesin fittings into their equipment platforms. When SCREEN ships a cleaning tool to TSMC or Samsung, that tool arrives with PILLAR fittings already installed. The equipment maker's design specifications call for PILLAR components, and the qualification of those components is tied to the equipment maker's own qualification at the fab -- a layered certification process that would take 12-18 months to repeat with an alternative supplier, carrying unacceptable contamination risk.

The second channel is direct supply to fabs through PILLAR's global subsidiary network. PILLAR Taiwan Co., Ltd. (with a factory in Kaohsiung) serves TSMC and other Taiwanese fabs. PILLAR Korea Co., Ltd. (Seoul) serves Samsung and SK Hynix. PILLAR Shanghai Co., Ltd. and Pillar Technology Chuzhou (a manufacturing subsidiary) serve SMIC and Hua Hong Semiconductor. PILLAR America Inc. (Fremont, California and Houston, Texas) serves Intel and other American fabs. A new Malaysia subsidiary, established in October 2025, positions the company for the growing Southeast Asian semiconductor ecosystem. This direct-to-fab channel supplies maintenance and replacement parts -- the fittings, tubing, and seals that must be periodically replaced as they degrade from prolonged chemical exposure. This creates a recurring revenue stream that persists for the operational life of each installed tool, typically 15-20 years.

Additionally, through the Entegris licensing relationship, PILLAR fittings are embedded in the fluid handling systems of Applied Materials, Lam Research, and KLA tools. These are the three largest semiconductor equipment companies in the world by revenue. PILLAR's total addressable reach therefore extends far beyond its direct client list.

The supply chain graph records 14 client edges for PILLAR -- one of the densest client networks of any company in the dataset. The edges span SCREEN (CMP-0003), Tokyo Electron (CMP-0004), Ebara (CMP-0036), Shibaura Mechatronics (CMP-0059), Kokusai Electric (CMP-0011), CKD (CMP-0043), Samco (CMP-0060), TSMC (CMP-0017), Samsung (CMP-0018), Intel (CMP-0019), SK Hynix (CMP-0020), SMIC (CMP-0066), Hua Hong (CMP-0070), and SEMES (CMP-0096, Samsung's equipment subsidiary).

### Segment Structure

PILLAR operates two business segments that provide both semiconductor purity and earnings resilience.

The **Electronic Equipment segment** (67 percent of consolidated sales) is the semiconductor pure-play. It produces the PILAFLON line of fluororesin fittings, pumps, valves, and tubing for wet process equipment. This segment is the engine of the investment thesis -- every dollar of incremental semiconductor capital expenditure on cleaning, etching, CMP, or CVD equipment translates into demand for PILLAR's Electronic Equipment products. The segment's growth is directly tied to global fab construction and cleaning intensity per wafer.

The **Industrial Equipment segment** (33 percent of sales) produces mechanical seals, gaskets, and packing for petrochemical plants, power generation facilities, and automotive applications. In April 2023, PILLAR acquired Tanken Seal Seiko for 6.6 billion yen, adding carbon-based mechanical seal capabilities and strengthening this segment. While the industrial business grows more slowly than the semiconductor business, it provides crucial earnings diversification: in semiconductor downturns, the industrial segment floors the earnings decline, preventing the kind of severe profit collapse that can destroy investor confidence and share price.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 21.54x |
| PBR | 2.42x |
| Forward PER | 19.24x |
| EPS | 376.5 yen |
| ROE | 11.78% |
| Revenue (FY2025/3) | 58.0 billion yen |
| Revenue Growth (YoY) | -1.05% |
| Operating Margin | 19.85% |
| Dividend Yield | 1.60% |
| Foreign Ownership | 21.28% |
| 10-Year Revenue CAGR | 10.34% |
| 10-Year Net Profit CAGR | 15.37% |

The financial profile reveals the hallmarks of a monopoly supplier. The operating margin of 19.85 percent is 1.33 times the G1 Semiconductor Equipment peer group median of 14.9 percent -- a premium that directly reflects the pricing power of a company with no meaningful competition. The 10-year net profit CAGR of 15.37 percent exceeding the revenue CAGR of 10.34 percent by five percentage points demonstrates the operating leverage inherent in a monopoly position: as revenue grows, an increasing proportion falls to the bottom line because the competitive dynamics that compress margins in other industries are absent.

FY2025/3 revenue of 58.0 billion yen represented a cyclical trough (down 1.05 percent year-over-year), but Q3 FY2026/3 showed an 8.14 percent year-over-year recovery, and full-year guidance has been revised upward with operating income expected to grow 16.5 percent. The stock has responded, rallying 119 percent over the past year from 2,810 to 8,110 yen -- yet it remains inexpensive relative to peers.

### Investment Perspective

PILLAR Corporation carries the second-highest investment thesis score in our entire coverage universe at 72.0/100, trailing only Gun Ei Chemical (78.9). The score reflects a rare convergence of monopoly quality, attractive valuation, and identifiable catalysts.

**The moat is near-perfect.** PILLAR's competitive position score (B=24/25) is the highest moat rating in the G1 Equipment peer group. The 90-percent-plus global market share, the S-300 de facto standard, the Entegris licensing validation, the 14 identified client relationships spanning equipment makers and fabs on four continents, the 100-year manufacturing heritage, and the 12-18 month requalification barrier combine to create what is, in practical terms, an unassailable monopoly.

**The valuation is still compelling despite the rally.** PER of 21.54x represents a 32 percent discount to the G1 peer median of 31.59x -- the deepest PER discount among monopoly-quality companies in our coverage. The forward PER of 19.24x is even more attractive. PBR of 2.42x is essentially at parity with the peer median of 2.49x. The stock trades at 0.68 times the peer group PER multiple -- a discount that would be difficult to justify for a company with average competitive positioning, let alone a monopolist.

**The foreign ownership gap is the primary catalyst.** At 21.28 percent, PILLAR's foreign institutional ownership is dramatically below the expected level of approximately 45 percent for a company with near-monopoly moat scores. This 23.7 percentage-point gap is the single strongest institutional underownership signal in our framework. For comparison: SCREEN Holdings has 40 percent foreign ownership; Tokyo Electron has 59.5 percent; Advantest has 50 percent; DISCO has 45 percent. PILLAR's gap exists for identifiable and correctable reasons: the company was named "Nippon Pillar Packing" until June 2024, equity databases frequently miscategorize it as an industrial seals company, market capitalization at 185 billion yen sits below the minimum threshold of many global semiconductor funds, and English-language research coverage is minimal. As these information barriers erode -- through the corporate rebrand, growing awareness of the semiconductor supply chain thesis, and potential index reclassification -- the structural bid from foreign institutions should provide sustained buying pressure. The free float at 74.9 percent is ample to absorb this demand without liquidity constraints.

**Additional catalysts include:** the AI/HPC capital expenditure boom driving unprecedented demand for advanced fab capacity (and therefore cleaning equipment and fittings); the global fab buildout (TSMC Arizona, Kumamoto, and Dresden; Intel Ohio and Magdeburg; Samsung Taylor; Rapidus Chitose); the Malaysia subsidiary established in October 2025; and an active buyback program (1 million shares authorized, 51,200 completed) that signals management's view that shares remain undervalued.

**Risks to monitor:** SCREEN customer concentration at 16.6 percent of revenue and growing; the theoretical possibility that Entegris could terminate its licensing agreement and develop a competing standard (low probability given S-300's installed base); Chinese fluororesin fitting makers developing competitive products as China's semiconductor self-sufficiency drive intensifies; and the inherent cyclicality of semiconductor equipment spending.

The conclusion is straightforward: PILLAR is the highest-conviction name in the G1 Equipment peer group and the second-highest in the entire coverage universe. The combination of a genuine monopoly, a large foreign ownership gap, and a still-attractive valuation after a significant rally creates an opportunity that is rare in any equity market, let alone one as systematically underresearched as Japan's mid-cap semiconductor supply chain.

---

## CKD Corporation (6407.T) -- Pneumatic Valves and Flow Control

**Founded:** 1943 | **HQ:** Komaki, Aichi Prefecture | **Market Cap:** 183.7 billion yen

CKD Corporation is a leading manufacturer of pneumatic valves, actuators, and flow control equipment for semiconductor manufacturing. The company's products are the nerve endings of a semiconductor fab -- the valves, cylinders, and mass flow controllers that open, close, regulate, and measure the flow of gases and liquids through every process tool in the cleanroom.

CKD was founded in 1943 in Nagoya as Chukyo Denki, originally manufacturing electrical components. The company pivoted to pneumatic automation equipment in the postwar decades, building a reputation in factory automation components -- air cylinders, solenoid valves, and pneumatic actuators for assembly lines and industrial machinery. The transition to semiconductor applications began as Japanese chipmakers demanded cleaner, more precise versions of standard pneumatic components for use inside process equipment.

In a modern semiconductor fab, every process tool -- deposition systems, etch chambers, cleaning equipment, gas delivery panels -- contains dozens of valves that must open and close with millisecond precision, cycle millions of times without failure, and introduce zero contamination to the process gases or chemicals passing through them. CKD supplies these valves and actuators to the major semiconductor equipment makers, with Tokyo Electron (CMP-0004) and SCREEN Holdings (CMP-0003) recorded as direct clients in the supply chain graph.

CKD's semiconductor product line includes:

**High-purity pneumatic valves** for process gas delivery, designed with electropolished internal surfaces and metal-sealed connections that minimize particle generation and outgassing. These valves control the flow of reactive gases (fluorine, chlorine, silane, ammonia) into etch chambers, CVD reactors, and other tools where contamination control is paramount.

**Chemical liquid valves** made from fluororesin materials (in many cases incorporating PILLAR's fittings -- PILLAR is recorded as a supplier to CKD in the supply chain graph) for wet chemical delivery systems. These valves must withstand the same corrosive environment described in the PILLAR section.

**Mass flow controllers** that regulate the flow rate of process gases with high precision. Accurate gas flow is essential for process repeatability -- a one-percent deviation in the flow rate of an etch gas can shift the etch rate enough to cause yield-killing variability across the wafer.

**Pneumatic actuators and cylinders** used in wafer handling, chamber lid opening, and other mechanical motions within process equipment.

CKD also supplies pneumatic components to Kokusai Electric (CMP-0011) for batch deposition equipment, as recorded in the supply chain graph.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 12.40x |
| PBR | 1.24x |
| EPS | 189.0 yen |
| ROE | 9.6% |
| Revenue (FY Latest) | 149.3 billion yen |
| Revenue Growth (YoY) | +6.94% |
| Operating Margin | 11.67% |
| Dividend Yield | 2.66% |
| Foreign Ownership | 49.0% |

CKD's financial profile is distinctly different from PILLAR's. The PER of 12.40x is less than half the G1 peer median of 31.59x -- the deepest PER discount in the equipment peer group. PBR of 1.24x is roughly half the peer median of 2.49x. These extreme valuation discounts reflect CKD's positioning as a component supplier with lower market share dominance (estimated 15-20 percent of the semiconductor pneumatic valve market) and lower switching costs compared to a monopolist like PILLAR. Revenue is substantially larger at 149.3 billion yen, reflecting the company's diversified product portfolio that spans both semiconductor and general automation markets. Operating margin at 11.67 percent is below the peer median, consistent with a competitive landscape that includes Japanese rivals like SMC Corporation and global players like Swagelok and Parker Hannifin.

The dividend yield of 2.66 percent is the highest among the companies profiled in this chapter, providing income support. Foreign ownership at 49.0 percent indicates that CKD is already well-discovered by international institutions -- a meaningful contrast to PILLAR's 21.28 percent.

### Investment Perspective

CKD scored 60.0/100 in our evaluation framework, ranking in the top 10 of the coverage universe and placing it alongside Samsung and Organo in the tenth position overall. The score is driven almost entirely by the valuation dimension: CKD received a perfect A=30/30 on valuation, reflecting the extraordinary PER and PBR discounts to the peer group. The moat score (B=11/25) is moderate, reflecting solid but not dominant market positioning in a competitive valve and actuator market. Growth and profitability (C=6/15) are below average, with operating margin and ROE both trailing peer medians.

The investment case for CKD is fundamentally a value play rather than a moat play. The stock trades at a severe discount to peers because the market views it as a diversified industrial automation company that happens to have semiconductor exposure, rather than a pure-play semiconductor equipment company. With a PER of 12.4x, CKD is priced as if its semiconductor business will not grow -- a pessimistic assumption given the secular increase in cleaning and gas delivery complexity at advanced nodes. The analyst consensus is constructive, with 6 Buy, 4 Hold, and 1 Sell recommendations and an average price target of 3,119 yen (21 percent above the current price of 2,573 yen).

---

## Horiba, Ltd. (6856.T) -- The Eyes and Ears of the Fab

**Founded:** 1945 | **HQ:** Kyoto | **Market Cap:** 842 billion yen

If PILLAR supplies the arteries of a semiconductor fab and CKD supplies the valves, Horiba supplies the senses. Horiba is a global leader in analytical and measuring instruments, with a semiconductor segment that produces mass flow controllers, chemical concentration monitors, reticle and mask particle detection systems, and residual gas analyzers. The company holds over thirty percent of the global market for semiconductor mass flow controllers -- the devices that precisely regulate the flow of process gases in deposition, etching, and other tools.

Horiba was founded in 1945 by Masao Horiba in Kyoto, initially as a research institute focused on analytical measurement. The company's founding philosophy -- "Joy and Fun" (omoshiro okashiku) -- belied the seriousness of its technology. Over the following decades, Horiba expanded into automotive emissions testing (where it became the global leader), medical diagnostics, environmental monitoring, and scientific instrumentation. The semiconductor segment emerged as fabs required increasingly precise measurement and control of process gases and chemicals.

In the context of etching and cleaning, Horiba's products serve as the quality assurance layer. Consider a typical etch step: a gas mixture of CF4 and O2 is flowed into a plasma chamber at precisely controlled rates to etch silicon dioxide with a specific selectivity and profile. Horiba's mass flow controllers regulate the flow of each gas to within one percent of the set point. Horiba's residual gas analyzers monitor the chamber atmosphere in real time, detecting trace contaminants or gas composition drift that could affect etch uniformity. In wet cleaning, Horiba's chemical concentration monitors verify that the SC-1, SC-2, SPM, and DHF solutions are mixed at the correct concentrations before they contact the wafer.

These measurements are not optional. At advanced nodes, process control budgets are specified in parts per million, and any deviation outside the specification window results in wafer scrap or yield loss. Horiba's instruments provide the closed-loop feedback that keeps every chemical and gas process within specification.

Horiba's semiconductor business also extends to reticle and mask particle detection -- systems that inspect photomasks for contamination during lithography, a function complementary to Lasertec's mask defect inspection described in Chapter 7.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 16.02x |
| PBR | 2.60x |
| EPS | 857.2 yen |
| ROE | 12.07% |
| Revenue (FY Latest) | 317.37 billion yen |
| Revenue Growth (YoY) | +9.23% |
| Operating Margin | 19.35% |
| EBITDA | 65.22 billion yen |
| Dividend Yield | 1.43% |
| Foreign Ownership | 56.0% |

Horiba's financial profile reflects its status as a diversified instrumentation conglomerate with high-quality earnings. The operating margin of 19.35 percent is the second-highest among the companies in this chapter (behind PILLAR's 19.85 percent) and well above the G1 peer median of 14.9 percent. Revenue of 317.37 billion yen makes Horiba the largest company profiled in this chapter by sales, reflecting its multi-segment structure spanning automotive, medical, environmental, scientific, and semiconductor markets.

The PER of 16.02x is a significant discount to the G1 peer median of 31.59x, though this discount partly reflects the market's assessment that Horiba is not a pure-play semiconductor company. PBR of 2.60x is slightly above the peer median. ROE at 12.07 percent sits at the threshold of excellence for the equipment peer group.

Foreign ownership at 56.0 percent is the highest of any company in this chapter and among the highest in the entire Japanese semiconductor supply chain dataset. This indicates that Horiba is well-known to international investors, likely because of its global automotive emissions testing franchise, which provides brand recognition that spills over into its semiconductor business. The analyst consensus is heavily skewed toward Hold (5 Buy, 19 Hold, 1 Sell), with an average price target of 17,750 yen -- below the current price of 20,240 yen, suggesting analysts view the stock as fairly valued or slightly extended.

Horiba's evaluation score of 54.8/100 places it in the middle of our coverage universe. The score reflects a balanced but not outstanding profile across dimensions: solid valuation (A=18.8/30), moderate moat (B=15/25) driven by the 30-percent-plus mass flow controller share and high technical differentiation, and good profitability (C=9/15). The ownership dynamics score (D=1/10) is low because foreign ownership is already high (no gap to close) and the stock trades near its 52-week high. The takeaway is that Horiba is a quality business that the market has already largely discovered and priced.

---

## Competitive Landscape

The etch and clean market sits at the intersection of two competitive dynamics. In cleaning equipment, SCREEN's dominant position faces competition primarily from Tokyo Electron (which produces cleaning systems alongside its broader equipment portfolio) and from Korean and Chinese challengers. SEMES (CMP-0096), a Samsung subsidiary, produces cleaning equipment primarily for Samsung fabs. ACM Research, a US/China-based company, has been gaining share in the Chinese market. However, SCREEN's installed base advantage, process recipe library, and deep relationships with leading foundries make displacement at the leading edge extremely unlikely.

In dry etch equipment, the chapter's scope does not include dedicated coverage of the major etch system manufacturers -- Lam Research (the global leader), Tokyo Electron, and Applied Materials -- because these are primarily covered in the context of their broader equipment portfolios. However, it is worth noting that PILLAR's fluororesin fittings, CKD's pneumatic valves, and Horiba's mass flow controllers are embedded inside all of these companies' etch platforms. The component suppliers profiled in this chapter are agnostic to which equipment maker wins the etch tool competition -- they supply all of them.

At the component level, PILLAR's competitive position is effectively uncontested. Potential challengers include Entegris (which licenses PILLAR's technology rather than competing), Swagelok and Parker Hannifin (which offer high-purity metal fittings but not fluororesin fittings at the semiconductor grade), and Junkosha (a private Japanese company that produces fluororesin tubing but not the full S-300 fitting system). None of these represents a near-term competitive threat.

CKD operates in a more competitive environment, facing SMC Corporation (the world's largest pneumatic component maker by revenue), Parker Hannifin, and Festo in general pneumatic components, and specialist semiconductor valve makers in its higher-purity product lines. CKD's competitive advantage lies in its deep integration with the Japanese equipment maker ecosystem -- particularly TEL and SCREEN -- and its long qualification history at major fabs.

Horiba's mass flow controller business competes with Brooks Instrument (a subsidiary of Azimut-Benetti Group), MKS Instruments (which also produces mass flow controllers and gas analyzers), and several smaller Japanese specialists. Horiba's 30-percent-plus global share reflects strong technology and customer relationships, but the market is more fragmented than PILLAR's.

---

## Supply Chain Connections

The supply chain relationships in this chapter form a nested structure that illustrates how Japan's semiconductor ecosystem functions.

**Upstream into this chapter:** PILLAR sources fluororesin raw materials (PFA/PTFE) from Daikin Industries, AGC Inc., and Chemours (the world's largest fluoropolymer producer). The ultra-high-purity chemicals that flow through PILLAR's fittings -- particularly hydrofluoric acid -- are supplied by Stella Chemifa and Morita Chemical Industries (Chapter 5). The ultrapure water used in cleaning rinses comes from systems built by Organo Corporation and Nomura Micro Science (also Chapter 5). SCREEN's cleaning tools incorporate aluminum vacuum chambers from Marumae (CMP-0030), thermal spray coatings from Tocalo (CMP-0031), wafer transfer robots from Rorze (CMP-0041), ceramic components from NGK Insulators (CMP-0037), and pneumatic valves from CKD (CMP-0043) -- a web of Japanese component suppliers that are profiled in Chapter 12 (Fab Infrastructure).

**Within this chapter:** PILLAR supplies fluororesin fittings to SCREEN (for wet cleaning tools), to Tokyo Electron (for cleaning and etch tools), to Ebara (for CMP tools, covered in Chapter 11), and to CKD (for fluid control integration). CKD supplies pneumatic valves to SCREEN and to Tokyo Electron. Horiba supplies mass flow controllers and analyzers to equipment makers across the etch and clean ecosystem.

**Downstream from this chapter:** SCREEN supplies wet cleaning equipment to TSMC (CMP-0017) and other leading chipmakers. PILLAR supplies replacement fittings directly to TSMC (via PILLAR Taiwan), Samsung (via PILLAR Korea), Intel (via PILLAR America), SK Hynix (via PILLAR Korea), SMIC (via PILLAR Shanghai), and Hua Hong (via PILLAR Shanghai). The output of the cleaning step -- a contamination-free wafer surface -- is the prerequisite for every subsequent process step: the next deposition, the next lithography exposure, the next etch. Clean wafers are the foundation on which yield is built.

---

## Key Takeaways

- **Cleaning is the most frequently repeated operation in semiconductor manufacturing.** A leading-edge wafer passes through the cleaning tool over 200 times during fabrication. Cleaning tools represent 15-25 percent of total process equipment spending in a modern fab, making cleaning one of the largest equipment categories by capital expenditure.

- **SCREEN Holdings dominates wet cleaning equipment globally,** with over 15,000 cumulative units shipped and the leading market share in single-wafer, batch, and scrubber cleaning. Its installed base of process recipes and customer relationships creates a moat that new entrants cannot replicate quickly.

- **PILLAR Corporation is the most compelling hidden monopoly in the semiconductor supply chain.** With over 90 percent global share in fluororesin fittings, the S-300 de facto industry standard, Entegris licensing validation, and 14 mapped client relationships spanning equipment makers and fabs across four continents, PILLAR's competitive position is effectively unassailable. Its evaluation score of 72.0/100 -- the second-highest in the entire coverage universe -- reflects a combination of monopoly quality (B=24/25), persistent valuation discount (PER 21.5x vs. peer median 31.6x), and the largest foreign ownership gap (23.7 percentage points) among monopoly-quality companies.

- **CKD Corporation and Horiba, Ltd. provide the control and measurement infrastructure** that makes precision etching and cleaning possible. CKD's pneumatic valves regulate the flow of chemicals and gases through every process tool; Horiba's mass flow controllers and analyzers ensure that every gas mixture and chemical concentration is within specification. Both companies trade at significant PER discounts to the equipment peer group, with CKD in particular offering deep value at 12.4x earnings.

- **The component suppliers in this chapter are platform-agnostic.** PILLAR, CKD, and Horiba supply components to every major equipment maker -- SCREEN, Tokyo Electron, Lam Research, Applied Materials, Ebara, Kokusai Electric, and others. They do not need to predict which equipment maker will win the next generation of etch or clean tools, because they supply all of them. This breadth of exposure, combined with recurring revenue from maintenance and replacement parts, makes these component suppliers among the most defensible businesses in the semiconductor ecosystem.

---

*Data sources: CMP-0003 (SCREEN Holdings), CMP-0042 (PILLAR Corporation), CMP-0043 (CKD Corporation), CMP-0012 (Horiba), graph.json edges, evaluation_progress.json*
