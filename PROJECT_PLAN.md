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

### 1.3 Seed Company Resolution [PENDING]

Resolve all seed companies from CLAUDE.md to their full identities.

| # | Input | Company Name (EN) | Ticker | Status |
|---|-------|-------------------|--------|--------|
| 1 | Tokyo Seimitsu | Tokyo Seimitsu Co., Ltd. | 7729.T | [PENDING] |
| 2 | Disco | DISCO Corporation | 6146.T | [PENDING] |
| 3 | Screen | SCREEN Holdings Co., Ltd. | 7735.T | [PENDING] |
| 4 | Tokyo Electron | Tokyo Electron Limited | 8035.T | [PENDING] |
| 5 | Advantest | Advantest Corporation | 6857.T | [PENDING] |
| 6 | Lasertech | Lasertec Corporation | 6920.T | [PENDING] |
| 7 | Fujimi | Fujimi Incorporated | 5384.T | [PENDING] |
| 8 | 4004.T | Resonac Holdings (Showa Denko) | 4004.T | [PENDING] |
| 9 | 6890.T | Ferrotec Holdings | 6890.T | [PENDING] |
| 10 | 4970.T | Toyo Gosei Co., Ltd. | 4970.T | [PENDING] |
| 11 | 6525.T (Kokusai) | Kokusai Electric Corporation | 6525.T | [PENDING] |
| 12 | 6856.T | Horiba, Ltd. | 6856.T | [PENDING] |
| 13 | 4368.T | Fuji Oil Holdings Inc. | 4368.T | [PENDING] |
| 14 | 285A | (To be researched - new listing) | 285A | [PENDING] |
| 15 | Hoya (7741.T) | HOYA Corporation | 7741.T | [PENDING] |
| 16 | Olympus (7733.T) | Olympus Corporation | 7733.T | [PENDING] |

**Tasks:**
- [ ] Research and verify each ticker symbol
- [ ] Confirm company names in English
- [ ] Identify any ticker symbol discrepancies

---

## Phase 2: Data Collection - Wave 1 (Seed Companies)

### 2.1 Data Collection Protocol [PENDING]

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

### 2.2 Wave 1 Collection Status [PENDING]

| ID | Company | Basic | Financial | Description | Suppliers | Clients | Status |
|----|---------|-------|-----------|-------------|-----------|---------|--------|
| CMP-0001 | Tokyo Electron | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |
| CMP-0002 | DISCO | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |
| CMP-0003 | Advantest | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |
| CMP-0004 | SCREEN | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |
| CMP-0005 | Lasertec | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |
| CMP-0006 | Tokyo Seimitsu | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |
| CMP-0007 | Kokusai Electric | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |
| CMP-0008 | Horiba | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |
| CMP-0009 | HOYA | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |
| CMP-0010 | Olympus | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |
| CMP-0011 | Fujimi | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |
| CMP-0012 | Resonac | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |
| CMP-0013 | Ferrotec | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |
| CMP-0014 | Toyo Gosei | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |
| CMP-0015 | 4368.T (TBD) | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |
| CMP-0016 | 285A (TBD) | [ ] | [ ] | [ ] | [ ] | [ ] | [PENDING] |

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

### 3.2 Discovery Queue [PENDING]

Companies discovered during collection that need their own records:

| Queue # | Company Name | Discovered From | Priority | Status |
|---------|--------------|-----------------|----------|--------|
| (populated during Wave 1) | | | | |

---

## Phase 4: Graph Construction

### 4.1 Relationship Mapping [PENDING]

- [ ] Generate bidirectional links (if A supplies B, then B is client of A)
- [ ] Validate all ID references exist
- [ ] Calculate network statistics:
  - Total nodes (companies)
  - Total edges (relationships)
  - Most connected nodes
  - Supply chain depth

### 4.2 Visualization [PENDING]

- [ ] Create interactive graph visualization
- [ ] Implement filtering by industry
- [ ] Show financial metrics on hover
- [ ] Export to various formats

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
```

---

## Current State Summary

**Last Updated:** 2025-02-21

| Phase | Status | Progress |
|-------|--------|----------|
| Phase 1: Foundation | [IN_PROGRESS] | 66% |
| Phase 2: Wave 1 Data | [PENDING] | 0% |
| Phase 3: Wave 2+ Data | [PENDING] | 0% |
| Phase 4: Graph | [PENDING] | 0% |
| Phase 5: Analytics | [PENDING] | 0% |

**Next Action:** Phase 1.3 - Resolve seed company ticker symbols via web search, then begin Wave 1 data collection

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

