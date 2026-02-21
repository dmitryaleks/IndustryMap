#!/usr/bin/env python3
"""
Generate output/supply_chain.html from:
  - data/graph.json        (nodes + edges)
  - data/companies/*.json  (descriptions, wave assignments)
  - evaluation_progress.json (scores, PER, foreign ownership, thesis)
"""
import json
import glob
import os

BASE = os.path.dirname(os.path.abspath(__file__))
GRAPH_FILE   = os.path.join(BASE, "data", "graph.json")
DB_FILE      = os.path.join(BASE, "data", "database.json")
EVAL_FILE    = os.path.join(BASE, "evaluation_progress.json")
COMPANY_DIR  = os.path.join(BASE, "data", "companies")
OUT_FILE     = os.path.join(BASE, "output", "supply_chain.html")


# ─── Edge label overrides (curated from prior work) ──────────────────────────
EDGE_LABELS = {
    ("CMP-0024","CMP-0017"): "silicon wafers",
    ("CMP-0025","CMP-0017"): "silicon wafers",
    ("CMP-0004","CMP-0017"): "coater/developers, etch, CVD",
    ("CMP-0003","CMP-0017"): "wafer cleaning",
    ("CMP-0007","CMP-0017"): "CMP slurry",
    ("CMP-0013","CMP-0017"): "CMP slurry",
    ("CMP-0015","CMP-0017"): "photomask blanks",
    ("CMP-0017","CMP-0022"): "chip manufacturing",
    ("CMP-0017","CMP-0028"): "chip manufacturing",
    ("CMP-0024","CMP-0018"): "silicon wafers",
    ("CMP-0025","CMP-0018"): "silicon wafers",
    ("CMP-0004","CMP-0018"): "deposition equipment",
    ("CMP-0005","CMP-0018"): "test equipment",
    ("CMP-0006","CMP-0018"): "EUV mask inspection",
    ("CMP-0011","CMP-0018"): "batch deposition",
    ("CMP-0015","CMP-0018"): "photomask blanks",
    ("CMP-0013","CMP-0018"): "CMP slurry",
    ("CMP-0024","CMP-0019"): "silicon wafers",
    ("CMP-0025","CMP-0019"): "silicon wafers",
    ("CMP-0004","CMP-0019"): "deposition equipment",
    ("CMP-0006","CMP-0019"): "EUV mask inspection",
    ("CMP-0011","CMP-0019"): "batch deposition",
    ("CMP-0015","CMP-0019"): "photomask blanks",
    ("CMP-0013","CMP-0019"): "CMP slurry",
    ("CMP-0024","CMP-0020"): "silicon wafers",
    ("CMP-0025","CMP-0020"): "silicon wafers",
    ("CMP-0004","CMP-0020"): "deposition equipment",
    ("CMP-0005","CMP-0020"): "test equipment",
    ("CMP-0011","CMP-0020"): "batch deposition",
    ("CMP-0015","CMP-0020"): "photomask blanks",
    ("CMP-0020","CMP-0028"): "HBM memory",
    ("CMP-0024","CMP-0021"): "silicon wafers",
    ("CMP-0025","CMP-0021"): "silicon wafers",
    ("CMP-0005","CMP-0021"): "test equipment",
    ("CMP-0011","CMP-0021"): "batch deposition",
    ("CMP-0014","CMP-0022"): "NAND flash",
    ("CMP-0011","CMP-0014"): "batch deposition",
    ("CMP-0026","CMP-0017"): "EUV lithography",
    ("CMP-0026","CMP-0018"): "EUV lithography",
    ("CMP-0026","CMP-0019"): "EUV lithography",
    ("CMP-0026","CMP-0020"): "EUV lithography",
    ("CMP-0026","CMP-0021"): "EUV lithography",
    ("CMP-0007","CMP-0019"): "CMP slurry",
    ("CMP-0005","CMP-0017"): "test equipment",
    ("CMP-0006","CMP-0017"): "EUV mask inspection",
    ("CMP-0001","CMP-0002"): "dicing equipment",
    ("CMP-0002","CMP-0001"): "dicing equipment",
    ("CMP-0024","CMP-0025"): "silicon wafers",
    ("CMP-0025","CMP-0024"): "silicon wafers",
    ("CMP-0014","CMP-0023"): "Yokkaichi/Kitakami JV",
    ("CMP-0023","CMP-0014"): "Yokkaichi/Kitakami JV",
    ("CMP-0018","CMP-0020"): "memory",
    ("CMP-0018","CMP-0021"): "memory",
    ("CMP-0006","CMP-0026"): "EUV inspection + lithography",
    ("CMP-0026","CMP-0006"): "EUV lithography + inspection",
    ("CMP-0015","CMP-0026"): "EUV blanks + lithography",
    ("CMP-0026","CMP-0015"): "EUV lithography + blanks",
    ("CMP-0010","CMP-0017"): "photoresist materials",
    ("CMP-0010","CMP-0018"): "photoresist materials",
    ("CMP-0010","CMP-0019"): "photoresist materials",
    ("CMP-0008","CMP-0017"): "semiconductor materials",
    ("CMP-0008","CMP-0018"): "semiconductor materials",
    ("CMP-0008","CMP-0019"): "semiconductor materials",
    ("CMP-0029","CMP-0004"): "precision machining parts (80%)",
    ("CMP-0030","CMP-0004"): "aluminum vacuum chambers",
    ("CMP-0030","CMP-0003"): "aluminum vacuum chambers",
    ("CMP-0031","CMP-0004"): "thermal spray coating",
    ("CMP-0031","CMP-0003"): "thermal spray coating",
    ("CMP-0032","CMP-0017"): "specialty gases",
    ("CMP-0032","CMP-0018"): "specialty gases",
    ("CMP-0032","CMP-0019"): "specialty gases",
    ("CMP-0032","CMP-0020"): "specialty gases",
    ("CMP-0032","CMP-0021"): "specialty gases",
    ("CMP-0033","CMP-0017"): "photoresist (25% world)",
    ("CMP-0033","CMP-0018"): "photoresist",
    ("CMP-0033","CMP-0019"): "photoresist",
    ("CMP-0034","CMP-0017"): "EUV photoresist",
    ("CMP-0034","CMP-0018"): "EUV photoresist",
    ("CMP-0034","CMP-0019"): "EUV photoresist",
    ("CMP-0035","CMP-0034"): "high-purity aromatics",
    ("CMP-0035","CMP-0033"): "high-purity aromatics",
    ("CMP-0036","CMP-0017"): "CMP systems, vacuum pumps",
    ("CMP-0036","CMP-0018"): "CMP systems, vacuum pumps",
    ("CMP-0036","CMP-0019"): "CMP systems, vacuum pumps",
    ("CMP-0037","CMP-0017"): "ceramic electrostatic chucks",
    ("CMP-0037","CMP-0018"): "ceramic electrostatic chucks",
    ("CMP-0038","CMP-0033"): "photosensitive resin",
    ("CMP-0038","CMP-0034"): "photosensitive resin",
    ("CMP-0039","CMP-0017"): "IC package substrates",
    ("CMP-0039","CMP-0018"): "IC package substrates",
    ("CMP-0040","CMP-0017"): "CMP slurry, photoresist",
    ("CMP-0040","CMP-0018"): "CMP slurry, photoresist",
    ("CMP-0041","CMP-0004"): "wafer transfer robots",
    ("CMP-0041","CMP-0003"): "wafer transfer robots",
    ("CMP-0041","CMP-0017"): "wafer handling systems",
    ("CMP-0042","CMP-0004"): "mechanical seals, bellows",
    ("CMP-0042","CMP-0003"): "mechanical seals, bellows",
    ("CMP-0043","CMP-0004"): "pneumatic valves",
    ("CMP-0043","CMP-0003"): "pneumatic valves",
    ("CMP-0043","CMP-0011"): "pneumatic valves",
    ("CMP-0044","CMP-0017"): "12-nine purity HF acid",
    ("CMP-0044","CMP-0018"): "12-nine purity HF acid",
    ("CMP-0044","CMP-0019"): "ultra-high purity HF",
    ("CMP-0044","CMP-0020"): "ultra-high purity HF",
    ("CMP-0044","CMP-0021"): "ultra-high purity HF",
    ("CMP-0045","CMP-0017"): "specialty fluorine gases",
    ("CMP-0045","CMP-0018"): "specialty fluorine gases",
    ("CMP-0046","CMP-0017"): "photoresist",
    ("CMP-0046","CMP-0018"): "photoresist",
    ("CMP-0047","CMP-0017"): "EUV photomasks",
    ("CMP-0047","CMP-0026"): "EUV photomask production",
    ("CMP-0026","CMP-0047"): "EUV lithography + masks",
    ("CMP-0048","CMP-0028"): "AI server IC substrates (50%+)",
    ("CMP-0048","CMP-0017"): "high-end FC-BGA substrates",
    ("CMP-0049","CMP-0026"): "nanoimprint lithography",
    ("CMP-0049","CMP-0017"): "photomask production",
    ("CMP-0026","CMP-0049"): "nanoimprint partnership",
    ("CMP-0050","CMP-0017"): "i-line/KrF steppers",
    ("CMP-0050","CMP-0018"): "lithography equipment",
    ("CMP-0050","CMP-0026"): "lithography equipment",
    ("CMP-0026","CMP-0050"): "lithography equipment",
    ("CMP-0051","CMP-0017"): "i-line/KrF steppers",
    ("CMP-0051","CMP-0018"): "lithography equipment",
    ("CMP-0051","CMP-0019"): "nanoimprint lithography",
    ("CMP-0051","CMP-0026"): "lithography equipment",
    ("CMP-0026","CMP-0051"): "lithography equipment",
    ("CMP-0052","CMP-0017"): "ultrapure water systems",
    ("CMP-0052","CMP-0018"): "ultrapure water systems",
    ("CMP-0053","CMP-0017"): "ultrapure water systems",
    ("CMP-0053","CMP-0020"): "ultrapure water systems",
    ("CMP-0054","CMP-0005"): "tester boards/probes",
    ("CMP-0054","CMP-0018"): "test equipment components",
    ("CMP-0055","CMP-0005"): "probe card springs",
    ("CMP-0055","CMP-0017"): "HDD suspension (50%)",
    ("CMP-0056","CMP-0017"): "cleanroom AMHS",
    ("CMP-0056","CMP-0018"): "cleanroom AMHS",
    ("CMP-0056","CMP-0019"): "cleanroom AMHS",
    ("CMP-0057","CMP-0048"): "copper surface treatment",
    ("CMP-0057","CMP-0017"): "PCB surface treatment",
    ("CMP-0058","CMP-0033"): "chemical distribution",
    ("CMP-0058","CMP-0034"): "chemical distribution",
    ("CMP-0058","CMP-0017"): "electronic chemicals",
    ("CMP-0059","CMP-0017"): "plasma processing equipment",
    ("CMP-0059","CMP-0018"): "plasma processing equipment",
    ("CMP-0060","CMP-0017"): "plasma CVD equipment",
    ("CMP-0060","CMP-0018"): "dry etching equipment",
    ("CMP-0061","CMP-0050"): "i-line UV lamps (75%)",
    ("CMP-0061","CMP-0051"): "i-line UV lamps",
    ("CMP-0062","CMP-0017"): "coater/developer equipment",
    ("CMP-0062","CMP-0018"): "coating equipment",
    # Wave 4
    ("CMP-0001","CMP-0017"): "probing, dicing, CMP equipment",
    ("CMP-0001","CMP-0018"): "probing, dicing equipment",
    ("CMP-0001","CMP-0019"): "probing, dicing equipment",
    ("CMP-0001","CMP-0020"): "probing, dicing equipment",
    ("CMP-0001","CMP-0021"): "probing, dicing equipment",
    ("CMP-0001","CMP-0014"): "probing, dicing equipment",
    ("CMP-0001","CMP-0063"): "dicing, probing (OSAT #1)",
    ("CMP-0001","CMP-0064"): "dicing, probing (OSAT #2)",
    ("CMP-0001","CMP-0065"): "dicing, probing (China OSAT #1)",
    ("CMP-0001","CMP-0066"): "CMP, probing, dicing (China foundry #1)",
    ("CMP-0001","CMP-0067"): "dicing, probing (China OSAT #2)",
    ("CMP-0001","CMP-0068"): "dicing, probing (China OSAT #3)",
    ("CMP-0001","CMP-0069"): "dicing, probing (Taiwan memory OSAT)",
    ("CMP-0001","CMP-0070"): "CMP, probing (China foundry #2)",
    ("CMP-0002","CMP-0063"): "dicing saws, blades",
    ("CMP-0002","CMP-0064"): "dicing saws, blades",
    ("CMP-0002","CMP-0065"): "dicing saws, blades",
    ("CMP-0002","CMP-0067"): "dicing saws, blades",
    ("CMP-0002","CMP-0068"): "dicing saws, blades",
    ("CMP-0002","CMP-0069"): "dicing saws, blades",
    ("CMP-0004","CMP-0066"): "coater/developer, etch, CVD",
    ("CMP-0004","CMP-0070"): "deposition equipment",
    ("CMP-0011","CMP-0066"): "batch deposition",
    ("CMP-0026","CMP-0066"): "DUV lithography",
    ("CMP-0005","CMP-0063"): "test equipment",
    ("CMP-0005","CMP-0064"): "test equipment",
    ("CMP-0072","CMP-0020"): "TC bonders for HBM (71% share)",
    ("CMP-0072","CMP-0021"): "TC bonders for HBM",
    ("CMP-0072","CMP-0063"): "flip chip bonders",
    ("CMP-0069","CMP-0021"): "memory packaging (key Micron supplier)",
    ("CMP-0066","CMP-0065"): "SMIC is JCET 2nd largest shareholder",
    ("CMP-0065","CMP-0066"): "JCET packaging for SMIC chips",
    ("CMP-0001","CMP-0071"): "probing equipment",
    ("CMP-0071","CMP-0001"): "probing equipment",
    ("CMP-0001","CMP-0073"): "probing (China domestic)",
    ("CMP-0073","CMP-0001"): "probing (China domestic)",
    ("CMP-0001","CMP-0074"): "dicing equipment",
    ("CMP-0074","CMP-0001"): "dicing equipment",
    ("CMP-0002","CMP-0074"): "dicing equipment",
    ("CMP-0074","CMP-0002"): "dicing equipment",
    ("CMP-0001","CMP-0072"): "package singulation",
    ("CMP-0072","CMP-0001"): "package singulation",
    ("CMP-0001","CMP-0005"): "die-level prober joint dev (2025)",
    ("CMP-0005","CMP-0001"): "die-level prober joint dev (2025)",
    ("CMP-0063","CMP-0064"): "OSAT services",
    ("CMP-0063","CMP-0065"): "OSAT services",
    # Wave 5 Korean
    ("CMP-0001","CMP-0075"): "probing, dicing (Korea foundry)",
    ("CMP-0001","CMP-0076"): "probing, dicing (Korea OSAT #1)",
    ("CMP-0001","CMP-0077"): "probing, dicing (Korea OSAT)",
    ("CMP-0001","CMP-0078"): "probing, dicing (Samsung backend)",
    ("CMP-0001","CMP-0079"): "probing, dicing (DDI specialist)",
    ("CMP-0001","CMP-0083"): "probing, dicing (China foundry)",
    ("CMP-0001","CMP-0084"): "probing, dicing (China IDM)",
    ("CMP-0001","CMP-0093"): "probing, dicing (YMTC)",
    ("CMP-0001","CMP-0094"): "probing, dicing (CanSemi)",
    ("CMP-0001","CMP-0095"): "probing, dicing (GTA Semi)",
    ("CMP-0076","CMP-0018"): "OSAT for Samsung",
    ("CMP-0076","CMP-0020"): "OSAT for SK Hynix",
    ("CMP-0078","CMP-0018"): "OSAT for Samsung",
    ("CMP-0080","CMP-0018"): "test handlers",
    ("CMP-0080","CMP-0020"): "test handlers",
    ("CMP-0081","CMP-0018"): "CMP equipment (Korea only)",
    ("CMP-0081","CMP-0020"): "CMP equipment",
    ("CMP-0082","CMP-0017"): "probe components",
    ("CMP-0082","CMP-0018"): "probe components, test sockets",
    ("CMP-0082","CMP-0028"): "test sockets for AI chips",
    ("CMP-0085","CMP-0066"): "deposition/etch equipment",
    ("CMP-0085","CMP-0070"): "deposition/etch equipment",
    ("CMP-0088","CMP-0066"): "CMP equipment (Huahai Qingke)",
    ("CMP-0088","CMP-0070"): "CMP equipment",
    ("CMP-0090","CMP-0066"): "fabless IC design client",
    ("CMP-0090","CMP-0083"): "fabless IC design client",
    ("CMP-0093","CMP-0088"): "CMP equipment for YMTC",
    ("CMP-0100","CMP-0075"): "used semiconductor equipment",
    ("CMP-0001","CMP-0002"): "dicing equipment",
    ("CMP-0002","CMP-0001"): "dicing equipment",
}

CRITICAL_IDS = {
    "CMP-0006", "CMP-0017", "CMP-0024", "CMP-0025", "CMP-0026",
    "CMP-0033", "CMP-0044", "CMP-0048", "CMP-0052", "CMP-0056",
    "CMP-0061", "CMP-0001", "CMP-0072", "CMP-0015", "CMP-0004",
}


def assign_wave(cid):
    num = int(cid.split("-")[1])
    if 1 <= num <= 16:   return 1
    if 17 <= num <= 28:  return 2
    if 29 <= num <= 62:  return 3
    if 63 <= num <= 74:  return 4
    if num in range(75, 83) or num == 100: return 5
    return 6


def load_data():
    with open(GRAPH_FILE, encoding="utf-8") as f:
        graph = json.load(f)
    with open(EVAL_FILE, encoding="utf-8") as f:
        eval_prog = json.load(f)

    # Company files: id -> full record
    company_map = {}
    for fp in glob.glob(os.path.join(COMPANY_DIR, "CMP-*.json")):
        with open(fp, encoding="utf-8") as f:
            c = json.load(f)
        company_map[c["id"]] = c

    # Eval map: ticker -> eval entry, also id -> eval entry
    eval_by_id = {c["id"]: c for c in eval_prog["companies"]}

    return graph, company_map, eval_by_id, eval_prog


def build_node_js(graph, company_map, eval_by_id):
    lines = []
    for n in graph["nodes"]:
        cid = n["id"]
        c = company_map.get(cid, {})
        ev = eval_by_id.get(cid, {})
        rd = ev.get("researchData", {})

        desc = c.get("description") or c.get("desc", "")
        wave = assign_wave(cid)
        critical = cid in CRITICAL_IDS

        # Eval fields
        final_score = ev.get("finalScore")
        confidence  = ev.get("confidence", "")
        per         = rd.get("PER")
        fo_pct      = rd.get("foreignOwnership_pct")
        thesis      = ev.get("investmentThesis", "")
        raw         = ev.get("rawComposite")
        scores      = ev.get("scores", {})
        moat_score  = scores.get("B", {}).get("total")

        node = {
            "id":          cid,
            "name":        n["name"],
            "industry":    n["industry"],
            "country":     n["country"],
            "ticker":      n.get("ticker") or "",
            "wave":        wave,
            "critical":    critical,
            "desc":        desc,
            "finalScore":  final_score,
            "confidence":  confidence,
            "per":         per,
            "foPct":       fo_pct,
            "thesis":      thesis,
            "rawScore":    raw,
            "moatScore":   moat_score,
        }
        lines.append("                " + json.dumps(node, ensure_ascii=False))
    return ",\n".join(lines)


def build_edge_js(graph):
    lines = []
    for e in graph["edges"]:
        src = e["source"]
        tgt = e["target"]
        typ = e.get("type", "supplier")
        label = EDGE_LABELS.get((src, tgt), "")
        edge = {"source": src, "target": tgt, "type": typ}
        if label:
            edge["label"] = label
        lines.append("                " + json.dumps(edge, ensure_ascii=False))
    return ",\n".join(lines)


def score_color(score):
    if score is None:
        return "none"
    if score >= 62:
        return "#f59e0b"   # gold — top tier
    if score >= 55:
        return "#22c55e"   # green — strong
    if score >= 45:
        return "#3b82f6"   # blue — moderate
    return "#6b7280"       # gray — weak


def generate_html(graph, company_map, eval_by_id, eval_prog):
    stats    = graph["statistics"]
    total_n  = stats["totalNodes"]
    total_e  = stats["totalEdges"]
    edge_t   = stats["edgeTypes"]

    geo = {}
    for n in graph["nodes"]:
        geo[n["country"]] = geo.get(n["country"], 0) + 1
    japan_count = geo.get("Japan", 0)

    node_js = build_node_js(graph, company_map, eval_by_id)
    edge_js = build_edge_js(graph)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Semiconductor Supply Chain Map - {total_n} Companies</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0a0a0f;
            color: #e0e0e0;
            overflow: hidden;
        }}
        #container {{ display: flex; height: 100vh; }}
        #sidebar {{
            width: 340px;
            background: #12121a;
            padding: 20px;
            overflow-y: auto;
            border-right: 1px solid #2a2a3a;
            flex-shrink: 0;
        }}
        #graph {{ flex: 1; position: relative; }}
        h1 {{ font-size: 1.4rem; margin-bottom: 8px; color: #fff; }}
        .subtitle {{ font-size: 0.85rem; color: #888; margin-bottom: 20px; }}
        .section {{ margin-bottom: 24px; }}
        .section-title {{
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #666;
            margin-bottom: 12px;
        }}
        .filter-group {{ display: flex; flex-wrap: wrap; gap: 6px; }}
        .filter-btn {{
            padding: 6px 12px;
            font-size: 0.8rem;
            border: 1px solid #3a3a4a;
            background: transparent;
            color: #aaa;
            border-radius: 16px;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .filter-btn:hover {{ border-color: #5a5a6a; color: #fff; }}
        .filter-btn.active {{ background: #2563eb; border-color: #2563eb; color: #fff; }}
        .legend {{ display: flex; flex-direction: column; gap: 8px; }}
        .legend-item {{ display: flex; align-items: center; gap: 10px; font-size: 0.85rem; }}
        .legend-circle {{ width: 14px; height: 14px; border-radius: 50%; flex-shrink: 0; }}
        .legend-line {{ width: 30px; height: 3px; border-radius: 2px; flex-shrink: 0; }}
        .stats-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
        .stat-card {{ background: #1a1a24; padding: 12px; border-radius: 8px; }}
        .stat-value {{ font-size: 1.5rem; font-weight: 600; color: #fff; }}
        .stat-label {{ font-size: 0.75rem; color: #888; }}
        #tooltip {{
            position: absolute;
            background: #1a1a24;
            border: 1px solid #3a3a4a;
            border-radius: 10px;
            padding: 14px 16px;
            font-size: 0.85rem;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.15s;
            max-width: 360px;
            z-index: 1000;
            line-height: 1.5;
        }}
        #tooltip.visible {{ opacity: 1; }}
        #tooltip h3 {{ font-size: 1rem; margin-bottom: 10px; color: #fff; }}
        #tooltip .info-row {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 4px;
            gap: 12px;
        }}
        #tooltip .info-label {{ color: #888; white-space: nowrap; }}
        #tooltip .info-value {{ color: #fff; text-align: right; }}
        #tooltip .divider {{
            border-top: 1px solid #2a2a3a;
            margin: 10px 0 8px;
        }}
        #tooltip .section-label {{
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #555;
            margin-bottom: 8px;
        }}
        #tooltip .score-bar-container {{
            background: #0f0f18;
            border-radius: 4px;
            height: 8px;
            margin: 6px 0 10px;
            overflow: hidden;
        }}
        #tooltip .score-bar {{
            height: 100%;
            border-radius: 4px;
            transition: width 0.3s;
        }}
        #tooltip .thesis-text {{
            font-size: 0.78rem;
            color: #bbb;
            line-height: 1.55;
            margin-top: 8px;
            padding-top: 8px;
            border-top: 1px solid #2a2a3a;
            max-height: 130px;
            overflow-y: auto;
        }}
        #tooltip .desc-text {{
            margin-top: 10px;
            padding-top: 8px;
            border-top: 1px solid #2a2a3a;
            font-size: 0.78rem;
            color: #aaa;
            line-height: 1.5;
            max-height: 90px;
            overflow-y: auto;
        }}
        #tooltip .confidence-badge {{
            display: inline-block;
            padding: 2px 8px;
            border-radius: 10px;
            font-size: 0.72rem;
            font-weight: 600;
        }}
        .conf-High       {{ background: #064e3b; color: #34d399; }}
        .conf-Medium     {{ background: #1e3a5f; color: #60a5fa; }}
        .conf-Low        {{ background: #3b1f00; color: #fb923c; }}
        .conf-Very-Low   {{ background: #2d1b4e; color: #a78bfa; }}
        .node {{ cursor: pointer; }}
        .node text {{ font-size: 10px; fill: #ccc; pointer-events: none; }}
        .link {{ fill: none; stroke-opacity: 0.3; }}
        .link.supplier   {{ stroke: #3b82f6; }}
        .link.competitor {{ stroke: #ef4444; }}
        .link.partner    {{ stroke: #22c55e; }}
        .link.ecosystem  {{ stroke: #a855f7; }}
        .link.highlighted {{ stroke-opacity: 1 !important; stroke-width: 3px !important; }}
        .node.dimmed circle, .node.dimmed ellipse {{ opacity: 0.15; }}
        .node.dimmed text  {{ opacity: 0.15; }}
        .link.dimmed       {{ stroke-opacity: 0.03 !important; }}
        #controls {{
            position: absolute;
            bottom: 20px;
            right: 20px;
            display: flex;
            gap: 8px;
        }}
        .control-btn {{
            width: 40px; height: 40px;
            border: 1px solid #3a3a4a;
            background: #12121a;
            color: #aaa;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1.2rem;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .control-btn:hover {{ background: #1a1a24; color: #fff; }}
        .critical-badge {{
            background: #dc2626; color: white;
            font-size: 0.65rem; padding: 2px 6px;
            border-radius: 4px; margin-left: 6px;
        }}
        #search {{
            width: 100%; padding: 10px 14px;
            background: #1a1a24;
            border: 1px solid #3a3a4a;
            border-radius: 8px;
            color: #fff; font-size: 0.9rem;
            margin-bottom: 20px;
        }}
        #search:focus {{ outline: none; border-color: #2563eb; }}
        #search::placeholder {{ color: #666; }}
        .critical-scroll {{ max-height: 200px; overflow-y: auto; }}
        .wave-badge {{ font-size: 0.65rem; padding: 2px 6px; border-radius: 4px; margin-left: 4px; }}
        .wave-1 {{ background: #059669; color: white; }}
        .wave-2 {{ background: #2563eb; color: white; }}
        .wave-3 {{ background: #7c3aed; color: white; }}
        .wave-4 {{ background: #f97316; color: white; }}
        .wave-5 {{ background: #0891b2; color: white; }}
        .wave-6 {{ background: #b45309; color: white; }}
        #score-legend {{
            display: flex;
            flex-direction: column;
            gap: 6px;
            font-size: 0.8rem;
        }}
        #score-legend .sl-row {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        #score-legend .sl-ring {{
            width: 16px; height: 16px;
            border-radius: 50%;
            border: 2.5px solid transparent;
            flex-shrink: 0;
        }}
    </style>
</head>
<body>
<div id="container">
    <div id="sidebar">
        <h1>Semiconductor Supply Chain</h1>
        <p class="subtitle">{total_n} companies across 7 regions (Wave 6 Complete)</p>

        <input type="text" id="search" placeholder="Search companies...">

        <div class="section">
            <div class="section-title">Statistics</div>
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-value">{total_n}</div>
                    <div class="stat-label">Companies</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">{total_e}</div>
                    <div class="stat-label">Relationships</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">{japan_count}</div>
                    <div class="stat-label">Japanese</div>
                </div>
                <div class="stat-card">
                    <div class="stat-value">{len(CRITICAL_IDS)}</div>
                    <div class="stat-label">Critical Nodes</div>
                </div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Filter by Country</div>
            <div class="filter-group" id="country-filters">
                <button class="filter-btn active" data-filter="all">All</button>
                <button class="filter-btn" data-filter="Japan">Japan ({geo.get('Japan',0)})</button>
                <button class="filter-btn" data-filter="China">China ({geo.get('China',0)})</button>
                <button class="filter-btn" data-filter="South Korea">Korea ({geo.get('South Korea',0)})</button>
                <button class="filter-btn" data-filter="USA">USA ({geo.get('USA',0)})</button>
                <button class="filter-btn" data-filter="Taiwan">Taiwan ({geo.get('Taiwan',0)})</button>
                <button class="filter-btn" data-filter="Hong Kong">HK ({geo.get('Hong Kong',0)})</button>
                <button class="filter-btn" data-filter="Netherlands">NL</button>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Filter by Industry</div>
            <div class="filter-group" id="industry-filters">
                <button class="filter-btn active" data-filter="all">All</button>
                <button class="filter-btn" data-filter="Semiconductor Equipment">Equipment</button>
                <button class="filter-btn" data-filter="Semiconductor Materials">Materials</button>
                <button class="filter-btn" data-filter="Semiconductor Packaging/OSAT">OSAT</button>
                <button class="filter-btn" data-filter="Semiconductor Foundry">Foundry</button>
                <button class="filter-btn" data-filter="Semiconductors">IDM/Fabless</button>
                <button class="filter-btn" data-filter="Memory Semiconductors">Memory</button>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Filter by Wave</div>
            <div class="filter-group" id="wave-filters">
                <button class="filter-btn active" data-filter="all">All</button>
                <button class="filter-btn" data-filter="1">W1 JP seed (16)</button>
                <button class="filter-btn" data-filter="2">W2 Global (12)</button>
                <button class="filter-btn" data-filter="3">W3 JP vendors (34)</button>
                <button class="filter-btn" data-filter="4">W4 OSAT/Foundry (12)</button>
                <button class="filter-btn" data-filter="5">W5 Korea (9)</button>
                <button class="filter-btn" data-filter="6">W6 China (13)</button>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Relationship Types</div>
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-line" style="background:#3b82f6;"></div>
                    <span>Supplier ({edge_t.get('supplier',0)})</span>
                </div>
                <div class="legend-item">
                    <div class="legend-line" style="background:#ef4444;"></div>
                    <span>Competitor ({edge_t.get('competitor',0)})</span>
                </div>
                <div class="legend-item">
                    <div class="legend-line" style="background:#22c55e;"></div>
                    <span>Partner ({edge_t.get('partner',0)})</span>
                </div>
                <div class="legend-item">
                    <div class="legend-line" style="background:#a855f7;"></div>
                    <span>Ecosystem ({edge_t.get('ecosystem',0)})</span>
                </div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Node Colors by Country</div>
            <div class="legend">
                <div class="legend-item"><div class="legend-circle" style="background:#ef4444;"></div><span>Japan</span></div>
                <div class="legend-item"><div class="legend-circle" style="background:#3b82f6;"></div><span>USA</span></div>
                <div class="legend-item"><div class="legend-circle" style="background:#22c55e;"></div><span>South Korea</span></div>
                <div class="legend-item"><div class="legend-circle" style="background:#f59e0b;"></div><span>Taiwan</span></div>
                <div class="legend-item"><div class="legend-circle" style="background:#f97316;"></div><span>China</span></div>
                <div class="legend-item"><div class="legend-circle" style="background:#06b6d4;"></div><span>Hong Kong</span></div>
                <div class="legend-item"><div class="legend-circle" style="background:#8b5cf6;"></div><span>Netherlands</span></div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Score Ring Legend</div>
            <div id="score-legend">
                <div class="sl-row"><div class="sl-ring" style="border-color:#f59e0b; background:#1a1a24;"></div><span>Gold — Top tier (≥62)</span></div>
                <div class="sl-row"><div class="sl-ring" style="border-color:#22c55e; background:#1a1a24;"></div><span>Green — Strong (55-61)</span></div>
                <div class="sl-row"><div class="sl-ring" style="border-color:#3b82f6; background:#1a1a24;"></div><span>Blue — Moderate (45-54)</span></div>
                <div class="sl-row"><div class="sl-ring" style="border-color:#6b7280; background:#1a1a24;"></div><span>Gray — Weak (&lt;45)</span></div>
                <div class="sl-row"><div class="sl-ring" style="border-color:transparent; background:#1a1a24;"></div><span>No ring — Not scored</span></div>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Critical Supply Chain Nodes</div>
            <div class="legend critical-scroll">
                <div class="legend-item"><span>ASML</span><span class="critical-badge">100% EUV</span></div>
                <div class="legend-item"><span>Lasertec</span><span class="critical-badge">100% inspection</span></div>
                <div class="legend-item"><span>Shin-Etsu</span><span class="critical-badge">42% wafers</span></div>
                <div class="legend-item"><span>TSMC</span><span class="critical-badge">90% AI chips</span></div>
                <div class="legend-item"><span>Stella Chemifa</span><span class="critical-badge">HF monopoly</span></div>
                <div class="legend-item"><span>Ibiden</span><span class="critical-badge">50% AI substrates</span></div>
                <div class="legend-item"><span>Organo</span><span class="critical-badge">TSMC water</span></div>
                <div class="legend-item"><span>TOK</span><span class="critical-badge">25% photoresist</span></div>
                <div class="legend-item"><span>Daifuku</span><span class="critical-badge">cleanroom auto</span></div>
                <div class="legend-item"><span>Ushio</span><span class="critical-badge">75% UV lamps</span></div>
                <div class="legend-item"><span>ACCRETECH</span><span class="critical-badge">46% probers</span></div>
                <div class="legend-item"><span>Hanmi Semi</span><span class="critical-badge">71% TC bonders</span></div>
                <div class="legend-item"><span>HOYA</span><span class="critical-badge">EUV blanks</span></div>
                <div class="legend-item"><span>Tokyo Electron</span><span class="critical-badge">coater/etch</span></div>
                <div class="legend-item"><span>SUMCO</span><span class="critical-badge">20% wafers</span></div>
            </div>
        </div>
    </div>

    <div id="graph">
        <svg id="svg"></svg>
        <div id="tooltip"></div>
        <div id="controls">
            <button class="control-btn" id="zoom-in">+</button>
            <button class="control-btn" id="zoom-out">-</button>
            <button class="control-btn" id="reset">R</button>
        </div>
    </div>
</div>

<script>
    const graphData = {{
        nodes: [
{node_js}
        ],
        edges: [
{edge_js}
        ]
    }};

    const countryColors = {{
        "Japan":       "#ef4444",
        "USA":         "#3b82f6",
        "South Korea": "#22c55e",
        "Taiwan":      "#f59e0b",
        "China":       "#f97316",
        "Hong Kong":   "#06b6d4",
        "Netherlands": "#8b5cf6"
    }};

    const linkColors = {{
        "supplier":   "#3b82f6",
        "competitor": "#ef4444",
        "partner":    "#22c55e",
        "ecosystem":  "#a855f7"
    }};

    function scoreRingColor(score) {{
        if (score === null || score === undefined) return null;
        if (score >= 62) return "#f59e0b";
        if (score >= 55) return "#22c55e";
        if (score >= 45) return "#3b82f6";
        return "#6b7280";
    }}

    function scoreBarColor(score) {{
        if (score === null || score === undefined) return "#6b7280";
        if (score >= 62) return "#f59e0b";
        if (score >= 55) return "#22c55e";
        if (score >= 45) return "#60a5fa";
        return "#6b7280";
    }}

    function fmtNum(v, decimals=1) {{
        if (v === null || v === undefined) return "—";
        return Number(v).toFixed(decimals) + "x";
    }}

    function fmtScore(v) {{
        if (v === null || v === undefined) return "—";
        return Number(v).toFixed(1);
    }}

    function fmtPct(v) {{
        if (v === null || v === undefined) return "—";
        return Number(v).toFixed(1) + "%";
    }}

    function confClass(conf) {{
        if (!conf) return "";
        return "conf-" + conf.replace(/ /g, "-");
    }}

    const width  = document.getElementById('graph').clientWidth;
    const height = document.getElementById('graph').clientHeight;

    const svg = d3.select('#svg').attr('width', width).attr('height', height);
    const g   = svg.append('g');

    const zoom = d3.zoom()
        .scaleExtent([0.15, 6])
        .on('zoom', (event) => {{ g.attr('transform', event.transform); }});
    svg.call(zoom);

    svg.append('defs').selectAll('marker')
        .data(['supplier','competitor','partner','ecosystem'])
        .enter().append('marker')
        .attr('id',          d => `arrow-${{d}}`)
        .attr('viewBox',     '0 -5 10 10')
        .attr('refX',        20)
        .attr('refY',        0)
        .attr('markerWidth', 5)
        .attr('markerHeight',5)
        .attr('orient',      'auto')
        .append('path')
        .attr('fill', d => linkColors[d])
        .attr('d', 'M0,-5L10,0L0,5');

    const simulation = d3.forceSimulation(graphData.nodes)
        .force('link',      d3.forceLink(graphData.edges).id(d => d.id).distance(75))
        .force('charge',    d3.forceManyBody().strength(-200))
        .force('center',    d3.forceCenter(width / 2, height / 2))
        .force('collision', d3.forceCollide().radius(28))
        .force('x',         d3.forceX(width  / 2).strength(0.04))
        .force('y',         d3.forceY(height / 2).strength(0.04));

    const link = g.append('g')
        .selectAll('line')
        .data(graphData.edges)
        .enter().append('line')
        .attr('class',       d => `link ${{d.type}}`)
        .attr('stroke',      d => linkColors[d.type])
        .attr('stroke-width', 1)
        .attr('marker-end',  d => `url(#arrow-${{d.type}})`);

    const node = g.append('g')
        .selectAll('g')
        .data(graphData.nodes)
        .enter().append('g')
        .attr('class', 'node')
        .call(d3.drag()
            .on('start', dragstarted)
            .on('drag',  dragged)
            .on('end',   dragended));

    // Score ring (outer)
    node.append('circle')
        .attr('r', d => (d.critical ? 14 : 10))
        .attr('fill',         'none')
        .attr('stroke',       d => scoreRingColor(d.finalScore) || 'none')
        .attr('stroke-width', d => scoreRingColor(d.finalScore) ? 2.5 : 0);

    // Main node circle
    node.append('circle')
        .attr('r',            d => d.critical ? 11 : 7)
        .attr('fill',         d => countryColors[d.country] || '#888')
        .attr('stroke',       d => d.critical ? '#fff' : 'none')
        .attr('stroke-width', d => d.critical ? 1.5 : 0);

    node.append('text')
        .attr('dx', 13)
        .attr('dy', 3)
        .text(d => d.name);

    // ── Tooltip ──────────────────────────────────────────────────────────────
    const tooltip = d3.select('#tooltip');

    node.on('mouseover', function(event, d) {{
        const suppliers = graphData.edges.filter(e =>
            (e.target.id || e.target) === d.id && e.type === 'supplier').length;
        const clients = graphData.edges.filter(e =>
            (e.source.id || e.source) === d.id && e.type === 'supplier').length;

        const hasScore = d.finalScore !== null && d.finalScore !== undefined;
        const scoreBarW = hasScore ? Math.min(100, d.finalScore) : 0;
        const ringColor = scoreRingColor(d.finalScore);
        const barColor  = scoreBarColor(d.finalScore);
        const confCls   = confClass(d.confidence);

        let evalHtml = '';
        if (hasScore) {{
            evalHtml = `
            <div class="divider"></div>
            <div class="section-label">Investment Score</div>
            <div class="info-row">
                <span class="info-label">Final Score</span>
                <span class="info-value" style="color:${{ringColor || '#fff'}};font-weight:700;">
                    ${{fmtScore(d.finalScore)}} / 100
                </span>
            </div>
            <div class="score-bar-container">
                <div class="score-bar" style="width:${{scoreBarW}}%;background:${{barColor}};"></div>
            </div>
            <div class="info-row">
                <span class="info-label">Confidence</span>
                <span class="info-value">
                    <span class="confidence-badge ${{confCls}}">${{d.confidence || '—'}}</span>
                </span>
            </div>
            <div class="info-row">
                <span class="info-label">PER</span>
                <span class="info-value">${{d.per !== null && d.per !== undefined ? Number(d.per).toFixed(1) + 'x' : '—'}}</span>
            </div>
            <div class="info-row">
                <span class="info-label">Foreign Ownership</span>
                <span class="info-value">${{fmtPct(d.foPct)}}</span>
            </div>`;

            if (d.thesis) {{
                evalHtml += `<div class="thesis-text">${{d.thesis}}</div>`;
            }}
        }}

        let descHtml = '';
        if (d.desc) {{
            descHtml = `<div class="desc-text">${{d.desc}}</div>`;
        }}

        tooltip.html(`
            <h3>${{d.name}}${{d.critical ? ' <span style="color:#ef4444;font-size:0.75rem;">● CRITICAL</span>' : ''}}</h3>
            <div class="info-row">
                <span class="info-label">Ticker</span>
                <span class="info-value">${{d.ticker || '—'}}</span>
            </div>
            <div class="info-row">
                <span class="info-label">Industry</span>
                <span class="info-value">${{d.industry}}</span>
            </div>
            <div class="info-row">
                <span class="info-label">Country</span>
                <span class="info-value">${{d.country}}</span>
            </div>
            <div class="info-row">
                <span class="info-label">Wave</span>
                <span class="info-value"><span class="wave-badge wave-${{d.wave}}">W${{d.wave}}</span></span>
            </div>
            <div class="info-row">
                <span class="info-label">Suppliers / Clients</span>
                <span class="info-value">${{suppliers}} → ${{clients}}</span>
            </div>
            ${{evalHtml}}
            ${{descHtml}}
        `)
        .style('left', (event.pageX + 16) + 'px')
        .style('top',  (event.pageY - 16) + 'px')
        .classed('visible', true);

        // Highlight neighbourhood
        const connected = new Set([d.id]);
        graphData.edges.forEach(e => {{
            const s = e.source.id || e.source;
            const t = e.target.id || e.target;
            if (s === d.id) connected.add(t);
            if (t === d.id) connected.add(s);
        }});
        node.classed('dimmed', n => !connected.has(n.id));
        link.classed('dimmed', e => {{
            const s = e.source.id || e.source;
            const t = e.target.id || e.target;
            return s !== d.id && t !== d.id;
        }});
        link.classed('highlighted', e => {{
            const s = e.source.id || e.source;
            const t = e.target.id || e.target;
            return s === d.id || t === d.id;
        }});
    }})
    .on('mousemove', function(event) {{
        tooltip
            .style('left', (event.pageX + 16) + 'px')
            .style('top',  (event.pageY - 16) + 'px');
    }})
    .on('mouseout', function() {{
        tooltip.classed('visible', false);
        node.classed('dimmed', false);
        link.classed('dimmed', false);
        link.classed('highlighted', false);
    }});

    simulation.on('tick', () => {{
        link
            .attr('x1', d => d.source.x)
            .attr('y1', d => d.source.y)
            .attr('x2', d => d.target.x)
            .attr('y2', d => d.target.y);
        node.attr('transform', d => `translate(${{d.x}},${{d.y}})`);
    }});

    function dragstarted(event) {{
        if (!event.active) simulation.alphaTarget(0.3).restart();
        event.subject.fx = event.subject.x;
        event.subject.fy = event.subject.y;
    }}
    function dragged(event) {{
        event.subject.fx = event.x;
        event.subject.fy = event.y;
    }}
    function dragended(event) {{
        if (!event.active) simulation.alphaTarget(0);
        event.subject.fx = null;
        event.subject.fy = null;
    }}

    // ── Filters ──────────────────────────────────────────────────────────────
    let activeCountry  = 'all';
    let activeIndustry = 'all';
    let activeWave     = 'all';

    function applyFilters() {{
        node.style('display', d => {{
            const cm = activeCountry  === 'all' || d.country   === activeCountry;
            const im = activeIndustry === 'all' || d.industry  === activeIndustry;
            const wm = activeWave     === 'all' || d.wave      === parseInt(activeWave);
            return (cm && im && wm) ? null : 'none';
        }});
        link.style('display', d => {{
            const sn = graphData.nodes.find(n => n.id === (d.source.id || d.source));
            const tn = graphData.nodes.find(n => n.id === (d.target.id || d.target));
            if (!sn || !tn) return 'none';
            const scm = activeCountry  === 'all' || sn.country  === activeCountry;
            const sim = activeIndustry === 'all' || sn.industry === activeIndustry;
            const swm = activeWave     === 'all' || sn.wave     === parseInt(activeWave);
            const tcm = activeCountry  === 'all' || tn.country  === activeCountry;
            const tim = activeIndustry === 'all' || tn.industry === activeIndustry;
            const twm = activeWave     === 'all' || tn.wave     === parseInt(activeWave);
            return (scm && sim && swm && tcm && tim && twm) ? null : 'none';
        }});
    }}

    document.querySelectorAll('#country-filters .filter-btn').forEach(btn => {{
        btn.addEventListener('click', function() {{
            document.querySelectorAll('#country-filters .filter-btn').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            activeCountry = this.dataset.filter;
            applyFilters();
        }});
    }});
    document.querySelectorAll('#industry-filters .filter-btn').forEach(btn => {{
        btn.addEventListener('click', function() {{
            document.querySelectorAll('#industry-filters .filter-btn').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            activeIndustry = this.dataset.filter;
            applyFilters();
        }});
    }});
    document.querySelectorAll('#wave-filters .filter-btn').forEach(btn => {{
        btn.addEventListener('click', function() {{
            document.querySelectorAll('#wave-filters .filter-btn').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            activeWave = this.dataset.filter;
            applyFilters();
        }});
    }});

    // ── Search ───────────────────────────────────────────────────────────────
    document.getElementById('search').addEventListener('input', function(e) {{
        const q = e.target.value.toLowerCase();
        if (!q) {{
            node.style('opacity', 1);
            link.style('opacity', 1);
            return;
        }}
        const hits = new Set();
        graphData.nodes.forEach(n => {{
            if (n.name.toLowerCase().includes(q) ||
                (n.ticker || '').toLowerCase().includes(q) ||
                n.country.toLowerCase().includes(q) ||
                n.industry.toLowerCase().includes(q)) {{
                hits.add(n.id);
            }}
        }});
        node.style('opacity', d => hits.has(d.id) ? 1 : 0.1);
        link.style('opacity', d => {{
            const s = d.source.id || d.source;
            const t = d.target.id || d.target;
            return (hits.has(s) || hits.has(t)) ? 0.6 : 0.04;
        }});
    }});

    // ── Zoom controls ────────────────────────────────────────────────────────
    document.getElementById('zoom-in').addEventListener('click', () =>
        svg.transition().duration(300).call(zoom.scaleBy, 1.3));
    document.getElementById('zoom-out').addEventListener('click', () =>
        svg.transition().duration(300).call(zoom.scaleBy, 0.77));
    document.getElementById('reset').addEventListener('click', () =>
        svg.transition().duration(500).call(zoom.transform, d3.zoomIdentity));

    window.addEventListener('resize', () => {{
        const w = document.getElementById('graph').clientWidth;
        const h = document.getElementById('graph').clientHeight;
        svg.attr('width', w).attr('height', h);
        simulation.force('center', d3.forceCenter(w / 2, h / 2));
        simulation.alpha(0.3).restart();
    }});

    setTimeout(() => {{
        svg.call(zoom.transform, d3.zoomIdentity.scale(0.6).translate(width * 0.25, height * 0.22));
    }}, 1200);
</script>
</body>
</html>"""
    return html


def main():
    print("Loading data...")
    graph, company_map, eval_by_id, eval_prog = load_data()
    print(f"  {len(graph['nodes'])} nodes, {len(graph['edges'])} edges")
    print(f"  {len(company_map)} company files")
    print(f"  {len(eval_by_id)} eval entries")

    print("Generating HTML...")
    html = generate_html(graph, company_map, eval_by_id, eval_prog)

    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    size_kb = os.path.getsize(OUT_FILE) // 1024
    print(f"Written: {OUT_FILE}  ({size_kb} KB)")


if __name__ == "__main__":
    main()
