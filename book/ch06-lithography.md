# Chapter 6: Lithography -- Printing the Circuit

> Lithography is the single most complex and expensive step in chip manufacturing, and while ASML's monopoly over extreme ultraviolet systems captures the headlines, Japan's entrenched positions in mature-node steppers, critical UV light sources, and a potentially disruptive nanoimprint technology mean that no lithography ecosystem functions without Japanese hands.

## Introduction

If semiconductor manufacturing were a publishing house, lithography would be the printing press. Every circuit, every transistor, every interconnect on a chip begins as a pattern of light projected through a mask onto a photosensitive surface. The pattern defines what the chip will become. If lithography fails -- if the lines blur, the alignment drifts, or the exposure dose wavers -- the chip is worthless. No amount of perfection in the subsequent deposition, etching, or planarization steps can rescue a pattern that was never properly printed.

Lithography is also the most expensive step in semiconductor manufacturing, both in terms of equipment cost and in its impact on overall fab economics. A single ASML EUV lithography system costs in excess of 150 million US dollars and requires its own dedicated cleanroom infrastructure, specialized power supply, and a team of engineers to maintain. A modern leading-edge fab may operate a dozen or more such systems, meaning the lithography toolset alone can represent several billion dollars of the total fab investment. Even at mature nodes, lithography equipment constitutes the single largest capital expenditure category for any fabrication facility.

Japan's relationship with lithography is both a story of loss and of enduring relevance. In the 1980s and early 1990s, Nikon Corporation dominated the lithography equipment market, holding well over fifty percent of global market share. Canon was a formidable second player. Together, these two Japanese companies controlled the technology that defined how chips were made. But through a combination of strategic missteps, a failed bet on electron-beam lithography, and ASML's masterful execution of the immersion lithography transition, Japan lost the leading edge of lithography to the Netherlands. Today, ASML holds a one-hundred-percent monopoly on EUV lithography and over ninety percent of the advanced ArF immersion market. Nikon retains roughly five to six percent of ArF immersion. Canon has exited the cutting-edge optical lithography contest entirely.

Yet Japan has not disappeared from lithography. Nikon and Canon remain significant suppliers of i-line and KrF steppers for the mature-node market -- a market that is growing, not shrinking, driven by automotive, industrial, and IoT demand. Ushio Inc. holds a seventy-five-percent global monopoly in the UV lamps that power these systems. And Canon is pursuing a radical alternative path: nanoimprint lithography, a technology that bypasses the physics of light entirely and could, if successful, reshape the economics of advanced chip patterning. This chapter explains the physics, the history, the economics, and the companies that define the lithography landscape.

---

## The Physics of Lithography: From Mercury Lamps to Tin Plasma

Lithography is, at its core, a photographic process. A pattern is created on a glass plate called a photomask, and light is projected through that mask onto a silicon wafer coated with a light-sensitive chemical called photoresist. Where the light strikes the resist, it changes the chemical structure, allowing the exposed (or unexposed, depending on the resist type) areas to be selectively removed by a developer solution. The resulting pattern on the wafer defines the geometry of one layer of the chip's circuitry.

The fundamental limit on how small a feature can be printed is governed by the Rayleigh criterion, a relationship from classical optics:

**Resolution = k1 x (wavelength / numerical aperture)**

This equation tells us that there are only three ways to print smaller features: reduce the wavelength of the light source, increase the numerical aperture of the lens system, or reduce the process factor k1 through clever engineering tricks such as phase-shift masks, off-axis illumination, and multiple patterning. The history of lithography is essentially the history of exploiting all three approaches simultaneously.

### i-Line: The Mercury Lamp Era (436 nm)

The earliest generation of modern semiconductor lithography used the i-line emission of a mercury arc lamp at 436 nanometers wavelength. These systems, known as i-line steppers, could pattern features down to approximately 350 nanometers. The technology was straightforward: a high-pressure mercury lamp produced broadband ultraviolet radiation, and optical filters selected the 436-nanometer spectral line for exposure.

i-line lithography may sound archaic, but it remains in active production today. Power management chips, automotive microcontrollers, MEMS sensors, and analog integrated circuits are manufactured at nodes of 130 nanometers and above -- well within i-line capability. These mature-node chips are experiencing a demand renaissance driven by the electrification of automobiles, industrial automation, and the proliferation of IoT devices. A single modern electric vehicle contains several thousand semiconductor devices, the vast majority of which are manufactured at mature process nodes using i-line or KrF lithography.

### KrF: The First Excimer Laser (248 nm)

As feature sizes shrank below 350 nanometers in the mid-1990s, the industry transitioned from mercury lamps to excimer lasers. The krypton fluoride (KrF) excimer laser produces deep ultraviolet light at 248 nanometers, nearly halving the wavelength and enabling a corresponding reduction in minimum feature size. KrF lithography pushed resolution to approximately 130 nanometers, enabling the transition from the 250-nanometer to the 130-nanometer technology node.

KrF systems required entirely new lens materials -- fused silica replaced conventional glass optics -- and new photoresist chemistries. The chemical amplification resist (CAR) concept was developed specifically for KrF, where a photoacid generator compound (PAG) absorbs the 248-nanometer photon and catalytically amplifies the chemical change in the resist polymer. This resist chemistry, pioneered largely by Japanese chemical companies including Tokyo Ohka Kogyo and JSR, remains the foundation of all DUV lithography.

### ArF: The Push to 193 nm

The argon fluoride (ArF) excimer laser at 193 nanometers took over for the 90-nanometer node and below. ArF lithography, combined with increasingly sophisticated resolution enhancement techniques, extended optical lithography far beyond what many physicists believed possible.

The critical breakthrough came with immersion lithography, commercialized in the mid-2000s. By placing a film of ultrapure water between the final lens element and the wafer surface, the effective numerical aperture could be increased from approximately 0.93 to 1.35 -- the refractive index of water at 193 nanometers is approximately 1.44, enabling light to be bent more tightly. This single innovation extended ArF lithography from the 65-nanometer node all the way to the 7-nanometer node and beyond, when combined with multiple patterning techniques.

It was the immersion lithography transition that proved decisive in the competitive battle between ASML and Nikon. ASML bet aggressively on immersion technology, working closely with TSMC and developing the TWINSCAN platform that could handle the water film at high throughput. Nikon, which had been the technology leader in dry ArF systems, was slower to commit to immersion. By the time Nikon's immersion systems reached production quality, ASML had established itself as the preferred tool for leading-edge fabs. The market share gap, once narrow, became a chasm.

### Multi-Patterning: Extending 193 nm Beyond Its Limits

When even immersion ArF could not resolve the features needed for nodes below 20 nanometers with a single exposure, the industry adopted multi-patterning techniques. In SADP (self-aligned double patterning), a single lithography step is followed by deposition and etching steps that effectively double the pattern density. SAQP (self-aligned quadruple patterning) repeats the process to achieve four times the density. At Samsung's 7-nanometer node using DUV lithography, certain critical layers required SAQP -- meaning four times as many process steps for a single layer, each one requiring precise alignment.

Multi-patterning worked, but it was expensive and slow. Each additional patterning pass required its own deposition, etch, and cleaning steps, multiplying the process complexity and cost. A single critical metal layer at 7 nanometers using SAQP might require twelve to fifteen process steps where a single EUV exposure would require only one. This cost differential is the economic engine that drives EUV adoption.

### EUV: The 13.5-Nanometer Revolution

Extreme ultraviolet lithography operates at a wavelength of 13.5 nanometers -- more than fourteen times shorter than ArF immersion. At this wavelength, virtually all materials absorb light, so the entire optical system must use reflective optics (multilayer mirrors of alternating molybdenum and silicon) rather than transmissive lenses, and the entire optical path must be maintained under high vacuum.

The EUV light source itself is one of the most extraordinary engineering achievements in the history of manufacturing. Molten tin droplets, each approximately 25 micrometers in diameter, are fired into a vacuum chamber at speeds exceeding 70 meters per second. A high-power carbon dioxide laser strikes each droplet twice -- a pre-pulse to flatten it into a pancake shape, then a main pulse to vaporize it into a plasma that emits 13.5-nanometer radiation. This process repeats 50,000 times per second. The overall conversion efficiency from laser power to usable EUV light at the wafer is approximately two percent. A modern EUV system consumes over one megawatt of electrical power -- roughly enough to power a thousand homes.

The development of EUV lithography spanned over two decades and consumed tens of billions of dollars in research investment across ASML, its partner Carl Zeiss (which manufactures the mirrors), and TRUMPF (which builds the laser systems). The first production-worthy EUV system, the NXE:3400B, reached semiconductor fabs in 2018-2019. By 2025, ASML had shipped hundreds of EUV systems, and the technology was in volume production at TSMC, Samsung, and Intel for nodes at 7 nanometers and below.

ASML's next-generation system, High-NA EUV, increases the numerical aperture from 0.33 to 0.55, enabling resolution below eight nanometers for a single exposure. The first High-NA system, the EXE:5000, shipped in 2024 at a price exceeding 350 million euros per unit.

---

## How Japan Lost the Leading Edge

The story of how Nikon and Canon lost the lithography market to ASML is one of the most studied competitive failures in semiconductor history. Understanding it is essential to evaluating where Japan stands today.

### The Golden Era: 1980-2000

Throughout the 1980s, Nikon and Canon were the undisputed leaders in photolithography equipment. Nikon, in particular, built its reputation on precision optics and mechanical engineering excellence. The company's stepper systems -- machines that expose one chip at a time by stepping across the wafer -- set the standard for overlay accuracy and image quality. By 1990, Nikon held approximately fifty percent of the global lithography market, with Canon at roughly twenty-five percent. ASML, founded in 1984 as a joint venture between Philips and ASM International, was a distant third.

Japan's dominance was not incidental. The country's VLSI (Very Large Scale Integration) research project of the late 1970s had created deep collaborative ties between Japanese equipment makers and Japan's then-dominant DRAM manufacturers -- NEC, Hitachi, Toshiba, Fujitsu, and Mitsubishi. These chipmakers demanded the best lithography tools, and their equipment suppliers delivered. The Japanese lithography ecosystem included not just Nikon and Canon as system integrators but also companies like Ushio, which supplied the light sources, and a network of precision optics and mechanics suppliers.

### The Immersion Inflection: 2002-2008

The critical turning point came with immersion lithography. As the industry debated how to extend optical lithography beyond the dry ArF limit, two competing approaches emerged. One school of thought, championed by researchers at MIT Lincoln Laboratory and supported by TSMC's then-CTO Burn-Jeng Lin, argued for placing water between the lens and the wafer to increase numerical aperture. The other school favored moving directly to shorter wavelengths -- either 157-nanometer fluorine laser lithography or electron-beam projection.

ASML embraced immersion lithography with conviction. The company formed a close engineering partnership with TSMC to co-develop the technology for volume manufacturing, and by 2006 it was shipping production-quality immersion scanners. ASML's TWINSCAN platform proved superior at managing the water film -- preventing bubbles, controlling temperature, and maintaining wafer throughput.

Nikon hesitated. The company had invested heavily in 157-nanometer lithography, which ultimately proved impractical due to lens material limitations (calcium fluoride, the only viable lens material at 157 nm, could not be produced in sufficient size and quality). When Nikon redirected to immersion, it found itself behind ASML in both technology maturity and customer relationships. Critically, TSMC -- which was rapidly becoming the world's most important customer for lithography tools -- had already committed to ASML's platform.

Canon's position eroded even more rapidly. The company, whose lithography business was always secondary to its camera and printer divisions, lacked the R&D intensity to keep pace with the accelerating investment required for advanced lithography.

### The EUV Lockout

ASML's immersion lithography victory was devastating, but the EUV transition made it permanent. ASML had been involved in EUV development since the 1990s through its participation in the EUV LLC consortium. When the technology finally matured for production in the late 2010s, only ASML had a commercially viable system. The development cost -- estimated at over 10 billion euros across ASML and its ecosystem partners -- was beyond what Nikon or Canon could match, particularly given their shrinking market shares in the preceding generation of tools.

Nikon explored EUV technology but never brought a production system to market. The company publicly acknowledged that it could not justify the investment required to compete with ASML in EUV given its reduced market share and revenue base. Canon made no serious attempt at EUV.

The result is a market structure that, at the leading edge, is a pure monopoly. ASML holds one hundred percent of EUV lithography and approximately ninety-four percent of the ArF immersion market. Nikon retains roughly five to six percent of ArF immersion. The remaining mature-node market -- i-line and KrF -- is where Japan still competes meaningfully.

---

## Company Profiles

### ASML Holding N.V. (ASML) -- The EUV Monopoly

**Founded:** 1984 | **HQ:** Veldhoven, Netherlands | **Market Cap:** ~45.3 trillion yen (USD 562 billion)

ASML is the most valuable semiconductor equipment company in the world and one of the most strategically important technology companies in existence. Its monopoly on EUV lithography gives it an irreplaceable position in the supply chain for every advanced chip manufactured on the planet.

The company's product portfolio spans the full spectrum of lithography technology. Its TWINSCAN NXE series provides EUV lithography for volume production at 7-nanometer nodes and below. The next-generation EXE series (High-NA EUV) targets the 2-nanometer node and beyond. ASML also continues to sell DUV systems -- both ArF immersion and KrF -- which remain essential for non-critical layers even at the most advanced nodes, and which dominate manufacturing at mature nodes.

ASML's moat is multi-layered. The technology itself is extraordinarily difficult to replicate -- the EUV source, the multilayer mirrors (supplied by Carl Zeiss SMT), and the laser system (supplied by TRUMPF) represent decades of accumulated engineering that no competitor can shortcut. The installed base creates a service and upgrade revenue stream that is highly recurring. And the ecosystem of complementary technologies -- Lasertec for mask inspection (see Chapter 7), HOYA for mask blanks, and a network of photoresist suppliers -- has been built around ASML's specifications.

The company's client list is effectively the entire advanced semiconductor industry. TSMC (CMP-0017), Samsung (CMP-0018), Intel (CMP-0019), SK Hynix (CMP-0020), and Micron (CMP-0021) are all confirmed ASML customers. The graph data shows ASML supplying EUV lithography to all five major chipmakers, plus DUV lithography to SMIC (CMP-0066), UMC (CMP-0102), and GlobalFoundries (CMP-0106).

ASML's ecosystem partnerships with Japanese companies are noteworthy. Lasertec (CMP-0006) provides the sole EUV mask inspection capability that validates the photomasks used in ASML's systems. HOYA (CMP-0015) supplies the EUV mask blanks. Toppan (CMP-0047) and Dai Nippon Printing (CMP-0049) produce the photomasks themselves. These Japanese companies are not suppliers to ASML in a direct sense, but they are indispensable co-participants in the EUV ecosystem -- without them, ASML's machines cannot produce chips.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 38.49x |
| PBR | 20.16x |
| ROE | 50.46% |
| Revenue (Latest FY) | ~4,585 billion yen |
| Revenue Growth YoY | 15.6% |
| Operating Margin | 34.6% |
| Dividend Yield | 0.86% |
| Evaluation Score | 54.8 / 100 |

ASML trades at a significant premium to its semiconductor equipment peers (G1 median PER: 31.59x), reflecting its monopoly status and extraordinary profitability. The PBR of 20.16x, more than eight times the G1 median of 2.49x, confirms that the market has fully priced in ASML's competitive position. The company's ROE of 50.46% is the highest among all 110 companies in the dataset, a direct consequence of its pricing power and high-margin installed base services. For investors, ASML is a superb company with limited valuation upside -- the moat is recognized and the stock is priced accordingly.

---

### Nikon Corporation (7731.T) -- The Fallen Champion

**Founded:** 1917 | **HQ:** Tokyo, Japan | **Market Cap:** ~648 billion yen

Nikon Corporation's semiconductor lithography division is a shadow of its former self, yet the company retains a meaningful position in the mature-node market and is developing a new ArF platform with ASML compatibility targeting 2028.

Nikon was incorporated in 1917 as Nippon Kogaku K.K., a manufacturer of optical lenses. The company built its first semiconductor lithography system in 1980 and quickly became the dominant force in the industry. Through the 1980s and 1990s, Nikon steppers and scanners set the standard for overlay accuracy -- the precision with which successive layers of circuit patterns are aligned to one another. Nikon's brand was synonymous with lithographic excellence.

The immersion transition changed everything. As described above, Nikon's delayed commitment to immersion technology allowed ASML to capture the leading-edge market. Today, Nikon holds approximately 5.7% of the ArF immersion lithography market, compared to ASML's 94.3%. The company has no EUV capability and no realistic path to developing one.

What Nikon does retain is a strong position in mature-node lithography. The company's i-line and KrF steppers continue to serve the automotive, industrial, and power semiconductor markets. These markets are growing -- the global installed base of mature-node lithography systems is expanding as new fabs are built for automotive chips, display driver ICs, and power management devices. Nikon's existing customer relationships with TSMC (CMP-0017), Samsung (CMP-0018), and Intel (CMP-0019) ensure a continuing revenue base from both new tool sales and aftermarket service.

The most intriguing development in Nikon's semiconductor strategy is the announcement of a new ArF immersion platform designed for ASML compatibility, targeting initial deployment in 2028. The logic is straightforward: with ASML holding a near-monopoly on ArF immersion, any reduction in customer concentration risk or improvement in tool availability represents value to the chipmakers. If Nikon can deliver a platform that integrates seamlessly into ASML-dominated fabs, it could recapture a meaningful share of the ArF immersion market without needing to compete at the technology frontier.

Beyond lithography, Nikon has diversified into precision measurement equipment, digital solutions, and healthcare imaging. Semiconductor lithography now represents a minority of the company's overall revenue, which totalled approximately 715.2 billion yen in the latest fiscal year.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 26.51x |
| PBR | 1.05x |
| ROE | 1.9% |
| Revenue (Latest FY) | ~715.2 billion yen |
| Revenue Growth YoY | -0.7% |
| Operating Margin | 1.68% |
| Foreign Ownership | 38.9% |
| Dividend Yield | 2.54% |
| Evaluation Score | 43.5 / 100 |

Nikon's financial profile reflects the challenges of its competitive position. The PBR of 1.05x -- essentially book value -- signals that the market views the company as a low-growth business with limited pricing power. The operating margin of 1.68% is well below the G1 semiconductor equipment median of 14.9%, reflecting both the lower margins of its mature-node lithography business and the drag from its non-semiconductor divisions. The ROE of 1.9% is strikingly low, suggesting that Nikon's capital is not being deployed efficiently.

The PER of 26.51x appears reasonable against the G1 median of 31.59x, but it must be contextualized against the company's weak earnings growth. Foreign ownership at 38.9% is among the higher levels in the Japanese semiconductor universe, suggesting that institutional investors have recognized the brand name if not the growth story. The evaluation score of 43.5 places Nikon in the lower half of the scored universe, reflecting its weak competitive moat (score B: 9/25) and poor financial performance metrics (score C: 2/15).

---

### Canon Inc. (7751.T) -- Mature Node Workhorse, Nanoimprint Disruptor

**Founded:** 1937 | **HQ:** Tokyo, Japan | **Market Cap:** ~4.19 trillion yen

Canon is a diversified Japanese electronics company best known for cameras, printers, and office equipment. Within its semiconductor equipment division, Canon holds two distinct positions: a mature-node lithography business supplying i-line and KrF steppers, and a potentially transformative nanoimprint lithography (NIL) program that could disrupt the economics of advanced node patterning.

Canon entered the semiconductor lithography market in the 1970s and was, alongside Nikon, one of the two dominant Japanese lithography companies through the 1980s and 1990s. Like Nikon, Canon lost ground to ASML during the immersion and EUV transitions. Unlike Nikon, Canon did not attempt to maintain a position in the ArF immersion market and instead pivoted strategically toward two opportunities: the continuing demand for mature-node steppers and the development of nanoimprint lithography.

Canon's i-line and KrF steppers supply TSMC (CMP-0017), Samsung (CMP-0018), and Intel (CMP-0019) for mature-node production. The graph data confirms Canon as a supplier of i-line/KrF steppers to TSMC and Samsung, and of nanoimprint lithography equipment to Intel. This customer breadth, spanning all three of the world's largest chipmakers, provides a stable revenue foundation.

**Nanoimprint Lithography: The Radical Alternative**

Canon's most significant strategic asset in the semiconductor space is its nanoimprint lithography (NIL) technology, which the company has been developing since 2004 and commercialized in 2023 with the FPA-1200NZ2C system.

Nanoimprint lithography operates on a fundamentally different principle from optical lithography. Instead of projecting a pattern with light, NIL physically presses a template (a quartz mold carrying the circuit pattern in relief) into a liquid resist on the wafer surface. The resist fills the nanoscale features of the template, is cured by UV light, and the template is lifted away, leaving the pattern transferred to the wafer. No complex lens system is required. No high-power laser. No vacuum chamber.

The advantages are compelling. Canon claims NIL consumes approximately one-tenth the power of an EUV system -- a critical consideration as fab operators face mounting pressure on energy costs and sustainability. The equipment cost is a fraction of an EUV tool. The resolution capability of the current system extends to 14 nanometers, with a development roadmap targeting finer nodes. Canon is collaborating with Dai Nippon Printing (CMP-0049) to develop templates capable of 1.4-nanometer patterning by 2027.

The challenges are equally significant. Throughput is the primary concern -- NIL processes each field sequentially through physical contact, which is inherently slower than the parallel optical exposure of a scanner. Defectivity is another issue: any particle trapped between the template and the wafer will be replicated across every subsequent imprint. Overlay accuracy -- the precision of aligning one layer to the previous one -- must match or exceed optical lithography standards, and this is difficult to achieve through mechanical contact.

Despite these challenges, NIL has attracted serious interest from the semiconductor industry. Canon has disclosed partnerships with a US semiconductor consortium, and Intel (CMP-0019) is a confirmed recipient of Canon's nanoimprint lithography equipment. If NIL can demonstrate production-worthy throughput and defect control, it could offer a dramatically lower-cost path to advanced patterning that would complement or partially substitute for EUV in certain layer types. Canon received Japan's Earth Environment Grand Prize in 2024 for the energy efficiency of its NIL technology, underscoring the growing importance of sustainability in fab economics.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 12.76x |
| PBR | 0.92x |
| ROE | 9.9% |
| Revenue (Latest FY) | ~4,650 billion yen |
| Revenue Growth YoY | 3.5% |
| Operating Margin | 6.5% |
| Dividend Yield | 3.29% |
| Evaluation Score | 65.0 / 100 |

Canon's valuation metrics are striking in the context of the semiconductor equipment peer group. The PER of 12.76x represents a sixty percent discount to the G1 median of 31.59x. The PBR of 0.92x means the company trades below book value -- extraordinary for a company with a viable advanced technology program and a diversified revenue base. The dividend yield of 3.29% is among the highest in the dataset.

#### Investment Perspective

Canon ranks fifth in the top-10 investment theses identified by the evaluation framework, with a composite score of 65.0 -- the highest among the four lithography companies profiled in this chapter. The thesis rests on two pillars.

First, **nanoimprint lithography optionality**. The NIL program represents a low-probability, high-impact call option on a technology that could disrupt the economics of advanced lithography. If NIL achieves production viability at advanced nodes, Canon's semiconductor equipment division would experience a step-change in revenue and margin. The market currently prices this optionality at approximately zero, as reflected in the below-book-value PBR. Canon scores 4/5 on technology differentiation (B3) and 3/3 on capacity expansion catalysts (E2), reflecting the evaluation framework's recognition of NIL's potential.

Second, **mature-node revenue stability**. Canon's existing lithography and broader semiconductor equipment business provides a stable base that supports the company through the NIL development period. With revenue of 4,650 billion yen and a diversified portfolio spanning imaging, medical systems, and industrial equipment, Canon is not a single-product bet.

The primary risk is execution. NIL has been "almost ready" for over a decade, and the throughput and defectivity challenges are real. Canon's overall operating margin of 6.5% is well below the G1 semiconductor equipment median, depressed by lower-margin consumer and office products segments. Investors in Canon are buying a diversified conglomerate at a deep value price with a free option on a potentially transformative semiconductor technology. The evaluation score of 65.0 reflects strong valuation marks (A: 30.0/30, the maximum possible) partially offset by modest competitive positioning and mediocre financial performance at the consolidated level.

---

### Ushio Inc. (6925.T) -- The UV Lamp Monopoly

**Founded:** 1964 | **HQ:** Tokyo, Japan | **Market Cap:** ~233.7 billion yen

Ushio Inc. is the world's dominant manufacturer of industrial UV lamps, holding an estimated seventy-five percent global market share in i-line lithography UV lamps. The company is a textbook example of a hidden monopolist -- virtually unknown to generalist investors, yet indispensable to the semiconductor lithography ecosystem.

Ushio was founded in 1964 in Himeji, Hyogo Prefecture, as a manufacturer of industrial light sources. The company developed expertise in ultra-high-pressure mercury and xenon lamps, which found their natural application in semiconductor lithography when the industry adopted UV light sources for wafer exposure. Ushio's lamps range from 500 watts to 35 kilowatts in power, serving applications from semiconductor exposure equipment to LCD panel manufacturing and UV curing for industrial processes.

In the semiconductor lithography context, Ushio's position is straightforward but critical. Every i-line stepper requires a high-intensity, spectrally pure UV lamp to generate the 436-nanometer exposure light. These lamps are consumable items -- they degrade over time and must be replaced at regular intervals. Ushio supplies these lamps to both Nikon (CMP-0050) and Canon (CMP-0051), the two remaining manufacturers of i-line steppers. The graph data explicitly shows Ushio as a supplier to both Nikon (labeled "i-line UV lamps, 75% share") and Canon (labeled "i-line UV lamps").

The nature of this business creates a recurring revenue stream tied to the installed base of i-line steppers worldwide. As long as fabs operate i-line systems -- and they will for decades to come, given the ongoing demand for mature-node chips -- Ushio's lamp replacement business continues. The switching cost for lamp suppliers is significant: lithography tools are qualified with specific lamp characteristics, and any change in lamp supplier requires requalification of the entire exposure process.

Beyond semiconductor lithography, Ushio's Industrial Process segment serves the broader UV industrial market, including LCD manufacturing, UV curing, and environmental sterilization. The company has also developed excimer lamp and LED-based UV sources, positioning itself for the evolution of industrial UV technology.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 61.68x |
| EPS | 50.18 yen |
| ROE | 3.41% |
| Revenue (Latest FY) | ~178.3 billion yen |
| Revenue Growth YoY | 0.0% |
| Operating Margin | 5.81% |
| Dividend Yield | 2.50% |
| Evaluation Score | 37.6 / 100 |

Ushio's financial profile presents a paradox. The company holds a dominant market position (B1: 8/10 for market share) but generates modest financial returns. The PER of 61.68x is nearly double the G1 median, suggesting that current earnings significantly understate the company's normalized earning power or, alternatively, that the stock price reflects speculative expectations for new growth areas. The operating margin of 5.81% is well below the equipment peer median of 14.9%. The ROE of 3.41% indicates that Ushio's monopoly pricing power does not translate into exceptional returns on equity -- likely because the i-line lamp market, while dominant, is relatively small in absolute terms.

Revenue growth is flat at 0.0%, reflecting the mature nature of the i-line lamp replacement market. The evaluation score of 37.6 is the lowest among the four companies in this chapter, dragged down by the stretched valuation (A: 1.9/30) and weak financial performance (C: 4.0/15). Ushio's moat score (B: 17/25) is strong, reflecting the genuine monopoly position and high switching costs, but the market appears to be pricing in growth that the current financials do not support.

---

## Competitive Landscape

The lithography equipment market is the most concentrated segment of the semiconductor equipment industry. The competitive dynamics differ sharply between the leading edge and the mature node market.

### Leading-Edge Lithography: Pure Monopoly

At the leading edge -- EUV and advanced ArF immersion -- ASML operates as a monopolist without meaningful competition. No other company manufactures EUV lithography systems, and ASML's 94.3% share of ArF immersion leaves Nikon's 5.7% as a rounding error in strategic terms. The graph data confirms this: both ASML and Nikon appear as lithography equipment competitors (bidirectional competitor edges between CMP-0026 and CMP-0050, and between CMP-0026 and CMP-0051), but the competitive relationship is asymmetric -- ASML competes with Nikon and Canon only in the sense that a lion competes with a house cat.

The barriers to entering EUV lithography are effectively absolute. The development cost exceeded 10 billion euros. The supply chain -- particularly Zeiss for mirrors and TRUMPF for laser systems -- is locked into ASML through long-term contracts and co-development agreements. The installed base of customer knowledge and process recipes is built around ASML's platform. No new entrant, whether from Japan, China, South Korea, or the United States, can realistically challenge this position within the next decade.

Chinese domestic efforts in lithography equipment, including work by Shanghai Micro Electronics Equipment (SMEE), remain focused on DUV systems at the 28-nanometer node and above -- roughly three to four generations behind the leading edge. These efforts may eventually capture a portion of the Chinese domestic mature-node market, adding competitive pressure to Nikon and Canon in that segment, but they pose no threat to ASML.

### Mature-Node Lithography: Nikon and Canon Hold Ground

The mature-node lithography market -- i-line (436 nm) and KrF (248 nm) systems operating at nodes from 350 nanometers to approximately 90 nanometers -- is a structurally different market from the leading edge. Tool prices are lower (tens of millions of dollars rather than hundreds of millions). Throughput requirements are less extreme. And the customer base is broader, spanning not just the major foundries but also specialty fabs, automotive chipmakers, and analog/power semiconductor manufacturers.

In this market, Nikon and Canon retain meaningful positions alongside ASML's DUV business. The mature-node market is experiencing structural growth driven by several factors:

- **Automotive electrification:** Each electric vehicle requires thousands of power management, sensor, and control chips manufactured at mature nodes.
- **Industrial IoT:** Connected sensors, edge processing devices, and industrial controllers use chips made on i-line and KrF processes.
- **5G infrastructure:** RF front-end components and baseband processors for cell towers use mature-node lithography.
- **Government incentives:** National semiconductor self-sufficiency programs in China, India, Europe, and Southeast Asia are funding new mature-node fabs.

This growth ensures that Nikon and Canon's i-line and KrF platforms have a long commercial life ahead. The installed base of mature-node lithography tools worldwide numbers in the thousands, and each tool requires ongoing service, lamp replacement (from Ushio), and periodic upgrades.

### Nanoimprint: Canon's Potential Disruption

Canon's nanoimprint lithography program introduces a potential competitive dimension that does not exist in the traditional optical lithography market. If NIL achieves production viability at advanced nodes, it would not directly compete with ASML's EUV systems on the same layers -- the technology profiles are too different -- but it could offer an alternative path for certain layer types where the extreme resolution of EUV is not strictly required but where DUV multi-patterning is prohibitively expensive.

The competitive question for NIL is not whether it can replace EUV (it almost certainly cannot, for the most critical layers) but whether it can capture a subset of layers currently served by EUV or DUV multi-patterning at a fraction of the cost. If Canon can demonstrate this for even a small number of layers per chip, the revenue opportunity is significant.

---

## Supply Chain Connections

Lithography sits at the intersection of multiple supply chains that are examined in detail in adjacent chapters of this book.

### Upstream Connections

**Photomasks and mask blanks (Chapter 7):** Every lithography exposure -- whether DUV, EUV, or nanoimprint -- requires a photomask. HOYA (CMP-0015) supplies EUV mask blanks, while Toppan (CMP-0047) and Dai Nippon Printing (CMP-0049) produce the finished masks. Lasertec (CMP-0006) inspects them. The quality of the mask directly determines the quality of the lithographic image; a single defect on a mask will be printed onto every wafer that passes through the stepper.

**Photoresist and chemicals (Chapter 8):** Lithography cannot function without photoresist -- the light-sensitive chemical that receives the pattern. Tokyo Ohka Kogyo (CMP-0033), JSR (CMP-0034), and other Japanese resist formulators supply the materials that must be precisely matched to each lithography wavelength. The resist chemistry for EUV is entirely different from KrF or i-line, and the development of new resist platforms is a multi-year effort requiring close collaboration between resist makers and lithography equipment suppliers.

**UV light sources:** Ushio (CMP-0061) supplies the UV lamps that power Nikon and Canon's i-line systems. This supply chain edge is explicit in the graph data: Ushio as supplier to both Nikon and Canon, with the seventy-five percent market share label on the Nikon edge.

**Precision optics and components:** While not tracked as individual nodes in the database, the lens systems in lithography tools require extreme precision. For ASML, Carl Zeiss SMT produces the mirrors. For Nikon and Canon, optics are largely manufactured in-house, drawing on decades of camera and microscopy lens experience. Aval Data (CMP-0054) supplies image processing modules and test components to Nikon, as confirmed by a supplier edge in the graph.

### Downstream Connections

**All major chipmakers:** Lithography equipment is sold directly to semiconductor manufacturers. The graph data shows ASML, Nikon, and Canon supplying TSMC (CMP-0017), Samsung (CMP-0018), and Intel (CMP-0019). ASML additionally supplies SK Hynix (CMP-0020), Micron (CMP-0021), SMIC (CMP-0066), UMC (CMP-0102), and GlobalFoundries (CMP-0106).

**Coater/developer equipment (Chapter 9):** After exposure by the lithography system, wafers must be coated with resist (before exposure) and developed (after exposure) using track equipment. Tokyo Electron (CMP-0004) dominates the coater/developer market with over ninety percent global share. The lithography scanner and the coater/developer track typically operate as an integrated cluster, with the track feeding wafers into and out of the scanner. TEL's dominance in track equipment means that every ASML EUV system operates in conjunction with a Tokyo Electron coater/developer.

**Cleaning and wet process (Chapter 10):** Post-lithography processing requires cleaning steps to remove residual resist and prepare the wafer for the next process step. SCREEN Holdings (CMP-0003) and its wet cleaning platforms are downstream of lithography in the process flow.

---

## The Economics of Lithography: Throughput, Cost-per-Layer, and Fab Design

Understanding the economics of lithography is essential to evaluating the competitive positions of the companies in this chapter.

### Cost per Wafer Layer

The fundamental economic metric in lithography is cost per wafer layer exposed. This is determined by three factors: the equipment cost (depreciated over its useful life), the throughput (wafers per hour), and the uptime (percentage of time the tool is productively exposing wafers).

An ASML EUV system costing 150 million dollars, operating at 200 wafers per hour with 80% uptime, over a five-year depreciation period, yields a depreciation cost of approximately 20 dollars per wafer layer. Add in maintenance, power consumption (over 1 megawatt), cleanroom space, and consumables, and the fully loaded cost can exceed 30-40 dollars per wafer layer.

Compare this to an ArF immersion system at roughly 50-60 million dollars with throughput of 250-300 wafers per hour: the cost per wafer layer drops to approximately 5-8 dollars. An i-line stepper at 10-15 million dollars with similar throughput costs under 3 dollars per wafer layer.

The economics explain why EUV is used only where it is strictly necessary. At the 3-nanometer node, a chip may have 80 or more lithography layers, but only 15-20 of those use EUV. The remaining layers are patterned with DUV (ArF immersion or KrF), and in some cases i-line for the least critical layers. This layered approach -- mixing lithography technologies within a single chip -- is why the mature-node lithography market remains vibrant even as EUV captures the headlines.

### Overlay Accuracy

Overlay accuracy -- the precision with which one layer is aligned to the previous one -- is perhaps the single most critical performance metric for a lithography system. At the 3-nanometer node, overlay must be controlled to within approximately 1.5 nanometers, or roughly five atomic diameters. Any misalignment greater than this causes the features on adjacent layers to fail to connect properly, resulting in non-functional transistors.

ASML's EUV systems achieve overlay accuracy below 1.5 nanometers through a combination of advanced metrology, machine learning-based correction algorithms, and extremely rigid mechanical platforms. Nikon's mature-node systems offer overlay accuracy that is fully adequate for the 65-nanometer and above nodes they serve, but they cannot match ASML's leading-edge specifications.

Canon's nanoimprint lithography faces a particular challenge in overlay accuracy because the template makes physical contact with the wafer. Any mechanical vibration, thermal expansion, or particle contamination affects alignment. Canon has invested heavily in solving this problem, and the FPA-1200NZ2C reportedly achieves overlay accuracy compatible with the 14-nanometer node, but whether this can be extended to tighter nodes remains an open question.

---

## Key Takeaways

- **ASML holds an absolute monopoly on EUV lithography and a near-monopoly on ArF immersion.** No competitor can realistically challenge this position within the next decade. The barriers are technological, financial, and ecosystem-based. ASML trades at a premium (PER 38.49x, PBR 20.16x) that fully reflects this moat.

- **Japan lost the leading edge of lithography but retained critical positions in the broader ecosystem.** Nikon and Canon supply i-line and KrF steppers for the growing mature-node market. Ushio holds 75% of the i-line UV lamp market. And Japan's photomask, photoresist, and mask inspection companies (covered in Chapters 7 and 8) are indispensable to all lithography systems, including ASML's.

- **The mature-node lithography market is structurally growing.** Automotive electrification, industrial IoT, and government-funded fab construction programs ensure that demand for i-line and KrF systems will persist and expand for decades. This is a tailwind for Nikon, Canon, and especially Ushio.

- **Canon's nanoimprint lithography is a high-optionality bet.** If NIL achieves production viability at advanced nodes, it could disrupt the cost structure of lithography. Canon's valuation (PER 12.76x, PBR 0.92x) prices this optionality at approximately zero, making it one of the most asymmetric risk-reward profiles in the semiconductor equipment space. Canon ranks fifth in the top-10 investment theses with a score of 65.0.

- **The lithography supply chain is deeply interconnected with other Japanese-dominated segments.** Photomasks (HOYA, Toppan, DNP), photoresist (TOK, JSR), mask inspection (Lasertec), and coater/developer equipment (Tokyo Electron) are all upstream or co-dependent technologies where Japanese companies hold dominant positions. Understanding lithography in isolation is impossible -- it must be understood as part of a patterning ecosystem that is overwhelmingly Japanese.

---

*Data sources: CMP-0026 (ASML), CMP-0050 (Nikon), CMP-0051 (Canon), CMP-0061 (Ushio), graph.json edges, evaluation_progress.json*
