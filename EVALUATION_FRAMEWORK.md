# Undervalued Score Evaluation Framework

> **Purpose**: Systematic methodology for scoring 62 semiconductor supply chain companies on a 0-100 "undervalued" scale.
> Score 100 = most undervalued. Score 0 = most overvalued or fairly valued.
>
> **Audience**: Senior hedge fund analyst performing fundamental + supply chain analysis.
>
> **Date**: 2026-02-21

---

## Table of Contents

1. [Scoring Philosophy](#1-scoring-philosophy)
2. [Scoring Dimensions](#2-scoring-dimensions)
   - [A. Valuation Ratios (30 pts)](#a-valuation-ratios-30-points)
   - [B. Supply Chain Moat (25 pts)](#b-supply-chain-moat-25-points)
   - [C. Growth & Earnings Quality (15 pts)](#c-growth--earnings-quality-15-points)
   - [D. Ownership & Float (10 pts)](#d-ownership--float-10-points)
   - [E. Catalysts & Sentiment (10 pts)](#e-catalysts--sentiment-10-points)
   - [F. Risk Adjustment (10 pts)](#f-risk-adjustment-10-points)
3. [Data Collection Plan](#3-data-collection-plan)
4. [Execution Steps](#4-execution-steps)
5. [Handling Data Gaps](#5-handling-data-gaps)
6. [Appendices](#6-appendices)

---

## 1. Scoring Philosophy

### What "undervalued" means

A company is **undervalued** when its current market price does not reflect the intrinsic worth implied by its fundamentals, competitive position, and forward prospects. In this framework, "undervalued" is a composite judgment that integrates:

- **Cheapness relative to peers** (valuation ratios below sector medians)
- **Structural advantages not priced in** (monopoly positions, irreplaceable supply chain roles)
- **Earnings momentum the market has not caught up with** (accelerating growth, margin expansion, AI/advanced-node tailwinds)
- **Ownership dynamics that signal upside** (low foreign ownership relative to quality, high float creating buying opportunity)
- **Upcoming catalysts** (capacity expansion, analyst upgrades, favorable policy changes)
- **Risk-adjusted** (discounting for forex exposure, customer concentration, geopolitical vulnerability)

### How the 0-100 scale works

| Score Range | Interpretation |
|-------------|---------------|
| 80-100 | Deeply undervalued. Strong buy signal across multiple dimensions. |
| 60-79 | Moderately undervalued. Attractive entry point with identifiable catalysts. |
| 40-59 | Fairly valued. Market pricing roughly reflects fundamentals. |
| 20-39 | Modestly overvalued. Premium pricing partially justified by quality. |
| 0-19 | Significantly overvalued. Market pricing exceeds reasonable intrinsic value. |

The composite score is the weighted sum of six dimensions (A through F), each scored independently. The weights sum to 100%, and the maximum possible score is 100 points.

### Key principles

1. **Peer-relative, not absolute**. A PER of 15 is cheap for semiconductor equipment but expensive for commodity chemicals. All valuation metrics are compared against the company's peer group median.
2. **Forward-looking bias**. Trailing metrics establish the baseline; forward estimates and growth trajectory determine whether the company deserves a premium or discount.
3. **Supply chain context matters**. A monopoly supplier scores higher on Dimension B even if its valuation ratios appear "fair" — the moat justifies paying up, so a fair-valued monopolist is actually undervalued relative to its strategic importance.
4. **Data transparency**. Every score includes a confidence flag (High / Medium / Low) based on data completeness. Companies with insufficient data receive a penalty in their composite score.

---

## 2. Scoring Dimensions

### A. Valuation Ratios (30 points)

**Weight**: 30% | **What it captures**: How cheap or expensive the company is relative to sector peers on fundamental valuation metrics.

#### Sub-scores

| Sub-dimension | Max Points | Metric |
|---------------|-----------|--------|
| A1. PER discount | 12 | Trailing PER vs peer group median PER |
| A2. Forward PER discount | 6 | Forward PER vs peer group median Forward PER |
| A3. PBR discount | 8 | PBR vs peer group median PBR |
| A4. Earnings yield premium | 4 | Earnings yield (1/PER) vs 10-year JGB yield spread |

#### Formulas

**A1. PER Discount Score (0-12)**

```
PER_ratio = Company_PER / Peer_Median_PER

If PER_ratio <= 0.50:  score = 12        (50%+ discount to peers)
If PER_ratio <= 0.70:  score = 10        (30-50% discount)
If PER_ratio <= 0.85:  score = 8         (15-30% discount)
If PER_ratio <= 1.00:  score = 6         (0-15% discount, at or below median)
If PER_ratio <= 1.15:  score = 4         (0-15% premium)
If PER_ratio <= 1.30:  score = 2         (15-30% premium)
If PER_ratio >  1.30:  score = 0         (30%+ premium)

Special cases:
  - Negative PER (loss-making): score = 0
  - PER > 100 (speculative): score = 0
  - PER not available: score = NULL (excluded from dimension, weight redistributed)
```

**A2. Forward PER Discount Score (0-6)**

```
Same tier structure as A1, scaled to max 6 points:
  <= 0.50: 6 | <= 0.70: 5 | <= 0.85: 4 | <= 1.00: 3 | <= 1.15: 2 | <= 1.30: 1 | > 1.30: 0
```

**A3. PBR Discount Score (0-8)**

```
PBR_ratio = Company_PBR / Peer_Median_PBR

If PBR_ratio <= 0.50:  score = 8
If PBR_ratio <= 0.70:  score = 6
If PBR_ratio <= 0.85:  score = 5
If PBR_ratio <= 1.00:  score = 4
If PBR_ratio <= 1.20:  score = 2
If PBR_ratio >  1.20:  score = 0

Special case:
  - PBR < 1.0 in absolute terms: bonus +1 point (capped at 8)
    Rationale: trading below book value is an additional signal regardless of peer comparison.
```

**A4. Earnings Yield Spread (0-4)**

```
Earnings_Yield = 1 / PER
Spread = Earnings_Yield - JGB_10Y_Yield

If Spread >= 6%:  score = 4   (earnings yield far exceeds risk-free)
If Spread >= 4%:  score = 3
If Spread >= 2%:  score = 2
If Spread >= 0%:  score = 1   (earnings yield just exceeds risk-free)
If Spread <  0%:  score = 0   (earnings yield below risk-free)
```

#### Dimension A total

```
A_score = A1 + A2 + A3 + A4
```

If any sub-score is NULL due to missing data, redistribute its weight proportionally among the available sub-scores:

```
A_score_adjusted = (sum of available sub-scores) / (max of available sub-scores) * 30
```

---

### B. Supply Chain Moat (25 points)

**Weight**: 25% | **What it captures**: The company's irreplaceability in the semiconductor supply chain, monopoly or oligopoly positioning, and competitive barriers.

This dimension is **semi-quantitative**: it uses structured rubrics applied through qualitative assessment informed by the supply chain graph data and industry research.

#### Sub-scores

| Sub-dimension | Max Points | Assessment basis |
|---------------|-----------|-----------------|
| B1. Market share position | 10 | Estimated global market share in primary product |
| B2. Switching costs / lock-in | 5 | Customer dependency, qualification cycles, integration depth |
| B3. Technology differentiation | 5 | Patent moat, process know-how, R&D intensity |
| B4. Supply chain centrality | 5 | Graph degree (supplier/client edges), critical node status |

#### Rubrics

**B1. Market Share Position (0-10)**

| Market Share | Score | Description |
|-------------|-------|-------------|
| >70% (monopoly) | 10 | Dominant, no viable alternative (e.g., ASML in EUV, Lasertec in EUV mask inspection) |
| 40-70% (oligopoly leader) | 8 | Leading share in oligopoly with 2-3 players |
| 25-40% (strong #1 or #2) | 6 | Significant share with meaningful competition |
| 10-25% (notable player) | 4 | Recognized participant, some pricing power |
| 5-10% (niche) | 2 | Niche presence, limited pricing power |
| <5% or unknown | 0 | Commodity participant or insufficient data |

**B2. Switching Costs / Lock-in (0-5)**

| Level | Score | Criteria |
|-------|-------|---------|
| Extreme | 5 | Multi-year qualification, product designed around supplier (e.g., photoresist for specific node) |
| High | 4 | 6-18 month qualification, significant requalification cost |
| Moderate | 3 | 3-6 month switch, some integration effort |
| Low | 2 | Commodity supply, multiple qualified vendors |
| Minimal | 0-1 | Drop-in replacement available |

**B3. Technology Differentiation (0-5)**

| Level | Score | Criteria |
|-------|-------|---------|
| Unique | 5 | Only company capable of producing the product at required spec |
| Leading | 4 | Best-in-class with significant patent portfolio |
| Strong | 3 | Differentiated technology, 1-2 year lead over competitors |
| Moderate | 2 | Some differentiation, competitive R&D |
| Commodity | 0-1 | Standard product, many capable producers |

**B4. Supply Chain Centrality (0-5)**

Derived from the supply chain graph (`data/graph.json`):

```
Degree = number of supplier edges + number of client edges for the company node
Critical_flag = 1 if company is in the criticalNodes list, 0 otherwise

If Critical_flag == 1:                    score = 5
Else if Degree >= 10:                     score = 4
Else if Degree >= 6:                      score = 3
Else if Degree >= 3:                      score = 2
Else:                                     score = 1
```

#### Dimension B total

```
B_score = B1 + B2 + B3 + B4     (max 25)
```

---

### C. Growth & Earnings Quality (15 points)

**Weight**: 15% | **What it captures**: Revenue growth trajectory, margin quality, and exposure to secular growth themes (AI, advanced packaging, EUV adoption).

#### Sub-scores

| Sub-dimension | Max Points | Metric |
|---------------|-----------|--------|
| C1. Revenue growth (YoY) | 5 | Most recent fiscal year revenue growth % |
| C2. Operating margin | 4 | Operating margin vs peer median |
| C3. ROE quality | 3 | ROE vs peer median, consistency |
| C4. AI / advanced-node exposure | 3 | Qualitative: revenue % tied to AI, HBM, EUV, advanced packaging |

#### Formulas

**C1. Revenue Growth Score (0-5)**

```
If YoY_Revenue_Growth >= 30%:  score = 5
If YoY_Revenue_Growth >= 20%:  score = 4
If YoY_Revenue_Growth >= 10%:  score = 3
If YoY_Revenue_Growth >= 0%:   score = 2
If YoY_Revenue_Growth >= -10%: score = 1
If YoY_Revenue_Growth < -10%:  score = 0
```

**C2. Operating Margin Score (0-4)**

```
OPM_ratio = Company_OPM / Peer_Median_OPM

If OPM_ratio >= 1.50:  score = 4   (margin 50%+ above peer median)
If OPM_ratio >= 1.20:  score = 3
If OPM_ratio >= 0.90:  score = 2   (roughly in line with peers)
If OPM_ratio >= 0.60:  score = 1
If OPM_ratio <  0.60:  score = 0
```

**C3. ROE Quality Score (0-3)**

```
ROE = EPS / BPS     (or equivalently: PBR / PER)

If ROE >= 20% and above peer median:  score = 3
If ROE >= 12% and near peer median:   score = 2
If ROE >= 5%:                          score = 1
If ROE < 5% or negative:              score = 0
```

**C4. AI / Advanced-Node Exposure (0-3)**

| Exposure Level | Score | Examples |
|---------------|-------|---------|
| High (>30% revenue from AI/advanced) | 3 | HBM testing (Advantest), EUV components (Lasertec, ASML), AI accelerator packaging |
| Moderate (10-30%) | 2 | Advanced node materials, CoWoS substrates |
| Low (<10% but present) | 1 | Indirect exposure through major customers |
| None or negligible | 0 | Legacy node or non-AI segments |

#### Dimension C total

```
C_score = C1 + C2 + C3 + C4     (max 15)
```

---

### D. Ownership & Float (10 points)

**Weight**: 10% | **What it captures**: Foreign ownership gap (room for institutional buying), float dynamics, and treasury stock signals.

#### Sub-scores

| Sub-dimension | Max Points | Metric |
|---------------|-----------|--------|
| D1. Foreign ownership gap | 5 | Current foreign ownership % vs peer median |
| D2. Circulating equity dynamics | 3 | Free float %, treasury stock buyback activity |
| D3. Price vs 52-week range | 2 | Where current price sits in 52-week range |

#### Formulas

**D1. Foreign Ownership Gap (0-5)**

The thesis: companies with **lower** foreign ownership than their quality warrants have room for foreign institutional buying, which is a positive catalyst.

```
Quality_Tier = f(B_score)    // supply chain moat score as proxy for quality
  If B_score >= 18: Quality_Tier = "High"
  If B_score >= 12: Quality_Tier = "Medium"
  Else:             Quality_Tier = "Low"

Expected_Foreign_Ownership:
  High quality:   40-50%
  Medium quality:  25-35%
  Low quality:     10-20%

Gap = Expected_Midpoint - Actual_Foreign_Ownership

If Gap >= 20%:  score = 5   (severely under-owned by foreigners relative to quality)
If Gap >= 15%:  score = 4
If Gap >= 10%:  score = 3
If Gap >= 5%:   score = 2
If Gap >= 0%:   score = 1
If Gap < 0%:    score = 0   (already at or above expected ownership)
```

**D2. Circulating Equity Dynamics (0-3)**

```
If active buyback program AND float < 70%:   score = 3
If active buyback program OR float < 70%:    score = 2
If float 70-90%, no buyback:                 score = 1
If float > 90%, no buyback:                  score = 0
```

**D3. Price vs 52-Week Range (0-2)**

```
Position = (Current_Price - 52W_Low) / (52W_High - 52W_Low)

If Position <= 0.25:  score = 2   (near 52-week low — potential value)
If Position <= 0.50:  score = 1   (lower half of range)
If Position >  0.50:  score = 0   (upper half — less upside from range perspective)
```

#### Dimension D total

```
D_score = D1 + D2 + D3     (max 10)
```

---

### E. Catalysts & Sentiment (10 points)

**Weight**: 10% | **What it captures**: Near-term price catalysts including analyst consensus, capacity expansion, policy tailwinds, and material news.

#### Sub-scores

| Sub-dimension | Max Points | Assessment basis |
|---------------|-----------|-----------------|
| E1. Analyst consensus | 4 | Buy/hold/sell distribution and price target vs current price |
| E2. Capacity expansion / capex plans | 3 | Announced factory builds, equipment orders, R&D commitments |
| E3. Policy / macro tailwinds | 3 | Government subsidies, trade policy, industry cycle position |

#### Rubrics

**E1. Analyst Consensus (0-4)**

```
Upside = (Average_Price_Target / Current_Price) - 1

If Upside >= 30% AND majority Buy ratings:     score = 4
If Upside >= 15% AND more Buy than Sell:        score = 3
If Upside >= 0%  AND balanced ratings:          score = 2
If Upside <  0%  OR majority Hold:              score = 1
If majority Sell AND negative target gap:       score = 0
```

**E2. Capacity Expansion (0-3)**

| Signal | Score | Criteria |
|--------|-------|---------|
| Major expansion | 3 | New fab/facility announced, significant capex increase, M&A activity |
| Moderate investment | 2 | Equipment upgrades, incremental capacity additions |
| Maintenance level | 1 | Steady capex, no major announcements |
| Contraction | 0 | Capex cuts, facility closures, restructuring |

**E3. Policy / Macro Tailwinds (0-3)**

| Signal | Score | Criteria |
|--------|-------|---------|
| Direct beneficiary | 3 | Named in government subsidy program (e.g., METI semiconductor strategy), favorable trade ruling |
| Indirect beneficiary | 2 | Sector-level tailwind (semiconductor cycle upturn, yen weakness for exporters) |
| Neutral | 1 | No notable policy impact |
| Headwind | 0 | Export controls, trade restrictions, regulatory burden |

#### Dimension E total

```
E_score = E1 + E2 + E3     (max 10)
```

---

### F. Risk Adjustment (10 points)

**Weight**: 10% | **What it captures**: Downside risks that should temper the undervalued thesis. Higher score = lower risk = more conviction in undervaluation.

This dimension is **inverted**: a risky company scores low (more risk = less confidence the undervaluation will be realized), a safe company scores high.

#### Sub-scores

| Sub-dimension | Max Points | Risk factor |
|---------------|-----------|-------------|
| F1. Forex sensitivity | 3 | Dependence on USD/JPY movements |
| F2. Customer concentration | 4 | Revenue dependency on top 1-3 customers |
| F3. Geopolitical risk | 3 | Exposure to China/Taiwan supply chain disruption |

#### Rubrics

**F1. Forex Sensitivity (0-3)** — higher score = lower forex risk

```
If ifForexSensitive == false AND domestic revenue > 50%:   score = 3
If ifForexSensitive == false AND mixed revenue:            score = 2
If ifForexSensitive == true  AND hedging program in place: score = 1
If ifForexSensitive == true  AND unhedged/heavy exposure:  score = 0
```

**F2. Customer Concentration (0-4)** — higher score = lower concentration risk

```
If top customer < 15% of revenue:    score = 4   (well diversified)
If top customer 15-25%:              score = 3
If top customer 25-40%:              score = 2
If top customer 40-60%:              score = 1
If top customer > 60%:               score = 0   (extreme concentration)
```

**F3. Geopolitical Risk (0-3)** — higher score = lower geopolitical risk

```
If minimal China/Taiwan exposure:             score = 3
If moderate exposure with diversification:    score = 2
If significant China manufacturing/sales:     score = 1
If critical Taiwan dependency or China >30%:  score = 0
```

#### Dimension F total

```
F_score = F1 + F2 + F3     (max 10)
```

---

### Composite Score Calculation

```
Composite = A_score + B_score + C_score + D_score + E_score + F_score

Range: 0 to 100
```

Each dimension already carries its weight in its max points (30 + 25 + 15 + 10 + 10 + 10 = 100), so no additional weighting multiplication is needed.

#### Data Confidence Modifier

After computing the raw composite, apply a confidence adjustment:

```
Data_Coverage = (number of non-null required fields) / (total required fields)

If Data_Coverage >= 0.80:  Confidence = "High",   no penalty
If Data_Coverage >= 0.60:  Confidence = "Medium",  composite *= 0.95 (5% haircut)
If Data_Coverage >= 0.40:  Confidence = "Low",     composite *= 0.85 (15% haircut)
If Data_Coverage <  0.40:  Confidence = "Very Low", composite *= 0.70 (30% haircut)
```

This prevents companies with incomplete data from being falsely ranked as "undervalued" simply because risk or overvaluation signals are missing.

---

## 3. Data Collection Plan

### 3.1 Current Data Status

Based on an audit of all 62 company JSON files:

| Field | Populated | Missing | Coverage |
|-------|-----------|---------|----------|
| companyName | 62 | 0 | 100% |
| industryCode | 62 | 0 | 100% |
| ticker | 62 | 0 | 100% |
| description | 62 | 0 | 100% |
| marketCapInYen | 12 | 50 | 19% |
| latestPriceYen | 16 | 46 | 26% |
| PER | 3 | 59 | 5% |
| PBR | 0 | 62 | 0% |
| EPS | 4 | 58 | 6% |
| percentOfForeignOwnership | 1 | 61 | 2% |
| percentOfCirculatingEquity | 0 | 62 | 0% |
| ifForexSensitive | 16 | 46 | 26% |
| suppliers (array) | 62 | 0 | 100% |
| clients (array) | 62 | 0 | 100% |

**Critical gap**: Financial data (PER, PBR, EPS, ownership %) is almost entirely missing. Wave 3 companies (CMP-0029 to CMP-0062, all 34 of them) have no financial data at all.

### 3.2 Fields to Collect per Company

The following fields must be gathered or verified for all 62 companies. Fields marked with `*` are new (not in current schema) and will be stored as additional metadata or derived at scoring time.

| # | Field | Source | Storage |
|---|-------|--------|---------|
| 1 | PER (trailing 12M) | Yahoo Finance, Nikkei, Bloomberg | `PER` in company JSON |
| 2 | Forward PER* | Analyst consensus via Yahoo Finance / Refinitiv | Scoring worksheet (not in JSON) |
| 3 | PBR | Yahoo Finance, Nikkei | `PBR` in company JSON |
| 4 | EPS (trailing 12M) | Yahoo Finance, annual report | `EPS` in company JSON (note: schema field, not `ESP`) |
| 5 | ROE* | Derived: `PBR / PER` or `EPS / BPS` | Scoring worksheet |
| 6 | marketCapInYen | Yahoo Finance (JPY-listed) / conversion for non-JPY | `marketCapInYen` in company JSON |
| 7 | latestPriceYen | Yahoo Finance, Google Finance | `latestPriceYen` in company JSON |
| 8 | percentOfForeignOwnership | Company IR page, EDINET filings, Nikkei | `percentOfForeignOwnership` in company JSON |
| 9 | percentOfCirculatingEquity | Company IR page, JPX data | `percentOfCirculatingEquity` in company JSON |
| 10 | 52-week high* | Yahoo Finance | Scoring worksheet |
| 11 | 52-week low* | Yahoo Finance | Scoring worksheet |
| 12 | Revenue (latest FY, in JPY)* | Annual report, Yahoo Finance | Scoring worksheet |
| 13 | Revenue growth YoY %* | Derived from consecutive FY revenue | Scoring worksheet |
| 14 | Operating margin %* | Annual report, Yahoo Finance | Scoring worksheet |
| 15 | Dividend yield* | Yahoo Finance | Scoring worksheet |
| 16 | Analyst consensus* | Yahoo Finance, Refinitiv (Buy/Hold/Sell counts + avg target) | Scoring worksheet |
| 17 | Recent material news* | Company IR, Nikkei, Reuters | Scoring worksheet |
| 18 | ifForexSensitive | Company annual report (overseas revenue %) | `ifForexSensitive` in company JSON |

### 3.3 Data Sources and Methodology

#### Primary sources (free / publicly available)

| Source | URL Pattern | Fields Covered | Notes |
|--------|-------------|----------------|-------|
| Yahoo Finance (JP) | `finance.yahoo.co.jp/quote/{TICKER}` | PER, PBR, EPS, market cap, price, 52W range, dividend yield | Best for TSE-listed companies |
| Yahoo Finance (US) | `finance.yahoo.com/quote/{TICKER}` | Same as above | For US-listed (INTC, MU, NVDA, AAPL, WDC, ASML) |
| Nikkei Company Profile | `www.nikkei.com/nkd/company/?scode={4-digit}` | PER, PBR, foreign ownership, financial summary | Japanese companies only |
| EDINET | `disclosure2.edinet-fsa.go.jp` | Foreign ownership, circulating equity | Annual securities reports (Yuho) |
| JPX (Japan Exchange) | `www.jpx.co.jp` | Float data, shareholder composition | Official exchange data |
| Company IR pages | Varies per company | Revenue breakdown, capex plans, overseas revenue % | Most authoritative for qualitative data |
| KRX (Korea Exchange) | `data.krx.co.kr` | Samsung, SK Hynix financials | Korean-listed companies |
| TWSE (Taiwan Exchange) | `www.twse.com.tw` | TSMC financials | Taiwan-listed |

#### Secondary sources (for cross-validation)

- Google Finance: quick price/market cap verification
- TradingView: chart-based 52W range, technical context
- Reuters / Nikkei news: catalyst and sentiment assessment
- Ullet.com: convenient Japanese company financial summaries

#### Methodology per field

1. **PER, PBR, EPS, market cap, price**: Pull from Yahoo Finance primary listing. Cross-check against Nikkei for Japanese companies. For non-JPY companies, convert market cap to JPY using the USD/JPY or KRW/JPY or TWD/JPY rate on the collection date.

2. **Foreign ownership %**: For Japanese companies, check the latest quarterly "major shareholder" disclosure on EDINET or the company IR page. For non-Japanese companies, this field is less meaningful (set to NULL with a note).

3. **Circulating equity %**: Use JPX's published free-float data for TSE-listed companies. For non-TSE companies, estimate from public filings (shares outstanding minus insider/treasury/strategic holdings).

4. **Revenue, growth, operating margin**: Pull from the most recent annual report (FY ending March 2025 for most Japanese companies, or December 2024 for calendar-year reporters). Compute YoY growth from the prior year.

5. **52-week high/low**: Pull directly from Yahoo Finance quote page.

6. **Analyst consensus**: Use Yahoo Finance "Analysis" tab or Refinitiv data where available. Record: number of Buy, Hold, Sell ratings and average 12-month price target.

7. **Forex sensitivity**: Classify based on overseas revenue percentage from the annual report. If overseas revenue > 50%, flag as forex sensitive. Cross-reference with the existing `ifForexSensitive` field in the database.

8. **AI / advanced-node exposure**: Qualitative assessment from company descriptions, investor presentations, and news coverage. Classify into High / Moderate / Low / None.

### 3.4 Collection Priority

Execute in the following order to maximize scoring coverage fastest:

| Priority | Companies | Count | Rationale |
|----------|-----------|-------|-----------|
| P1 | Wave 3 Japanese companies (CMP-0029 to CMP-0062) | 34 | Zero financial data. All TSE-listed, data readily available from Yahoo Finance JP. |
| P2 | Wave 1 Japanese companies with gaps (CMP-0001 to CMP-0016) | 16 | Partial data exists. Fill PBR, foreign ownership, circulating equity, revenue/growth. |
| P3 | Wave 2 non-Japanese companies (CMP-0017 to CMP-0028 except JP) | 9 | Different exchanges. Convert financials to JPY. Some fields (foreign ownership) less applicable. |
| P4 | Wave 2 Japanese companies in this range (CMP-0024, CMP-0025, CMP-0027) | 3 | Same as P2 but in Wave 2 ID range. |

### 3.5 Non-Japanese Company Handling

The 11 non-Japanese companies require special treatment:

| Company | Ticker | Exchange | Currency | Notes |
|---------|--------|----------|----------|-------|
| TSMC | 2330.TW | TWSE | TWD | Convert to JPY. Foreign ownership N/A (use FINI % as proxy). |
| Samsung | 005930.KS | KRX | KRW | Convert to JPY. Foreign ownership from KRX disclosure. |
| Intel | INTC | NASDAQ | USD | Convert to JPY. US institutional ownership data available. |
| SK Hynix | 000660.KS | KRX | KRW | Same as Samsung. |
| Micron | MU | NASDAQ | USD | Same as Intel. |
| Apple | AAPL | NASDAQ | USD | Same as Intel. Primarily a customer, not a semiconductor company. |
| Western Digital | WDC | NASDAQ | USD | Same as Intel. |
| ASML | ASML | NASDAQ/AEX | EUR/USD | Dual-listed. Use USD for consistency. |
| NVIDIA | NVDA | NASDAQ | USD | Same as Intel. |

For Dimension D (Ownership & Float), non-Japanese companies will be scored using their home-market institutional ownership dynamics rather than the Japan-specific "foreign ownership gap" model. The D1 sub-score rubric will substitute:

```
For non-Japanese companies:
  D1 = Institutional ownership change score (0-5)
  If institutional ownership increased >5% in past year: score = 5
  If increased 2-5%: score = 4
  If stable (+/- 2%): score = 2
  If decreased 2-5%: score = 1
  If decreased >5%: score = 0
```

---

## 4. Execution Steps

### Step 1: Define Peer Groups

Group the 62 companies into peer cohorts for relative comparison. Peer groups are defined by **industry code** and **market cap tier**.

**Industry Groups** (primary grouping):

| Group ID | Industry Code(s) | Companies |
|----------|------------------|-----------|
| G1 | Semiconductor Equipment | 25 companies |
| G2 | Semiconductor Materials | 26 companies |
| G3 | Semiconductors, Memory Semiconductors | 6 companies (Samsung, Intel, Kioxia, SK Hynix, Micron, NVIDIA) |
| G4 | Semiconductor Foundry, Components, Consumer Electronics, Storage/Memory, Precision Instruments | 4 companies (TSMC, Kyocera, Apple, WDC) |

Note: G4 is a catch-all for companies without enough peers. They will be compared against G1/G2 medians weighted by their closest resemblance, or scored using absolute thresholds.

**Market Cap Tiers** (secondary grouping within industry):

| Tier | Market Cap (JPY) | Label |
|------|------------------|-------|
| Large | > 1 trillion | Large-cap |
| Mid | 100 billion - 1 trillion | Mid-cap |
| Small | < 100 billion | Small-cap |

Peer medians are calculated within each (Industry Group x Market Cap Tier) cell. If a cell has fewer than 3 companies, merge with the adjacent tier.

### Step 2: Data Enrichment Sweep

Execute the data collection plan (Section 3) in priority order:

1. **Batch P1** (34 Wave 3 companies): Collect all 18 fields from Yahoo Finance JP. Estimated effort: 2-3 sessions of systematic web research.
2. **Batch P2** (16 Wave 1 companies): Fill gaps in existing records. Focus on PBR, foreign ownership, circulating equity, revenue/growth.
3. **Batch P3** (9 non-Japanese companies): Collect from Yahoo Finance US, KRX, TWSE. Convert all monetary values to JPY.
4. **Batch P4** (3 remaining Japanese Wave 2 companies): Fill gaps similar to P2.

After each batch, validate data by checking:
- PER should be positive for profitable companies
- PBR should be > 0
- EPS * shares outstanding ~ market cap (sanity check)
- Foreign ownership should be 0-100%

### Step 3: Compute Sector Medians

For each peer group, calculate:

```
Median_PER     = median(PER for all companies in group with non-null PER)
Median_PBR     = median(PBR for all companies in group with non-null PBR)
Median_ROE     = median(ROE for all companies in group with non-null ROE)
Median_Growth  = median(YoY revenue growth for all companies in group)
Median_OPM     = median(Operating margin for all companies in group)
Median_ForeignOwnership = median(foreign ownership % for Japanese companies in group)
```

Store these medians in a reference table for scoring.

### Step 4: Score Dimension A (Valuation Ratios)

For each company:
1. Look up its peer group medians
2. Compute PER_ratio, PBR_ratio, earnings yield spread
3. Apply the A1-A4 rubrics
4. Sum to get A_score (0-30)
5. Apply data gap adjustment if any sub-scores are NULL

### Step 5: Score Dimension B (Supply Chain Moat)

For each company:
1. Assess market share from company descriptions, industry reports, and existing database notes
2. Evaluate switching costs based on product type and qualification requirements
3. Rate technology differentiation from patent data, R&D spending, and competitive landscape
4. Compute supply chain centrality from `data/graph.json` (degree count + critical node flag)
5. Sum B1-B4 to get B_score (0-25)

Reference the 11 critical nodes already identified in the graph:
- ASML (CMP-0026): EUV lithography monopoly
- Lasertec (CMP-0006): EUV mask inspection monopoly
- TSMC (CMP-0017): Advanced node foundry dominance
- Shin-Etsu Chemical (CMP-0024): Silicon wafer duopoly
- SUMCO (CMP-0025): Silicon wafer duopoly
- Tokyo Electron (CMP-0004): Coater/developer oligopoly
- Stella Chemifa (CMP-0044): Ultra-high purity HF monopoly
- Ibiden (CMP-0048): AI server IC substrate dominance
- Organo (CMP-0052): TSMC ultrapure water exclusive supplier
- Plus others flagged in graph.json

### Step 6: Score Dimension C (Growth & Earnings Quality)

For each company:
1. Pull revenue growth YoY from collected data
2. Compare operating margin to peer median
3. Compute ROE and compare to peer median
4. Assess AI/advanced-node exposure qualitatively
5. Sum C1-C4 to get C_score (0-15)

### Step 7: Score Dimension D (Ownership & Float)

For each company:
1. Determine quality tier from B_score
2. Compute expected foreign ownership based on quality
3. Calculate gap between expected and actual foreign ownership
4. Assess float dynamics (buyback programs, treasury stock)
5. Compute price position in 52-week range
6. Sum D1-D3 to get D_score (0-10)

### Step 8: Score Dimension E (Catalysts & Sentiment)

For each company:
1. Pull analyst consensus (Buy/Hold/Sell counts, price target)
2. Compute upside to price target
3. Scan for recent capacity expansion announcements
4. Assess policy tailwinds (METI subsidies, export control implications)
5. Sum E1-E3 to get E_score (0-10)

### Step 9: Score Dimension F (Risk Adjustment)

For each company:
1. Assess forex sensitivity from `ifForexSensitive` field and overseas revenue %
2. Estimate customer concentration from supply chain graph (client edges) and company disclosures
3. Evaluate geopolitical exposure (China revenue %, Taiwan supply dependency)
4. Sum F1-F3 to get F_score (0-10)

### Step 10: Compute Composite Score

```
Raw_Composite = A + B + C + D + E + F
Data_Coverage = count(non-null scored fields) / total(required fields)
Confidence_Multiplier = f(Data_Coverage)   // see Section 2, Data Confidence Modifier
Final_Score = Raw_Composite * Confidence_Multiplier
```

### Step 11: Rank and Identify Top 10

1. Sort all 62 companies by Final_Score descending
2. Identify the top 10 most undervalued
3. For each top-10 company, produce a brief thesis:
   - Why the market is mispricing this company
   - Key catalyst that could unlock value
   - Primary risk to the thesis
   - Recommended position sizing (conviction level)

### Step 12: Sensitivity Analysis

Test robustness of the top 10 ranking by varying dimension weights:

| Scenario | A | B | C | D | E | F | Purpose |
|----------|---|---|---|---|---|---|---------|
| Base case | 30 | 25 | 15 | 10 | 10 | 10 | Default weights |
| Value-heavy | 40 | 20 | 10 | 10 | 10 | 10 | Emphasize cheapness |
| Moat-heavy | 20 | 35 | 15 | 10 | 10 | 10 | Emphasize competitive position |
| Growth-heavy | 20 | 20 | 25 | 10 | 15 | 10 | Emphasize growth trajectory |
| Equal-weight | 17 | 17 | 17 | 17 | 16 | 16 | No bias |

For each scenario, recompute composite scores and check if the top 10 list changes materially. Companies that remain in the top 10 across all scenarios have the highest conviction.

---

## 5. Handling Data Gaps

Even after the data collection sweep, some companies will have incomplete data. The framework handles this through three mechanisms:

### 5.1 Pro-rata rescaling within a dimension

If a sub-score is NULL (e.g., Forward PER unavailable), exclude it and rescale the remaining sub-scores to fill the dimension's max:

```
Example for Dimension A:
  A1 = 10 (out of 12)
  A2 = NULL (Forward PER unavailable)
  A3 = 5 (out of 8)
  A4 = 3 (out of 4)

  Available_max = 12 + 8 + 4 = 24
  Available_sum = 10 + 5 + 3 = 18
  A_score = (18 / 24) * 30 = 22.5
```

### 5.2 Confidence penalty on composite

As described in the composite score section, companies with low data coverage receive a multiplicative haircut (5-30%) to prevent false positives.

### 5.3 Unlisted / private company handling

- **JSR Corporation (CMP-0034)**: Delisted after JIC acquisition (2024). No public market data. Score Dimension A as NULL entirely. Score B-F from available qualitative data. Apply maximum confidence penalty. Flag as "not actionable for public equity investment."
- **Non-Japanese companies**: Foreign ownership metrics are adapted per Section 3.5.
- **Companies with fiscal year ending in the future**: Use the most recently completed fiscal year.

---

## 6. Appendices

### Appendix A: Peer Group Assignments

#### G1: Semiconductor Equipment (25 companies)

| ID | Company | Ticker | Sub-segment |
|----|---------|--------|-------------|
| CMP-0001 | Tokyo Seimitsu | 7729.T | Wafer probing, dicing, metrology |
| CMP-0002 | DISCO | 6146.T | Precision cutting, grinding, polishing |
| CMP-0003 | SCREEN Holdings | 7735.T | Cleaning, coating, lithography |
| CMP-0004 | Tokyo Electron | 8035.T | Coater/developer, etch, deposition |
| CMP-0005 | Advantest | 6857.T | Semiconductor test equipment |
| CMP-0006 | Lasertec | 6920.T | EUV mask inspection |
| CMP-0011 | Kokusai Electric | 6525.T | Thin-film deposition (batch furnace) |
| CMP-0012 | Horiba | 6856.T | Mass flow controllers, analytical equipment |
| CMP-0026 | ASML | ASML | Lithography systems (EUV monopoly) |
| CMP-0029 | Naigai Tech | 3374.T | Cleanroom construction, equipment installation |
| CMP-0030 | Marumae | 6264.T | Precision machined parts for equipment |
| CMP-0036 | Ebara | 6361.T | CMP equipment, vacuum pumps |
| CMP-0041 | Rorze | 6323.T | Wafer/glass substrate handling robots |
| CMP-0042 | PILLAR | 6490.T | Fluid control equipment, seals |
| CMP-0043 | CKD | 6407.T | Pneumatic valves, flow controllers |
| CMP-0050 | Nikon | 7731.T | Lithography (DUV/i-line), metrology |
| CMP-0051 | Canon | 7751.T | Lithography (i-line, KrF), NIL |
| CMP-0052 | Organo | 6368.T | Ultrapure water systems |
| CMP-0053 | Nomura Micro Science | 6254.T | Ultrapure water systems |
| CMP-0054 | Aval Data | 6918.T | Image processing boards for inspection |
| CMP-0056 | Daifuku | 6383.T | Cleanroom transport systems (AMHS) |
| CMP-0059 | Shibaura Mechatronics | 6590.T | Coating, sputtering equipment |
| CMP-0060 | Samco | 6387.T | CVD, RIE, plasma etching |
| CMP-0061 | Ushio | 6925.T | UV light sources for lithography |
| CMP-0062 | Tazmo | 6266.T | Coating, developing equipment |

#### G2: Semiconductor Materials (26 companies)

| ID | Company | Ticker | Sub-segment |
|----|---------|--------|-------------|
| CMP-0007 | Fujimi | 5384.T | CMP slurry, polishing materials |
| CMP-0008 | Resonac | 4004.T | Specialty chemicals, advanced packaging materials |
| CMP-0009 | Ferrotec | 6890.T | Silicon parts, thermoelectric modules |
| CMP-0010 | Toyo Gosei | 4970.T | Photoacid generators for EUV resists |
| CMP-0013 | Fuso Chemical | 4368.T | Colloidal silica for CMP |
| CMP-0015 | HOYA | 7741.T | Photomask blanks, EUV pellicles |
| CMP-0024 | Shin-Etsu Chemical | 4063.T | Silicon wafers, photoresists, PVC |
| CMP-0025 | SUMCO | 3436.T | Silicon wafers |
| CMP-0031 | Tocalo | 3433.T | Thermal spray coatings |
| CMP-0032 | Nippon Sanso | 4091.T | Industrial gases for fab |
| CMP-0033 | Tokyo Ohka Kogyo (TOK) | 4186.T | Photoresists, EUV materials |
| CMP-0034 | JSR | 4185.T | Photoresists (delisted, JIC-owned) |
| CMP-0035 | Maruzen Petrochemical | 4634.T | Ultra-high purity solvents |
| CMP-0037 | NGK Insulators | 5333.T | Ceramic substrates, NAS batteries |
| CMP-0038 | Gun Ei Chemical | 4229.T | Phenolic resins for photoresists |
| CMP-0039 | Niterra | 5334.T | Ceramic packages, spark plugs |
| CMP-0040 | FUJIFILM | 4901.T | CMP slurry, photoresists, display materials |
| CMP-0044 | Stella Chemifa | 4109.T | Ultra-high purity hydrofluoric acid |
| CMP-0045 | Kanto Denka Kogyo | 4047.T | Specialty gases (NF3, WF6) |
| CMP-0046 | Sumitomo Chemical | 4005.T | Photoresists, display materials |
| CMP-0047 | TOPPAN | 7911.T | Photomasks, FC-BGA substrates |
| CMP-0048 | Ibiden | 4062.T | IC substrates, printed circuit boards |
| CMP-0049 | Dai Nippon Printing (DNP) | 7912.T | Photomasks, lead frames |
| CMP-0055 | NHK Spring | 5991.T | HDD suspensions, precision springs |
| CMP-0057 | MEC Company | 4971.T | Copper surface treatment chemicals |
| CMP-0058 | Nagase & Co. | 8012.T | Chemical distribution, specialty materials |

#### G3: Semiconductors & Memory (6 companies)

| ID | Company | Ticker | Sub-segment |
|----|---------|--------|-------------|
| CMP-0014 | Kioxia | 285A.T | NAND flash memory |
| CMP-0018 | Samsung Electronics | 005930.KS | Memory + foundry + consumer |
| CMP-0019 | Intel | INTC | Logic, foundry |
| CMP-0020 | SK Hynix | 000660.KS | DRAM, HBM |
| CMP-0021 | Micron | MU | DRAM, NAND |
| CMP-0028 | NVIDIA | NVDA | GPU, AI accelerators |

#### G4: Other (4 companies)

| ID | Company | Ticker | Sub-segment |
|----|---------|--------|-------------|
| CMP-0016 | Olympus | 7733.T | Precision instruments (medical endoscopes) |
| CMP-0017 | TSMC | 2330.TW | Semiconductor foundry |
| CMP-0022 | Apple | AAPL | Consumer electronics (semiconductor customer) |
| CMP-0023 | Western Digital | WDC | Storage (HDD + NAND) |
| CMP-0027 | Kyocera | 6971.T | Ceramic packages, components |

### Appendix B: Reference Sector Medians (to be populated after data collection)

These values will be computed in Step 3 after the data enrichment sweep is complete.

| Peer Group | Tier | Median PER | Median PBR | Median ROE | Median Rev Growth | Median OPM |
|-----------|------|-----------|-----------|-----------|-------------------|-----------|
| G1 Equipment | Large | TBD | TBD | TBD | TBD | TBD |
| G1 Equipment | Mid | TBD | TBD | TBD | TBD | TBD |
| G1 Equipment | Small | TBD | TBD | TBD | TBD | TBD |
| G2 Materials | Large | TBD | TBD | TBD | TBD | TBD |
| G2 Materials | Mid | TBD | TBD | TBD | TBD | TBD |
| G2 Materials | Small | TBD | TBD | TBD | TBD | TBD |
| G3 Semis+Memory | All | TBD | TBD | TBD | TBD | TBD |
| G4 Other | All | TBD | TBD | TBD | TBD | TBD |

### Appendix C: Key Data Source URLs

| Source | URL | Use |
|--------|-----|-----|
| Yahoo Finance Japan | https://finance.yahoo.co.jp/ | PER, PBR, EPS, price, market cap for TSE stocks |
| Yahoo Finance US | https://finance.yahoo.com/ | US/global listed company financials |
| Nikkei Company Data | https://www.nikkei.com/nkd/ | Japanese company financials, shareholder data |
| EDINET | https://disclosure2.edinet-fsa.go.jp/ | Annual securities reports, foreign ownership |
| JPX Listed Company Info | https://www.jpx.co.jp/listing/ | Float data, market cap tiers |
| KRX Market Data | https://data.krx.co.kr/ | Korean-listed company data |
| TWSE Market Data | https://www.twse.com.tw/ | TSMC data |
| Ullet | https://www.ullet.com/ | Quick Japanese company financial lookup |
| Google Finance | https://www.google.com/finance/ | Cross-validation of prices and market caps |
| TradingView | https://www.tradingview.com/ | 52-week range, technical context |
| Bank of Japan | https://www.boj.or.jp/ | JGB yields (for earnings yield spread calculation) |

### Appendix D: Critical Supply Chain Nodes (from graph.json)

The following companies are flagged as critical nodes in the supply chain graph. These companies receive automatic maximum scores on B4 (Supply Chain Centrality = 5).

| ID | Company | Critical Reason |
|----|---------|----------------|
| CMP-0026 | ASML | 100% monopoly on EUV lithography systems |
| CMP-0006 | Lasertec | 100% monopoly on EUV mask/pellicle inspection |
| CMP-0017 | TSMC | 90%+ share of advanced AI chip manufacturing |
| CMP-0024 | Shin-Etsu Chemical | Duopoly with SUMCO in 300mm silicon wafers |
| CMP-0025 | SUMCO | Duopoly with Shin-Etsu in 300mm silicon wafers |
| CMP-0004 | Tokyo Electron | Oligopoly in coater/developer, strong in etch and deposition |
| CMP-0044 | Stella Chemifa | World monopoly in 12-nine purity hydrofluoric acid |
| CMP-0048 | Ibiden | 50%+ share in AI server IC substrates |
| CMP-0052 | Organo | Near-exclusive ultrapure water supplier to TSMC |
| CMP-0005 | Advantest | Duopoly with Teradyne in SoC/memory test |
| CMP-0028 | NVIDIA | 80%+ share in AI training accelerators |

### Appendix E: Schema Field Naming Note

The project `CLAUDE.md` lists a field `ESP` in the data model. The actual JSON schema (`schema/company.schema.json`) defines the field as `EPS` (Earnings Per Share). All references in this framework use `EPS`. When updating company JSON files, use the field name `EPS`, not `ESP`.

### Appendix F: Scoring Worksheet Template

For each company, the scoring worksheet should contain:

```
Company: [Name] ([Ticker])
ID: [CMP-XXXX]
Peer Group: [G1/G2/G3/G4] - [Large/Mid/Small]
Data Coverage: [X/18 fields] = [XX%]
Confidence: [High/Medium/Low/Very Low]

Dimension A: Valuation Ratios          [__] / 30
  A1. PER discount:                    [__] / 12
  A2. Forward PER discount:            [__] / 6
  A3. PBR discount:                    [__] / 8
  A4. Earnings yield spread:           [__] / 4

Dimension B: Supply Chain Moat         [__] / 25
  B1. Market share position:           [__] / 10
  B2. Switching costs:                 [__] / 5
  B3. Technology differentiation:      [__] / 5
  B4. Supply chain centrality:         [__] / 5

Dimension C: Growth & Earnings         [__] / 15
  C1. Revenue growth:                  [__] / 5
  C2. Operating margin:                [__] / 4
  C3. ROE quality:                     [__] / 3
  C4. AI/advanced-node exposure:       [__] / 3

Dimension D: Ownership & Float         [__] / 10
  D1. Foreign ownership gap:           [__] / 5
  D2. Circulating equity dynamics:     [__] / 3
  D3. Price vs 52-week range:          [__] / 2

Dimension E: Catalysts & Sentiment     [__] / 10
  E1. Analyst consensus:               [__] / 4
  E2. Capacity expansion:              [__] / 3
  E3. Policy/macro tailwinds:          [__] / 3

Dimension F: Risk Adjustment           [__] / 10
  F1. Forex sensitivity:               [__] / 3
  F2. Customer concentration:          [__] / 4
  F3. Geopolitical risk:               [__] / 3

Raw Composite:                         [__] / 100
Confidence Multiplier:                 [____]
Final Score:                           [____] / 100

Thesis (for top-10 candidates):
  Mispricing reason: _______________
  Key catalyst: _______________
  Primary risk: _______________
  Conviction: [High / Medium / Low]
```

---

*End of Evaluation Framework*
