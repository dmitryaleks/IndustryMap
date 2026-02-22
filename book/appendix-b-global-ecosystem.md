# Appendix B: Global Ecosystem Reference

This appendix profiles all 48 non-Japanese companies tracked in the supply chain graph (CMP-0063 through CMP-0110). Each card identifies the company, its role in the semiconductor value chain, and -- critically -- its supply chain edges connecting back to Japanese companies. These links demonstrate how the global semiconductor ecosystem depends on Japan's hidden infrastructure of equipment, materials, and components.

Companies are grouped by country or region. Edge notation follows the format used in `graph.json`: "supplier" edges indicate a buyer-seller relationship; "competitor" edges indicate direct market overlap; "ecosystem" edges indicate strategic partnerships or corporate affiliations.

---

## Taiwan

Taiwan's semiconductor ecosystem anchors global chip manufacturing. Its foundries, OSAT houses, and testing companies are among the largest consumers of Japanese equipment and materials.

---

### ASE Technology Holding Co., Ltd. (3711.TW)
**ID:** CMP-0063 | **Country:** Taiwan | **Industry:** Semiconductor Packaging/OSAT

World's largest OSAT company with approximately 30% global market share. Formed in 2018 by combining ASE Group, Siliconware Precision Industries, and Universal Scientific Industrial. Provides semiconductor packaging, interconnect materials, front-end engineering testing, wafer probing, and final testing services. Market cap approximately 7.36 trillion JPY. Major clients include Apple, Qualcomm, MediaTek, and NVIDIA.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> ASE: dicing, probing equipment (OSAT #1)
- DISCO (CMP-0002) --> ASE: dicing saws, blades
- Tokyo Electron (CMP-0004) --> ASE: process equipment
- Advantest (CMP-0005) --> ASE: test equipment
- Hanmi Semiconductor (CMP-0072) --> ASE: flip chip bonders

---

### Powertech Technology Inc. (6239.TW)
**ID:** CMP-0069 | **Country:** Taiwan | **Industry:** Semiconductor Packaging/OSAT

Taiwan's leading memory-focused OSAT company and a key supplier to Micron for memory packaging. Services include wafer-level packaging, flip chips, wire bond BGA, lead frame, SiP, and chip probing/final test. Operations span Taiwan, Japan, Singapore, USA, Europe, and China. Market cap approximately 772 billion JPY. Memory OSAT prices jumped 30% in 2026, driven partly by Powertech.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> Powertech: dicing, probing equipment (Taiwan memory OSAT)
- DISCO (CMP-0002) --> Powertech: dicing saws, blades
- Powertech --> Micron (CMP-0021): memory packaging (key Micron supplier)

---

### King Yuan Electronics Co., Ltd. (2449.TW)
**ID:** CMP-0101 | **Country:** Taiwan | **Industry:** Semiconductor Testing/OSAT

World's largest pure-play semiconductor testing company. Services include wafer probing (43% of revenue), IC final testing (50%), and wafer grinding/dicing (7%). Trailing twelve-month revenue approximately 1.02 billion USD. Headquartered in Hsinchu, Taiwan. Recently divested its Chinese subsidiary (Suzhou) due to geopolitical tensions. One of the most important buyers of wafer probing equipment globally.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> King Yuan: probing equipment (world #1 pure-play tester)
- DISCO (CMP-0002) --> King Yuan: dicing saws
- Advantest (CMP-0005) --> King Yuan: test equipment

---

### United Microelectronics Corporation (2303.TW)
**ID:** CMP-0102 | **Country:** Taiwan | **Industry:** Semiconductor Foundry

Taiwan's first semiconductor company (1980, spun off from ITRI) and the world's third-largest specialty foundry. Operates 12 fabs with combined capacity exceeding 400,000 wafers per month (12-inch equivalent), including facilities in Singapore and Xiamen, China. Processes cover high voltage, BCD, SOI, discrete, logic, mixed-signal, analog, and embedded memory. Market cap approximately 4.0 trillion JPY.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> UMC: CMP, probing, dicing (Taiwan #2 foundry)
- Tokyo Electron (CMP-0004) --> UMC: process equipment
- Stella Chemifa (CMP-0044) --> UMC: ultra-high purity HF

---

### Vanguard International Semiconductor Corporation (5347.TWO)
**ID:** CMP-0103 | **Country:** Taiwan | **Industry:** Semiconductor Foundry

Taiwan specialty foundry originally affiliated with TSMC. Focuses on 200mm and 300mm legacy-node wafers (180nm to 55nm) for high voltage, BCD, SOI, discrete, logic, mixed-signal, and analog applications. Market cap approximately 540 billion JPY. Headquarters in Hsinchu. Stable equipment customer due to its mature-node focus.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> Vanguard: CMP, probing, dicing (Taiwan specialty foundry)

---

### Chipbond Technology Corporation (6147.TWO)
**ID:** CMP-0104 | **Country:** Taiwan | **Industry:** Semiconductor Packaging/OSAT

Taiwan OSAT specializing in driver IC and non-driver IC packaging and testing. Services include gold/solder/copper bumping, RDL, wafer probe testing, die processing (wafer grinding, thinning, dicing, tape-and-reel), chip-on-film, chip-on-glass, and WLCSP. Also handles compound semiconductors including SiGe, GaAs, GaN, and SiC. Market cap approximately 110 billion JPY. Six factories in Taiwan plus one in Malaysia.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> Chipbond: probing, dicing (Taiwan OSAT)
- DISCO (CMP-0002) --> Chipbond: dicing saws

---

### ChipMOS Technologies Inc. (8150.TW)
**ID:** CMP-0105 | **Country:** Taiwan | **Industry:** Semiconductor Packaging/OSAT

Taiwan OSAT for back-end assembly and testing of memory and logic/mixed-signal semiconductors. Segments include testing, assembly, LCD driver, bumping, and others. Services cover engineering test, wafer probing, final test, multi-chip packaging, BGA, COF, wafer bumping, and WLCSP. Dual-listed on TWSE and NASDAQ (IMOS). Market cap approximately 100 billion JPY. Headquartered in Hsinchu.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> ChipMOS: probing, dicing (Taiwan OSAT)
- DISCO (CMP-0002) --> ChipMOS: dicing saws

---

### MPI Corporation (6223.TW)
**ID:** CMP-0071 | **Country:** Taiwan | **Industry:** Semiconductor Equipment

Taiwan's leading wafer prober and semiconductor RF test solution provider. Founded 1995 in Hsinchu. Products include advanced wafer probers, probe cards, thermal systems, and engineering probe stations. Holds approximately 10% of the global prober market (third after Tokyo Seimitsu at 46% and Tokyo Electron at 27%). Market cap approximately 1.0 trillion JPY. First prober company to list on Taiwan TPEx.

**Key Japanese Supply Chain Links:**
- MPI <--> Tokyo Seimitsu (CMP-0001): competitor in probing equipment

---

## United States

One US-headquartered OSAT company falls within the CMP-0063 to CMP-0110 range. Its deep reliance on Japanese equipment underscores that even American semiconductor services companies cannot operate without Japan's backend infrastructure.

---

### Amkor Technology, Inc. (AMKR)
**ID:** CMP-0064 | **Country:** USA | **Industry:** Semiconductor Packaging/OSAT

World's second-largest OSAT company with 15.2% global market share. Provides semiconductor packaging and test services including advanced SiP, flip chip, wire bond BGA, and wafer-level packaging. Major operations in Korea, Japan, China, Malaysia, Vietnam, Philippines, and Portugal. FY2024 revenue: 6.32 billion USD. Apple and Qualcomm together represent 41% of total sales. Record Advanced SiP revenue in 2024. New facility ramped in Vietnam. Market cap approximately 1.83 trillion JPY. PER 39.25, PBR 1.6.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> Amkor: dicing, probing equipment (OSAT #2)
- DISCO (CMP-0002) --> Amkor: dicing saws, blades
- Tokyo Electron (CMP-0004) --> Amkor: process equipment
- Advantest (CMP-0005) --> Amkor: test equipment

---

## South Korea

South Korea's semiconductor industry revolves around Samsung Electronics and SK Hynix. An ecosystem of domestic equipment and OSAT companies has developed to serve these two giants, though dependence on Japanese equipment remains significant.

---

### Hanmi Semiconductor Co., Ltd. (042700.KS)
**ID:** CMP-0072 | **Country:** South Korea | **Industry:** Semiconductor Equipment

South Korea's leading semiconductor packaging equipment manufacturer and the world's number one in HBM thermocompression bonders with 71.2% global market share. Key products include TC bonders for HBM production, MSVP package singulation systems, and flip chip bonders. FY2024 revenue: 576.7 billion KRW (record high) with 43.6% operating margin. Selected by TechInsights as the only Korean company in the global top 10 semiconductor equipment firms (2025). Market cap approximately 2.0 trillion JPY.

**Key Japanese Supply Chain Links:**
- Hanmi --> SK Hynix (CMP-0020): TC bonders for HBM (71% share)
- Hanmi --> Micron (CMP-0021): TC bonders for HBM
- Hanmi --> ASE (CMP-0063): flip chip bonders
- Hanmi <--> Tokyo Seimitsu (CMP-0001): competitor in package singulation equipment

---

### DB HiTek Co., Ltd. (000990.KS)
**ID:** CMP-0075 | **Country:** South Korea | **Industry:** Semiconductor Foundry

South Korea's second-largest semiconductor foundry (after Samsung). Specializes in 200mm wafer fabrication for legacy and mature-node chips: power management ICs, display driver ICs, contact image sensors, and automotive semiconductors. Operates fabs in Bucheon and Sangwoo (Eumseong). Market cap approximately 404.6 billion JPY. PER 18.04, PBR 1.98. Investing 1.2 trillion KRW through 2030 for capacity expansion. Secured a Tesla 10-year PMIC foundry contract.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> DB HiTek: probing, dicing, CMP equipment (Korea #2 foundry)
- SurplusGLOBAL (CMP-0100) --> DB HiTek: used semiconductor equipment

---

### HANA Micron Inc. (067310.KQ)
**ID:** CMP-0076 | **Country:** South Korea | **Industry:** Semiconductor Packaging/OSAT

Korea's largest OSAT company and global number eight with 920 million USD annual revenue (2024). Specializes in memory semiconductor packaging and testing for mobile DRAM stack chips, NAND packages, and silicon components. Major customers are Samsung Electronics and SK Hynix. Overseas subsidiaries in Brazil and Vietnam. PER 22.41, PBR 5.29. Foreign ownership 15.13%.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> HANA Micron: probing, dicing equipment (Korea #1 OSAT)
- HANA Micron --> Samsung (CMP-0018): memory packaging and test
- HANA Micron --> SK Hynix (CMP-0020): memory packaging and test

---

### Nepes Corporation (033640.KQ)
**ID:** CMP-0077 | **Country:** South Korea | **Industry:** Semiconductor Packaging/OSAT

Korean advanced packaging and OSAT specialist, ranked approximately 17th globally. Pioneer in Fan-Out Panel Level Packaging (FO-PLP) technology, ahead of ASE in FO-PLP commercialization. Provides turnkey backend services from test to packaging. FY2024 revenue: 464.3 billion KRW. PBR 3.72. One-year stock return: +109.92%. Currently unprofitable (EPS -2,699 KRW) as it invests in AI semiconductor packaging technologies.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> Nepes: probing, dicing equipment (Korea OSAT)

---

### SFA Semicon Co., Ltd. (036540.KQ)
**ID:** CMP-0078 | **Country:** South Korea | **Industry:** Semiconductor Packaging/OSAT

Korean OSAT company specializing in memory and non-memory semiconductor packaging and testing, ranked approximately 16th globally. Founded as a Samsung Electronics backend outsourcing partner. Parent company SFA holds a 54.95% stake. Expanding from commodity memory packaging into non-memory, automotive, and AI semiconductor packaging. PER 56.35, PBR 2.41. Market cap approximately 1.2 trillion KRW.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> SFA Semicon: probing, dicing equipment (Korea OSAT)
- SFA Semicon --> Samsung (CMP-0018): memory packaging/test outsourcing

---

### LB Semicon Co., Ltd. (061970.KQ)
**ID:** CMP-0079 | **Country:** South Korea | **Industry:** Semiconductor Packaging/OSAT

Korean OSAT company specializing in display driver IC and mobile semiconductor packaging and testing, ranked approximately 18th globally. High exposure to DDI and mobile segments makes it sensitive to demand volatility. Expanding into PMIC, CIS, SoC, and AI/high-performance semiconductor packaging. PBR 0.98 (trading below book value). Foreign ownership relatively high at 31.84%. Currently unprofitable with EPS -507 KRW.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> LB Semicon: probing, dicing equipment (Korea OSAT)

---

### Techwing Inc. (089030.KQ)
**ID:** CMP-0080 | **Country:** South Korea | **Industry:** Semiconductor Equipment

Korea's leading semiconductor test handler manufacturer and global number one in memory test handlers with approximately 70% market share. Key products include memory/SoC test handlers, display inspection equipment, and CubeProber HBM inspection equipment. Major customers are SK Hynix and Samsung Electronics. PBR 8.39. Market cap approximately 1.7 trillion KRW. CubeProber is a new wafer-level probing system for HBM inspection.

**Key Japanese Supply Chain Links:**
- Techwing --> Samsung (CMP-0018): memory test handlers
- Techwing --> SK Hynix (CMP-0020): memory test handlers

---

### KCTech Co., Ltd. (281820.KS)
**ID:** CMP-0081 | **Country:** South Korea | **Industry:** Semiconductor Equipment

Korea's only domestic CMP equipment and CMP slurry materials manufacturer. Successfully localized CMP equipment that was previously import-dependent. Products include the VENTUS CMP System, wet cleaning systems, display equipment, and CMP slurry materials (ceria and silica). PER 18.81, PBR 1.94. Market cap approximately 982.8 billion KRW. New VENTUS CMP system is under Samsung qualification testing, with supply confirmation expected within one year.

**Key Japanese Supply Chain Links:**
- KCTech --> Samsung (CMP-0018): CMP equipment, slurry (VENTUS system)
- KCTech --> SK Hynix (CMP-0020): CMP equipment, cleaning, slurry
- Competes with Tokyo Seimitsu (CMP-0001) ChaMP CMP systems and Ebara (CMP-0036) CMP equipment

---

### Leeno Industrial Inc. (058470.KQ)
**ID:** CMP-0082 | **Country:** South Korea | **Industry:** Semiconductor Components

Korea's leading manufacturer of semiconductor test sockets (IC Test Sockets) and probe components under the LEENO brand. Developing next-generation products including TSV probe cards, tri-temperature test probes, and 100GHz-compatible sockets. Customers include Qualcomm, TSMC, Samsung Electronics, and NVIDIA. PER 64.92, PBR 11.77. Market cap approximately 735.4 billion KRW. FY2025 operating profit growth: +42.51% YoY.

**Key Japanese Supply Chain Links:**
- Leeno --> TSMC (CMP-0017): IC test sockets
- Leeno --> Samsung (CMP-0018): IC test sockets
- Leeno --> NVIDIA (CMP-0028): test sockets
- Ecosystem overlap with NHK Spring (CMP-0055) probe card springs and Tokyo Seimitsu (CMP-0001) wafer probers

---

### SEMES Co., Ltd. (unlisted)
**ID:** CMP-0096 | **Country:** South Korea | **Industry:** Semiconductor Equipment

Korea's largest semiconductor equipment maker and a Samsung Electronics subsidiary (91.5% ownership). Annual revenue exceeds 3 trillion KRW. World top-10 equipment firm for six consecutive years. Products span front-end (cleaning, photo track, etch, deposition) and back-end (bonders, probers, test handlers). The SEMPRO PRIME prober directly competes with Tokyo Seimitsu wafer probers. Represents Samsung's strategic effort to reduce dependence on Japanese equipment makers.

**Key Japanese Supply Chain Links:**
- SEMES --> Samsung (CMP-0018): probers, photo track, cleaning (Samsung captive)
- PILLAR (CMP-0042) --> SEMES: mechanical seals, bellows
- SEMES <--> Tokyo Seimitsu (CMP-0001): competitor in probing equipment (Korea Samsung captive)
- Competes with Tokyo Electron (CMP-0004) in photo track and cleaning, SCREEN (CMP-0003) in cleaning

---

### SEMICS Inc. (unlisted)
**ID:** CMP-0097 | **Country:** South Korea | **Industry:** Semiconductor Equipment

Korea's only independent wafer prober manufacturer and the world's third-largest wafer prober maker after Tokyo Seimitsu (46% share) and Tokyo Electron (27% share). Has supplied Samsung Electronics for over 15 years. Revenue: 179.8 billion KRW (2024). Innovative "apartment-type" stacked prober achieves 670% cleanroom efficiency improvement by fitting 12 probers in the footprint of two conventional probers. Target: 2 trillion KRW revenue by 2030.

**Key Japanese Supply Chain Links:**
- SEMICS --> Samsung (CMP-0018): wafer probers (15-year relationship)
- SEMICS --> SK Hynix (CMP-0020): wafer probers
- SEMICS <--> Tokyo Seimitsu (CMP-0001): competitor in probing equipment (Korea world #3)

---

### WONIK IPS Co., Ltd. (240810.KQ)
**ID:** CMP-0098 | **Country:** South Korea | **Industry:** Semiconductor Equipment

Major Korean semiconductor deposition equipment maker. Products include PECVD, ALD, and thermal processing equipment. Key supplier to Samsung and SK Hynix fabs. Part of the Wonik Group. PER 41.96, PBR 3.72. Foreign ownership 22.52%. TTM revenue approximately 603 million USD. Competes in the same fab equipment ecosystem as Tokyo Seimitsu but in different process steps (deposition versus probing/dicing/CMP).

**Key Japanese Supply Chain Links:**
- WONIK IPS --> Samsung (CMP-0018): PECVD, ALD, thermal equipment
- WONIK IPS --> SK Hynix (CMP-0020): deposition equipment
- Competes with Tokyo Electron (CMP-0004) and Kokusai Electric (CMP-0011) in deposition equipment

---

### EO Technics Co., Ltd. (039030.KQ)
**ID:** CMP-0099 | **Country:** South Korea | **Industry:** Semiconductor Equipment

Korean laser technology specialist for semiconductor manufacturing. Successfully localized laser stealth dicing technology that competes with DISCO's blade dicing (70%+ market share). Laser dicing has advantages for thin wafers (below 200 micrometers) and HBM applications. Products include laser stealth dicing, laser markers, laser annealing, and laser grooving equipment. PER 107.11, PBR 7.49. FY2026 forecast revenue: 480 billion KRW (record), with operating profit growth of +187.3% YoY.

**Key Japanese Supply Chain Links:**
- EO Technics --> Samsung (CMP-0018): laser dicing, marking, annealing
- EO Technics --> SK Hynix (CMP-0020): laser stealth dicing for HBM
- EO Technics <--> DISCO (CMP-0002): competitor in dicing equipment (laser vs blade)
- EO Technics <--> Tokyo Seimitsu (CMP-0001): competitor in dicing equipment (laser vs blade)

---

### SurplusGLOBAL Inc. (140070.KQ)
**ID:** CMP-0100 | **Country:** South Korea | **Industry:** Semiconductor Equipment

World's number one used semiconductor equipment dealer and platform. Buys, sells, consigns, and brokers 1,500+ used semiconductor equipment units annually. Since 2000, has transacted 50,000+ units with 4,000+ semiconductor companies globally. Located in Yongin, Gyeonggi Province, with a 21,000-pyeong semiconductor equipment cluster including a 660-pyeong cleanroom. Subsidiaries in USA, China, Japan, Taiwan, and Singapore. PER 17.09, PBR 0.40 (deeply undervalued on book basis).

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> SurplusGLOBAL: handles used Accretech probers, dicers, CMP equipment
- DISCO (CMP-0002) --> SurplusGLOBAL: used dicing equipment
- Tokyo Electron (CMP-0004) --> SurplusGLOBAL: used front-end equipment
- SurplusGLOBAL --> DB HiTek (CMP-0075): used equipment for legacy node fabs

---

## China

China's semiconductor ecosystem represents the most dynamic and politically significant segment of the global supply chain. Its companies are simultaneously the largest growth market for Japanese equipment and the most active competitors attempting to localize replacements for Japanese technology under export control pressure.

---

### Semiconductor Manufacturing International Corporation -- SMIC (0981.HK)
**ID:** CMP-0066 | **Country:** China | **Industry:** Semiconductor Foundry

China's largest and world's third-largest semiconductor foundry. Provides IC foundry services with specialty and advanced process technologies, capable of production down to 7nm-class. Operations in Shanghai, Beijing, Tianjin, Shenzhen, and Ningbo. Also listed on Shanghai STAR Market (688981.SS). Market cap approximately 13.3 trillion JPY. PER 110.36, PBR 2.96. Second-largest shareholder of JCET (CMP-0065).

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> SMIC: CMP, probing, dicing (China foundry #1)
- Tokyo Electron (CMP-0004) --> SMIC: coater/developer, etch, CVD
- Kokusai Electric (CMP-0011) --> SMIC: batch deposition
- Stella Chemifa (CMP-0044) --> SMIC: ultra-high purity HF
- Organo (CMP-0052) --> SMIC: ultrapure water systems
- PILLAR (CMP-0042) --> SMIC: mechanical seals, bellows
- SMIC <--> JCET (CMP-0065): ecosystem (SMIC is JCET's 2nd largest shareholder)

---

### Hua Hong Semiconductor Limited (1347.HK)
**ID:** CMP-0070 | **Country:** China | **Industry:** Semiconductor Foundry

China's second-largest and world's seventh-largest pure-play foundry. Specializes in specialty technologies including embedded/standalone NVM, power discrete, analog/power management, logic, and RF. Operates 8-inch and 12-inch fabs in Shanghai and Wuxi. Also listed on Shanghai STAR Market (688347.SS). Market cap approximately 3.7 trillion JPY. PER 239.0, PBR 1.2.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> Hua Hong: CMP, probing equipment (China foundry #2)
- Tokyo Electron (CMP-0004) --> Hua Hong: deposition equipment
- Stella Chemifa (CMP-0044) --> Hua Hong: ultra-high purity HF
- Organo (CMP-0052) --> Hua Hong: ultrapure water systems
- PILLAR (CMP-0042) --> Hua Hong: mechanical seals, bellows

---

### JCET Group Co., Ltd. (600584.SS)
**ID:** CMP-0065 | **Country:** China | **Industry:** Semiconductor Packaging/OSAT

China's largest and world's third-largest OSAT company with approximately 12% global market share. Provides IC system integration packaging design, technology development, wafer probing, wafer-level packaging, system-level packaging, and chip testing services. Production bases in Korea, Singapore, and multiple Chinese cities. FY2024 revenue approximately 5.0 billion USD (+19.3% YoY). Market cap approximately 1.79 trillion JPY. PER 44.35. Leading in SiP and Chiplet technologies.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> JCET: dicing, probing equipment (China OSAT #1)
- DISCO (CMP-0002) --> JCET: dicing saws, blades
- JCET <--> SMIC (CMP-0066): ecosystem (JCET packaging for SMIC chips; SMIC is JCET's 2nd largest shareholder)

---

### Tongfu Microelectronics Co., Ltd. (002156.SZ)
**ID:** CMP-0067 | **Country:** China | **Industry:** Semiconductor Packaging/OSAT

China's second-largest OSAT company and global number four. Specializes in IC packaging and testing with expertise in advanced packaging including flip chip, BGA, SiP, and wafer-level packaging. AMD is the largest customer, contributing more than 50% of revenue. FY2024 revenue approximately 3.32 billion USD (+5.6% YoY). PER 80.0. Tongfu is AMD's largest packaging test supplier.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> Tongfu: dicing, probing equipment (China OSAT #2)
- DISCO (CMP-0002) --> Tongfu: dicing saws, blades

---

### Tianshui Huatian Technology Co., Ltd. (002185.SZ)
**ID:** CMP-0068 | **Country:** China | **Industry:** Semiconductor Packaging/OSAT

China's third-largest OSAT company and global number six. Provides semiconductor packaging and testing services including 3D, SiP, FC, TSV, Bumping, Fan-Out, and WLP advanced packaging technologies. Strategic partnership with Yangtze Memory Technologies (YMTC). FY2024 revenue approximately 2.01 billion USD (+26% YoY). PER 60.0. Parent company of Unisem Malaysia (CMP-0109). Relatively diversified customer base compared to peers.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> Huatian: dicing, probing equipment (China OSAT #3)
- DISCO (CMP-0002) --> Huatian: dicing saws, blades
- Huatian <--> Unisem Malaysia (CMP-0109): ecosystem (Huatian is parent of Unisem)

---

### Nexchip Semiconductor Corporation (688249.SS)
**ID:** CMP-0083 | **Country:** China | **Industry:** Semiconductor Foundry

China's third-largest semiconductor foundry. Founded 2015 in Hefei, Anhui. Primarily a 12-inch wafer foundry and the world's leading DDIC (Display Driver IC) foundry. Product mix: DDIC 68.5%, CIS 16%, PMIC 9%, MCU 2.4%, Logic 3.8%. Technology nodes extend to 55nm with 40nm in development. Joint venture origin with Taiwan's Powerchip. Market cap approximately 1.68 trillion JPY. Q1-Q3 2025 revenue: 8.13 billion CNY (+20% YoY).

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> Nexchip: probing, dicing, CMP (China #3 foundry)

---

### China Resources Microelectronics Limited (688396.SS)
**ID:** CMP-0084 | **Country:** China | **Industry:** Semiconductors

China's leading IDM (Integrated Device Manufacturer) with a full semiconductor value chain: chip design, mask fabrication, wafer manufacturing, packaging, and testing. Core focus on power semiconductors (MOSFET number one in China), smart sensors, and intelligent control. Multiple fabs covering 6-inch, 8-inch, and 12-inch wafers. Subsidiary of China Resources Holdings (state-owned conglomerate). Revenue FY2024: 10.119 billion CNY (first time exceeding 10 billion). Market cap approximately 1.26 trillion JPY.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> CR Micro: probing, dicing (China IDM)

---

### NAURA Technology Group Co., Ltd. (002371.SZ)
**ID:** CMP-0085 | **Country:** China | **Industry:** Semiconductor Equipment

China's number one and world's number six semiconductor equipment company. The only domestic platform-type equipment maker covering etching, thin-film deposition (PVD/CVD), thermal processing, cleaning, coating/developing, CMP, ion implantation, and test equipment. FY2024 revenue approximately 30 billion CNY, net profit 5.62 billion CNY (number one profit in China's semiconductor sector). Market cap approximately 7.4 trillion JPY. PER 32.

**Key Japanese Supply Chain Links:**
- NAURA --> SMIC (CMP-0066): etching, deposition, cleaning equipment
- NAURA --> Hua Hong (CMP-0070): process equipment
- NAURA <--> Tokyo Seimitsu (CMP-0001): competitor in CMP and probing equipment
- Competes with Tokyo Electron (CMP-0004) in etching and coating/developing

---

### Hwatsing Technology Co., Ltd. (688001.SS)
**ID:** CMP-0086 | **Country:** China | **Industry:** Semiconductor Equipment

China's first company listed on the Shanghai STAR Market in 2019. Leading flat panel display inspection equipment maker with 32% AMOLED Cell/Module inspection market share in China. Expanding into semiconductor test equipment with the self-developed T7600 SoC test machine comparable to the Teradyne J750 series. Revenue FY2024 approximately 1.86 billion CNY. Market cap approximately 306 billion JPY. 2025 Q1-Q3 revenue: 1.579 billion CNY (+23.7% YoY).

**Key Japanese Supply Chain Links:**
- Competes with Advantest (CMP-0005) in SoC and memory test machines
- Adjacent competition with Tokyo Seimitsu (CMP-0001) in the semiconductor test ecosystem

---

### Hangzhou Changchuan Technology Co., Ltd. (300604.SZ)
**ID:** CMP-0087 | **Country:** China | **Industry:** Semiconductor Equipment

China's leading semiconductor backend test equipment manufacturer. Core products include test machines (ATE), sorters/handlers, probe stations, and AOI inspection equipment. Successfully developed a fully automatic 12-inch probe station (CP12-Memory) for memory chip testing. 2025 H1 revenue: 2.167 billion CNY (+41.8% YoY). Market cap approximately 714 billion JPY. Probe station project (2.6 billion CNY investment) directly targets the market dominated by Tokyo Seimitsu and Tokyo Electron probers.

**Key Japanese Supply Chain Links:**
- Changchuan <--> Tokyo Seimitsu (CMP-0001): competitor in probing equipment (China)
- Competes with Advantest (CMP-0005) in test machines

---

### Huahai Qingke / Hwatsing Technology Co., Ltd. (688120.SS)
**ID:** CMP-0088 | **Country:** China | **Industry:** Semiconductor Equipment

China's number one CMP equipment manufacturer. Founded 2013 as a joint venture between Tianjin government and Tsinghua University. Domestic market share rose from 6% (2019) to over 50% (2024 for 12-inch). Products include CMP equipment (core business), wafer thinning/back-grinding, dicing/scribing, edge polishing, ion implantation, and wet processing equipment. Market cap approximately 1.35 trillion JPY. 2025 H1 revenue: 1.95 billion CNY (+30.3% YoY). The most direct Chinese competitor to Tokyo Seimitsu's CMP business.

**Key Japanese Supply Chain Links:**
- Huahai Qingke --> SMIC (CMP-0066): CMP equipment
- Huahai Qingke --> Hua Hong (CMP-0070): CMP equipment
- Huahai Qingke --> YMTC (CMP-0093): CMP equipment (post-sanctions substitute)
- Huahai Qingke <--> Tokyo Seimitsu (CMP-0001): competitor in CMP equipment (China #1 CMP)
- Competes with Ebara (CMP-0036) in CMP equipment

---

### Shenyang Heyan Technology Co., Ltd. (unlisted)
**ID:** CMP-0089 | **Country:** China | **Industry:** Semiconductor Equipment

Chinese precision dicing machine manufacturer based in Shenyang, Liaoning. Founded 2011 by a team from China's early national dicing machine development project with over 40 years of experience. The DS9260 was the first domestically mass-produced wafer dicing machine in China. Product range covers 6-inch through 12-inch fully automatic dicing machines. Private company, not publicly listed. Over 20 patents, member of China Semiconductor Industry Association.

**Key Japanese Supply Chain Links:**
- Heyan <--> Tokyo Seimitsu (CMP-0001): competitor in dicing equipment (China)
- Competes with DISCO (CMP-0002) in dicing equipment (targeting DISCO's 70% and Accretech's 10% combined 90%+ global share)

---

### GigaDevice Semiconductor Inc. (603986.SS)
**ID:** CMP-0090 | **Country:** China | **Industry:** Semiconductors

Global leading fabless chip supplier. China's number one in NOR Flash (23% global share, world number two) and 32-bit MCU (domestic leader, global number eight). Core products include storage (NOR Flash, SLC NAND, DRAM accounting for over 70% of revenue), 32-bit general-purpose MCU, and smart human-machine interaction sensors. Revenue FY2024: 7.356 billion CNY. Market cap approximately 1.18 trillion JPY. PER 51. Planning a Hong Kong dual listing.

**Key Japanese Supply Chain Links:**
- SMIC (CMP-0066) --> GigaDevice: foundry services (SMIC uses Tokyo Seimitsu, Tokyo Electron, and Kokusai Electric equipment)
- Nexchip (CMP-0083) --> GigaDevice: foundry services
- Indirect Japanese equipment dependency through foundry partners

---

### Beijing Shuoke Jingwei Electronics Equipment Co., Ltd. (unlisted)
**ID:** CMP-0091 | **Country:** China | **Industry:** Semiconductor Equipment

CETC (China Electronics Technology Group) subsidiary specializing in CMP equipment. Founded 2019 from CETC's CMP technology commercialization. Products include 200mm and 300mm CMP equipment, with the parent CETC group also producing ion implanters, ECD, lithography machines, dicing machines, thinning machines, and flip-chip bonders. 300mm CMP equipment has entered international mainstream production lines for verification. Private company, not publicly listed.

**Key Japanese Supply Chain Links:**
- Shuoke <--> Tokyo Seimitsu (CMP-0001): competitor in CMP and dicing equipment (China state-owned)
- Competes with Ebara (CMP-0036) in CMP equipment

---

### Beijing TSD Semiconductor Equipment Co., Ltd. (unlisted)
**ID:** CMP-0092 | **Country:** China | **Industry:** Semiconductor Equipment

Chinese specialist in ultra-precision surface processing equipment for semiconductors. Core products include CMP polishing machines, wafer thinning/back-grinding machines, and double-side grinding/lapping machines. Focused on compound semiconductor substrates (SiC, GaN). Number one domestic market share in compound semiconductor CMP equipment. Only Chinese company with volume production of compound semiconductor-specific thinning, polishing, and CMP equipment. 170+ patents. Private company, designated as a "Chinese Potential Unicorn Enterprise."

**Key Japanese Supply Chain Links:**
- TSD <--> Tokyo Seimitsu (CMP-0001): competitor in CMP and grinding (compound semiconductor)
- Competes with DISCO (CMP-0002) in grinding equipment

---

### Yangtze Memory Technologies Co., Ltd. (unlisted)
**ID:** CMP-0093 | **Country:** China | **Industry:** Memory Semiconductors

China's most important 3D NAND flash memory manufacturer. Founded 2016 in Wuhan, Hubei. Monthly capacity approximately 130,000 wafers approaching 150,000 (2025 target), aiming for 15% global NAND share by 2026. Shipped 232-layer TLC chips with 294-layer equivalent density via dual-stack. Proprietary Xtacking architecture for 3D NAND. On the US Entity List, which restricts access to advanced equipment from the US, Japan, and the Netherlands. Estimated valuation: 160 billion CNY (approximately 3.36 trillion JPY).

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> YMTC: CMP, probing, dicing (China NAND, pre-sanctions)
- Huahai Qingke (CMP-0088) --> YMTC: CMP equipment (post-sanctions domestic substitute)
- YMTC was previously a customer for Tokyo Electron (CMP-0004) process equipment before tightened export controls
- Now pursuing first fully domestic equipment production line

---

### CanSemi Technology Co., Ltd. (unlisted)
**ID:** CMP-0094 | **Country:** China | **Industry:** Semiconductor Foundry

Greater Bay Area's (Guangdong-Hong Kong-Macao) only 12-inch wafer foundry in full production. Founded 2017 in Guangzhou. Specializes in analog chips, power management ICs, and power discrete devices. Three phases operational with technology nodes from 180nm to 55nm. IPO application accepted by Shenzhen ChiNext in December 2025, targeting a 7.5 billion CNY fundraise. Latest valuation: 25.3 billion CNY (approximately 531 billion JPY). Product yield exceeds 97%.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> CanSemi: probing, dicing, CMP (Guangzhou foundry)

---

### GTA Semiconductor Co., Ltd. (unlisted)
**ID:** CMP-0095 | **Country:** China | **Industry:** Semiconductor Foundry

Shanghai-based specialty foundry focusing on automotive, industrial, and power semiconductor chips. State-owned (CEC subsidiary). Operates two fab sites in Shanghai with total capacity of 300,000 wafers per month (8-inch equivalent) covering 6-inch, 8-inch, 12-inch, and SiC wafers. China's largest SiC foundry capacity at 30,000 wafers per month. Unicorn valuation: 31 billion CNY (approximately 651 billion JPY). Raised 13.5 billion CNY in a mega round in 2023. Not yet publicly listed.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> GTA Semi: probing, dicing (Shanghai specialty foundry)

---

### Sidea Semiconductor Equipment (301629.SZ)
**ID:** CMP-0073 | **Country:** China | **Industry:** Semiconductor Equipment

China's largest domestic prober station manufacturer with 25.7% Chinese domestic prober market share (2023). Founded 2003 in Shenzhen. First Chinese company to achieve mass production of 12-inch wafer probe stations. IPO on ChiNext in March 2025 at 52.28 CNY per share, first-day close +202% at 157.93 CNY. FY2022-2024 revenue: 399M/442M/546M CNY. Raised 5.45 billion CNY via IPO. PER approximately 50.

**Key Japanese Supply Chain Links:**
- Sidea <--> Tokyo Seimitsu (CMP-0001): competitor in probing equipment (China domestic)
- Breaking the Japanese monopoly held by Tokyo Seimitsu (46%) and Tokyo Electron (27%) in the global prober market

---

### Guangli Technology Co., Ltd. (300480.SZ)
**ID:** CMP-0074 | **Country:** China | **Industry:** Semiconductor Equipment

Chinese semiconductor dicing saw manufacturer. Originally a coal mine safety monitoring equipment company (founded 1994). Entered semiconductor dicing via 2019 acquisition of Israel's ADT (Advanced Dicing Technologies) for 37 million USD. One of only two companies globally (with DISCO) to manufacture both dicing saws and high-precision air-bearing spindles in-house. ADT dicing equipment achieves 0.1 micrometer precision control. PER approximately 40.

**Key Japanese Supply Chain Links:**
- Guangli <--> Tokyo Seimitsu (CMP-0001): competitor in dicing equipment
- Guangli <--> DISCO (CMP-0002): competitor in dicing equipment
- Chinese domestic dicing market approximately 5% penetration versus DISCO 70% and Tokyo Seimitsu 10%

---

## Singapore

Singapore serves as a critical neutral manufacturing hub for semiconductor foundries and OSAT companies, benefiting from political stability and proximity to Southeast Asian markets.

---

### GlobalFoundries Inc. (GFS)
**ID:** CMP-0106 | **Country:** Singapore | **Industry:** Semiconductor Foundry

World's third-largest foundry by revenue. Two fabs in Singapore (one 200mm and one 300mm facility) form a key manufacturing hub. In 2023, a 4 billion USD expansion raised Singapore capacity to approximately 1.5 million 300mm wafers per year. Acquired Advanced Micro Foundry (silicon photonics) in Singapore in November 2025. Additional fabs in Dresden (Germany) and Malta, NY (USA). FY2025 revenue: 6.79 billion USD. Market cap approximately 3.9 trillion JPY. Owned by Mubadala Investment Company (Abu Dhabi). NASDAQ listed.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> GlobalFoundries: CMP, probing, dicing (Singapore fabs)
- Tokyo Electron (CMP-0004) --> GlobalFoundries: process equipment
- Stella Chemifa (CMP-0044) --> GlobalFoundries: ultra-high purity HF

---

### UTAC Group (unlisted)
**ID:** CMP-0107 | **Country:** Singapore | **Industry:** Semiconductor Packaging/OSAT

Major global OSAT company headquartered in Singapore. Services include wafer-level packaging, laminate packages, leadframe solutions, SiP integration, MEMS and sensors, power applications, wafer probing, and final testing. Serves automotive, computing, and communications markets. Production bases in Singapore, Thailand, Indonesia, and China. Owned by Wise Road Capital (Beijing). Estimated valuation approximately 3 billion USD. Foxconn reportedly bid to acquire UTAC for up to 3 billion USD in 2025.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> UTAC: probing, dicing (Singapore OSAT)
- DISCO (CMP-0002) --> UTAC: dicing saws

---

## Malaysia

Malaysia's Penang and Ipoh corridors are home to a cluster of OSAT companies that serve as the backend manufacturing hub for the global semiconductor industry. All three tracked Malaysian companies rely on Japanese probing and dicing equipment.

---

### Inari Amertron Berhad (0166.KL)
**ID:** CMP-0108 | **Country:** Malaysia | **Industry:** Semiconductor Packaging/OSAT

Malaysia's leading OSAT and EMS company. Services include DC and RF wafer testing, wafer back-grinding, wafer sawing (dicing), wire bonding, substrate molding, flip-chip dice tape-and-reel, and automated visual inspection. Investing in SiP, flip-chip, and 2.5D packaging for AI/HPC. Key customer: Broadcom (RF filters for Apple iPhone). 11 plants across Malaysia, Philippines, and China. Over 6,000 employees. Market cap approximately 230 billion JPY. Bursa Malaysia listed. Headquarters in Bayan Lepas, Penang.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> Inari Amertron: probing, dicing (Malaysia #1 OSAT)
- DISCO (CMP-0002) --> Inari Amertron: dicing saws

---

### Unisem (M) Berhad (5005.KL)
**ID:** CMP-0109 | **Country:** Malaysia | **Industry:** Semiconductor Packaging/OSAT

Malaysian OSAT and subsidiary of Tianshui Huatian Technology (CMP-0068, China's third-largest OSAT). Services include advanced IC packaging (wafer bump, RDL, flip chip, WLCSP), leadframe IC packages, test services (wafer probe and final testing on RF, analog, digital, mixed-signal platforms), and turnkey services. Key customers include Qorvo, Skyworks, Broadcom, Elmos, Allegro, Microchip, and Renesas. Founded 1989, headquarters in Ipoh, Malaysia. Market cap approximately 170 billion JPY. Bursa Malaysia listed.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> Unisem: probing, dicing (Malaysia OSAT)
- DISCO (CMP-0002) --> Unisem: dicing saws
- Unisem <--> Tianshui Huatian (CMP-0068): ecosystem (Unisem is subsidiary of Huatian)

---

### Malaysian Pacific Industries Berhad (3867.KL)
**ID:** CMP-0110 | **Country:** Malaysia | **Industry:** Semiconductor Packaging/OSAT

Malaysian OSAT operating through subsidiary Carsem (M) Sdn Bhd. Full turnkey solutions for leaded and leadless semiconductor packaging and test. Carsem has over 500 testers and handlers across 125,000 square feet of dedicated test and wafer probe area. Operations in Ipoh (2 plants) and Suzhou, China. Part of the Hong Leong Group. Market cap approximately 230 billion JPY. Bursa Malaysia listed. Subsidiary Carsem was founded in 1972.

**Key Japanese Supply Chain Links:**
- Tokyo Seimitsu (CMP-0001) --> MPI Berhad: probing, dicing (Malaysia OSAT)
- DISCO (CMP-0002) --> MPI Berhad: dicing saws

---

## Summary: Japan's Reach Across the Global Ecosystem

Across all 48 non-Japanese companies profiled in this appendix, the pattern is consistent. Tokyo Seimitsu (ACCRETECH) and DISCO together supply probing and dicing equipment to nearly every foundry and OSAT company in the graph, regardless of geography. Tokyo Electron's coater/developers, etch, and deposition tools are present at every leading-edge foundry. Stella Chemifa's ultra-high purity hydrofluoric acid, Organo's ultrapure water systems, and PILLAR's mechanical seals flow into fabs from Taiwan to China to Singapore. Even companies explicitly designed to replace Japanese equipment -- NAURA, Huahai Qingke, Sidea, SEMES, SEMICS -- define themselves in relation to the Japanese incumbents they are attempting to displace.

The edges in `graph.json` make the dependency quantifiable: of the 48 companies profiled here, 35 have direct supplier edges from Japanese companies, 13 have competitor edges with Japanese companies, and several have both. Japan's semiconductor infrastructure is not merely a supply chain participant; it is the substrate upon which the global ecosystem is built.
