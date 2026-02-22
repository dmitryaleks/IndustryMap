#!/usr/bin/env python3
"""
Sync researched financial metrics from evaluation_progress.json
back into individual company JSON files (data/companies/CMP-*.json).

Updates: PER, PBR, EPS, marketCapInYen, latestPriceYen,
         percentOfForeignOwnership, percentOfCirculatingEquity, isForexSensitive
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
EVAL_FILE = os.path.join(BASE, "evaluation_progress.json")
COMPANIES_DIR = os.path.join(BASE, "data", "companies")

def main():
    with open(EVAL_FILE, "r", encoding="utf-8") as f:
        evaluation = json.load(f)

    companies_eval = {c["id"]: c for c in evaluation["companies"]}

    updated = 0
    skipped = 0

    for cid, ev in sorted(companies_eval.items()):
        cfile = os.path.join(COMPANIES_DIR, f"{cid}.json")
        if not os.path.exists(cfile):
            print(f"  SKIP {cid} — no company file")
            skipped += 1
            continue

        with open(cfile, "r", encoding="utf-8") as f:
            company = json.load(f)

        rd = ev.get("researchData", {})
        if not rd:
            skipped += 1
            continue

        changed = False

        # PER
        if rd.get("PER") is not None:
            if company.get("PER") != rd["PER"]:
                company["PER"] = rd["PER"]
                changed = True

        # PBR
        if rd.get("PBR") is not None:
            if company.get("PBR") != rd["PBR"]:
                company["PBR"] = rd["PBR"]
                changed = True

        # EPS
        if rd.get("EPS") is not None:
            if company.get("EPS") != rd["EPS"]:
                company["EPS"] = rd["EPS"]
                changed = True

        # Market cap in Yen
        if rd.get("marketCapInYen") is not None:
            if company.get("marketCapInYen") != rd["marketCapInYen"]:
                company["marketCapInYen"] = rd["marketCapInYen"]
                changed = True

        # Latest price in Yen
        if rd.get("latestPriceYen") is not None:
            if company.get("latestPriceYen") != rd["latestPriceYen"]:
                company["latestPriceYen"] = rd["latestPriceYen"]
                changed = True

        # Foreign ownership
        if rd.get("foreignOwnership_pct") is not None:
            if company.get("percentOfForeignOwnership") != rd["foreignOwnership_pct"]:
                company["percentOfForeignOwnership"] = rd["foreignOwnership_pct"]
                changed = True

        # Circulating equity
        if rd.get("circulatingEquity_pct") is not None:
            if company.get("percentOfCirculatingEquity") != rd["circulatingEquity_pct"]:
                company["percentOfCirculatingEquity"] = rd["circulatingEquity_pct"]
                changed = True

        # Forex sensitivity
        if rd.get("isForexSensitive") is not None:
            if company.get("isForexSensitive") != rd["isForexSensitive"]:
                company["isForexSensitive"] = rd["isForexSensitive"]
                changed = True

        if changed:
            with open(cfile, "w", encoding="utf-8") as f:
                json.dump(company, f, indent=2, ensure_ascii=False)
            updated += 1
            print(f"  UPDATED {cid} ({ev.get('name', '')})")
        else:
            skipped += 1

    print(f"\nDone: {updated} files updated, {skipped} unchanged/skipped")

if __name__ == "__main__":
    main()
