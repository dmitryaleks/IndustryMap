#!/usr/bin/env python3
"""
Merge new research data into evaluation_progress.json and re-run scoring.
Reads research_results_*.json files, merges into the progress file,
then re-runs the full evaluation pipeline.
"""
import json
import glob
import os
import statistics

BASE = os.path.dirname(os.path.abspath(__file__))
PROGRESS_FILE = os.path.join(BASE, "evaluation_progress.json")
RESEARCH_DIR = BASE  # research files live in project root

# Import scoring functions from run_evaluation
from run_evaluation import (
    compute_dimension_A, compute_dimension_C, compute_dimension_D,
    compute_dimension_E, compute_data_coverage, confidence_multiplier,
    compute_composite, compute_peer_medians, compute_graph_degrees,
    load_json, save_json, CRITICAL_NODES, NON_JAPANESE_IDS, DELISTED_IDS,
    GRAPH_FILE
)


def merge_research_data(progress, research_files):
    """Merge research results into progress companies."""
    # Build lookup by ticker
    ticker_to_company = {}
    for c in progress["companies"]:
        ticker_to_company[c["ticker"]] = c

    merged_count = 0
    fields_added = 0

    for filepath in research_files:
        print(f"  Loading {os.path.basename(filepath)}...")
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                research = json.load(f)
        except Exception as e:
            print(f"    ERROR loading {filepath}: {e}")
            continue

        if not isinstance(research, list):
            print(f"    WARNING: {filepath} is not a list, skipping")
            continue

        for item in research:
            ticker = item.get("ticker")
            if not ticker:
                continue

            company = ticker_to_company.get(ticker)
            if not company:
                print(f"    WARNING: ticker {ticker} not found in progress, skipping")
                continue

            rd = company["researchData"]

            # Map research fields to progress fields
            field_map = {
                "PER": "PER",
                "PBR": "PBR",
                "marketCapInYen": "marketCapInYen",
                "marketCapUSD": "marketCapUSD",
                "latestPriceYen": "latestPriceYen",
                "latestPriceLocal": "latestPriceLocal",
                "localCurrency": "localCurrency",
                "weekHigh52": "weekHigh52",
                "weekLow52": "weekLow52",
                "revenueGrowthYoY_pct": "revenueGrowthYoY_pct",
                "operatingMargin_pct": "operatingMargin_pct",
                "foreignOwnership_pct": "foreignOwnership_pct",
                "hasBuyback": "hasBuyback",
                "circulatingEquity_pct": "circulatingEquity_pct",
                "EPS": "EPS",
                "forwardPER": "forwardPER",
                "dividendYield_pct": "dividendYield_pct",
            }

            company_updated = False
            for src_key, dst_key in field_map.items():
                new_val = item.get(src_key)
                if new_val is not None:
                    old_val = rd.get(dst_key)
                    if old_val is None:
                        rd[dst_key] = new_val
                        fields_added += 1
                        company_updated = True
                    elif old_val != new_val:
                        # Update with newer data
                        rd[dst_key] = new_val
                        company_updated = True

            # Handle market cap conversion for non-JPY companies
            if item.get("marketCapUSD") and not rd.get("marketCapInYen"):
                usd_jpy = progress.get("usdJpyRate", 152)
                rd["marketCapInYen"] = int(item["marketCapUSD"] * usd_jpy)
                fields_added += 1
                company_updated = True

            if item.get("marketCapLocal") and item.get("localCurrency"):
                currency = item["localCurrency"]
                mcap_local = item["marketCapLocal"]
                fx_rates = {"CNY": 21.0, "HKD": 19.5, "TWD": 4.7, "KRW": 0.11, "USD": 152, "EUR": 165}
                rate = fx_rates.get(currency)
                if rate and not rd.get("marketCapInYen"):
                    rd["marketCapInYen"] = int(mcap_local * rate)
                    fields_added += 1
                    company_updated = True

            if company_updated:
                merged_count += 1

    print(f"  Merged data for {merged_count} companies, {fields_added} new field values added")
    return progress


def rescore_all(progress):
    """Re-run scoring for all companies using updated data."""
    companies = progress["companies"]
    jgb_yield = progress.get("jgb10yYield_pct", 1.5)

    # Load graph
    graph = load_json(GRAPH_FILE)
    degrees = compute_graph_degrees(graph)

    # Recompute peer medians with new data
    peer_medians = compute_peer_medians(companies)
    print("\n  Updated Peer Group Medians:")
    for pg, meds in peer_medians.items():
        print(f"    {pg}: PER={meds['PER']}, PBR={meds['PBR']}, OPM={meds['OPM_pct']}, "
              f"RevGrowth={meds['revenueGrowth_pct']}, ROE={meds['ROE_pct']}")

    # Update medians in progress
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
                "note": "Recomputed after research sweep"
            })

    scoring_complete = 0
    research_complete = 0

    for c in companies:
        cid = c["id"]
        rd = c["researchData"]
        pg = c.get("peerGroup", "G4")
        pm = peer_medians.get(pg, {})
        existing_scores = c["scores"]

        # Dimension A
        a_scores = compute_dimension_A(rd, pm, jgb_yield)
        c["scores"]["A"] = a_scores

        # Dimension B (keep existing, verify B4)
        b_existing = existing_scores.get("B", {})
        b4_graph = 5 if cid in CRITICAL_NODES else (
            4 if degrees.get(cid, 0) >= 10 else
            3 if degrees.get(cid, 0) >= 6 else
            2 if degrees.get(cid, 0) >= 3 else 1
        )
        if b_existing.get("B4_chainCentrality") != b4_graph:
            b_existing["B4_chainCentrality"] = b4_graph
            b1 = b_existing.get("B1_marketShare", 0) or 0
            b2 = b_existing.get("B2_switchingCosts", 0) or 0
            b3 = b_existing.get("B3_techDiff", 0) or 0
            b_existing["total"] = b1 + b2 + b3 + b4_graph
        c["scores"]["B"] = b_existing

        # Dimension C
        existing_c4 = existing_scores.get("C", {}).get("C4_AIexposure")
        c_scores = compute_dimension_C(rd, existing_c4, pm)
        c["scores"]["C"] = c_scores

        # Dimension D
        b_total = c["scores"]["B"].get("total")
        d_scores = compute_dimension_D(rd, b_total, cid)
        c["scores"]["D"] = d_scores

        # Dimension E
        existing_e2 = existing_scores.get("E", {}).get("E2_capacityExpansion")
        existing_e3 = existing_scores.get("E", {}).get("E3_policyTailwinds")
        e_scores = compute_dimension_E(rd, existing_e2, existing_e3)
        c["scores"]["E"] = e_scores

        # Dimension F (keep existing)

        # Composite
        raw = compute_composite(c["scores"])
        c["rawComposite"] = raw

        coverage = compute_data_coverage(rd, c["scores"])
        c["dataCoverage_pct"] = coverage

        mult, conf = confidence_multiplier(coverage)
        c["confidenceMultiplier"] = mult
        c["confidence"] = conf

        c["finalScore"] = round(raw * mult, 1) if raw is not None else None

        # Status updates
        all_dims = all(c["scores"].get(d, {}).get("total") is not None for d in ["A", "B", "C", "D", "E", "F"])
        some_dims = any(c["scores"].get(d, {}).get("total") is not None for d in ["A", "B", "C", "D", "E", "F"])

        if all_dims:
            c["scoringStatus"] = "complete"
            scoring_complete += 1
        elif some_dims:
            c["scoringStatus"] = "partial"
        else:
            c["scoringStatus"] = "pending"

        research_fields = [
            "PER", "forwardPER", "PBR", "EPS", "ROE",
            "marketCapInYen", "latestPriceYen",
            "weekHigh52", "weekLow52",
            "revenueLatestFY_JPY_B", "revenueGrowthYoY_pct", "operatingMargin_pct",
            "foreignOwnership_pct", "circulatingEquity_pct", "isForexSensitive"
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

    # Update status
    progress["status"]["totalCompanies"] = len(companies)
    progress["status"]["researchComplete"] = research_complete
    progress["status"]["scoringComplete"] = scoring_complete

    dims_fully = []
    dims_partial = []
    for dim in ["A", "B", "C", "D", "E", "F"]:
        scored = sum(1 for c in companies if c["scores"].get(dim, {}).get("total") is not None)
        if scored == len(companies):
            dims_fully.append(dim)
        elif scored > 0:
            dims_partial.append(dim)
    progress["status"]["dimensionsFullyScored"] = dims_fully
    progress["status"]["dimensionsPartiallyScored"] = dims_partial
    progress["status"]["compositeRanked"] = True
    progress["lastUpdated"] = "2026-02-21"

    return progress, scoring_complete, research_complete


def print_rankings(progress):
    """Print final rankings."""
    companies = progress["companies"]
    scored = [c for c in companies if c.get("finalScore") is not None]
    scored.sort(key=lambda x: x["finalScore"], reverse=True)

    print(f"\n{'='*100}")
    print(f"FINAL RANKINGS — TOP 25 MOST UNDERVALUED")
    print(f"{'='*100}")
    print(f"{'Rank':<5} {'ID':<10} {'Name':<32} {'PG':<4} {'Raw':>6} {'Conf':<9} {'Mult':>5} {'Final':>7} {'Cover':>7}")
    print("-" * 95)
    for i, c in enumerate(scored[:25], 1):
        print(f"{i:<5} {c['id']:<10} {c['name'][:31]:<32} {c.get('peerGroup','?'):<4} "
              f"{c['rawComposite']:>6.1f} {c['confidence']:<9} "
              f"{c['confidenceMultiplier']:>5.2f} {c['finalScore']:>7.1f} "
              f"{c['dataCoverage_pct']:>6.1f}%")

    print(f"\n{'='*100}")
    print(f"DETAILED BREAKDOWN — TOP 15")
    print(f"{'='*100}")
    for i, c in enumerate(scored[:15], 1):
        s = c["scores"]
        a = s.get("A", {}).get("total")
        b = s.get("B", {}).get("total")
        cc = s.get("C", {}).get("total")
        d = s.get("D", {}).get("total")
        e = s.get("E", {}).get("total")
        f = s.get("F", {}).get("total")
        a_str = f"{a:5.1f}" if a is not None else " NULL"
        b_str = f"{b:5.1f}" if b is not None else " NULL"
        c_str = f"{cc:5.1f}" if cc is not None else " NULL"
        d_str = f"{d:5.1f}" if d is not None else " NULL"
        e_str = f"{e:5.1f}" if e is not None else " NULL"
        f_str = f"{f:5.1f}" if f is not None else " NULL"
        print(f"\n#{i} {c['name']} ({c['ticker']}) — Final: {c['finalScore']:.1f} [{c['confidence']}]")
        print(f"   A(Val)={a_str}/30  B(Moat)={b_str}/25  C(Growth)={c_str}/15  "
              f"D(Own)={d_str}/10  E(Cat)={e_str}/10  F(Risk)={f_str}/10")
        # Show key research data
        rd = c["researchData"]
        per = rd.get("PER")
        pbr = rd.get("PBR")
        fo = rd.get("foreignOwnership_pct")
        rg = rd.get("revenueGrowthYoY_pct")
        opm = rd.get("operatingMargin_pct")
        mcap = rd.get("marketCapInYen")
        parts = []
        if per: parts.append(f"PER={per}")
        if pbr: parts.append(f"PBR={pbr}")
        if fo: parts.append(f"FO={fo}%")
        if rg: parts.append(f"RevG={rg}%")
        if opm: parts.append(f"OPM={opm}%")
        if mcap: parts.append(f"MCap={mcap/1e12:.1f}T JPY")
        print(f"   Data: {', '.join(parts) if parts else 'Minimal data'}")

    # Confidence distribution
    conf_dist = {}
    for c in scored:
        conf = c.get("confidence", "Unknown")
        conf_dist[conf] = conf_dist.get(conf, 0) + 1
    print(f"\nConfidence Distribution: {conf_dist}")


def main():
    print("=" * 60)
    print("RESEARCH MERGE & RE-SCORING PIPELINE")
    print("=" * 60)

    # Load progress
    print("\n[1] Loading evaluation_progress.json...")
    progress = load_json(PROGRESS_FILE)
    print(f"    {len(progress['companies'])} companies loaded")

    # Find research result files
    print("\n[2] Finding research result files...")
    research_files = sorted(glob.glob(os.path.join(RESEARCH_DIR, "research_results_*.json")))
    if not research_files:
        print("    No research_results_*.json files found!")
        print("    Please create research files first.")
        return
    print(f"    Found {len(research_files)} research files: {[os.path.basename(f) for f in research_files]}")

    # Merge research data
    print("\n[3] Merging research data...")
    progress = merge_research_data(progress, research_files)

    # Re-score
    print("\n[4] Re-scoring all companies...")
    progress, scoring_complete, research_complete = rescore_all(progress)
    print(f"    Scoring complete for {scoring_complete} companies")
    print(f"    Research complete for {research_complete} companies")

    # Print rankings
    print_rankings(progress)

    # Save
    print(f"\n[5] Saving updated evaluation_progress.json...")
    save_json(PROGRESS_FILE, progress)
    print("    Done!")


if __name__ == "__main__":
    main()
