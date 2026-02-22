"""
Initialization script for evaluation_progress.json.
Scores Dimensions B, C4, E2, E3, F from existing data.
Marks A, C1-C3, D, E1 as pending research.
"""

import json
import os
from datetime import date

DATA_DIR = "data/companies"
GRAPH_FILE = "data/graph.json"
OUTPUT_FILE = "evaluation_progress.json"

# ── Peer group assignments ────────────────────────────────────────────────────
PEER_GROUPS = {
    # G1: Semiconductor Equipment (25)
    "CMP-0001": "G1", "CMP-0002": "G1", "CMP-0003": "G1", "CMP-0004": "G1",
    "CMP-0005": "G1", "CMP-0006": "G1", "CMP-0011": "G1", "CMP-0012": "G1",
    "CMP-0026": "G1", "CMP-0029": "G1", "CMP-0030": "G1", "CMP-0036": "G1",
    "CMP-0041": "G1", "CMP-0042": "G1", "CMP-0043": "G1", "CMP-0050": "G1",
    "CMP-0051": "G1", "CMP-0052": "G1", "CMP-0053": "G1", "CMP-0054": "G1",
    "CMP-0056": "G1", "CMP-0059": "G1", "CMP-0060": "G1", "CMP-0061": "G1",
    "CMP-0062": "G1",
    # G2: Semiconductor Materials (26)
    "CMP-0007": "G2", "CMP-0008": "G2", "CMP-0009": "G2", "CMP-0010": "G2",
    "CMP-0013": "G2", "CMP-0015": "G2", "CMP-0024": "G2", "CMP-0025": "G2",
    "CMP-0031": "G2", "CMP-0032": "G2", "CMP-0033": "G2", "CMP-0034": "G2",
    "CMP-0035": "G2", "CMP-0037": "G2", "CMP-0038": "G2", "CMP-0039": "G2",
    "CMP-0040": "G2", "CMP-0044": "G2", "CMP-0045": "G2", "CMP-0046": "G2",
    "CMP-0047": "G2", "CMP-0048": "G2", "CMP-0049": "G2", "CMP-0055": "G2",
    "CMP-0057": "G2", "CMP-0058": "G2",
    # G3: Semiconductors + Memory (6)
    "CMP-0014": "G3", "CMP-0018": "G3", "CMP-0019": "G3",
    "CMP-0020": "G3", "CMP-0021": "G3", "CMP-0028": "G3",
    # G4: Other (5)
    "CMP-0016": "G4", "CMP-0017": "G4", "CMP-0022": "G4",
    "CMP-0023": "G4", "CMP-0027": "G4",
}

# ── B-dimension pre-scored values ─────────────────────────────────────────────
# B1: market share (0-10), B2: switching costs (0-5), B3: tech diff (0-5)
# B4 derived from graph data
B_MANUAL = {
    # id: (B1, B2, B3)  — B4 computed from graph
    "CMP-0001": (8,  4, 4),   # ACCRETECH: 46% probing, high qual, unique tech
    "CMP-0002": (8,  3, 4),   # DISCO: 70% dicing, moderate sw cost, blade IP
    "CMP-0003": (8,  4, 4),   # SCREEN: #1 cleaning, integrated, cleaning IP
    "CMP-0004": (8,  5, 4),   # TEL: oligopoly coater/dev, multi-year qual
    "CMP-0005": (8,  5, 4),   # Advantest: 60-70% memory test, platform lock
    "CMP-0006": (10, 5, 5),   # Lasertec: 100% EUV mask inspection, unique
    "CMP-0007": (8,  4, 4),   # Fujimi: 90%+ wafer polish + 18% CMP slurry
    "CMP-0008": (8,  3, 3),   # Resonac: #1 materials overall, competitive
    "CMP-0009": (4,  3, 3),   # Ferrotec: specialty parts, moderate
    "CMP-0010": (8,  5, 5),   # Toyo Gosei: 60-70% EUV photosensitive, unique
    "CMP-0011": (8,  5, 4),   # Kokusai: 70% batch ALD, long qual, unique
    "CMP-0012": (6,  4, 4),   # Horiba: 30%+ MFC, process-critical
    "CMP-0013": (10, 5, 5),   # Fuso: 90% semiconductor colloidal silica, unique
    "CMP-0014": (4,  3, 3),   # Kioxia: 14% NAND, competitive
    "CMP-0015": (8,  5, 4),   # HOYA: 60%+ blanks, 75%+ EUV blanks, lock-in
    "CMP-0016": (8,  4, 4),   # Olympus: #1 endoscopes (medical, not semicond)
    "CMP-0017": (10, 5, 5),   # TSMC: 90%+ advanced, unique capability
    "CMP-0018": (8,  3, 4),   # Samsung: #1 memory, HBM
    "CMP-0019": (6,  3, 3),   # Intel: IDM, x86 legacy
    "CMP-0020": (8,  5, 4),   # SK Hynix: 50%+ HBM, NVIDIA-specific design
    "CMP-0021": (6,  3, 3),   # Micron: #3 memory
    "CMP-0022": (4,  5, 5),   # Apple: customer, strong design (different role)
    "CMP-0023": (4,  2, 3),   # WDC: HDD+NAND, commodity
    "CMP-0024": (8,  5, 4),   # Shin-Etsu: 42% wafer, yield-critical
    "CMP-0025": (6,  4, 3),   # SUMCO: 20% wafer, duopoly
    "CMP-0026": (10, 5, 5),   # ASML: 100% EUV, impossible to replace
    "CMP-0027": (4,  3, 3),   # Kyocera: ceramic packages, moderate
    "CMP-0028": (10, 5, 5),   # NVIDIA: 85-90% AI GPU, CUDA lock-in
    "CMP-0029": (2,  3, 2),   # Naigai Tech: niche TEL supplier
    "CMP-0030": (2,  3, 3),   # Marumae: precision parts, clean cert
    "CMP-0031": (6,  4, 4),   # Tocalo: Japan #1 thermal spray, specialized
    "CMP-0032": (6,  3, 3),   # Nippon Sanso: world top 3 gases
    "CMP-0033": (6,  5, 4),   # TOK: 25% photoresist, EUV chemistry
    "CMP-0034": (8,  5, 4),   # JSR: #1 ArF, top 2, strong IP
    "CMP-0035": (10, 5, 5),   # Maruzen Petrochem: world #1 photoresist polymer
    "CMP-0036": (6,  3, 3),   # Ebara: #2 CMP, #2 vacuum pumps
    "CMP-0037": (4,  4, 4),   # NGK: AlN ceramic heaters, specialized
    "CMP-0038": (6,  4, 3),   # Gun Ei: high share photoresist polymer
    "CMP-0039": (4,  4, 3),   # Niterra: ceramic ESC (NTK Ceratec)
    "CMP-0040": (8,  4, 4),   # FUJIFILM: #1 copper CMP slurry, 5T target
    "CMP-0041": (6,  4, 4),   # Rorze: world top-class wafer transfer
    "CMP-0042": (10, 5, 5),   # PILLAR: 90% cleaning fittings, fluororesin
    "CMP-0043": (4,  3, 2),   # CKD: pneumatic valves, standard
    "CMP-0044": (10, 5, 5),   # Stella Chemifa: world monopoly 12-nine HF
    "CMP-0045": (6,  3, 4),   # Kanto Denka: 15+ gas types, unique breadth
    "CMP-0046": (4,  4, 3),   # Sumitomo Chemical: photoresist full lineup
    "CMP-0047": (6,  4, 4),   # TOPPAN: world-leading photomask, IBM JV
    "CMP-0048": (8,  5, 4),   # Ibiden: 50%+ AI server IC substrates
    "CMP-0049": (4,  4, 3),   # DNP: photomask + lead frames
    "CMP-0050": (2,  3, 2),   # Nikon: 5.7% ArF, declining
    "CMP-0051": (4,  3, 4),   # Canon: NIL pioneer, early stage
    "CMP-0052": (10, 5, 4),   # Organo: nearly exclusive TSMC UPW
    "CMP-0053": (4,  3, 3),   # Nomura Micro: UPW specialist, Korea
    "CMP-0054": (2,  3, 2),   # Aval Data: image boards
    "CMP-0055": (8,  4, 3),   # NHK Spring: 50% HDD suspension
    "CMP-0056": (10, 5, 4),   # Daifuku: near-monopoly advanced AMHS
    "CMP-0057": (6,  4, 4),   # MEC: world standard copper roughening
    "CMP-0058": (2,  3, 2),   # Nagase: trading + specialty resins
    "CMP-0059": (6,  4, 4),   # Shibaura: #1 post-polish cleaning
    "CMP-0060": (4,  3, 3),   # Samco: PECVD pioneer
    "CMP-0061": (8,  4, 4),   # Ushio: 75% i-line UV lamps
    "CMP-0062": (4,  3, 2),   # Tazmo: coating equipment
}

# ── C4: AI/advanced-node exposure (0-3) ─────────────────────────────────────
C4_SCORES = {
    "CMP-0001": 3, "CMP-0002": 3, "CMP-0003": 3, "CMP-0004": 3,
    "CMP-0005": 3, "CMP-0006": 3, "CMP-0007": 3, "CMP-0008": 2,
    "CMP-0009": 2, "CMP-0010": 3, "CMP-0011": 3, "CMP-0012": 2,
    "CMP-0013": 3, "CMP-0014": 2, "CMP-0015": 3, "CMP-0016": 0,
    "CMP-0017": 3, "CMP-0018": 3, "CMP-0019": 2, "CMP-0020": 3,
    "CMP-0021": 3, "CMP-0022": 2, "CMP-0023": 3, "CMP-0024": 2,
    "CMP-0025": 2, "CMP-0026": 3, "CMP-0027": 1, "CMP-0028": 3,
    "CMP-0029": 2, "CMP-0030": 2, "CMP-0031": 2, "CMP-0032": 2,
    "CMP-0033": 3, "CMP-0034": 3, "CMP-0035": 3, "CMP-0036": 2,
    "CMP-0037": 1, "CMP-0038": 3, "CMP-0039": 2, "CMP-0040": 3,
    "CMP-0041": 2, "CMP-0042": 3, "CMP-0043": 2, "CMP-0044": 3,
    "CMP-0045": 2, "CMP-0046": 3, "CMP-0047": 3, "CMP-0048": 3,
    "CMP-0049": 3, "CMP-0050": 1, "CMP-0051": 3, "CMP-0052": 3,
    "CMP-0053": 2, "CMP-0054": 1, "CMP-0055": 2, "CMP-0056": 3,
    "CMP-0057": 3, "CMP-0058": 3, "CMP-0059": 2, "CMP-0060": 2,
    "CMP-0061": 2, "CMP-0062": 2,
}

# ── E2: Capacity expansion (0-3) ─────────────────────────────────────────────
E2_SCORES = {
    "CMP-0001": 2, "CMP-0002": 2, "CMP-0003": 2, "CMP-0004": 3,
    "CMP-0005": 3, "CMP-0006": 2, "CMP-0007": 2, "CMP-0008": 2,
    "CMP-0009": 1, "CMP-0010": 3, "CMP-0011": 3, "CMP-0012": 2,
    "CMP-0013": 3, "CMP-0014": 3, "CMP-0015": 2, "CMP-0016": 2,
    "CMP-0017": 3, "CMP-0018": 3, "CMP-0019": 3, "CMP-0020": 3,
    "CMP-0021": 3, "CMP-0022": 3, "CMP-0023": 3, "CMP-0024": 2,
    "CMP-0025": 1, "CMP-0026": 3, "CMP-0027": 2, "CMP-0028": 3,
    "CMP-0029": 1, "CMP-0030": 2, "CMP-0031": 2, "CMP-0032": 3,
    "CMP-0033": 3, "CMP-0034": 2, "CMP-0035": 3, "CMP-0036": 2,
    "CMP-0037": 1, "CMP-0038": 3, "CMP-0039": 3, "CMP-0040": 3,
    "CMP-0041": 2, "CMP-0042": 3, "CMP-0043": 2, "CMP-0044": 3,
    "CMP-0045": 3, "CMP-0046": 3, "CMP-0047": 3, "CMP-0048": 3,
    "CMP-0049": 3, "CMP-0050": 2, "CMP-0051": 3, "CMP-0052": 3,
    "CMP-0053": 2, "CMP-0054": 1, "CMP-0055": 2, "CMP-0056": 3,
    "CMP-0057": 2, "CMP-0058": 3, "CMP-0059": 2, "CMP-0060": 2,
    "CMP-0061": 2, "CMP-0062": 1,
}

# ── E3: Policy/macro tailwinds (0-3) ─────────────────────────────────────────
E3_SCORES = {
    "CMP-0001": 2, "CMP-0002": 2, "CMP-0003": 2, "CMP-0004": 2,
    "CMP-0005": 2, "CMP-0006": 1, "CMP-0007": 3, "CMP-0008": 2,
    "CMP-0009": 2, "CMP-0010": 3, "CMP-0011": 1, "CMP-0012": 2,
    "CMP-0013": 3, "CMP-0014": 2, "CMP-0015": 3, "CMP-0016": 1,
    "CMP-0017": 3, "CMP-0018": 2, "CMP-0019": 3, "CMP-0020": 3,
    "CMP-0021": 3, "CMP-0022": 2, "CMP-0023": 2, "CMP-0024": 3,
    "CMP-0025": 3, "CMP-0026": 1, "CMP-0027": 2, "CMP-0028": 3,
    "CMP-0029": 2, "CMP-0030": 2, "CMP-0031": 3, "CMP-0032": 3,
    "CMP-0033": 3, "CMP-0034": 3, "CMP-0035": 3, "CMP-0036": 2,
    "CMP-0037": 2, "CMP-0038": 3, "CMP-0039": 3, "CMP-0040": 3,
    "CMP-0041": 2, "CMP-0042": 3, "CMP-0043": 2, "CMP-0044": 3,
    "CMP-0045": 3, "CMP-0046": 3, "CMP-0047": 3, "CMP-0048": 2,
    "CMP-0049": 3, "CMP-0050": 2, "CMP-0051": 3, "CMP-0052": 3,
    "CMP-0053": 2, "CMP-0054": 2, "CMP-0055": 2, "CMP-0056": 3,
    "CMP-0057": 3, "CMP-0058": 3, "CMP-0059": 2, "CMP-0060": 2,
    "CMP-0061": 2, "CMP-0062": 1,
}

# ── F1: Forex sensitivity (0-3, higher = lower risk) ─────────────────────────
# Based on isForexSensitive + company size
F1_SCORES = {
    # Large/well-hedged exporters: 1; Fuso Chemical (domestic): 3
    "CMP-0001": 1, "CMP-0002": 1, "CMP-0003": 1, "CMP-0004": 1,
    "CMP-0005": 1, "CMP-0006": 1, "CMP-0007": 1, "CMP-0008": 1,
    "CMP-0009": 1, "CMP-0010": 1, "CMP-0011": 1, "CMP-0012": 1,
    "CMP-0013": 3,  # domestic, isForexSensitive=false
    "CMP-0014": 1, "CMP-0015": 1, "CMP-0016": 1,
    "CMP-0017": 0,  # TWD/USD revenue, JPY not base currency
    "CMP-0018": 0, "CMP-0019": 0, "CMP-0020": 0,
    "CMP-0021": 0, "CMP-0022": 0, "CMP-0023": 0,
    "CMP-0024": 1, "CMP-0025": 1, "CMP-0026": 0,
    "CMP-0027": 1, "CMP-0028": 0,
    "CMP-0029": 1, "CMP-0030": 1, "CMP-0031": 1, "CMP-0032": 1,
    "CMP-0033": 1, "CMP-0034": 1, "CMP-0035": 1, "CMP-0036": 1,
    "CMP-0037": 1, "CMP-0038": 1, "CMP-0039": 1, "CMP-0040": 1,
    "CMP-0041": 1, "CMP-0042": 1, "CMP-0043": 1, "CMP-0044": 1,
    "CMP-0045": 1, "CMP-0046": 1, "CMP-0047": 1, "CMP-0048": 1,
    "CMP-0049": 1, "CMP-0050": 1, "CMP-0051": 1, "CMP-0052": 1,
    "CMP-0053": 1, "CMP-0054": 1, "CMP-0055": 1, "CMP-0056": 1,
    "CMP-0057": 1, "CMP-0058": 1, "CMP-0059": 1, "CMP-0060": 1,
    "CMP-0061": 1, "CMP-0062": 1,
}

# ── F2: Customer concentration (0-4, higher = lower concentration) ───────────
F2_SCORES = {
    "CMP-0001": 3, "CMP-0002": 4, "CMP-0003": 3, "CMP-0004": 3,
    "CMP-0005": 2, "CMP-0006": 1, "CMP-0007": 3, "CMP-0008": 3,
    "CMP-0009": 3, "CMP-0010": 2, "CMP-0011": 2, "CMP-0012": 3,
    "CMP-0013": 3, "CMP-0014": 2, "CMP-0015": 3, "CMP-0016": 4,
    "CMP-0017": 3, "CMP-0018": 3, "CMP-0019": 4, "CMP-0020": 1,
    "CMP-0021": 2, "CMP-0022": 3, "CMP-0023": 3, "CMP-0024": 4,
    "CMP-0025": 3, "CMP-0026": 3, "CMP-0027": 4, "CMP-0028": 3,
    "CMP-0029": 0, "CMP-0030": 1, "CMP-0031": 2, "CMP-0032": 3,
    "CMP-0033": 3, "CMP-0034": 3, "CMP-0035": 2, "CMP-0036": 3,
    "CMP-0037": 2, "CMP-0038": 2, "CMP-0039": 2, "CMP-0040": 3,
    "CMP-0041": 2, "CMP-0042": 2, "CMP-0043": 2, "CMP-0044": 3,
    "CMP-0045": 3, "CMP-0046": 3, "CMP-0047": 3, "CMP-0048": 1,
    "CMP-0049": 3, "CMP-0050": 2, "CMP-0051": 2, "CMP-0052": 0,
    "CMP-0053": 2, "CMP-0054": 2, "CMP-0055": 2, "CMP-0056": 3,
    "CMP-0057": 2, "CMP-0058": 2, "CMP-0059": 2, "CMP-0060": 3,
    "CMP-0061": 3, "CMP-0062": 2,
}

# ── F3: Geopolitical risk (0-3, higher = lower risk) ─────────────────────────
F3_SCORES = {
    "CMP-0001": 0, "CMP-0002": 2, "CMP-0003": 1, "CMP-0004": 1,
    "CMP-0005": 2, "CMP-0006": 2, "CMP-0007": 2, "CMP-0008": 2,
    "CMP-0009": 1, "CMP-0010": 2, "CMP-0011": 1, "CMP-0012": 2,
    "CMP-0013": 2, "CMP-0014": 2, "CMP-0015": 2, "CMP-0016": 3,
    "CMP-0017": 0, "CMP-0018": 1, "CMP-0019": 2, "CMP-0020": 2,
    "CMP-0021": 2, "CMP-0022": 1, "CMP-0023": 2, "CMP-0024": 2,
    "CMP-0025": 2, "CMP-0026": 1, "CMP-0027": 2, "CMP-0028": 2,
    "CMP-0029": 3, "CMP-0030": 3, "CMP-0031": 2, "CMP-0032": 2,
    "CMP-0033": 2, "CMP-0034": 2, "CMP-0035": 3, "CMP-0036": 2,
    "CMP-0037": 2, "CMP-0038": 3, "CMP-0039": 2, "CMP-0040": 2,
    "CMP-0041": 1, "CMP-0042": 2, "CMP-0043": 2, "CMP-0044": 2,
    "CMP-0045": 2, "CMP-0046": 2, "CMP-0047": 2, "CMP-0048": 2,
    "CMP-0049": 2, "CMP-0050": 1, "CMP-0051": 3, "CMP-0052": 0,
    "CMP-0053": 1, "CMP-0054": 3, "CMP-0055": 2, "CMP-0056": 2,
    "CMP-0057": 2, "CMP-0058": 2, "CMP-0059": 2, "CMP-0060": 3,
    "CMP-0061": 2, "CMP-0062": 2,
}

# ── Load graph data ───────────────────────────────────────────────────────────
with open(GRAPH_FILE, "r", encoding="utf-8") as f:
    graph = json.load(f)

CRITICAL_NODES = {n["id"] for n in graph.get("criticalNodes", [])}

# Compute degree (supplier edges only to match framework intent)
degree = {}
for edge in graph["edges"]:
    if edge["type"] == "supplier":
        degree[edge["source"]] = degree.get(edge["source"], 0) + 1
        degree[edge["target"]] = degree.get(edge["target"], 0) + 1

def b4_score(cid):
    if cid in CRITICAL_NODES:
        return 5
    d = degree.get(cid, 0)
    if d >= 10: return 4
    if d >= 6:  return 3
    if d >= 3:  return 2
    return 1

# ── Load all company JSON files ───────────────────────────────────────────────
companies_raw = {}
for fname in sorted(os.listdir(DATA_DIR)):
    if fname.endswith(".json"):
        cid = fname.replace(".json", "")
        with open(os.path.join(DATA_DIR, fname), "r", encoding="utf-8") as f:
            companies_raw[cid] = json.load(f)

# ── Helper: extract known financial data ─────────────────────────────────────
def extract_known_data(c):
    """Extract whatever financial data already exists in the company JSON."""
    return {
        "PER": c.get("PER"),
        "forwardPER": None,
        "PBR": c.get("PBR"),
        "EPS": c.get("EPS"),
        "ROE": None,
        "marketCapInYen": c.get("marketCapInYen"),
        "marketCapUSD": c.get("marketCapUSD"),
        "latestPriceYen": c.get("latestPriceYen"),
        "latestPriceLocal": (
            c.get("latestPriceTWD") or c.get("latestPriceKRW") or
            c.get("latestPriceUSD") or c.get("latestPriceEUR")
        ),
        "localCurrency": (
            "TWD" if c.get("latestPriceTWD") else
            "KRW" if c.get("latestPriceKRW") else
            "USD" if c.get("latestPriceUSD") else
            "EUR" if c.get("latestPriceEUR") else None
        ),
        "weekHigh52": None,
        "weekLow52": None,
        "revenueLatestFY_JPY_B": None,    # in billions JPY
        "revenueGrowthYoY_pct": None,
        "operatingMargin_pct": None,
        "dividendYield_pct": None,
        "foreignOwnership_pct": c.get("percentOfForeignOwnership"),
        "circulatingEquity_pct": c.get("percentOfCirculatingEquity"),
        "analystBuy": None,
        "analystHold": None,
        "analystSell": None,
        "analystAvgTarget_local": None,
        "isForexSensitive": c.get("isForexSensitive"),
        "chinaRevenue_pct_est": None,
        "topCustomerRev_pct_est": None,
        "hasBuyback": None,
    }

# Patch known data from metadata notes
KNOWN_PATCHES = {
    # id: dict of fields to override
    "CMP-0001": {
        "revenueLatestFY_JPY_B": 150.5,
        "revenueGrowthYoY_pct": 11.8,
        "weekHigh52": 16170, "weekLow52": 6148,
        "chinaRevenue_pct_est": 34,
    },
    "CMP-0002": {
        "weekHigh52": 76890, "weekLow52": 22640,
        "dividendYield_pct": 0.57,
        "analystBuy": 12,
    },
    "CMP-0004": {
        "revenueLatestFY_JPY_B": 2600.0,   # FY2026 forecast
        "revenueGrowthYoY_pct": 6.9,
        "operatingMargin_pct": 31.24,       # EBITDA margin as proxy
        "dividendYield_pct": 1.27,
        "chinaRevenue_pct_est": 30,
    },
    "CMP-0005": {
        "revenueLatestFY_JPY_B": 1070.0,   # FY2026 guidance
    },
    "CMP-0007": {
        "revenueGrowthYoY_pct": 21.5,
    },
    "CMP-0008": {
        "operatingMargin_pct": 17.46,      # EBITDA margin proxy
    },
    "CMP-0011": {
        "revenueLatestFY_JPY_B": 238.93,
        "revenueGrowthYoY_pct": 32.0,
    },
    "CMP-0012": {
        "operatingMargin_pct": 19.35,
    },
    "CMP-0014": {
        "analystBuy": 9,
        "analystAvgTarget_local": 26525,   # JPY
    },
    "CMP-0015": {
        "weekHigh52": 28000, "weekLow52": 14345,
        "analystBuy": 12,
    },
    "CMP-0016": {
        "operatingMargin_pct": 25.32,
    },
    "CMP-0024": {
        "analystBuy": 13,
    },
    "CMP-0025": {
        "weekHigh52": 1790, "weekLow52": 745,
    },
}

# ── Market cap tier ───────────────────────────────────────────────────────────
def market_cap_tier(cid, c):
    mc = c.get("marketCapInYen")
    if mc:
        if mc > 1_000_000_000_000:   return "Large"
        if mc > 100_000_000_000:     return "Mid"
        return "Small"
    mc_usd = c.get("marketCapUSD")
    if mc_usd:
        mc_jpy = mc_usd * 150  # approximate
        if mc_jpy > 1_000_000_000_000:  return "Large"
        if mc_jpy > 100_000_000_000:    return "Mid"
        return "Small"
    return "Unknown"

# ── Build evaluation_progress.json ───────────────────────────────────────────
companies_out = []

for cid in sorted(companies_raw.keys()):
    c = companies_raw[cid]
    pg = PEER_GROUPS.get(cid, "G1")
    tier = market_cap_tier(cid, c)

    # Research data
    rd = extract_known_data(c)
    if cid in KNOWN_PATCHES:
        rd.update(KNOWN_PATCHES[cid])

    # Score B
    b1, b2, b3 = B_MANUAL.get(cid, (2, 2, 2))
    b4 = b4_score(cid)
    b_total = b1 + b2 + b3 + b4

    # Score C (partial — C1, C2, C3 pending; C4 scored)
    c4 = C4_SCORES.get(cid, 1)

    # Score E (E1 pending; E2, E3 scored)
    e2 = E2_SCORES.get(cid, 1)
    e3 = E3_SCORES.get(cid, 1)

    # Score F
    f1 = F1_SCORES.get(cid, 1)
    f2 = F2_SCORES.get(cid, 2)
    f3 = F3_SCORES.get(cid, 2)
    f_total = f1 + f2 + f3

    # Count how many research fields are already available
    research_fields = [
        "PER", "PBR", "EPS", "marketCapInYen", "latestPriceYen",
        "weekHigh52", "weekLow52", "revenueLatestFY_JPY_B",
        "revenueGrowthYoY_pct", "operatingMargin_pct", "foreignOwnership_pct",
        "circulatingEquity_pct", "analystBuy", "analystAvgTarget_local",
        "isForexSensitive",
    ]
    filled = sum(1 for k in research_fields if rd.get(k) is not None)
    research_pct = round(filled / len(research_fields) * 100, 1)

    entry = {
        "id": cid,
        "name": c.get("companyName"),
        "ticker": c.get("ticker"),
        "industryCode": c.get("industryCode"),
        "peerGroup": pg,
        "marketCapTier": tier,
        "researchStatus": "pending",
        "scoringStatus": "partial",
        "researchCompleteness_pct": research_pct,
        "researchData": rd,
        "scores": {
            "A": {
                "A1_PER_discount": None,
                "A2_fwdPER_discount": None,
                "A3_PBR_discount": None,
                "A4_earningsYield": None,
                "total": None,
                "note": "Pending: requires peer group medians after research sweep"
            },
            "B": {
                "B1_marketShare": b1,
                "B2_switchingCosts": b2,
                "B3_techDiff": b3,
                "B4_chainCentrality": b4,
                "total": b_total,
                "note": "Scored from company descriptions and graph.json"
            },
            "C": {
                "C1_revenueGrowth": None,
                "C2_operatingMargin": None,
                "C3_ROE": None,
                "C4_AIexposure": c4,
                "total": None,
                "note": "C1-C3 pending research; C4 scored from descriptions"
            },
            "D": {
                "D1_foreignOwnershipGap": None,
                "D2_floatDynamics": None,
                "D3_priceVs52W": None,
                "total": None,
                "note": "Pending: requires foreign ownership, float, 52W range"
            },
            "E": {
                "E1_analystConsensus": None,
                "E2_capacityExpansion": e2,
                "E3_policyTailwinds": e3,
                "total": None,
                "note": "E1 pending research; E2/E3 scored from descriptions"
            },
            "F": {
                "F1_forexSensitivity": f1,
                "F2_customerConcentration": f2,
                "F3_geopoliticalRisk": f3,
                "total": f_total,
                "note": "Scored from isForexSensitive, client arrays, descriptions"
            }
        },
        "rawComposite": None,
        "dataCoverage_pct": None,
        "confidenceMultiplier": None,
        "finalScore": None,
        "confidence": None,
        "notes": ""
    }

    companies_out.append(entry)

# ── Assemble final output ─────────────────────────────────────────────────────
output = {
    "version": "1.0",
    "created": str(date.today()),
    "lastUpdated": str(date.today()),
    "description": "Evaluation progress tracker — 0-100 undervalued score for 62 semiconductor supply chain companies",
    "scoringFramework": "EVALUATION_FRAMEWORK.md",
    "status": {
        "totalCompanies": len(companies_out),
        "researchComplete": 0,
        "scoringComplete": 0,
        "compositeRanked": False,
        "dimensionsFullyScored": ["B", "F"],
        "dimensionsPartiallyScored": ["C", "E"],
        "dimensionsPendingResearch": ["A", "D", "C1-C3", "E1"]
    },
    "peerGroupMedians": {
        "G1_Equipment":      {"PER": None, "PBR": None, "ROE_pct": None, "revenueGrowth_pct": None, "OPM_pct": None, "note": "To compute after research sweep"},
        "G2_Materials":      {"PER": None, "PBR": None, "ROE_pct": None, "revenueGrowth_pct": None, "OPM_pct": None, "note": "To compute after research sweep"},
        "G3_Semiconductors": {"PER": None, "PBR": None, "ROE_pct": None, "revenueGrowth_pct": None, "OPM_pct": None, "note": "To compute after research sweep"},
        "G4_Other":          {"PER": None, "PBR": None, "ROE_pct": None, "revenueGrowth_pct": None, "OPM_pct": None, "note": "To compute after research sweep"}
    },
    "jgb10yYield_pct": 1.5,   # approximate as of Feb 2026
    "usdJpyRate": 152.0,       # approximate as of Feb 2026
    "companies": companies_out
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

# ── Summary ───────────────────────────────────────────────────────────────────
b_scores = [(e["id"], e["scores"]["B"]["total"]) for e in companies_out]
b_scores.sort(key=lambda x: -x[1])
print(f"Created {OUTPUT_FILE} with {len(companies_out)} companies.")
print(f"\nTop 10 by Dimension B (Supply Chain Moat):")
for cid, score in b_scores[:10]:
    name = companies_raw[cid]["companyName"]
    b4 = companies_raw[cid].get("id", "")
    crit = "★ CRITICAL" if cid in CRITICAL_NODES else ""
    print(f"  {cid} [{score:2d}/25] {name} {crit}")

f_scores = [(e["id"], e["scores"]["F"]["total"]) for e in companies_out]
f_scores.sort(key=lambda x: -x[1])
print(f"\nTop 10 by Dimension F (Risk: lower risk → higher score):")
for cid, score in f_scores[:10]:
    name = companies_raw[cid]["companyName"]
    print(f"  {cid} [{score}/10] {name}")
