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

# ── critical nodes get larger radius + white stroke ──────────────────────────
CRITICAL_IDS = {
    "CMP-0001", "CMP-0004", "CMP-0006", "CMP-0013", "CMP-0024",
    "CMP-0028", "CMP-0035", "CMP-0042", "CMP-0044", "CMP-0056",
    "CMP-0003", "CMP-0005", "CMP-0007", "CMP-0017", "CMP-0029",
}

# ── curated edge labels ───────────────────────────────────────────────────────
EDGE_LABELS = {
    ("CMP-0001","CMP-0017"): "prober customer",
    ("CMP-0001","CMP-0018"): "prober customer",
    ("CMP-0001","CMP-0019"): "prober customer",
    ("CMP-0001","CMP-0020"): "prober customer",
    ("CMP-0001","CMP-0021"): "prober customer",
    ("CMP-0001","CMP-0022"): "CMM tools",
    ("CMP-0001","CMP-0028"): "prober+CMM buyer",
    ("CMP-0002","CMP-0017"): "dicing blades",
    ("CMP-0002","CMP-0018"): "dicing blades",
    ("CMP-0002","CMP-0019"): "dicing blades",
    ("CMP-0003","CMP-0017"): "wafer polishing",
    ("CMP-0003","CMP-0018"): "wafer polishing",
    ("CMP-0004","CMP-0017"): "etch/CVD tools",
    ("CMP-0004","CMP-0018"): "etch/CVD tools",
    ("CMP-0004","CMP-0019"): "etch/CVD tools",
    ("CMP-0004","CMP-0020"): "etch/CVD tools",
    ("CMP-0004","CMP-0028"): "GPU fab tools",
    ("CMP-0005","CMP-0017"): "test handlers",
    ("CMP-0005","CMP-0018"): "test handlers",
    ("CMP-0006","CMP-0017"): "mask inspection",
    ("CMP-0006","CMP-0018"): "mask inspection",
    ("CMP-0006","CMP-0019"): "mask inspection",
    ("CMP-0007","CMP-0017"): "wafer cleaning",
    ("CMP-0007","CMP-0018"): "wafer cleaning",
    ("CMP-0008","CMP-0017"): "photoresist",
    ("CMP-0008","CMP-0018"): "photoresist",
    ("CMP-0009","CMP-0017"): "specialty gases",
    ("CMP-0010","CMP-0017"): "HF etchant",
    ("CMP-0011","CMP-0017"): "wafer substrate",
    ("CMP-0012","CMP-0017"): "photomask blanks",
    ("CMP-0013","CMP-0002"): "CMP slurry",
    ("CMP-0013","CMP-0003"): "CMP slurry",
    ("CMP-0013","CMP-0017"): "CMP slurry",
    ("CMP-0013","CMP-0018"): "CMP slurry",
    ("CMP-0013","CMP-0019"): "CMP slurry",
    ("CMP-0024","CMP-0017"): "silicon wafers",
    ("CMP-0024","CMP-0018"): "silicon wafers",
    ("CMP-0024","CMP-0019"): "silicon wafers",
    ("CMP-0024","CMP-0020"): "silicon wafers",
    ("CMP-0028","CMP-0017"): "GPU design→fab",
    ("CMP-0028","CMP-0019"): "GPU design→fab",
    ("CMP-0044","CMP-0009"): "fluorine supply",
    ("CMP-0044","CMP-0017"): "HF etchant",
    ("CMP-0044","CMP-0018"): "HF etchant",
    ("CMP-0056","CMP-0017"): "fab AMHS",
    ("CMP-0056","CMP-0018"): "fab AMHS",
    ("CMP-0056","CMP-0019"): "fab AMHS",
}

# ── country colour palette ────────────────────────────────────────────────────
COUNTRY_COLORS = {
    "Japan":       "#ef4444",
    "USA":         "#3b82f6",
    "South Korea": "#22c55e",
    "Taiwan":      "#f59e0b",
    "China":       "#f97316",
    "Hong Kong":   "#06b6d4",
    "Netherlands": "#8b5cf6",
    "Unknown":     "#6b7280",
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
    with open(GRAPH_FILE, "r", encoding="utf-8") as f:
        graph = json.load(f)
    with open(EVAL_FILE, "r", encoding="utf-8") as f:
        eval_data = json.load(f)

    # Index evaluation data by id
    eval_map = {c["id"]: c for c in eval_data.get("companies", [])}

    # Load individual company files
    comp_map = {}
    for fp in glob.glob(os.path.join(COMPANY_DIR, "CMP-*.json")):
        with open(fp, "r", encoding="utf-8") as f:
            c = json.load(f)
        comp_map[c["id"]] = c

    return graph, eval_map, comp_map, eval_data


def score_ring_color(score):
    if score is None:  return "#6b7280"
    if score >= 62:    return "#f59e0b"   # gold
    if score >= 55:    return "#22c55e"   # green
    if score >= 45:    return "#3b82f6"   # blue
    return "#6b7280"                       # grey


def build_node_js(graph, eval_map, comp_map):
    rows = []
    for n in graph["nodes"]:
        cid = n["id"]
        ev  = eval_map.get(cid, {})
        cp  = comp_map.get(cid, {})
        rd  = ev.get("researchData", {})

        score  = ev.get("finalScore")
        conf   = ev.get("confidence", "")
        per    = rd.get("PER") or cp.get("PER")
        fo     = rd.get("foreignOwnership_pct") or cp.get("percentOfForeignOwnership")
        ticker = n.get("ticker") or cp.get("ticker") or ""
        wave   = assign_wave(cid)
        ring   = score_ring_color(score)
        crit   = cid in CRITICAL_IDS

        row = {
            "id":      cid,
            "name":    n["name"],
            "ticker":  ticker,
            "country": n.get("country", "Unknown"),
            "industry":n.get("industry", ""),
            "wave":    wave,
            "score":   score,
            "conf":    conf,
            "per":     per,
            "fo":      fo,
            "ring":    ring,
            "crit":    crit,
        }
        rows.append(row)
    return json.dumps(rows, ensure_ascii=False)


def build_edge_js(graph):
    rows = []
    for e in graph["edges"]:
        key = (e["source"], e["target"])
        rows.append({
            "source": e["source"],
            "target": e["target"],
            "type":   e.get("type", "supplier"),
            "label":  EDGE_LABELS.get(key, ""),
        })
    return json.dumps(rows, ensure_ascii=False)


def build_detail_map(graph, eval_map, comp_map):
    """Build per-company comprehensive detail objects for the investment card."""
    # Build adjacency sets keyed by type
    adj = {}  # cid -> {suppliers:[], clients:[], competitors:[], partners:[], ecosystem:[]}
    for n in graph["nodes"]:
        adj[n["id"]] = {"suppliers": [], "clients": [], "competitors": [],
                        "partners": [], "ecosystem": []}

    id_to_name = {n["id"]: n["name"] for n in graph["nodes"]}

    for e in graph["edges"]:
        src, tgt, etype = e["source"], e["target"], e.get("type", "supplier")
        lbl = EDGE_LABELS.get((src, tgt), "")
        if etype == "supplier":
            if tgt in adj:
                adj[tgt]["suppliers"].append({"id": src, "name": id_to_name.get(src, src), "label": lbl})
            if src in adj:
                adj[src]["clients"].append({"id": tgt, "name": id_to_name.get(tgt, tgt), "label": lbl})
        elif etype == "competitor":
            for x, y in [(src, tgt), (tgt, src)]:
                if x in adj:
                    adj[x]["competitors"].append({"id": y, "name": id_to_name.get(y, y), "label": lbl})
        elif etype == "partner":
            for x, y in [(src, tgt), (tgt, src)]:
                if x in adj:
                    adj[x]["partners"].append({"id": y, "name": id_to_name.get(y, y), "label": lbl})
        elif etype == "ecosystem":
            for x, y in [(src, tgt), (tgt, src)]:
                if x in adj:
                    adj[x]["ecosystem"].append({"id": y, "name": id_to_name.get(y, y), "label": lbl})

    detail = {}
    for n in graph["nodes"]:
        cid = n["id"]
        ev  = eval_map.get(cid, {})
        cp  = comp_map.get(cid, {})
        rd  = ev.get("researchData", {})

        # Score dimensions — read from ev["scores"][dim]
        DIM_MAX = {"A": 30, "B": 25, "C": 15, "D": 10, "E": 10, "F": 10}
        scores_data = ev.get("scores", {})
        dims = {}
        for dim in ["A", "B", "C", "D", "E", "F"]:
            sd = scores_data.get(dim, {})
            subs = {k: v for k, v in sd.items()
                    if k not in ("total", "note") and v is not None}
            dims[dim] = {
                "score": sd.get("total"),
                "max":   DIM_MAX[dim],
                "subs":  subs,
                "note":  sd.get("note", ""),
            }

        # Financial row helper – prefer research data then company file
        def f(key_rd, key_cp=None):
            v = rd.get(key_rd)
            if v is None and key_cp:
                v = cp.get(key_cp)
            return v

        detail[cid] = {
            "id":       cid,
            "name":     n["name"],
            "ticker":   n.get("ticker") or cp.get("ticker") or "",
            "country":  n.get("country", "Unknown"),
            "industry": n.get("industry", ""),
            "wave":     assign_wave(cid),
            "website":  cp.get("website", ""),
            "description": cp.get("description", ""),
            # Scores
            "finalScore":        ev.get("finalScore"),
            "rawComposite":      ev.get("rawComposite"),
            "confidence":        ev.get("confidence", ""),
            "confidenceMult":    ev.get("confidenceMultiplier"),
            "dataCoverage":      ev.get("dataCoverage_pct"),
            "researchComplete":  ev.get("researchCompleteness_pct"),
            "dims":              dims,
            "investmentThesis":  ev.get("investmentThesis", ""),
            # Financials
            "marketCapInYen":    f("marketCapInYen", "marketCapInYen"),
            "latestPriceYen":    f("latestPriceYen", "latestPriceYen"),
            "weekHigh52":        f("weekHigh52"),
            "weekLow52":         f("weekLow52"),
            "PER":               f("PER", "PER"),
            "forwardPER":        f("forwardPER"),
            "PBR":               f("PBR", "PBR"),
            "EPS":               f("EPS", "EPS"),
            "ROE":               f("ROE"),
            "dividendYield":     f("dividendYield_pct"),
            "revenueGrowth":     f("revenueGrowthYoY_pct"),
            "OPM":               f("operatingMargin_pct"),
            "foreignOwnership":  f("foreignOwnership_pct", "percentOfForeignOwnership"),
            "chinaRevenue":      f("chinaRevenue_pct_est"),
            "hasBuyback":        f("hasBuyback"),
            "analystBuy":        f("analystBuy"),
            "analystHold":       f("analystHold"),
            "analystSell":       f("analystSell"),
            "forexSensitive":    f("isForexSensitive") if f("isForexSensitive") is not None else cp.get("isForexSensitive"),
            # Supply chain
            "suppliers":    adj[cid]["suppliers"],
            "clients":      adj[cid]["clients"],
            "competitors":  adj[cid]["competitors"],
            "partners":     adj[cid]["partners"],
            "ecosystem":    adj[cid]["ecosystem"],
        }

    return json.dumps(detail, ensure_ascii=False)


def generate_html(nodes_js, edges_js, detail_js, country_colors):
    country_colors_js = json.dumps(country_colors, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Semiconductor Supply Chain Map</title>
<style>
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: #0f1117; color: #e2e8f0;
       display: flex; height: 100vh; overflow: hidden; }}

/* ── Sidebar ────────────────────────────────────────────────────── */
#sidebar {{
  width: 270px; min-width: 270px; background: #1a1d27; border-right: 1px solid #2d3148;
  display: flex; flex-direction: column; overflow: hidden; z-index: 20;
}}
#sidebar h1 {{ font-size: 13px; font-weight: 700; color: #94a3b8;
               padding: 14px 16px 10px; border-bottom: 1px solid #2d3148;
               text-transform: uppercase; letter-spacing: .08em; }}
.filter-section {{ padding: 10px 14px; border-bottom: 1px solid #2d3148; }}
.filter-section h2 {{ font-size: 11px; color: #64748b; text-transform: uppercase;
                      letter-spacing: .07em; margin-bottom: 8px; }}
.filter-row {{ display: flex; align-items: center; gap: 8px; margin-bottom: 5px; cursor: pointer; }}
.filter-row input[type=checkbox] {{ accent-color: #6366f1; cursor: pointer; }}
.filter-row label {{ font-size: 12px; color: #cbd5e1; cursor: pointer; flex: 1; }}
.dot {{ width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }}
.legend-score {{ display: flex; align-items: center; gap: 8px; margin-bottom: 5px; }}
.legend-score .ring {{ width: 14px; height: 14px; border-radius: 50%;
                        border: 3px solid; background: transparent; flex-shrink: 0; }}
.legend-score label {{ font-size: 12px; color: #cbd5e1; }}
#stats {{ padding: 10px 14px; font-size: 11px; color: #64748b; margin-top: auto; }}
#stats span {{ display: block; margin-bottom: 3px; }}

/* ── Detail panel ───────────────────────────────────────────────── */
#detail-panel {{
  width: 0; min-width: 0; overflow: hidden;
  background: #141720; border-right: 1px solid #2d3148;
  transition: width 0.28s cubic-bezier(0.4,0,0.2,1);
  display: flex; flex-direction: column; z-index: 10;
}}
#detail-panel.open {{ width: 440px; min-width: 440px; }}
#dp-inner {{ width: 440px; height: 100%; overflow-y: auto; display: flex; flex-direction: column; }}

/* scrollbar */
#dp-inner::-webkit-scrollbar {{ width: 5px; }}
#dp-inner::-webkit-scrollbar-track {{ background: #0f1117; }}
#dp-inner::-webkit-scrollbar-thumb {{ background: #2d3148; border-radius: 3px; }}

#dp-header {{
  display: flex; align-items: flex-start; gap: 10px;
  padding: 16px 16px 12px; border-bottom: 1px solid #2d3148;
  position: sticky; top: 0; background: #141720; z-index: 2;
}}
#dp-header .title-block {{ flex: 1; min-width: 0; }}
#dp-header h2 {{ font-size: 15px; font-weight: 700; color: #f1f5f9;
                 white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
#dp-header .sub {{ font-size: 11px; color: #64748b; margin-top: 2px; }}
#dp-close {{ background: none; border: none; color: #64748b; font-size: 18px;
              cursor: pointer; padding: 0 2px; line-height: 1; flex-shrink: 0; }}
#dp-close:hover {{ color: #e2e8f0; }}

/* card sections */
.card-section {{ padding: 14px 16px; border-bottom: 1px solid #1e2233; }}
.card-section h3 {{ font-size: 10px; text-transform: uppercase; letter-spacing: .09em;
                    color: #475569; margin-bottom: 10px; font-weight: 600; }}

/* score bar */
.score-bar-wrap {{ margin-bottom: 10px; }}
.score-num {{ font-size: 28px; font-weight: 800; line-height: 1; }}
.score-meta {{ font-size: 11px; color: #64748b; margin-top: 2px; margin-bottom: 8px; }}
.bar-bg {{ height: 8px; background: #1e2233; border-radius: 4px; overflow: hidden; }}
.bar-fill {{ height: 100%; border-radius: 4px; transition: width .4s; }}
.conf-badge {{ display: inline-block; padding: 2px 8px; border-radius: 10px;
               font-size: 10px; font-weight: 600; text-transform: uppercase;
               letter-spacing: .06em; margin-top: 6px; }}
.conf-high   {{ background: #14532d; color: #86efac; }}
.conf-med    {{ background: #1e3a5f; color: #93c5fd; }}
.conf-low    {{ background: #431407; color: #fed7aa; }}
.conf-vlow   {{ background: #1c1917; color: #a8a29e; }}

/* dim grid */
.dim-grid {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 6px; margin-top: 8px; }}
.dim-cell {{ background: #1a1d27; border-radius: 6px; padding: 7px 8px; cursor: default; }}
.dim-cell .dim-label {{ font-size: 9px; color: #64748b; text-transform: uppercase;
                        letter-spacing: .07em; margin-bottom: 3px; }}
.dim-cell .dim-score {{ font-size: 13px; font-weight: 700; color: #e2e8f0; }}
.dim-cell .dim-max {{ font-size: 10px; color: #475569; }}
.dim-bar-bg {{ height: 3px; background: #2d3148; border-radius: 2px; margin: 5px 0 6px; overflow: hidden; }}
.dim-bar-fill {{ height: 100%; border-radius: 2px; transition: width .4s; }}
.dim-subs {{ border-top: 1px solid #2d3148; margin-top: 4px; padding-top: 4px; }}
.sub-row {{ display: flex; justify-content: space-between; align-items: center;
            font-size: 9px; margin-bottom: 2px; gap: 4px; }}
.sub-key {{ color: #475569; flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
.sub-val {{ color: #94a3b8; font-weight: 700; flex-shrink: 0; }}
.dim-note {{ font-size: 9px; color: #334155; margin-top: 4px; line-height: 1.4; font-style: italic; }}

/* thesis */
.thesis-text {{ font-size: 12px; color: #cbd5e1; line-height: 1.65; }}

/* financial table */
.fin-table {{ width: 100%; border-collapse: collapse; }}
.fin-table tr td {{ padding: 4px 2px; font-size: 12px; border-bottom: 1px solid #1e2233; }}
.fin-table tr:last-child td {{ border-bottom: none; }}
.fin-table td:first-child {{ color: #64748b; width: 54%; }}
.fin-table td:last-child {{ color: #f1f5f9; font-weight: 600; text-align: right; }}

/* sc list */
.sc-group {{ margin-bottom: 10px; }}
.sc-group-label {{ font-size: 10px; color: #475569; text-transform: uppercase;
                   letter-spacing: .07em; margin-bottom: 4px; }}
.sc-list {{ display: flex; flex-wrap: wrap; gap: 5px; }}
.sc-chip {{ background: #1a1d27; border: 1px solid #2d3148; border-radius: 12px;
            padding: 3px 10px; font-size: 11px; color: #94a3b8; cursor: pointer;
            transition: background .15s, color .15s; white-space: nowrap; }}
.sc-chip:hover {{ background: #6366f1; color: #fff; border-color: #6366f1; }}

/* website link */
.website-link {{ font-size: 12px; color: #6366f1; text-decoration: none; word-break: break-all; }}
.website-link:hover {{ text-decoration: underline; }}
.desc-text {{ font-size: 12px; color: #cbd5e1; line-height: 1.6; margin-top: 6px; }}

/* ── Graph area ─────────────────────────────────────────────────── */
#graph {{ flex: 1; position: relative; overflow: hidden; }}
svg {{ width: 100%; height: 100%; }}

/* tooltip */
.tooltip {{
  position: absolute; background: #1a1d27ee; border: 1px solid #2d3148;
  border-radius: 8px; padding: 10px 13px; font-size: 12px; color: #e2e8f0;
  pointer-events: none; opacity: 0; transition: opacity .15s;
  max-width: 240px; z-index: 100;
}}
.tooltip .tt-name {{ font-weight: 700; font-size: 13px; margin-bottom: 4px; }}
.tooltip .tt-row {{ display: flex; justify-content: space-between; gap: 10px; margin-bottom: 2px; }}
.tooltip .tt-key {{ color: #64748b; }}
.tooltip .tt-val {{ color: #f1f5f9; font-weight: 600; }}
.tooltip .tt-score {{ font-size: 15px; font-weight: 800; margin-top: 5px; }}
.tooltip .tt-hint {{ font-size: 10px; color: #475569; margin-top: 5px; }}
</style>
</head>
<body>

<!-- ── Sidebar ──────────────────────────────────────────────────── -->
<div id="sidebar">
  <h1>Semiconductor Supply Chain</h1>

  <div class="filter-section">
    <h2>Country</h2>
    <div id="country-filters"></div>
  </div>

  <div class="filter-section">
    <h2>Wave</h2>
    <div id="wave-filters"></div>
  </div>

  <div class="filter-section">
    <h2>Score ring</h2>
    <div class="legend-score"><div class="ring" style="border-color:#f59e0b"></div><label>≥ 62 — High conviction</label></div>
    <div class="legend-score"><div class="ring" style="border-color:#22c55e"></div><label>55–61 — Watchlist</label></div>
    <div class="legend-score"><div class="ring" style="border-color:#3b82f6"></div><label>45–54 — Monitor</label></div>
    <div class="legend-score"><div class="ring" style="border-color:#6b7280"></div><label>&lt; 45 / unscored</label></div>
  </div>

  <div class="filter-section">
    <h2>Edge type</h2>
    <div class="filter-row"><input type="checkbox" id="e-supplier" checked><label for="e-supplier">Supplier / Customer</label></div>
    <div class="filter-row"><input type="checkbox" id="e-competitor" checked><label for="e-competitor">Competitor</label></div>
    <div class="filter-row"><input type="checkbox" id="e-partner" checked><label for="e-partner">Partner</label></div>
    <div class="filter-row"><input type="checkbox" id="e-ecosystem" checked><label for="e-ecosystem">Ecosystem</label></div>
    <div style="margin-top:8px;font-size:10px;color:#475569;line-height:1.7">
      Hover a node to reveal direction:<br>
      <span style="color:#22c55e;font-weight:700">&#x2192;</span> outgoing (node supplies)<br>
      <span style="color:#f59e0b;font-weight:700">&#x2192;</span> incoming (node receives)
    </div>
  </div>

  <div id="stats">
    <span id="stat-nodes">Nodes: —</span>
    <span id="stat-edges">Edges: —</span>
    <span id="stat-visible">Visible: —</span>
  </div>
</div>

<!-- ── Detail panel ──────────────────────────────────────────────── -->
<div id="detail-panel">
  <div id="dp-inner">
    <div id="dp-header">
      <div class="title-block">
        <h2 id="dp-name">—</h2>
        <div class="sub" id="dp-sub">—</div>
      </div>
      <button id="dp-close" title="Close">✕</button>
    </div>
    <div id="dp-body"></div>
  </div>
</div>

<!-- ── Graph ──────────────────────────────────────────────────────── -->
<div id="graph">
  <svg id="svg"></svg>
  <div class="tooltip" id="tooltip"></div>
</div>

<script src="https://d3js.org/d3.v7.min.js"></script>
<script>
// ── Data ────────────────────────────────────────────────────────────
const NODES_DATA   = {nodes_js};
const EDGES_DATA   = {edges_js};
const DETAIL_MAP   = {detail_js};
const COUNTRY_CLR  = {country_colors_js};

const WAVE_LABELS = {{1:"Wave 1 – JP seed",2:"Wave 2 – Global",3:"Wave 3 – JP vendors",
                      4:"Wave 4 – OSAT/Foundry",5:"Wave 5 – Korea",6:"Wave 6 – China"}};
const EDGE_CLR = {{supplier:"#334155",competitor:"#7c3aed",partner:"#0e7490",ecosystem:"#065f46"}};

// ── Build filters ────────────────────────────────────────────────────
const countries = [...new Set(NODES_DATA.map(n=>n.country))].sort();
const countryDiv = document.getElementById('country-filters');
countries.forEach(c => {{
  const div = document.createElement('div'); div.className='filter-row';
  div.innerHTML = `<input type="checkbox" id="c-${{c}}" checked>
    <div class="dot" style="background:${{COUNTRY_CLR[c]||'#6b7280'}}"></div>
    <label for="c-${{c}}">${{c}}</label>`;
  countryDiv.appendChild(div);
}});

const waves = [...new Set(NODES_DATA.map(n=>n.wave))].sort((a,b)=>a-b);
const waveDiv = document.getElementById('wave-filters');
waves.forEach(w => {{
  const div = document.createElement('div'); div.className='filter-row';
  div.innerHTML = `<input type="checkbox" id="w-${{w}}" checked>
    <label for="w-${{w}}">${{WAVE_LABELS[w]||'Wave '+w}}</label>`;
  waveDiv.appendChild(div);
}});

// ── D3 setup ─────────────────────────────────────────────────────────
const svg = d3.select('#svg');
const container = document.getElementById('graph');
let W = container.clientWidth, H = container.clientHeight;
const g = svg.append('g');

// ── Arrow markers ─────────────────────────────────────────────────────────
const defs = svg.append('defs');
function mkArrow(id, color, sz) {{
  defs.append('marker')
    .attr('id', id).attr('viewBox','0 -4 8 8').attr('refX',8).attr('refY',0)
    .attr('markerWidth', sz||5).attr('markerHeight', sz||5).attr('orient','auto')
    .append('path').attr('d','M0,-4L8,0L0,4').attr('fill', color);
}}
mkArrow('arr-supp',   '#55677e', 5);   // default supplier edge (subtle)
mkArrow('arr-hl-out', '#22c55e', 8);   // hover: hovered node is the supplier
mkArrow('arr-hl-in',  '#f59e0b', 8);   // hover: hovered node is the customer

svg.attr('width', W).attr('height', H);

const zoom = d3.zoom().scaleExtent([0.05, 6])
  .on('zoom', e => g.attr('transform', e.transform));
svg.call(zoom);

const edgeLayer = g.append('g').attr('class','edges');
const nodeLayer = g.append('g').attr('class','nodes');

// ── Simulation ────────────────────────────────────────────────────────
const sim = d3.forceSimulation()
  .force('link', d3.forceLink().id(d=>d.id).distance(80).strength(0.4))
  .force('charge', d3.forceManyBody().strength(-280))
  .force('center', d3.forceCenter(W/2, H/2))
  .force('x', d3.forceX(W/2).strength(0.04))
  .force('y', d3.forceY(H/2).strength(0.04))
  .force('collision', d3.forceCollide().radius(d => (d.crit?18:12)+4));

// ── State ─────────────────────────────────────────────────────────────
let activeCid = null;
let nodeById = {{}};
let linkSel, nodeSel;

function getActiveCountries() {{
  return new Set(countries.filter(c=>{{
    const el = document.getElementById('c-'+c);
    return el && el.checked;
  }}));
}}
function getActiveWaves() {{
  return new Set(waves.filter(w=>{{
    const el = document.getElementById('w-'+w);
    return el && el.checked;
  }}));
}}
function getActiveEdgeTypes() {{
  const types = [];
  if (document.getElementById('e-supplier').checked) types.push('supplier');
  if (document.getElementById('e-competitor').checked) types.push('competitor');
  if (document.getElementById('e-partner').checked) types.push('partner');
  if (document.getElementById('e-ecosystem').checked) types.push('ecosystem');
  return new Set(types);
}}

function render() {{
  const ac = getActiveCountries();
  const aw = getActiveWaves();
  const ae = getActiveEdgeTypes();

  const visNodes = NODES_DATA.filter(n => ac.has(n.country) && aw.has(n.wave));
  const visIds = new Set(visNodes.map(n=>n.id));
  const visEdges = EDGES_DATA.filter(e => visIds.has(e.source.id||e.source) && visIds.has(e.target.id||e.target) && ae.has(e.type));

  nodeById = {{}};
  visNodes.forEach(n => nodeById[n.id] = n);

  document.getElementById('stat-nodes').textContent = `Nodes: ${{NODES_DATA.length}}`;
  document.getElementById('stat-edges').textContent = `Edges: ${{EDGES_DATA.length}}`;
  document.getElementById('stat-visible').textContent = `Visible: ${{visNodes.length}} nodes, ${{visEdges.length}} edges`;

  // edges
  linkSel = edgeLayer.selectAll('path.edge').data(visEdges, d=>`${{d.source.id||d.source}}-${{d.target.id||d.target}}-${{d.type}}`);
  linkSel.exit().remove();
  const linkEnter = linkSel.enter().append('path').attr('class','edge')
    .attr('fill','none')
    .attr('stroke-width', d => d.type==='supplier'?1.5:1.5)
    .attr('stroke-opacity', d => d.type==='supplier'?0.3:0.5)
    .attr('stroke-dasharray', d => d.type!=='supplier'?'4,3':null)
    .attr('marker-end', d => d.type==='supplier'?'url(#arr-supp)':null);
  linkSel = linkEnter.merge(linkSel)
    .attr('stroke', d => EDGE_CLR[d.type]||'#334155');

  // nodes
  nodeSel = nodeLayer.selectAll('g.node').data(visNodes, d=>d.id);
  nodeSel.exit().remove();
  const nodeEnter = nodeSel.enter().append('g').attr('class','node').style('cursor','pointer');

  // outer ring (score color)
  nodeEnter.append('circle').attr('class','ring-circle');
  // inner fill
  nodeEnter.append('circle').attr('class','fill-circle');
  // label
  nodeEnter.append('text').attr('class','node-label')
    .attr('text-anchor','middle').attr('dy','0.35em')
    .attr('pointer-events','none').style('user-select','none');

  nodeSel = nodeEnter.merge(nodeSel);

  nodeSel.select('.ring-circle')
    .attr('r', d => (d.crit?17:11)+2)
    .attr('fill','transparent')
    .attr('stroke', d => d.ring)
    .attr('stroke-width', d => d.crit?3:2);

  nodeSel.select('.fill-circle')
    .attr('r', d => d.crit?17:11)
    .attr('fill', d => COUNTRY_CLR[d.country]||'#6b7280')
    .attr('stroke', d => d.id===activeCid?'#fff':'none')
    .attr('stroke-width',3);

  nodeSel.select('.node-label')
    .attr('font-size', d => d.crit?7:6)
    .attr('fill','#fff')
    .attr('dy', d => (d.crit?17:11)+10)
    .text(d => d.ticker||d.name.split(' ')[0]);

  // interactions
  nodeSel
    .on('mouseover', (event,d) => {{ showTooltip(event,d); highlightEdges(d); }})
    .on('mousemove', (event) => moveTooltip(event))
    .on('mouseout', (event,d) => {{ hideTooltip(); unhighlightEdges(); }})
    .on('click', (event,d) => {{ event.stopPropagation(); togglePanel(d.id); }})
    .call(d3.drag()
      .on('start', (event,d) => {{ if(!event.active) sim.alphaTarget(.3).restart(); d.fx=d.x; d.fy=d.y; }})
      .on('drag',  (event,d) => {{ d.fx=event.x; d.fy=event.y; }})
      .on('end',   (event,d) => {{ if(!event.active) sim.alphaTarget(0); d.fx=null; d.fy=null; }})
    );

  svg.on('click', () => closePanel());

  sim.nodes(visNodes);
  sim.force('link').links(visEdges);
  sim.alpha(.8).restart();
  sim.on('tick', ticked);
}}

function ticked() {{
  if (linkSel) linkSel.attr('d', d => {{
    const dx = d.target.x - d.source.x, dy = d.target.y - d.source.y;
    const dist = Math.sqrt(dx*dx + dy*dy) || 1;
    const sr = (d.source.crit ? 17 : 11) + 2;
    const tr = (d.target.crit ? 17 : 11) + 2;
    const x1 = d.source.x + dx/dist * sr, y1 = d.source.y + dy/dist * sr;
    const x2 = d.target.x - dx/dist * tr, y2 = d.target.y - dy/dist * tr;
    return `M${{x1.toFixed(2)}},${{y1.toFixed(2)}}L${{x2.toFixed(2)}},${{y2.toFixed(2)}}`;
  }});
  if (nodeSel) nodeSel
    .attr('transform', d=>`translate(${{d.x}},${{d.y}})`);
}}

// ── Edge hover highlighting ──────────────────────────────────────────────
function highlightEdges(d) {{
  if (!linkSel) return;
  const hid = d.id;
  linkSel
    .attr('stroke-opacity', e => {{
      const sid = e.source.id||e.source, tid = e.target.id||e.target;
      return (sid===hid||tid===hid) ? 1 : 0.04;
    }})
    .attr('stroke', e => {{
      const sid = e.source.id||e.source, tid = e.target.id||e.target;
      if (e.type==='supplier') {{
        if (sid===hid) return '#22c55e';   // hovered node supplies to target
        if (tid===hid) return '#f59e0b';   // source supplies to hovered node
      }}
      if (sid===hid||tid===hid) return EDGE_CLR[e.type]||'#334155';
      return EDGE_CLR[e.type]||'#334155';
    }})
    .attr('stroke-width', e => {{
      const sid = e.source.id||e.source, tid = e.target.id||e.target;
      return (sid===hid||tid===hid) ? 2.5 : 1.5;
    }})
    .attr('marker-end', e => {{
      if (e.type!=='supplier') return null;
      const sid = e.source.id||e.source, tid = e.target.id||e.target;
      if (sid===hid) return 'url(#arr-hl-out)';
      if (tid===hid) return 'url(#arr-hl-in)';
      return null;
    }});
  if (nodeSel) nodeSel.style('opacity', n => {{
    if (n.id===hid) return 1;
    const conn = linkSel.data().some(e => {{
      const sid = e.source.id||e.source, tid = e.target.id||e.target;
      return (sid===hid&&tid===n.id)||(tid===hid&&sid===n.id);
    }});
    return conn ? 1 : 0.2;
  }});
}}

function unhighlightEdges() {{
  if (!linkSel) return;
  linkSel
    .attr('stroke-opacity', e => e.type==='supplier'?0.3:0.5)
    .attr('stroke', e => EDGE_CLR[e.type]||'#334155')
    .attr('stroke-width', () => 1.5)
    .attr('marker-end', e => e.type==='supplier'?'url(#arr-supp)':null);
  if (nodeSel) nodeSel.style('opacity', 1);
}}

// ── Tooltip ───────────────────────────────────────────────────────────
const tooltip = document.getElementById('tooltip');
function showTooltip(event, d) {{
  const sc = d.score!=null ? `<div class="tt-score" style="color:${{d.ring}}">${{d.score.toFixed(1)}}</div>` : '';
  const per = d.per!=null ? `<div class="tt-row"><span class="tt-key">PER</span><span class="tt-val">${{d.per.toFixed(1)}}x</span></div>` : '';
  const fo  = d.fo!=null  ? `<div class="tt-row"><span class="tt-key">Foreign own.</span><span class="tt-val">${{d.fo.toFixed(1)}}%</span></div>` : '';
  tooltip.innerHTML = `
    <div class="tt-name">${{d.name}}</div>
    <div class="tt-row"><span class="tt-key">Ticker</span><span class="tt-val">${{d.ticker||'—'}}</span></div>
    <div class="tt-row"><span class="tt-key">Country</span><span class="tt-val">${{d.country}}</span></div>
    ${{sc}}${{per}}${{fo}}
    <div class="tt-hint">Click to open investment card</div>`;
  tooltip.style.opacity = '1';
  moveTooltip(event);
}}
function moveTooltip(event) {{
  const r = container.getBoundingClientRect();
  let x = event.clientX - r.left + 14;
  let y = event.clientY - r.top + 14;
  if (x + 250 > W) x -= 270;
  tooltip.style.left = x+'px';
  tooltip.style.top  = y+'px';
}}
function hideTooltip() {{ tooltip.style.opacity='0'; }}

// ── Investment card panel ─────────────────────────────────────────────
const panel = document.getElementById('detail-panel');
document.getElementById('dp-close').addEventListener('click', e => {{ e.stopPropagation(); closePanel(); }});

function togglePanel(cid) {{
  if (activeCid === cid) {{ closePanel(); return; }}
  activeCid = cid;
  populateCard(DETAIL_MAP[cid]);
  panel.classList.add('open');
  // highlight node
  nodeSel && nodeSel.select('.fill-circle')
    .attr('stroke', d => d.id===cid?'#fff':'none');
}}

function closePanel() {{
  activeCid = null;
  panel.classList.remove('open');
  nodeSel && nodeSel.select('.fill-circle').attr('stroke','none');
}}

function goToNode(cid) {{
  const nd = nodeById[cid];
  if (!nd) return;
  const scale = 2.2;
  const tx = W/2 - scale*nd.x;
  const ty = H/2 - scale*nd.y;
  svg.transition().duration(600)
    .call(zoom.transform, d3.zoomIdentity.translate(tx,ty).scale(scale));
  togglePanel(cid);
}}

function fmt(v, suffix='', dp=1) {{
  if (v==null) return '—';
  return (+v).toFixed(dp) + suffix;
}}
function fmtCap(v) {{
  if (v==null) return '—';
  if (v>=1e12) return (v/1e12).toFixed(2)+'T ¥';
  if (v>=1e9)  return (v/1e9).toFixed(1)+'B ¥';
  return (v/1e6).toFixed(0)+'M ¥';
}}
function confClass(label) {{
  if (!label) return '';
  const l = label.toLowerCase();
  if (l.includes('very low')) return 'conf-vlow';
  if (l.includes('low'))      return 'conf-low';
  if (l.includes('medium')||l.includes('med')) return 'conf-med';
  if (l.includes('high'))     return 'conf-high';
  return '';
}}

function scGroup(title, arr) {{
  if (!arr || !arr.length) return '';
  const chips = arr.map(x =>
    `<span class="sc-chip" data-goto="${{x.id}}" title="${{x.label||x.name}}">${{x.name}}</span>`
  ).join('');
  return `<div class="sc-group">
    <div class="sc-group-label">${{title}} (${{arr.length}})</div>
    <div class="sc-list">${{chips}}</div>
  </div>`;
}}

function populateCard(d) {{
  if (!d) {{ document.getElementById('dp-body').innerHTML='<div style="padding:20px;color:#475569">No data</div>'; return; }}

  document.getElementById('dp-name').textContent = d.name;
  document.getElementById('dp-sub').textContent =
    [d.ticker, d.country, d.industry, 'Wave '+d.wave].filter(Boolean).join(' · ');

  // ── Score section ──
  const score = d.finalScore;
  const ringClr = score==null?'#6b7280':score>=62?'#f59e0b':score>=55?'#22c55e':score>=45?'#3b82f6':'#6b7280';
  const pct = score==null?0:Math.min(100,score);

  const DIM_META = {{
    A:{{label:'Valuation', max:30}}, B:{{label:'Moat', max:25}},
    C:{{label:'Growth',    max:15}}, D:{{label:'Ownership', max:10}},
    E:{{label:'Catalysts', max:10}}, F:{{label:'Risk', max:10}}
  }};
  const SUB_LABELS = {{
    A1_PER_discount:'PER Discount', A2_fwdPER_discount:'Fwd PER', A3_PBR_discount:'PBR Disc.',
    A4_earningsYield:'Earn. Yield',
    B1_marketShare:'Mkt Share', B2_switchingCosts:'Switch. Costs',
    B3_techDiff:'Tech Diff.', B4_chainCentrality:'Chain Cent.',
    C1_revenueGrowth:'Rev. Growth', C2_operatingMargin:'Op. Margin',
    C3_ROE:'ROE', C4_AIexposure:'AI Exposure',
    D1_foreignOwnershipGap:'Foreign Own. Gap', D2_floatDynamics:'Float Dyn.',
    D3_priceVs52W:'Price vs 52W',
    E1_analystConsensus:'Analyst Consens.', E2_capacityExpansion:'Capex Expan.',
    E3_policyTailwinds:'Policy Tailwinds',
    F1_forexSensitivity:'Forex Sensitiv.', F2_customerConcentration:'Cust. Concent.',
    F3_geopoliticalRisk:'Geo. Risk'
  }};

  let dimHtml = '<div class="dim-grid">';
  for (const [k, meta] of Object.entries(DIM_META)) {{
    const dim = d.dims[k] || {{}};
    const ds  = dim.score != null ? (+dim.score).toFixed(1) : '—';
    const barPct = dim.score != null ? Math.min(100, (dim.score / meta.max) * 100) : 0;
    const barClr = dim.score == null ? '#334155'
                 : barPct >= 70 ? '#22c55e' : barPct >= 40 ? '#3b82f6' : '#ef4444';
    const subs = dim.subs || {{}};
    const subRows = Object.entries(subs)
      .filter(([,v]) => v != null)
      .map(([k,v]) => `<div class="sub-row">
        <span class="sub-key">${{SUB_LABELS[k]||k}}</span>
        <span class="sub-val">${{v}}</span></div>`)
      .join('');
    dimHtml += `<div class="dim-cell" title="${{dim.note||''}}">
      <div class="dim-label">${{k}} · ${{meta.label}}</div>
      <div class="dim-score">${{ds}}<span class="dim-max">/${{meta.max}}</span></div>
      <div class="dim-bar-bg"><div class="dim-bar-fill" style="width:${{barPct.toFixed(1)}}%;background:${{barClr}}"></div></div>
      ${{subRows ? `<div class="dim-subs">${{subRows}}</div>` : ''}}
    </div>`;
  }}
  dimHtml += '</div>';

  const confBadge = d.confidence
    ? `<span class="conf-badge ${{confClass(d.confidence)}}">${{d.confidence}}</span>` : '';

  const scoreHtml = `<div class="card-section">
    <h3>Investment Score</h3>
    <div class="score-bar-wrap">
      <div class="score-num" style="color:${{ringClr}}">${{score!=null?score.toFixed(1):'—'}}</div>
      <div class="score-meta">Raw composite: ${{d.rawComposite!=null?d.rawComposite.toFixed(1):'—'}} &nbsp;·&nbsp;
        Conf. mult.: ${{d.confidenceMult!=null?d.confidenceMult.toFixed(2):'—'}} &nbsp;·&nbsp;
        Data coverage: ${{d.dataCoverage!=null?d.dataCoverage.toFixed(0)+'%':(d.researchComplete!=null?d.researchComplete.toFixed(0)+'%':'—')}}</div>
      <div class="bar-bg"><div class="bar-fill" style="width:${{pct}}%;background:${{ringClr}}"></div></div>
      ${{confBadge}}
    </div>
    ${{dimHtml}}
  </div>`;

  // ── Thesis ──
  const thesisHtml = d.investmentThesis ? `<div class="card-section">
    <h3>Investment Thesis</h3>
    <div class="thesis-text">${{d.investmentThesis.replace(/\\n/g,'<br>')}}</div>
  </div>` : '';

  // ── Financials ──
  const rows = [
    ['Market cap',       fmtCap(d.marketCapInYen)],
    ['Price (¥)',        fmt(d.latestPriceYen,'',0)],
    ['52W High/Low (¥)', d.weekHigh52!=null&&d.weekLow52!=null ? fmt(d.weekHigh52,'',0)+' / '+fmt(d.weekLow52,'',0) : '—'],
    ['PER',              fmt(d.PER,'x')],
    ['Forward PER',      fmt(d.forwardPER,'x')],
    ['PBR',              fmt(d.PBR,'x')],
    ['EPS (¥)',          fmt(d.EPS,'',2)],
    ['ROE',              fmt(d.ROE,'%')],
    ['Revenue growth',   fmt(d.revenueGrowth,'%')],
    ['Op. margin',       fmt(d.OPM,'%')],
    ['Dividend yield',   fmt(d.dividendYield,'%')],
    ['Foreign ownership',fmt(d.foreignOwnership,'%')],
    ['China revenue',    fmt(d.chinaRevenue,'%')],
    ['Forex sensitive',  d.forexSensitive!=null?(d.forexSensitive?'Yes':'No'):'—'],
    ['Buyback active',   d.hasBuyback!=null?(d.hasBuyback?'Yes':'No'):'—'],
    ['Analyst Buy/Hold/Sell',
      (d.analystBuy!=null||d.analystHold!=null||d.analystSell!=null)
        ? [d.analystBuy,d.analystHold,d.analystSell].map(v=>v??'—').join(' / ')
        : '—'],
  ];
  const finRows = rows.map(([k,v]) =>
    `<tr><td>${{k}}</td><td>${{v}}</td></tr>`).join('');
  const finHtml = `<div class="card-section">
    <h3>Financial Data</h3>
    <table class="fin-table">${{finRows}}</table>
  </div>`;

  // ── Supply chain position ──
  const scHtml = `<div class="card-section">
    <h3>Supply Chain Position</h3>
    ${{scGroup('Suppliers', d.suppliers)}}
    ${{scGroup('Clients', d.clients)}}
    ${{scGroup('Competitors', d.competitors)}}
    ${{scGroup('Partners', d.partners)}}
    ${{scGroup('Ecosystem', d.ecosystem)}}
  </div>`;

  // ── Company profile ──
  const websiteLink = d.website
    ? `<a class="website-link" href="${{d.website}}" target="_blank">${{d.website}}</a>` : '';
  const profileHtml = `<div class="card-section">
    <h3>Company Profile</h3>
    ${{websiteLink}}
    <div class="desc-text">${{d.description||''}}</div>
  </div>`;

  document.getElementById('dp-body').innerHTML =
    scoreHtml + thesisHtml + finHtml + scHtml + profileHtml;

  // bind SC chip clicks
  document.querySelectorAll('#dp-body .sc-chip[data-goto]').forEach(chip => {{
    chip.addEventListener('click', e => {{
      e.stopPropagation();
      goToNode(chip.dataset.goto);
    }});
  }});
}}

// ── Filter listeners ──────────────────────────────────────────────────
document.querySelectorAll('#country-filters input, #wave-filters input, #sidebar input[type=checkbox]')
  .forEach(el => el.addEventListener('change', render));

// ── Resize ────────────────────────────────────────────────────────────
window.addEventListener('resize', () => {{
  W = container.clientWidth; H = container.clientHeight;
  svg.attr('width', W).attr('height', H);
  sim.force('center', d3.forceCenter(W/2, H/2)).alpha(.3).restart();
}});

// ── Init ─────────────────────────────────────────────────────────────
render();
</script>
</body>
</html>"""
    return html


def main():
    print("Loading data...")
    graph, eval_map, comp_map, eval_data = load_data()

    print(f"  Graph: {len(graph['nodes'])} nodes, {len(graph['edges'])} edges")
    print(f"  Eval map: {len(eval_map)} companies")
    print(f"  Company files: {len(comp_map)} files")

    print("Building JS data...")
    nodes_js  = build_node_js(graph, eval_map, comp_map)
    edges_js  = build_edge_js(graph)
    detail_js = build_detail_map(graph, eval_map, comp_map)

    print("Generating HTML...")
    html = generate_html(nodes_js, edges_js, detail_js, COUNTRY_COLORS)

    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    size_kb = os.path.getsize(OUT_FILE) // 1024
    print(f"Written {OUT_FILE}  ({size_kb} KB)")


if __name__ == "__main__":
    main()
