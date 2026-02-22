# Chapter 14: Dicing & Singulation

> After hundreds of fabrication steps costing billions of dollars, every chip on a wafer must be individually separated with micrometer precision -- and two Japanese companies control ninety percent of the equipment that performs this task.

## Introduction

A finished semiconductor wafer is a marvel of engineering. It may contain thousands of individual die -- each one a processor, memory chip, sensor, or power device -- arrayed in a perfect grid across a disc of silicon three hundred millimeters in diameter and less than a millimeter thick. Hundreds of process steps, weeks of fabrication time, and materials sourced from dozens of suppliers across the globe have conspired to produce this single object. Its value, depending on the complexity of the circuits it carries, can range from a few thousand dollars to well over fifty thousand dollars.

But a wafer is not a product. No one buys a wafer. Customers buy individual chips -- discrete pieces of silicon that can be mounted on substrates, wired to packages, and soldered onto circuit boards. To get from wafer to chip, every die on that wafer must be physically separated from its neighbors in a process called dicing, or singulation. This is the first major step in back-end manufacturing, and it is the bridge between the pristine world of the front-end fab and the high-volume reality of semiconductor packaging and assembly.

Dicing sounds simple. In essence, it is cutting. But the tolerances involved transform what might seem like a mundane mechanical operation into one of the most demanding precision processes in the entire supply chain. A dicing blade is typically thirty to fifty micrometers wide -- thinner than a human hair -- and must cut through silicon, low-k dielectric layers, copper interconnects, and sometimes compound semiconductor materials without chipping the die edges, without cracking the ultra-thin wafer, and without deviating from its programmed path by more than a few micrometers over a cut length of three hundred millimeters. If the blade wanders, if it chips the die edge, if it generates excessive heat or mechanical stress, the chip it is separating can be rendered defective -- wiping out the entire investment in front-end processing for that die.

The stakes are not academic. In a modern fab producing advanced logic chips, a single wafer may carry five hundred to a thousand die, each worth anywhere from fifty to several hundred dollars at the die level. A dicing defect that destroys even a few percent of the die on every wafer represents millions of dollars in lost yield over the course of a year. In the chiplet era -- where multiple small die are combined into a single package -- the problem compounds further. More dies per wafer means more cuts. Thinner die means less mechanical tolerance for error. Tighter spacing between die means narrower streets and thinner blades. Every trend in advanced semiconductor manufacturing makes dicing harder, not easier.

Two Japanese companies dominate this critical process step. DISCO Corporation, headquartered in Ota-ku, Tokyo, commands over seventy percent of the global market for dicing saws and a similarly dominant position in wafer grinding equipment. Tokyo Seimitsu (trading under the brand name ACCRETECH), based in Hachioji, Tokyo, holds approximately ten percent of the dicing market -- the number two position globally. Together, they account for roughly ninety percent of all precision dicing equipment sold worldwide. This chapter explains the physics of how wafers are diced, the technology evolution from blade cutting to laser processing, the competitive dynamics between these two Japanese champions, and the emerging threats from Korea and China that could -- or could not -- challenge their dominance.

---

## The Physics of Dicing

### Blade Dicing: The Workhorse

The most widely used dicing method today is blade dicing, a technique that has been refined over four decades to an extraordinary degree of precision. The principle is straightforward: a thin circular blade embedded with diamond abrasive particles rotates at high speed -- typically thirty thousand to sixty thousand revolutions per minute -- and cuts through the wafer along the scribe lines (called "streets") that separate individual die.

The blade itself is a marvel of materials engineering. It consists of a metal or resin bond matrix in which synthetic diamond grains of precisely controlled size are distributed. Blade widths range from as thin as fifteen micrometers for advanced applications to around fifty micrometers for standard cuts. The choice of blade depends on the material being cut, the thickness of the wafer, the acceptable kerf width (the amount of material removed by the cut), and the chipping tolerance for the die.

Kerf width is a critical economic parameter. Every micrometer of kerf represents silicon that is destroyed during the cutting process -- silicon that cannot become a functioning die. On a standard three-hundred-millimeter wafer with die arrayed in a grid, the streets between die are typically fifty to eighty micrometers wide. A blade that cuts a thirty-micrometer kerf leaves some margin on each side for alignment tolerance and edge chipping. But if the kerf can be reduced -- or if the blade can cut more precisely with less chipping -- more die can be packed onto each wafer, or the streets can be made narrower, allowing either more die per wafer or larger die at the same wafer size. In high-volume manufacturing, even a five-micrometer improvement in kerf control can translate to meaningful yield improvements across millions of wafers per year.

Chipping is the primary quality concern in blade dicing. As the diamond-embedded blade cuts through the wafer, it generates mechanical stress at the die edges. If that stress exceeds the fracture toughness of the silicon (or, more critically, of the low-k dielectric films stacked on top of it), small chips will break away from the die edge. These chips -- measured in micrometers -- can propagate as cracks into the active circuit area, causing electrical failures that may not manifest until the chip is packaged and tested, or worse, until it has been deployed in the field. Front-side chipping (on the circuit-bearing surface) is particularly dangerous because it can damage interconnect layers and passivation films. Back-side chipping is more tolerable but still constrained by packaging requirements.

The management of chipping drives much of the engineering in blade dicing systems. Spindle design, blade composition, cutting speed, feed rate, cooling water flow, and blade dressing schedules are all optimized to minimize edge damage. DISCO's decades of accumulated process data -- covering hundreds of thousands of cutting recipes across virtually every semiconductor material -- is one of the foundations of its market dominance. A new entrant can build a dicing saw, but replicating the recipe library that tells the machine exactly how to cut a specific wafer type with a specific blade at specific parameters is an entirely different challenge.

### Laser Dicing: Precision Without Contact

Laser dicing emerged as an alternative to blade dicing in the early 2000s, driven by the need to process wafers that were too thin, too fragile, or composed of materials too difficult for mechanical blades to handle reliably.

There are two fundamentally different approaches to laser dicing, and the distinction matters enormously.

**Ablation dicing** uses a high-energy laser beam to vaporize material along the scribe line, physically removing silicon and dielectric layers to create a separation groove. This is conceptually similar to blade dicing -- material is removed to create a kerf -- but the removal mechanism is thermal rather than mechanical. Ablation dicing avoids the mechanical stress of a spinning blade, which is advantageous for thin wafers and brittle materials such as gallium arsenide or silicon carbide. However, it introduces its own problems: the laser generates a heat-affected zone (HAZ) around the cut, which can cause thermal damage to adjacent circuits. Debris from the vaporized material (called "recast" or "splatter") must be managed carefully to prevent contamination of the die surface. And ablation dicing is generally slower than blade dicing for thick silicon wafers, making it less economical for standard applications.

**Stealth dicing** is a fundamentally different technology. Rather than removing material from the wafer surface, stealth dicing uses a laser focused inside the silicon wafer to create a line of internal modifications -- microscopic damage zones within the bulk silicon -- without affecting the wafer surface at all. The laser passes through the top surface of the silicon (which is transparent to the laser's wavelength) and focuses at a controlled depth inside the wafer, where the energy density is sufficient to create a modified layer. After the laser has scribed all the internal modification lines, the wafer is expanded on a stretching frame or tape, and the die separate along the modified lines -- much like snapping a piece of glass along a scored line.

Stealth dicing has several remarkable advantages. Because no material is removed, there is effectively zero kerf loss -- the street width can be reduced to near zero, enabling more die per wafer. There is no chipping, because no mechanical force is applied to the die edges. There is no heat-affected zone on the surface, because the laser energy is delivered internally. And the die edges produced by stealth dicing are exceptionally clean and strong, which improves die strength -- an increasingly important parameter for ultra-thin die used in stacked packages.

The technology was pioneered by Hamamatsu Photonics in Japan and commercialized by DISCO, which licenses the technology and integrates it into its dicing platforms. EO Technics, a Korean company discussed later in this chapter, has independently developed competitive laser stealth dicing technology and is gaining traction, particularly for High Bandwidth Memory (HBM) stacking applications at Samsung and SK Hynix.

### Dicing Before Grinding (DBG)

As advanced packaging demands ever-thinner die -- fifty micrometers or less for memory stacking, and as thin as twenty micrometers for certain applications -- a process innovation called Dicing Before Grinding (DBG) has become essential.

In the conventional process flow, the wafer is first ground (thinned) from the backside to the target thickness, then diced. But ultra-thin wafers are extremely fragile and prone to breakage during dicing. DBG reverses the sequence: the wafer is partially diced from the front side (cutting grooves to a depth slightly greater than the final target thickness) while the wafer is still at its original, mechanically robust thickness. The wafer is then flipped and ground from the backside until the grinding reaches the bottom of the dicing grooves, at which point the die naturally separate.

DBG eliminates the need to dice an ultra-thin wafer, dramatically reducing breakage and chipping risks. It is widely used in NAND flash memory production (where die are stacked eight, sixteen, or even sixty-four layers high in a single package), in DRAM production for HBM (which requires stacking four to sixteen die with through-silicon vias), and increasingly in advanced logic packaging where chiplets demand thin die for thermal and electrical performance.

Both DISCO and Tokyo Seimitsu offer integrated DBG-capable platforms that combine dicing and grinding in a single tool or in tightly coupled tool sets. The integration of these two process steps -- dicing and grinding -- is one of the reasons the same companies dominate both markets.

### Tape Mounting and Die Pick-Up

Before dicing begins, the wafer is mounted on a dicing tape -- a UV-sensitive adhesive film stretched over a rigid frame. The tape holds the individual die in place during and after the cutting process, preventing them from scattering. After dicing, the tape is exposed to ultraviolet light, which weakens its adhesive properties, allowing individual die to be picked up by a vacuum collet and placed onto a substrate or package.

The quality of the tape mount, the uniformity of the adhesive, and the precision of the die pick-up process all affect yield. A die that is slightly tilted on the tape may be picked up at an angle, causing placement errors in the packaging step. A die that was not fully separated during dicing may resist pick-up, requiring mechanical force that risks cracking. These downstream effects mean that dicing quality -- chipping, edge straightness, and die separation completeness -- directly determines the yield of the entire packaging line.

This is the essential point that non-specialists often miss: dicing is not merely a cutting operation. It is the process that determines whether the front-end's investment in each die can be successfully converted into a packaged, testable, shippable product. A fab with a ninety-five percent front-end yield but a three percent dicing loss is effectively operating at a ninety-two percent overall yield. In high-volume manufacturing, that difference represents hundreds of millions of yen in lost revenue annually.

---

## Why Dicing Matters More in the Chiplet Era

The semiconductor industry's transition toward chiplet-based architectures amplifies every challenge in dicing technology.

In the traditional monolithic approach, a single large die contains all of a chip's functionality. In the chiplet approach -- championed by AMD, Intel, and increasingly adopted for AI accelerators -- that functionality is distributed across multiple smaller die (chiplets) that are assembled into a single package using advanced packaging technologies such as TSMC's CoWoS or Intel's EMIB.

This shift has three direct consequences for dicing.

**More dies per wafer, more cuts per wafer.** A chiplet design that replaces one large die with four smaller chiplets quadruples the number of die on the wafer (approximately -- yield effects vary). Each additional die requires additional dicing cuts. The total length of dicing cuts per wafer increases proportionally, raising throughput demands on dicing equipment and amplifying the impact of any per-cut defect rate.

**Thinner die for stacking.** Many chiplet architectures involve vertical stacking -- HBM memory stacks, logic-on-logic stacks, or hybrid bonding of logic and memory chiplets. Stacking requires thin die, often fifty micrometers or below. Thinner die are more susceptible to chipping and cracking during dicing, driving demand for stealth dicing and DBG processes.

**Tighter tolerances for heterogeneous integration.** When chiplets from different process nodes and different fabs are assembled into a single package, the dimensional tolerances on each chiplet must be extremely tight. Die edge straightness, die size uniformity, and surface cleanliness after dicing all affect the alignment accuracy and bonding quality of the subsequent packaging step. A chip that was perfectly functional after front-end processing can be rendered useless by a dicing defect that prevents proper alignment in a CoWoS interposer assembly.

The chiplet transition, in short, makes precision dicing more critical, more technically demanding, and more valuable. It is a secular tailwind for the companies that dominate this process step.

---

## DISCO Corporation (6146.T) -- The Undisputed Leader in Precision Dicing

**Founded:** 1937 | **HQ:** Ota-ku, Tokyo | **Market Cap:** 8.0 trillion yen

DISCO Corporation is one of the most remarkable niche monopolists in the global semiconductor equipment industry. Founded in 1937 as Dai-Ichi Seitosho (First Grinding Company), DISCO began as a manufacturer of grinding wheels and abrasive products. Over nine decades, it evolved into the world's dominant supplier of precision cutting, grinding, and polishing equipment for semiconductor manufacturing. The name "DISCO" is not an acronym or a reference to music -- it derives from the company's original Japanese name and was adopted as the official corporate brand in 1977.

DISCO's core product lines span three categories: dicing saws (which cut wafers into individual die), grinders (which thin wafers from the backside), and polishers (which create ultra-smooth surfaces). In dicing saws specifically, DISCO commands a market share estimated at seventy to eighty percent globally -- a dominance that has persisted essentially unchallenged for decades. In wafer grinders, its share is similarly commanding. When dicing and grinding are considered together, DISCO is not merely the market leader; it is the market.

### The DISCO Business Model

What distinguishes DISCO from many equipment companies is the dual nature of its revenue. Equipment sales -- dicing saws, grinders, polishers -- represent a significant portion of revenue, but consumables and services provide a recurring, high-margin revenue stream that smooths cyclicality. Diamond blades wear out and must be replaced regularly. Grinding wheels degrade with use. Dicing tape, flanges, nozzles, and other accessories require periodic replenishment. Every dicing saw DISCO installs becomes a long-term revenue generator through its consumable ecosystem.

This installed-base leverage is reflected in DISCO's extraordinary profitability. The company reported an operating margin of 41.38 percent -- a figure that would be exceptional for any industrial company and is nearly triple the semiconductor equipment peer group median of 14.9 percent. DISCO's operating margin is not a cyclical peak; it has been consistently above thirty percent for years, reflecting the pricing power that accompanies a near-monopoly in an essential process step with high switching costs.

The switching costs are real and substantial. A semiconductor fab that uses DISCO dicing saws has optimized its entire back-end process around DISCO's equipment, DISCO's blades, DISCO's process recipes, and DISCO's service support infrastructure. Switching to an alternative supplier would require requalification of the dicing process for every product running in the fab -- a process that can take six to twelve months per product and involves significant risk of yield disruption during the transition. Fabs do not change dicing equipment suppliers casually.

### Technology and Innovation

DISCO's technology portfolio extends well beyond conventional blade dicing. The company offers laser dicing systems (both ablation and stealth dicing configurations), plasma dicing, and integrated DBG platforms. Its KABRA (Kerf-less Ablation and BreakAlong for Realizing Autonomy) process is a proprietary approach to laser-based singulation for thin wafers. DISCO has invested heavily in automation, developing fully automated production lines that integrate dicing, grinding, cleaning, and inspection into seamless process flows.

The company's approach to innovation is methodical and customer-driven. DISCO maintains dedicated process development centers where it works with customers to optimize dicing and grinding parameters for new materials and device structures. As semiconductor materials diversify -- silicon carbide for power devices, gallium nitride for RF applications, glass substrates for advanced packaging -- DISCO develops new blade compositions, new laser processes, and new equipment configurations for each material. This continuous expansion of the application space is a structural growth driver that extends beyond the traditional silicon wafer dicing market.

### Financial Profile

DISCO's financial characteristics are those of a franchise business operating at the peak of its competitive position.

**Key Financials:**

| Metric | Value |
|--------|-------|
| Market Cap | 8.0 trillion yen |
| PER | 51.18x |
| PBR | 8.97x |
| EPS | 1,206.5 yen |
| ROE | 26.5% |
| Revenue Growth (YoY) | 12.64% |
| Operating Margin | 41.38% |
| Dividend Yield | 0.57% |
| Foreign Ownership | 45.0% |
| Latest Price | 74,070 yen |
| 52-Week Range | 22,640 - 76,890 yen |

The most striking feature of this profile is the combination of dominant market share, extreme profitability, and premium valuation. DISCO trades at 51.2x earnings -- a massive premium to the semiconductor equipment peer group median PER of 31.6x. Its PBR of 8.97x is similarly elevated against a peer median of 2.49x. This premium valuation is why DISCO scores just 46.2 in the IndustryMap evaluation framework, despite its extraordinary business quality: the framework's Dimension A (valuation attractiveness) penalizes stocks that trade far above peer medians, and DISCO scores just 1.2 out of a possible 30 points on valuation. In other words, the market fully recognizes DISCO's dominance and has priced it in -- and then some.

This is a critical insight for investors evaluating the dicing equipment space. DISCO is arguably the highest-quality niche franchise in the Japanese semiconductor ecosystem. Its moat is as wide as any company in this book. But at 51x earnings, the stock offers limited margin of safety. The evaluation framework assigns DISCO 18 out of 20 on Dimension B (competitive position) -- one of the highest scores in the entire dataset -- and 13 out of 15 on Dimension C (growth and profitability). It is the valuation dimension that drags the overall score down. DISCO is a great business that trades at a price reflecting its greatness.

The stock's 52-week range tells a volatile story: from a low of 22,640 yen to a high of 76,890 yen, representing a range of over 240 percent from trough to peak. This volatility reflects both the cyclicality of semiconductor equipment spending and the high expectations embedded in the valuation. At 74,070 yen, the stock sits near its 52-week high, consistent with the strong cycle dynamics of 2025-2026.

Foreign ownership at 45 percent confirms that global institutional investors are well aware of DISCO. Twelve out of fifteen analysts rate the stock a Buy, with an average price target of 63,711 yen -- notably below the current trading price of 74,070 yen, suggesting the stock may be running ahead of consensus expectations.

---

## Tokyo Seimitsu Co., Ltd. (7729.T) -- The Scrappy Number Two

**Founded:** 1949 | **HQ:** Hachioji, Tokyo | **Market Cap:** 561.8 billion yen

If DISCO is the undisputed monarch of dicing, Tokyo Seimitsu -- trading under the brand name ACCRETECH -- is the resourceful challenger that has carved out its own substantial position by refusing to compete on DISCO's terms alone.

Tokyo Seimitsu was founded in 1949 as a manufacturer of precision measuring instruments, and metrology remains a core business to this day. The company operates in two segments: Semiconductor Production Equipment (SPE), which accounts for 74 percent of revenue, and Metrology, which accounts for the remaining 26 percent. Within the SPE segment, Tokyo Seimitsu's product range is notably broader than DISCO's: it encompasses wafer probing machines (where it is world number one with a 46 percent global share), dicing machines (approximately ten percent global share), CMP equipment, polish grinders, and edge grinders.

This breadth is both a strategic strength and a competitive constraint. In dicing alone, Tokyo Seimitsu cannot match DISCO's scale, installed base, or recipe library. But Tokyo Seimitsu can offer customers an integrated back-end equipment portfolio -- probing, dicing, grinding, and CMP -- from a single vendor with a unified service infrastructure. For smaller fabs, OSATs, and foundries that lack the resources to manage multiple equipment vendors for each back-end step, this integration has genuine value.

### The Prober Franchise

Tokyo Seimitsu's probing business, covered in detail in Chapter 13, deserves mention here because it is the primary economic engine that funds the company's competitive position in dicing. As the world's number one prober manufacturer -- ahead of Tokyo Electron and MPI Corporation of Taiwan -- Tokyo Seimitsu generates the revenue base and customer relationships that sustain its dicing business. Many customers who buy Tokyo Seimitsu probers also purchase its dicing equipment, creating a portfolio effect that neither DISCO (which does not make probers) nor specialized prober companies (which do not make dicers) can replicate.

### Dicing Technology

In dicing technology specifically, Tokyo Seimitsu offers a range of blade dicing saws, laser dicing systems, and integrated DBG solutions. Its dicing saws serve a broad customer base that spans foundries, memory manufacturers, OSATs, and IDMs across Asia, Europe, and North America. The company's dicing equipment is well-regarded for reliability and is competitively priced against DISCO's offerings, though it does not match DISCO's absolute cutting-edge performance in the most demanding applications.

Tokyo Seimitsu's client list in the IndustryMap database reflects its global reach. The company supplies dicing, probing, and/or CMP equipment to TSMC, Samsung, Intel, SK Hynix, Micron, Kioxia, ASE Technology (the world's largest OSAT), Amkor (number two), JCET (China's largest OSAT), SMIC, Tongfu Microelectronics, Tianshui Huatian, Powertech Technology, DB HiTek, HANA Micron, Nepes, SFA Semicon, LB Semicon, Nexchip, CR Micro, YMTC, CanSemi, GTA Semiconductor, KYEC, UMC, VSMC/Vanguard, Chipbond, ChipMOS, GlobalFoundries, UTAC, Inari Amertron, Unisem, and MPI Malaysia/Carsem. The database identifies thirty-five distinct client relationships across seven countries -- one of the broadest customer bases of any equipment company in this book.

### Financial Profile

Tokyo Seimitsu's financial profile is that of a solid, diversified equipment company trading at a meaningful discount to its pure-play peers.

**Key Financials:**

| Metric | Value |
|--------|-------|
| Market Cap | 561.8 billion yen |
| PER | 21.26x |
| PBR | 2.35x |
| EPS | 111.78 yen |
| ROE | 15.3% |
| Revenue (FY2025/3) | 150.5 billion yen |
| Revenue Growth (YoY) | 11.8% |
| Operating Margin | 19.0% |
| Dividend Yield | 1.4% |
| Foreign Ownership | 50.06% |
| Latest Price | 15,820 yen |
| 52-Week Range | 6,148 - 16,170 yen |
| China Revenue (est.) | 34% |

The contrast with DISCO is instructive. Tokyo Seimitsu trades at 21.3x earnings versus DISCO's 51.2x -- a 58 percent discount. Its PBR of 2.35x is just slightly below the equipment peer group median of 2.49x, compared to DISCO's 8.97x. Yet Tokyo Seimitsu is growing revenue at 11.8 percent, generates a respectable 19 percent operating margin (above the peer median of 14.9 percent), and earns a 15.3 percent ROE.

The valuation discount largely explains why Tokyo Seimitsu scores 61.0 in the IndustryMap evaluation framework -- significantly higher than DISCO's 46.2, despite DISCO's objectively superior competitive position. Tokyo Seimitsu scores 20.0 out of 30 on Dimension A (valuation), compared to DISCO's 1.2. The framework is designed to identify undervaluation relative to quality, and Tokyo Seimitsu's valuation metrics signal room for upward rerating that DISCO's do not.

### Investment Perspective

Tokyo Seimitsu occupies dual leadership positions: semiconductor probers (world number one with a 46 percent global share) and precision coordinate measuring machines (metrology). At a PER of 21.3x versus the equipment peer group median of 31.6x, the stock trades at a meaningful discount despite 11.8 percent revenue growth and 50 percent foreign ownership -- the latter indicating strong institutional recognition of the company's quality.

The stock has staged a dramatic recovery, trading at 15,820 yen against a 52-week low of 6,148 yen -- more than a 150 percent gain from the trough. It sits near its 52-week high of 16,170 yen, suggesting momentum.

The primary risk is China exposure. With an estimated 34 percent of revenue derived from Chinese customers, Tokyo Seimitsu is more exposed to geopolitical disruption and export control tightening than most Japanese equipment peers. Chinese domestic substitution efforts (discussed below) also represent a longer-term structural threat, particularly in CMP equipment where Chinese competitors have already captured over 50 percent of the domestic market. Dicing, however, remains more defensible -- the precision requirements and qualification barriers have so far limited Chinese alternatives to lower-end applications.

The catalyst is AI-driven capital expenditure at TSMC, Samsung, and the major memory makers. The December 2025 announcement of a joint die-level prober development program with Advantest (CMP-0005) signals that Tokyo Seimitsu is positioning itself at the frontier of known-good-die testing for chiplet architectures -- a high-growth adjacency.

---

## Competitive Landscape

### The Japanese Duopoly

The competitive dynamic between DISCO and Tokyo Seimitsu is best understood as a natural duopoly with asymmetric market shares. DISCO commands roughly seventy to eighty percent of the global dicing equipment market; Tokyo Seimitsu holds approximately ten percent. Together, they account for roughly ninety percent of global dicing equipment sales. The remaining ten percent is fragmented among several smaller players, primarily in China, Korea, and Israel.

This is not a contested duopoly in which two rivals of similar size battle for share. DISCO is the clear incumbent, the default choice, the safe option for any fab or OSAT procuring dicing equipment. Tokyo Seimitsu competes primarily by offering a broader product portfolio, competitive pricing, and the convenience of a single vendor for multiple back-end process steps. In the most demanding applications -- leading-edge logic dicing with sub-thirty-micrometer kerfs, advanced DBG processes for HBM memory -- DISCO's technology and recipe library give it an advantage that Tokyo Seimitsu struggles to match. In standard applications, Tokyo Seimitsu's offerings are fully competitive, and its pricing often undercuts DISCO's premium.

The duopoly is sustained by the same barriers that protect both companies: the extreme precision required in dicing equipment (sub-micrometer spindle runout, nanometer-level alignment), the long qualification cycles at customer sites (six to twelve months), the deep application knowledge embedded in decades of process data, and the global service infrastructure required to support equipment installed in fabs across Asia, the Americas, and Europe. These barriers are structural and reinforcing -- the longer a company has been the incumbent, the more process data it accumulates, and the harder it is for a challenger to replicate its capabilities.

### Emerging Competition: EO Technics (Korea)

EO Technics Co., Ltd. (CMP-0099, ticker 039030.KQ) represents the most technologically significant challenge to the DISCO-Tokyo Seimitsu duopoly. Based in South Korea, EO Technics is a laser technology specialist that has successfully localized laser stealth dicing technology -- a process in which it directly competes with DISCO's own laser dicing offerings.

EO Technics' position is notable for several reasons. First, its technology addresses the fastest-growing segment of the dicing market: thin-wafer processing for stacked die applications, particularly HBM. SK Hynix, the world leader in HBM production, uses EO Technics' laser stealth dicing equipment for its HBM stacking process. Samsung, the other major Korean memory maker, is also a confirmed customer for laser dicing, marking, and annealing equipment. As HBM production scales to meet AI datacenter demand -- SK Hynix's HBM3E is the de facto standard for NVIDIA's AI GPUs -- EO Technics rides a powerful demand wave.

Second, EO Technics benefits from Korean semiconductor industry policy. Both Samsung and SK Hynix have strategic incentives to develop domestic equipment suppliers, reducing dependence on Japanese companies amid periodic geopolitical tensions. Korea's semiconductor equipment localization drive, though less aggressive than China's, provides EO Technics with preferential access to customer roadmaps and joint development opportunities.

EO Technics' financial trajectory reflects this momentum. The company forecasts record revenue of 480 billion Korean won for fiscal year 2026, with operating profit growth of over 187 percent year-over-year. Its stock has surged from a 52-week low of 120,600 won to a high of 380,000 won.

However, EO Technics' competitive scope should not be overstated. Laser stealth dicing is not a universal replacement for blade dicing. Blade dicing remains the dominant technology for standard-thickness wafers, compound semiconductors, and many packaging applications where cost per cut matters more than zero-kerf capability. EO Technics does not manufacture dicing saws and has no position in blade dicing. It competes in the laser dicing segment, where it is strong but where DISCO also has capable offerings. The relevant market share to watch is not EO Technics versus DISCO in total dicing, but EO Technics versus DISCO in laser dicing for thin-wafer applications -- a narrower contest where EO Technics is genuinely competitive.

### Emerging Competition: Guangli Technology / ADT (China/Israel)

Henan Guangli Technology Co., Ltd. (CMP-0074, ticker 300480.SZ) is a Chinese company that entered the semiconductor dicing market through its 2019 acquisition of Advanced Dicing Technologies (ADT), an Israeli company that is the world's third-largest dicing saw manufacturer.

Guangli's trajectory is unusual. The parent company was founded in 1994 as a manufacturer of coal mine safety monitoring equipment -- about as far from semiconductor precision as one can imagine. Its entry into semiconductor dicing was entirely acquisition-driven, leveraging ADT's established technology and customer base. ADT's dicing equipment achieves 0.1-micrometer precision control and the company is one of only two in the world (alongside DISCO) that manufactures both dicing saws and high-precision air-bearing spindles in-house -- a critical precision component.

Despite these capabilities, Guangli/ADT's global market share in dicing remains in the single digits. The Chinese domestic dicing market, where Guangli has the strongest position, is still approximately five percent of the global total -- reflecting both the early stage of China's semiconductor manufacturing buildout and the dominance of DISCO and Tokyo Seimitsu in established fabs worldwide. Guangli is building a semiconductor intelligent manufacturing base in Zhengzhou, signaling ambition to scale domestically, but the gap between its current position and the Japanese incumbents remains vast.

For DISCO and Tokyo Seimitsu, Guangli/ADT represents a longer-term strategic concern rather than a near-term competitive threat. The concern is that Chinese government subsidies and preferential procurement policies could accelerate Guangli's penetration of the Chinese domestic market -- a market that is growing rapidly as China builds new fabs. If Chinese fabs are incentivized or required to purchase domestically manufactured dicing equipment, the addressable market for Japanese equipment in China could shrink over time.

### Emerging Competition: Shenyang Heyan Technology (China)

Shenyang Heyan Technology Co., Ltd. (CMP-0089) is a private Chinese company that has achieved a notable milestone: producing the first domestically mass-produced wafer dicing machine in China.

Founded in 2011 by a team drawn from China's early national dicing machine development project -- a lineage claimed to encompass over forty years of accumulated experience -- Heyan offers a range of dicing machines spanning six-inch to twelve-inch wafer sizes. Its DS9260 fully automatic twelve-inch dual-axis dicing machine represents the current state of the art for Chinese domestic dicing equipment, featuring high-power opposing dual spindles and advanced alignment systems.

Heyan holds over twenty patents and is a member of the China Semiconductor Industry Association. However, as a private company with no public financial disclosures, its actual production volumes, customer base, and technology capabilities are difficult to verify independently. The company's equipment is understood to serve lower-end applications -- LED packaging, QFN/DFN/BGA packaging, and mature-node IC production -- rather than the advanced logic and memory applications where DISCO dominates.

### Other Chinese Competitors

The IndustryMap database identifies two additional Chinese entities with dicing-related capabilities:

**Beijing Shuoke Jingwei (CETC subsidiary, CMP-0091)** is a state-owned enterprise under the China Electronics Technology Group Corporation (CETC) umbrella. It develops both CMP and dicing equipment as part of China's national semiconductor equipment platform strategy. State ownership provides access to government subsidies and preferential procurement by state-affiliated fabs, but also imposes bureaucratic constraints that can slow commercial responsiveness.

**TSD / Tesi Di (CMP-0092)** is primarily focused on CMP and grinding equipment for compound semiconductors, with some overlap into dicing-adjacent processes. It is the number one player in compound semiconductor CMP within China.

Together, these Chinese competitors represent the early stages of a domestic substitution effort that China has pursued across virtually every semiconductor equipment category. The pattern is consistent: initial penetration in lower-end applications, gradual improvement in precision and reliability, and expansion into higher-value segments as domestic fabs grow and as geopolitical pressures incentivize local sourcing.

In dicing specifically, the Chinese substitution effort faces steeper barriers than in some other equipment categories. The precision requirements for dicing -- sub-micrometer blade positioning, nanometer-level spindle runout, single-digit-micrometer chipping tolerances -- are among the most demanding in semiconductor manufacturing. The recipe knowledge that DISCO has accumulated over decades, covering thousands of material-thickness-device combinations, cannot be replicated quickly. And unlike some equipment categories where a Chinese fab might tolerate slightly inferior performance in exchange for supply chain security, dicing defects directly destroy finished die -- making the cost of using inferior equipment immediately and painfully visible.

---

## Supply Chain Connections

### Upstream: Who Feeds the Dicing Step

Dicing sits at the transition point between front-end and back-end manufacturing. Its immediate upstream processes are wafer testing (Chapter 13) and wafer thinning (grinding). The wafer arriving at the dicing station has already passed through probing -- where each die is electrically tested to identify defectives -- and in many cases has been thinned from its original thickness to the target die thickness.

DISCO and Tokyo Seimitsu both manufacture grinding equipment, meaning the dicing step is often performed on integrated platforms from the same supplier that performed the preceding grinding step. This vertical integration within the back-end process flow reinforces the incumbents' positions: a customer using DISCO grinders has a natural path to DISCO dicers, and vice versa.

The consumables supply chain for dicing is dominated by the same companies. Diamond blades, grinding wheels, dicing tape, and process chemicals are largely sourced from DISCO's in-house consumables business or from a small number of specialized suppliers. DISCO's control of both the equipment and the consumables is a key source of its extraordinary margins -- it captures value at multiple points in the dicing process.

### Downstream: Who Depends on Dicing Output

The output of the dicing step -- individual die separated on dicing tape, ready for pick-up -- feeds directly into the die attach and packaging process (Chapter 15). The quality of the diced die determines the yield of every subsequent packaging step.

DISCO's confirmed supplier edges in the IndustryMap graph illustrate the breadth of its downstream reach. The company supplies dicing saws and blades to ASE Technology (CMP-0063, the world's largest OSAT), Amkor (CMP-0064, number two), JCET (CMP-0065, China's largest OSAT), Tongfu Microelectronics (CMP-0067), Tianshui Huatian (CMP-0068), Powertech Technology (CMP-0069, Taiwan's memory OSAT), KYEC (CMP-0101, the world's largest pure-play tester), Chipbond (CMP-0104), ChipMOS (CMP-0105), UTAC (CMP-0107, Singapore OSAT), Inari Amertron (CMP-0108, Malaysia's largest OSAT), Unisem (CMP-0109), and MPI Malaysia/Carsem (CMP-0110). This is thirteen confirmed OSAT and packaging customer relationships spanning Taiwan, China, South Korea, Singapore, and Malaysia.

Tokyo Seimitsu supplies the same broad customer base through its own dicing equipment, plus it provides probing and CMP equipment to many of the same customers, creating multi-product relationships that deepen commercial ties.

The downstream connection to advanced packaging (Chapter 15) is particularly significant. As chiplet architectures drive demand for precision singulation of smaller die with tighter tolerances, the packaging companies listed above will require ever-more-capable dicing equipment. DISCO and Tokyo Seimitsu are the suppliers that will deliver that capability -- or fail to, at enormous cost to the global semiconductor supply chain.

---

## The Valuation Paradox: Why the Better Business Scores Lower

One of the most instructive features of the DISCO and Tokyo Seimitsu comparison is the apparent paradox in their IndustryMap evaluation scores.

DISCO, with its seventy-plus percent market share, 41 percent operating margins, and impregnable competitive moat, scores 46.2 out of 100. Tokyo Seimitsu, with a ten percent dicing share and margins less than half of DISCO's, scores 61.0 -- more than fourteen points higher.

The explanation lies in the design of the evaluation framework, which is constructed as an investment screening tool rather than a business quality ranking. The framework's Dimension A measures valuation attractiveness relative to sector peers. DISCO trades at a PER of 51.2x against a peer median of 31.6x -- a 62 percent premium. Its PBR of 8.97x is 260 percent above the peer median of 2.49x. On valuation alone, DISCO scores just 1.2 out of 30. Tokyo Seimitsu, at PER 21.3x and PBR 2.35x, scores 20.0 out of 30 on the same dimension.

In Dimension B (competitive position), DISCO outscores Tokyo Seimitsu only modestly: 18 versus 20. This seems counterintuitive given DISCO's far superior market share, but Tokyo Seimitsu's probing monopoly (46 percent global share, world number one) and broader product portfolio offset its weaker dicing position, resulting in competitive position scores that are closer than one might expect.

In Dimension F (risk), DISCO actually scores worse (7) than Tokyo Seimitsu (4), partly because DISCO's customer concentration risk is higher -- the company is more narrowly focused on dicing and grinding, making it more exposed to any single-process disruption.

The lesson for investors is clear: a great business is not necessarily a great investment at every price. DISCO is an exceptional franchise, but at 51x earnings, the margin of safety is thin. Tokyo Seimitsu is a less dominant business with a more attractive entry point. The optimal investment approach may depend on whether the investor is buying DISCO for its quality (a compounder to hold through cycles) or screening for undervalued opportunities (where Tokyo Seimitsu's discount to peers offers more upside potential).

---

## Key Takeaways

- **Dicing is a precision bottleneck, not a commodity process.** Singulation quality -- measured in micrometers of chipping, straightness of cuts, and completeness of die separation -- directly determines the yield of the entire back-end packaging line. A few percent improvement in dicing yield translates to hundreds of millions of yen in recovered value annually for a high-volume fab.

- **Two Japanese companies control ninety percent of the global market.** DISCO (70-80% share) and Tokyo Seimitsu (approximately 10% share) form a natural duopoly sustained by extreme precision requirements, decades of accumulated process knowledge, long customer qualification cycles, and integrated equipment-plus-consumables business models.

- **Technology is evolving from blade to laser, but blade remains dominant.** Stealth dicing and laser ablation offer advantages for thin wafers and advanced packaging applications, particularly HBM stacking. However, blade dicing remains the workhorse for the majority of semiconductor production. The shift is gradual and additive, not substitutive -- expanding the total dicing equipment market rather than displacing one technology with another.

- **The chiplet era is a secular tailwind for dicing equipment.** More die per wafer, thinner die, tighter tolerances, and heterogeneous integration all increase the demands on dicing equipment and the value of precision singulation. DISCO and Tokyo Seimitsu are the primary beneficiaries.

- **Chinese domestic substitution is a long-term risk, not a near-term threat.** Guangli/ADT, Shenyang Heyan, and state-backed entities are developing domestic dicing capabilities, but the precision gap with Japanese equipment remains large. Korean laser specialist EO Technics is a more immediate competitive factor in the laser dicing segment, particularly for HBM applications.

- **DISCO is the better business; Tokyo Seimitsu may be the better investment.** DISCO's dominant market position and extraordinary profitability are fully reflected in its 51x PER premium valuation. Tokyo Seimitsu's broader product portfolio, prober leadership, and PER discount to equipment peers offer greater potential for valuation rerating, despite its smaller dicing market share.

---

*Data sources: CMP-0001 (Tokyo Seimitsu), CMP-0002 (DISCO Corporation), CMP-0074 (Guangli Technology / ADT), CMP-0089 (Shenyang Heyan Technology), CMP-0091 (CETC / Shuoke Jingwei), CMP-0099 (EO Technics), graph.json (110 nodes, 321 edges), evaluation_progress.json (scoring and investment theses)*
