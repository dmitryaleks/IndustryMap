#!/usr/bin/env python3
"""
Evaluation scoring engine for semiconductor supply chain companies.
Reads evaluation_progress.json, applies EVALUATION_FRAMEWORK.md rubrics,
computes all scorable dimensions, composites, and rankings.
"""
import json
import statistics
import copy
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PROGRESS_FILE = os.path.join(BASE, "evaluation_progress.json")
GRAPH_FILE = os.path.join(BASE, "data", "graph.json")

# --- Constants from the framework ---
JGB_10Y_YIELD = 1.5  # percent, will be read from progress file

CRITICAL_NODES = {
    "CMP-0026",  # ASML
    "CMP-0006",  # Lasertec
    "CMP-0017",  # TSMC
    "CMP-0024",  # Shin-Etsu
    "CMP-0025",  # SUMCO
    "CMP-0004",  # Tokyo Electron
    "CMP-0044",  # Stella Chemifa
    "CMP-0048",  # Ibiden
    "CMP-0052",  # Organo
    "CMP-0005",  # Advantest
    "CMP-0028",  # NVIDIA
}

NON_JAPANESE_IDS = {
    "CMP-0017",  # TSMC
    "CMP-0018",  # Samsung
    "CMP-0019",  # Intel
    "CMP-0020",  # SK Hynix
    "CMP-0021",  # Micron
    "CMP-0022",  # Apple
    "CMP-0023",  # Western Digital
    "CMP-0026",  # ASML
    "CMP-0028",  # NVIDIA
    "CMP-0063",  # ASE Technology
    "CMP-0064",  # Amkor
    "CMP-0065",  # JCET
    "CMP-0066",  # SMIC
    "CMP-0067",  # Tongfu
    "CMP-0068",  # Tianshui Huatian
    "CMP-0069",  # Powertech
    "CMP-0070",  # Hua Hong
    "CMP-0071",  # MPI Corporation
    "CMP-0072",  # Hanmi Semiconductor
    "CMP-0073",  # Sidea
    "CMP-0074",  # Guangli
}

DELISTED_IDS = {"CMP-0034"}  # JSR


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def compute_graph_degrees(graph):
    """Compute degree (supplier+client edges) for each node from graph.json."""
    degrees = {}
    for node in graph.get("nodes", []):
        degrees[node["id"]] = 0
    for edge in graph.get("edges", []):
        if edge.get("type") == "supplier":
            src = edge["source"]
            tgt = edge["target"]
            degrees[src] = degrees.get(src, 0) + 1
            degrees[tgt] = degrees.get(tgt, 0) + 1
    return degrees


def compute_peer_medians(companies):
    """Compute peer group medians for each peer group from available data."""
    groups = {}
    for c in companies:
        pg = c.get("peerGroup", "G4")
        if pg not in groups:
            groups[pg] = []
        groups[pg].append(c)

    medians = {}
    for pg, members in groups.items():
        rd_list = [m["researchData"] for m in members]

        def safe_median(field):
            vals = [rd[field] for rd in rd_list if rd.get(field) is not None and rd[field] > 0]
            return statistics.median(vals) if len(vals) >= 2 else (vals[0] if len(vals) == 1 else None)

        medians[pg] = {
            "PER": safe_median("PER"),
            "PBR": safe_median("PBR"),
            "ROE_pct": None,  # derived below
            "revenueGrowth_pct": safe_median("revenueGrowthYoY_pct"),
            "OPM_pct": safe_median("operatingMargin_pct"),
            "foreignOwnership_pct": None,
        }

        # ROE: derive from PBR/PER where both exist
        roes = []
        for rd in rd_list:
            per = rd.get("PER")
            pbr = rd.get("PBR")
            if per and pbr and per > 0:
                roes.append((pbr / per) * 100)
        medians[pg]["ROE_pct"] = statistics.median(roes) if len(roes) >= 2 else (roes[0] if len(roes) == 1 else None)

        # Foreign ownership: only for Japanese companies
        fo_vals = []
        for m in members:
            if m["id"] not in NON_JAPANESE_IDS:
                fo = m["researchData"].get("foreignOwnership_pct")
                if fo is not None:
                    fo_vals.append(fo)
        medians[pg]["foreignOwnership_pct"] = statistics.median(fo_vals) if fo_vals else None

    return medians


# ===================== DIMENSION SCORING FUNCTIONS =====================

def score_A1(per, peer_median_per):
    """PER Discount Score (0-12)"""
    if per is None or peer_median_per is None:
        return None
    if per < 0 or per > 100:
        return 0
    ratio = per / peer_median_per
    if ratio <= 0.50:
        return 12
    elif ratio <= 0.70:
        return 10
    elif ratio <= 0.85:
        return 8
    elif ratio <= 1.00:
        return 6
    elif ratio <= 1.15:
        return 4
    elif ratio <= 1.30:
        return 2
    else:
        return 0


def score_A2(fwd_per, peer_median_fwd_per):
    """Forward PER Discount Score (0-6)"""
    if fwd_per is None or peer_median_fwd_per is None:
        return None
    if fwd_per < 0 or fwd_per > 100:
        return 0
    ratio = fwd_per / peer_median_fwd_per
    if ratio <= 0.50:
        return 6
    elif ratio <= 0.70:
        return 5
    elif ratio <= 0.85:
        return 4
    elif ratio <= 1.00:
        return 3
    elif ratio <= 1.15:
        return 2
    elif ratio <= 1.30:
        return 1
    else:
        return 0


def score_A3(pbr, peer_median_pbr):
    """PBR Discount Score (0-8)"""
    if pbr is None or peer_median_pbr is None:
        return None
    if pbr <= 0:
        return None
    ratio = pbr / peer_median_pbr
    if ratio <= 0.50:
        score = 8
    elif ratio <= 0.70:
        score = 6
    elif ratio <= 0.85:
        score = 5
    elif ratio <= 1.00:
        score = 4
    elif ratio <= 1.20:
        score = 2
    else:
        score = 0
    # Bonus for PBR < 1.0 absolute
    if pbr < 1.0:
        score = min(score + 1, 8)
    return score


def score_A4(per, jgb_yield_pct):
    """Earnings Yield Spread (0-4)"""
    if per is None or per <= 0:
        return None
    earnings_yield_pct = (1.0 / per) * 100
    spread = earnings_yield_pct - jgb_yield_pct
    if spread >= 6:
        return 4
    elif spread >= 4:
        return 3
    elif spread >= 2:
        return 2
    elif spread >= 0:
        return 1
    else:
        return 0


def compute_dimension_A(rd, peer_med, jgb_yield):
    """Compute dimension A total with pro-rata rescaling."""
    a1 = score_A1(rd.get("PER"), peer_med.get("PER"))
    a2 = score_A2(rd.get("forwardPER"), peer_med.get("PER"))  # use PER median as proxy if no fwd median
    a3 = score_A3(rd.get("PBR"), peer_med.get("PBR"))
    a4 = score_A4(rd.get("PER"), jgb_yield)

    sub_scores = {"A1_PER_discount": a1, "A2_fwdPER_discount": a2, "A3_PBR_discount": a3, "A4_earningsYield": a4}
    max_map = {"A1_PER_discount": 12, "A2_fwdPER_discount": 6, "A3_PBR_discount": 8, "A4_earningsYield": 4}

    available_sum = 0
    available_max = 0
    for key, val in sub_scores.items():
        if val is not None:
            available_sum += val
            available_max += max_map[key]

    if available_max > 0:
        total = round((available_sum / available_max) * 30, 1)
    else:
        total = None

    notes = []
    if a1 is not None:
        notes.append(f"PER ratio vs peer")
    if a2 is not None:
        notes.append(f"Fwd PER scored")
    if a3 is not None:
        notes.append(f"PBR scored")
    if a4 is not None:
        notes.append(f"EY spread scored")
    if not notes:
        note = "No valuation data available — all sub-scores NULL"
    else:
        null_count = sum(1 for v in sub_scores.values() if v is None)
        note = f"Scored {4 - null_count}/4 sub-dimensions; pro-rata rescaled to 30"

    sub_scores["total"] = total
    sub_scores["note"] = note
    return sub_scores


def score_C1(rev_growth):
    """Revenue Growth Score (0-5)"""
    if rev_growth is None:
        return None
    if rev_growth >= 30:
        return 5
    elif rev_growth >= 20:
        return 4
    elif rev_growth >= 10:
        return 3
    elif rev_growth >= 0:
        return 2
    elif rev_growth >= -10:
        return 1
    else:
        return 0


def score_C2(opm, peer_median_opm):
    """Operating Margin Score (0-4)"""
    if opm is None or peer_median_opm is None or peer_median_opm == 0:
        return None
    ratio = opm / peer_median_opm
    if ratio >= 1.50:
        return 4
    elif ratio >= 1.20:
        return 3
    elif ratio >= 0.90:
        return 2
    elif ratio >= 0.60:
        return 1
    else:
        return 0


def score_C3(per, pbr, peer_median_roe):
    """ROE Quality Score (0-3). ROE = PBR/PER * 100."""
    if per is None or pbr is None or per <= 0:
        return None
    roe = (pbr / per) * 100
    if roe >= 20 and (peer_median_roe is None or roe >= peer_median_roe):
        return 3
    elif roe >= 12:
        return 2
    elif roe >= 5:
        return 1
    else:
        return 0


def compute_dimension_C(rd, existing_c4, peer_med):
    """Compute dimension C with existing C4 preserved and new C1-C3 where data exists."""
    c1 = score_C1(rd.get("revenueGrowthYoY_pct"))
    c2 = score_C2(rd.get("operatingMargin_pct"), peer_med.get("OPM_pct"))
    c3 = score_C3(rd.get("PER"), rd.get("PBR"), peer_med.get("ROE_pct"))
    c4 = existing_c4  # preserve existing AI/advanced-node exposure score

    sub_scores = {"C1_revenueGrowth": c1, "C2_operatingMargin": c2, "C3_ROE": c3, "C4_AIexposure": c4}
    max_map = {"C1_revenueGrowth": 5, "C2_operatingMargin": 4, "C3_ROE": 3, "C4_AIexposure": 3}

    available_sum = 0
    available_max = 0
    for key, val in sub_scores.items():
        if val is not None:
            available_sum += val
            available_max += max_map[key]

    if available_max > 0:
        total = round((available_sum / available_max) * 15, 1)
    else:
        total = None

    null_count = sum(1 for v in sub_scores.values() if v is None)
    if null_count == 0:
        note = "All sub-dimensions scored"
    elif null_count == 4:
        note = "No data available"
    else:
        note = f"Scored {4 - null_count}/4 sub-dimensions; pro-rata rescaled to 15"

    sub_scores["total"] = total
    sub_scores["note"] = note
    return sub_scores


def score_D1(b_score, foreign_ownership_pct, is_non_japanese):
    """Foreign Ownership Gap (0-5)"""
    if is_non_japanese:
        # For non-Japanese, use placeholder score of 2 (neutral) since we lack institutional ownership change data
        return 2

    if foreign_ownership_pct is None or b_score is None:
        return None

    # Determine quality tier from B score
    if b_score >= 18:
        expected_mid = 45  # High quality: 40-50%
    elif b_score >= 12:
        expected_mid = 30  # Medium quality: 25-35%
    else:
        expected_mid = 15  # Low quality: 10-20%

    gap = expected_mid - foreign_ownership_pct
    if gap >= 20:
        return 5
    elif gap >= 15:
        return 4
    elif gap >= 10:
        return 3
    elif gap >= 5:
        return 2
    elif gap >= 0:
        return 1
    else:
        return 0


def score_D2(circulating_equity_pct, has_buyback):
    """Circulating Equity Dynamics (0-3)"""
    if circulating_equity_pct is None and has_buyback is None:
        return None
    buyback = has_buyback if has_buyback is not None else False
    float_pct = circulating_equity_pct if circulating_equity_pct is not None else 80  # assume 80% if unknown

    if buyback and float_pct < 70:
        return 3
    elif buyback or float_pct < 70:
        return 2
    elif float_pct <= 90:
        return 1
    else:
        return 0


def score_D3(price, high52, low52):
    """Price vs 52-Week Range (0-2)"""
    if price is None or high52 is None or low52 is None:
        return None
    if high52 == low52:
        return 1
    position = (price - low52) / (high52 - low52)
    if position <= 0.25:
        return 2
    elif position <= 0.50:
        return 1
    else:
        return 0


def compute_dimension_D(rd, b_total, company_id):
    """Compute dimension D."""
    is_non_jp = company_id in NON_JAPANESE_IDS
    d1 = score_D1(b_total, rd.get("foreignOwnership_pct"), is_non_jp)
    d2 = score_D2(rd.get("circulatingEquity_pct"), rd.get("hasBuyback"))
    d3 = score_D3(rd.get("latestPriceYen"), rd.get("weekHigh52"), rd.get("weekLow52"))

    sub_scores = {"D1_foreignOwnershipGap": d1, "D2_floatDynamics": d2, "D3_priceVs52W": d3}
    max_map = {"D1_foreignOwnershipGap": 5, "D2_floatDynamics": 3, "D3_priceVs52W": 2}

    available_sum = 0
    available_max = 0
    for key, val in sub_scores.items():
        if val is not None:
            available_sum += val
            available_max += max_map[key]

    if available_max > 0:
        total = round((available_sum / available_max) * 10, 1)
    else:
        total = None

    null_count = sum(1 for v in sub_scores.values() if v is None)
    if null_count == 0:
        note = "All sub-dimensions scored"
    elif null_count == 3:
        note = "No ownership/float/price data available"
    else:
        note = f"Scored {3 - null_count}/3 sub-dimensions; pro-rata rescaled to 10"

    sub_scores["total"] = total
    sub_scores["note"] = note
    return sub_scores


def score_E1(analyst_buy, analyst_hold, analyst_sell, avg_target, current_price):
    """Analyst Consensus (0-4)"""
    if avg_target is not None and current_price is not None and current_price > 0:
        upside = (avg_target / current_price) - 1
        total_analysts = (analyst_buy or 0) + (analyst_hold or 0) + (analyst_sell or 0)
        majority_buy = (analyst_buy or 0) > total_analysts / 2 if total_analysts > 0 else False
        more_buy = (analyst_buy or 0) > (analyst_sell or 0)
        majority_sell = (analyst_sell or 0) > total_analysts / 2 if total_analysts > 0 else False

        if upside >= 0.30 and majority_buy:
            return 4
        elif upside >= 0.15 and more_buy:
            return 3
        elif upside >= 0:
            return 2
        elif majority_sell and upside < 0:
            return 0
        else:
            return 1
    elif analyst_buy is not None:
        # Partial data: just have analyst counts
        total = (analyst_buy or 0) + (analyst_hold or 0) + (analyst_sell or 0)
        if total > 0 and (analyst_buy or 0) > total * 0.6:
            return 3
        elif total > 0 and (analyst_buy or 0) > (analyst_sell or 0):
            return 2
        elif total > 0:
            return 1
        return None
    return None


def compute_dimension_E(rd, existing_e2, existing_e3):
    """Compute dimension E with existing E2/E3 preserved."""
    price = rd.get("latestPriceYen") or rd.get("latestPriceLocal")
    e1 = score_E1(
        rd.get("analystBuy"), rd.get("analystHold"), rd.get("analystSell"),
        rd.get("analystAvgTarget_local"), price
    )
    e2 = existing_e2
    e3 = existing_e3

    sub_scores = {"E1_analystConsensus": e1, "E2_capacityExpansion": e2, "E3_policyTailwinds": e3}
    max_map = {"E1_analystConsensus": 4, "E2_capacityExpansion": 3, "E3_policyTailwinds": 3}

    available_sum = 0
    available_max = 0
    for key, val in sub_scores.items():
        if val is not None:
            available_sum += val
            available_max += max_map[key]

    if available_max > 0:
        total = round((available_sum / available_max) * 10, 1)
    else:
        total = None

    null_count = sum(1 for v in sub_scores.values() if v is None)
    if null_count == 0:
        note = "All sub-dimensions scored"
    else:
        note = f"Scored {3 - null_count}/3 sub-dimensions; pro-rata rescaled to 10"

    sub_scores["total"] = total
    sub_scores["note"] = note
    return sub_scores


def compute_data_coverage(rd, scores):
    """Compute data coverage percentage for confidence modifier."""
    # Required fields for a complete evaluation
    required_fields = [
        "PER", "PBR", "marketCapInYen", "latestPriceYen",
        "revenueGrowthYoY_pct", "operatingMargin_pct",
        "foreignOwnership_pct", "circulatingEquity_pct",
        "weekHigh52", "weekLow52", "isForexSensitive",
        "chinaRevenue_pct_est", "topCustomerRev_pct_est",
    ]
    total_fields = len(required_fields)
    populated = sum(1 for f in required_fields if rd.get(f) is not None)

    # Also count scored dimensions
    scored_dims = sum(1 for dim in ["A", "B", "C", "D", "E", "F"]
                      if scores.get(dim, {}).get("total") is not None)
    # Weight: 60% data fields, 40% scored dimensions
    coverage = 0.6 * (populated / total_fields) + 0.4 * (scored_dims / 6)
    return round(coverage * 100, 1)


def confidence_multiplier(coverage_pct):
    """Apply confidence modifier based on data coverage."""
    if coverage_pct >= 80:
        return 1.0, "High"
    elif coverage_pct >= 60:
        return 0.95, "Medium"
    elif coverage_pct >= 40:
        return 0.85, "Low"
    else:
        return 0.70, "Very Low"


def compute_composite(scores):
    """Compute raw composite from dimension totals."""
    total = 0
    scored = 0
    max_total = 0
    dim_maxes = {"A": 30, "B": 25, "C": 15, "D": 10, "E": 10, "F": 10}
    for dim, max_pts in dim_maxes.items():
        dim_total = scores.get(dim, {}).get("total")
        if dim_total is not None:
            total += dim_total
            max_total += max_pts
            scored += 1

    if scored == 0:
        return None

    # If not all dimensions scored, rescale to 100
    if max_total > 0 and max_total < 100:
        raw = round((total / max_total) * 100, 1)
    else:
        raw = round(total, 1)

    return raw


def main():
    print("Loading evaluation_progress.json...")
    progress = load_json(PROGRESS_FILE)
    companies = progress["companies"]
    jgb_yield = progress.get("jgb10yYield_pct", JGB_10Y_YIELD)

    print(f"Loaded {len(companies)} companies")

    # Load graph for centrality verification
    print("Loading graph.json for centrality checks...")
    graph = load_json(GRAPH_FILE)
    degrees = compute_graph_degrees(graph)

    # Step 1: Compute peer group medians
    print("\n--- Step 1: Computing Peer Group Medians ---")
    peer_medians = compute_peer_medians(companies)
    for pg, meds in peer_medians.items():
        print(f"  {pg}: PER={meds['PER']}, PBR={meds['PBR']}, OPM={meds['OPM_pct']}, "
              f"RevGrowth={meds['revenueGrowth_pct']}, ROE={meds['ROE_pct']}")

    # Update peer medians in progress file
    pg_key_map = {"G1": "G1_Equipment", "G2": "G2_Materials", "G3": "G3_Semiconductors", "G4": "G4_Other"}
    for pg, meds in peer_medians.items():
        key = pg_key_map.get(pg, pg)
        if key in progress["peerGroupMedians"]:
            progress["peerGroupMedians"][key].update({
                "PER": meds["PER"],
                "PBR": meds["PBR"],
                "ROE_pct": meds["ROE_pct"],
                "revenueGrowth_pct": meds["revenueGrowth_pct"],
                "OPM_pct": meds["OPM_pct"],
                "note": "Computed from available data (sparse)"
            })

    # Step 2: Score each company
    print("\n--- Step 2: Scoring All Companies ---")
    scoring_complete = 0
    research_complete = 0

    for c in companies:
        cid = c["id"]
        name = c["name"]
        pg = c.get("peerGroup", "G4")
        rd = c["researchData"]
        existing_scores = c["scores"]

        pm = peer_medians.get(pg, {})

        # --- Dimension A: Valuation Ratios ---
        a_scores = compute_dimension_A(rd, pm, jgb_yield)
        c["scores"]["A"] = a_scores

        # --- Dimension B: Supply Chain Moat (already scored, verify B4 from graph) ---
        b_existing = existing_scores.get("B", {})
        b4_graph = 5 if cid in CRITICAL_NODES else (
            4 if degrees.get(cid, 0) >= 10 else
            3 if degrees.get(cid, 0) >= 6 else
            2 if degrees.get(cid, 0) >= 3 else 1
        )
        # Use existing B scores, but update B4 from graph if it changed
        if b_existing.get("B4_chainCentrality") != b4_graph:
            b_existing["B4_chainCentrality"] = b4_graph
            # Recompute B total
            b1 = b_existing.get("B1_marketShare", 0) or 0
            b2 = b_existing.get("B2_switchingCosts", 0) or 0
            b3 = b_existing.get("B3_techDiff", 0) or 0
            b_existing["total"] = b1 + b2 + b3 + b4_graph
            b_existing["note"] = "B4 updated from graph.json; others from prior scoring"
        c["scores"]["B"] = b_existing

        # --- Dimension C: Growth & Earnings Quality ---
        existing_c4 = existing_scores.get("C", {}).get("C4_AIexposure")
        c_scores = compute_dimension_C(rd, existing_c4, pm)
        c["scores"]["C"] = c_scores

        # --- Dimension D: Ownership & Float ---
        b_total = c["scores"]["B"].get("total")
        d_scores = compute_dimension_D(rd, b_total, cid)
        c["scores"]["D"] = d_scores

        # --- Dimension E: Catalysts & Sentiment ---
        existing_e2 = existing_scores.get("E", {}).get("E2_capacityExpansion")
        existing_e3 = existing_scores.get("E", {}).get("E3_policyTailwinds")
        e_scores = compute_dimension_E(rd, existing_e2, existing_e3)
        c["scores"]["E"] = e_scores

        # --- Dimension F: Risk Adjustment (already scored, keep as-is) ---
        # F is already fully scored, no changes needed

        # --- Composite Score ---
        raw = compute_composite(c["scores"])
        c["rawComposite"] = raw

        coverage = compute_data_coverage(rd, c["scores"])
        c["dataCoverage_pct"] = coverage

        mult, conf = confidence_multiplier(coverage)
        c["confidenceMultiplier"] = mult
        c["confidence"] = conf

        if raw is not None:
            c["finalScore"] = round(raw * mult, 1)
        else:
            c["finalScore"] = None

        # Update statuses
        all_dims_scored = all(
            c["scores"].get(d, {}).get("total") is not None
            for d in ["A", "B", "C", "D", "E", "F"]
        )
        some_dims_scored = any(
            c["scores"].get(d, {}).get("total") is not None
            for d in ["A", "B", "C", "D", "E", "F"]
        )

        if all_dims_scored:
            c["scoringStatus"] = "complete"
            scoring_complete += 1
        elif some_dims_scored:
            c["scoringStatus"] = "partial"
        else:
            c["scoringStatus"] = "pending"

        # Determine research completeness
        research_fields = [
            "PER", "forwardPER", "PBR", "EPS", "ROE",
            "marketCapInYen", "latestPriceYen",
            "weekHigh52", "weekLow52",
            "revenueLatestFY_JPY_B", "revenueGrowthYoY_pct", "operatingMargin_pct",
            "foreignOwnership_pct", "circulatingEquity_pct",
            "isForexSensitive"
        ]
        populated = sum(1 for f in research_fields if rd.get(f) is not None)
        c["researchCompleteness_pct"] = round(populated / len(research_fields) * 100, 1)
        if c["researchCompleteness_pct"] >= 80:
            c["researchStatus"] = "complete"
            research_complete += 1
        elif c["researchCompleteness_pct"] >= 30:
            c["researchStatus"] = "partial"
        else:
            c["researchStatus"] = "pending"

        # Special handling for delisted JSR
        if cid in DELISTED_IDS:
            c["scores"]["A"]["note"] = "Delisted (JIC acquisition). Dimension A = NULL."
            c["notes"] = "Delisted after JIC acquisition in 2024. Not actionable for public equity."

    # Step 3: Update overall status
    progress["status"]["totalCompanies"] = len(companies)
    progress["status"]["researchComplete"] = research_complete
    progress["status"]["scoringComplete"] = scoring_complete

    # Check which dimensions are fully scored
    dims_fully = []
    dims_partial = []
    dims_pending = []
    for dim in ["A", "B", "C", "D", "E", "F"]:
        scored_count = sum(1 for c in companies if c["scores"].get(dim, {}).get("total") is not None)
        if scored_count == len(companies):
            dims_fully.append(dim)
        elif scored_count > 0:
            dims_partial.append(dim)
        else:
            dims_pending.append(dim)

    progress["status"]["dimensionsFullyScored"] = dims_fully
    progress["status"]["dimensionsPartiallyScored"] = dims_partial
    progress["status"]["dimensionsPendingResearch"] = dims_pending

    # Compute composite ranked flag
    ranked = sum(1 for c in companies if c.get("finalScore") is not None)
    progress["status"]["compositeRanked"] = ranked > 0

    # Step 4: Print summary
    print(f"\n--- EVALUATION SUMMARY ---")
    print(f"Total companies: {len(companies)}")
    print(f"Research complete: {research_complete}")
    print(f"Scoring complete (all 6 dims): {scoring_complete}")
    print(f"Companies with final scores: {ranked}")
    print(f"Dimensions fully scored: {dims_fully}")
    print(f"Dimensions partially scored: {dims_partial}")

    # Step 5: Rank and print top companies
    scored_companies = [c for c in companies if c.get("finalScore") is not None]
    scored_companies.sort(key=lambda x: x["finalScore"], reverse=True)

    print(f"\n--- TOP 20 MOST UNDERVALUED (by Final Score) ---")
    print(f"{'Rank':<5} {'ID':<10} {'Name':<30} {'Raw':>6} {'Conf':<8} {'Mult':>5} {'Final':>7} {'Coverage':>8}")
    print("-" * 90)
    for i, c in enumerate(scored_companies[:20], 1):
        print(f"{i:<5} {c['id']:<10} {c['name']:<30} "
              f"{c['rawComposite']:>6.1f} {c['confidence']:<8} "
              f"{c['confidenceMultiplier']:>5.2f} {c['finalScore']:>7.1f} "
              f"{c['dataCoverage_pct']:>7.1f}%")

    # Step 6: Show scoring breakdown for top 10
    print(f"\n--- SCORING BREAKDOWN (Top 10) ---")
    for i, c in enumerate(scored_companies[:10], 1):
        scores = c["scores"]
        print(f"\n#{i} {c['name']} ({c['id']}, {c['ticker']})")
        print(f"  Peer Group: {c['peerGroup']} | Confidence: {c['confidence']} | Coverage: {c['dataCoverage_pct']}%")
        for dim in ["A", "B", "C", "D", "E", "F"]:
            dim_data = scores.get(dim, {})
            total = dim_data.get("total", "NULL")
            dim_names = {"A": "Valuation", "B": "Moat", "C": "Growth", "D": "Ownership", "E": "Catalysts", "F": "Risk"}
            dim_maxes = {"A": 30, "B": 25, "C": 15, "D": 10, "E": 10, "F": 10}
            print(f"  {dim}. {dim_names[dim]:<12}: {total if total is not None else 'NULL':>6} / {dim_maxes[dim]}")
        print(f"  Raw Composite: {c['rawComposite']:.1f} | Final: {c['finalScore']:.1f}")

    # Save updated progress
    progress["lastUpdated"] = "2026-02-21"
    save_json(PROGRESS_FILE, progress)
    print(f"\n--- Saved updated evaluation_progress.json ---")
    print(f"Done!")


if __name__ == "__main__":
    main()
