# Chapter 11: CMP -- Planarization

> Chemical Mechanical Polishing is the process that makes modern chips possible -- without angstrom-level flatness after every deposited layer, multi-patterning lithography would fail and the entire back-end-of-line metal stack would collapse, and the companies that dominate this step are overwhelmingly Japanese.

## Introduction

Imagine building a skyscraper where each floor must be perfectly level to within a fraction of the thickness of a single atom before the next floor can be added. If any floor is slightly tilted, every subsequent floor amplifies that tilt, and by the twentieth story the structure is unusable. This is the challenge of Chemical Mechanical Polishing, or CMP -- the semiconductor manufacturing step that ensures each layer of a chip is flat enough for the next to be built on top of it.

Modern logic chips at the three-nanometer node contain more than fifteen layers of copper interconnect wiring, each separated by dielectric insulation, each deposited and patterned in sequence. Between every one of those layers, the wafer surface must be planarized -- polished back to a flatness measured in angstroms, where one angstrom is one ten-billionth of a meter. If this planarization fails, the lithography system that patterns the next layer cannot achieve focus across the wafer surface. At advanced nodes using multi-patterning, where a single circuit layer requires two, three, or even four sequential exposures that must overlay each other with sub-nanometer accuracy, even a few nanometers of height variation across the die can cause pattern misalignment, bridging defects, or open circuits. CMP is not optional. It is the process that makes the vertical dimension of a chip possible.

Japan dominates CMP from multiple angles. Ebara Corporation builds the polishing systems. Tokyo Seimitsu manufactures CMP equipment alongside its probing and dicing lines. Fujimi Incorporated supplies the polishing slurries that remove material atom by atom. Fuso Chemical provides the ultra-high-purity colloidal silica particles that serve as the abrasive core of those slurries -- a position so dominant it approaches monopoly. FUJIFILM Holdings leads the world in copper CMP slurry. Resonac Holdings, the company formerly known as Showa Denko, supplies CMP materials as part of the broadest semiconductor materials portfolio in Japan. And Tocalo, a thermal spray coating specialist, protects the internal surfaces of CMP and other process equipment from the punishing chemical and mechanical environment of the fab. Together, these seven companies form the infrastructure of planarization -- the invisible step that occurs more times in chip manufacturing than any other single process and that, if it failed, would halt every advanced fab on earth.

---

## The Physics of Planarization

### Why Flatness Matters

The need for CMP arises from a fundamental tension in semiconductor manufacturing. Every time material is deposited on a wafer -- whether by chemical vapor deposition, physical vapor deposition, or electroplating -- the deposited layer conforms to the topography of the surface beneath it. If the underlying surface has bumps, trenches, or steps, the new layer reproduces and often amplifies those features. After several cycles of deposition and patterning, the wafer surface becomes increasingly rough and uneven, creating what engineers call topography.

Topography is the enemy of lithography. Optical lithography systems have a finite depth of focus -- the range of heights over which the projected image remains sharp enough to define a circuit feature. At the 193-nanometer wavelength used in deep ultraviolet lithography, the depth of focus for the most aggressive pitches is on the order of one hundred to two hundred nanometers. At EUV wavelengths (13.5 nanometers), the depth of focus shrinks further. Multi-patterning techniques, which expose the same layer multiple times to achieve feature sizes smaller than the wavelength of light, are exquisitely sensitive to surface variation because each successive exposure must overlay previous patterns with precision better than a few nanometers.

If the wafer surface has height variation that exceeds the depth of focus of the lithography tool, some areas of the die will be in focus and others will not. The result is defocus -- a blurring of the pattern that produces either incomplete features (open circuits) or merged features (short circuits). Either outcome kills the chip. CMP exists to prevent this by restoring the wafer surface to a condition so flat that the lithography system can achieve uniform focus across the entire die.

### The CMP Mechanism: Chemistry Meets Mechanics

CMP is a deceptively simple concept executed with enormous complexity. The basic mechanism involves pressing a rotating wafer face-down against a rotating polishing pad while flowing a chemical slurry between them. The slurry contains two active components: abrasive particles that mechanically remove material through friction, and chemical agents that weaken or dissolve the surface layer of the material being polished.

Neither the chemistry nor the mechanics works alone. Pure mechanical abrasion -- grinding the wafer with particles -- would produce scratches, subsurface damage, and non-uniform removal. Pure chemical etching would remove material isotropically (equally in all directions), failing to preferentially remove high points. The genius of CMP is that the chemical component softens or oxidizes the surface layer, and the mechanical component selectively removes the softened material from high points -- the areas where the pad makes contact -- while leaving material in the recessed areas (trenches) relatively untouched. The net effect is a global leveling of the surface: high points are removed faster than low points until the surface converges to flatness.

The slurry composition determines the selectivity and rate of the process. Different materials require different chemistries:

**Oxide CMP** uses a silica-based slurry at alkaline pH (typically pH 10-11) to polish silicon dioxide. The alkaline environment softens the oxide surface through hydrolysis, and sub-micron silica particles abrade the softened layer away. This is the oldest and most common CMP step, used after every interlayer dielectric deposition.

**Metal CMP** uses slurries tailored to specific metals. Copper CMP, which became critical when the industry transitioned from aluminum to copper interconnects in the late 1990s, employs an acidic or near-neutral slurry containing an oxidizer (typically hydrogen peroxide), a complexing agent to dissolve the oxidized copper, a corrosion inhibitor (often benzotriazole or BTA) to protect recessed areas, and alumina or silica abrasive particles. Copper CMP is typically performed in two or three steps: a first step for bulk copper removal, a second for barrier metal removal, and sometimes a third for buffing.

**Tungsten CMP** uses iron-based oxidizing slurries to remove tungsten plug material, typically with alumina abrasives.

**Polysilicon CMP** uses ceria (cerium oxide) or silica-based slurries to polish polycrystalline silicon layers used for gate electrodes and memory cell structures.

**STI (Shallow Trench Isolation) CMP** uses ceria-based slurries that exploit the selectivity of cerium oxide for silicon dioxide over silicon nitride, allowing the polish to stop precisely when it reaches the nitride liner at the top of the trench.

### Pad Conditioning and Endpoint Detection

The polishing pad is not a passive component. CMP pads, typically made of polyurethane with a microporous or grooved surface, degrade during polishing as their surface asperities are worn down and their pores become clogged with debris. To maintain consistent removal rates, a diamond-encrusted conditioning disc is swept across the pad surface during or between polishes, roughening the pad to restore its cutting ability. Pad conditioning is a delicate balance: too aggressive, and the pad wears out prematurely; too gentle, and the removal rate drifts, causing thickness non-uniformity across the wafer.

Endpoint detection -- knowing when to stop polishing -- is equally critical. Over-polishing removes too much material, thinning the metal lines and increasing their electrical resistance. Under-polishing leaves excess material on the surface, causing short circuits or excessive topography. Modern CMP systems use in-situ endpoint detection methods including optical interferometry (measuring reflected light to determine film thickness in real time), motor current monitoring (the friction between wafer and pad changes as different materials are exposed), and eddy current sensing (which can measure the thickness of conductive films without optical access).

### Dishing, Erosion, and the Defect Landscape

CMP introduces its own class of defects that must be managed. **Dishing** occurs when the center of a wide metal feature is polished lower than its edges, creating a concave surface. This happens because the pad, being compliant, deflects slightly into wide features and continues to remove material even after the surrounding dielectric is clear. Dishing increases the resistance of the metal line and creates topography that propagates to subsequent layers.

**Erosion** is the over-polishing of the dielectric surface in areas with high metal pattern density. Dense arrays of narrow metal lines cause the pad to remove dielectric material more aggressively than in areas with isolated features, leading to a systematic thickness difference between dense and isolated regions. Both dishing and erosion become more severe as chip designs use wider metal lines or denser metal patterns, making CMP process optimization intimately tied to the design rules of the process node.

**Scratches** from oversized abrasive particles, **corrosion** from chemical attack during or after polishing, and **particle contamination** from slurry residue are additional defect modes that require careful management through slurry filtration, post-CMP cleaning, and tool maintenance.

---

## CMP in the Back-End-of-Line: A Step Repeated Fifteen Times

Front-end-of-line (FEOL) processing creates the transistors. Back-end-of-line (BEOL) processing connects them with metal wiring. At advanced nodes, the BEOL accounts for the majority of the process steps and an increasingly large fraction of manufacturing cost and yield loss.

A modern three-nanometer logic chip has thirteen to fifteen metal layers, designated M1 through M15, arranged in a hierarchy. The lowest layers (M1 through M3) carry local interconnects between nearby transistors and have the finest pitch -- as small as twenty to thirty nanometers. Middle layers (M4 through M9) carry semi-global routing at intermediate pitches. Upper layers (M10 through M15) carry global power distribution and clock routing at the widest pitches.

Each metal layer requires the following sequence: deposit a dielectric layer, pattern trenches and vias using lithography and etch, deposit a barrier metal liner (typically tantalum or tantalum nitride), fill the trenches with copper by electroplating, and then CMP the excess copper and barrier metal to leave copper only in the trenches. This is the damascene process, and each metal layer requires at least one CMP step, often two (one for bulk copper removal and one for barrier metal removal). Additionally, CMP is required after shallow trench isolation (STI) in the FEOL, after polysilicon gate patterning, and in some process flows after interlayer dielectric deposition.

The math is straightforward: fifteen metal layers at one to two CMP steps each, plus three to four FEOL CMP steps, yields roughly twenty to thirty CMP operations per wafer. No other single process step -- not lithography, not etch, not deposition -- is repeated as many times. CMP is the most frequently performed process in advanced chip manufacturing, and its cumulative impact on yield is correspondingly enormous. If each CMP step has a defect rate of even 0.01 percent, the cumulative probability of a CMP-induced defect across twenty-five steps becomes non-trivial. This is why CMP equipment reliability, slurry consistency, and endpoint detection accuracy are not incremental concerns but existential ones for fab operators.

---

## CMP Systems: The Polishing Platforms

### Ebara Corporation (6361.T) -- CMP Systems and Vacuum Pumps

**Founded:** 1912 | **HQ:** Tokyo | **Market Cap:** 2.51 trillion yen

Ebara Corporation is one of those Japanese industrial companies whose name suggests nothing about semiconductors. Founded in 1912 as a pump manufacturer, Ebara spent its first eight decades building fluid machinery for water treatment, chemical plants, and power generation. The company still earns the majority of its revenue from pumps, compressors, and environmental engineering systems. But its Precision Machinery segment -- which builds CMP equipment and dry vacuum pumps for semiconductor manufacturing -- has become the strategic heart of the company and the primary driver of its growth.

Ebara's CMP equipment business traces to the 1990s, when the transition from aluminum to copper interconnects created massive demand for planarization tools. Ebara developed its FREX series of CMP systems, which have become a standard platform at the world's leading fabs. The FREX platform uses a multi-head design where multiple wafers are polished simultaneously on separate platens, with automated wafer handling and in-situ endpoint detection. Ebara is the world's number-two supplier of CMP equipment, behind only Applied Materials of the United States.

What distinguishes Ebara from pure-play CMP equipment makers is its parallel position in dry vacuum pumps. Every vacuum-based process in a semiconductor fab -- CVD, PVD, etch, ion implantation -- requires dry vacuum pumps to maintain the process chamber at sub-atmospheric pressure. Ebara is the world's number-two supplier of dry vacuum pumps for semiconductor applications, again behind only a Western competitor (Edwards, now part of the Atlas Copco group). This dual position in CMP systems and vacuum pumps gives Ebara unusual breadth of exposure to semiconductor capital equipment spending.

The semiconductor segment represents over thirty percent of Ebara's total revenue, and its growth rate far exceeds the traditional pump and environmental businesses. Ebara's confirmed clients include the five largest chipmakers in the world: TSMC, Samsung, Intel, SK Hynix, and Micron. In 2024, Ebara opened a new facility near TSMC's Kumamoto fab (JASM), positioning itself to serve the rapid expansion of Japanese semiconductor manufacturing capacity driven by government subsidies.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 21.31x |
| EPS | 166.2 yen |
| ROE | 15.81% |
| Revenue (FY) | 958.0 billion yen |
| Operating Margin | 8.0% |
| Dividend Yield | 1.04% |
| Analyst Consensus | 8 Buy, 0 Hold, 0 Sell |
| 52-Week Range | 1,770 - 5,919 yen |

Ebara's operating margin of eight percent reflects the dilution from its lower-margin pump and environmental divisions. The semiconductor segment operates at substantially higher margins, but the company does not disclose segment-level profitability in detail. The stock has appreciated dramatically -- from a 52-week low of 1,770 yen to a recent price of 5,524 yen -- as investors have re-rated the company for its semiconductor exposure. All eight covering analysts rate it a Buy, with an average target price of 4,960 yen, which the stock has already surpassed, suggesting the rally has outrun consensus expectations.

Ebara's PER of 21.3x is in line with the G1 Semiconductor Equipment peer group median of 31.6x only if adjusted for the company's conglomerate structure. A sum-of-the-parts analysis that assigns a higher multiple to the semiconductor division and a lower multiple to the pump business would suggest the semiconductor operations are implicitly valued at a premium -- or alternatively, that the market has not yet fully disaggregated the value.

### Tokyo Seimitsu (7729.T) -- CMP, Probing, and Dicing Under One Roof

**Founded:** 1949 | **HQ:** Tokyo | **Market Cap:** 561.8 billion yen

Tokyo Seimitsu, which operates under the brand name ACCRETECH, is one of the most versatile equipment companies in the semiconductor industry. It manufactures CMP equipment, wafer probers (world number one with forty-six percent global share), dicing machines (approximately ten percent global share behind DISCO), polish grinders, edge grinders, and precision coordinate measuring machines. This breadth is unusual -- most semiconductor equipment companies specialize in a single process step.

Tokyo Seimitsu's CMP equipment business is smaller than Ebara's but serves a complementary market. While Ebara's FREX systems target the largest logic fabs running the most advanced nodes, Tokyo Seimitsu's CMP offerings find traction in memory fabs, mature-node logic, and specialty applications where the company's integrated suite of back-end equipment -- probing, dicing, and CMP on a single platform -- offers workflow advantages. The company supplies CMP equipment to TSMC, SMIC, Hua Hong Semiconductor, UMC, GlobalFoundries, DB HiTek, and multiple Chinese foundries, reflecting broad geographic reach that includes markets where Ebara's presence is less established.

The company's Semiconductor Production Equipment (SPE) segment accounts for seventy-four percent of total revenue, with the remaining twenty-six percent from its Metrology segment. Revenue for FY2025/3 reached 150.5 billion yen, growing 11.8 percent year-over-year. The stock trades at 15,820 yen per share, near the top of its 52-week range (6,148 to 16,170 yen), reflecting strong institutional demand -- foreign ownership stands at fifty percent, among the highest for any mid-cap Japanese semiconductor equipment company.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 21.26x |
| PBR | 2.35x |
| EPS | 111.78 yen |
| ROE | 15.3% |
| Revenue (FY2025/3) | 150.5 billion yen |
| Revenue Growth | 11.8% |
| Operating Margin | 19.0% |
| Dividend Yield | 1.4% |
| Foreign Ownership | 50.06% |
| Analyst Consensus | 3 Buy, 0 Hold, 1 Sell |
| 52-Week Range | 6,148 - 16,170 yen |

The competitive landscape for Tokyo Seimitsu's CMP business is more fragmented than for its probing or dicing businesses. In CMP equipment, Applied Materials is the global leader, Ebara is number two, and Korean competitor KCTech (with its VENTUS system) has been gaining share. Chinese domestic competitors have emerged aggressively: Huahai Qingke holds over fifty percent of China's domestic 12-inch CMP market, and state-owned CETC subsidiary Shuoke Jingwei competes in both CMP and dicing. Tokyo Seimitsu's CMP market share in China has come under significant pressure -- more so than its probing or dicing positions, where its technology lead remains wider.

#### Investment Perspective

Tokyo Seimitsu scored 61.0 in the six-dimension evaluation framework, placing it eighth among all seventy-four scored companies. The investment thesis centers on dual leadership: the company's number-one position in wafer probing and its multi-product portfolio create a diversified revenue base that is less cyclical than single-product equipment peers.

At PER 21.3x against the G1 equipment peer median of 31.6x, the stock trades at a meaningful discount despite consistent revenue growth and a fifty-percent foreign ownership level that signals institutional recognition of quality. The PBR of 2.35x is close to the G1 median of 2.49x, suggesting the valuation discount is concentrated in the earnings multiple rather than the balance sheet.

The primary risk is China, which represents thirty-four percent of revenue. Geopolitical tensions and export controls could restrict sales to Chinese customers, while aggressive domestic substitution by Huahai Qingke, NAURA, and CETC could erode market share even absent regulatory constraints. The CMP business is most exposed to this risk -- Chinese competitors have already achieved parity in CMP equipment for 12-inch wafers, while the probing business retains a wider technology moat.

Catalysts include continued AI-driven capital expenditure at TSMC and Samsung, the December 2025 announcement of a joint die-level prober development project with Advantest, and the potential for CMP business recovery if Tokyo Seimitsu can differentiate on integrated back-end solutions.

---

## CMP Consumables: The Slurry Ecosystem

If CMP equipment is the polishing platform, slurry is the medium that does the actual work. The CMP slurry market -- estimated at over five billion dollars globally -- is one of the most technically demanding consumables markets in semiconductor manufacturing. Slurry must be reformulated for each new material, each new process node, and each specific CMP step within the process flow. A fab running a fifteen-metal-layer process may use six to ten different slurry formulations, each optimized for a different combination of material, removal rate, selectivity, and defect performance.

The slurry supply chain has a distinctive structure: slurry formulators (who blend the final product) depend on upstream suppliers of ultra-pure abrasive particles, and those particle suppliers often hold the most defensible positions in the value chain.

### Fujimi Incorporated (5384.T) -- Precision Abrasives and CMP Slurry

**Founded:** 1950 | **HQ:** Kiyosu, Aichi | **Market Cap:** 196.2 billion yen

Fujimi Incorporated was manufacturing precision abrasives decades before the semiconductor industry existed. Founded in 1950, the company built its initial business on synthetic abrasive powders for polishing optical lenses, metalworking tools, and ceramic components. When the semiconductor industry emerged and began requiring atomically smooth surfaces, Fujimi's expertise in particle synthesis and surface chemistry positioned it as a natural supplier.

Today, Fujimi holds approximately eighteen percent of the global CMP slurry market -- making it one of the top three slurry suppliers alongside American competitors Cabot Microelectronics (now part of CMC Materials, acquired by Entegris) and Versum Materials (absorbed into Merck KGaA). But Fujimi's position is far stronger in specific segments than the overall market share suggests. In polysilicon CMP for front-end-of-line processing -- the polishing step used to planarize polycrystalline silicon gate electrodes -- Fujimi commands over fifty percent of the global market. Its slurries are widely adopted for five-nanometer and three-nanometer processes at Taiwanese foundries, with TSMC and Intel confirmed as major customers.

Fujimi's revenue growth reflects the intensity of advanced-node ramp: FY2025 revenue grew 21.5 percent year-over-year, driven primarily by advanced logic semiconductor materials. The most recent quarterly data shows polishing slurry sales up 18.9 percent. This growth trajectory is structural -- as nodes shrink and metal layer counts increase, the volume of CMP slurry consumed per wafer rises proportionally.

Beyond semiconductors, Fujimi supplies wafer polishing materials (with over ninety percent global share in wafer polishing abrasives) and abrasives for hard disk drive substrates. This diversification provides a revenue floor, but the semiconductor CMP business is the growth engine.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 17.92x |
| PBR | 2.08x |
| EPS | 127.1 yen |
| ROE | 12.7% |
| Revenue Growth | 13.0% |
| Operating Margin | 18.5% |
| Dividend Yield | 2.31% |
| Foreign Ownership | 27.0% |
| Analyst Consensus | 0 Buy, 2 Hold, 0 Sell |
| 52-Week Range | 1,536 - 3,205 yen |

Fujimi trades at PER 17.9x against the G2 Materials peer median of 17.0x -- essentially at parity with its peer group. The PBR of 2.08x represents a moderate premium to the G2 median of 1.32x, reflecting the market's recognition of Fujimi's above-average profitability (operating margin of 18.5 percent versus the G2 median of 15.2 percent) and growth rate. Foreign ownership at twenty-seven percent is moderate for a Japanese semiconductor materials company, suggesting some but not full international recognition.

The scored evaluation assigned Fujimi a final score of 50.8 -- below the top tier. The score reflects limited valuation discount (the stock is fairly valued rather than cheap), moderate supply chain centrality (Fujimi operates in a competitive slurry market rather than a monopoly position), and mixed analyst sentiment (two Holds, zero Buys). The company's strength lies in its capacity expansion -- new production lines are being built to meet advanced-node demand -- and in policy tailwinds from Japan's semiconductor industrial strategy.

### Fuso Chemical Co., Ltd. (4368.T) -- The Invisible Monopolist in Colloidal Silica

**Founded:** 1952 | **HQ:** Osaka | **Market Cap:** 220.4 billion yen

If there is a single company in the CMP supply chain that embodies Japan's hidden dominance thesis, it is Fuso Chemical. This is a company with 930 employees and 75.5 billion yen in revenue that commands approximately ninety percent of the global market for ultra-high-purity colloidal silica used in semiconductor CMP slurries. That figure is not a typographical error. Nine out of ten nanoscale silica particles used in CMP processes worldwide trace their origin to Fuso Chemical's factories.

Colloidal silica is the abrasive core of most oxide CMP slurries. These are not ordinary silica particles -- they are nanometer-scale spheres synthesized with controlled size distribution (typically twenty to one hundred nanometers in diameter) and purified to a standard where total metal ion contamination is below one part per million. The manufacturing process requires precise control of nucleation, growth, and surface chemistry -- capabilities that Fuso Chemical has developed over decades.

The company's dominance arises from a combination of process know-how, purity standards, and scale. CMP slurry formulators -- whether Fujimi, FUJIFILM, Cabot, or any other blender -- do not synthesize their own abrasive particles. They purchase them from a particle manufacturer and blend them with proprietary chemical additives. Fuso Chemical is, in practical terms, the particle manufacturer for the entire industry. Switching to an alternative particle supplier would require re-qualifying the slurry at every fab where it is used, a process that can take twelve to twenty-four months and involves re-running all defect and yield validation tests. Given that Fuso's particles already meet the most stringent purity and size specifications in the industry, and given the risk and cost of re-qualification, customers have no incentive to switch.

In 2022, Fuso Chemical expanded its production capacity by fifty percent to meet accelerating demand from advanced-node fabs. Its customer base, while not disclosed at the individual company level, functionally includes every significant chipmaker in the world -- because the slurry formulators who buy Fuso's particles sell their finished slurries to TSMC, Samsung, Intel, SK Hynix, and Micron. Fuso sits one step upstream from the fab, invisible to most supply chain analyses, but structurally irreplaceable.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 17.1x |
| PBR | 1.6x |
| EPS | 372.69 yen |
| ROE | 11.2% |
| Revenue (FY) | 75.5 billion yen |
| Revenue Growth | 7.0% |
| Operating Margin | 17.5% |
| Dividend Yield | 1.36% |
| Analyst Consensus | 1 Buy, 1 Hold, 1 Sell |
| 52-Week Range | 2,922 - 6,360 yen |

#### Investment Perspective

Fuso Chemical scored 55.8 in the evaluation framework, earning a formal investment thesis as one of the highest-conviction names in the dataset. The thesis is built on a simple foundation: a near-monopolist trading at a reasonable valuation with structural demand growth and no meaningful substitution risk.

At PER 17.1x, Fuso trades at a marginal premium to the G2 Materials median of 17.0x -- essentially at parity despite holding a ninety-percent market share in a product with no viable substitute. The PBR of 1.6x is modest for a company with monopolistic characteristics. Operating margin of 17.5 percent and revenue growth of 7.0 percent are solid for a specialty materials business, and the growth rate understates the underlying trajectory because Fuso's revenue scales with global wafer starts and CMP slurry consumption, both of which are growing faster than the broader semiconductor market.

Fuso Chemical is not forex sensitive -- its products are sold in yen to Japanese slurry formulators -- which removes a risk factor that affects most other Japanese semiconductor companies. The company's capacity expansion plans are well-timed, adding production just as advanced-node fabs proliferate globally. Japan's semiconductor industrial policy provides additional tailwinds.

The key risk is the small market capitalization of 220.4 billion yen, which limits institutional liquidity and means the stock can be volatile on modest trading volumes. Analyst coverage is thin -- three analysts, split one Buy, one Hold, one Sell -- reflecting the lack of attention that Japanese micro-cap monopolists typically receive. For an investor willing to accept lower liquidity, Fuso Chemical represents a structurally protected business at a price that barely reflects its monopoly status.

### FUJIFILM Holdings Corporation (4901.T) -- The World Leader in Copper CMP Slurry

**Founded:** 1934 | **HQ:** Tokyo | **Market Cap:** 3.64 trillion yen

FUJIFILM's presence in the CMP chapter may surprise readers who associate the company with cameras and film. But FUJIFILM Holdings is one of the most successful corporate reinventions in Japanese industrial history. When digital photography destroyed the photographic film market in the 2000s, FUJIFILM pivoted aggressively into healthcare, life sciences, and advanced materials -- leveraging its core competencies in chemical synthesis, precision coating, and thin-film engineering. Semiconductor materials became a major growth vector.

FUJIFILM is the world's number-one supplier of copper CMP slurry -- the slurry used to planarize the copper interconnect layers that form the wiring of every modern chip. Copper CMP is the most demanding and highest-volume CMP application in advanced manufacturing, consuming more slurry per wafer than any other CMP step. FUJIFILM's leadership in this segment reflects decades of process chemistry expertise derived from its photographic film heritage -- the chemistry of grain formation, surface coating, and colloidal dispersion used in film manufacturing maps directly to the synthesis of CMP slurry abrasives and chemical additives.

The company's semiconductor materials portfolio extends well beyond CMP slurry. FUJIFILM also produces photoresists (including a PFAS-free ArF resist developed in 2025), process chemicals, and advanced materials for semiconductor packaging. The company has publicly stated a target of five trillion yen in semiconductor materials sales by 2030, signaling a strategic commitment to the segment that goes far beyond opportunistic participation.

FUJIFILM supplies CMP slurry and photoresist to TSMC, Samsung, and Intel -- the three largest logic chipmakers -- as confirmed by graph.json supplier edges. The company's approach to customer service has been described as "ultimate customer service" for TSMC, suggesting a depth of technical collaboration that goes beyond simple material supply.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 15.43x |
| PBR | 1.16x |
| EPS | 226.2 yen |
| ROE | 7.87% |
| Revenue (FY) | 3,200.0 billion yen |
| Revenue Growth | 4.83% |
| Operating Margin | 9.29% |
| Dividend Yield | 2.04% |
| Foreign Ownership | 30.0% |
| Analyst Consensus | 10 Buy, 4 Hold, 0 Sell |
| 52-Week Range | 2,516 - 3,787 yen |

FUJIFILM's financial profile is that of a diversified conglomerate -- its 3.2 trillion yen in revenue spans healthcare (Fujifilm Healthcare, formerly Hitachi Medical), imaging, document solutions, and advanced materials. The semiconductor materials division, while strategically important, represents a single-digit percentage of total revenue. This means the stock does not trade as a pure-play semiconductor materials investment, and investors seeking direct CMP exposure should consider this dilution.

At PER 15.4x and PBR 1.16x, FUJIFILM trades below both the G2 Materials peer group medians (PER 17.0x, PBR 1.32x) -- a discount that likely reflects the market's view of the company as a slow-growth conglomerate rather than a high-growth semiconductor play. Ten out of fourteen analysts rate it a Buy, suggesting professional consensus that the stock is undervalued. The evaluation framework scored FUJIFILM at 59.2 -- above the median but below the top tier, consistent with a company that has strong competitive positions embedded within a broader business that dilutes the investment case.

### Resonac Holdings Corporation (4004.T) -- The Broadest Semiconductor Materials Platform

**Founded:** 1939 (as Showa Denko K.K.) | **HQ:** Tokyo | **Market Cap:** 1.97 trillion yen

Resonac Holdings is the product of the 2020 merger between Showa Denko K.K. and Hitachi Chemical, rebranded in January 2023. The merger created what the company describes as the world's number-one semiconductor materials supplier, excluding silicon wafers. This is a sprawling materials platform that supplies CMP slurries, high-purity gases, epoxy encapsulants, die-bonding materials, SiC epitaxial wafers, functional chemicals, and hard disk media to the global semiconductor industry.

Resonac's CMP materials business is one division within this broad portfolio. The company produces CMP slurries for oxide, metal, and barrier polishing, drawing on chemical synthesis capabilities inherited from both Showa Denko (specialty chemicals, gases) and Hitachi Chemical (electronic materials, packaging). The company is a member of the JOINT2 consortium, a group of twelve companies collaborating on next-generation semiconductor technology, which provides early access to emerging material requirements at future process nodes.

Resonac's competitive advantage in CMP is not market dominance in any single slurry type but rather the breadth of its materials portfolio. A fab purchasing manager working with Resonac can source CMP slurries, process gases, encapsulants, and die-attach materials from a single supplier relationship, simplifying procurement and qualification. This platform effect is the company's stated strategic differentiator, and the "open innovation" approach to next-generation semiconductor development -- collaborating with equipment makers and chipmakers simultaneously -- is designed to entrench Resonac as a system-level materials partner rather than a point-product supplier.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 16.79x |
| EPS | 197.04 yen |
| ROE | 5.72% |
| Revenue (FY) | 1,390.0 billion yen |
| Revenue Growth | 0.8% |
| Operating Margin | 4.62% |
| Dividend Yield | 1.27% |
| Analyst Consensus | 10 Buy, 2 Hold, 0 Sell |
| 52-Week Range | 2,235 - 10,945 yen |

Resonac's financial profile shows the strain of post-merger integration. Revenue growth of 0.8 percent is essentially flat, and operating margin of 4.62 percent is well below the G2 Materials peer median of 15.2 percent, reflecting the drag of lower-margin legacy businesses (particularly hard disks and basic chemicals) alongside the higher-margin semiconductor materials divisions. ROE of 5.72 percent is also below the peer median, consistent with a company still optimizing its asset base after a major acquisition.

The stock's dramatic 52-week range -- from 2,235 yen to 10,945 yen -- reflects the market's evolving view of Resonac's semiconductor transformation potential. Twelve analysts covering the company are overwhelmingly positive (ten Buy, two Hold), suggesting professional consensus that the transformation will succeed and margins will expand as legacy businesses are divested or restructured. The evaluation framework scored Resonac at 54.8, reflecting the tension between strong competitive positions (world number one in SiC epitaxial wafers, broad CMP portfolio) and weak current financials.

---

## Thermal Spray Coatings: The Invisible Protective Layer

### Tocalo Co., Ltd. (3433.T) -- Thermal Spray Coatings for Semiconductor Equipment

**Founded:** 1951 | **HQ:** Kobe | **Market Cap:** 148.7 billion yen

Tocalo is the most unusual company in this chapter and perhaps one of the most unusual in the semiconductor supply chain. It does not make equipment. It does not make materials that go onto or into chips. It applies thermal spray coatings to the internal surfaces of semiconductor manufacturing equipment -- including CMP tools, etch chambers, CVD chambers, and deposition systems -- to protect them from the corrosive chemicals, abrasive particles, and extreme temperatures they encounter during operation.

Thermal spray coating is a surface engineering process where a material (typically a ceramic, metal, or cermet) is heated to a molten or semi-molten state and sprayed onto a substrate surface at high velocity. The sprayed particles flatten on impact and solidify, building up a coating that can be tens to hundreds of micrometers thick. In semiconductor applications, these coatings serve multiple purposes: they protect aluminum or stainless steel chamber surfaces from attack by fluorine-based plasma gases and corrosive chemicals, they reduce particle generation from chamber wall erosion (which would contaminate the wafers), and they can be engineered to have specific surface roughness or porosity to control plasma behavior.

Tocalo is Japan's number-one thermal spray coating company and operates what it describes as an "engineering-type service" rather than a simple coating application. This means the company works with equipment manufacturers to co-develop coating solutions optimized for specific chamber geometries, process chemistries, and lifetime requirements. The distinction matters -- Tocalo is not applying commodity coatings from a catalog but engineering bespoke surface treatments that become an integral part of the equipment's performance specification.

The company's largest customer is Tokyo Electron, which accounts for twenty-seven percent of Tocalo's revenue. Applied Materials is the second-largest customer. Through these two equipment makers, Tocalo's coatings end up inside process chambers at every major fab in the world. The relationship with Tokyo Electron, in particular, represents a deep technical partnership: TEL specifies Tocalo coatings in its chamber designs, and fabs that purchase TEL equipment receive chambers with Tocalo coatings already applied. Switching to a different coating supplier would require TEL to re-qualify its chambers, a process that TEL has no incentive to undertake given Tocalo's consistent quality and co-development relationship.

Tocalo also provides coating services for SCREEN Holdings' wet cleaning equipment, as confirmed by the graph.json edge showing Tocalo as a supplier of thermal spray coatings to both Tokyo Electron (CMP-0004) and SCREEN Holdings (CMP-0003). In the CMP context, Tocalo coatings protect the process-critical surfaces of CMP tools from the abrasive slurries and corrosive chemicals used in polishing.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 16.67x |
| EPS | 150.0 yen |
| ROE | 13.3% |
| Revenue (FY) | 57.0 billion yen |
| Revenue Growth | 10.0% |
| Operating Margin | 28.7% |
| Dividend Yield | 2.8% |
| Analyst Consensus | 3 Buy, 0 Hold, 0 Sell |
| 52-Week Range | 1,369 - 2,524 yen |

Tocalo's financial profile is remarkable. An operating margin of 28.7 percent is the highest of any company in this chapter and nearly double the G2 Materials peer median of 15.2 percent. This margin reflects the value-added nature of Tocalo's engineering services -- the company charges for specialized expertise, not commodity materials, and its costs are primarily labor and equipment depreciation rather than expensive raw materials. ROE of 13.3 percent exceeds the G2 peer median of 9.4 percent, and revenue growth of ten percent reflects the secular expansion of semiconductor equipment installed base.

The stock trades at PER 16.7x, below the G2 median of 17.0x, and all three covering analysts rate it a Buy. The stock recently traded at 2,680 yen, above its 52-week high of 2,524 yen, suggesting strong recent momentum. The evaluation framework scored Tocalo at 55.5 (when calculated from available data points, acknowledging several null fields that reduce confidence). The score is potentially understated due to missing data on foreign ownership and price-versus-52-week positioning, as the pro-rata rescaling of partial data may not fully capture the company's quality.

---

## Competitive Landscape

The CMP competitive landscape divides into two distinct arenas: equipment and consumables.

**Equipment:** The global CMP equipment market is dominated by Applied Materials (United States), which holds the largest share through its Mirra and Reflexion series. Ebara is the clear number two globally, with particular strength at advanced logic fabs. Tokyo Seimitsu occupies a smaller niche, leveraging its integrated back-end portfolio. Outside Japan, the most significant emerging competitor is KCTech of South Korea, whose VENTUS CMP system has gained traction at Samsung and Korean memory fabs. In China, Huahai Qingke has achieved over fifty percent domestic market share in 12-inch CMP equipment, making CMP one of the process steps where Chinese domestic substitution has progressed furthest. State-owned CETC subsidiary Shuoke Jingwei and TSD (Tesi Di) also compete in the Chinese market. This competitive pressure is most acute for Tokyo Seimitsu, whose CMP share in China has eroded faster than its probing or dicing positions.

**Consumables:** The CMP slurry market is more fragmented but structurally stickier. Each slurry formulation must be qualified at each fab for each CMP step, creating high switching costs. FUJIFILM leads in copper CMP slurry. Fujimi leads in polysilicon CMP and wafer polishing abrasives. CMC Materials (now Entegris) is the global leader in tungsten CMP slurry. Resonac competes across multiple slurry categories without dominant share in any single one. The upstream particle market, by contrast, is a near-monopoly: Fuso Chemical supplies approximately ninety percent of the ultra-high-purity colloidal silica particles used across all silica-based CMP slurries, regardless of who formulates the final product. This gives Fuso a unique structural position -- it is simultaneously a supplier to and a beneficiary of every CMP slurry competitor.

**Coatings:** Tocalo's competitive position in thermal spray coatings is defined by its customer relationships rather than formal market share statistics. The company's entrenchment at Tokyo Electron and Applied Materials creates a self-reinforcing dynamic: equipment makers specify Tocalo coatings, fabs receive equipment with Tocalo coatings, and re-qualification risk prevents switching. Japanese domestic competitors exist in thermal spray coatings, but none has achieved comparable penetration in the semiconductor segment.

---

## Supply Chain Connections

The CMP chapter sits at the intersection of multiple upstream and downstream supply chains.

**Upstream dependencies:** CMP equipment and slurry companies depend on precision engineering components, specialty chemicals, and ultra-pure raw materials from earlier in the supply chain. Fuso Chemical's colloidal silica is the critical upstream input for most CMP slurries. PILLAR Corporation's fluororesin fittings (Chapter 10) carry the corrosive slurries through CMP tools. Tocalo's thermal spray coatings protect the equipment from the very chemicals and abrasives used in CMP. This creates a circular supply chain where CMP's own consumables determine the service requirements for its own equipment.

**Downstream connections:** CMP's output -- a planarized wafer surface -- feeds directly back into the lithography and deposition steps for the next metal layer. The quality of CMP planarization determines the process window for the subsequent lithography exposure (Chapter 6), the adhesion of the next deposited layer (Chapter 9), and ultimately the yield of the finished chip. CMP also feeds into wafer testing (Chapter 13) through its impact on inter-layer via resistance and metal line quality -- if CMP leaves excessive dishing or erosion, the test step downstream will detect elevated resistive open failures.

**Cross-chapter company appearances:** FUJIFILM (CMP-0040) appears in both this chapter (CMP slurry) and Chapter 8 (photoresist), reflecting the company's dual semiconductor materials business. Tokyo Seimitsu (CMP-0001) appears in this chapter for CMP equipment, in Chapter 13 for wafer probing, and in Chapter 14 for dicing equipment. Resonac (CMP-0008) appears here for CMP materials and in Chapter 15 for advanced packaging materials. Tocalo (CMP-0031) could equally appear in Chapter 10 (etching and cleaning) or Chapter 9 (deposition), as its coatings protect equipment across all of those process steps.

**Key supply chain edges from graph.json:**

- Ebara (CMP-0036) supplies CMP systems and vacuum pumps to TSMC, Samsung, Intel, SK Hynix, and Micron
- Fujimi (CMP-0007) supplies CMP slurry to TSMC and Intel
- Fuso Chemical (CMP-0013) supplies CMP slurry to TSMC, Samsung, and Intel
- FUJIFILM (CMP-0040) supplies CMP slurry and photoresist to TSMC, Samsung, and Intel
- Resonac (CMP-0008) supplies semiconductor materials to TSMC, Samsung, and Intel
- Tocalo (CMP-0031) supplies thermal spray coatings to Tokyo Electron and SCREEN Holdings
- Tokyo Seimitsu (CMP-0001) supplies probing, dicing, and CMP equipment to TSMC, Samsung, Intel, SK Hynix, Micron, Kioxia, and over twenty additional foundries and OSATs worldwide
- PILLAR (CMP-0042) supplies fluororesin fittings to Ebara (CMP-0036)

---

## Key Takeaways

- **CMP is the most frequently repeated process step in advanced chip manufacturing.** A single leading-edge wafer undergoes twenty to thirty CMP operations, more than any other process step. This frequency makes CMP consumables -- slurries, pads, and conditioning discs -- a high-volume, recurring revenue business tied directly to wafer starts.

- **Angstrom-level flatness is not optional for multi-patterning.** The depth of focus constraints of both DUV multi-patterning and EUV lithography make planarization a prerequisite for every subsequent patterning step. CMP failure cascades through the entire BEOL stack.

- **Fuso Chemical's ninety-percent share of colloidal silica particles represents one of the deepest chokepoints in the semiconductor supply chain.** Unlike equipment monopolies, which are at least partially visible, Fuso's position is hidden one level upstream of the slurry formulators, making it structurally invisible to most industry analyses -- and correspondingly undervalued.

- **Japan dominates CMP from equipment through consumables to coatings.** Ebara and Tokyo Seimitsu in equipment, Fujimi and FUJIFILM in slurry, Fuso Chemical in abrasive particles, Resonac in materials breadth, and Tocalo in equipment protection -- collectively, these seven companies form a Japanese infrastructure layer that every fab depends on.

- **Chinese CMP equipment substitution is the most advanced of any semiconductor process step,** with Huahai Qingke holding over fifty percent of the Chinese domestic 12-inch market. This makes CMP equipment the bellwether for the broader Chinese semiconductor localization effort and poses the most immediate competitive risk to Tokyo Seimitsu's CMP business. CMP consumables, by contrast, remain dominated by Japanese and Western suppliers due to higher qualification barriers and tighter purity specifications.

---

*Data sources: CMP-0036 (Ebara), CMP-0007 (Fujimi), CMP-0013 (Fuso Chemical), CMP-0008 (Resonac), CMP-0040 (FUJIFILM), CMP-0031 (Tocalo), CMP-0001 (Tokyo Seimitsu), evaluation_progress.json, graph.json*
