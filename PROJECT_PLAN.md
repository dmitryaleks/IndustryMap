# IndustryMap Project Plan

## Project Overview

**Objective:** Build a supply chain mapping and analysis system for Japanese semiconductor equipment companies, starting from a seed list of 16 companies and iteratively expanding the network by discovering suppliers and clients.

**Status Legend:**
- `[PENDING]` - Not started
- `[IN_PROGRESS]` - Currently being worked on
- `[DONE]` - Completed
- `[BLOCKED]` - Waiting on dependency

---

## Phase 1: Foundation Setup

### 1.1 Define JSON Schema [DONE]

Create formal JSON schema at `schema/company.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "company.schema.json",
  "title": "Company",
  "description": "A company node in the supply chain graph",
  "type": "object",
  "required": ["id", "companyName", "industryCode"],
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier (format: CMP-XXXX)",
      "pattern": "^CMP-[0-9]{4}$"
    },
    "companyName": {
      "type": "string",
      "description": "Company name in English"
    },
    "companyNameJapanese": {
      "type": "string",
      "description": "Company name in Japanese (for reference)"
    },
    "industryCode": {
      "type": "string",
      "description": "Short industry name in English",
      "examples": ["Semiconductors", "Semiconductor Equipment", "Chemicals"]
    },
    "ticker": {
      "type": ["string", "null"],
      "description": "Stock ticker symbol (e.g., 8035.T for Tokyo Stock Exchange)",
      "pattern": "^[0-9A-Z]+\\.[A-Z]+$"
    },
    "description": {
      "type": "string",
      "description": "Key products and business focus"
    },
    "marketCapInYen": {
      "type": ["number", "null"],
      "description": "Market capitalization in Japanese Yen"
    },
    "PER": {
      "type": ["number", "null"],
      "description": "Price to Earnings Ratio"
    },
    "PBR": {
      "type": ["number", "null"],
      "description": "Price to Book Ratio"
    },
    "EPS": {
      "type": ["number", "null"],
      "description": "Earnings Per Share (corrected from ESP in spec)"
    },
    "website": {
      "type": ["string", "null"],
      "format": "uri",
      "description": "Company website URL"
    },
    "percentOfForeignOwnership": {
      "type": ["number", "null"],
      "minimum": 0,
      "maximum": 100,
      "description": "Percentage of foreign institutional ownership"
    },
    "percentOfCirculatingEquity": {
      "type": ["number", "null"],
      "minimum": 0,
      "maximum": 100,
      "description": "Percentage of shares in public circulation"
    },
    "latestPriceYen": {
      "type": ["number", "null"],
      "description": "Latest stock price in JPY"
    },
    "isForexSensitive": {
      "type": ["boolean", "null"],
      "description": "Whether company revenue is significantly affected by USD/JPY"
    },
    "suppliers": {
      "type": "array",
      "items": { "type": "string", "pattern": "^CMP-[0-9]{4}$" },
      "description": "Array of supplier company IDs",
      "default": []
    },
    "clients": {
      "type": "array",
      "items": { "type": "string", "pattern": "^CMP-[0-9]{4}$" },
      "description": "Array of client company IDs",
      "default": []
    },
    "_metadata": {
      "type": "object",
      "properties": {
        "dataCollectedAt": { "type": "string", "format": "date-time" },
        "dataSource": { "type": "string" },
        "confidenceLevel": { "type": "string", "enum": ["high", "medium", "low"] },
        "lastUpdated": { "type": "string", "format": "date-time" }
      }
    }
  }
}
```

**Tasks:**
- [x] Create `schema/` directory
- [x] Write `company.schema.json`
- [ ] Create validation utility script

---

### 1.2 Create Directory Structure [DONE]

```
IndustryMap/
├── CLAUDE.md              # Project spec (exists)
├── PROJECT_PLAN.md        # This plan (exists)
├── schema/
│   └── company.schema.json
├── data/
│   ├── companies/         # Individual company JSON files
│   │   └── CMP-0001.json
│   ├── database.json      # Consolidated company database
│   └── graph.json         # Supply chain relationships
├── scripts/
│   ├── validate.py        # JSON validation
│   ├── merge_database.py  # Merge individual files
│   └── visualize.py       # Graph visualization
└── output/
    └── supply_chain.html  # Visual output
```

**Tasks:**
- [x] Create `schema/` directory
- [x] Create `data/companies/` directory
- [x] Create `scripts/` directory
- [x] Create `output/` directory
- [x] Create `data/database.json` template
- [x] Create `data/seed_companies.json` with resolved IDs

---

### 1.3 Seed Company Resolution [DONE]

Resolve all seed companies from CLAUDE.md to their full identities.

| # | Input | Company Name (EN) | Ticker | Status |
|---|-------|-------------------|--------|--------|
| 1 | Tokyo Seimitsu | Tokyo Seimitsu Co., Ltd. | 7729.T | [DONE] |
| 2 | Disco | DISCO Corporation | 6146.T | [DONE] |
| 3 | Screen | SCREEN Holdings Co., Ltd. | 7735.T | [DONE] |
| 4 | Tokyo Electron | Tokyo Electron Limited | 8035.T | [DONE] |
| 5 | Advantest | Advantest Corporation | 6857.T | [DONE] |
| 6 | Lasertech | Lasertec Corporation | 6920.T | [DONE] |
| 7 | Fujimi | Fujimi Incorporated | 5384.T | [DONE] |
| 8 | 4004.T | Resonac Holdings Corporation | 4004.T | [DONE] |
| 9 | 6890.T | Ferrotec Holdings Corporation | 6890.T | [DONE] |
| 10 | 4970.T | Toyo Gosei Co., Ltd. | 4970.T | [DONE] |
| 11 | 6525.T (Kokusai) | Kokusai Electric Corporation | 6525.T | [DONE] |
| 12 | 6856.T | Horiba, Ltd. | 6856.T | [DONE] |
| 13 | 4368.T | Fuso Chemical Co., Ltd. | 4368.T | [DONE] |
| 14 | 285A | Kioxia Holdings Corporation | 285A.T | [DONE] |
| 15 | Hoya (7741.T) | HOYA Corporation | 7741.T | [DONE] |
| 16 | Olympus (7733.T) | Olympus Corporation | 7733.T | [DONE] |

**Tasks:**
- [x] Research and verify each ticker symbol
- [x] Confirm company names in English
- [x] Identify any ticker symbol discrepancies (4368.T = Fuso Chemical, not Fuji Oil; 285A = Kioxia)

---

## Phase 2: Data Collection - Wave 1 (Seed Companies)

### 2.1 Data Collection Protocol [DONE]

For each seed company, collect:

1. **Basic Information**
   - Official company name (EN and JP)
   - Stock ticker and exchange
   - Official website URL
   - Industry classification

2. **Financial Metrics** (via web search)
   - Market capitalization (JPY)
   - PER, PBR, EPS
   - Latest stock price
   - Foreign ownership %
   - Circulating equity %

3. **Business Description**
   - Core products/services
   - Key business segments
   - USD/JPY sensitivity assessment

4. **Supply Chain Relationships** (critical)
   - Major suppliers (materials, components, equipment)
   - Major clients/customers
   - Note: Relationships discovered here form Wave 2

**Data Sources:**
- Company IR pages
- Yahoo Finance Japan
- Bloomberg
- Nikkei
- Company annual reports

---

### 2.2 Wave 1 Collection Status [DONE]

| ID | Company | Basic | Financial | Description | Suppliers | Clients | Status |
|----|---------|-------|-----------|-------------|-----------|---------|--------|
| CMP-0001 | Tokyo Seimitsu | [x] | [x] | [x] | [x] | [x] | [DONE] |
| CMP-0002 | DISCO | [x] | [x] | [x] | [x] | [x] | [DONE] |
| CMP-0003 | SCREEN Holdings | [x] | [x] | [x] | [x] | [x] | [DONE] |
| CMP-0004 | Tokyo Electron | [x] | [x] | [x] | [x] | [x] | [DONE] |
| CMP-0005 | Advantest | [x] | [x] | [x] | [x] | [x] | [DONE] |
| CMP-0006 | Lasertec | [x] | [x] | [x] | [x] | [x] | [DONE] |
| CMP-0007 | Fujimi | [x] | [x] | [x] | [x] | [x] | [DONE] |
| CMP-0008 | Resonac Holdings | [x] | [x] | [x] | [x] | [x] | [DONE] |
| CMP-0009 | Ferrotec | [x] | [x] | [x] | [x] | [x] | [DONE] |
| CMP-0010 | Toyo Gosei | [x] | [x] | [x] | [x] | [x] | [DONE] |
| CMP-0011 | Kokusai Electric | [x] | [x] | [x] | [x] | [x] | [DONE] |
| CMP-0012 | Horiba | [x] | [x] | [x] | [x] | [x] | [DONE] |
| CMP-0013 | Fuso Chemical | [x] | [x] | [x] | [x] | [x] | [DONE] |
| CMP-0014 | Kioxia Holdings | [x] | [x] | [x] | [x] | [x] | [DONE] |
| CMP-0015 | HOYA | [x] | [x] | [x] | [x] | [x] | [DONE] |
| CMP-0016 | Olympus | [x] | [x] | [x] | [x] | [x] | [DONE] |

---

## Phase 3: Data Collection - Wave 2+ (Discovered Companies)

### 3.1 Expansion Strategy [PENDING]

After Wave 1, the agent will:

1. **Extract Relationship References**
   - Parse supplier/client names from Wave 1 data
   - Create a queue of undiscovered companies

2. **Prioritization Criteria**
   - Companies appearing multiple times (high connectivity)
   - Companies in semiconductor supply chain
   - Listed companies (easier to get financial data)

3. **Iterative Expansion**
   - Wave 2: Direct suppliers/clients of seed companies
   - Wave 3: Suppliers/clients of Wave 2 companies
   - Continue until network stabilizes or scope limit reached

### 3.2 Discovery Queue [DONE]

All 12 discovered companies have been collected. See `data/wave2_discovery_queue.json` for full details.

| Queue # | Company Name | Country | ID | Status |
|---------|--------------|---------|-----|--------|
| 1 | TSMC | Taiwan | CMP-0017 | [DONE] |
| 2 | Samsung Electronics | Korea | CMP-0018 | [DONE] |
| 3 | Intel Corporation | USA | CMP-0019 | [DONE] |
| 4 | SK Hynix | Korea | CMP-0020 | [DONE] |
| 5 | Micron Technology | USA | CMP-0021 | [DONE] |
| 6 | Apple Inc. | USA | CMP-0022 | [DONE] |
| 7 | Western Digital | USA | CMP-0023 | [DONE] |
| 8 | Shin-Etsu Chemical | Japan | CMP-0024 | [DONE] |
| 9 | SUMCO Corporation | Japan | CMP-0025 | [DONE] |
| 10 | ASML Holding | Netherlands | CMP-0026 | [DONE] |
| 11 | Kyocera Corporation | Japan | CMP-0027 | [DONE] |
| 12 | NVIDIA Corporation | USA | CMP-0028 | [DONE] |

---

## Phase 4: Graph Construction

### 4.1 Relationship Mapping [DONE]

- [x] Generate bidirectional links (if A supplies B, then B is client of A)
- [x] Validate all ID references exist
- [x] Calculate network statistics:
  - Total nodes: 28 companies
  - Total edges: 68 relationships
  - Edge types: 52 supplier, 4 competitor, 4 partner, 8 ecosystem
  - Most connected nodes: TSMC (11 suppliers), Samsung (8 suppliers), Intel (7 suppliers)
  - Supply chain depth: 4 levels (wafers -> equipment -> foundry -> consumer)

### 4.2 Visualization [DONE]

- [x] Create interactive graph visualization (`output/supply_chain.html`)
- [x] Implement filtering by country and industry
- [x] Show company details on hover (ticker, industry, connections)
- [x] Highlight connected nodes on selection
- [x] Node colors by country, edge colors by relationship type
- [x] Zoom/pan controls, search functionality
- [x] Critical supply chain nodes highlighted

---

## Phase 5: Analytics

### 5.1 Planned Analyses [PENDING]

1. **Concentration Risk**
   - Single points of failure in supply chain
   - Companies with few alternatives

2. **Financial Health Correlation**
   - How supplier health affects clients
   - Forex sensitivity propagation

3. **Industry Segmentation**
   - Cluster analysis by business type
   - Vertical integration patterns

---

## Execution Log

### Session Progress Tracking

Use this section to track progress across sessions.

```
[SESSION START]
Date: 2025-02-21
Agent: Claude Code (Opus 4.5)
Current Phase: Phase 1 - Foundation Setup
Tasks Completed This Session:
  - Created PROJECT_PLAN.md with full project roadmap
  - Created schema/company.schema.json with JSON Schema draft-07
  - Created directory structure (schema/, data/companies/, scripts/, output/)
  - Created data/database.json template
  - Created data/seed_companies.json with 16 seed companies and pre-assigned IDs
  - Defined ID format: CMP-XXXX (4-digit sequential)
Tasks Remaining:
  - Phase 1.3: Verify ticker symbols via web search
  - Phase 2.1: Begin Wave 1 data collection for seed companies
  - Create validation utility script
Notes:
  - ESP in original spec likely meant EPS (Earnings Per Share) - corrected in schema
  - Some tickers need verification: 4368.T, 285A, 4970.T
  - isForexSensitive renamed from ifForexSensitive for clarity
[SESSION END]

[SESSION START]
Date: 2026-02-21 (continued)
Agent: Claude Code (Opus 4.5)
Current Phase: Phase 2 - Wave 1 Data Collection
Tasks Completed This Session:
  - Resolved all 16 seed company identities via web search
  - Discovered 4368.T = Fuso Chemical (not Fuji Oil as initially thought)
  - Discovered 285A = Kioxia Holdings (former Toshiba Memory, IPO Dec 2024)
  - Created 16 company JSON files (CMP-0001 to CMP-0016)
  - Collected basic info, financial metrics, descriptions for all companies
  - Updated database.json with company index
  - Industry breakdown: 8 Equipment, 5 Materials, 1 Semiconductors, 1 Precision
Tasks Remaining:
  - Discover supplier/client relationships for each company
  - Build Wave 2 discovery queue from relationships
  - Link companies via supplier/client arrays
Notes:
  - Major players: Tokyo Electron (19.2T JPY), Advantest (19.65T JPY), DISCO, Lasertec
  - Kioxia is notable new addition (5.64T JPY market cap, IPO just 2 months ago)
  - Some financial data incomplete (PBR, foreign ownership % missing for several)
[SESSION END]

[SESSION START]
Date: 2026-02-21 (continued)
Agent: Claude Code (Opus 4.5)
Current Phase: Phase 2 - Supplier/Client Discovery
Tasks Completed This Session:
  - Discovered supplier/client relationships for all 16 seed companies
  - Searched in both English and Japanese for comprehensive data
  - Created wave2_discovery_queue.json with 12 external companies to add
  - Updated all company JSON files with _externalRelationships field
  - Key clients identified: TSMC, Samsung, Intel (mentioned by 5-8 companies each)
  - Internal relationships: DISCO vs Tokyo Seimitsu (competitors), Kioxia uses Kokusai Electric
  - Market share data: Lasertec 100% EUV inspection, DISCO 70%+ dicing, Fuso Chemical 90% CMP slurry
Tasks Remaining:
  - Wave 2 data collection for external companies
  - Build graph visualization
  - Populate internal suppliers/clients arrays with CMP-XXXX IDs
Notes:
  - Most relationships are external (customers are global chip giants)
  - Japanese searches yielded additional detail (e.g., Nikkei articles)
  - Olympus has minimal semiconductor supply chain involvement (medical focus)
[SESSION END]

[SESSION START]
Date: 2026-02-21 (continued)
Agent: Claude Code (Opus 4.5)
Current Phase: Phase 3 - Wave 2 Data Collection
Tasks Completed This Session:
  - Collected data for all 12 Wave 2 companies (CMP-0017 to CMP-0028)
  - Created company JSON files for: TSMC, Samsung, Intel, SK Hynix, Micron, Apple,
    Western Digital, Shin-Etsu Chemical, SUMCO, ASML, Kyocera, NVIDIA
  - Searched in both English and Japanese for comprehensive financial and relationship data
  - Updated database.json with 28 total companies across 5 countries
  - Updated wave2_discovery_queue.json to mark collection as complete
  - Identified key supply chain relationships and critical chokepoints
Key Findings:
  - TSMC: $1.1T market cap, 90%+ AI chip manufacturing, 64 Lasertec EUV tools
  - Shin-Etsu + SUMCO: Control ~90% of global silicon wafer market
  - ASML: 100% monopoly on EUV lithography systems
  - NVIDIA: $4.65T company, fabless model using TSMC + SK Hynix HBM
  - Intel: Largest Lasertec customer (14 EUV inspection tools)
Geographic Distribution:
  - Japan: 17 companies (60%)
  - USA: 5 companies (18%)
  - South Korea: 2 companies (7%)
  - Taiwan: 1 company (4%)
  - Netherlands: 1 company (4%)
Tasks Remaining:
  - Phase 4: Build interactive supply chain graph visualization
  - Phase 5: Run analytics (concentration risk, financial correlation)
  - Populate internal suppliers/clients arrays with cross-references
Notes:
  - Full supply chain now mapped: silicon wafers → equipment → foundries → end products
  - Critical dependencies identified (single points of failure)
  - Wave 3 expansion possible but scope complete for current objectives
[SESSION END]

[SESSION START]
Date: 2026-02-21 (continued)
Agent: Claude Code (Opus 4.5)
Current Phase: Phase 4 - Graph Construction
Tasks Completed This Session:
  - Created data/graph.json with full supply chain graph structure
  - Built interactive D3.js visualization at output/supply_chain.html
  - Mapped 68 relationships across 28 companies
  - Implemented node/edge coloring by country and relationship type
  - Added filtering by country and industry
  - Added search functionality and zoom/pan controls
  - Highlighted critical supply chain nodes (monopolies/chokepoints)
  - Added tooltips showing company details and connection counts
Graph Statistics:
  - 28 nodes (companies)
  - 68 edges (52 supplier, 4 competitor, 4 partner, 8 ecosystem)
  - Most connected: TSMC (11 incoming), Samsung (8), Intel (7)
  - Supply chain depth: 4 levels (wafers -> equipment -> foundry -> consumer)
Critical Nodes Identified:
  - Shin-Etsu: 42% of silicon wafer market
  - ASML: 100% EUV lithography monopoly
  - Lasertec: 100% EUV mask inspection
  - TSMC: 90%+ of advanced AI chips
  - HOYA: 75% of EUV mask blanks
Tasks Remaining:
  - Phase 5: Analytics (concentration risk, financial correlation)
Notes:
  - Interactive visualization works in any modern browser
  - Force-directed layout with draggable nodes
  - Hover highlights connected subgraph
[SESSION END]
```

---

## Current State Summary

**Last Updated:** 2026-02-21

| Phase | Status | Progress |
|-------|--------|----------|
| Phase 1: Foundation | [DONE] | 100% |
| Phase 2: Wave 1 Data | [DONE] | 100% |
| Phase 3: Wave 2+ Data | [DONE] | 100% |
| Phase 4: Graph | [DONE] | 100% |
| Phase 5: Analytics | [PENDING] | 0% |

**Database Stats:** 28 companies, 5 countries, 68 relationships, full supply chain from silicon wafers to consumer products

**Graph Files:**
- `data/graph.json` - Graph data structure with nodes, edges, and statistics
- `output/supply_chain.html` - Interactive D3.js visualization

**Next Action:** Run analytics (concentration risk, financial correlation, industry segmentation)

---

## Appendix A: Example Company JSON

```json
{
  "id": "CMP-0001",
  "companyName": "Tokyo Electron Limited",
  "companyNameJapanese": "東京エレクトロン株式会社",
  "industryCode": "Semiconductor Equipment",
  "ticker": "8035.T",
  "description": "Global supplier of semiconductor and flat panel display production equipment. Key products include coater/developers, etch systems, and CVD equipment.",
  "marketCapInYen": 15000000000000,
  "PER": 25.5,
  "PBR": 6.2,
  "EPS": 2150,
  "website": "https://www.tel.co.jp/",
  "percentOfForeignOwnership": 45.2,
  "percentOfCirculatingEquity": 78.5,
  "latestPriceYen": 23500,
  "isForexSensitive": true,
  "suppliers": ["CMP-0011", "CMP-0012"],
  "clients": ["CMP-0020", "CMP-0021"],
  "_metadata": {
    "dataCollectedAt": "2025-02-21T10:00:00Z",
    "dataSource": "Company IR, Yahoo Finance Japan",
    "confidenceLevel": "high",
    "lastUpdated": "2025-02-21T10:00:00Z"
  }
}
```

---

## Appendix B: Agent Instructions

When resuming this project, the Claude Code agent should:

1. **Read this file first** to understand current state
2. **Check the "Current State Summary"** for overall progress
3. **Look at the execution log** for session-specific context
4. **Find the first [PENDING] task** and begin work
5. **Update status markers** as work progresses
6. **Log session activity** before ending

**ID Assignment Rule:**
- New companies get sequential IDs: CMP-0001, CMP-0002, etc.
- Check `data/companies/` for the highest existing ID before assigning new ones

**Data Quality Guidelines:**
- Mark uncertain data with confidence: "low"
- Always cite data sources in `_metadata`
- Use null for unavailable financial metrics (not 0)
- Verify ticker symbols against TSE listings

---

## Appendix C: Known Data Source URLs

| Source | URL | Use For |
|--------|-----|---------|
| Yahoo Finance Japan | https://finance.yahoo.co.jp/ | Stock prices, financial ratios |
| JPX (Japan Exchange) | https://www.jpx.co.jp/ | Official listings, ticker verification |
| Company IR Pages | (per company) | Official financials, descriptions |
| Nikkei | https://www.nikkei.com/ | News, market cap |

