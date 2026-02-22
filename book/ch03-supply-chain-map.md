# Chapter 3: The Supply Chain Map

> The semiconductor supply chain is not a simple linear chain but a dense, multi-layered network -- and when you map it, Japan's centrality becomes unmistakable.

## Introduction

If Chapter 2 described how a chip is made, this chapter answers a different question: *who* makes it possible? The semiconductor industry is often described as a "supply chain," a phrase that conjures an image of a neat sequence -- raw materials enter at one end, finished chips emerge at the other. This mental model is dangerously incomplete.

The reality is a network. A dense, multi-layered, interlocking web of companies supplying companies supplying companies, where a single firm in Osaka can be a critical vendor to a dozen factories on three continents simultaneously. Where a mid-cap chemical company with 200 employees can be the sole global source of a molecule without which no advanced chip can be printed. Where the same Japanese equipment maker sells to TSMC in Hsinchu, Samsung in Pyeongtaek, and SMIC in Shanghai -- and also competes with domestic alternatives in each of those countries.

This chapter presents the supply chain graph that underpins the rest of this book. It is based on a database of 110 companies connected by 321 documented relationships. Think of it as the map legend: every subsequent chapter will zoom into one section of this network, exploring individual companies and process steps in detail. But before we zoom in, we need to see the full picture. The patterns that emerge from this graph -- Japan's extraordinary centrality, the asymmetric dependency of the world's largest chipmakers on Japanese suppliers, the chokepoint positions that give small companies outsized strategic importance -- are the structural thesis of this book.

---

## The Graph at a Glance

The supply chain graph contains **110 companies** (nodes) connected by **321 relationships** (edges). Each node represents a company with a defined role in semiconductor manufacturing -- a foundry, an equipment maker, a materials supplier, an outsourced assembly and test house (OSAT), or an end customer. Each edge represents a documented relationship between two companies.

The 321 edges are classified into four types:

| Edge Type | Count | Description |
|-----------|-------|-------------|
| **Supplier** | 263 | Company A provides products or services to Company B |
| **Competitor** | 42 | Companies competing in the same product category |
| **Ecosystem** | 12 | Complementary relationships -- co-dependent products, parent-subsidiary ties |
| **Partner** | 4 | Joint ventures and strategic co-development agreements |

The dominance of supplier edges (82% of the total) reflects the fundamental nature of the semiconductor industry: it is a supply-chain business. Chipmakers do not mine their own silicon, formulate their own chemicals, or build their own equipment. They buy from specialists. And as we will see, those specialists are overwhelmingly Japanese.

The 110 companies span **eight countries**:

| Country | Companies | Share |
|---------|-----------|-------|
| Japan | 53 | 48.2% |
| China | 20 | 18.2% |
| South Korea | 16 | 14.5% |
| Taiwan | 9 | 8.2% |
| USA | 6 | 5.5% |
| Malaysia | 3 | 2.7% |
| Singapore | 2 | 1.8% |
| Netherlands | 1 | 0.9% |

Japan accounts for nearly half of all companies in the graph -- and as we will demonstrate, its share of critical supply relationships is even larger than its share of nodes.

---

## Nodes by Country and Industry

### Japan: 53 Companies -- The Supply Side

Japan's 53 companies divide neatly into two major clusters: **semiconductor equipment** (25 companies) and **semiconductor materials** (24 companies), plus a handful in components, memory, and precision instruments. This dual concentration -- equipment and materials -- is the structural foundation of Japan's supply chain dominance. No other country has critical mass in both.

**Equipment makers** span the full spectrum of the chip manufacturing process:

| Company | Ticker | Core Products |
|---------|--------|---------------|
| Tokyo Electron (TEL) | 8035.T | Coater/developers, etch systems, CVD, cleaning |
| SCREEN Holdings | 7735.T | Wet cleaning systems |
| Advantest | 6857.T | Semiconductor testers |
| Lasertec | 6920.T | EUV mask inspection (near-100% global share) |
| DISCO | 6146.T | Dicing saws and grinders (70%+ global share) |
| Tokyo Seimitsu (ACCRETECH) | 7729.T | Probers (#1 global, 46% share), dicing, CMP |
| Kokusai Electric | 6525.T | Batch CVD/ALD deposition |
| Ebara | 6361.T | CMP systems, vacuum pumps |
| Rorze | 6323.T | Wafer transfer robots |
| Daifuku | 6383.T | Automated material handling systems (AMHS) |
| Nikon | 7731.T | i-line/KrF lithography steppers |
| Canon | 7751.T | Lithography, nanoimprint |
| Horiba | 6856.T | Gas/chemical analysis, mass flow controllers |
| PILLAR | 6490.T | Fluororesin fittings (90%+ global share) |
| CKD | 6407.T | Pneumatic valves for process equipment |
| Shibaura Mechatronics | 6590.T | Plasma processing, cleaning equipment |
| Samco | 6387.T | Plasma CVD, dry etching |
| Tazmo | 6266.T | Coater/developer systems |
| Organo | 6368.T | Ultrapure water systems |
| Nomura Micro Science | 6254.T | Ultrapure water systems |
| Ushio | 6925.T | UV light sources (75% share in i-line lamps) |
| Aval Data | 6918.T | Tester boards, image processing for equipment |
| NHK Spring | 5991.T | Probe card springs, HDD suspensions |
| Naigai Tech | 3374.T | Precision machined parts for TEL |
| Marumae | 6264.T | Aluminum vacuum chambers |

**Materials companies** supply the chemicals, substrates, and consumables that physically become part of the chip -- or that enable its manufacture:

| Company | Ticker | Core Products |
|---------|--------|---------------|
| Shin-Etsu Chemical | 4063.T | Silicon wafers, photoresist, PVC |
| SUMCO | 3436.T | Silicon wafers |
| Tokyo Ohka Kogyo (TOK) | 4186.T | Photoresist (25% world share) |
| JSR | 4185.T | EUV photoresist, CMP slurry |
| HOYA | 7741.T | Photomask blanks (EUV monopoly) |
| Fujimi | 5384.T | CMP slurry |
| Fuso Chemical | 4368.T | Colloidal silica CMP slurry |
| Resonac Holdings | 4004.T | Die-attach films, encapsulants, CMP slurry |
| FUJIFILM Holdings | 4901.T | CMP slurry, photoresist, process chemicals |
| Sumitomo Chemical | 4005.T | Photoresist |
| Toyo Gosei | 4970.T | Photoacid generators (PAGs) for EUV resist |
| Gun Ei Chemical | 4229.T | Novolac resins for photoresist |
| Maruzen Petrochemical | 4634.T | High-purity aromatic solvents |
| Stella Chemifa | 4109.T | Ultra-high purity hydrofluoric acid |
| Kanto Denka Kogyo | 4047.T | Specialty fluorine gases |
| Nippon Sanso | 4091.T | Specialty and bulk gases |
| NGK Insulators | 5333.T | Ceramic electrostatic chucks |
| Tocalo | 3433.T | Thermal spray coatings for equipment parts |
| Ibiden | 4062.T | FC-BGA IC substrates (50%+ of NVIDIA AI substrates) |
| MEC Company | 4971.T | Copper surface treatment chemicals |
| Nagase | 8012.T | Chemical distribution |
| TOPPAN Holdings | 7911.T | Photomasks, EUV mask production |
| Dai Nippon Printing (DNP) | 7912.T | Photomasks, nanoimprint templates |
| Ferrotec Holdings | 6890.T | Silicon crystal growth, quartz crucibles |

Plus **Kyocera** (6971.T, semiconductor ceramic packages/components), **Niterra** (5334.T, IC package substrates), **Olympus** (7733.T, precision measurement/microscopy), and **Kioxia** (285A.T, NAND flash memory).

The breadth is striking. Japan has companies in silicon wafer production, photoresist formulation, photomask manufacturing, deposition equipment, etch and clean systems, CMP equipment and consumables, lithography (mature nodes), wafer probing, dicing, gas supply, water purification, material handling, and IC packaging substrates. There is no major step in chip manufacturing where Japan is absent.

### Taiwan: 9 Companies -- Fabrication and Assembly

Taiwan's nine entries center on the world's dominant foundry ecosystem:

| Company | Role |
|---------|------|
| **TSMC** (2330.TW) | World #1 foundry, 71% global share, 90%+ of advanced chips |
| UMC (2303.TW) | #2 Taiwan foundry, mature/specialty nodes |
| Vanguard (5347.TWO) | Specialty foundry (power, analog) |
| ASE Technology (3711.TW) | World #1 OSAT |
| Powertech Technology (6239.TW) | Memory OSAT, key Micron supplier |
| King Yuan (KYEC) (2449.TW) | World #1 pure-play testing house |
| Chipbond (6147.TWO) | Driver IC packaging specialist |
| ChipMOS (8150.TW) | Memory and logic OSAT |
| MPI Corporation (6223.TW) | Probing equipment, competitor to Tokyo Seimitsu |

Taiwan's companies sit at the center of the graph as *consumers* of equipment and materials. TSMC alone has 40 incoming supplier edges -- more than any other node in the network.

### South Korea: 16 Companies -- Memory, Foundry, and Domestic Ecosystem

South Korea fields a diverse set of companies spanning IDMs, OSATs, and a growing domestic equipment sector:

| Segment | Companies |
|---------|-----------|
| **IDM/Foundry** | Samsung Electronics (005930.KS), SK Hynix (000660.KS), DB HiTek (000990.KS) |
| **OSAT** | HANA Micron (067310.KQ), Nepes (033640.KQ), SFA Semicon (036540.KQ), LB Semicon (061970.KQ) |
| **Equipment** | SEMES (Samsung captive), SEMICS (prober, world #3), WONIK IPS (240810.KQ, deposition), Hanmi Semiconductor (042700.KS, TC bonders), Techwing (089030.KQ, test handlers), KCTech (281820.KS, CMP), EO Technics (039030.KQ, laser dicing), SurplusGLOBAL (140070.KQ, refurbished equipment) |
| **Components** | Leeno Industrial (058470.KQ, test probes) |

South Korea's graph position is distinctive: it is both a major buyer of Japanese equipment and materials (through Samsung and SK Hynix) and a developing domestic supply chain that aims to reduce that dependency. SEMES, a Samsung subsidiary, competes with Tokyo Seimitsu in probing. KCTech competes with Ebara and Tokyo Seimitsu in CMP. WONIK IPS competes with Tokyo Electron and Kokusai Electric in deposition. These competitive edges are significant -- they represent active localization efforts by Korea's semiconductor giants.

### USA: 6 Companies -- Design, Memory, and End Markets

| Company | Role |
|---------|------|
| **Intel** (INTC) | IDM, foundry (Intel Foundry Services) |
| **Micron** (MU) | Memory (DRAM, NAND) |
| **NVIDIA** (NVDA) | GPU/AI chip design (fabless) |
| **Apple** (AAPL) | Chip design (fabless), TSMC's largest customer |
| **Western Digital** (WDC) | NAND flash (Kioxia JV partner) |
| **Amkor Technology** (AMKR) | #2 global OSAT |

The American companies in the graph are primarily *demand-side* nodes -- they consume chips (Apple, NVIDIA) or manufacture them using Japanese equipment and materials (Intel, Micron). The notable exception is Amkor, which provides packaging and test services. The absence of American equipment companies from this particular graph is not because they do not exist -- Applied Materials, Lam Research, and KLA are major players -- but because the graph is constructed from the perspective of Japanese supply chain relationships. American equipment makers are complementary rather than competitive to most of the Japanese companies covered here.

### China: 20 Companies -- Foundries, OSATs, and Domestic Substitution

China's 20 entries represent the world's most active effort at semiconductor supply chain localization:

| Segment | Companies |
|---------|-----------|
| **Foundries** | SMIC (0981.HK), Hua Hong (1347.HK), Nexchip (688249.SS), CanSemi, GTA Semiconductor |
| **Memory** | YMTC (Yangtze Memory Technologies) |
| **IDM** | China Resources Microelectronics (688396.SS), GigaDevice (603986.SS) |
| **Equipment** | NAURA (002371.SZ), Hwatsing/Huahai Qingke (688120.SS, CMP), Hangzhou Changchuan (300604.SZ, probers), Sidea (301629.SZ, probers), Guangli (300480.SZ, dicing), Shenyang Heyan (dicing), Beijing Shuoke Jingwei (CMP), Beijing TSD (CMP/grinding) |
| **OSAT** | JCET (600584.SS), Tongfu (002156.SZ), Tianshui Huatian (002185.SZ) |

China's position in the graph is dual: its foundries and memory companies are *clients* of Japanese equipment and materials suppliers (SMIC and Hua Hong both receive supplier edges from Tokyo Seimitsu, Tokyo Electron, PILLAR, Organo, and Stella Chemifa), while its domestic equipment companies appear as *competitors* to Japanese incumbents. NAURA competes with Tokyo Seimitsu in CMP and probing. Huahai Qingke competes in CMP. Changchuan competes in probing. Sidea competes in probing. Guangli and Shenyang Heyan compete in dicing. These 42 competitor edges in the graph tell the story of a tug-of-war between Japanese incumbency and Chinese localization.

### Netherlands: 1 Company -- But What a Company

ASML (ASML) is the sole Dutch entry in the graph. It is also the most valuable semiconductor equipment company on earth, with a market capitalization exceeding $560 billion. ASML's monopoly on EUV lithography systems -- machines that cost over $350 million each -- makes it arguably the single most critical node in the global semiconductor supply chain. Every chipmaker manufacturing at 7nm or below depends on ASML.

In our graph, ASML has 21 edges: 8 supplier edges (providing lithography equipment to TSMC, Samsung, Intel, SK Hynix, Micron, SMIC, UMC, and GlobalFoundries), 4 competitor edges (with Nikon and Canon), and 9 ecosystem edges (with Lasertec, HOYA, Toppan, and DNP -- companies whose products are co-dependent with ASML's lithography systems).

### Singapore: 2 Companies

| Company | Role |
|---------|------|
| GlobalFoundries (GFS) | World #3 foundry (mature/specialty nodes) |
| UTAC Holdings | OSAT |

### Malaysia: 3 Companies

| Company | Role |
|---------|------|
| Inari Amertron (0166.KL) | Malaysia's #1 OSAT, RF/optoelectronic packaging |
| Unisem (5005.KL) | OSAT, subsidiary of China's Tianshui Huatian |
| Malaysian Pacific Industries (MPI) (3867.KL) | OSAT, automotive/industrial |

Malaysia's three companies are all OSATs -- back-end assembly and test houses. They receive dicing and probing equipment from both Tokyo Seimitsu and DISCO, placing them firmly downstream of Japanese suppliers.

---

## Edge Types Explained

The 321 edges in the graph represent four distinct types of inter-company relationships. Understanding these types is essential for reading the supply chain map correctly.

### Supplier Edges (263): The Backbone of the Network

A supplier edge means that Company A provides a product, material, or service to Company B. This is the most common and most economically significant relationship type. Supplier edges are directional: they flow from the supplier to the customer.

Examples from the graph, with their labels:

| Source | Target | Label |
|--------|--------|-------|
| Shin-Etsu Chemical (CMP-0024) | TSMC (CMP-0017) | silicon wafers |
| SUMCO (CMP-0025) | TSMC (CMP-0017) | silicon wafers |
| Tokyo Electron (CMP-0004) | TSMC (CMP-0017) | coater/developers, etch, CVD |
| SCREEN Holdings (CMP-0003) | TSMC (CMP-0017) | wafer cleaning |
| Fujimi (CMP-0007) | TSMC (CMP-0017) | CMP slurry |
| Fuso Chemical (CMP-0013) | TSMC (CMP-0017) | CMP slurry |
| HOYA (CMP-0015) | TSMC (CMP-0017) | photomask blanks |
| ASML (CMP-0026) | TSMC (CMP-0017) | EUV lithography |
| Lasertec (CMP-0006) | Samsung (CMP-0018) | EUV mask inspection |
| Stella Chemifa (CMP-0044) | TSMC (CMP-0017) | 12-nine purity HF acid |
| Tokyo Ohka Kogyo (CMP-0033) | TSMC (CMP-0017) | photoresist (25% world share) |
| Ibiden (CMP-0048) | NVIDIA (CMP-0028) | AI server IC substrates (50%+) |
| Naigai Tech (CMP-0029) | Tokyo Electron (CMP-0004) | precision machining parts (80% sales) |
| PILLAR (CMP-0042) | SCREEN Holdings (CMP-0003) | mechanical seals, bellows |
| Daifuku (CMP-0056) | Intel (CMP-0019) | cleanroom AMHS |
| Organo (CMP-0052) | TSMC (CMP-0017) | ultrapure water systems |

Supplier edges form cascades. Gun Ei Chemical (CMP-0038) supplies novolac resins to TOK (CMP-0033) and JSR (CMP-0034), who formulate photoresist and sell it to TSMC (CMP-0017), Samsung (CMP-0018), and Intel (CMP-0019). Maruzen Petrochemical (CMP-0035) supplies high-purity aromatic solvents to the same resist makers. A disruption at Gun Ei or Maruzen would ripple forward through TOK and JSR to every leading-edge fab in the world.

Similarly, PILLAR (CMP-0042) supplies fluororesin fittings to SCREEN (CMP-0003), Tokyo Electron (CMP-0004), Ebara (CMP-0036), Kokusai Electric (CMP-0011), CKD (CMP-0043), Shibaura Mechatronics (CMP-0059), and Samco (CMP-0060) -- essentially every Japanese equipment maker that handles corrosive chemicals. PILLAR also sells directly to TSMC, Samsung, Intel, SK Hynix, SMIC, Hua Hong, and SEMES for maintenance and replacement parts. This dual role -- supplier to equipment makers *and* supplier to fabs -- gives PILLAR 14 outgoing supplier edges, tied for second among all companies in the graph.

### Competitor Edges (42): The Battle Lines

A competitor edge indicates that two companies compete in the same product category. These edges are always bidirectional: if A competes with B, then B competes with A. The 42 competitor edges therefore represent 21 unique competitive relationships.

Key competitive battlegrounds in the graph:

| Product Category | Competitors |
|-----------------|-------------|
| **Dicing equipment** | Tokyo Seimitsu vs DISCO (the 90/10 duopoly), plus Guangli (China), Shenyang Heyan (China), EO Technics (Korea, laser approach) |
| **Probing equipment** | Tokyo Seimitsu vs MPI Corporation (Taiwan), SEMES (Korea, Samsung captive), SEMICS (Korea), Sidea (China), NAURA (China), Hangzhou Changchuan (China) |
| **CMP equipment** | Tokyo Seimitsu vs Huahai Qingke (China), Beijing Shuoke Jingwei (China), Beijing TSD (China) |
| **Lithography** | ASML vs Nikon vs Canon |
| **Memory** | Samsung vs SK Hynix vs Micron |
| **OSAT services** | ASE vs Amkor vs JCET |
| **Silicon wafers** | Shin-Etsu vs SUMCO |

The competitor edges reveal a striking asymmetry. Tokyo Seimitsu alone participates in 30 of the 42 competitor edges (as either source or target), reflecting its position as the most contested Japanese equipment maker. The reason is structural: Tokyo Seimitsu competes in three overlapping product categories (probing, dicing, CMP), and in each category it faces competitors from multiple countries. The company is simultaneously fighting battles in Japan (vs DISCO), Taiwan (vs MPI), South Korea (vs SEMES, SEMICS, Hanmi, EO Technics), and China (vs Sidea, Guangli, Heyan, NAURA, Huahai Qingke, Shuoke Jingwei, TSD, Changchuan).

By contrast, Lasertec has zero competitor edges. It faces no documented competitor in EUV mask inspection. PILLAR also has zero competitor edges within the graph's scope. These absences are as informative as the presences -- they signal monopoly positions.

### Partner Edges (4): Strategic Alliances

Partner edges represent joint ventures and formal co-development agreements. Only four exist in the graph, reflecting the rarity of deep strategic partnerships in an industry where companies guard proprietary technology fiercely.

| Partners | Label |
|----------|-------|
| Kioxia (CMP-0014) -- Western Digital (CMP-0023) | Yokkaichi/Kitakami JV (bidirectional) |
| Tokyo Seimitsu (CMP-0001) -- Advantest (CMP-0005) | Die-level prober joint development, announced 2025 (bidirectional) |

The Kioxia-Western Digital partnership is one of the semiconductor industry's most enduring joint ventures. The two companies jointly operate NAND flash memory fabs in Yokkaichi and Kitakami, Japan, sharing capital expenditure and technology development while competing in the market with separate brands.

The Tokyo Seimitsu-Advantest partnership, announced in December 2025, is more recent and more targeted: the two companies are jointly developing die-level probers for AI and HPC chips. This partnership merges Tokyo Seimitsu's world-leading prober hardware (46% global share) with Advantest's tester platforms, addressing the growing need to test individual chiplets before they are assembled into multi-chip packages.

### Ecosystem Edges (12): Co-Dependence

Ecosystem edges describe relationships that are neither simple supply nor competition, but complementary co-dependence. They include parent-subsidiary relationships, cross-investment ties, and technical co-dependencies where two companies' products must work together.

| Companies | Label |
|-----------|-------|
| Lasertec (CMP-0006) -- ASML (CMP-0026) | EUV inspection + lithography (bidirectional) |
| HOYA (CMP-0015) -- ASML (CMP-0026) | EUV blanks + lithography (bidirectional) |
| TOPPAN (CMP-0047) -- ASML (CMP-0026) | EUV photomask production + lithography (bidirectional) |
| DNP (CMP-0049) -- ASML (CMP-0026) | Nanoimprint partnership (bidirectional) |
| SMIC (CMP-0066) -- JCET (CMP-0065) | SMIC is JCET's 2nd largest shareholder / JCET packages SMIC chips (bidirectional) |
| Tianshui Huatian (CMP-0068) -- Unisem (CMP-0109) | Huatian parent of Unisem Malaysia (bidirectional) |

The cluster of ecosystem edges around ASML is particularly revealing. ASML's EUV lithography system does not function in isolation -- it requires EUV photomask blanks (from HOYA, the sole supplier), EUV mask inspection systems (from Lasertec, the sole supplier), and photomask production capability (from Toppan and DNP). This quartet -- ASML, HOYA, Lasertec, Toppan/DNP -- forms what might be called the "EUV ecosystem," and three of its four members are Japanese. When an analyst evaluates ASML, they are implicitly evaluating HOYA and Lasertec as well. The ecosystem edges in the graph make this co-dependence explicit.

---

## Japan's Centrality -- By the Numbers

The statistics above hint at Japan's structural importance, but a deeper analysis of the graph's topology makes the case conclusive.

### Who Supplies the World's Chipmakers?

Of the 263 supplier edges in the graph, **226 originate from Japanese companies** -- that is, 86% of all documented supplier relationships flow from Japan outward. The remaining 40 supplier edges originate from South Korea (primarily SEMES, SEMICS, WONIK, Techwing, KCTech, Hanmi, and EO Technics supplying Samsung and SK Hynix), from ASML (Netherlands), from a handful of Chinese domestic suppliers to Chinese fabs, and from Taiwan-based OSATs.

This 86% figure is the single most important number in this book. It means that for every ten documented supply relationships in the semiconductor industry as mapped here, more than eight begin in Japan.

### TSMC's Japanese Dependency

TSMC (CMP-0017) -- the world's largest and most important semiconductor foundry, responsible for manufacturing chips for Apple, NVIDIA, AMD, Qualcomm, and dozens of other companies -- has **40 incoming supplier edges** in the graph. Of those 40, **38 originate from Japanese companies**. The only non-Japanese suppliers feeding TSMC in this graph are ASML (Netherlands, EUV lithography) and Leeno Industrial (South Korea, test probes).

The 38 Japanese suppliers to TSMC span the entire chip manufacturing process:

- **Wafers**: Shin-Etsu Chemical, SUMCO
- **Equipment**: Tokyo Electron (coater/developer, etch, CVD), SCREEN Holdings (cleaning), Advantest (testing), Lasertec (EUV mask inspection), Tokyo Seimitsu (probing, dicing, CMP), Ebara (CMP systems, vacuum pumps), Rorze (wafer handling), Daifuku (AMHS), Nikon (i-line/KrF steppers), Canon (i-line/KrF steppers), Shibaura Mechatronics (plasma processing), Samco (plasma CVD), Tazmo (coater/developer), PILLAR (fluororesin fittings), Organo (ultrapure water), Nomura Micro Science (ultrapure water)
- **Materials and chemicals**: Fujimi (CMP slurry), Fuso Chemical (CMP slurry), HOYA (photomask blanks), Toyo Gosei (photoresist materials), Resonac (semiconductor materials), Nippon Sanso (specialty gases), TOK (photoresist), JSR (EUV photoresist), FUJIFILM (CMP slurry, photoresist), Sumitomo Chemical (photoresist), Stella Chemifa (HF acid), Kanto Denka Kogyo (fluorine gases), Nagase (electronic chemicals), MEC Company (PCB surface treatment)
- **Substrates and packaging**: NGK Insulators (ceramic chucks), Niterra (IC package substrates), Ibiden (FC-BGA substrates), TOPPAN (photomasks), DNP (photomasks)
- **Subsystems**: NHK Spring (HDD suspension)

TSMC itself has noted that 13 Japanese companies appear in its top 30 suppliers. Our graph captures a broader set, including second- and third-tier suppliers that TSMC may not directly procure from but whose products are embedded in the equipment and materials it uses.

### Samsung's Japanese Dependency

Samsung Electronics (CMP-0018) presents a similar picture. It has **44 incoming supplier edges** -- the most of any node in the graph. Of those 44, **34 originate from Japanese companies** (77%). The remaining 10 come from South Korean domestic suppliers (SEMES, SEMICS, WONIK IPS, Techwing, KCTech, EO Technics, HANA Micron, SFA Semicon, Leeno Industrial) and ASML.

Samsung's position is slightly different from TSMC's in that it has a more developed domestic equipment ecosystem. SEMES, a Samsung subsidiary, provides probers, photo track systems, and cleaning equipment. WONIK IPS supplies deposition equipment. KCTech provides CMP systems. These Korean suppliers represent a deliberate strategy by Samsung to reduce dependency on Japanese vendors -- a strategy that has been partially successful but has not dislodged Japanese companies from the most critical positions. Samsung still depends on Shin-Etsu and SUMCO for wafers, TOK and JSR for photoresist, Lasertec for EUV mask inspection, HOYA for photomask blanks, and Stella Chemifa for ultra-high purity HF.

### Intel, SK Hynix, and Micron

The pattern repeats for every major chipmaker:

| Chipmaker | Total Incoming Supplier Edges | From Japan | Japan Share |
|-----------|-------------------------------|------------|-------------|
| TSMC | 40 | 38 | 95% |
| Samsung | 44 | 34 | 77% |
| Intel | 27 | 24+ | ~89% |
| SK Hynix | 22 | 17+ | ~77% |
| Micron | 12 | 10+ | ~83% |

Even SK Hynix, which alongside Samsung benefits from Korea's domestic equipment initiatives, relies on Japanese companies for the majority of its supply relationships. Shin-Etsu and SUMCO supply its silicon wafers. Tokyo Electron provides deposition equipment. Advantest supplies testers. Kokusai Electric provides batch deposition. HOYA provides photomask blanks. Stella Chemifa supplies ultra-high purity HF. Nippon Sanso supplies specialty gases. Ebara provides CMP systems and vacuum pumps. Nomura Micro Science supplies ultrapure water systems. PILLAR provides fluororesin fittings.

### The Most-Connected Nodes

Ranking companies by total edge count (both incoming and outgoing, across all edge types) reveals the structural hubs of the network:

| Rank | Company | Country | Total Edges | Role |
|------|---------|---------|-------------|------|
| 1 | Tokyo Seimitsu | Japan | 65 | Prober/dicer/CMP supplier + multi-front competitor |
| 2 | Samsung Electronics | South Korea | 46 | Major buyer + competitor |
| 3 | TSMC | Taiwan | 42 | The world's largest equipment/materials buyer |
| 4 | Intel | USA | 27 | IDM/foundry buyer |
| 5 | SK Hynix | South Korea | 22 | Memory IDM buyer |
| 6 | ASML | Netherlands | 21 | Lithography monopolist + EUV ecosystem hub |
| 7 | Tokyo Electron | Japan | 20 | Equipment supplier to all major fabs |
| 8 | DISCO | Japan | 20 | Dicing monopolist supplying all OSAT/fabs |
| 9 | PILLAR | Japan | 14 | Fluororesin fitting monopolist |
| 10 | Micron | USA | 12 | Memory IDM buyer |
| 11 | SMIC | China | 12 | China's #1 foundry buyer |
| 12 | Advantest | Japan | 11 | Tester supplier + partner |
| 13 | Stella Chemifa | Japan | 10 | HF acid supplier to all major fabs |
| 14 | Shin-Etsu Chemical | Japan | 8 | Wafer duopoly |
| 15 | HOYA | Japan | 8 | EUV blank monopolist + ecosystem |

The top-ranked node is not TSMC or Samsung -- it is **Tokyo Seimitsu**, a Japanese equipment maker with a market capitalization of approximately 562 billion yen. Tokyo Seimitsu's 65 edges reflect its extraordinary reach: it supplies probing, dicing, and CMP equipment to 35 companies across all major semiconductor-producing regions, while simultaneously competing with 15 companies in multiple product categories, and partnering with Advantest on next-generation prober development.

Among the top 15 most-connected nodes, 8 are Japanese. More importantly, the Japanese nodes are overwhelmingly *suppliers* (outgoing edges), while the non-Japanese nodes are overwhelmingly *buyers* (incoming edges). This asymmetry is the graph-theoretic expression of Japan's structural position: Japan supplies; the rest of the world buys.

### Top Suppliers by Outgoing Edges

Ranking companies by outgoing supplier edges (i.e., how many customers they supply) reveals the network's most prolific suppliers:

| Rank | Company | Country | Outgoing Supplier Edges |
|------|---------|---------|------------------------|
| 1 | Tokyo Seimitsu | Japan | 35 |
| 2 | PILLAR | Japan | 14 |
| 3 | DISCO | Japan | 14 |
| 4 | Tokyo Electron | Japan | 11 |
| 5 | Stella Chemifa | Japan | 10 |
| 6 | ASML | Netherlands | 8 |
| 7 | Advantest | Japan | 7 |
| 8 | HOYA | Japan | 6 |
| 9 | Kokusai Electric | Japan | 6 |
| 10 | Shin-Etsu Chemical | Japan | 5 |

Nine of the top ten suppliers by customer reach are Japanese. The sole exception is ASML. This list is a roster of companies that, if disrupted, would cause cascading failures across the global semiconductor supply chain.

---

## The Five Chokepoint Categories

Not all Japanese companies are equally critical. Some could theoretically be replaced by alternatives; others occupy positions so narrow and so deeply entrenched that substitution would take years -- if it is possible at all. We can organize Japan's supply chain positions into five categories of increasing replaceability.

### 1. Sole-Source Monopolies

These companies are the only supplier in the world for a specific product. There is no backup.

**Lasertec** (6920.T) -- *EUV mask inspection*. Lasertec holds near-100% global market share in EUV actinic patterned mask inspection systems. Every chipmaker that uses EUV lithography (TSMC, Samsung, Intel) must buy Lasertec's inspection tools to verify the quality of their photomasks. No other company -- not KLA, not Zeiss, not any Chinese or Korean competitor -- offers a comparable product. If Lasertec ceased to function, EUV chip manufacturing would stop. The company has zero competitor edges in the graph.

**PILLAR** (6490.T) -- *Fluororesin fittings for semiconductor equipment*. PILLAR holds 90%+ global market share in fluororesin fittings used in semiconductor wet cleaning and chemical delivery systems. Its Super 300 (S-300) fitting is the de facto industry standard -- even Entegris, the American fluid handling giant, licenses PILLAR's fitting technology rather than attempting to develop its own. PILLAR supplies fittings to virtually every equipment maker (SCREEN, TEL, Ebara, Kokusai, CKD, Shibaura, Samco) and directly to major fabs (TSMC, Samsung, Intel, SK Hynix, SMIC, Hua Hong). PILLAR also has zero competitor edges in the graph.

### 2. Tight Duopolies

These are pairs of companies that together control the overwhelming majority of global supply for a critical input. In most cases, both members of the duopoly are Japanese.

**Shin-Etsu Chemical + SUMCO** -- *Silicon wafers*. Together, these two companies supply more than 50% of the world's 300mm silicon wafers. The graph shows both companies supplying TSMC, Samsung, Intel, SK Hynix, and Micron. They compete with each other (the graph contains bidirectional competitor edges labeled "silicon wafers"), but from the perspective of any chipmaker, the choice is Shin-Etsu or SUMCO -- or both. No other wafer supplier approaches their combined scale, quality, or consistency. Shin-Etsu's semiconductor materials division alone generates revenue comparable to the entirety of the next-largest competitor.

**Stella Chemifa + Morita Chemical** -- *Ultra-high purity hydrofluoric acid*. Stella Chemifa (4109.T) appears in the graph with 10 outgoing supplier edges, delivering ultra-high purity HF to TSMC, Samsung, Intel, SK Hynix, Micron, Kioxia, SMIC, Hua Hong, UMC, and GlobalFoundries. Its competitor, Morita Chemical (not in the graph), together with Stella Chemifa controls the market for 12-nine purity HF -- acid so pure that it contains fewer than one impurity atom per trillion. At advanced nodes (5nm and below), the purity of the etch chemicals directly determines yield. There is no substitute for this level of purity, and achieving it requires decades of process refinement.

**Gun Ei Chemical + Maruzen Petrochemical** -- *Novolac resins and high-purity aromatics for photoresist*. Gun Ei Chemical (CMP-0038) supplies novolac resins to TOK (CMP-0033), JSR (CMP-0034), Shin-Etsu (CMP-0024), FUJIFILM (CMP-0040), and Sumitomo Chemical (CMP-0046). Maruzen Petrochemical (CMP-0035) supplies high-purity aromatic solvents to TOK and JSR. Together, these two companies sit at the very top of the photoresist supply chain -- upstream of the resist formulators who are themselves upstream of every chipmaker. They are the suppliers' suppliers, invisible to most analysts but utterly essential.

**Fujimi + Fuso Chemical** -- *CMP slurry*. The graph shows both Fujimi (CMP-0007) and Fuso Chemical (CMP-0013) supplying CMP slurry to TSMC, Samsung, and Intel. They compete with FUJIFILM, Resonac, and international players like Cabot Microelectronics, but in Japan, Fujimi and Fuso together dominate the high-end of the colloidal silica slurry market used in advanced-node CMP.

### 3. Dominant Oligopolies

Three to five companies that collectively control a process step, with Japanese firms holding the leading positions.

**Tokyo Electron + SCREEN + Kokusai Electric** -- *Process equipment*. These three companies cover the three major categories of front-end process equipment: TEL dominates in coater/developers, etch, and CVD; SCREEN dominates in wet cleaning; Kokusai Electric holds a strong position in batch deposition (CVD and ALD). The graph shows TEL supplying 11 customers, SCREEN embedded in a web of supplier relationships, and Kokusai Electric with 6 outgoing supplier edges to major fabs (TSMC, Samsung, Intel, SK Hynix, Micron, SMIC, Kioxia). Together, they equip a substantial share of the world's clean rooms.

**TOK + JSR + Sumitomo Chemical** -- *Photoresist*. Japanese companies collectively hold approximately 90% of the global photoresist market. TOK (25% world share) supplies photoresist to TSMC, Samsung, and Intel. JSR supplies EUV photoresist to the same three. Sumitomo Chemical adds additional capacity. The graph also shows upstream dependencies: Gun Ei Chemical supplies novolac resins to TOK and JSR; Maruzen Petrochemical supplies high-purity aromatics. This layered Japanese dominance in photoresist -- from upstream resin chemistry to finished resist formulation -- is among the most strategically significant positions in the supply chain.

**Nikon + Canon** -- *Mature-node lithography*. While ASML monopolizes EUV, Nikon and Canon remain the dominant suppliers of i-line and KrF lithography steppers used in mature semiconductor nodes (28nm and above) and in back-end processes. The graph shows both companies supplying TSMC, Samsung, and Intel. Nikon and Canon also hold competitor edges with ASML, though the competition is now primarily in the mature-node segment. The mature-node market represents over 70% of all wafers produced globally, and it is growing rapidly as demand for power semiconductors, IoT chips, and automotive ICs accelerates.

### 4. Critical Infrastructure

Companies that supply essential services or materials to the fab environment itself, rather than to a specific process step.

**Organo + Nomura Micro Science** -- *Ultrapure water (UPW)*. A leading-edge semiconductor fab uses 30,000-40,000 tonnes of ultrapure water per day. Organo (CMP-0052) is estimated to supply 70-80% of TSMC's water treatment plants, with a reported 100% share for fabs at 10nm and below. The graph shows Organo supplying TSMC, Samsung, SMIC, and Hua Hong. Nomura Micro Science (CMP-0053) supplies TSMC, Samsung, and SK Hynix. Together, they dominate the UPW systems market across East Asia. UPW quality at advanced nodes must achieve resistivity of 18.2 megaohm-cm and total organic carbon below 1 ppb -- specifications that require continuous monitoring and proprietary ion exchange and filtration technology.

**Nippon Sanso** (4091.T) -- *Specialty gases*. The graph shows Nippon Sanso (CMP-0032) supplying specialty gases to TSMC, Samsung, Intel, SK Hynix, and Micron -- all five of the world's largest chipmakers. Semiconductor fabs consume dozens of specialty gases (nitrogen trifluoride, silane, arsine, phosphine, and many others) in deposition, etch, and doping processes. Gas purity is specified to parts-per-billion or better, and on-site gas generation and delivery require continuous service relationships that are difficult for competitors to displace.

**Daifuku** (6383.T) -- *Automated material handling systems (AMHS)*. A modern 300mm fab contains thousands of wafer cassettes (FOUPs) that must be transported between process tools on overhead hoist transport (OHT) tracks. Daifuku is the global leader in cleanroom AMHS. The graph shows Daifuku supplying TSMC, Samsung, and Intel. Changing AMHS providers is extraordinarily costly because the transport system is physically integrated into the fab's structure -- it is, in effect, part of the building.

### 5. Precision Components

Small and mid-cap companies making specialized parts that are embedded inside larger equipment systems. They are invisible to most investors but often irreplaceable.

**Naigai Tech** (3374.T) derives 80% of its sales from precision machined parts supplied to Tokyo Electron. It is, in effect, a single-customer company -- but that customer is one of the world's top three equipment makers.

**Marumae** (6264.T) manufactures aluminum vacuum chambers used in equipment from Tokyo Electron and SCREEN Holdings. Vacuum chambers must meet extreme specifications for surface finish, dimensional tolerance, and material purity. They cannot be sourced from generic metalworking shops.

**Tocalo** (3433.T) provides thermal spray coatings for equipment parts used by Tokyo Electron and SCREEN. These coatings protect chamber internals from the corrosive plasmas and chemicals used in etch and deposition processes. The coating must be uniform to micron-level tolerances and adhere perfectly under thermal cycling.

**NHK Spring** (5991.T) supplies probe card springs to Advantest and HDD suspension springs to TSMC. Its probe card springs are a critical component of the test interface -- the physical connection between the tester and the chip being tested.

**Aval Data** (6918.T) supplies tester boards, image processing components, and probes to Advantest, Tokyo Electron, and Nikon. These subsystems are deeply integrated into the host equipment's architecture.

These five companies represent a pattern that repeats throughout the Japanese semiconductor supply chain: small, specialized, deeply embedded, and quietly indispensable. An investor scanning the Nikkei 225 would never notice Naigai Tech or Marumae. But their products are inside the equipment that makes every advanced chip on earth.

---

## Japan's Presence Across the Process Flow

One of the most remarkable features of the graph is that Japanese companies appear in **every single major step** of the semiconductor manufacturing process. No other country can claim this. Taiwan's strength is concentrated in foundry and OSAT. South Korea's is in memory and a growing equipment base. The USA dominates chip design and some equipment categories (not mapped in this graph). The Netherlands has ASML. But only Japan has critical companies at every stage.

| Process Step | Japanese Companies |
|--------------|-------------------|
| **Silicon wafer production** | Shin-Etsu, SUMCO, Ferrotec |
| **Ultrapure water** | Organo, Nomura Micro Science |
| **Specialty gases** | Nippon Sanso, Kanto Denka Kogyo |
| **Photomask blanks** | HOYA |
| **Photomask production** | TOPPAN, DNP |
| **Photomask inspection** | Lasertec |
| **Lithography (mature)** | Nikon, Canon, Ushio (UV lamps) |
| **Photoresist** | TOK, JSR, Sumitomo Chemical, FUJIFILM, Toyo Gosei |
| **Resist raw materials** | Gun Ei Chemical, Maruzen Petrochemical |
| **Deposition** | Tokyo Electron, Kokusai Electric, Shibaura Mechatronics, Samco, Tazmo |
| **Etch chemicals (HF)** | Stella Chemifa, Kanto Denka |
| **Cleaning equipment** | SCREEN Holdings |
| **CMP equipment** | Ebara, Tokyo Seimitsu |
| **CMP consumables** | Fujimi, Fuso Chemical, FUJIFILM, Resonac |
| **Equipment components** | PILLAR (fittings), CKD (valves), Marumae (chambers), Tocalo (coatings), NGK (chucks), Naigai Tech (parts) |
| **Wafer handling** | Rorze (robots), Daifuku (AMHS) |
| **Process monitoring** | Horiba (gas analysis), Olympus (microscopy) |
| **Probing/testing** | Tokyo Seimitsu, Advantest, Aval Data, NHK Spring |
| **Dicing** | DISCO, Tokyo Seimitsu |
| **Packaging substrates** | Ibiden, Niterra, Kyocera, Resonac |
| **Chemical distribution** | Nagase |
| **Surface treatment** | MEC Company |
| **Memory chips** | Kioxia |

This comprehensive presence is not accidental. It is the result of decades of investment by the Japanese government and private sector in building a vertically complete semiconductor ecosystem. When MITI (now METI) organized the VLSI Technology Research Association in the 1970s, the explicit goal was to develop domestic capabilities across the full stack -- from raw materials to finished chips. That project succeeded beyond its original ambitions: Japan may have lost leadership in chip fabrication itself (to Taiwan and South Korea), but it retained and deepened its dominance in the equipment and materials that make fabrication possible.

---

## How to Read This Book

This chapter has presented the supply chain graph in its entirety. The rest of the book zooms in.

**Part II (Chapters 4-5)** covers the foundational inputs that enter every fab: silicon wafers (Chapter 4) and the two invisible essentials of ultrapure water and specialty gases (Chapter 5). These are the "raw materials" chapters -- the bottom layer of the supply chain.

**Part III (Chapters 6-8)** follows the light. Lithography (Chapter 6) is the step that defines the chip's circuit pattern. Photomasks (Chapter 7) are the templates that carry that pattern. Photoresist (Chapter 8) is the light-sensitive chemical that receives it. This triad -- equipment, template, chemical -- represents the most technologically demanding and strategically concentrated segment of the supply chain.

**Part IV (Chapters 9-11)** covers the three process steps that build the chip layer by layer: deposition (Chapter 9), etch and clean (Chapter 10), and CMP planarization (Chapter 11). These chapters are where the largest Japanese equipment companies -- TEL, SCREEN, Kokusai, Ebara -- take center stage.

**Part V (Chapter 12)** steps back from the process flow to examine the infrastructure of the fab itself: the automated material handling systems, wafer transfer robots, precision machined parts, ceramic components, and other systems that keep the factory running. This chapter covers the smallest and most obscure companies in the graph -- but some of the most instructive investment stories.

**Part VI (Chapters 13-15)** covers back-end manufacturing: wafer testing and probing (Chapter 13), dicing and singulation (Chapter 14), and the rapidly evolving world of advanced packaging (Chapter 15). These chapters bring together Tokyo Seimitsu, DISCO, Advantest, Ibiden, and the global OSAT ecosystem.

**Part VII (Chapters 16-17)** turns to the demand side and the broader context. Chapter 16 profiles the foundries, IDMs, and fabless companies that drive equipment and materials spending -- and explains how AI capex cycles ripple backward through the Japanese supply chain. Chapter 17 addresses geopolitics: Japan's position in the US-China technology rivalry, export controls, and the risks and opportunities they create for Japanese suppliers.

**Part VIII (Chapter 18 and Appendices)** concludes with an investment framework. Chapter 18 presents a systematic scoring methodology for evaluating Japanese semiconductor companies across six dimensions, identifies the most undervalued names, and provides investment theses for the highest-conviction positions. The appendices contain reference material: company cards for all 110 companies, the complete edge list from the graph, the scoring methodology, and a glossary.

Each chapter can be read independently, but the chapters are designed to build on each other. A reader who has digested the supply chain map in this chapter will recognize the edges and relationships described in every subsequent chapter. A reader who follows the full sequence from Chapter 4 through Chapter 17 will have, by the end, traversed every node and edge in the graph -- and will understand not just *what* Japan makes, but *why* it matters.

---

## Key Takeaways

- The semiconductor supply chain graph contains **110 companies connected by 321 relationships**, spanning 8 countries. Japan accounts for nearly half of all nodes and an even larger share of supply relationships.

- **86% of all supplier edges originate from Japanese companies**. Japan is, overwhelmingly, the supply side of the semiconductor industry.

- **TSMC has 40 incoming supplier edges; 38 are from Japan.** The world's most important foundry depends on Japanese companies for 95% of its documented supply relationships. Samsung shows a similar pattern at 77%.

- **Tokyo Seimitsu is the most-connected node in the entire graph** (65 edges), supplying equipment to 35 companies across 7 countries while competing with 15 rivals. Among companies ranked by outgoing supplier edges, 9 of the top 10 are Japanese.

- **Japan has companies at every single step** of the chip manufacturing process. No other country has this breadth. This comprehensive presence is the structural foundation of Japan's supply chain power -- and the reason this book exists.

---

*Data sources: graph.json (110 nodes, 321 edges), CMP-0001.json (Tokyo Seimitsu), CMP-0002.json (DISCO), CMP-0004.json (Tokyo Electron), CMP-0006.json (Lasertec), CMP-0017.json (TSMC), CMP-0018.json (Samsung), CMP-0042.json (PILLAR)*
