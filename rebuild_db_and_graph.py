#!/usr/bin/env python3
"""
Rebuild database.json and graph.json to reflect all company JSON files
under data/companies/ as the authoritative source of truth.
"""
import json
import glob
import os
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))
COMPANIES_DIR = os.path.join(BASE, "data", "companies")
DATABASE_FILE = os.path.join(BASE, "data", "database.json")
GRAPH_FILE = os.path.join(BASE, "data", "graph.json")

# Country inference from ticker suffix / known companies
def infer_country(company):
    ticker = company.get("ticker") or ""
    name = company.get("companyName", "")
    cid = company.get("id", "")

    if ticker.endswith(".T"):
        return "Japan"
    if ticker.endswith(".TW"):
        return "Taiwan"
    if ticker.endswith(".KS") or ticker.endswith(".KQ"):
        return "South Korea"
    if ticker.endswith(".HK"):
        return "Hong Kong"
    if ticker.endswith(".SS") or ticker.endswith(".SZ"):
        return "China"
    if ticker in ("NVDA", "INTC", "MU", "WDC", "AAPL", "AMKR"):
        return "USA"
    if ticker == "ASML":
        return "Netherlands"
    # Unlisted Chinese companies by name patterns
    china_keywords = [
        "Beijing", "Shanghai", "Shenzhen", "Hangzhou", "Yangtze", "Nexchip",
        "GigaDevice", "Hwatsing", "Huahai", "Shenyang", "NAURA", "CanSemi",
        "GTA Semiconductor", "China Resources", "Tongfu", "Huatian",
        "SMIC", "Hua Hong", "JCET", "Sidea", "Guangli",
    ]
    for kw in china_keywords:
        if kw.lower() in name.lower():
            return "China"
    # Unlisted Korean companies by known IDs
    if cid in ("CMP-0086_old", "CMP-0087_old"):  # placeholder
        return "South Korea"
    return "Unknown"


def load_all_companies():
    """Load all company JSON files sorted by ID."""
    files = sorted(glob.glob(os.path.join(COMPANIES_DIR, "CMP-*.json")))
    companies = []
    for filepath in files:
        with open(filepath, "r", encoding="utf-8") as f:
            c = json.load(f)
        companies.append(c)
    return companies


def assign_wave(cid):
    """Assign wave number based on company ID range."""
    num = int(cid.split("-")[1])
    if 1 <= num <= 16:
        return 1
    elif 17 <= num <= 28:
        return 2
    elif 29 <= num <= 62:
        return 3
    elif 63 <= num <= 74:
        return 4
    elif num in range(75, 83) or num == 100:
        return 5   # Korean ecosystem
    elif 83 <= num <= 95:
        return 6   # Chinese ecosystem
    else:
        return 6


def rebuild_database(companies):
    """Rebuild database.json from all company files."""
    print("[database.json] Rebuilding...")

    # Build company index
    index = []
    for c in companies:
        index.append({
            "id": c["id"],
            "name": c["companyName"],
            "ticker": c.get("ticker"),
            "wave": assign_wave(c["id"]),
        })

    # Industry breakdown
    industry_counter = Counter(c.get("industryCode", "Unknown") for c in companies)
    industry_breakdown = dict(sorted(industry_counter.items(), key=lambda x: -x[1]))

    # Geography breakdown
    geo_counter = Counter(infer_country(c) for c in companies)
    geo_breakdown = dict(sorted(geo_counter.items(), key=lambda x: -x[1]))

    # Wave breakdown
    wave_companies = {}
    for c in companies:
        w = assign_wave(c["id"])
        wave_companies.setdefault(w, []).append(c["id"])

    waves = {
        "wave1": {
            "count": len(wave_companies.get(1, [])),
            "status": "complete",
            "description": "Japanese seed companies",
        },
        "wave2": {
            "count": len(wave_companies.get(2, [])),
            "status": "complete",
            "description": "Global customers/suppliers",
        },
        "wave3": {
            "count": len(wave_companies.get(3, [])),
            "status": "complete",
            "description": "Japanese vendors/suppliers to existing companies",
        },
        "wave4": {
            "count": len(wave_companies.get(4, [])),
            "status": "complete",
            "description": "Tokyo Seimitsu deep dive - clients (OSAT/foundry) and competitors from JP/CN/KR/TW sources",
        },
        "wave5": {
            "count": len(wave_companies.get(5, [])),
            "status": "complete",
            "description": "Korean semiconductor ecosystem - OSAT clients, equipment competitors, and ecosystem players linked to Tokyo Seimitsu/Accretech",
        },
        "wave6": {
            "count": len(wave_companies.get(6, [])),
            "status": "complete",
            "description": "Chinese semiconductor ecosystem - foundries, equipment makers, and memory/IC companies linked to existing supply chain nodes",
        },
    }

    # Load existing to preserve keyRelationships and notes
    with open(DATABASE_FILE, "r", encoding="utf-8") as f:
        existing = json.load(f)

    db = {
        "$schema": existing.get("$schema", "../schema/company.schema.json"),
        "version": "3.0.0",
        "lastUpdated": "2026-02-21T23:00:00Z",
        "totalCompanies": len(companies),
        "waves": waves,
        "industryBreakdown": industry_breakdown,
        "geographyBreakdown": geo_breakdown,
        "companyIndex": index,
        "keyRelationships": existing.get("keyRelationships", {}),
        "notes": (
            existing.get("notes", "") +
            " Wave 6: Chinese semiconductor ecosystem deep dive. Added 13 Chinese companies: "
            "foundries (Nexchip, China Resources Micro, CanSemi, GTA Semi), memory (YMTC), "
            "IC design (GigaDevice), and equipment makers (NAURA, Hwatsing, Hangzhou Changchuan, "
            "Hwatsing Huahai, Shenyang Heyan, Beijing Shuoke, Beijing TSD). "
            f"Total {len(companies)} companies across 7 regions."
        ),
    }

    with open(DATABASE_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    print(f"  Written {len(index)} companies to database.json")
    print(f"  Industry breakdown: {industry_breakdown}")
    print(f"  Geography breakdown: {geo_breakdown}")
    print(f"  Waves: { {k: v['count'] for k, v in waves.items()} }")
    return db


def rebuild_graph(companies):
    """Rebuild graph.json nodes and edges from all company files."""
    print("\n[graph.json] Rebuilding...")

    # Load existing graph to preserve existing edges and metadata
    with open(GRAPH_FILE, "r", encoding="utf-8") as f:
        existing = json.load(f)

    existing_node_ids = {n["id"] for n in existing["nodes"]}
    existing_edges = existing["edges"]

    # Build set of existing edges for deduplication
    existing_edge_keys = set()
    for e in existing_edges:
        existing_edge_keys.add((e["source"], e["target"], e.get("type", "supplier")))

    # Build company lookup
    company_map = {c["id"]: c for c in companies}

    # Build full node list
    all_nodes = list(existing["nodes"])  # preserve existing
    new_nodes_added = 0

    for c in companies:
        cid = c["id"]
        if cid in existing_node_ids:
            continue  # already exists
        country = infer_country(c)
        node = {
            "id": cid,
            "name": c["companyName"],
            "industry": c.get("industryCode", "Unknown"),
            "country": country,
            "ticker": c.get("ticker"),
            "marketCap": c.get("marketCapInYen"),
        }
        all_nodes.append(node)
        new_nodes_added += 1

    # Sort nodes by ID
    all_nodes.sort(key=lambda n: int(n["id"].split("-")[1]))

    # Build full edge list - start from existing, add new edges from new companies
    all_edges = list(existing_edges)
    new_edges_added = 0

    for c in companies:
        cid = c["id"]

        # supplier -> company edges
        for sup_id in c.get("suppliers", []):
            if sup_id not in company_map:
                continue
            key = (sup_id, cid, "supplier")
            if key not in existing_edge_keys:
                all_edges.append({"source": sup_id, "target": cid, "type": "supplier"})
                existing_edge_keys.add(key)
                new_edges_added += 1

        # company -> client edges
        for cli_id in c.get("clients", []):
            if cli_id not in company_map:
                continue
            key = (cid, cli_id, "supplier")
            if key not in existing_edge_keys:
                all_edges.append({"source": cid, "target": cli_id, "type": "supplier"})
                existing_edge_keys.add(key)
                new_edges_added += 1

    # Count edge types
    edge_type_counts = Counter(e.get("type", "supplier") for e in all_edges)

    # Country set for description
    countries = sorted({infer_country(c) for c in companies} - {"Unknown"})

    graph = {
        "version": "4.0.0",
        "generatedAt": "2026-02-21T23:00:00Z",
        "description": (
            f"Semiconductor supply chain graph - {len(all_nodes)} companies, "
            f"{len(countries)} regions "
            f"(Wave 6: Chinese ecosystem - foundries, equipment, memory/IC)"
        ),
        "statistics": {
            "totalNodes": len(all_nodes),
            "totalEdges": len(all_edges),
            "edgeTypes": dict(edge_type_counts),
        },
        "nodes": all_nodes,
        "edges": all_edges,
    }

    with open(GRAPH_FILE, "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)

    print(f"  Nodes: {len(existing['nodes'])} -> {len(all_nodes)} (+{new_nodes_added} new)")
    print(f"  Edges: {len(existing_edges)} -> {len(all_edges)} (+{new_edges_added} new)")
    print(f"  Edge types: {dict(edge_type_counts)}")
    return graph


def main():
    print("=" * 60)
    print("REBUILD database.json AND graph.json FROM COMPANY FILES")
    print("=" * 60)

    companies = load_all_companies()
    print(f"\nLoaded {len(companies)} company files from {COMPANIES_DIR}")

    rebuild_database(companies)
    rebuild_graph(companies)

    print("\nDone.")


if __name__ == "__main__":
    main()
