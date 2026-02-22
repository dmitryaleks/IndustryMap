# Appendix D: Evaluation Scoring Methodology

> This appendix provides a complete, reproducible reference for the six-dimension undervalued score framework used throughout this book to evaluate 74 semiconductor supply chain companies on a 0--100 scale.

---

## D.1 Framework Overview

The evaluation framework assigns each company a composite score on a scale of 0 to 100, where **100 represents the most undervalued** and **0 represents the most overvalued or fairly valued**. The term "undervalued" is a composite judgment that integrates six independent dimensions of analysis:

- **Cheapness relative to peers** -- valuation ratios below sector medians.
- **Structural advantages not priced in** -- monopoly positions, irreplaceable supply chain roles.
- **Earnings momentum the market has not caught up with** -- accelerating growth, margin expansion, AI and advanced-node tailwinds.
- **Ownership dynamics that signal upside** -- low foreign ownership relative to quality, high float creating buying opportunity.
- **Upcoming catalysts** -- capacity expansion, analyst upgrades, favorable policy changes.
- **Risk adjustment** -- discounting for forex exposure, customer concentration, geopolitical vulnerability.

The composite score is the weighted sum of six dimensions (A through F), each scored independently. The weights sum to 100%, and the maximum possible score is 100 points. Because the maximum point allocation for each dimension already encodes its weight (30 + 25 + 15 + 10 + 10 + 10 = 100), no additional weighting multiplication is required -- the raw sub-score totals are simply summed.

### Key Principles

1. **Peer-relative, not absolute.** A PER of 15 is cheap for semiconductor equipment but expensive for commodity chemicals. All valuation metrics are compared against the company's peer group median, not against an absolute threshold.

2. **Forward-looking bias.** Trailing metrics establish the baseline; forward estimates and growth trajectory determine whether the company deserves a premium or discount relative to that baseline.

3. **Supply chain context matters.** A monopoly supplier scores higher on Dimension B even if its valuation ratios appear "fair." The moat justifies paying up, so a fair-valued monopolist is actually undervalued relative to its strategic importance.

4. **Data transparency.** Every score includes a confidence flag (High, Medium, Low, or Very Low) based on data completeness. Companies with insufficient data receive a penalty in their composite score to prevent false positives.

---

## D.2 Score Interpretation

The following table governs how composite scores should be read:

| Score Range | Interpretation |
|-------------|----------------|
| 80--100 | **Deeply undervalued.** Strong buy signal across multiple dimensions. The market is significantly mispricing the company relative to its fundamentals, competitive position, and forward prospects. |
| 60--79 | **Moderately undervalued.** Attractive entry point with identifiable catalysts. One or more dimensions show clear mispricing, though other dimensions may be fairly valued. |
| 40--59 | **Fairly valued.** Market pricing roughly reflects fundamentals. The company may have individual dimensions that score well (strong moat, cheap on one metric), but these are offset by others (growth headwinds, elevated risk). |
| 20--39 | **Modestly overvalued.** Premium pricing is partially justified by quality, but the market has already priced in most of the upside. Limited margin of safety. |
| 0--19 | **Significantly overvalued.** Market pricing exceeds reasonable intrinsic value across most dimensions. The premium is not supported by fundamentals or forward prospects. |

---

## D.3 Dimension A: Valuation Ratios (30 Points)

**Weight:** 30% of composite score.

**What it captures:** How cheap or expensive the company is relative to sector peers on fundamental valuation metrics. This is the heaviest-weighted dimension because the framework is designed to identify undervalued companies, and valuation ratios are the most direct measure of cheapness.

### Sub-scores

| Sub-dimension | Max Points | Metric |
|---------------|------------|--------|
| A1. PER discount | 12 | Trailing PER vs peer group median PER |
| A2. Forward PER discount | 6 | Forward PER vs peer group median Forward PER |
| A3. PBR discount | 8 | PBR vs peer group median PBR |
| A4. Earnings yield premium | 4 | Earnings yield (1/PER) vs 10-year JGB yield spread |

### A1. PER Discount Score (0--12)

The PER discount measures how cheap a company's trailing price-to-earnings ratio is relative to its peer group median. A ratio below 1.0 means the company trades at a discount to peers; above 1.0 means a premium.

**Formula:**

```
PER_ratio = Company_PER / Peer_Median_PER
```

**Scoring tiers:**

| PER Ratio | Score | Interpretation |
|-----------|-------|----------------|
| <= 0.50 | 12 | 50%+ discount to peers |
| <= 0.70 | 10 | 30--50% discount to peers |
| <= 0.85 | 8 | 15--30% discount to peers |
| <= 1.00 | 6 | 0--15% discount (at or below median) |
| <= 1.15 | 4 | 0--15% premium to peers |
| <= 1.30 | 2 | 15--30% premium to peers |
| > 1.30 | 0 | 30%+ premium to peers |

**Special cases:**

- **Negative PER (loss-making company):** Score = 0. A company that is losing money cannot be considered cheap on an earnings basis.
- **PER > 100 (speculative valuation):** Score = 0. Extreme multiples suggest the market is pricing in highly uncertain future earnings.
- **PER not available:** Score = NULL. This sub-dimension is excluded from the dimension total, and its weight is redistributed proportionally among the available sub-scores (see Section D.3.6 below).

**Example:** Tokyo Seimitsu (7729.T) has a trailing PER of 21.26. Its peer group G1 (Semiconductor Equipment) has a median PER of 31.59. The ratio is 21.26 / 31.59 = 0.673. This falls in the <= 0.70 tier, yielding a score of 10 out of 12.

### A2. Forward PER Discount Score (0--6)

The forward PER discount uses the same methodology as A1 but applies to consensus analyst forward earnings estimates rather than trailing results. It carries half the weight of A1 because forward estimates are inherently less reliable than reported earnings.

**Formula:**

```
Forward_PER_ratio = Company_Forward_PER / Peer_Median_Forward_PER
```

**Scoring tiers:**

| Forward PER Ratio | Score |
|-------------------|-------|
| <= 0.50 | 6 |
| <= 0.70 | 5 |
| <= 0.85 | 4 |
| <= 1.00 | 3 |
| <= 1.15 | 2 |
| <= 1.30 | 1 |
| > 1.30 | 0 |

**Note on data availability:** Forward PER requires analyst consensus estimates, which are not available for all companies in the dataset. As of this writing, A2 remains the sub-dimension with the lowest data coverage across the 74-company universe. When unavailable, A2 is scored as NULL and its 6 points are redistributed proportionally across A1, A3, and A4.

### A3. PBR Discount Score (0--8)

The price-to-book ratio measures how the market values the company relative to its net asset value. In capital-intensive semiconductor industries, book value provides a floor valuation that is meaningful for asset-heavy manufacturers.

**Formula:**

```
PBR_ratio = Company_PBR / Peer_Median_PBR
```

**Scoring tiers:**

| PBR Ratio | Score | Interpretation |
|-----------|-------|----------------|
| <= 0.50 | 8 | 50%+ discount to peer median PBR |
| <= 0.70 | 6 | 30--50% discount |
| <= 0.85 | 5 | 15--30% discount |
| <= 1.00 | 4 | At or below peer median |
| <= 1.20 | 2 | 0--20% premium |
| > 1.20 | 0 | 20%+ premium |

**Absolute book value bonus:** If the company's PBR is below 1.0 in absolute terms (i.e., the stock trades below its book value per share), a bonus of +1 point is awarded, capped at the maximum of 8. The rationale is that trading below book value is an additional undervaluation signal regardless of peer comparison. This bonus applies after the tier-based score is determined.

**Example:** Gun Ei Chemical (4229.T) has a PBR of 0.64. Its peer group G2 (Semiconductor Materials) has a median PBR of 1.32. The ratio is 0.64 / 1.32 = 0.485, placing it in the <= 0.50 tier for a base score of 8. Since the absolute PBR of 0.64 is also below 1.0, the bonus would apply, but the score is already at the maximum of 8. The absolute-value bonus is relevant primarily when a company with PBR < 1.0 falls into a mid-range tier (e.g., 4 or 5) -- the +1 pushes it up by one point.

### A4. Earnings Yield Spread (0--4)

The earnings yield spread measures how much the company's earnings yield exceeds the risk-free rate, proxied by the 10-year Japanese Government Bond (JGB) yield. A wide spread indicates the stock is cheap relative to government bonds.

**Formula:**

```
Earnings_Yield = 1 / PER
Spread = Earnings_Yield - JGB_10Y_Yield
```

The reference JGB 10-year yield used in this framework is **1.50%** (as of February 2026).

**Scoring tiers:**

| Spread | Score | Interpretation |
|--------|-------|----------------|
| >= 6% | 4 | Earnings yield far exceeds risk-free rate |
| >= 4% | 3 | Significant premium over risk-free |
| >= 2% | 2 | Moderate premium over risk-free |
| >= 0% | 1 | Earnings yield just exceeds risk-free rate |
| < 0% | 0 | Earnings yield below risk-free rate (very expensive) |

**Example:** A company with a PER of 15 has an earnings yield of 6.67%. The spread over the 1.50% JGB yield is 5.17%, which falls in the >= 4% tier for a score of 3. A company with a PER of 50 has an earnings yield of 2.00%, yielding a spread of only 0.50%, scoring 1.

### Dimension A Total

```
A_score = A1 + A2 + A3 + A4
Maximum: 12 + 6 + 8 + 4 = 30 points
```

### Missing Data Adjustment for Dimension A

If any sub-score is NULL due to missing data, its weight is redistributed proportionally among the available sub-scores. The formula is:

```
A_score_adjusted = (sum of available sub-scores) / (max of available sub-scores) * 30
```

**Worked example:**

Suppose a company has:
- A1 = 10 (out of 12)
- A2 = NULL (Forward PER unavailable)
- A3 = 5 (out of 8)
- A4 = 3 (out of 4)

The available maximum is 12 + 8 + 4 = 24. The available sum is 10 + 5 + 3 = 18. The adjusted score is (18 / 24) x 30 = **22.5 out of 30**.

This approach ensures that companies are not penalized simply for lacking forward PER estimates, while maintaining comparable scoring across the full universe.

---

## D.4 Dimension B: Supply Chain Moat (25 Points)

**Weight:** 25% of composite score.

**What it captures:** The company's irreplaceability in the semiconductor supply chain, monopoly or oligopoly positioning, and competitive barriers. This dimension is **semi-quantitative**: it uses structured rubrics applied through qualitative assessment informed by the supply chain graph data and industry research.

### Sub-scores

| Sub-dimension | Max Points | Assessment basis |
|---------------|------------|------------------|
| B1. Market share position | 10 | Estimated global market share in primary product |
| B2. Switching costs / lock-in | 5 | Customer dependency, qualification cycles, integration depth |
| B3. Technology differentiation | 5 | Patent moat, process know-how, R&D intensity |
| B4. Supply chain centrality | 5 | Graph degree (supplier/client edges), critical node status |

### B1. Market Share Position (0--10)

Market share is the single largest sub-score in Dimension B because it is the most direct indicator of competitive dominance and pricing power.

| Estimated Global Market Share | Score | Description |
|-------------------------------|-------|-------------|
| >70% (monopoly) | 10 | Dominant, no viable alternative. Examples: ASML in EUV lithography, Lasertec in EUV mask inspection. |
| 40--70% (oligopoly leader) | 8 | Leading share in oligopoly with 2--3 players. |
| 25--40% (strong #1 or #2) | 6 | Significant share with meaningful competition. |
| 10--25% (notable player) | 4 | Recognized participant with some pricing power. |
| 5--10% (niche) | 2 | Niche presence, limited pricing power. |
| <5% or unknown | 0 | Commodity participant or insufficient data. |

Market share estimates are sourced from company disclosures, industry analyst reports, and investor presentations. Where exact figures are unavailable, ranges are estimated from known competitive dynamics and cross-referenced against multiple sources.

### B2. Switching Costs / Lock-in (0--5)

Switching costs reflect how difficult it is for a customer to replace a given supplier. In semiconductor manufacturing, where process qualification can take months to years and a single material change can destroy wafer yields, switching costs are often the deepest source of competitive moat.

| Level | Score | Criteria |
|-------|-------|----------|
| Extreme | 5 | Multi-year qualification required. Product is designed around the supplier's specification. Customer's manufacturing process would require re-development to switch. Example: photoresist for a specific lithography node. |
| High | 4 | 6--18 month qualification cycle. Significant requalification cost and yield risk. |
| Moderate | 3 | 3--6 month switch possible. Some integration effort and testing required. |
| Low | 2 | Commodity supply with multiple qualified vendors. Switching primarily a logistics exercise. |
| Minimal | 0--1 | Drop-in replacement available. No qualification barrier. |

### B3. Technology Differentiation (0--5)

Technology differentiation assesses the depth of a company's proprietary knowledge, patent protection, and R&D capability relative to competitors.

| Level | Score | Criteria |
|-------|-------|----------|
| Unique | 5 | Only company capable of producing the product at the required specification. No known competitor can replicate the technology within 3+ years. |
| Leading | 4 | Best-in-class with significant patent portfolio. 2--3 year lead over nearest competitor. |
| Strong | 3 | Differentiated technology with meaningful competitive advantage. 1--2 year lead over competitors. |
| Moderate | 2 | Some differentiation, competitive R&D spending, but peers offer comparable solutions. |
| Commodity | 0--1 | Standard product. Many capable producers worldwide. |

### B4. Supply Chain Centrality (0--5)

This sub-score is derived algorithmically from the supply chain graph (`data/graph.json`), which contains 110 company nodes and 321 edges. Two inputs determine the score: the company's degree (total number of supplier and client edges) and whether it appears on the critical nodes list.

**Formula:**

```
Degree = count(supplier edges) + count(client edges)
Critical_flag = 1 if company is in the criticalNodes list, 0 otherwise

If Critical_flag == 1:                    score = 5
Else if Degree >= 10:                     score = 4
Else if Degree >= 6:                      score = 3
Else if Degree >= 3:                      score = 2
Else:                                     score = 1
```

The critical node designation overrides the degree-based score. A company designated as a critical node receives the maximum score of 5 regardless of its edge count, reflecting its systemic importance to the supply chain even if it has relatively few direct connections.

**Critical nodes in the dataset (automatic score = 5):**

| ID | Company | Reason for Critical Designation |
|----|---------|--------------------------------|
| CMP-0026 | ASML | 100% monopoly on EUV lithography systems |
| CMP-0006 | Lasertec | 100% monopoly on EUV mask and pellicle inspection |
| CMP-0017 | TSMC | 90%+ share of advanced AI chip manufacturing |
| CMP-0024 | Shin-Etsu Chemical | Duopoly with SUMCO in 300mm silicon wafers |
| CMP-0025 | SUMCO | Duopoly with Shin-Etsu in 300mm silicon wafers |
| CMP-0004 | Tokyo Electron | Oligopoly in coater/developer, strong in etch and deposition |
| CMP-0044 | Stella Chemifa | World monopoly in twelve-nine purity hydrofluoric acid |
| CMP-0048 | Ibiden | 50%+ share in AI server IC substrates |
| CMP-0052 | Organo | Near-exclusive ultrapure water supplier to TSMC |
| CMP-0005 | Advantest | Duopoly with Teradyne in SoC and memory test |
| CMP-0028 | NVIDIA | 80%+ share in AI training accelerators |

### Dimension B Total

```
B_score = B1 + B2 + B3 + B4
Maximum: 10 + 5 + 5 + 5 = 25 points
```

---

## D.5 Dimension C: Growth & Earnings Quality (15 Points)

**Weight:** 15% of composite score.

**What it captures:** Revenue growth trajectory, margin quality, and exposure to secular growth themes -- specifically AI infrastructure, advanced packaging, and EUV adoption. This dimension rewards companies whose earnings power is expanding, not merely stable.

### Sub-scores

| Sub-dimension | Max Points | Metric |
|---------------|------------|--------|
| C1. Revenue growth (YoY) | 5 | Most recent fiscal year revenue growth percentage |
| C2. Operating margin | 4 | Operating margin vs peer median |
| C3. ROE quality | 3 | ROE vs peer median, consistency |
| C4. AI / advanced-node exposure | 3 | Qualitative: revenue percentage tied to AI, HBM, EUV, advanced packaging |

### C1. Revenue Growth Score (0--5)

Revenue growth is measured on a trailing year-over-year basis using the most recently completed fiscal year.

| YoY Revenue Growth | Score |
|--------------------|-------|
| >= 30% | 5 |
| >= 20% | 4 |
| >= 10% | 3 |
| >= 0% | 2 |
| >= -10% | 1 |
| < -10% | 0 |

**Note on fiscal year alignment:** Most Japanese companies in this dataset report on a March fiscal year (FY ending March 2025 for the most recent complete year). Non-Japanese companies typically report on a December calendar year (CY2024 for the most recent). Growth rates are computed within each company's own fiscal calendar.

### C2. Operating Margin Score (0--4)

Operating margin is compared against the peer group median to assess relative profitability.

**Formula:**

```
OPM_ratio = Company_OPM / Peer_Median_OPM
```

| OPM Ratio | Score | Interpretation |
|-----------|-------|----------------|
| >= 1.50 | 4 | Operating margin 50%+ above peer median |
| >= 1.20 | 3 | 20--50% above peer median |
| >= 0.90 | 2 | Roughly in line with peers (within 10%) |
| >= 0.60 | 1 | 10--40% below peer median |
| < 0.60 | 0 | 40%+ below peer median |

### C3. ROE Quality Score (0--3)

Return on equity measures how efficiently the company converts shareholder equity into earnings. ROE is computed as:

```
ROE = EPS / BPS
```

Or equivalently:

```
ROE = PBR / PER
```

The second formula is used when EPS and book value per share are not directly available but PER and PBR are.

| ROE Level | Score | Criteria |
|-----------|-------|----------|
| >= 20% and above peer median | 3 | Exceptional capital efficiency, outperforming peers |
| >= 12% and near peer median | 2 | Good capital efficiency, in line with sector |
| >= 5% | 1 | Adequate but below average |
| < 5% or negative | 0 | Poor capital efficiency or loss-making |

### C4. AI / Advanced-Node Exposure (0--3)

This sub-score is a qualitative assessment of how much of the company's revenue and growth prospects are tied to the secular themes driving semiconductor capital expenditure: AI training and inference infrastructure, high-bandwidth memory (HBM), EUV lithography adoption, advanced packaging (CoWoS, fan-out), and sub-5nm process nodes.

| Exposure Level | Score | Examples |
|----------------|-------|----------|
| High (>30% of revenue from AI/advanced themes) | 3 | Advantest (HBM testing), Lasertec (EUV mask inspection), Ibiden (AI server IC substrates), ASML (EUV systems) |
| Moderate (10--30%) | 2 | Advanced node materials suppliers, CoWoS substrate makers |
| Low (<10% but present) | 1 | Indirect exposure through major customers shifting to advanced nodes |
| None or negligible | 0 | Legacy node only, non-AI segments dominate |

### Dimension C Total

```
C_score = C1 + C2 + C3 + C4
Maximum: 5 + 4 + 3 + 3 = 15 points
```

---

## D.6 Dimension D: Ownership & Float (10 Points)

**Weight:** 10% of composite score.

**What it captures:** Foreign ownership gap (room for institutional buying), float dynamics, and price positioning within the 52-week range. This dimension is particularly relevant for Japanese equities, where foreign institutional ownership has historically been a powerful catalyst for price discovery.

### Sub-scores

| Sub-dimension | Max Points | Metric |
|---------------|------------|--------|
| D1. Foreign ownership gap | 5 | Current foreign ownership percentage vs expected level given quality |
| D2. Circulating equity dynamics | 3 | Free float percentage, treasury stock buyback activity |
| D3. Price vs 52-week range | 2 | Where current price sits relative to its 52-week trading range |

### D1. Foreign Ownership Gap (0--5)

The thesis behind this sub-score: companies with **lower** foreign ownership than their quality warrants have room for foreign institutional buying, which is a positive catalyst for price appreciation. Foreign investors tend to discover high-quality small- and mid-cap Japanese companies later than domestic institutions, creating a window of opportunity.

**Step 1 -- Determine quality tier from Dimension B score:**

```
If B_score >= 18:  Quality_Tier = "High"
If B_score >= 12:  Quality_Tier = "Medium"
Else:              Quality_Tier = "Low"
```

**Step 2 -- Determine expected foreign ownership range:**

| Quality Tier | Expected Foreign Ownership Range | Midpoint |
|--------------|----------------------------------|----------|
| High | 40--50% | 45% |
| Medium | 25--35% | 30% |
| Low | 10--20% | 15% |

**Step 3 -- Compute gap and score:**

```
Gap = Expected_Midpoint - Actual_Foreign_Ownership
```

| Gap | Score | Interpretation |
|-----|-------|----------------|
| >= 20% | 5 | Severely under-owned by foreigners relative to quality |
| >= 15% | 4 | Significantly under-owned |
| >= 10% | 3 | Moderately under-owned |
| >= 5% | 2 | Slightly under-owned |
| >= 0% | 1 | Near expected ownership level |
| < 0% | 0 | Already at or above expected ownership (no gap) |

**Example:** PILLAR Corporation (6490.T) has a B_score of 20 (quality tier: High, expected midpoint = 45%). Its actual foreign ownership is 21.28%. The gap is 45% - 21.28% = 23.72%, which falls in the >= 20% tier for a maximum score of 5. This represents a significant ownership gap: a high-quality monopoly supplier that foreign institutions have not yet discovered.

### D1 Adaptation for Non-Japanese Companies

For the 11 non-Japanese companies in the dataset (TSMC, Samsung, Intel, SK Hynix, Micron, Apple, Western Digital, ASML, NVIDIA, and others), the Japan-specific "foreign ownership gap" model is not applicable. Instead, D1 substitutes an institutional ownership change score:

```
If institutional ownership increased > 5% in past year:   score = 5
If institutional ownership increased 2--5%:                score = 4
If stable (+/- 2%):                                        score = 2
If decreased 2--5%:                                        score = 1
If decreased > 5%:                                         score = 0
```

### D2. Circulating Equity Dynamics (0--3)

This sub-score assesses float tightness and buyback activity, both of which can reduce available supply of shares and create upward price pressure.

| Condition | Score |
|-----------|-------|
| Active buyback program AND float < 70% | 3 |
| Active buyback program OR float < 70% | 2 |
| Float 70--90%, no buyback | 1 |
| Float > 90%, no buyback | 0 |

"Active buyback program" means the company has announced or is currently executing a share repurchase program within the past 12 months, as disclosed in company IR materials or securities filings.

### D3. Price vs 52-Week Range (0--2)

This sub-score measures where the current stock price sits within its trailing 52-week range. Companies trading near their 52-week low offer more potential upside from a mean-reversion perspective.

**Formula:**

```
Position = (Current_Price - 52W_Low) / (52W_High - 52W_Low)
```

| Position in Range | Score | Interpretation |
|-------------------|-------|----------------|
| <= 0.25 | 2 | Near 52-week low -- potential value entry point |
| <= 0.50 | 1 | Lower half of range |
| > 0.50 | 0 | Upper half of range -- less upside from range perspective |

### Dimension D Total

```
D_score = D1 + D2 + D3
Maximum: 5 + 3 + 2 = 10 points
```

---

## D.7 Dimension E: Catalysts & Sentiment (10 Points)

**Weight:** 10% of composite score.

**What it captures:** Near-term price catalysts including analyst consensus, capacity expansion plans, policy tailwinds, and material news that could drive re-rating. This dimension is the most time-sensitive -- catalysts have expiration dates, and the scores should be periodically refreshed.

### Sub-scores

| Sub-dimension | Max Points | Assessment basis |
|---------------|------------|------------------|
| E1. Analyst consensus | 4 | Buy/hold/sell distribution and price target vs current price |
| E2. Capacity expansion / capex plans | 3 | Announced factory builds, equipment orders, R&D commitments |
| E3. Policy / macro tailwinds | 3 | Government subsidies, trade policy, industry cycle position |

### E1. Analyst Consensus (0--4)

Analyst consensus is evaluated on two criteria: the direction of recommendations (buy/hold/sell distribution) and the magnitude of upside to the average price target.

**Formula:**

```
Upside = (Average_Price_Target / Current_Price) - 1
```

| Condition | Score |
|-----------|-------|
| Upside >= 30% AND majority Buy ratings | 4 |
| Upside >= 15% AND more Buy than Sell | 3 |
| Upside >= 0% AND balanced ratings | 2 |
| Upside < 0% OR majority Hold | 1 |
| Majority Sell AND negative target gap | 0 |

"Majority" means more than 50% of covering analysts. "More Buy than Sell" means Buy count exceeds Sell count even if neither constitutes a majority. Analyst coverage data is sourced from Yahoo Finance and Refinitiv consensus databases.

### E2. Capacity Expansion (0--3)

| Signal | Score | Criteria |
|--------|-------|----------|
| Major expansion | 3 | New fab or facility announced, significant capex increase (>30% YoY), M&A activity targeting capacity |
| Moderate investment | 2 | Equipment upgrades, incremental capacity additions, new product line investments |
| Maintenance level | 1 | Steady capex at historical levels, no major announcements |
| Contraction | 0 | Capex cuts, facility closures, restructuring charges |

### E3. Policy / Macro Tailwinds (0--3)

| Signal | Score | Criteria |
|--------|-------|----------|
| Direct beneficiary | 3 | Named in government subsidy program (e.g., METI semiconductor strategy, CHIPS Act for US companies), favorable trade ruling, industry policy specifically targeting company's segment |
| Indirect beneficiary | 2 | Sector-level tailwind such as semiconductor cycle upturn, yen weakness benefiting exporters, broad policy support for the industry |
| Neutral | 1 | No notable policy impact in either direction |
| Headwind | 0 | Export controls restricting sales, trade restrictions, unfavorable regulatory actions |

### Dimension E Total

```
E_score = E1 + E2 + E3
Maximum: 4 + 3 + 3 = 10 points
```

---

## D.8 Dimension F: Risk Adjustment (10 Points)

**Weight:** 10% of composite score.

**What it captures:** Downside risks that should temper the undervalued thesis. This dimension is **inverted** relative to the others: a **higher** score means **lower** risk, and therefore greater conviction that any undervaluation identified in Dimensions A through E will be realized. A risky company scores low; a safe company scores high.

### Sub-scores

| Sub-dimension | Max Points | Risk factor |
|---------------|------------|-------------|
| F1. Forex sensitivity | 3 | Dependence on USD/JPY movements |
| F2. Customer concentration | 4 | Revenue dependency on top 1--3 customers |
| F3. Geopolitical risk | 3 | Exposure to China/Taiwan supply chain disruption |

### F1. Forex Sensitivity (0--3)

Higher score = lower forex risk. The scoring uses the `ifForexSensitive` flag in the company database combined with revenue geographic breakdown.

| Condition | Score |
|-----------|-------|
| Not forex sensitive AND domestic revenue > 50% | 3 |
| Not forex sensitive AND mixed revenue (domestic and overseas) | 2 |
| Forex sensitive AND hedging program in place | 1 |
| Forex sensitive AND unhedged or heavy overseas exposure | 0 |

The `ifForexSensitive` flag is set to true when overseas revenue exceeds 50% of total revenue, as disclosed in the company's annual report. The reference exchange rate for the framework is USD/JPY 152.0 (as of February 2026).

### F2. Customer Concentration (0--4)

Higher score = lower concentration risk. This is the heaviest sub-score in Dimension F because customer concentration represents the most direct operational risk: the loss of a single customer can be catastrophic.

| Top Customer Revenue Share | Score | Interpretation |
|----------------------------|-------|----------------|
| < 15% of revenue | 4 | Well diversified customer base |
| 15--25% | 3 | Moderate concentration |
| 25--40% | 2 | Notable concentration |
| 40--60% | 1 | High concentration |
| > 60% | 0 | Extreme concentration risk |

Customer concentration is estimated from company disclosures, supply chain graph client edges, and industry knowledge. Where exact revenue breakdowns by customer are not disclosed, estimates are derived from the number and relative importance of client edges in the supply chain graph.

### F3. Geopolitical Risk (0--3)

Higher score = lower geopolitical risk. This sub-score assesses exposure to the two primary geopolitical risks in the semiconductor supply chain: China-related trade and export control risk, and Taiwan-related supply chain continuity risk.

| Condition | Score |
|-----------|-------|
| Minimal China/Taiwan exposure | 3 |
| Moderate exposure with active diversification | 2 |
| Significant China manufacturing presence or sales (15--30% of revenue) | 1 |
| Critical Taiwan dependency OR China revenue > 30% | 0 |

**Context for Japan-based companies:** Japanese semiconductor equipment and materials companies face a particular geopolitical dynamic. Japan's October 2023 export control revisions (aligned with US policy) restrict sales of advanced equipment to China, directly impacting companies like Tokyo Electron, SCREEN Holdings, and Tokyo Seimitsu, all of which derived significant revenue from Chinese customers. The China revenue percentage estimate in the dataset reflects this exposure.

### Dimension F Total

```
F_score = F1 + F2 + F3
Maximum: 3 + 4 + 3 = 10 points
```

---

## D.9 Composite Score Calculation

### Raw Composite

```
Raw_Composite = A_score + B_score + C_score + D_score + E_score + F_score

Range: 0 to 100
```

Each dimension already carries its weight in its maximum point allocation:

| Dimension | Max Points | Weight |
|-----------|------------|--------|
| A. Valuation Ratios | 30 | 30% |
| B. Supply Chain Moat | 25 | 25% |
| C. Growth & Earnings Quality | 15 | 15% |
| D. Ownership & Float | 10 | 10% |
| E. Catalysts & Sentiment | 10 | 10% |
| F. Risk Adjustment | 10 | 10% |
| **Total** | **100** | **100%** |

No additional weighting multiplication is needed -- the raw sub-score totals are summed directly.

### Data Confidence Modifier

After computing the raw composite, a confidence adjustment is applied to penalize companies with incomplete data. This prevents companies from being falsely ranked as "undervalued" simply because risk signals or overvaluation indicators are missing from the dataset.

**Formula:**

```
Data_Coverage = (number of non-null required fields) / (total required fields)
```

The required fields for full coverage are the 18 data points listed in Section D.11 below.

| Data Coverage | Confidence Level | Multiplier | Effect |
|---------------|-----------------|------------|--------|
| >= 80% | High | 1.00 | No penalty |
| >= 60% | Medium | 0.95 | 5% haircut |
| >= 40% | Low | 0.85 | 15% haircut |
| < 40% | Very Low | 0.70 | 30% haircut |

**Final score formula:**

```
Final_Score = Raw_Composite * Confidence_Multiplier
```

**Example:** A company with a raw composite of 72 but only 55% data coverage (Medium confidence) receives a final score of 72 x 0.95 = **68.4**.

### Sensitivity Analysis

To test the robustness of rankings, the framework supports re-weighting the dimensions under alternative scenarios:

| Scenario | A | B | C | D | E | F | Purpose |
|----------|---|---|---|---|---|---|---------|
| Base case | 30 | 25 | 15 | 10 | 10 | 10 | Default weights as described above |
| Value-heavy | 40 | 20 | 10 | 10 | 10 | 10 | Emphasizes cheapness over all other factors |
| Moat-heavy | 20 | 35 | 15 | 10 | 10 | 10 | Emphasizes competitive position and irreplaceability |
| Growth-heavy | 20 | 20 | 25 | 10 | 15 | 10 | Emphasizes growth trajectory and catalyst momentum |
| Equal-weight | 17 | 17 | 17 | 17 | 16 | 16 | Removes all bias, tests for broad multi-dimensional undervaluation |

Companies that remain in the top 10 across all five scenarios are considered to have the highest conviction. In the equal-weight scenario, each dimension's raw sub-scores are rescaled to the target weight before summing.

---

## D.10 Peer Group Definitions and Median Values

Companies are grouped into four peer cohorts for relative comparison. All valuation ratio comparisons (A1, A2, A3), margin comparisons (C2), and ROE comparisons (C3) use the median values of the company's peer group as the benchmark.

### Peer Group Assignments

**G1: Semiconductor Equipment (25 companies)**

Companies that design, manufacture, or service equipment used in semiconductor fabrication. This includes lithography systems, deposition tools, etch systems, cleaning equipment, CMP systems, test equipment, metrology instruments, wafer handling robots, ultrapure water systems, and fab infrastructure components.

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
| CMP-0041 | Rorze | 6323.T | Wafer and glass substrate handling robots |
| CMP-0042 | PILLAR | 6490.T | Fluid control equipment, seals |
| CMP-0043 | CKD | 6407.T | Pneumatic valves, flow controllers |
| CMP-0050 | Nikon | 7731.T | Lithography (DUV/i-line), metrology |
| CMP-0051 | Canon | 7751.T | Lithography (i-line, KrF), nanoimprint |
| CMP-0052 | Organo | 6368.T | Ultrapure water systems |
| CMP-0053 | Nomura Micro Science | 6254.T | Ultrapure water systems |
| CMP-0054 | Aval Data | 6918.T | Image processing boards for inspection |
| CMP-0056 | Daifuku | 6383.T | Cleanroom transport systems (AMHS) |
| CMP-0059 | Shibaura Mechatronics | 6590.T | Coating, sputtering equipment |
| CMP-0060 | Samco | 6387.T | CVD, RIE, plasma etching |
| CMP-0061 | Ushio | 6925.T | UV light sources for lithography |
| CMP-0062 | Tazmo | 6266.T | Coating, developing equipment |

**G2: Semiconductor Materials (26 companies)**

Companies that produce raw materials, chemicals, gases, substrates, and consumables used in semiconductor manufacturing. This includes silicon wafers, photoresists, CMP slurries, specialty gases, solvents, photomask blanks, IC substrates, and surface treatment chemicals.

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

**G3: Semiconductors & Memory (6 companies)**

Companies that design and/or manufacture semiconductor devices -- logic, memory, and GPU processors. These are the demand-side drivers of the supply chain.

| ID | Company | Ticker | Sub-segment |
|----|---------|--------|-------------|
| CMP-0014 | Kioxia | 285A.T | NAND flash memory |
| CMP-0018 | Samsung Electronics | 005930.KS | Memory, foundry, and consumer electronics |
| CMP-0019 | Intel | INTC | Logic and foundry |
| CMP-0020 | SK Hynix | 000660.KS | DRAM and HBM |
| CMP-0021 | Micron | MU | DRAM and NAND |
| CMP-0028 | NVIDIA | NVDA | GPU and AI accelerators |

**G4: Other (5 companies)**

A catch-all group for companies that do not fit neatly into the equipment, materials, or semiconductor device categories. These companies are compared against G1/G2 medians weighted by their closest resemblance, or scored using absolute thresholds.

| ID | Company | Ticker | Sub-segment |
|----|---------|--------|-------------|
| CMP-0016 | Olympus | 7733.T | Precision instruments (medical endoscopes) |
| CMP-0017 | TSMC | 2330.TW | Semiconductor foundry |
| CMP-0022 | Apple | AAPL | Consumer electronics (semiconductor customer) |
| CMP-0023 | Western Digital | WDC | Storage (HDD and NAND) |
| CMP-0027 | Kyocera | 6971.T | Ceramic packages, components |

### Market Cap Tiers

Within each industry group, companies are further classified by market capitalization to ensure comparisons are made among similarly-sized peers:

| Tier | Market Cap (JPY) | Label |
|------|------------------|-------|
| Large | > 1 trillion | Large-cap |
| Mid | 100 billion -- 1 trillion | Mid-cap |
| Small | < 100 billion | Small-cap |

Peer medians are ideally calculated within each (Industry Group x Market Cap Tier) cell. If a cell contains fewer than 3 companies, it is merged with the adjacent tier to ensure statistical meaningfulness of the median.

### Reference Sector Medians

The following peer group medians were computed after the February 2026 research sweep, which populated financial data for the majority of the 74-company universe.

| Peer Group | Median PER | Median PBR | Median ROE | Median Revenue Growth | Median OPM |
|------------|------------|------------|------------|-----------------------|------------|
| G1: Semiconductor Equipment | 31.59 | 2.49 | 14.65% | 15.6% | 14.9% |
| G2: Semiconductor Materials | 17.0 | 1.32 | 9.38% | 7.0% | 15.19% |
| G3: Semiconductors & Memory | 29.3 | 2.11 | 22.55% | 61.6% | 22.4% |
| G4: Other | 27.7 | 9.9 | 38.8% | 7.7% | 28.0% |

**Notes on the medians:**

- **G1 Equipment** has the highest median PER (31.59) and PBR (2.49) among the Japanese-heavy groups, reflecting the market's premium for equipment companies' operating leverage to the semiconductor capital expenditure cycle.
- **G2 Materials** has the lowest median PER (17.0) and PBR (1.32), reflecting the market's lower growth expectations for materials companies, many of which have diversified businesses beyond semiconductors.
- **G3 Semiconductors** shows the highest median revenue growth (61.6%), driven by the explosive AI-related demand cycle affecting NVIDIA, SK Hynix (HBM), and Samsung. The median ROE of 22.55% reflects the capital efficiency of fabless and memory-focused business models.
- **G4 Other** shows the highest median PBR (9.9) and OPM (28.0%), heavily influenced by TSMC and Apple, both of which command extreme premium valuations.

### Additional Reference Rate

- **10-year JGB yield:** 1.50% (used for Dimension A4 earnings yield spread calculation)
- **USD/JPY exchange rate:** 152.0 (used for converting non-JPY market caps and financials)

---

## D.11 Data Requirements and Coverage

### Required Fields per Company

The following 18 data points are required (or desired) for a complete scoring of each company. Data coverage across these fields determines the confidence level applied to the composite score.

| # | Field | Source | Used In |
|---|-------|--------|---------|
| 1 | PER (trailing 12M) | Yahoo Finance, Nikkei, Bloomberg | A1, A4 |
| 2 | Forward PER | Analyst consensus | A2 |
| 3 | PBR | Yahoo Finance, Nikkei | A3 |
| 4 | EPS (trailing 12M) | Yahoo Finance, annual report | A4, C3 |
| 5 | ROE | Derived: PBR / PER or EPS / BPS | C3 |
| 6 | Market cap (JPY) | Yahoo Finance | Peer group tier |
| 7 | Latest stock price (JPY) | Yahoo Finance, Google Finance | D3, E1 |
| 8 | Foreign ownership % | Company IR, EDINET, Nikkei | D1 |
| 9 | Circulating equity % | Company IR, JPX | D2 |
| 10 | 52-week high | Yahoo Finance | D3 |
| 11 | 52-week low | Yahoo Finance | D3 |
| 12 | Revenue (latest FY, JPY) | Annual report, Yahoo Finance | C1 |
| 13 | Revenue growth YoY % | Derived from consecutive FY revenue | C1 |
| 14 | Operating margin % | Annual report, Yahoo Finance | C2 |
| 15 | Dividend yield | Yahoo Finance | Reference only |
| 16 | Analyst consensus (Buy/Hold/Sell + avg target) | Yahoo Finance, Refinitiv | E1 |
| 17 | Recent material news | Company IR, Nikkei, Reuters | E2, E3 |
| 18 | Forex sensitivity flag | Annual report (overseas revenue %) | F1 |

### Confidence Level Thresholds

| Data Coverage | Fields Available (of 18) | Confidence | Composite Multiplier |
|---------------|--------------------------|------------|---------------------|
| >= 80% | 15+ fields | High | 1.00 (no penalty) |
| >= 60% | 11--14 fields | Medium | 0.95 (5% haircut) |
| >= 40% | 8--10 fields | Low | 0.85 (15% haircut) |
| < 40% | 0--7 fields | Very Low | 0.70 (30% haircut) |

### Handling Special Cases

**Delisted companies.** JSR Corporation (CMP-0034) was delisted in 2024 following acquisition by the Japan Investment Corporation (JIC). No public market data is available. Dimension A is scored as NULL entirely. Dimensions B through F are scored from available qualitative data (supply chain position, technology assessment, industry reports). The maximum confidence penalty applies. The company is flagged as "not actionable for public equity investment."

**Non-Japanese companies.** Foreign ownership metrics in Dimension D are adapted as described in Section D.6. Financial data is converted to JPY using the reference USD/JPY rate of 152.0 (or KRW/JPY, TWD/JPY as appropriate) for market cap and revenue comparisons. Peer group medians within G3 and G4 account for the different reporting currencies.

**Fiscal year misalignment.** Companies with fiscal years ending in the future use the most recently completed fiscal year. Most Japanese companies report on a March fiscal year (FY ending March 2025), while non-Japanese companies typically report on a December calendar year (CY ending December 2024).

---

## D.12 Scoring Worksheet Template

For each company, the scoring worksheet follows this standardized format. This template is used internally during the evaluation process and is reproduced here for reference transparency.

```
Company:     [Name] ([Ticker])
ID:          [CMP-XXXX]
Peer Group:  [G1/G2/G3/G4] - [Large/Mid/Small]
Data Coverage: [X/18 fields] = [XX%]
Confidence:  [High/Medium/Low/Very Low]

Dimension A: Valuation Ratios              [__] / 30
  A1. PER discount:                        [__] / 12
  A2. Forward PER discount:                [__] / 6
  A3. PBR discount:                        [__] / 8
  A4. Earnings yield spread:               [__] / 4

Dimension B: Supply Chain Moat             [__] / 25
  B1. Market share position:               [__] / 10
  B2. Switching costs:                     [__] / 5
  B3. Technology differentiation:          [__] / 5
  B4. Supply chain centrality:             [__] / 5

Dimension C: Growth & Earnings Quality     [__] / 15
  C1. Revenue growth:                      [__] / 5
  C2. Operating margin:                    [__] / 4
  C3. ROE quality:                         [__] / 3
  C4. AI/advanced-node exposure:           [__] / 3

Dimension D: Ownership & Float             [__] / 10
  D1. Foreign ownership gap:               [__] / 5
  D2. Circulating equity dynamics:         [__] / 3
  D3. Price vs 52-week range:              [__] / 2

Dimension E: Catalysts & Sentiment         [__] / 10
  E1. Analyst consensus:                   [__] / 4
  E2. Capacity expansion:                  [__] / 3
  E3. Policy/macro tailwinds:              [__] / 3

Dimension F: Risk Adjustment               [__] / 10
  F1. Forex sensitivity:                   [__] / 3
  F2. Customer concentration:              [__] / 4
  F3. Geopolitical risk:                   [__] / 3

Raw Composite:                             [__] / 100
Confidence Multiplier:                     [____]
Final Score:                               [____] / 100

Thesis (for top-10 candidates):
  Mispricing reason: _______________
  Key catalyst:      _______________
  Primary risk:      _______________
  Conviction:        [High / Medium / Low]
```

---

## D.13 Execution Sequence

The framework is applied in the following order:

1. **Define peer groups.** Assign each company to G1, G2, G3, or G4 based on its primary industry code, then classify by market cap tier (Large/Mid/Small).

2. **Collect data.** Gather the 18 required fields for each company from public sources (Yahoo Finance, Nikkei, EDINET, company IR pages, JPX). Priority order: Wave 3 Japanese companies with zero data first, then Wave 1 gap-filling, then non-Japanese companies.

3. **Compute sector medians.** For each peer group, calculate the median PER, PBR, ROE, revenue growth, and operating margin from available data.

4. **Score Dimension A** (Valuation Ratios). For each company, compute PER_ratio, PBR_ratio, and earnings yield spread against peer medians. Apply the A1--A4 tier rubrics. Apply data gap adjustment if any sub-score is NULL.

5. **Score Dimension B** (Supply Chain Moat). Assess market share, switching costs, technology differentiation from company descriptions and industry research. Compute supply chain centrality from the graph. Sum B1--B4.

6. **Score Dimension C** (Growth & Earnings Quality). Pull revenue growth, compare operating margin and ROE against peer medians, assess AI/advanced-node exposure. Sum C1--C4.

7. **Score Dimension D** (Ownership & Float). Compute foreign ownership gap from B_score quality tier, assess float dynamics, compute price position in 52-week range. Sum D1--D3.

8. **Score Dimension E** (Catalysts & Sentiment). Evaluate analyst consensus, scan for capacity expansion announcements, assess policy tailwinds. Sum E1--E3.

9. **Score Dimension F** (Risk Adjustment). Assess forex sensitivity, customer concentration, geopolitical exposure. Sum F1--F3.

10. **Compute composite.** Sum A through F for raw composite. Apply confidence multiplier based on data coverage.

11. **Rank and identify top 10.** Sort all companies by final score descending. For each top-10 company, produce an investment thesis covering mispricing reason, key catalyst, primary risk, and conviction level.

12. **Sensitivity analysis.** Re-run the composite calculation under the five alternative weighting scenarios (value-heavy, moat-heavy, growth-heavy, equal-weight) to identify companies with robust, scenario-independent rankings.

---

## D.14 Limitations and Caveats

The framework is designed for systematic comparison across a specific universe of 74 semiconductor supply chain companies. Users should be aware of the following limitations:

**Point-in-time data.** All financial metrics reflect a specific observation date (February 2026 for the current dataset). Market prices, analyst estimates, and ownership percentages change continuously. Scores should be refreshed quarterly at minimum.

**Qualitative dimensions.** Dimensions B (Supply Chain Moat) and portions of C4 (AI exposure), E2 (capacity expansion), E3 (policy tailwinds), and F2/F3 (customer concentration, geopolitical risk) rely on structured qualitative assessment rather than purely formulaic calculation. While rubrics enforce consistency, different analysts applying the rubrics may arrive at modestly different scores for these sub-dimensions.

**Peer group size.** G3 (6 companies) and G4 (5 companies) are small peer groups. Medians computed from fewer than 10 observations are less stable. G4 in particular is a heterogeneous catch-all, and its median values (especially the 9.9 PBR driven by Apple and TSMC) may not represent a meaningful benchmark for all five member companies.

**Forward PER coverage.** At the time of scoring, forward PER (sub-dimension A2) had the lowest data coverage of any sub-dimension, requiring pro-rata adjustment for the majority of companies. This means Dimension A scores are effectively weighted more heavily toward trailing PER (A1) and PBR (A3) than the framework design intends.

**Currency conversion.** Non-Japanese companies' financials are converted to JPY at a point-in-time exchange rate. Movements in USD/JPY, KRW/JPY, or TWD/JPY between the conversion date and the scoring date introduce noise.

**No position sizing guidance.** The framework identifies relative undervaluation but does not prescribe position sizes, portfolio weights, or entry/exit timing. A score of 78.9 (Gun Ei Chemical, the dataset's highest-ranked company) indicates strong relative undervaluation but does not constitute investment advice.

---

*This appendix reproduces the evaluation methodology documented in `EVALUATION_FRAMEWORK.md` (version dated 2026-02-21) and the peer group medians from `evaluation_progress.json` (last updated 2026-02-22). All formulas, rubrics, and thresholds are presented exactly as implemented in the scoring system. For the scored results and investment theses derived from this framework, see Chapter 18.*

---

*Data sources: EVALUATION_FRAMEWORK.md, evaluation_progress.json, data/graph.json*
