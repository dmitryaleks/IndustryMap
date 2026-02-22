# Appendix C: Supply Chain Edge List

> Complete listing of all 324 supply chain relationships in the semiconductor industry graph.

This appendix reproduces every directed edge from the project's supply chain graph (`graph.json` v4.0.0, generated 2026-02-21). Each edge connects a **source** company to a **target** company and carries a type classification and an optional descriptive label. Edges are grouped by type and sorted by source ID, then target ID, within each section.

**Note on edge counts:** The `graph.json` header records 321 edges (263 supplier), but the actual edges array contains 324 edges (266 supplier) following the Wave 6 Gun Ei Chemical update. This appendix lists all edges present in the data.

## Overview

| Metric | Count |
|--------|-------|
| **Total edges** | 324 |
| Supplier relationships | 266 |
| Competitor relationships | 42 |
| Partner relationships | 4 |
| Ecosystem relationships | 12 |

**Reading the tables:** The Source supplies to, competes with, partners with, or shares an ecosystem with the Target. Labels describe the product, service, or nature of the relationship. Where no label was recorded in the source data, the cell shows "---".

---

## Supplier Relationships (266)

| # | Source | Source Name | Target | Target Name | Label |
|---|--------|-------------|--------|-------------|-------|
| 1 | CMP-0001 | Tokyo Seimitsu | CMP-0014 | Kioxia Holdings | probing, dicing equipment |
| 2 | CMP-0001 | Tokyo Seimitsu | CMP-0017 | TSMC | probing, dicing, CMP equipment |
| 3 | CMP-0001 | Tokyo Seimitsu | CMP-0018 | Samsung Electronics | probing, dicing equipment |
| 4 | CMP-0001 | Tokyo Seimitsu | CMP-0019 | Intel | probing, dicing equipment |
| 5 | CMP-0001 | Tokyo Seimitsu | CMP-0020 | SK Hynix | probing, dicing equipment |
| 6 | CMP-0001 | Tokyo Seimitsu | CMP-0021 | Micron | probing, dicing equipment |
| 7 | CMP-0001 | Tokyo Seimitsu | CMP-0063 | ASE Technology | dicing, probing equipment (OSAT #1) |
| 8 | CMP-0001 | Tokyo Seimitsu | CMP-0064 | Amkor Technology | dicing, probing equipment (OSAT #2) |
| 9 | CMP-0001 | Tokyo Seimitsu | CMP-0065 | JCET Group | dicing, probing equipment (China OSAT #1) |
| 10 | CMP-0001 | Tokyo Seimitsu | CMP-0066 | SMIC | CMP, probing, dicing (China foundry #1) |
| 11 | CMP-0001 | Tokyo Seimitsu | CMP-0067 | Tongfu Microelectronics | dicing, probing equipment (China OSAT #2) |
| 12 | CMP-0001 | Tokyo Seimitsu | CMP-0068 | Tianshui Huatian | dicing, probing equipment (China OSAT #3) |
| 13 | CMP-0001 | Tokyo Seimitsu | CMP-0069 | Powertech Technology | dicing, probing equipment (Taiwan memory OSAT) |
| 14 | CMP-0001 | Tokyo Seimitsu | CMP-0070 | Hua Hong Semiconductor | CMP, probing equipment (China foundry #2) |
| 15 | CMP-0001 | Tokyo Seimitsu | CMP-0075 | DB HiTek Co., Ltd. | probing, dicing, CMP equipment (Korea #2 foundry) |
| 16 | CMP-0001 | Tokyo Seimitsu | CMP-0076 | HANA Micron Inc. | probing, dicing equipment (Korea #1 OSAT) |
| 17 | CMP-0001 | Tokyo Seimitsu | CMP-0077 | Nepes Corporation | probing, dicing equipment (Korea OSAT) |
| 18 | CMP-0001 | Tokyo Seimitsu | CMP-0078 | SFA Semicon Co., Ltd. | probing, dicing equipment (Korea OSAT) |
| 19 | CMP-0001 | Tokyo Seimitsu | CMP-0079 | LB Semicon Co., Ltd. | probing, dicing equipment (Korea OSAT) |
| 20 | CMP-0001 | Tokyo Seimitsu | CMP-0083 | Nexchip Semiconductor Corporation | probing, dicing, CMP (China #3 foundry) |
| 21 | CMP-0001 | Tokyo Seimitsu | CMP-0084 | China Resources Microelectronics Limited | probing, dicing (China IDM) |
| 22 | CMP-0001 | Tokyo Seimitsu | CMP-0093 | Yangtze Memory Technologies Co., Ltd. | CMP, probing, dicing (China NAND, pre-sanctions) |
| 23 | CMP-0001 | Tokyo Seimitsu | CMP-0094 | CanSemi Technology Co., Ltd. | probing, dicing, CMP (Guangzhou foundry) |
| 24 | CMP-0001 | Tokyo Seimitsu | CMP-0095 | GTA Semiconductor Co., Ltd. | probing, dicing (Shanghai specialty foundry) |
| 25 | CMP-0001 | Tokyo Seimitsu | CMP-0100 | SurplusGLOBAL Inc. | --- |
| 26 | CMP-0001 | Tokyo Seimitsu | CMP-0101 | King Yuan Electronics Co., Ltd. | probing equipment (world #1 pure-play tester) |
| 27 | CMP-0001 | Tokyo Seimitsu | CMP-0102 | United Microelectronics Corporation | CMP, probing, dicing (Taiwan #2 foundry) |
| 28 | CMP-0001 | Tokyo Seimitsu | CMP-0103 | Vanguard International Semiconductor Corporation | CMP, probing, dicing (Taiwan specialty foundry) |
| 29 | CMP-0001 | Tokyo Seimitsu | CMP-0104 | Chipbond Technology Corporation | probing, dicing (Taiwan OSAT) |
| 30 | CMP-0001 | Tokyo Seimitsu | CMP-0105 | ChipMOS Technologies Inc. | probing, dicing (Taiwan OSAT) |
| 31 | CMP-0001 | Tokyo Seimitsu | CMP-0106 | GlobalFoundries Inc. | CMP, probing, dicing (Singapore fabs) |
| 32 | CMP-0001 | Tokyo Seimitsu | CMP-0107 | UTAC Holdings Ltd. | probing, dicing (Singapore OSAT) |
| 33 | CMP-0001 | Tokyo Seimitsu | CMP-0108 | Inari Amertron Berhad | probing, dicing (Malaysia #1 OSAT) |
| 34 | CMP-0001 | Tokyo Seimitsu | CMP-0109 | Unisem (M) Berhad | probing, dicing (Malaysia OSAT) |
| 35 | CMP-0001 | Tokyo Seimitsu | CMP-0110 | Malaysian Pacific Industries Berhad | probing, dicing (Malaysia OSAT) |
| 36 | CMP-0002 | DISCO | CMP-0063 | ASE Technology | dicing saws, blades |
| 37 | CMP-0002 | DISCO | CMP-0064 | Amkor Technology | dicing saws, blades |
| 38 | CMP-0002 | DISCO | CMP-0065 | JCET Group | dicing saws, blades |
| 39 | CMP-0002 | DISCO | CMP-0067 | Tongfu Microelectronics | dicing saws, blades |
| 40 | CMP-0002 | DISCO | CMP-0068 | Tianshui Huatian | dicing saws, blades |
| 41 | CMP-0002 | DISCO | CMP-0069 | Powertech Technology | dicing saws, blades |
| 42 | CMP-0002 | DISCO | CMP-0100 | SurplusGLOBAL Inc. | --- |
| 43 | CMP-0002 | DISCO | CMP-0101 | King Yuan Electronics Co., Ltd. | dicing saws |
| 44 | CMP-0002 | DISCO | CMP-0104 | Chipbond Technology Corporation | dicing saws |
| 45 | CMP-0002 | DISCO | CMP-0105 | ChipMOS Technologies Inc. | dicing saws |
| 46 | CMP-0002 | DISCO | CMP-0107 | UTAC Holdings Ltd. | dicing saws |
| 47 | CMP-0002 | DISCO | CMP-0108 | Inari Amertron Berhad | dicing saws |
| 48 | CMP-0002 | DISCO | CMP-0109 | Unisem (M) Berhad | dicing saws |
| 49 | CMP-0002 | DISCO | CMP-0110 | Malaysian Pacific Industries Berhad | dicing saws |
| 50 | CMP-0003 | SCREEN Holdings | CMP-0017 | TSMC | wafer cleaning |
| 51 | CMP-0004 | Tokyo Electron | CMP-0017 | TSMC | coater/developers, etch, CVD |
| 52 | CMP-0004 | Tokyo Electron | CMP-0018 | Samsung Electronics | deposition equipment |
| 53 | CMP-0004 | Tokyo Electron | CMP-0019 | Intel | deposition equipment |
| 54 | CMP-0004 | Tokyo Electron | CMP-0020 | SK Hynix | deposition equipment |
| 55 | CMP-0004 | Tokyo Electron | CMP-0063 | ASE Technology | --- |
| 56 | CMP-0004 | Tokyo Electron | CMP-0064 | Amkor Technology | --- |
| 57 | CMP-0004 | Tokyo Electron | CMP-0066 | SMIC | coater/developer, etch, CVD |
| 58 | CMP-0004 | Tokyo Electron | CMP-0070 | Hua Hong Semiconductor | deposition equipment |
| 59 | CMP-0004 | Tokyo Electron | CMP-0100 | SurplusGLOBAL Inc. | --- |
| 60 | CMP-0004 | Tokyo Electron | CMP-0102 | United Microelectronics Corporation | --- |
| 61 | CMP-0004 | Tokyo Electron | CMP-0106 | GlobalFoundries Inc. | --- |
| 62 | CMP-0005 | Advantest | CMP-0017 | TSMC | test equipment |
| 63 | CMP-0005 | Advantest | CMP-0018 | Samsung Electronics | test equipment |
| 64 | CMP-0005 | Advantest | CMP-0020 | SK Hynix | test equipment |
| 65 | CMP-0005 | Advantest | CMP-0021 | Micron | test equipment |
| 66 | CMP-0005 | Advantest | CMP-0063 | ASE Technology | test equipment |
| 67 | CMP-0005 | Advantest | CMP-0064 | Amkor Technology | test equipment |
| 68 | CMP-0005 | Advantest | CMP-0101 | King Yuan Electronics Co., Ltd. | --- |
| 69 | CMP-0006 | Lasertec | CMP-0017 | TSMC | EUV mask inspection |
| 70 | CMP-0006 | Lasertec | CMP-0018 | Samsung Electronics | EUV mask inspection |
| 71 | CMP-0006 | Lasertec | CMP-0019 | Intel | EUV mask inspection |
| 72 | CMP-0007 | Fujimi | CMP-0017 | TSMC | CMP slurry |
| 73 | CMP-0007 | Fujimi | CMP-0019 | Intel | CMP slurry |
| 74 | CMP-0008 | Resonac Holdings | CMP-0017 | TSMC | semiconductor materials |
| 75 | CMP-0008 | Resonac Holdings | CMP-0018 | Samsung Electronics | semiconductor materials |
| 76 | CMP-0008 | Resonac Holdings | CMP-0019 | Intel | semiconductor materials |
| 77 | CMP-0010 | Toyo Gosei | CMP-0017 | TSMC | photoresist materials |
| 78 | CMP-0010 | Toyo Gosei | CMP-0018 | Samsung Electronics | photoresist materials |
| 79 | CMP-0010 | Toyo Gosei | CMP-0019 | Intel | photoresist materials |
| 80 | CMP-0011 | Kokusai Electric | CMP-0014 | Kioxia Holdings | batch deposition |
| 81 | CMP-0011 | Kokusai Electric | CMP-0018 | Samsung Electronics | batch deposition |
| 82 | CMP-0011 | Kokusai Electric | CMP-0019 | Intel | batch deposition |
| 83 | CMP-0011 | Kokusai Electric | CMP-0020 | SK Hynix | batch deposition |
| 84 | CMP-0011 | Kokusai Electric | CMP-0021 | Micron | batch deposition |
| 85 | CMP-0011 | Kokusai Electric | CMP-0066 | SMIC | batch deposition |
| 86 | CMP-0013 | Fuso Chemical | CMP-0017 | TSMC | CMP slurry |
| 87 | CMP-0013 | Fuso Chemical | CMP-0018 | Samsung Electronics | CMP slurry |
| 88 | CMP-0013 | Fuso Chemical | CMP-0019 | Intel | CMP slurry |
| 89 | CMP-0014 | Kioxia Holdings | CMP-0022 | Apple | NAND flash |
| 90 | CMP-0015 | HOYA | CMP-0017 | TSMC | photomask blanks |
| 91 | CMP-0015 | HOYA | CMP-0018 | Samsung Electronics | photomask blanks |
| 92 | CMP-0015 | HOYA | CMP-0019 | Intel | photomask blanks |
| 93 | CMP-0015 | HOYA | CMP-0020 | SK Hynix | photomask blanks |
| 94 | CMP-0015 | HOYA | CMP-0047 | TOPPAN Holdings | --- |
| 95 | CMP-0015 | HOYA | CMP-0049 | Dai Nippon Printing | --- |
| 96 | CMP-0017 | TSMC | CMP-0022 | Apple | chip manufacturing |
| 97 | CMP-0017 | TSMC | CMP-0028 | NVIDIA | chip manufacturing |
| 98 | CMP-0020 | SK Hynix | CMP-0028 | NVIDIA | HBM memory |
| 99 | CMP-0024 | Shin-Etsu Chemical | CMP-0017 | TSMC | silicon wafers |
| 100 | CMP-0024 | Shin-Etsu Chemical | CMP-0018 | Samsung Electronics | silicon wafers |
| 101 | CMP-0024 | Shin-Etsu Chemical | CMP-0019 | Intel | silicon wafers |
| 102 | CMP-0024 | Shin-Etsu Chemical | CMP-0020 | SK Hynix | silicon wafers |
| 103 | CMP-0024 | Shin-Etsu Chemical | CMP-0021 | Micron | silicon wafers |
| 104 | CMP-0025 | SUMCO | CMP-0017 | TSMC | silicon wafers |
| 105 | CMP-0025 | SUMCO | CMP-0018 | Samsung Electronics | silicon wafers |
| 106 | CMP-0025 | SUMCO | CMP-0019 | Intel | silicon wafers |
| 107 | CMP-0025 | SUMCO | CMP-0020 | SK Hynix | silicon wafers |
| 108 | CMP-0025 | SUMCO | CMP-0021 | Micron | silicon wafers |
| 109 | CMP-0026 | ASML | CMP-0017 | TSMC | EUV lithography |
| 110 | CMP-0026 | ASML | CMP-0018 | Samsung Electronics | EUV lithography |
| 111 | CMP-0026 | ASML | CMP-0019 | Intel | EUV lithography |
| 112 | CMP-0026 | ASML | CMP-0020 | SK Hynix | EUV lithography |
| 113 | CMP-0026 | ASML | CMP-0021 | Micron | EUV lithography |
| 114 | CMP-0026 | ASML | CMP-0066 | SMIC | DUV lithography |
| 115 | CMP-0026 | ASML | CMP-0102 | United Microelectronics Corporation | --- |
| 116 | CMP-0026 | ASML | CMP-0106 | GlobalFoundries Inc. | --- |
| 117 | CMP-0029 | Naigai Tech | CMP-0004 | Tokyo Electron | precision machining parts (80% sales) |
| 118 | CMP-0030 | Marumae | CMP-0003 | SCREEN Holdings | aluminum vacuum chambers |
| 119 | CMP-0030 | Marumae | CMP-0004 | Tokyo Electron | aluminum vacuum chambers |
| 120 | CMP-0031 | Tocalo | CMP-0003 | SCREEN Holdings | thermal spray coating |
| 121 | CMP-0031 | Tocalo | CMP-0004 | Tokyo Electron | thermal spray coating |
| 122 | CMP-0032 | Nippon Sanso | CMP-0017 | TSMC | specialty gases |
| 123 | CMP-0032 | Nippon Sanso | CMP-0018 | Samsung Electronics | specialty gases |
| 124 | CMP-0032 | Nippon Sanso | CMP-0019 | Intel | specialty gases |
| 125 | CMP-0032 | Nippon Sanso | CMP-0020 | SK Hynix | specialty gases |
| 126 | CMP-0032 | Nippon Sanso | CMP-0021 | Micron | specialty gases |
| 127 | CMP-0033 | Tokyo Ohka Kogyo | CMP-0014 | Kioxia Holdings | --- |
| 128 | CMP-0033 | Tokyo Ohka Kogyo | CMP-0017 | TSMC | photoresist (25% world share) |
| 129 | CMP-0033 | Tokyo Ohka Kogyo | CMP-0018 | Samsung Electronics | photoresist |
| 130 | CMP-0033 | Tokyo Ohka Kogyo | CMP-0019 | Intel | photoresist |
| 131 | CMP-0034 | JSR | CMP-0017 | TSMC | EUV photoresist |
| 132 | CMP-0034 | JSR | CMP-0018 | Samsung Electronics | EUV photoresist |
| 133 | CMP-0034 | JSR | CMP-0019 | Intel | EUV photoresist |
| 134 | CMP-0035 | Maruzen Petrochemical | CMP-0033 | Tokyo Ohka Kogyo | high-purity aromatics |
| 135 | CMP-0035 | Maruzen Petrochemical | CMP-0034 | JSR | high-purity aromatics |
| 136 | CMP-0036 | Ebara | CMP-0017 | TSMC | CMP systems, vacuum pumps |
| 137 | CMP-0036 | Ebara | CMP-0018 | Samsung Electronics | CMP systems, vacuum pumps |
| 138 | CMP-0036 | Ebara | CMP-0019 | Intel | CMP systems, vacuum pumps |
| 139 | CMP-0036 | Ebara | CMP-0020 | SK Hynix | --- |
| 140 | CMP-0036 | Ebara | CMP-0021 | Micron | --- |
| 141 | CMP-0037 | NGK Insulators | CMP-0003 | SCREEN Holdings | --- |
| 142 | CMP-0037 | NGK Insulators | CMP-0004 | Tokyo Electron | --- |
| 143 | CMP-0037 | NGK Insulators | CMP-0017 | TSMC | ceramic electrostatic chucks |
| 144 | CMP-0037 | NGK Insulators | CMP-0018 | Samsung Electronics | ceramic electrostatic chucks |
| 145 | CMP-0038 | Gun Ei Chemical | CMP-0024 | Shin-Etsu Chemical | novolac resins for photoresist |
| 146 | CMP-0038 | Gun Ei Chemical | CMP-0033 | Tokyo Ohka Kogyo | photosensitive resin materials |
| 147 | CMP-0038 | Gun Ei Chemical | CMP-0034 | JSR | photosensitive resin materials |
| 148 | CMP-0038 | Gun Ei Chemical | CMP-0040 | FUJIFILM Holdings | novolac resins for photoresist |
| 149 | CMP-0038 | Gun Ei Chemical | CMP-0046 | Sumitomo Chemical | novolac resins for photoresist |
| 150 | CMP-0039 | Niterra | CMP-0004 | Tokyo Electron | --- |
| 151 | CMP-0039 | Niterra | CMP-0017 | TSMC | IC package substrates |
| 152 | CMP-0039 | Niterra | CMP-0018 | Samsung Electronics | IC package substrates |
| 153 | CMP-0040 | FUJIFILM Holdings | CMP-0017 | TSMC | CMP slurry, photoresist |
| 154 | CMP-0040 | FUJIFILM Holdings | CMP-0018 | Samsung Electronics | CMP slurry, photoresist |
| 155 | CMP-0040 | FUJIFILM Holdings | CMP-0019 | Intel | --- |
| 156 | CMP-0041 | Rorze | CMP-0003 | SCREEN Holdings | wafer transfer robots |
| 157 | CMP-0041 | Rorze | CMP-0004 | Tokyo Electron | wafer transfer robots |
| 158 | CMP-0041 | Rorze | CMP-0017 | TSMC | wafer handling systems |
| 159 | CMP-0041 | Rorze | CMP-0018 | Samsung Electronics | --- |
| 160 | CMP-0042 | PILLAR | CMP-0003 | SCREEN Holdings | mechanical seals, bellows |
| 161 | CMP-0042 | PILLAR | CMP-0004 | Tokyo Electron | mechanical seals, bellows |
| 162 | CMP-0042 | PILLAR | CMP-0011 | Kokusai Electric | --- |
| 163 | CMP-0042 | PILLAR | CMP-0017 | TSMC | --- |
| 164 | CMP-0042 | PILLAR | CMP-0018 | Samsung Electronics | --- |
| 165 | CMP-0042 | PILLAR | CMP-0019 | Intel | --- |
| 166 | CMP-0042 | PILLAR | CMP-0020 | SK Hynix | --- |
| 167 | CMP-0042 | PILLAR | CMP-0036 | Ebara | --- |
| 168 | CMP-0042 | PILLAR | CMP-0043 | CKD | --- |
| 169 | CMP-0042 | PILLAR | CMP-0059 | Shibaura Mechatronics | --- |
| 170 | CMP-0042 | PILLAR | CMP-0060 | Samco | --- |
| 171 | CMP-0042 | PILLAR | CMP-0066 | SMIC | --- |
| 172 | CMP-0042 | PILLAR | CMP-0070 | Hua Hong Semiconductor | --- |
| 173 | CMP-0042 | PILLAR | CMP-0096 | SEMES Co., Ltd. | --- |
| 174 | CMP-0043 | CKD | CMP-0003 | SCREEN Holdings | pneumatic valves |
| 175 | CMP-0043 | CKD | CMP-0004 | Tokyo Electron | pneumatic valves |
| 176 | CMP-0043 | CKD | CMP-0011 | Kokusai Electric | pneumatic valves |
| 177 | CMP-0044 | Stella Chemifa | CMP-0014 | Kioxia Holdings | --- |
| 178 | CMP-0044 | Stella Chemifa | CMP-0017 | TSMC | 12-nine purity HF acid |
| 179 | CMP-0044 | Stella Chemifa | CMP-0018 | Samsung Electronics | 12-nine purity HF acid |
| 180 | CMP-0044 | Stella Chemifa | CMP-0019 | Intel | ultra-high purity HF |
| 181 | CMP-0044 | Stella Chemifa | CMP-0020 | SK Hynix | ultra-high purity HF |
| 182 | CMP-0044 | Stella Chemifa | CMP-0021 | Micron | ultra-high purity HF |
| 183 | CMP-0044 | Stella Chemifa | CMP-0066 | SMIC | --- |
| 184 | CMP-0044 | Stella Chemifa | CMP-0070 | Hua Hong Semiconductor | --- |
| 185 | CMP-0044 | Stella Chemifa | CMP-0102 | United Microelectronics Corporation | --- |
| 186 | CMP-0044 | Stella Chemifa | CMP-0106 | GlobalFoundries Inc. | --- |
| 187 | CMP-0045 | Kanto Denka Kogyo | CMP-0017 | TSMC | specialty fluorine gases |
| 188 | CMP-0045 | Kanto Denka Kogyo | CMP-0018 | Samsung Electronics | specialty fluorine gases |
| 189 | CMP-0045 | Kanto Denka Kogyo | CMP-0019 | Intel | --- |
| 190 | CMP-0046 | Sumitomo Chemical | CMP-0017 | TSMC | photoresist (via Sumitomo Bakelite) |
| 191 | CMP-0046 | Sumitomo Chemical | CMP-0018 | Samsung Electronics | photoresist |
| 192 | CMP-0046 | Sumitomo Chemical | CMP-0019 | Intel | --- |
| 193 | CMP-0047 | TOPPAN Holdings | CMP-0017 | TSMC | EUV photomasks (with Mitsui) |
| 194 | CMP-0047 | TOPPAN Holdings | CMP-0018 | Samsung Electronics | --- |
| 195 | CMP-0047 | TOPPAN Holdings | CMP-0019 | Intel | --- |
| 196 | CMP-0048 | Ibiden | CMP-0017 | TSMC | high-end FC-BGA substrates |
| 197 | CMP-0048 | Ibiden | CMP-0019 | Intel | --- |
| 198 | CMP-0048 | Ibiden | CMP-0028 | NVIDIA | AI server IC substrates (50%+) |
| 199 | CMP-0049 | Dai Nippon Printing | CMP-0017 | TSMC | photomask production |
| 200 | CMP-0049 | Dai Nippon Printing | CMP-0018 | Samsung Electronics | --- |
| 201 | CMP-0049 | Dai Nippon Printing | CMP-0019 | Intel | --- |
| 202 | CMP-0049 | Dai Nippon Printing | CMP-0026 | ASML | nanoimprint lithography |
| 203 | CMP-0050 | Nikon | CMP-0017 | TSMC | i-line/KrF steppers |
| 204 | CMP-0050 | Nikon | CMP-0018 | Samsung Electronics | lithography equipment |
| 205 | CMP-0050 | Nikon | CMP-0019 | Intel | --- |
| 206 | CMP-0051 | Canon | CMP-0017 | TSMC | i-line/KrF steppers |
| 207 | CMP-0051 | Canon | CMP-0018 | Samsung Electronics | lithography equipment |
| 208 | CMP-0051 | Canon | CMP-0019 | Intel | nanoimprint lithography |
| 209 | CMP-0052 | Organo | CMP-0017 | TSMC | ultrapure water systems |
| 210 | CMP-0052 | Organo | CMP-0018 | Samsung Electronics | ultrapure water systems |
| 211 | CMP-0052 | Organo | CMP-0066 | SMIC | --- |
| 212 | CMP-0052 | Organo | CMP-0070 | Hua Hong Semiconductor | --- |
| 213 | CMP-0053 | Nomura Micro Science | CMP-0017 | TSMC | ultrapure water systems |
| 214 | CMP-0053 | Nomura Micro Science | CMP-0018 | Samsung Electronics | --- |
| 215 | CMP-0053 | Nomura Micro Science | CMP-0020 | SK Hynix | ultrapure water systems |
| 216 | CMP-0054 | Aval Data | CMP-0004 | Tokyo Electron | --- |
| 217 | CMP-0054 | Aval Data | CMP-0005 | Advantest | tester boards/probes |
| 218 | CMP-0054 | Aval Data | CMP-0018 | Samsung Electronics | test equipment components |
| 219 | CMP-0054 | Aval Data | CMP-0050 | Nikon | --- |
| 220 | CMP-0055 | NHK Spring | CMP-0005 | Advantest | probe card springs |
| 221 | CMP-0055 | NHK Spring | CMP-0017 | TSMC | HDD suspension (50% share) |
| 222 | CMP-0056 | Daifuku | CMP-0017 | TSMC | cleanroom AMHS |
| 223 | CMP-0056 | Daifuku | CMP-0018 | Samsung Electronics | cleanroom AMHS |
| 224 | CMP-0056 | Daifuku | CMP-0019 | Intel | cleanroom AMHS |
| 225 | CMP-0057 | MEC Company | CMP-0017 | TSMC | PCB surface treatment |
| 226 | CMP-0057 | MEC Company | CMP-0048 | Ibiden | copper surface treatment |
| 227 | CMP-0058 | Nagase | CMP-0017 | TSMC | electronic chemicals |
| 228 | CMP-0058 | Nagase | CMP-0033 | Tokyo Ohka Kogyo | chemical distribution |
| 229 | CMP-0058 | Nagase | CMP-0034 | JSR | chemical distribution |
| 230 | CMP-0059 | Shibaura Mechatronics | CMP-0017 | TSMC | plasma processing equipment |
| 231 | CMP-0059 | Shibaura Mechatronics | CMP-0018 | Samsung Electronics | plasma processing equipment |
| 232 | CMP-0060 | Samco | CMP-0017 | TSMC | plasma CVD equipment |
| 233 | CMP-0060 | Samco | CMP-0018 | Samsung Electronics | dry etching equipment |
| 234 | CMP-0061 | Ushio | CMP-0050 | Nikon | i-line UV lamps (75% share) |
| 235 | CMP-0061 | Ushio | CMP-0051 | Canon | i-line UV lamps |
| 236 | CMP-0062 | Tazmo | CMP-0017 | TSMC | coater/developer equipment |
| 237 | CMP-0062 | Tazmo | CMP-0018 | Samsung Electronics | coating equipment |
| 238 | CMP-0066 | SMIC | CMP-0090 | GigaDevice Semiconductor Inc. | --- |
| 239 | CMP-0069 | Powertech Technology | CMP-0021 | Micron | memory packaging (key Micron supplier) |
| 240 | CMP-0072 | Hanmi Semiconductor | CMP-0020 | SK Hynix | TC bonders for HBM (71% share) |
| 241 | CMP-0072 | Hanmi Semiconductor | CMP-0021 | Micron | TC bonders for HBM |
| 242 | CMP-0072 | Hanmi Semiconductor | CMP-0063 | ASE Technology | flip chip bonders |
| 243 | CMP-0076 | HANA Micron Inc. | CMP-0018 | Samsung Electronics | --- |
| 244 | CMP-0076 | HANA Micron Inc. | CMP-0020 | SK Hynix | --- |
| 245 | CMP-0078 | SFA Semicon Co., Ltd. | CMP-0018 | Samsung Electronics | --- |
| 246 | CMP-0080 | Techwing Inc. | CMP-0018 | Samsung Electronics | memory test handlers |
| 247 | CMP-0080 | Techwing Inc. | CMP-0020 | SK Hynix | memory test handlers |
| 248 | CMP-0081 | KCTech Co., Ltd. | CMP-0018 | Samsung Electronics | CMP equipment, slurry (VENTUS system) |
| 249 | CMP-0081 | KCTech Co., Ltd. | CMP-0020 | SK Hynix | CMP equipment, cleaning, slurry |
| 250 | CMP-0082 | Leeno Industrial Inc. | CMP-0017 | TSMC | --- |
| 251 | CMP-0082 | Leeno Industrial Inc. | CMP-0018 | Samsung Electronics | --- |
| 252 | CMP-0082 | Leeno Industrial Inc. | CMP-0028 | NVIDIA | --- |
| 253 | CMP-0083 | Nexchip Semiconductor Corporation | CMP-0090 | GigaDevice Semiconductor Inc. | --- |
| 254 | CMP-0085 | NAURA Technology Group Co., Ltd. | CMP-0066 | SMIC | etching, deposition, cleaning |
| 255 | CMP-0085 | NAURA Technology Group Co., Ltd. | CMP-0070 | Hua Hong Semiconductor | process equipment |
| 256 | CMP-0088 | Hwatsing Technology Co., Ltd. (Huahai Qingke) | CMP-0066 | SMIC | CMP equipment |
| 257 | CMP-0088 | Hwatsing Technology Co., Ltd. (Huahai Qingke) | CMP-0070 | Hua Hong Semiconductor | CMP equipment |
| 258 | CMP-0088 | Hwatsing Technology Co., Ltd. (Huahai Qingke) | CMP-0093 | Yangtze Memory Technologies Co., Ltd. | --- |
| 259 | CMP-0096 | SEMES Co., Ltd. | CMP-0018 | Samsung Electronics | probers, photo track, cleaning (Samsung captive) |
| 260 | CMP-0097 | SEMICS Inc. | CMP-0018 | Samsung Electronics | wafer probers (15yr relationship) |
| 261 | CMP-0097 | SEMICS Inc. | CMP-0020 | SK Hynix | wafer probers |
| 262 | CMP-0098 | WONIK IPS Co., Ltd. | CMP-0018 | Samsung Electronics | PECVD, ALD, thermal equipment |
| 263 | CMP-0098 | WONIK IPS Co., Ltd. | CMP-0020 | SK Hynix | deposition equipment |
| 264 | CMP-0099 | EO Technics Co., Ltd. | CMP-0018 | Samsung Electronics | laser dicing, marking, annealing |
| 265 | CMP-0099 | EO Technics Co., Ltd. | CMP-0020 | SK Hynix | laser stealth dicing for HBM |
| 266 | CMP-0100 | SurplusGLOBAL Inc. | CMP-0075 | DB HiTek Co., Ltd. | --- |

---

## Competitor Relationships (42)

| # | Source | Source Name | Target | Target Name | Label |
|---|--------|-------------|--------|-------------|-------|
| 1 | CMP-0001 | Tokyo Seimitsu | CMP-0002 | DISCO | dicing equipment |
| 2 | CMP-0001 | Tokyo Seimitsu | CMP-0071 | MPI Corporation | probing equipment |
| 3 | CMP-0001 | Tokyo Seimitsu | CMP-0072 | Hanmi Semiconductor | package singulation equipment |
| 4 | CMP-0001 | Tokyo Seimitsu | CMP-0073 | Sidea Semiconductor | probing equipment (China domestic) |
| 5 | CMP-0001 | Tokyo Seimitsu | CMP-0074 | Guangli Technology | dicing equipment |
| 6 | CMP-0001 | Tokyo Seimitsu | CMP-0085 | NAURA Technology Group Co., Ltd. | CMP, probing equipment |
| 7 | CMP-0001 | Tokyo Seimitsu | CMP-0087 | Hangzhou Changchuan Technology Co., Ltd. | probing equipment (China) |
| 8 | CMP-0001 | Tokyo Seimitsu | CMP-0088 | Hwatsing Technology Co., Ltd. (Huahai Qingke) | CMP equipment (China #1 CMP) |
| 9 | CMP-0001 | Tokyo Seimitsu | CMP-0089 | Shenyang Heyan Technology Co., Ltd. | dicing equipment (China) |
| 10 | CMP-0001 | Tokyo Seimitsu | CMP-0091 | Beijing Shuoke Jingwei Electronics Equipment Co., Ltd. | CMP, dicing equipment (China state-owned) |
| 11 | CMP-0001 | Tokyo Seimitsu | CMP-0092 | Beijing TSD Semiconductor Equipment Co., Ltd. | CMP, grinding (compound semi) |
| 12 | CMP-0001 | Tokyo Seimitsu | CMP-0096 | SEMES Co., Ltd. | probing equipment (Korea Samsung captive) |
| 13 | CMP-0001 | Tokyo Seimitsu | CMP-0097 | SEMICS Inc. | probing equipment (Korea world #3) |
| 14 | CMP-0001 | Tokyo Seimitsu | CMP-0099 | EO Technics Co., Ltd. | dicing equipment (laser vs blade) |
| 15 | CMP-0002 | DISCO | CMP-0001 | Tokyo Seimitsu | dicing equipment |
| 16 | CMP-0002 | DISCO | CMP-0074 | Guangli Technology | dicing equipment |
| 17 | CMP-0002 | DISCO | CMP-0099 | EO Technics Co., Ltd. | dicing equipment (laser vs blade) |
| 18 | CMP-0018 | Samsung Electronics | CMP-0020 | SK Hynix | memory |
| 19 | CMP-0018 | Samsung Electronics | CMP-0021 | Micron | memory |
| 20 | CMP-0024 | Shin-Etsu Chemical | CMP-0025 | SUMCO | silicon wafers |
| 21 | CMP-0025 | SUMCO | CMP-0024 | Shin-Etsu Chemical | silicon wafers |
| 22 | CMP-0026 | ASML | CMP-0050 | Nikon | lithography equipment |
| 23 | CMP-0026 | ASML | CMP-0051 | Canon | lithography equipment |
| 24 | CMP-0050 | Nikon | CMP-0026 | ASML | lithography equipment |
| 25 | CMP-0051 | Canon | CMP-0026 | ASML | lithography equipment |
| 26 | CMP-0063 | ASE Technology | CMP-0064 | Amkor Technology | OSAT services |
| 27 | CMP-0063 | ASE Technology | CMP-0065 | JCET Group | OSAT services |
| 28 | CMP-0071 | MPI Corporation | CMP-0001 | Tokyo Seimitsu | probing equipment |
| 29 | CMP-0072 | Hanmi Semiconductor | CMP-0001 | Tokyo Seimitsu | package singulation equipment |
| 30 | CMP-0073 | Sidea Semiconductor | CMP-0001 | Tokyo Seimitsu | probing equipment (China domestic) |
| 31 | CMP-0074 | Guangli Technology | CMP-0001 | Tokyo Seimitsu | dicing equipment |
| 32 | CMP-0074 | Guangli Technology | CMP-0002 | DISCO | dicing equipment |
| 33 | CMP-0085 | NAURA Technology Group Co., Ltd. | CMP-0001 | Tokyo Seimitsu | CMP, probing equipment |
| 34 | CMP-0087 | Hangzhou Changchuan Technology Co., Ltd. | CMP-0001 | Tokyo Seimitsu | probing equipment (China) |
| 35 | CMP-0088 | Hwatsing Technology Co., Ltd. (Huahai Qingke) | CMP-0001 | Tokyo Seimitsu | CMP equipment (China #1 CMP) |
| 36 | CMP-0089 | Shenyang Heyan Technology Co., Ltd. | CMP-0001 | Tokyo Seimitsu | dicing equipment (China) |
| 37 | CMP-0091 | Beijing Shuoke Jingwei Electronics Equipment Co., Ltd. | CMP-0001 | Tokyo Seimitsu | CMP, dicing equipment (China state-owned) |
| 38 | CMP-0092 | Beijing TSD Semiconductor Equipment Co., Ltd. | CMP-0001 | Tokyo Seimitsu | CMP, grinding (compound semi) |
| 39 | CMP-0096 | SEMES Co., Ltd. | CMP-0001 | Tokyo Seimitsu | probing equipment (Korea Samsung captive) |
| 40 | CMP-0097 | SEMICS Inc. | CMP-0001 | Tokyo Seimitsu | probing equipment (Korea world #3) |
| 41 | CMP-0099 | EO Technics Co., Ltd. | CMP-0001 | Tokyo Seimitsu | dicing equipment (laser vs blade) |
| 42 | CMP-0099 | EO Technics Co., Ltd. | CMP-0002 | DISCO | dicing equipment (laser vs blade) |

---

## Partner Relationships (4)

| # | Source | Source Name | Target | Target Name | Label |
|---|--------|-------------|--------|-------------|-------|
| 1 | CMP-0001 | Tokyo Seimitsu | CMP-0005 | Advantest | die-level prober joint development (2025) |
| 2 | CMP-0005 | Advantest | CMP-0001 | Tokyo Seimitsu | die-level prober joint development (2025) |
| 3 | CMP-0014 | Kioxia Holdings | CMP-0023 | Western Digital | Yokkaichi/Kitakami JV |
| 4 | CMP-0023 | Western Digital | CMP-0014 | Kioxia Holdings | Yokkaichi/Kitakami JV |

---

## Ecosystem Relationships (12)

| # | Source | Source Name | Target | Target Name | Label |
|---|--------|-------------|--------|-------------|-------|
| 1 | CMP-0006 | Lasertec | CMP-0026 | ASML | EUV inspection + lithography |
| 2 | CMP-0015 | HOYA | CMP-0026 | ASML | EUV blanks + lithography |
| 3 | CMP-0026 | ASML | CMP-0006 | Lasertec | EUV lithography + inspection |
| 4 | CMP-0026 | ASML | CMP-0015 | HOYA | EUV lithography + blanks |
| 5 | CMP-0026 | ASML | CMP-0047 | TOPPAN Holdings | EUV lithography + masks |
| 6 | CMP-0026 | ASML | CMP-0049 | Dai Nippon Printing | nanoimprint partnership |
| 7 | CMP-0047 | TOPPAN Holdings | CMP-0026 | ASML | EUV photomask production |
| 8 | CMP-0049 | Dai Nippon Printing | CMP-0026 | ASML | EUV photomask partnership |
| 9 | CMP-0065 | JCET Group | CMP-0066 | SMIC | JCET packaging for SMIC chips |
| 10 | CMP-0066 | SMIC | CMP-0065 | JCET Group | SMIC is JCET 2nd largest shareholder |
| 11 | CMP-0068 | Tianshui Huatian | CMP-0109 | Unisem (M) Berhad | Huatian parent of Unisem Malaysia |
| 12 | CMP-0109 | Unisem (M) Berhad | CMP-0068 | Tianshui Huatian | Unisem subsidiary of Huatian |

---

## Notes on This Data

1. **Directionality.** All edges are directed. A supplier edge from A to B means "A supplies B." Competitor and ecosystem edges typically appear as symmetric pairs (A to B and B to A), reflecting the bidirectional nature of those relationships.

2. **Labels.** Labels are taken verbatim from the graph data. Where the original record contained no label, the cell displays "---". Labels sometimes include contextual annotations in parentheses (e.g., market share figures, geographic context, or ranking information).

3. **Sorting.** Within each section, edges are sorted first by the numeric portion of the source company ID, then by the numeric portion of the target company ID. This means all edges originating from CMP-0001 appear before those from CMP-0002, and within CMP-0001's edges, targets are listed in ascending ID order.

4. **Edge count discrepancy.** The `graph.json` statistics header reports 321 total edges (263 supplier), but the edges array contains 324 edges (266 supplier). The three additional supplier edges (CMP-0038 to CMP-0024, CMP-0040, and CMP-0046) were added during the Gun Ei Chemical deep research update and the statistics header was not updated. This appendix lists all 324 edges present in the data.

---

*Data source: `data/graph.json` v4.0.0 (110 nodes, 324 edges)*
