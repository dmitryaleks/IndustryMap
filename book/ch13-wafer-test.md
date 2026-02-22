# Chapter 13: Wafer Test & Probing

> Before a single die is separated from its wafer, every chip must prove it works -- and the companies that build the machines to make that determination hold one of the most strategically important and least understood positions in the semiconductor supply chain.

## Introduction

A finished semiconductor wafer, after hundreds of process steps spanning lithography, deposition, etching, CMP, and metallization, carries thousands of individual integrated circuits arranged in a precise grid across its surface. Each die is the product of weeks of processing, hundreds of chemical and thermal steps, and capital investment that can exceed ten thousand dollars per wafer at leading-edge nodes. But not every die works. Defects are inevitable -- a particle landing during lithography, a void forming during deposition, a misalignment accumulating across multiple patterning steps, a gate oxide thinned by a fraction of an angstrom too many. The question is not whether defects exist. The question is which die have them.

Wafer test -- sometimes called wafer sort, wafer probe, or simply "probe" -- is the process of electrically testing every die on a completed wafer before it is diced into individual chips. A machine called a wafer prober positions the wafer with sub-micron accuracy beneath an array of tiny contact points -- a probe card -- that simultaneously touch hundreds or thousands of pads on one or more die. An automatic test equipment system, connected to the probe card through a complex interface, then sends electrical signals into the die and measures the responses. In a matter of seconds, the tester determines whether each die meets its functional and parametric specifications. Die that pass are marked good. Die that fail are marked for discard. The wafer is then sent downstream for dicing and packaging, and only the known-good die proceed to the expensive packaging and assembly steps that follow.

The economics of this gate are stark. A single AI accelerator die at the 3-nanometer node can be worth several hundred dollars in raw silicon cost alone. Packaging that die -- particularly in advanced packaging schemes like CoWoS or HBM stacking -- adds hundreds more. Shipping a defective die into a package wastes not only the die itself but the substrate, the interposer, the bonding materials, and the assembly labor. In chiplet architectures where multiple die are integrated into a single package, a single bad die can destroy an entire multi-chip module worth thousands of dollars. Wafer test exists to prevent this. It is the semiconductor industry's quality gate, and its importance grows with every node shrink and every increase in packaging complexity.

Japan dominates this gate. Tokyo Seimitsu, operating under its Accretech brand, holds forty-six percent of the global market for wafer probers -- the machines that physically position the wafer and bring the probe card into contact with the die. Advantest Corporation is the world's number one maker of automatic test equipment, the systems that generate and analyze the electrical test signals. Together with their supporting ecosystem of subsystem suppliers -- Aval Data for tester interface boards and NHK Spring for the precision springs inside probe cards -- these Japanese companies form a test infrastructure that every chipmaker on the planet depends on.

---

## The Physics and Engineering of Wafer Test

### What Happens at the Probe Station

A wafer prober is, at its core, a precision alignment and contact system. The wafer sits on a temperature-controlled chuck that can be heated or cooled to simulate the operating conditions the finished chip will encounter. Above the wafer hangs the probe card -- a complex printed circuit board studded with thousands of microscopic contact tips, arranged to match the pad layout of the die being tested. The prober must align the wafer to the probe card with accuracy better than one micron -- roughly one-fiftieth the width of a human hair -- and then bring them into contact with precisely controlled force: enough to make reliable electrical contact through any oxide layer on the pad surface, but not so much as to damage the delicate structures beneath.

Modern high-end probers achieve positioning accuracy of plus or minus 0.5 microns at temperatures ranging from minus forty degrees to over three hundred degrees Celsius. They can test multiple die simultaneously -- a technique called multi-die probing or parallel test -- by using probe cards with contact arrays covering four, eight, sixteen, or even thirty-two die at once. The throughput of a prober is measured in wafers per hour, and the economics of the test floor depend heavily on this metric. A prober that tests 25 wafers per hour instead of 20 reduces the cost of test per die by twenty percent, directly improving the fab's profitability.

The probe card itself is one of the most critical components in the system. Three major probe card architectures have evolved over the decades, each suited to different applications:

**Cantilever probe cards** use individually mounted wire probes that extend horizontally from a supporting ring and bend downward to contact the die pads. This was the original probe card architecture and remains common for lower pin-count devices and engineering characterization. Cantilever cards are relatively inexpensive to manufacture and easy to customize, but they struggle with the high pin counts and tight pitch requirements of modern processors and memory devices. The individual wires have significant inductance, which limits their ability to carry high-frequency signals, and the mechanical compliance of the cantilever structure makes it difficult to achieve uniform contact force across thousands of simultaneous contact points.

**Vertical probe cards** solve the pitch and parallelism problem by using spring-loaded pins arranged vertically -- perpendicular to the wafer surface. Each pin is a tiny spring-loaded mechanism, typically a few hundred microns in diameter, that compresses when it contacts the die pad and provides both electrical contact and mechanical compliance. Vertical probe cards can achieve much higher pin densities than cantilever cards and maintain more uniform contact force across large arrays, making them the standard for high-volume memory testing where thousands of pads must be contacted simultaneously. The springs inside these probe pins are one of the most demanding precision components in the semiconductor test ecosystem -- and this is where NHK Spring enters the picture, supplying the micro-springs that enable probe cards to make reliable contact with die pads spaced as little as thirty microns apart.

**MEMS probe cards** represent the leading edge of probe card technology. Instead of individual mechanical springs, MEMS probe cards use photolithographically fabricated contact structures -- essentially semiconductor manufacturing techniques applied to the probe card itself. This allows for even tighter pitch, more uniform contact characteristics, and better high-frequency signal integrity. Companies like FormFactor (the world's largest probe card maker) and MPI Corporation (a Taiwanese competitor to Tokyo Seimitsu in the prober market) have invested heavily in MEMS probe card technology. The transition to MEMS probe cards has been particularly important for the testing of advanced logic devices with pad pitches below forty microns and for the testing of high-bandwidth memory (HBM) die, where thousands of through-silicon-via (TSV) connections must be verified before stacking.

### Automatic Test Equipment: The Brain of the Test Cell

While the prober provides the mechanical interface between the test system and the wafer, the actual testing is performed by the automatic test equipment -- the ATE. An ATE system is, in essence, a massively parallel precision measurement instrument combined with a high-speed digital signal generator. It generates the input signals that stimulate the chip under test, captures the output responses, and determines whether those responses match the expected behavior defined in the test program.

ATE systems are divided into two broad categories:

**Parametric test** (also called wafer acceptance test or WAT) measures the fundamental electrical properties of the transistors and interconnects on the wafer: threshold voltage, leakage current, resistance, capacitance, and similar parameters. Parametric test is typically performed on special test structures placed in the scribe lanes between die -- the areas that will be destroyed when the wafer is diced. The results serve as a process control monitor: if parametric values drift outside acceptable ranges, the fab knows that something has changed in the manufacturing process and can take corrective action before entire lots of wafers are affected.

**Functional test** verifies that the actual circuits on the die operate correctly. For a logic device, this means applying patterns of input signals and checking that the outputs match expected values at the correct timing. For a memory device, this means writing data to every cell and reading it back, checking for stuck bits, coupling faults, and retention failures. For a mixed-signal device, this means generating precise analog waveforms and measuring the device's response in both the time and frequency domains.

The complexity of modern ATE systems is staggering. Testing an advanced AI accelerator with billions of transistors and thousands of I/O pins requires a test system with hundreds of parallel channels, each capable of generating and capturing signals at frequencies exceeding ten gigahertz. The test program -- the software that defines the sequence of tests to be applied -- can take months to develop and may represent millions of dollars in engineering investment. A single ATE system can cost between two and ten million dollars, and a high-volume test floor at a major chipmaker or outsourced semiconductor assembly and test (OSAT) facility may deploy dozens of them.

Advantest dominates this market. The company holds sixty to seventy percent of the global market for memory ATE and thirty-five to forty-five percent for SoC (system-on-chip) ATE. Its V93000 platform has become the de facto standard for advanced logic testing, deployed at TSMC, Samsung, Intel, and every major OSAT. Its T5500 series holds a comparable position in memory test. In a market where the alternative is Teradyne -- the American competitor that holds most of the remaining share -- Advantest and Teradyne together constitute an effective duopoly that controls over eighty percent of the global ATE market.

### The Wafer-Level Test Flow

The complete wafer-level test sequence typically proceeds as follows:

1. **Incoming wafer inspection** -- optical or e-beam inspection identifies visible defects and marks suspect die before any electrical contact is made.

2. **Parametric test (WAT)** -- test structures in the scribe lanes are probed to verify that process parameters are within specification. This is a sampling operation, not a full wafer test.

3. **Wafer probe / functional test** -- every die on the wafer is contacted and tested. Die are categorized as pass, fail, or marginal. Some die may be "repaired" if they contain redundant circuits (as is standard in memory devices, which include spare rows and columns that can be substituted for defective ones through laser fuse or electrical fuse programming).

4. **Ink / map** -- historically, failed die were physically marked with an ink dot. In modern practice, the test results are recorded electronically in a wafer map file, and the downstream dicing and pick-and-place equipment reads this map to skip failed die.

5. **Binning** -- passed die may be sorted into different performance grades (bins) based on their test results. A processor die that meets its highest speed specification goes into the top bin and is sold at a premium price. A die that passes all functional tests but only at a lower clock speed goes into a lower bin and is sold as a budget-grade product. This binning process -- sometimes called "speed sorting" or "yield grading" -- is a critical source of profitability for chipmakers, turning what would otherwise be waste into a tiered product portfolio.

### Known-Good Die: The Chiplet Imperative

The concept of the known-good die (KGD) has existed since the 1990s, when it was primarily relevant to multi-chip module (MCM) packaging. The idea is straightforward: before integrating a die into a package with other die, you must be certain -- not merely confident, but certain -- that it works. In a single-chip package, a defective die wastes only the packaging materials for that one chip. In a multi-die package, a defective die wastes all the other good die in the module as well.

The chiplet revolution has transformed KGD from a niche concern into one of the most critical challenges in semiconductor manufacturing. Consider NVIDIA's Blackwell B200 GPU, which integrates two compute die on a single interposer. If the yield of each individual die is ninety percent, the probability that both die in a package are good is only eighty-one percent -- meaning nearly one in five packages would be wasted if die were not tested before integration. For packages integrating four, eight, or twelve chiplets, the math becomes devastating. At ninety percent individual die yield, an eight-chiplet module has a composite yield of just forty-three percent without KGD screening.

High-bandwidth memory (HBM) presents an even more extreme case. An HBM4 stack integrates sixteen DRAM die vertically, connected through thousands of through-silicon vias. If even one die in the stack is defective, the entire stack fails. At ninety-five percent individual die yield, a sixteen-die stack has a composite yield of only forty-four percent. HBM manufacturers -- principally SK Hynix, Samsung, and Micron -- must therefore test each DRAM die to an extraordinarily high confidence level before stacking. The cost of the wafer test step is dwarfed by the cost of scrapping a partially assembled HBM stack.

This is the context in which the December 2025 announcement of a joint development partnership between Tokyo Seimitsu and Advantest must be understood. The two companies are co-developing a die-level prober system optimized for known-good-die verification of chiplets and HBM die. This system integrates Tokyo Seimitsu's precision wafer handling and alignment technology with Advantest's test signal generation and measurement capabilities, creating a unified test cell specifically designed for the chiplet era. The partnership is a strategic acknowledgment that the traditional separation between the prober (mechanical) and the tester (electrical) is breaking down as test requirements become more demanding. Die-level testing at speed -- meaning testing each die at its intended operating frequency and temperature before integration -- requires tighter coupling between the prober's thermal and mechanical systems and the tester's signal integrity, and neither company can achieve this alone.

### The Economics of Test

Semiconductor test is sometimes described as the "tax" on manufacturing -- an unavoidable cost that adds no features to the product but prevents the much larger cost of shipping defective parts. The economics of this trade-off are governed by a simple inequality:

**Cost of test per die < Expected cost of shipping a bad die**

The cost of test per die is determined by three factors: the capital cost of the test equipment (prober plus ATE, amortized over their useful life), the throughput of the test cell (wafers per hour, die per wafer), and the operating costs (electricity, maintenance, test program development, labor). For a high-volume memory product tested in parallel across thirty-two die at a time, the cost of test might be less than one cent per die. For a complex AI accelerator tested one die at a time with a test program lasting several seconds, the cost of test can exceed one dollar per die.

The cost of shipping a bad die depends on where the defect is caught. A die that fails at wafer probe costs only the raw silicon and processing -- perhaps one hundred to five hundred dollars per die at leading-edge nodes. A die that passes wafer test but fails after packaging costs the silicon plus the packaging materials and assembly labor -- potentially one thousand to three thousand dollars for an advanced package. A die that passes both wafer test and package test but fails in the customer's system costs everything above plus the cost of a product recall, customer downtime, and reputational damage. For automotive or aerospace applications, a field failure can result in safety incidents and liability claims measured in millions.

The semiconductor industry therefore invests heavily in test -- globally, the ATE market alone exceeds six billion dollars per year, and the total test equipment market (including probers, probe cards, handlers, and test interfaces) approaches ten billion dollars. As chip complexity increases and advanced packaging raises the stakes of escaping defects, the share of total manufacturing cost attributable to test is growing, not shrinking. This is the secular tailwind behind both Advantest's and Tokyo Seimitsu's growth trajectories.

---

## Company Profiles

### Tokyo Seimitsu / Accretech (7729.T) -- World Number One in Wafer Probers

**Founded:** 1949 | **HQ:** Hachioji, Tokyo | **Market Cap:** 561.8 billion yen

Tokyo Seimitsu -- known internationally by its brand name Accretech -- is a company that defies easy categorization. Its two business segments, Semiconductor Production Equipment (SPE, seventy-four percent of sales) and Metrology (twenty-six percent of sales), span wafer probers, dicing machines, CMP equipment, polish grinders, edge grinders, precision dicing blades, and coordinate measuring machines. But it is in wafer probing where the company has achieved true global dominance.

Accretech holds approximately forty-six percent of the global market for wafer probers -- making it the undisputed world leader, ahead of Tokyo Electron at approximately twenty-seven percent. The remaining market is fragmented among MPI Corporation of Taiwan (roughly ten percent), SEMICS and SEMES of Korea, and a growing set of Chinese domestic competitors including Sidea, Changchuan Technology, and NAURA. But Accretech's position at the top has been stable for years, built on decades of accumulated expertise in precision mechanics, thermal management, and alignment systems.

The company's prober lineup spans the full range of applications: from engineering probe stations used in device characterization to high-volume production probers capable of testing hundreds of wafers per day in fully automated operation. Accretech probers support wafer sizes from 150mm to 300mm, temperature ranges from minus sixty degrees to three hundred degrees Celsius, and probing configurations from single-die to full-wafer parallel test. The company's latest platforms incorporate AI-based alignment algorithms that can compensate for wafer warpage and thermal expansion in real time -- critical capabilities as die sizes grow and thermal requirements become more extreme.

What makes Tokyo Seimitsu particularly remarkable in the context of this book's supply chain analysis is its position as the most connected node in the entire 110-company graph. With sixty-five edges spanning supplier, competitor, and partner relationships across seven countries, Tokyo Seimitsu touches more companies than any other node in the dataset -- more than TSMC, more than Samsung, more than Tokyo Electron. This connectivity reflects the fundamental nature of the company's products: every fab, every foundry, every OSAT needs probers and dicers. Tokyo Seimitsu supplies probing, dicing, and CMP equipment to TSMC, Samsung, Intel, SK Hynix, Micron, and Kioxia -- the six largest chipmakers in the world. It supplies ASE Technology, Amkor, JCET, and Tongfu Microelectronics -- the four largest OSATs. It supplies foundries in China (SMIC, Hua Hong, Nexchip, CanSemi, GTA Semiconductor), Korea (DB HiTek), Taiwan (UMC, VSMC/Vanguard), and Singapore (GlobalFoundries). It supplies OSATs in Taiwan (KYEC, Chipbond, ChipMOS), Korea (HANA Micron, Nepes, SFA Semicon, LB Semicon), Singapore (UTAC), and Malaysia (Inari Amertron, Unisem, MPI/Carsem). Its client list reads like the complete directory of the global semiconductor back-end industry.

This breadth of customer relationships is both a strength and a vulnerability. It is a strength because it provides extraordinary revenue diversification -- no single customer dominates, and the loss of any one account would be painful but not existential. It is a vulnerability because it means Tokyo Seimitsu sells to customers in every geography, including China, where thirty-four percent of its revenue is generated. The company faces intensifying competition from Chinese domestic substitution efforts, particularly in CMP equipment (where Huahai Qingke has captured over fifty percent of the Chinese domestic market for twelve-inch wafer CMP) and increasingly in probing equipment (where Sidea holds approximately twenty-six percent of the Chinese domestic market). Korean localization through Samsung subsidiary SEMES and independent competitor SEMICS adds a second front of competitive pressure.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 21.3x |
| PBR | 2.35x |
| EPS | 111.78 yen |
| ROE | 15.3% |
| Revenue (FY2025/3) | 150.5 billion yen |
| Revenue Growth YoY | +11.8% |
| Operating Margin | 19.0% |
| Foreign Ownership | 50.06% |
| 52-Week Range | 6,148 -- 16,170 yen |
| Dividend Yield | 1.4% |

#### Investment Perspective

Tokyo Seimitsu ranks eighth in our evaluation framework with a final score of 61.0 out of 100, placing it among the top ten most compelling names in the dataset. The investment thesis centers on the company's dual leadership in semiconductor probers and precision coordinate measuring machines, combined with a valuation that trades at a meaningful discount to its equipment peer group.

At a PER of 21.3x, Tokyo Seimitsu trades at a thirty-two percent discount to the G1 semiconductor equipment peer median of 31.6x. This discount persists despite the company's global leadership in probing equipment (forty-six percent market share), eleven-point-eight percent revenue growth, and institutional-quality foreign ownership at fifty percent. The stock sits near its fifty-two-week high, signaling momentum, and analyst consensus is favorable with three buy ratings against zero holds and one sell.

The primary risk factor is China exposure. At thirty-four percent of revenue, the company's dependence on Chinese sales creates meaningful geopolitical risk -- both from potential export controls restricting sales to Chinese customers and from accelerating domestic substitution that could erode share in the Chinese market over the medium term. The CMP equipment category has already seen substantial Chinese domestic penetration, and probing is under increasing pressure. Dicing equipment, where blade quality and reliability remain harder to replicate, appears more defensible.

The catalyst case rests on the AI-driven capex cycle at TSMC, Samsung, and the major memory makers. As advanced packaging -- particularly HBM and chiplet architectures -- raises the criticality of known-good-die verification, demand for high-end probing equipment is accelerating. The joint die-level prober development with Advantest, announced in December 2025, positions Tokyo Seimitsu at the center of this transition. If the partnership produces a commercially successful product, it could expand Tokyo Seimitsu's addressable market from wafer-level probing into the higher-value die-level test segment.

---

### Advantest Corporation (6857.T) -- Number One Global Semiconductor Test Equipment Maker

**Founded:** 1954 | **HQ:** Nerima, Tokyo | **Market Cap:** 17.63 trillion yen

Advantest is to semiconductor test what ASML is to lithography -- the dominant platform provider whose equipment is essential to the operation of every significant chipmaker on earth. The company's automatic test equipment systems are deployed at Samsung, SK Hynix, Micron, and throughout the TSMC ecosystem. With sixty to seventy percent market share in memory ATE and thirty-five to forty-five percent in SoC ATE, Advantest and its American rival Teradyne together constitute a duopoly that collectively controls over eighty percent of the global ATE market.

The company's history traces back to 1954, when it was founded as Takeda Riken Industry Co., Ltd. -- a maker of electronic measuring instruments. Through decades of strategic evolution, the company transitioned from general-purpose test and measurement into semiconductor-specific ATE, a market that has grown dramatically with the complexity of integrated circuits. The company was renamed Advantest in 1985 and has since grown into a global operation with offices and service centers in Japan, the United States, Germany, Korea, Taiwan, China, Singapore, and Malaysia.

Advantest's current product portfolio centers on two flagship ATE platforms. The V93000 system, originally developed by its acquired subsidiary Verigy (previously the semiconductor test division of Agilent Technologies), is the industry standard for testing advanced logic, mixed-signal, and system-on-chip devices. The V93000's modular architecture allows customers to configure the system for a wide range of device types and pin counts, from smartphone application processors to the most complex AI accelerator die. The T5500 series occupies a comparable position in memory test, serving the high-volume DRAM and NAND flash testing requirements of Samsung, SK Hynix, and Micron.

The AI boom has been transformative for Advantest's business. As NVIDIA, AMD, and other AI chip designers push the boundaries of transistor count and I/O bandwidth, the complexity of testing each chip increases correspondingly. An AI accelerator with tens of billions of transistors and thousands of high-speed I/O pins requires more test time, more test channels, and more sophisticated test programs than any device in the history of the industry. Advantest's FY2026/3 guidance calls for net sales of 1.07 trillion yen -- making it only the second Japanese semiconductor equipment company (after Tokyo Electron) to exceed the one-trillion-yen revenue threshold -- with operating income of 454 billion yen, implying operating margins approaching forty percent.

The company's stock price performance reflects this momentum. Advantest reached an all-time high of 29,250 yen on January 29, 2026, driven by record quarterly results and continued strength in AI-related tester demand. At a current price of approximately 25,475 yen, the stock trades at a PER of 56.3x and a PBR of 30.4x -- premium multiples that reflect the market's recognition of Advantest's competitive position and growth trajectory. Foreign ownership stands at fifty percent, indicating deep institutional conviction.

In the supply chain graph, Advantest appears as a supplier to Samsung, SK Hynix, Micron, TSMC, and the major OSATs including ASE Technology and Amkor. The graph also records two inbound supplier edges: from Aval Data (tester boards and probes) and NHK Spring (probe card springs), reflecting the ecosystem of Japanese subsystem suppliers that feeds into Advantest's equipment. The partner edge with Tokyo Seimitsu -- the die-level prober joint development announced in December 2025 -- is one of only four formal partnership edges in the entire 321-edge graph, signaling its strategic significance.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 56.3x |
| PBR | 30.36x |
| EPS | 452.34 yen |
| ROE | 31.8% |
| Revenue Guidance (FY2026/3) | 1,070 billion yen |
| Revenue Growth YoY | +37.0% |
| Operating Margin | 39.4% |
| Foreign Ownership | 50.0% |
| 52-Week Range | 4,703 -- 29,250 yen |
| Dividend Yield | 0.21% |

Advantest's evaluation score of 52.2 reflects a profile common to high-quality growth companies: exceptionally strong competitive positioning (Dimension B: 22 out of 25) and financial quality (Dimension C: 15 out of 15), offset by a premium valuation (Dimension A: 1.2 out of 30) that leaves little margin of safety. The company scores maximally or near-maximally on market share, switching costs, technology differentiation, supply chain centrality, revenue growth, operating margin, and ROE. But at a PER of 56.3x -- nearly double the G1 equipment peer median of 31.6x -- the stock prices in much of its future growth already. For investors seeking value, Advantest is a superb company at a full price. For investors seeking quality regardless of valuation, it is arguably the single best franchise in the Japanese semiconductor equipment sector.

---

### Aval Data Corporation (6918.T) -- The Hidden Subsystem Supplier

**Founded:** 1980 | **HQ:** Machida, Tokyo | **Market Cap:** 26.3 billion yen

Aval Data occupies a position deep in the semiconductor supply chain's interior -- a company that most investors have never heard of, supplying critical subsystems to equipment makers that are themselves suppliers to the chipmakers. The company manufactures industrial electronics including image processing modules, tester interface boards, near-infrared camera systems for defect detection, and custom electronic assemblies for semiconductor equipment manufacturers.

Approximately eighty percent of Aval Data's revenue comes from contract manufacturing for semiconductor equipment companies. Its client list includes two confirmed major customers: Tokyo Electron (CMP-0004), the world's third-largest semiconductor equipment maker, and Nikon (CMP-0050), a leading lithography and inspection equipment manufacturer. The supply chain graph also records an edge from Aval Data to Advantest, with the label "tester boards/probes" -- indicating that Aval Data supplies the interface boards that connect Advantest's ATE systems to the device under test.

These tester interface boards -- sometimes called device interface boards (DIBs), load boards, or test socket boards -- are the custom-designed printed circuit assemblies that sit between the ATE's standardized pin electronics and the probe card or test socket. Each device type requires its own interface board, tailored to the specific pin configuration, signal routing requirements, and power delivery needs of the chip being tested. The interface board market is fragmented and largely invisible, but it is essential: without the right interface board, the most expensive ATE system in the world cannot test a single chip.

Aval Data's near-infrared camera technology deserves particular mention. Semiconductor manufacturers increasingly use infrared imaging to detect subsurface defects in silicon wafers and die -- defects that are invisible to conventional optical inspection. Aval Data's near-infrared cameras, based on Sony image sensors, are embedded in inspection systems used throughout the semiconductor production line.

The company's financial profile is striking for its apparent undervaluation. At a PER of 6.1x, Aval Data trades at an eighty percent discount to the G1 semiconductor equipment peer median of 31.6x. Its dividend yield of 6.08 percent is the highest among all companies in the dataset. A single analyst covers the stock with a buy rating and a target price of 5,304 yen -- nearly double the current price of 2,682 yen. The evaluation framework assigns Aval Data a score of 57.0 (raw composite 60.0, reduced by a confidence multiplier of 0.95 due to medium data coverage), with maximum marks in Dimension A (valuation discount) offset by lower scores in competitive positioning and growth quality, reflecting the company's small scale and limited product differentiation.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 6.1x |
| PBR | 1.24x |
| EPS | 243.15 yen |
| Revenue (Latest FY) | 10.4 billion yen |
| Dividend Yield | 6.08% |
| 52-Week Range | 1,666 -- 3,700 yen |
| Analyst Target | 5,304 yen (1 Buy) |

The investment case for Aval Data is, at its essence, a bet on the criticality of the test subsystem supply chain. As AI-driven demand increases the volume and complexity of semiconductor testing, the companies that supply the boards, probes, and imaging systems embedded in test equipment should benefit -- and Aval Data's extreme valuation discount suggests the market has not connected this company to the secular trend it participates in.

---

### NHK Spring Co., Ltd. (5991.T) -- Precision Springs for Probe Cards and Beyond

**Founded:** 1939 | **HQ:** Yokohama, Kanagawa | **Market Cap:** 634.5 billion yen

NHK Spring -- formally Nihon Hatsujo, known by the brand Nippatus -- is one of those companies whose true strategic significance is hidden beneath its mundane-sounding name. The company is Japan's largest spring manufacturer and one of the world's leading producers of precision mechanical components. Its two dominant positions -- fifty percent global market share in hard disk drive (HDD) suspension assemblies and a growing presence in semiconductor process components -- give it a unique dual exposure to the data storage and semiconductor manufacturing industries.

Founded in 1939, NHK Spring built its reputation on automotive suspension springs and industrial precision components before diversifying into electronic components in the 1970s and 1980s. The company's expertise in manufacturing micro-scale mechanical components with extremely tight tolerances -- springs measured in microns, suspension assemblies with nanometer-level flatness -- translated naturally into the semiconductor industry, where probe card springs, precision bonding fixtures, and etching/deposition chamber components require similar capabilities.

The probe card spring business, while not NHK Spring's largest revenue contributor, is strategically important because of what it enables. The vertical probe cards that dominate high-volume semiconductor testing depend on thousands of individually spring-loaded contact pins, each of which must provide consistent contact force, low electrical resistance, and reliable operation over millions of touchdowns. The springs inside these pins are typically made from beryllium copper or other specialized alloys, formed with tolerances measured in single microns, and must maintain their mechanical properties through temperature cycles ranging from cryogenic to over two hundred degrees Celsius. NHK Spring's decades of experience in precision spring manufacturing, combined with its expertise in surface treatment and metallurgical bonding, make it one of a handful of companies globally capable of producing these components at the required quality and volume.

The supply chain graph records a direct supplier edge from NHK Spring to Advantest with the label "probe card springs," confirming the company's role in the ATE ecosystem. The graph also records a supplier edge from NHK Spring to TSMC with the label "HDD suspension (50% share)" -- reflecting NHK Spring's role as a critical supplier to TSMC's data storage customers, though this relationship is relevant to the broader technology ecosystem rather than to wafer test specifically.

NHK Spring's semiconductor business is growing rapidly. The company has been expanding its portfolio of semiconductor process components, including precision parts for etching and deposition chambers, electrostatic chuck components, and bonding tools. This expansion leverages the same core competencies that underpin the probe card spring business -- precision metal forming, surface engineering, and tight-tolerance manufacturing -- while providing exposure to the faster-growing semiconductor equipment market.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 12.8x |
| PBR | 1.24x |
| EPS | 196.6 yen |
| ROE | 9.87% |
| Revenue (Latest FY) | 801.7 billion yen |
| Revenue Growth YoY | +4.53% |
| Dividend Yield | 2.24% |
| 52-Week Range | 1,298 -- 3,239 yen |

NHK Spring's evaluation score of 54.8 reflects a solid but unspectacular profile: moderate valuation discount (Dimension A: 20 out of 30), strong market share positioning (B1: 8 out of 8, reflecting the HDD suspension dominance), but modest growth and AI exposure scores. The company is not a pure-play semiconductor name -- its largest business remains automotive springs and components, and its HDD suspension business faces secular headwinds from the ongoing transition from hard disk drives to solid-state drives. But for investors seeking a diversified Japanese industrials company with a growing semiconductor component business, moderate valuation, and the technical moat of precision micro-mechanical manufacturing, NHK Spring offers an interesting profile at just 1.24 times book value.

---

## Competitive Landscape

The wafer test equipment market is structured as a set of overlapping duopolies and oligopolies, each operating at a different layer of the test ecosystem.

**Wafer probers** are led by Tokyo Seimitsu / Accretech at forty-six percent global share, followed by Tokyo Electron at twenty-seven percent. The third position is contested by MPI Corporation of Taiwan (approximately ten percent) and a rising group of Korean and Chinese competitors. SEMICS, a Korean company and Samsung supplier for fifteen years, holds the world's third-largest prober market share. SEMES, a Samsung subsidiary, competes primarily in captive Samsung applications. In China, Sidea (twenty-six percent domestic market share), Changchuan Technology (developing twelve-inch memory prober capabilities), and NAURA (the diversified Chinese semiconductor equipment platform) are all investing in prober technology as part of the broader domestic substitution initiative.

**Automatic test equipment** is a global duopoly between Advantest and Teradyne, with combined share exceeding eighty percent. Advantest leads in memory test (sixty to seventy percent) and Teradyne has historically been stronger in certain SoC test segments, but Advantest's V93000 platform has been gaining share in advanced logic test driven by AI demand. Chinese domestic ATE alternatives remain limited -- Huafeng Test (a listed Chinese company) has made progress in lower-end test applications, but the performance gap relative to Advantest and Teradyne in high-end test remains wide.

**Probe cards** represent a separate competitive layer. FormFactor (United States) is the global leader, followed by Japan Electronic Materials (JEM), Technoprobe (Italy), and MPI Corporation. NHK Spring competes not at the probe card level but at the component level -- supplying the springs and precision mechanical parts that go into probe cards made by others. This positions NHK Spring as a supplier to multiple probe card makers, giving it revenue regardless of which probe card company wins any particular design engagement.

**Tester interface boards** are a fragmented market where Aval Data competes with numerous smaller contract manufacturers, many of them Japanese. The barriers to entry are lower than in probers or ATE, but the customer qualification process and design complexity create meaningful switching costs for established suppliers.

The competitive dynamics between Tokyo Seimitsu and its prober competitors are worth examining in detail. In the established markets -- Taiwan, Korea, Japan, Singapore, Malaysia -- Tokyo Seimitsu's installed base and service infrastructure create significant switching costs. Probers are integrated into automated production lines with specific software interfaces, recipe libraries, and maintenance routines. Switching prober vendors means requalifying the entire test process for every product running on that prober -- a process that can take months and carries yield risk. This installed-base advantage is Tokyo Seimitsu's deepest moat.

In China, however, the dynamics are different. Government subsidies and procurement preferences are actively steering demand toward domestic suppliers. The Chinese prober market is the fastest growing in the world, driven by massive fab construction at SMIC, Hua Hong, Nexchip, CanSemi, GTA Semiconductor, YMTC, and CR Micro, among others. Tokyo Seimitsu still holds a strong position in this market -- thirty-four percent of its total revenue comes from China -- but its share is under pressure. The company must balance the short-term revenue opportunity of selling to Chinese customers against the long-term strategic risk of enabling domestic competitors through technology transfer and the medium-term regulatory risk of potential export control restrictions.

---

## Supply Chain Connections

The wafer test step sits at a critical junction in the semiconductor value chain, connecting the front-end manufacturing sequence described in Chapters 4 through 12 with the back-end packaging and assembly steps described in Chapters 14 and 15.

**Upstream connections:** Wafer test receives completed wafers from the fab after all front-end processing is finished. The quality of the incoming wafers -- determined by the lithography precision (Chapter 6), the deposition uniformity (Chapter 9), the etch selectivity (Chapter 10), and the CMP planarity (Chapter 11) -- directly affects the yield at probe. A fab that runs a tight process produces wafers with high yield at probe; a fab with process excursions sees the results immediately in higher probe failure rates. Wafer test is, in this sense, the ultimate scorecard for every upstream process step.

**Downstream connections:** Die that pass wafer test proceed to dicing (Chapter 14), where the wafer is separated into individual die. The wafer map generated during probe -- marking each die as pass, fail, or binned to a specific speed grade -- travels with the wafer to the dicing step and determines which die are picked up for packaging. In advanced packaging applications (Chapter 15), the known-good-die requirement creates an even tighter feedback loop: die must not merely pass a functional test but must pass at a confidence level sufficient to justify their integration into multi-die packages worth thousands of dollars each.

**Internal ecosystem connections:** The four companies profiled in this chapter form a vertical ecosystem within the test equipment supply chain. NHK Spring supplies probe card springs to probe card manufacturers, who supply probe cards to Tokyo Seimitsu's probers. Aval Data supplies tester interface boards to Advantest's ATE systems. Tokyo Seimitsu's probers and Advantest's testers are deployed together in test cells at fabs and OSATs worldwide. And as of December 2025, Tokyo Seimitsu and Advantest are formally partnered to co-develop the next generation of die-level test systems.

The graph also reveals the geographic breadth of this ecosystem's reach. Tokyo Seimitsu's thirty-five identified clients span seven countries: Japan (Kioxia), Taiwan (TSMC, UMC, VSMC, KYEC, Chipbond, ChipMOS, Powertech), Korea (Samsung, SK Hynix, DB HiTek, HANA Micron, Nepes, SFA Semicon, LB Semicon), China (SMIC, Hua Hong, JCET, Tongfu, Tianshui Huatian, Nexchip, CR Micro, YMTC, CanSemi, GTA), the United States (Intel, Micron), Singapore (GlobalFoundries, UTAC), and Malaysia (Inari Amertron, Unisem, MPI/Carsem). Advantest's coverage mirrors this global footprint. There is virtually no significant semiconductor manufacturing operation in the world that does not depend on Japanese test equipment.

---

## The Tokyo Seimitsu-Advantest Partnership: A Structural Shift

The partnership between Tokyo Seimitsu and Advantest, announced in December 2025, deserves deeper examination because it represents more than an incremental product development -- it is a structural shift in how the test equipment industry is organized.

Historically, the prober market and the ATE market have operated as separate industries with separate companies, separate sales channels, and separate customer relationships. The prober maker builds the mechanical platform. The ATE maker builds the electronic test system. The customer buys them separately and integrates them in the test cell. The probe card maker supplies the probe card as a third independent product. This decoupled architecture has worked well for decades because the mechanical and electrical requirements could be specified and optimized independently.

The chiplet era is breaking this model. Die-level testing for chiplet integration requires capabilities that span the traditional boundary between prober and tester. The prober must maintain sub-micron alignment and thermal control while the tester runs at-speed functional patterns at multi-gigahertz frequencies. Signal integrity from the tester's pin electronics through the interface board, through the probe card, through the contact tips, and into the die must be maintained at performance levels that were previously only achievable in final package test. The thermal environment must be controlled precisely because chiplet die will be tested at their intended operating temperature, which may be very different from room temperature.

No single company possesses all of these capabilities. Tokyo Seimitsu has the world's best wafer handling and alignment technology but limited expertise in high-speed digital signal generation. Advantest has the world's best ATE technology but limited expertise in precision mechanical positioning and thermal management. The joint development program brings these complementary capabilities together in a co-designed system that neither company could build alone.

In the supply chain graph, this partnership is recorded as a bidirectional partner edge -- one of only four formal partnership edges in the entire 321-edge dataset. The other three partnership edges represent similarly strategic collaborations. The rarity of the partnership classification underscores the significance of the Tokyo Seimitsu-Advantest collaboration: it is not a routine supplier relationship or a casual co-marketing agreement, but a joint technology development with potential to reshape the test equipment market.

For investors, the partnership has implications for both companies. For Tokyo Seimitsu, it opens a path into the higher-value die-level test segment, potentially expanding the company's addressable market beyond traditional wafer probing. For Advantest, it strengthens the mechanical front-end of its test cell, potentially allowing higher throughput and better yield in the known-good-die verification flow. For the industry, it could accelerate the adoption of chiplet architectures by improving the economics of die-level test -- removing one of the key bottlenecks that currently constrains chiplet yield and cost.

---

## Key Takeaways

- **Wafer test is the semiconductor industry's quality gate.** Every die on every wafer must be electrically verified before dicing and packaging. The cost of skipping this step -- shipping defective die into expensive advanced packages -- far exceeds the cost of the test itself. This economic imperative is permanent and grows with packaging complexity.

- **Tokyo Seimitsu is the most connected node in the supply chain graph.** With sixty-five edges spanning seven countries, Tokyo Seimitsu's probers and dicers reach every major chipmaker and OSAT on the planet. Its forty-six percent global prober market share and position at the center of the semiconductor back-end make it one of the most strategically important companies in the dataset -- and at a PER of 21.3x, it trades at a meaningful discount to its equipment peers.

- **Advantest is the ASML of semiconductor test.** Its sixty-to-seventy percent share of memory ATE and thirty-five-to-forty-five percent share of SoC ATE, combined with thirty-seven percent revenue growth and nearly forty percent operating margins, justify its premium valuation. The AI boom is a structural tailwind: as chip complexity increases, test complexity and test time increase correspondingly, driving demand for more and better ATE.

- **The chiplet era transforms test economics.** Known-good-die verification is no longer optional -- it is mathematically necessary when multiple die are integrated into a single package. The December 2025 Tokyo Seimitsu-Advantest joint development of a die-level prober is a strategic response to this shift, combining the world's best wafer handling with the world's best test electronics in a co-designed system.

- **The Japanese test ecosystem extends from springs to systems.** NHK Spring's micro-springs enable the probe cards that contact the die. Aval Data's interface boards connect the ATE to the probe card. Tokyo Seimitsu's probers position the wafer with sub-micron accuracy. Advantest's testers generate and analyze the signals. This vertical stack of Japanese capabilities -- from component to subsystem to system -- creates an ecosystem that is difficult to replicate and expensive to replace.

---

*Data sources: CMP-0001 (Tokyo Seimitsu / Accretech), CMP-0005 (Advantest Corporation), CMP-0054 (Aval Data Corporation), CMP-0055 (NHK Spring Co., Ltd.), graph.json (321 edges, 110 nodes), evaluation_progress.json (scoring and investment theses)*
