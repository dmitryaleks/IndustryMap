# Chapter 8: Photoresist & Chemicals

> The chemicals that define the circuit pattern on a silicon wafer -- photoresists, developers, and rinse agents -- are among the most tightly controlled materials in the semiconductor supply chain, and Japan dominates every layer of their production from upstream resin synthesis to final formulation and distribution.

## Introduction

If lithography is the act of printing a circuit, photoresist is the ink. Without it, the most advanced EUV scanner in the world -- a machine that costs over 350 million dollars and took decades to develop -- is nothing more than an extraordinarily expensive light source with no surface to write on.

Photoresist is a light-sensitive polymer film, typically less than 100 nanometers thick at advanced nodes, that is coated onto a silicon wafer before each patterning step. When exposed to light of a specific wavelength through a photomask, the resist undergoes a chemical transformation that changes its solubility. The exposed regions (or in negative-tone resists, the unexposed regions) are then dissolved away by a developer solution, leaving behind a precise pattern that guides subsequent etching or deposition steps. This process is repeated dozens of times on a single wafer -- once for every layer of the circuit -- making photoresist not a one-time consumable but a material consumed in enormous volume across the entire manufacturing flow.

The global photoresist market is worth approximately 2.5 billion dollars annually, a figure that seems modest against the 600-billion-dollar semiconductor industry it enables. But this modest market size conceals outsized strategic importance. A single contamination event in a photoresist batch -- a few parts per billion of metallic ions -- can destroy an entire production lot of wafers worth tens of millions of dollars. The qualification of a new photoresist at a leading-edge fab takes twelve to eighteen months, and once qualified, the formulation is locked in for the life of the technology node. There are no emergency substitutions. There is no second source. The resist that works is the resist that ships.

Japan controls this market with a completeness that has no parallel in any other semiconductor material. Five Japanese companies -- Tokyo Ohka Kogyo, JSR, Shin-Etsu Chemical, Sumitomo Chemical, and FUJIFILM -- together hold roughly ninety percent of the global photoresist market. The upstream raw materials that these formulators depend on -- the novolac resins, the advanced polymers, the photoacid generators -- are themselves produced by a second tier of Japanese specialty chemical companies, several of which operate as monopolists or duopolists in their respective niches. And the distribution infrastructure that moves these chemicals from factory to fab is dominated by Nagase, a Japanese trading house with a 193-year history and a near-unrivaled network in electronic materials logistics.

This chapter maps the entire resist-developer-rinse chemical stack, from the upstream resin suppliers through the formulators to the specialty component makers and the distribution channel. It profiles eight companies across four tiers of the supply chain and explains why this particular segment of the semiconductor ecosystem may be the most difficult for any non-Japanese competitor to penetrate.

---

## The Chemistry of Patterning

To understand the companies in this chapter, it is necessary to understand the chemistry they work with. Photoresist technology has evolved through four distinct generations, each driven by the need to print smaller features using shorter wavelengths of light.

### Generation One: Novolac/DNQ Resists for g-line and i-line

The earliest photoresists used in modern semiconductor manufacturing are based on novolac resin -- a phenol-formaldehyde polymer -- combined with a photoactive compound called diazonaphthoquinone, or DNQ. The novolac resin is inherently soluble in alkaline developer solutions. The DNQ, when unexposed, acts as an inhibitor that prevents the resin from dissolving. When UV light strikes the resist at g-line (436 nm) or i-line (365 nm) wavelengths, the DNQ undergoes a photochemical reaction that converts it into indenecarboxylic acid, which actually enhances the dissolution rate. The result is a dramatic solubility contrast between exposed and unexposed regions -- enough to create clean, sharp patterns down to approximately 250 nanometers.

Novolac/DNQ resists are positive-tone: light makes the resist dissolve. They have been in continuous production since the late 1970s, when Tokyo Ohka Kogyo's OFPR-800 -- formulated on Gun Ei Chemical's RESITOP novolac -- became the global standard for 64K DRAM patterning. Remarkably, novolac-based i-line resists remain in high-volume production today. Even in fabs running the most advanced EUV processes, non-critical layers -- alignment marks, pad openings, certain implant masks -- are still patterned with i-line lithography because it is fast, cheap, and proven. Every leading-edge fab maintains i-line exposure tools alongside its EUV scanners. This means the market for novolac resin has not shrunk with the advance of technology; it has grown in proportion to the total number of wafer starts, which continues to increase.

The quality of the novolac resin determines the quality of the resist. Molecular weight distribution, residual metal ion content, and batch-to-batch consistency must be controlled at extraordinary precision. The resin must contain fewer than ten parts per billion of metallic impurities -- sodium, iron, chromium, nickel -- because even trace contamination in the resist becomes contamination on the wafer, which becomes defects in the transistors. This purity requirement is the fundamental barrier to entry for upstream resin suppliers. Achieving sub-ppb metal ion purity in a phenol-formaldehyde resin requires not only specialized synthesis and purification equipment but decades of accumulated process knowledge that cannot be replicated by reading a patent.

### Generation Two: Chemically Amplified Resists for DUV (KrF and ArF)

As feature sizes shrank below 250 nanometers, the semiconductor industry moved to shorter wavelengths: KrF excimer laser at 248 nm and ArF excimer laser at 193 nm. At these wavelengths, the novolac/DNQ chemistry no longer provides adequate sensitivity or resolution. The solution, pioneered in the 1980s at IBM Almaden Research Center by Hiroshi Ito and C. Grant Willson, was the chemically amplified resist (CAR).

In a chemically amplified resist, the photochemical event does not directly change the polymer's solubility. Instead, light generates a strong acid from a molecule called a photoacid generator, or PAG. This acid then catalyzes a cascade of chemical reactions during a post-exposure bake, amplifying the original photon event by orders of magnitude. A single photon generates a single acid molecule, but that acid molecule can catalyze the deprotection of hundreds of polymer side groups, flipping them from dissolution-inhibiting to dissolution-promoting. This chemical amplification is what gives DUV resists the sensitivity they need to work with the relatively low light intensity available at 248 nm and 193 nm.

For KrF resists, the base polymer is typically polyhydroxystyrene (PHS), a derivative of styrene that absorbs minimally at 248 nm. For ArF resists, which must be transparent at 193 nm, the polymers shift to methacrylate-based or cyclic olefin-based structures that have no aromatic rings -- since aromatic compounds absorb strongly at 193 nm and would block the light.

The PAG is the critical active ingredient. Its job is to generate a strong acid upon exposure -- typically a perfluorinated sulfonic acid -- with high quantum yield and minimal diffusion during the post-exposure bake. If the acid diffuses too far, the pattern blurs. If it does not diffuse enough, the amplification is incomplete. The PAG must be tuned to the specific wavelength, the specific polymer, and the specific process conditions at each fab. This is why photoacid generator chemistry is a specialized discipline in its own right, and why a single Japanese company -- Toyo Gosei -- has been able to capture sixty to seventy percent of the global PAG market.

### Generation Three: ArF Immersion and the Limits of DUV

ArF immersion lithography, which places a layer of ultrapure water between the lens and the wafer to increase the effective numerical aperture, extended DUV patterning to feature sizes below 40 nanometers. The resist chemistry for immersion lithography is fundamentally the same as dry ArF -- chemically amplified with methacrylate polymers and PAGs -- but with the addition of a topcoat that prevents the water from contaminating the resist. JSR Corporation was a pioneer in developing these immersion topcoats, and its materials became critical to the success of multi-patterning techniques that kept DUV lithography viable at the 10-nanometer and 7-nanometer nodes.

### Generation Four: EUV Resists and the Frontier

Extreme ultraviolet lithography operates at 13.5 nm -- a wavelength so short that it is absorbed by virtually all materials, including air. EUV resist chemistry is fundamentally different from DUV. The photon energy at 13.5 nm is 92 electron volts, compared to 6.4 eV for ArF -- enough to ionize molecules and generate secondary electrons that contribute to the chemical exposure. This creates both opportunity and challenge: the high energy means fewer photons are needed, but the stochastic nature of individual photon absorption creates shot noise, leading to random variations in the pattern known as line-edge roughness (LER) and line-width roughness (LWR).

The industry is pursuing two parallel approaches to EUV resist. The first is chemically amplified EUV resists -- extensions of the CAR platform with new PAGs and polymers optimized for EUV absorption. The second, and potentially more transformative, is metal-oxide resists -- inorganic materials based on tin-oxo clusters or hafnium-based compounds that absorb EUV photons far more efficiently than organic polymers and produce sharper patterns with less line-edge roughness. Metal-oxide resists, pioneered by Inpria (now a subsidiary of JSR after its 2021 acquisition), represent a platform shift that could reshape the competitive landscape. JSR's ownership of Inpria technology, now backed by the financial resources of the Japan Investment Corporation (JIC), positions Japan at the technological frontier of resist development.

The "RLS trade-off" -- resolution, line-edge roughness, and sensitivity, which cannot all be optimized simultaneously -- is the defining challenge of EUV patterning. Every resist formulator and every component supplier in this chapter is, in some way, working to push the boundaries of that trade-off.

### The Developer-Rinse Stack

Photoresist does not work in isolation. After exposure and post-exposure bake, the resist must be developed -- typically using a 2.38% solution of tetramethylammonium hydroxide (TMAH) in ultrapure water. This is the industry-standard positive-tone developer, and its concentration has not changed in decades. The consistency of the developer is critical: concentration uniformity across the wafer, temperature stability, and metal ion purity must all be controlled at parts-per-trillion levels.

After development, the wafer is rinsed to remove residual developer and dissolved resist. Rinse chemistry -- seemingly the simplest step -- is in practice a carefully optimized process. The rinse must not damage the remaining resist pattern, must not leave residues, and must not create pattern collapse in the narrow spaces between features. At EUV dimensions, where feature widths are below 20 nanometers, the surface tension of the rinse liquid can physically pull over tall, thin resist lines -- a phenomenon called pattern collapse that limits the practical aspect ratio of resist features and imposes constraints on resist thickness.

Tokyo Ohka Kogyo and FUJIFILM both supply developers and rinse agents alongside their resist products, creating integrated chemical stacks that are qualified as systems at each fab. Switching any single component -- the resist, the developer, or the rinse -- requires requalification of the entire stack, further deepening the switching costs that protect incumbent suppliers.

---

## Upstream Raw Materials

### Gun Ei Chemical (4229.T) -- Novolac Resin Duopolist and the Book's Highest-Conviction Name

**Founded:** 1945 | **HQ:** Takasaki, Gunma Prefecture | **Market Cap:** 45.9 billion yen

Gun Ei Chemical Industry is a Gunma-based specialty chemical company that has quietly established itself as the dominant supplier of novolac-type phenol-formaldehyde resins -- sold under the RESITOP brand -- used as the base polymers in photoresists for semiconductor manufacturing. It is the kind of company that does not appear in any semiconductor ETF, is covered by almost no sell-side analysts outside Japan, and yet sits at the very foundation of the photoresist supply chain. Its strategic position is confirmed by the most revealing signal available in Japanese corporate culture: two of the nation's largest photoresist makers, Tokyo Ohka Kogyo and Shin-Etsu Chemical, each hold equity stakes in Gun Ei -- a cross-shareholding structure that in Japan signals a deep, long-term supply relationship that both parties consider essential to protect.

Gun Ei claims to be the world's only supplier with a continuous photoresist resin lineup spanning all commercial lithography wavelengths -- from g-line (436 nm) through i-line (365 nm), KrF (248 nm), and ArF (193 nm). This breadth of coverage is not merely a product catalog achievement; it represents decades of accumulated formulation knowledge across four distinct polymer chemistries. In the g-line and i-line novolac segment, Gun Ei operates in a duopoly with Maruzen Petrochemical, with Gun Ei holding the dominant position in mature-node novolac and Maruzen leading in advanced-node (KrF, ArF, EUV) polymers. Together, these two companies supply essentially all of the photoresist base polymers consumed by Japan's five major photoresist formulators.

The relationship between Gun Ei and Tokyo Ohka Kogyo is foundational. TOK's OFPR-800 g-line photoresist, introduced in 1979 and adopted globally as the standard for 64K DRAM production, was formulated on Gun Ei's RESITOP novolac. That commercial relationship has persisted for over forty years, and TOK holds a 1.87% equity stake in Gun Ei to this day. Shin-Etsu Chemical, which entered the photoresist business in 1997 at its Naoetsu plant in Niigata, holds a larger 3.66% stake -- the largest single external shareholder position in Gun Ei's register. These cross-shareholdings are not passive investments; they are commercial anchors that guarantee long-term supply stability in a material where requalification takes six to twelve months and disruption is unacceptable.

Gun Ei's operations extend well beyond photoresist polymers, though the semiconductor materials segment is the strategic core. The company is the world's sole commercial producer of Kainol -- a phenol resin-derived activated carbon fiber with the highest limiting oxygen index of any organic textile, making it permanently flame-resistant without surface treatment. This monopoly product, distributed globally through subsidiary Kynol Inc., serves niche markets in solvent recovery, fire protection, and environmental filtration. The company also holds the global Milex brand for friction-material binder resins used in automotive disc brakes, acquired from Mitsui Fine Chemicals in July 2022 along with all associated patents, know-how, and global distribution rights.

Vertical integration provides additional defensibility. Gun Ei's wholly-owned subsidiary Tohoku Uloid Industrial Co., Ltd. -- acquired from Mitsui Chemicals in 2014 and located in Iwate Prefecture -- produces formaldehyde in-house across seven reaction vessels (5-30 m3 capacity), securing self-sufficiency in one of the two primary monomers for novolac synthesis. For the other monomer, phenol, Gun Ei sources domestically from Mitsui Chemicals and Mitsubishi Chemical. Mitsui's announced closure of its Ichihara phenol plant by FY2026 introduces a near-term raw material supply risk, partially mitigated by an emerging Mitsui-Mitsubishi joint supply arrangement announced in January 2025.

Gun Ei is investing aggressively ahead of demand. A first-phase expansion completed in FY2024 added approximately thirty percent additional photoresist polymer capacity. A second expansion -- a 3.5 billion yen new factory at the Gunma headquarters -- is completing in FY2026, adding a further step-change in capacity. President Kiichiro Arita stated explicitly that "looking at future growth, current equipment cannot keep up," linking the investment directly to AI-driven semiconductor demand acceleration. This positions Gun Ei one to two layers upstream from the direct capacity wave driven by TSMC's JASM Kumamoto fab, Kioxia-Western Digital NAND expansion, and Rapidus's 2nm pilot line at Chitose.

Gun Ei operates additional production subsidiaries in Thailand (Thai GCI Resitop, contributing over ten percent of consolidated revenue), India (GCI India, where capacity is being doubled for automotive brake resins), and the United States (GCI America, for Milex distribution in North America).

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 17.6x |
| PBR | 0.64x |
| EPS | 289.5 yen |
| Revenue (FY2025) | 30.54 billion yen (+0.78% YoY) |
| Operating Margin | 7.51% |
| Net Income (FY2025) | 1.92 billion yen |
| Foreign Ownership | 3.6% |
| Dividend | 100 yen/share (~35% payout) |
| Net Cash | 10.21 billion yen (22% of market cap) |
| Equity Ratio | 81.2% |

#### Investment Perspective

Gun Ei Chemical holds the highest investment thesis score in this book's entire 74-company evaluation framework: 78.9 out of 100, with High confidence.

The thesis rests on five pillars. First, a structural moat: Gun Ei operates in a duopoly with Maruzen Petrochemical in photoresist base polymers, with dominant share in g/i-line novolac and the world's only claimed all-wavelength product lineup. Re-qualification switching costs of six to twelve months make supplier displacement prohibitively expensive for downstream resist formulators. Metal ion purity at sub-ppb levels requires decades of accumulated process knowledge.

Second, valuation cushion: despite a stock price gain of eighty-eight percent over twelve months (hitting a ten-year high of 5,180 yen on February 12, 2026), PBR remains at 0.64x -- the stock trades well below book value. Net cash of 10.21 billion yen represents twenty-two percent of the entire market capitalization, implying the operating business is valued at only approximately 35.7 billion yen on a cash-adjusted basis. The equity ratio of 81.2% represents a fortress balance sheet. Treasury shares of 26.25% of total shares outstanding provide ammunition for future buybacks.

Third, capacity investment ahead of demand: the 3.5 billion yen Gunma factory, arriving in FY2026, positions Gun Ei to capture incremental polymer demand from Japan's semiconductor renaissance before competitors can respond. Q3 FY2026 cumulative operating income of 2.23 billion yen already reached 96.8% of full-year guidance with one quarter remaining, implying a meaningful full-year earnings beat.

Fourth, international underfollowing: foreign ownership stands at 3.6% -- a fraction of the 28-30% average for Nikkei 225 constituents. Gun Ei appears in no major global semiconductor materials ETF. Its Stockopedia quantitative rank of 99/100 ("Super Stock") highlights an extreme gap between fundamental quality and international investor awareness. Formal sell-side coverage is sparse; the analyst consensus target of approximately 4,000 yen has been comprehensively exceeded by the market.

Fifth, a medium-term growth roadmap: the GCI 2030 plan, announced June 2025, targets revenue of 40 billion yen by FY2031 (from 30.5 billion; a thirty-one percent increase) and operating profit of 4 billion yen (from 2.3 billion; a seventy-four percent increase). Two growth pillars drive the plan: electronic materials (AI/semiconductor capex via RESITOP photoresist polymers and GPI reactive polyimide for semiconductor packaging) and environmental materials (Kainol fiber as Chinese solvent recovery markets stabilize).

Risks to monitor include: ROE of 3.86%, suppressed by the large net cash balance, requiring capital allocation discipline; the Mitsui Chemicals Ichihara phenol plant closure introducing raw material supply chain uncertainty; Kainol segment cyclicality tied to Chinese industrial demand; and the stock's rapid re-rating reducing the margin of safety for new entrants.

### Maruzen Petrochemical (4634.T) -- Advanced-Node Polymer Leader

**Founded:** 1959 | **HQ:** Tokyo (subsidiary of Cosmo Energy Holdings) | **Market Cap:** Not separately listed (consolidated subsidiary)

If Gun Ei Chemical dominates the novolac resin supply for mature lithography nodes, Maruzen Petrochemical occupies the complementary position in advanced-node polymers. Maruzen is the world's leading supplier of photoresist polymers for KrF, ArF, and EUV applications -- the chemically amplified resist platforms that define the frontier of semiconductor patterning.

Maruzen began manufacturing photoresist polymers in 1997, the same year that Shin-Etsu Chemical entered the photoresist business and JSR was developing its early ArF immersion materials. The timing was not coincidental: the late 1990s marked the industry's transition from i-line to DUV lithography, creating demand for an entirely new class of polymer chemistries -- polyhydroxystyrene for KrF, methacrylate copolymers and cyclic olefins for ArF -- that required different synthesis capabilities than the phenol-formaldehyde chemistry of novolac.

Maruzen's petrochemical heritage -- the company's core business is high-purity aromatics and ethylene from naphtha cracking -- provided a natural platform for synthesizing the aromatic and olefinic monomers needed for advanced resist polymers. Its Chiba refinery complex, part of the Cosmo Energy group, generates the ultra-pure chemical intermediates that flow into its specialty polymer division.

The company supplies photoresist polymers to both Tokyo Ohka Kogyo (CMP-0033) and JSR (CMP-0034) -- the two largest photoresist formulators in the world -- as confirmed by supply chain edge data. This positions Maruzen as a critical upstream node: if the formulators are the companies that semiconductor fabs interact with directly, Maruzen is the company that supplies the formulators with their most critical raw material for advanced-node applications.

As a consolidated subsidiary of Cosmo Energy Holdings, Maruzen Petrochemical does not trade independently and has no separately disclosed market capitalization, PER, or other public equity metrics. Its strategic importance to the photoresist supply chain is, however, disproportionate to its visibility. The evaluation framework assigns maximum scores on market share (10/10) and switching costs (5/5), reflecting the fact that photoresist base chemicals are purity-critical and qualification cycles at fabs make substitution prohibitively costly.

**Key Financials:** Not separately disclosed (consolidated within Cosmo Energy Holdings)

---

## Photoresist Formulators

### Tokyo Ohka Kogyo / TOK (4186.T) -- World's Largest Photoresist Manufacturer

**Founded:** 1940 | **HQ:** Kawasaki, Kanagawa Prefecture | **Market Cap:** 1.11 trillion yen

Tokyo Ohka Kogyo -- universally known as TOK -- is the world's number one photoresist manufacturer, with approximately twenty-five percent of the global market. The company supplies every category of photoresist from the oldest g-line formulations to the most advanced EUV materials, along with developers, thinners, and high-purity process chemicals. Over eighty percent of its sales are generated overseas, making TOK one of the most internationally oriented companies in the Japanese semiconductor materials sector.

TOK's history is inseparable from the history of photoresist itself. The company's OFPR-800 g-line resist, launched in 1979, became the global standard for DRAM patterning in the early 1980s and established Japan's dominance in photoresist that persists to this day. That product was built on Gun Ei Chemical's novolac resin and represented the kind of deep "suriawase" (mutual fine-tuning) collaboration between materials supplier and formulator that characterizes Japanese manufacturing relationships at their best. TOK holds a 1.87% equity stake in Gun Ei, reinforcing this foundational relationship.

In the EUV era, TOK holds approximately twenty-five percent of the global EUV photoresist market -- a position built through years of collaborative development with leading-edge fabs. The company's customer list includes TSMC, Samsung, Intel, and Kioxia, all confirmed through supply chain data. TOK's relationship with TSMC is particularly significant: TSMC's extraordinary process discipline requires resist suppliers who can deliver absolute consistency across billions of exposure events per year, and TOK has met this standard across multiple technology nodes.

TOK's competitive advantage lies not merely in the resist formulation but in the integrated chemical stack -- resist, developer, thinner, and rinse -- that is qualified as a system at each customer fab. Switching a single component in the stack requires requalification of the entire system, a process that typically takes twelve to eighteen months and consumes significant engineering resources at the fab. This systemic lock-in creates switching costs that far exceed those of any individual chemical product.

The company reported revenue of 237 billion yen in its latest fiscal year, with year-over-year growth of 17.9% driven by EUV resist demand and capacity expansion at major foundry customers. Operating margin stands at 17.0% -- a healthy level for a semiconductor materials company and above the G2 peer group median of 15.19%. Return on equity of 15.6% also exceeds the G2 median of 9.38%, reflecting efficient capital deployment in a high-value-added product category.

Foreign ownership of 37.5% is well above the Japanese market average, reflecting strong international institutional recognition of TOK's strategic position. All six covering analysts rate the stock a Buy, and at a PER of 24.7x, the stock trades at a modest premium to the G2 semiconductor materials median of 17.0x -- a premium justified by its global leadership position and above-peer-group growth rate.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 24.7x |
| EPS | 278.42 yen |
| Revenue | 237 billion yen (+17.9% YoY) |
| Operating Margin | 17.0% |
| ROE | 15.6% |
| Foreign Ownership | 37.5% |
| Evaluation Score | 47.8 / 100 |

### JSR Corporation (4185.T, delisted) -- EUV Photoresist Pioneer

**Founded:** 1957 | **HQ:** Tokyo | **Market Cap:** N/A (taken private by JIC in 2024)

JSR Corporation stands as the most consequential strategic move Japan has made in the photoresist space in a generation. In December 2024, JSR was taken private by the Japan Investment Corporation (JIC) -- the Japanese government's sovereign investment fund -- in a transaction valued at approximately 900 billion yen. The acquisition transformed a publicly traded specialty chemical company into a state-backed national champion in semiconductor materials.

JSR's photoresist credentials are formidable. The company holds the world's number one share in ArF photoresist -- the workhorse chemistry for the immersion lithography that dominates volume production at nodes from 7 nm to 28 nm. Its immersion lithography topcoats, which prevent water contamination of the resist during immersion exposure, were instrumental in making multi-patterning techniques viable at the 10 nm and 7 nm nodes. JSR's products are used in the production of roughly one third of all semiconductors manufactured worldwide, and the company received TSMC's Excellent Performance Award in 2022 -- an accolade reserved for the foundry's most critical and highest-performing suppliers.

What makes JSR's delisting strategically significant is the company's ownership of Inpria Corporation, a materials startup acquired in 2021 that develops metal-oxide EUV resists based on tin-oxo cluster chemistry. Metal-oxide resists represent a potential paradigm shift from chemically amplified organic resists: they absorb EUV photons far more efficiently, producing higher-contrast patterns with reduced line-edge roughness at a given dose. If metal-oxide resists become the standard at the 2 nm node and beyond -- an outcome that many industry observers consider likely -- JSR-Inpria will hold the foundational intellectual property for the dominant resist platform of the next decade.

JIC's acquisition of JSR was explicitly motivated by semiconductor supply chain security. The Japanese government recognized that JSR's photoresist technology is critical infrastructure -- too important to be subject to the vicissitudes of public market short-termism, hostile acquisition, or technology transfer pressure. By taking JSR private, JIC ensured that the company's R&D investments in EUV and next-generation resists would continue without quarterly earnings pressure, and that its intellectual property would remain under Japanese control.

JSR continues to supply TSMC, Samsung, and Intel as its anchor customers. As a private company, it no longer discloses financial metrics, and it was scored as "not applicable" in the evaluation framework for public equity investment purposes. But its role in the photoresist supply chain is undiminished, and in many respects, the JIC backing has strengthened its competitive position by removing capital constraints on long-cycle R&D.

**Key Financials:** Not available (private since December 2024)

### Sumitomo Chemical (4005.T) -- Photoresist via the Sumitomo Group

**Founded:** 1913 | **HQ:** Tokyo | **Market Cap:** 970.6 billion yen

Sumitomo Chemical is a major diversified chemical company -- one of Japan's largest, with annual revenue of 2.6 trillion yen -- that includes a significant photoresist business within its IT-related chemicals division. The company markets photoresists under the Sumilever brand, offering a full lineup from i-line through EUV, and supplies TSMC, Samsung, and Intel.

Sumitomo Chemical's scale provides advantages that pure-play resist makers cannot match: deep R&D budgets across multiple chemistry platforms, global production and distribution infrastructure, and the financial resilience to absorb the long qualification cycles and upfront investment required for new resist development. The company has committed 1 trillion yen in total semiconductor materials investment and is expanding its EUV resist production capacity, including a new evaluation facility at its Osaka plant scheduled for completion in 2025-2026.

However, the photoresist business is a relatively small component of Sumitomo Chemical's consolidated operations, and the company's overall financial profile reflects the challenges of its broader chemical portfolio. Revenue declined 10.2% year-over-year in the latest fiscal year, and operating margin stands at 3.45% -- well below the G2 semiconductor materials median of 15.19%. PBR of 0.76x reflects the market's tepid assessment of the broader business, though it could also be read as offering semiconductor materials exposure at a meaningful discount to pure-play valuations.

For investors, Sumitomo Chemical is a way to gain photoresist exposure within a larger, diversified chemical platform -- albeit one where the semiconductor segment's contribution to consolidated earnings is diluted by less attractive divisions. The company's connections to the Sumitomo Bakelite subsidiary provide additional semiconductor materials exposure through phenolic resins and epoxy molding compounds used in packaging.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 15.8x |
| PBR | 0.76x |
| EPS | 59.5 yen |
| Revenue | 2,606.3 billion yen (-10.2% YoY) |
| Operating Margin | 3.45% |
| ROE | 13.58% |
| Evaluation Score | 49.0 / 100 |

### FUJIFILM Holdings (4901.T) -- The Materials Platform

**Founded:** 1934 | **HQ:** Tokyo | **Market Cap:** 3.64 trillion yen

FUJIFILM's transformation from a photographic film company to a diversified technology and materials conglomerate is one of the most celebrated corporate reinventions of the past two decades. Within that reinvention, the company's semiconductor materials division has become a quietly powerful force in both photoresist and CMP slurry.

FUJIFILM is the world's number one supplier of copper CMP slurry -- the chemical mixture used to planarize copper interconnect layers in back-end-of-line processing. It also produces photoresists, developers, and process chemicals for semiconductor fabs, supplying TSMC, Samsung, and Intel. The company's approach to the semiconductor market is distinctive: where pure-play resist makers like TOK compete primarily on formulation excellence, FUJIFILM competes on breadth of platform. A fab that sources CMP slurry, photoresist, and process chemicals from a single supplier benefits from integrated supply chain management, combined shipping logistics, and the ability to negotiate across multiple product categories.

The company has set a target of 5 trillion yen in semiconductor-related sales by 2030, a figure that would make it one of the largest semiconductor materials suppliers in the world. Its development of PFAS-free ArF photoresist, announced in 2025, positions the company ahead of anticipated regulatory changes that could restrict the use of per- and polyfluoroalkyl substances in semiconductor manufacturing -- a proactive environmental strategy that could become a competitive advantage if PFAS regulations tighten globally.

FUJIFILM's approach to TSMC exemplifies what the company calls "ultimate customer service" -- embedding technical staff at customer sites to provide continuous process support and rapid problem resolution. This service model, combined with the breadth of its product portfolio, creates deep customer relationships that resist purely cost-based competition.

As a 3.64 trillion yen market cap company with revenue of 3.2 trillion yen, FUJIFILM's semiconductor business is one division among many -- healthcare, office solutions, and imaging also contribute significantly. PER of 15.43x and PBR of 1.16x reflect a valuation that the market assigns to the diversified whole, not specifically to the semiconductor materials opportunity. Foreign ownership of 30.0% indicates solid international institutional interest.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 15.43x |
| PBR | 1.16x |
| EPS | 226.2 yen |
| Revenue | 3,200 billion yen (+4.83% YoY) |
| Operating Margin | 9.29% |
| ROE | 7.87% |
| Foreign Ownership | 30.0% |
| Dividend Yield | 2.04% |
| Evaluation Score | 51.2 / 100 |

---

## Specialty Components

### Toyo Gosei (4970.T) -- The PAG Monopolist

**Founded:** 1954 | **HQ:** Tokyo | **Market Cap:** 49.5 billion yen

If the photoresist is the ink and the novolac resin is its backbone, the photoacid generator is its trigger. Toyo Gosei is the dominant global supplier of PAGs for chemically amplified photoresists, holding an estimated sixty to seventy percent of the world market for KrF and ArF photosensitive materials, with a similar or even higher share in EUV photoacid generators. In a supply chain already characterized by concentrated market positions, Toyo Gosei's PAG dominance stands out as one of the most critical single-source dependencies.

Toyo Gosei has been manufacturing photosensitive materials for semiconductor applications since 1997, coinciding with the industry's transition from novolac/DNQ to chemically amplified resist systems. The timing was strategic: as PAG chemistry became the rate-limiting component of advanced resist performance, Toyo Gosei invested in the synthesis capabilities and purity standards that allowed it to capture and hold a commanding market share across successive lithography generations.

The company's EUV photosensitive materials position is particularly significant. As EUV lithography moves from technology development to high-volume manufacturing -- driven by TSMC, Samsung, and Intel all ramping EUV-intensive nodes at 5 nm and below -- demand for EUV-optimized PAGs is growing rapidly. Toyo Gosei's supply chain edges confirm that it supplies photoresist materials to TSMC, Samsung, and Intel, positioning it as a direct supplier to the world's three largest EUV adopters.

The financial picture at Toyo Gosei requires careful interpretation. The company reported negative EPS of -84.79 yen and negative operating margin of -2.97% in its latest fiscal year, with ROE of -10.82%. Revenue of 41.5 billion yen grew 7.0% year-over-year, but the bottom line was depressed by what appear to be investment-phase costs associated with scaling EUV material production. The stock, trading at 4,635 yen against a 52-week range of 4,055 to 8,470 yen, sits near its lows -- a sharp contrast to the momentum seen in peer companies like Gun Ei Chemical.

Analyst coverage is notably bullish despite the current losses: all seven covering analysts rate Toyo Gosei a Buy, with an average target price of 7,131 yen -- representing over fifty percent upside from the current share price. This consensus reflects a market expectation that Toyo Gosei's losses are temporary and that the EUV scaling cycle will drive a significant earnings inflection as production volumes ramp.

The evaluation framework assigns Toyo Gosei a final score of 62.4 out of 100 (sixth highest overall), with the highest possible scores on market share (B1: 8/10) and strong scores on capacity expansion (E2: 3/3) and policy tailwinds (E3: 3/3). The absence of valuation data (negative earnings, no disclosed PBR) prevents full scoring on the valuation dimension.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | N/A (negative earnings) |
| EPS | -84.79 yen |
| Revenue | 41.5 billion yen (+7.0% YoY) |
| Operating Margin | -2.97% |
| 52-Week Range | 4,055 - 8,470 yen |
| Analyst Consensus | 7 Buy / 0 Hold / 0 Sell |
| Analyst Target | 7,131 yen |
| Evaluation Score | 62.4 / 100 |

---

## Distribution

### Nagase & Co. (8012.T) -- The Chemical Supply Chain Backbone

**Founded:** 1832 | **HQ:** Osaka | **Market Cap:** 456.2 billion yen

Nagase is a trading company that has operated continuously for 193 years -- one of Japan's oldest surviving businesses -- and has evolved from a dye merchant in Kyoto into the dominant distributor of electronic chemicals and materials for the semiconductor industry. Its role in the photoresist supply chain is not as a manufacturer but as the logistical and commercial infrastructure that connects Japanese chemical producers to global semiconductor fabs.

In the photoresist ecosystem, Nagase provides chemical distribution services to both Tokyo Ohka Kogyo and JSR, as confirmed by supply chain edge data. This means that when a TSMC fab in Taiwan or a Samsung fab in Korea orders photoresist, the physical delivery, storage, handling, and quality assurance of that material often passes through Nagase's distribution network. For ultra-high-purity semiconductor chemicals, distribution is not simply warehousing and trucking -- it requires contamination-controlled supply chains, specialized containers, temperature and humidity management, and chain-of-custody documentation that meets the stringent requirements of leading-edge fabs.

Beyond distribution, Nagase operates its own manufacturing capability through subsidiary Nagase ChemteX, which produces modified epoxy resins used in semiconductor packaging -- specifically for AI server applications, a segment growing rapidly with the expansion of large-language-model training infrastructure. This manufacturing arm adds proprietary value that distinguishes Nagase from a pure trading intermediary.

Nagase also supplies electronic chemicals directly to TSMC, as confirmed by supply chain data showing a direct supplier edge labeled "electronic chemicals." This direct relationship with the world's largest foundry underscores Nagase's role as more than a passive distributor -- it is a trusted chemical supply partner with the technical credibility to serve leading-edge fabs.

The company's financial profile reflects its trading-house model: revenue of 951 billion yen with a relatively thin operating margin of 3.0%, typical of distribution businesses where value creation comes from volume throughput and customer relationships rather than high per-unit margins. PER of 10.25x is well below the G2 semiconductor materials peer group median of 17.0x, though this reflects the market's standard discount for trading company business models. PBR of 1.09x is near book value.

Foreign ownership of 47.0% is remarkably high for a Japanese trading company of this size, suggesting strong international institutional recognition of Nagase's strategic position in the semiconductor materials supply chain. The dividend yield of 2.31% provides income appeal.

**Key Financials:**

| Metric | Value |
|--------|-------|
| PER | 10.25x |
| PBR | 1.09x |
| EPS | 270.17 yen |
| Revenue | 951 billion yen (+5.0% YoY) |
| Operating Margin | 3.0% |
| ROE | 6.23% |
| Foreign Ownership | 47.0% |
| Dividend Yield | 2.31% |
| Evaluation Score | 40.2 / 100 |

---

## Competitive Landscape

The photoresist market's competitive structure is unusual in the semiconductor supply chain: rather than a single dominant player, it features a Japanese oligopoly where five companies collectively control roughly ninety percent of global supply, with each player occupying partially overlapping but distinct niches.

**Resist Formulators:** TOK leads with approximately twenty-five percent global share, followed closely by JSR (now JIC-backed), with Shin-Etsu Chemical, Sumitomo Chemical, and FUJIFILM rounding out the top five. The American companies Dow and DuPont and the Korean company Dongjin Semichem represent the only meaningful non-Japanese participants, collectively holding less than ten percent of the global market. The competitive dynamic among the Japanese five is characterized by coopetition: they compete fiercely for qualification slots at each fab for each node, but they all depend on the same upstream Japanese suppliers for base polymers and PAGs.

**Upstream Polymers:** Gun Ei Chemical and Maruzen Petrochemical constitute a duopoly in photoresist base polymers, with Gun Ei dominant in novolac (g-line, i-line) and Maruzen leading in advanced-node polymers (KrF, ArF, EUV). Nippon Soda provides polyhydroxystyrene for certain KrF applications, but the duopoly holds the overwhelming majority of the market. Both companies benefit from the same switching cost structure that protects the resist formulators: once a polymer is qualified in a resist formulation, it is not changed.

**Photoacid Generators:** Toyo Gosei's sixty-to-seventy percent global share in PAGs creates the most concentrated position in the chemical stack. The only meaningful competitors in PAG synthesis are the resist formulators themselves (TOK and JSR maintain some in-house PAG capability) and a handful of specialty chemical producers in Japan and Korea. But Toyo Gosei's breadth -- PAGs for KrF, ArF, and EUV -- and its track record of maintaining purity standards across wavelength generations make it the default supplier.

**EUV-Specific Competition:** The EUV resist space is the most dynamic competitive frontier. JSR-Inpria's metal-oxide resist technology could potentially disrupt the chemically amplified resist platform that TOK, Sumitomo, and FUJIFILM have invested in. If metal-oxide resists become the dominant platform at the 2 nm node, JSR (backed by JIC resources) would gain a structural advantage that could shift market shares significantly. For now, both approaches coexist: chemically amplified EUV resists dominate volume production, while metal-oxide resists are in advanced qualification at multiple fabs.

**Distribution:** Nagase's position as the dominant electronic chemicals distributor is challenged primarily by other Japanese trading houses (Mitsui and Mitsubishi Chemical's distribution arms) and by direct-sales models where resist formulators deliver directly to their largest accounts. However, for the complex multi-product, multi-destination distribution that characterizes the semiconductor chemicals supply chain, Nagase's established network and contamination-controlled logistics represent a formidable competitive position.

---

## Supply Chain Connections

The photoresist supply chain forms a clearly layered structure that flows from upstream raw material suppliers through formulators and specialty component makers to the end-use semiconductor fabs. The edges mapped in the supply chain graph for this chapter's companies illustrate these connections with precision.

**Upstream to Formulators:**
- Gun Ei Chemical (CMP-0038) supplies photosensitive resin materials to TOK (CMP-0033), JSR (CMP-0034), Shin-Etsu Chemical (CMP-0024), FUJIFILM (CMP-0040), and Sumitomo Chemical (CMP-0046). Gun Ei is the most connected upstream node in the photoresist sub-graph, with five confirmed downstream edges.
- Maruzen Petrochemical (CMP-0035) supplies high-purity aromatics to TOK (CMP-0033) and JSR (CMP-0034), serving as the advanced-node polymer counterpart to Gun Ei's novolac supply.

**Formulators to Fabs:**
- TOK (CMP-0033) supplies photoresist to TSMC (CMP-0017), Samsung (CMP-0018), Intel (CMP-0019), and Kioxia (CMP-0014) -- four of the world's largest chip manufacturers. The TSMC edge is labeled "photoresist (25% world share)," reflecting TOK's market leadership.
- JSR (CMP-0034) supplies EUV photoresist to TSMC, Samsung, and Intel -- the three companies at the frontier of EUV adoption.
- Sumitomo Chemical (CMP-0046) supplies photoresist to TSMC (via Sumitomo Bakelite), Samsung, and Intel.
- FUJIFILM (CMP-0040) supplies CMP slurry and photoresist to TSMC, Samsung, and Intel. FUJIFILM's dual product supply (resist plus CMP slurry) makes it a uniquely broad materials supplier among the resist formulators.

**Specialty Components to Fabs:**
- Toyo Gosei (CMP-0010) supplies photoresist materials directly to TSMC, Samsung, and Intel. While Toyo Gosei primarily supplies PAGs to the resist formulators (who then sell the complete resist to fabs), the direct supply edges suggest that Toyo Gosei also provides certain photosensitive materials directly to fab customers.

**Distribution:**
- Nagase (CMP-0058) provides chemical distribution services to TOK (CMP-0033) and JSR (CMP-0034), and supplies electronic chemicals directly to TSMC (CMP-0017). Nagase serves as the logistical backbone connecting Japanese chemical producers to global fab operations.

**Cross-Chapter Connections:**
- This chapter connects upstream to Chapter 4 (Silicon Wafers) through Shin-Etsu Chemical, which is both a silicon wafer manufacturer and a photoresist producer -- and a customer of Gun Ei Chemical for its resist resin supply.
- Downstream, photoresist connects directly to Chapter 6 (Lithography) and Chapter 7 (Photomasks): the resist is coated onto the wafer, exposed through the photomask by the lithography system, and developed. The entire patterning sequence -- mask, scanner, resist, developer -- must be qualified as an integrated system.
- FUJIFILM bridges this chapter and Chapter 11 (CMP Planarization) through its dual position as a photoresist formulator and the world's number one copper CMP slurry supplier.
- Nagase bridges this chapter and Chapter 12 (Fab Infrastructure) through its broader role as an electronic chemicals distributor serving the entire fab ecosystem.

---

## Key Takeaways

- **Japan's photoresist monopoly is comprehensive.** Five Japanese companies control approximately ninety percent of the global photoresist market. This dominance extends from raw material supply (Gun Ei, Maruzen) through formulation (TOK, JSR, Sumitomo, FUJIFILM) to specialty components (Toyo Gosei) and distribution (Nagase). No other segment of the semiconductor supply chain exhibits this degree of single-country concentration across every layer of the value chain.

- **Switching costs are measured in years, not months.** Photoresist qualification at a leading-edge fab requires twelve to eighteen months and involves the complete resist-developer-rinse stack. Once qualified, suppliers are locked in for the life of the technology node. This creates recurring revenue streams with near-zero customer churn and insulates incumbent Japanese suppliers from price-based competition.

- **The upstream duopoly is the hidden chokepoint.** While resist formulators like TOK and JSR receive the attention, the upstream resin suppliers -- Gun Ei Chemical and Maruzen Petrochemical -- represent the true bottleneck. If either company experienced a factory disruption, every major photoresist formulator on earth would be affected. Gun Ei's 3.5 billion yen capacity expansion is a direct response to this strategic criticality.

- **EUV is reshaping the competitive landscape.** JSR's acquisition by JIC and its ownership of Inpria's metal-oxide resist technology represents a deliberate Japanese government bet on next-generation photoresist. If metal-oxide resists displace chemically amplified resists at the 2 nm node, JSR-Inpria will control the foundational platform. Meanwhile, Toyo Gosei's PAG dominance ensures that even within the chemically amplified EUV approach, Japan holds the critical specialty component position.

- **Gun Ei Chemical is the book's highest-conviction investment thesis.** At a score of 78.9 out of 100, Gun Ei combines a structural duopoly moat, PBR of 0.64x with fortress-like net cash representing twenty-two percent of market cap, capacity expansion timed to the AI semiconductor capex wave, and foreign ownership of just 3.6% that implies massive international re-rating potential. It is the archetype of the book's central thesis: an invisible, indispensable Japanese company trading at a valuation that does not reflect its strategic importance.

---

*Data sources: CMP-0033 (Tokyo Ohka Kogyo), CMP-0034 (JSR), CMP-0038 (Gun Ei Chemical), CMP-0010 (Toyo Gosei), CMP-0035 (Maruzen Petrochemical), CMP-0046 (Sumitomo Chemical), CMP-0040 (FUJIFILM Holdings), CMP-0058 (Nagase), graph.json (supply chain edges), evaluation_progress.json (scores and investment theses)*
