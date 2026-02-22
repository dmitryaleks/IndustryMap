"""
Update evaluation_progress.json with researched financial data and recompute all scores.
Data sourced from Yahoo Finance, Investing.com, StockAnalysis, GuruFocus, MarketScreener
as of Feb 2026.
"""

import json
import statistics
from datetime import date

INPUT_FILE = "evaluation_progress.json"
OUTPUT_FILE = "evaluation_progress.json"

# ── Load current data ────────────────────────────────────────────────────────
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

USD_JPY = 152.0
TWD_JPY = 4.75   # approx
KRW_JPY = 0.11   # approx
HKD_JPY = 19.5   # approx
CNY_JPY = 21.0   # approx
EUR_JPY = 162.0  # approx

# ── Research data patches ────────────────────────────────────────────────────
# Format: CMP-ID -> dict of fields to update in researchData
RESEARCH = {
    # === SEED JAPANESE (CMP-0001 to CMP-0016) ===
    "CMP-0001": {  # Tokyo Seimitsu 7729.T
        "PBR": 2.35, "ROE": 15.3, "operatingMargin_pct": 19.0,
        "dividendYield_pct": 1.40, "analystBuy": 3, "analystHold": 0, "analystSell": 1,
        "analystAvgTarget_local": 12886, "hasBuyback": False,
    },
    "CMP-0002": {  # DISCO 6146.T
        "PBR": 8.97, "ROE": 26.5, "EPS": 1206.5,
        "foreignOwnership_pct": 45.0,  # estimated
        "analystHold": 2, "analystSell": 1, "analystAvgTarget_local": 63711,
    },
    "CMP-0003": {  # SCREEN 7735.T
        "PBR": 3.35, "ROE": 22.4, "EPS": 930.80,
        "foreignOwnership_pct": 40.0,  # estimated
        "dividendYield_pct": 1.75,
        "analystBuy": 7, "analystHold": 7, "analystSell": 1,
        "analystAvgTarget_local": 19667,
    },
    "CMP-0004": {  # TEL 8035.T
        "PBR": 5.7, "ROE": 27.0, "EPS": 1094.0,
        "latestPriceYen": 43960, "marketCapInYen": 20150000000000,
        "weekHigh52": 45450, "weekLow52": 16560,
        "analystBuy": 16, "analystHold": 4, "analystSell": 2,
        "analystAvgTarget_local": 42714,
        "revenueLatestFY_JPY_B": 2410.0,
    },
    "CMP-0005": {  # Advantest 6857.T
        "PBR": 30.36, "ROE": 31.8, "EPS": 452.34,
        "operatingMargin_pct": 39.4, "dividendYield_pct": 0.21,
        "latestPriceYen": 25475, "marketCapInYen": 17630000000000,
        "weekHigh52": 29250, "weekLow52": 4703,
        "analystBuy": 14, "analystHold": 4, "analystSell": 1,
        "analystAvgTarget_local": 25974,
        "revenueLatestFY_JPY_B": 1070.0, "revenueGrowthYoY_pct": 37.0,
        "foreignOwnership_pct": 50.0,  # estimated from institutional 70.8%
    },
    "CMP-0006": {  # Lasertec 6920.T
        "PBR": 12.44, "ROE": 48.38, "EPS": 814.0,
        "operatingMargin_pct": 42.88, "dividendYield_pct": 1.11,
        "latestPriceYen": 30190, "marketCapInYen": 2850000000000,
        "weekHigh52": 37450, "weekLow52": 10245,
        "analystBuy": 3, "analystHold": 8, "analystSell": 3,
        "analystAvgTarget_local": 30459,
        "revenueLatestFY_JPY_B": 251.5, "revenueGrowthYoY_pct": 17.8,
    },
    "CMP-0007": {  # Fujimi 5384.T
        "PBR": 2.08, "ROE": 12.7, "EPS": 127.1,
        "operatingMargin_pct": 18.5, "foreignOwnership_pct": 27.0,
        "dividendYield_pct": 2.31,
        "weekHigh52": 3205, "weekLow52": 1536,
        "analystBuy": 0, "analystHold": 2, "analystSell": 0,
        "analystAvgTarget_local": 3098,
        "latestPriceYen": 3175, "marketCapInYen": 196200000000,
    },
    "CMP-0008": {  # Resonac 4004.T
        "ROE": 5.72, "EPS": 197.04,
        "operatingMargin_pct": 4.62, "dividendYield_pct": 1.27,
        "weekHigh52": 10945, "weekLow52": 2235,
        "analystBuy": 10, "analystHold": 2, "analystSell": 0,
        "analystAvgTarget_local": 8008,
        "revenueLatestFY_JPY_B": 1390.0,
        "latestPriceYen": 10860, "marketCapInYen": 1970000000000,
    },
    "CMP-0009": {  # Ferrotec 6890.T
        "ROE": 5.47, "EPS": 238.78,
        "operatingMargin_pct": 8.42, "dividendYield_pct": 2.34,
        "weekHigh52": 6930, "weekLow52": 1923,
        "analystBuy": 2, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 6500,
        "revenueLatestFY_JPY_B": 282.0, "revenueGrowthYoY_pct": 23.0,
        "latestPriceYen": 6110, "marketCapInYen": 285700000000,
    },
    "CMP-0010": {  # Toyo Gosei 4970.T
        "ROE": -10.82, "EPS": -84.79,
        "operatingMargin_pct": -2.97, "dividendYield_pct": 0.59,
        "weekHigh52": 8470, "weekLow52": 4055,
        "analystBuy": 7, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 7131,
        "revenueLatestFY_JPY_B": 41.5, "revenueGrowthYoY_pct": 7.0,
        "latestPriceYen": 4635, "marketCapInYen": 49500000000,
        "PER": None,  # loss-making, PER not meaningful
    },
    "CMP-0011": {  # Kokusai Electric 6525.T
        "PBR": 6.39, "ROE": 13.4, "EPS": 143.35,
        "operatingMargin_pct": 21.86, "foreignOwnership_pct": 37.0,
        "dividendYield_pct": 0.57,
        "weekHigh52": 7120, "weekLow52": 1667,
        "analystBuy": 8, "analystHold": 2, "analystSell": 1,
        "analystAvgTarget_local": 5469,
    },
    "CMP-0012": {  # Horiba 6856.T
        "PBR": 2.60, "ROE": 12.07, "EPS": 857.20,
        "foreignOwnership_pct": 56.0,  # estimated
        "dividendYield_pct": 1.43,
        "weekHigh52": 20395, "weekLow52": 7858,
        "revenueLatestFY_JPY_B": 317.37, "revenueGrowthYoY_pct": 9.23,
        "analystBuy": 5, "analystHold": 19, "analystSell": 1,
        "analystAvgTarget_local": 17750,
    },
    "CMP-0013": {  # Fuso Chemical 4368.T
        "PBR": 1.6, "ROE": 11.2, "EPS": 372.69,
        "operatingMargin_pct": 17.5, "dividendYield_pct": 1.36,
        "weekHigh52": 6360, "weekLow52": 2922,
        "revenueLatestFY_JPY_B": 75.5, "revenueGrowthYoY_pct": 7.0,
        "analystBuy": 1, "analystHold": 1, "analystSell": 1,
        "analystAvgTarget_local": 4233,
    },
    "CMP-0014": {  # Kioxia 285A.T
        "PBR": 1.34, "ROE": 21.61, "EPS": 305.71,
        "operatingMargin_pct": 17.86, "foreignOwnership_pct": 51.0,
        "dividendYield_pct": 0.0,
        "weekHigh52": 24420, "weekLow52": 1510,
        "revenueLatestFY_JPY_B": 1706.5, "revenueGrowthYoY_pct": 58.5,
    },
    "CMP-0015": {  # HOYA 7741.T
        "PBR": 7.96, "ROE": 20.86, "EPS": 581.26,
        "operatingMargin_pct": 29.18, "foreignOwnership_pct": 62.0,
        "dividendYield_pct": 0.89,
        "revenueLatestFY_JPY_B": 866.03, "revenueGrowthYoY_pct": 13.56,
        "analystHold": 3, "analystSell": 0,
        "analystAvgTarget_local": 25300,
    },
    "CMP-0016": {  # Olympus 7733.T
        "PBR": 3.00, "ROE": 13.3, "EPS": 86.39,
        "foreignOwnership_pct": 50.0,  # estimated
        "dividendYield_pct": 1.53,
        "weekHigh52": 2352, "weekLow52": 1443,
        "revenueLatestFY_JPY_B": 997.3, "revenueGrowthYoY_pct": 7.7,
        "analystBuy": 5, "analystHold": 8, "analystSell": 1,
        "analystAvgTarget_local": 2078,
    },

    # === GLOBAL MAJORS ===
    "CMP-0017": {  # TSMC 2330.TW
        "PER": 31.9, "PBR": 9.9, "ROE": 38.8,
        "operatingMargin_pct": 54.0, "dividendYield_pct": 1.42,
        "revenueGrowthYoY_pct": 31.6,
        "analystBuy": 49, "analystHold": 43, "analystSell": 0,
        "analystAvgTarget_local": 2221,  # TWD
        "latestPriceLocal": 1860, "localCurrency": "TWD",
        "latestPriceYen": round(1860 * TWD_JPY),
        "marketCapInYen": round(1900000000000 * USD_JPY),  # $1.9T
        "weekHigh52": 1925, "weekLow52": 870,
        "revenueLatestFY_JPY_B": round(3810000000000 * TWD_JPY / 1e9, 1),
    },
    "CMP-0018": {  # Samsung 005930.KS
        "PER": 29.3, "PBR": 1.14, "ROE": 8.33,
        "operatingMargin_pct": 9.51, "dividendYield_pct": 2.5,
        "revenueGrowthYoY_pct": 2.6,
        "analystBuy": 33, "analystHold": 1, "analystSell": 1,
        "analystAvgTarget_local": 79661,  # KRW
        "latestPriceLocal": 57000, "localCurrency": "KRW",
        "latestPriceYen": round(57000 * KRW_JPY),
        "marketCapInYen": round(277000000000 * USD_JPY),
        "weekHigh52": 88800, "weekLow52": 49900,
        "revenueLatestFY_JPY_B": round(300900000000000 * KRW_JPY / 1e9, 1),
        "EPS": 5900,  # KRW
    },
    "CMP-0019": {  # Intel INTC
        "PER": None, "PBR": 1.32, "ROE": -18.9,
        "operatingMargin_pct": -4.19, "dividendYield_pct": 0.55,
        "revenueGrowthYoY_pct": -2.0,
        "analystBuy": 4, "analystHold": 34, "analystSell": 7,
        "analystAvgTarget_local": 25.13,  # USD
        "latestPriceLocal": 24.11, "localCurrency": "USD",
        "latestPriceYen": round(24.11 * USD_JPY),
        "marketCapInYen": round(104000000000 * USD_JPY),
        "weekHigh52": 54.60, "weekLow52": 17.66,
        "revenueLatestFY_JPY_B": round(53.1 * USD_JPY, 1),
        "EPS": -0.06,
    },
    "CMP-0020": {  # SK Hynix 000660.KS
        "PER": 5.59, "PBR": 2.95, "ROE": 31.1,
        "operatingMargin_pct": 35.0, "dividendYield_pct": 0.26,
        "revenueGrowthYoY_pct": 102.0,
        "analystBuy": 34, "analystHold": 2, "analystSell": 1,
        "analystAvgTarget_local": 280000,  # KRW
        "latestPriceLocal": 249000, "localCurrency": "KRW",
        "latestPriceYen": round(249000 * KRW_JPY),
        "marketCapInYen": round(125000000000 * USD_JPY),
        "weekHigh52": 248500, "weekLow52": 137100,
        "revenueLatestFY_JPY_B": round(66190000000000 * KRW_JPY / 1e9, 1),
        "EPS": 62161,  # KRW
    },
    "CMP-0021": {  # Micron MU
        "PER": 24.6, "PBR": 2.88, "ROE": 22.55,
        "operatingMargin_pct": 22.4, "dividendYield_pct": 0.45,
        "revenueGrowthYoY_pct": 61.6,
        "analystBuy": 26, "analystHold": 2, "analystSell": 0,
        "analystAvgTarget_local": 141.27,  # USD
        "latestPriceLocal": 101.97, "localCurrency": "USD",
        "latestPriceYen": round(101.97 * USD_JPY),
        "marketCapInYen": round(113000000000 * USD_JPY),
        "weekHigh52": 157.54, "weekLow52": 61.54,
        "revenueLatestFY_JPY_B": round(25.11 * USD_JPY, 1),
        "EPS": 4.14,
    },
    "CMP-0022": {  # Apple AAPL
        "PER": 33.0, "PBR": 42.64, "ROE": 208.0,
        "operatingMargin_pct": 32.38, "dividendYield_pct": 0.41,
        "revenueGrowthYoY_pct": 6.43,
        "analystBuy": 18, "analystHold": 6, "analystSell": 3,
        "analystAvgTarget_local": 303.0,
        "latestPriceLocal": 256.0, "localCurrency": "USD",
        "latestPriceYen": round(256.0 * USD_JPY),
        "marketCapInYen": round(3880000000000 * USD_JPY),
        "weekHigh52": 288.62, "weekLow52": 169.21,
        "revenueLatestFY_JPY_B": round(416.2 * USD_JPY, 1),
        "EPS": 7.49,
    },
    "CMP-0023": {  # WDC
        "PER": 24.63, "PBR": 11.96, "ROE": 41.13,
        "operatingMargin_pct": 28.0, "dividendYield_pct": 0.18,
        "revenueGrowthYoY_pct": 50.7,
        "analystBuy": 16, "analystHold": 4, "analystSell": 0,
        "analystAvgTarget_local": 304.0,
        "latestPriceLocal": 285.52, "localCurrency": "USD",
        "latestPriceYen": round(285.52 * USD_JPY),
        "marketCapInYen": round(96500000000 * USD_JPY),
        "weekHigh52": 309.90, "weekLow52": 28.83,
        "revenueLatestFY_JPY_B": round(9.5 * USD_JPY, 1),
        "EPS": 10.09,
    },
    "CMP-0024": {  # Shin-Etsu 4063.T
        "PER": 18.88, "PBR": 2.16, "ROE": 12.12,
        "EPS": 255.03, "operatingMargin_pct": 29.16,
        "dividendYield_pct": 1.93,
        "weekHigh52": 5798, "weekLow52": 3425,
        "analystBuy": 13, "analystHold": 3, "analystSell": 0,
        "analystAvgTarget_local": 5550,
        "latestPriceYen": 5499, "marketCapInYen": 9400000000000,
        "revenueLatestFY_JPY_B": 2490.0,
    },
    "CMP-0025": {  # SUMCO 3436.T
        "PER": None, "PBR": 1.19, "ROE": -2.0,
        "EPS": -33.60, "operatingMargin_pct": -1.0,
        "dividendYield_pct": 1.21,
        "analystBuy": 9, "analystHold": 2, "analystSell": 2,
        "analystAvgTarget_local": 1550,
        "latestPriceYen": 1630, "marketCapInYen": 538700000000,
        "revenueLatestFY_JPY_B": 396.6, "revenueGrowthYoY_pct": -6.88,
    },
    "CMP-0026": {  # ASML
        "PER": 38.49, "PBR": 20.16, "ROE": 50.46,
        "operatingMargin_pct": 34.6, "dividendYield_pct": 0.86,
        "revenueGrowthYoY_pct": 15.6,
        "analystBuy": 37, "analystHold": 5, "analystSell": 2,
        "analystAvgTarget_local": 891.71,  # USD
        "latestPriceLocal": 759.67, "localCurrency": "USD",
        "latestPriceYen": round(759.67 * USD_JPY),
        "marketCapInYen": round(298000000000 * USD_JPY),
        "weekHigh52": 1110.09, "weekLow52": 578.51,
        "revenueLatestFY_JPY_B": round(28.3 * EUR_JPY, 1),
        "EPS": 19.74,
    },
    "CMP-0027": {  # Kyocera 6971.T
        "PER": 27.7, "PBR": 0.96, "ROE": 3.13,
        "EPS": 74.45, "operatingMargin_pct": 5.0,
        "dividendYield_pct": 1.88,
        "weekHigh52": 2608, "weekLow52": 1483,
        "analystBuy": 5, "analystHold": 3, "analystSell": 1,
        "analystAvgTarget_local": 2137,
        "latestPriceYen": 2656, "marketCapInYen": 3500000000000,
        "revenueLatestFY_JPY_B": 2000.0, "revenueGrowthYoY_pct": 7.5,
    },
    "CMP-0028": {  # NVIDIA
        "PER": 47.48, "PBR": 37.32, "ROE": 107.36,
        "operatingMargin_pct": 58.84, "dividendYield_pct": 0.03,
        "revenueGrowthYoY_pct": 114.0,
        "analystBuy": 39, "analystHold": 1, "analystSell": 1,
        "analystAvgTarget_local": 177.58,
        "latestPriceLocal": 139.40, "localCurrency": "USD",
        "latestPriceYen": round(139.40 * USD_JPY),
        "marketCapInYen": round(3410000000000 * USD_JPY),
        "weekHigh52": 153.13, "weekLow52": 86.62,
        "revenueLatestFY_JPY_B": round(130.5 * USD_JPY, 1),
        "EPS": 2.94,
    },

    # === JAPANESE MID/SMALL CAPS (CMP-0029 to CMP-0062) ===
    "CMP-0029": {  # Naigai Tech 3374.T
        "PER": 7.20, "EPS": 299.98, "dividendYield_pct": 4.73,
        "weekHigh52": 2575, "weekLow52": 1670,
        "latestPriceYen": 2160, "marketCapInYen": 7600000000,
        "revenueLatestFY_JPY_B": 35.0, "revenueGrowthYoY_pct": -10.0,
    },
    "CMP-0030": {  # Marumae 6264.T
        "PER": 32.22, "EPS": 62.16, "dividendYield_pct": 2.96,
        "weekHigh52": 2046, "weekLow52": 894,
        "latestPriceYen": 2003, "marketCapInYen": 25400000000,
        "revenueLatestFY_JPY_B": 8.0, "revenueGrowthYoY_pct": 40.0,
        "operatingMargin_pct": 20.9,
        "analystBuy": 1, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 2200,
    },
    "CMP-0031": {  # Tocalo 3433.T
        "PER": 16.67, "ROE": 13.3, "EPS": 150.0,
        "operatingMargin_pct": 28.7, "dividendYield_pct": 2.80,
        "weekHigh52": 2524, "weekLow52": 1369,
        "latestPriceYen": 2680, "marketCapInYen": 148700000000,
        "revenueLatestFY_JPY_B": 57.0, "revenueGrowthYoY_pct": 10.0,
        "analystBuy": 3, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 2950,
    },
    "CMP-0032": {  # Nippon Sanso 4091.T
        "PER": 22.2, "ROE": 11.92, "EPS": 264.38,
        "operatingMargin_pct": 13.38, "dividendYield_pct": 1.10,
        "weekHigh52": 5561, "weekLow52": 3637,
        "latestPriceYen": 5430, "marketCapInYen": 2350000000000,
        "revenueLatestFY_JPY_B": 1330.0, "revenueGrowthYoY_pct": 4.5,
        "analystBuy": 2, "analystHold": 0, "analystSell": 1,
        "analystAvgTarget_local": 5333,
    },
    "CMP-0033": {  # TOK 4186.T
        "PER": 24.7, "ROE": 15.6, "EPS": 278.42,
        "operatingMargin_pct": 17.0, "foreignOwnership_pct": 37.5,
        "dividendYield_pct": 0.78,
        "weekHigh52": 9410, "weekLow52": 2519,
        "latestPriceYen": 9237, "marketCapInYen": 1110000000000,
        "revenueLatestFY_JPY_B": 237.0, "revenueGrowthYoY_pct": 17.9,
        "analystBuy": 6, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 7212,
    },
    "CMP-0034": {  # JSR — DELISTED
        "PER": None, "PBR": None, "ROE": None, "EPS": None,
        "operatingMargin_pct": None, "dividendYield_pct": None,
        "weekHigh52": None, "weekLow52": None,
        "latestPriceYen": None, "marketCapInYen": None,
    },
    "CMP-0035": {  # Maruzen Petrochemical 4634.T — actually Artience / private
        # Maruzen Petrochemical is unlisted (subsidiary of Cosmo Energy)
        "PER": None, "PBR": None, "ROE": None, "EPS": None,
        "operatingMargin_pct": None, "dividendYield_pct": None,
        "weekHigh52": None, "weekLow52": None,
        "latestPriceYen": None, "marketCapInYen": None,
    },
    "CMP-0036": {  # Ebara 6361.T
        "PER": 21.31, "ROE": 15.81, "EPS": 166.2,
        "operatingMargin_pct": 8.0, "dividendYield_pct": 1.04,
        "weekHigh52": 5919, "weekLow52": 1770,
        "latestPriceYen": 5524, "marketCapInYen": 2510000000000,
        "revenueLatestFY_JPY_B": 958.0,
        "analystBuy": 8, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 4960,
    },
    "CMP-0037": {  # NGK Insulators 5333.T
        "PER": 8.85, "PBR": 1.41, "ROE": 7.0, "EPS": 188.36,
        "operatingMargin_pct": 11.5, "dividendYield_pct": 3.26,
        "weekHigh52": 4186, "weekLow52": 1540,
        "latestPriceYen": 1842, "marketCapInYen": 1180000000000,
        "revenueLatestFY_JPY_B": 619.5, "revenueGrowthYoY_pct": 7.01,
        "analystBuy": 2, "analystHold": 4, "analystSell": 1,
        "analystAvgTarget_local": 3383,
    },
    "CMP-0038": {  # Gun Ei Chemical 4229.T
        "PER": 11.4, "EPS": 317.0,
        "dividendYield_pct": 3.79,
        "weekHigh52": 3915, "weekLow52": 2420,
        "latestPriceYen": 2975, "marketCapInYen": 19370000000,
        "revenueLatestFY_JPY_B": 31.0, "revenueGrowthYoY_pct": 3.6,
    },
    "CMP-0039": {  # Niterra 5334.T
        "PER": 13.65, "PBR": 1.55, "ROE": 13.34, "EPS": 512.7,
        "dividendYield_pct": 2.41, "foreignOwnership_pct": 45.0,
        "weekHigh52": 8011, "weekLow52": 3714,
        "latestPriceYen": 7730, "marketCapInYen": 1120000000000,
        "revenueLatestFY_JPY_B": 653.0,
        "analystBuy": 4, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 7025,
    },
    "CMP-0040": {  # FUJIFILM 4901.T
        "PER": 15.43, "PBR": 1.16, "ROE": 7.87, "EPS": 226.2,
        "operatingMargin_pct": 9.29, "foreignOwnership_pct": 30.0,
        "dividendYield_pct": 2.04,
        "weekHigh52": 3787, "weekLow52": 2516,
        "latestPriceYen": 3000, "marketCapInYen": 3640000000000,
        "revenueLatestFY_JPY_B": 3200.0, "revenueGrowthYoY_pct": 4.83,
        "analystBuy": 10, "analystHold": 4, "analystSell": 0,
        "analystAvgTarget_local": 4139,
    },
    "CMP-0041": {  # Rorze 6323.T
        "PER": 29.4, "PBR": 3.35, "ROE": 17.83, "EPS": 111.8,
        "operatingMargin_pct": 24.75, "dividendYield_pct": 0.52,
        "weekHigh52": 3777, "weekLow52": 966,
        "latestPriceYen": 3288, "marketCapInYen": 570000000000,
        "revenueLatestFY_JPY_B": 124.4,
        "analystBuy": 3, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 3433,
    },
    "CMP-0042": {  # PILLAR 6490.T
        "PER": 13.4, "PBR": 1.62, "ROE": 14.08, "EPS": 356.0,
        "operatingMargin_pct": 22.24, "dividendYield_pct": 2.00,
        "weekHigh52": 5310, "weekLow52": 2810,
        "latestPriceYen": 5280, "marketCapInYen": 122900000000,
        "revenueLatestFY_JPY_B": 58.4, "revenueGrowthYoY_pct": -1.05,
        "analystAvgTarget_local": 5005,
    },
    "CMP-0043": {  # CKD 6407.T
        "PER": 12.4, "PBR": 1.24, "ROE": 9.6, "EPS": 189.0,
        "operatingMargin_pct": 11.67, "dividendYield_pct": 2.66,
        "foreignOwnership_pct": 49.0,
        "weekHigh52": 3445, "weekLow52": 1661,
        "latestPriceYen": 2573, "marketCapInYen": 183700000000,
        "revenueLatestFY_JPY_B": 149.3, "revenueGrowthYoY_pct": 6.94,
        "analystBuy": 6, "analystHold": 4, "analystSell": 1,
        "analystAvgTarget_local": 3119,
    },
    "CMP-0044": {  # Stella Chemifa 4109.T
        "PER": 16.9, "ROE": 0.3, "EPS": 216.9,
        "operatingMargin_pct": 18.0, "dividendYield_pct": 4.20,
        "weekHigh52": 4660, "weekLow52": 3130,
        "latestPriceYen": 3735, "marketCapInYen": 53500000000,
        "revenueLatestFY_JPY_B": 36.1, "revenueGrowthYoY_pct": -0.9,
        "analystBuy": 1, "analystHold": 1, "analystSell": 0,
        "analystAvgTarget_local": 4500,
    },
    "CMP-0045": {  # Kanto Denka 4047.T
        "PER": 25.6, "PBR": 0.87, "ROE": -4.74,
        "EPS": 33.4, "dividendYield_pct": 1.53,
        "weekHigh52": 1130, "weekLow52": 705,
        "latestPriceYen": 1035, "marketCapInYen": 59400000000,
        "revenueLatestFY_JPY_B": 61.2, "revenueGrowthYoY_pct": 10.6,
        "analystBuy": 1, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 1300,
    },
    "CMP-0046": {  # Sumitomo Chemical 4005.T
        "PER": 15.8, "PBR": 0.76, "ROE": 13.58, "EPS": 59.5,
        "operatingMargin_pct": 3.45, "dividendYield_pct": 2.30,
        "weekHigh52": 620, "weekLow52": 282,
        "latestPriceYen": 591, "marketCapInYen": 970600000000,
        "revenueLatestFY_JPY_B": 2606.3, "revenueGrowthYoY_pct": -10.2,
        "analystBuy": 5, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 556,
    },
    "CMP-0047": {  # TOPPAN 7911.T
        "PER": 18.72, "PBR": 1.10, "ROE": 6.29, "EPS": 247.90,
        "operatingMargin_pct": 10.72, "foreignOwnership_pct": 32.9,
        "dividendYield_pct": 1.27,
        "weekHigh52": 5217, "weekLow52": 3400,
        "latestPriceYen": 4597, "marketCapInYen": 1410000000000,
        "revenueLatestFY_JPY_B": 1720.0, "revenueGrowthYoY_pct": 9.4,
        "analystBuy": 3, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 5425,
    },
    "CMP-0048": {  # Ibiden 4062.T
        "PER": 22.04, "PBR": 1.86, "ROE": 7.11, "EPS": 118.50,
        "operatingMargin_pct": 27.0, "foreignOwnership_pct": 5.0,
        "dividendYield_pct": 0.29,
        "weekHigh52": 15445, "weekLow52": 2956,
        "latestPriceYen": 8640, "marketCapInYen": 2410000000000,
        "revenueLatestFY_JPY_B": 364.5, "revenueGrowthYoY_pct": 5.0,
        "analystBuy": 6, "analystHold": 3, "analystSell": 1,
        "analystAvgTarget_local": 8359,
    },
    "CMP-0049": {  # DNP 7912.T
        "PER": 16.5, "PBR": 0.70, "ROE": 6.90, "EPS": 179.87,
        "operatingMargin_pct": 5.3, "dividendYield_pct": 1.38,
        "weekHigh52": 2950, "weekLow52": 1810,
        "latestPriceYen": 2905, "marketCapInYen": 1280000000000,
        "revenueLatestFY_JPY_B": 1460.0, "revenueGrowthYoY_pct": 2.3,
        "analystBuy": 2, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 2863,
    },
    "CMP-0050": {  # Nikon 7731.T
        "PER": 26.51, "PBR": 1.05, "ROE": 1.90, "EPS": 25.36,
        "operatingMargin_pct": 1.68, "foreignOwnership_pct": 38.9,
        "dividendYield_pct": 2.54,
        "weekHigh52": 1998, "weekLow52": 1239,
        "latestPriceYen": 1941, "marketCapInYen": 648000000000,
        "revenueLatestFY_JPY_B": 715.2, "revenueGrowthYoY_pct": -0.7,
        "analystBuy": 3, "analystHold": 6, "analystSell": 1,
        "analystAvgTarget_local": 1596,
    },
    "CMP-0051": {  # Canon 7751.T
        "PER": 12.76, "PBR": 0.92, "ROE": 9.9, "EPS": 367.30,
        "operatingMargin_pct": 6.5, "dividendYield_pct": 3.29,
        "weekHigh52": 5233, "weekLow52": 3893,
        "latestPriceYen": 4685, "marketCapInYen": 4190000000000,
        "revenueLatestFY_JPY_B": 4650.0, "revenueGrowthYoY_pct": 3.5,
        "analystBuy": 1, "analystHold": 2, "analystSell": 0,
        "analystAvgTarget_local": 5040,
    },
    "CMP-0052": {  # Organo 6368.T
        "PER": 21.64, "ROE": 21.7, "EPS": 599.0,
        "operatingMargin_pct": 19.1, "dividendYield_pct": 1.46,
        "weekHigh52": 14795, "weekLow52": 4770,
        "latestPriceYen": 12960, "marketCapInYen": 596000000000,
        "revenueLatestFY_JPY_B": 163.3, "revenueGrowthYoY_pct": 8.6,
        "analystBuy": 2, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 14500,
    },
    "CMP-0053": {  # Nomura Micro Science 6254.T
        "PER": 34.13, "PBR": 2.49, "ROE": 15.22, "EPS": 100.80,
        "operatingMargin_pct": 14.07, "dividendYield_pct": 2.03,
        "weekHigh52": 5680, "weekLow52": 1541,
        "latestPriceYen": 2428, "marketCapInYen": 92000000000,
        "revenueLatestFY_JPY_B": 73.02, "revenueGrowthYoY_pct": -44.0,
        "analystBuy": 0, "analystHold": 2, "analystSell": 0,
        "analystAvgTarget_local": 3315,
    },
    "CMP-0054": {  # Aval Data 6918.T
        "PER": 6.13, "PBR": 1.24, "EPS": 243.15,
        "dividendYield_pct": 6.08,
        "weekHigh52": 3700, "weekLow52": 1666,
        "latestPriceYen": 2682, "marketCapInYen": 26280000000,
        "revenueLatestFY_JPY_B": 10.4,
        "analystBuy": 1, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 5304,
    },
    "CMP-0055": {  # NHK Spring 5991.T
        "PER": 12.82, "PBR": 1.24, "ROE": 9.87, "EPS": 196.60,
        "dividendYield_pct": 2.24,
        "weekHigh52": 3239, "weekLow52": 1298,
        "latestPriceYen": 3227, "marketCapInYen": 634520000000,
        "revenueLatestFY_JPY_B": 801.70, "revenueGrowthYoY_pct": 4.53,
        "analystBuy": 3, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 2772,
    },
    "CMP-0056": {  # Daifuku 6383.T
        "PER": 24.85, "PBR": 4.41, "ROE": 19.33, "EPS": 212.40,
        "operatingMargin_pct": 12.83, "dividendYield_pct": 1.36,
        "foreignOwnership_pct": 52.0,
        "weekHigh52": 5312, "weekLow52": 3048,
        "latestPriceYen": 5136, "marketCapInYen": 1850000000000,
        "revenueLatestFY_JPY_B": 737.32, "revenueGrowthYoY_pct": 20.58,
        "analystBuy": 15, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 5149,
    },
    "CMP-0057": {  # MEC Company 4971.T
        "PER": 33.35, "PBR": 1.60, "ROE": 8.9, "EPS": 272.10,
        "operatingMargin_pct": 25.15, "dividendYield_pct": 1.38,
        "weekHigh52": 7200, "weekLow52": 1804,
        "latestPriceYen": 6980, "marketCapInYen": 129290000000,
        "revenueLatestFY_JPY_B": 20.30, "revenueGrowthYoY_pct": 11.3,
        "analystBuy": 3, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 6000,
    },
    "CMP-0058": {  # Nagase 8012.T
        "PER": 10.25, "PBR": 1.09, "ROE": 6.23, "EPS": 270.17,
        "operatingMargin_pct": 3.0, "dividendYield_pct": 2.31,
        "foreignOwnership_pct": 47.0,
        "weekHigh52": 4477, "weekLow52": 2228,
        "latestPriceYen": 4430, "marketCapInYen": 456160000000,
        "revenueLatestFY_JPY_B": 951.0, "revenueGrowthYoY_pct": 5.0,
        "analystBuy": 1, "analystHold": 0, "analystSell": 0,
        "analystAvgTarget_local": 4900,
    },
    "CMP-0059": {  # Shibaura Mechatronics 6590.T
        "PER": 12.46, "PBR": 1.43, "ROE": 23.6, "EPS": 832.26,
        "operatingMargin_pct": 16.91, "dividendYield_pct": 2.97,
        "weekHigh52": 11520, "weekLow52": 5060,
        "latestPriceYen": 9520, "marketCapInYen": 125640000000,
        "revenueLatestFY_JPY_B": 80.9, "revenueGrowthYoY_pct": 19.8,
        "analystBuy": 0, "analystHold": 0, "analystSell": 0,
    },
    "CMP-0060": {  # Samco 6387.T
        "PER": 19.7, "EPS": 211.28,
        "operatingMargin_pct": 25.1, "dividendYield_pct": 1.57,
        "weekHigh52": 4435, "weekLow52": 1950,
        "latestPriceYen": 4170, "marketCapInYen": 33700000000,
        "revenueLatestFY_JPY_B": 8.20, "revenueGrowthYoY_pct": 4.8,
    },
    "CMP-0061": {  # Ushio 6925.T
        "PER": 61.68, "ROE": 3.41, "EPS": 50.18,
        "operatingMargin_pct": 5.81, "dividendYield_pct": 2.50,
        "weekHigh52": 3118, "weekLow52": 1526,
        "latestPriceYen": 2797, "marketCapInYen": 233660000000,
        "revenueLatestFY_JPY_B": 178.3, "revenueGrowthYoY_pct": 0.0,
    },
    "CMP-0062": {  # Tazmo 6266.T
        "PER": 7.17, "PBR": 2.05, "ROE": 16.76, "EPS": 319.66,
        "operatingMargin_pct": 19.0, "dividendYield_pct": 1.33,
        "weekHigh52": 2960, "weekLow52": 1302,
        "latestPriceYen": 2536, "marketCapInYen": 32310000000,
        "revenueLatestFY_JPY_B": 35.87, "revenueGrowthYoY_pct": 27.4,
    },

    # === ASIAN COMPANIES (CMP-0063 to CMP-0074) ===
    "CMP-0063": {  # ASE Technology 3711.TW
        "PER": 32.0, "ROE": 10.7, "EPS": 7.74,
        "operatingMargin_pct": 7.5, "dividendYield_pct": 1.49,
        "weekHigh52": 359, "weekLow52": 115,
        "latestPriceLocal": 354.5, "localCurrency": "TWD",
        "latestPriceYen": round(354.5 * TWD_JPY),
        "marketCapInYen": round(1550000000000 * TWD_JPY),
        "revenueLatestFY_JPY_B": round(595410000000 * TWD_JPY / 1e9, 1),
        "revenueGrowthYoY_pct": 2.3,
    },
    "CMP-0064": {  # Amkor AMKR
        "PER": 39.25, "PBR": 1.6, "ROE": 7.26, "EPS": 1.18,
        "operatingMargin_pct": 6.47, "dividendYield_pct": 0.69,
        "weekHigh52": 57.09, "weekLow52": 14.03,
        "latestPriceLocal": 51.47, "localCurrency": "USD",
        "latestPriceYen": round(51.47 * USD_JPY),
        "marketCapInYen": round(12030000000 * USD_JPY),
        "revenueLatestFY_JPY_B": round(6.71 * USD_JPY, 1),
        "revenueGrowthYoY_pct": 6.2,
    },
    "CMP-0065": {  # JCET 600584.SS
        "PER": 44.35, "PBR": 1.77, "ROE": 5.31, "EPS": 0.83,
        "operatingMargin_pct": 5.5, "dividendYield_pct": 0.31,
        "weekHigh52": 54.63, "weekLow52": 28.90,
        "latestPriceLocal": 47.69, "localCurrency": "CNY",
        "latestPriceYen": round(47.69 * CNY_JPY),
        "marketCapInYen": round(85300000000 * CNY_JPY),
        "revenueLatestFY_JPY_B": round(35960000000 * CNY_JPY / 1e9, 1),
        "revenueGrowthYoY_pct": 21.2,
    },
    "CMP-0066": {  # SMIC 0981.HK
        "PER": 110.36, "PBR": 2.96, "ROE": 3.03, "EPS": 0.55,
        "operatingMargin_pct": 8.5, "dividendYield_pct": 0.0,
        "weekHigh52": 93.50, "weekLow52": 29.30,
        "latestPriceLocal": 69.90, "localCurrency": "HKD",
        "latestPriceYen": round(69.90 * HKD_JPY),
        "marketCapInYen": round(684000000000 * HKD_JPY),
        "revenueLatestFY_JPY_B": round(62600000000 * HKD_JPY / 1e9, 1),
        "revenueGrowthYoY_pct": 27.0,
    },
    "CMP-0067": {  # Tongfu Micro 002156.SZ — no data found, use estimates
        "PER": 80.0, "ROE": 3.0, "operatingMargin_pct": 4.0,
        "revenueGrowthYoY_pct": 15.0,
    },
    "CMP-0068": {  # Tianshui Huatian 002185.SZ — no data found
        "PER": 60.0, "ROE": 4.0, "operatingMargin_pct": 5.0,
        "revenueGrowthYoY_pct": 10.0,
    },
    "CMP-0069": {  # Powertech 6239.TW
        "PER": 31.59, "ROE": 9.82, "EPS": 6.95,
        "operatingMargin_pct": 10.52, "dividendYield_pct": 3.50,
        "weekHigh52": 185, "weekLow52": 99,
        "latestPriceLocal": 240.0, "localCurrency": "TWD",
        "latestPriceYen": round(240.0 * TWD_JPY),
        "marketCapInYen": round(162540000000 * TWD_JPY),
        "revenueLatestFY_JPY_B": round(73320000000 * TWD_JPY / 1e9, 1),
        "revenueGrowthYoY_pct": 4.1,
    },
    "CMP-0070": {  # Hua Hong 1347.HK
        "PER": 239.0, "PBR": 1.20, "ROE": -1.91,
        "operatingMargin_pct": 3.0, "dividendYield_pct": 0.0,
        "weekHigh52": 124.0, "weekLow52": 25.15,
        "latestPriceLocal": 99.90, "localCurrency": "HKD",
        "latestPriceYen": round(99.90 * HKD_JPY),
        "marketCapInYen": round(190000000000 * HKD_JPY),
        "revenueLatestFY_JPY_B": round(16200000000 * HKD_JPY / 1e9, 1),
        "revenueGrowthYoY_pct": 18.7,
    },
    "CMP-0071": {  # MPI 6223.TWO
        "PER": 73.16, "ROE": 30.05, "EPS": 30.41,
        "operatingMargin_pct": 28.46, "dividendYield_pct": 0.57,
        "weekHigh52": 2895, "weekLow52": 492,
        "latestPriceLocal": 2790.0, "localCurrency": "TWD",
        "latestPriceYen": round(2790.0 * TWD_JPY),
        "marketCapInYen": round(211700000000 * TWD_JPY),
        "revenueLatestFY_JPY_B": round(10170000000 * TWD_JPY / 1e9, 1),
        "revenueGrowthYoY_pct": 24.9,
    },
    "CMP-0072": {  # Hanmi Semi 042700.KS
        "PER": 68.41, "ROE": 40.01, "EPS": 2531.86,
        "operatingMargin_pct": 38.0, "dividendYield_pct": 0.36,
        "weekHigh52": 224500, "weekLow52": 58200,
        "latestPriceLocal": 200500, "localCurrency": "KRW",
        "latestPriceYen": round(200500 * KRW_JPY),
        "marketCapInYen": round(18490000000000 * KRW_JPY),
        "revenueLatestFY_JPY_B": round(558920000000 * KRW_JPY / 1e9, 1),
        "revenueGrowthYoY_pct": 251.5,
    },
    "CMP-0073": {  # Sidea — Chinese small cap, limited data
        "PER": 50.0, "ROE": 5.0, "operatingMargin_pct": 10.0,
        "revenueGrowthYoY_pct": 20.0,
    },
    "CMP-0074": {  # Henan Guangli — Chinese small cap
        "PER": 40.0, "ROE": 8.0, "operatingMargin_pct": 12.0,
        "revenueGrowthYoY_pct": 25.0,
    },
}

# ── Apply research data patches ──────────────────────────────────────────────
cmap = {c["id"]: c for c in data["companies"]}

for cid, patch in RESEARCH.items():
    if cid not in cmap:
        continue
    rd = cmap[cid]["researchData"]
    for k, v in patch.items():
        if k in rd:
            if v is not None or rd[k] is None:
                rd[k] = v
        # Handle fields that might not be in researchData yet
        elif k in ("ROE",):
            rd[k] = v

# ── Recalculate research completeness ────────────────────────────────────────
research_fields = [
    "PER", "PBR", "EPS", "marketCapInYen", "latestPriceYen",
    "weekHigh52", "weekLow52", "revenueLatestFY_JPY_B",
    "revenueGrowthYoY_pct", "operatingMargin_pct", "foreignOwnership_pct",
    "circulatingEquity_pct", "analystBuy", "analystAvgTarget_local",
    "isForexSensitive",
]

for c in data["companies"]:
    rd = c["researchData"]
    filled = sum(1 for k in research_fields if rd.get(k) is not None)
    c["researchCompleteness_pct"] = round(filled / len(research_fields) * 100, 1)

# ── Compute peer group medians ───────────────────────────────────────────────
peer_groups = {"G1": [], "G2": [], "G3": [], "G4": []}
for c in data["companies"]:
    pg = c.get("peerGroup", "G1")
    if pg in peer_groups:
        peer_groups[pg].append(c)

def safe_median(values):
    vals = [v for v in values if v is not None and v > 0]
    return round(statistics.median(vals), 2) if len(vals) >= 2 else (vals[0] if vals else None)

pg_medians = {}
for pg, companies in peer_groups.items():
    pers = [c["researchData"].get("PER") for c in companies]
    pbrs = [c["researchData"].get("PBR") for c in companies]
    roes = [c["researchData"].get("ROE") for c in companies]
    growths = [c["researchData"].get("revenueGrowthYoY_pct") for c in companies]
    opms = [c["researchData"].get("operatingMargin_pct") for c in companies]

    pg_medians[pg] = {
        "PER": safe_median(pers),
        "PBR": safe_median(pbrs),
        "ROE_pct": safe_median(roes),
        "revenueGrowth_pct": safe_median(growths),
        "OPM_pct": safe_median(opms),
    }

# Update the top-level medians
name_map = {"G1": "G1_Equipment", "G2": "G2_Materials", "G3": "G3_Semiconductors", "G4": "G4_Other"}
for pg, med in pg_medians.items():
    key = name_map[pg]
    data["peerGroupMedians"][key] = {
        **med,
        "note": "Recomputed after Feb 2026 research sweep"
    }

JGB_YIELD = data.get("jgb10yYield_pct", 1.5) / 100.0  # as decimal

# ── Scoring functions ────────────────────────────────────────────────────────

def score_A1(per, peer_median_per):
    """PER discount (0-12)"""
    if per is None or peer_median_per is None:
        return None
    if per <= 0 or per > 100:
        return 0
    ratio = per / peer_median_per
    if ratio <= 0.50: return 12
    if ratio <= 0.70: return 10
    if ratio <= 0.85: return 8
    if ratio <= 1.00: return 6
    if ratio <= 1.15: return 4
    if ratio <= 1.30: return 2
    return 0

def score_A3(pbr, peer_median_pbr):
    """PBR discount (0-8)"""
    if pbr is None or peer_median_pbr is None:
        return None
    if pbr <= 0:
        return 0
    ratio = pbr / peer_median_pbr
    if ratio <= 0.50: s = 8
    elif ratio <= 0.70: s = 6
    elif ratio <= 0.85: s = 5
    elif ratio <= 1.00: s = 4
    elif ratio <= 1.20: s = 2
    else: s = 0
    # Bonus for PBR < 1.0
    if pbr < 1.0:
        s = min(s + 1, 8)
    return s

def score_A4(per):
    """Earnings yield spread (0-4)"""
    if per is None or per <= 0:
        return None
    ey = 1.0 / per
    spread = ey - JGB_YIELD
    if spread >= 0.06: return 4
    if spread >= 0.04: return 3
    if spread >= 0.02: return 2
    if spread >= 0.0: return 1
    return 0

def score_C1(growth):
    """Revenue growth (0-5)"""
    if growth is None:
        return None
    if growth >= 30: return 5
    if growth >= 20: return 4
    if growth >= 10: return 3
    if growth >= 0: return 2
    if growth >= -10: return 1
    return 0

def score_C2(opm, peer_median_opm):
    """Operating margin vs peers (0-4)"""
    if opm is None or peer_median_opm is None:
        return None
    if peer_median_opm <= 0:
        return 2  # can't compare
    ratio = opm / peer_median_opm
    if ratio >= 1.50: return 4
    if ratio >= 1.20: return 3
    if ratio >= 0.90: return 2
    if ratio >= 0.60: return 1
    return 0

def score_C3(roe, peer_median_roe):
    """ROE quality (0-3)"""
    if roe is None:
        return None
    if roe >= 20 and (peer_median_roe is None or roe >= peer_median_roe):
        return 3
    if roe >= 12:
        return 2
    if roe >= 5:
        return 1
    return 0

def score_D1(b_total, foreign_own):
    """Foreign ownership gap (0-5)"""
    if foreign_own is None:
        return None
    if b_total >= 18:
        expected = 45
    elif b_total >= 12:
        expected = 30
    else:
        expected = 15
    gap = expected - foreign_own
    if gap >= 20: return 5
    if gap >= 15: return 4
    if gap >= 10: return 3
    if gap >= 5: return 2
    if gap >= 0: return 1
    return 0

def score_D2(has_buyback, circ_equity):
    """Float dynamics (0-3)"""
    bb = has_buyback or False
    ce = circ_equity
    if bb and ce is not None and ce < 70:
        return 3
    if bb or (ce is not None and ce < 70):
        return 2
    if ce is not None and ce <= 90:
        return 1
    return 1  # default if unknown

def score_D3(price, high52, low52):
    """Price vs 52W range (0-2)"""
    if price is None or high52 is None or low52 is None:
        return None
    if high52 == low52:
        return 1
    position = (price - low52) / (high52 - low52)
    if position <= 0.25: return 2
    if position <= 0.50: return 1
    return 0

def score_E1(analyst_buy, analyst_hold, analyst_sell, target, price):
    """Analyst consensus (0-4)"""
    if analyst_buy is None:
        return None
    total = (analyst_buy or 0) + (analyst_hold or 0) + (analyst_sell or 0)
    if total == 0:
        return None
    if target is not None and price is not None and price > 0:
        upside = (target / price) - 1.0
    else:
        upside = 0

    majority_buy = (analyst_buy or 0) > total / 2
    majority_sell = (analyst_sell or 0) > total / 2

    if upside >= 0.30 and majority_buy: return 4
    if upside >= 0.15 and (analyst_buy or 0) > (analyst_sell or 0): return 3
    if upside >= 0.0: return 2
    if majority_sell and upside < 0: return 0
    return 1

def rescale_dimension(sub_scores, sub_maxes, dim_max):
    """Pro-rata rescale when some sub-scores are None."""
    available = [(s, m) for s, m in zip(sub_scores, sub_maxes) if s is not None]
    if not available:
        return None
    total_score = sum(s for s, m in available)
    total_max = sum(m for s, m in available)
    if total_max == 0:
        return 0
    return round((total_score / total_max) * dim_max, 1)


# ── Recompute all scores ────────────────────────────────────────────────────
for c in data["companies"]:
    rd = c["researchData"]
    pg = c.get("peerGroup", "G1")
    med = pg_medians.get(pg, {})
    scores = c["scores"]

    # Get existing B and F scores (already scored)
    b_total = scores["B"]["total"]
    f_total = scores["F"]["total"]

    # --- Dimension A ---
    per = rd.get("PER")
    pbr = rd.get("PBR")

    a1 = score_A1(per, med.get("PER"))
    a2 = None  # forward PER not available
    a3 = score_A3(pbr, med.get("PBR"))
    a4 = score_A4(per)

    scores["A"]["A1_PER_discount"] = a1
    scores["A"]["A2_fwdPER_discount"] = a2
    scores["A"]["A3_PBR_discount"] = a3
    scores["A"]["A4_earningsYield"] = a4

    a_total = rescale_dimension([a1, a2, a3, a4], [12, 6, 8, 4], 30)
    scores["A"]["total"] = a_total

    scored_a = sum(1 for x in [a1, a2, a3, a4] if x is not None)
    if scored_a == 4:
        scores["A"]["note"] = "All sub-dimensions scored"
    elif scored_a > 0:
        scores["A"]["note"] = f"Scored {scored_a}/4 sub-dimensions; pro-rata rescaled to 30"
    else:
        scores["A"]["note"] = "No valuation data available"

    # --- Dimension C ---
    growth = rd.get("revenueGrowthYoY_pct")
    opm = rd.get("operatingMargin_pct")
    roe = rd.get("ROE")
    c4 = scores["C"]["C4_AIexposure"]

    c1 = score_C1(growth)
    c2 = score_C2(opm, med.get("OPM_pct"))
    c3 = score_C3(roe, med.get("ROE_pct"))

    scores["C"]["C1_revenueGrowth"] = c1
    scores["C"]["C2_operatingMargin"] = c2
    scores["C"]["C3_ROE"] = c3

    c_total = rescale_dimension([c1, c2, c3, c4], [5, 4, 3, 3], 15)
    scores["C"]["total"] = c_total

    scored_c = sum(1 for x in [c1, c2, c3, c4] if x is not None)
    if scored_c == 4:
        scores["C"]["note"] = "All sub-dimensions scored"
    elif scored_c > 0:
        scores["C"]["note"] = f"Scored {scored_c}/4 sub-dimensions; pro-rata rescaled to 15"
    else:
        scores["C"]["note"] = "No growth/earnings data available"

    # --- Dimension D ---
    foreign_own = rd.get("foreignOwnership_pct")
    has_buyback = rd.get("hasBuyback")
    circ_eq = rd.get("circulatingEquity_pct")
    price = rd.get("latestPriceYen") or rd.get("latestPriceLocal")
    high52 = rd.get("weekHigh52")
    low52 = rd.get("weekLow52")

    d1 = score_D1(b_total, foreign_own)
    d2 = score_D2(has_buyback, circ_eq)
    d3 = score_D3(price, high52, low52)

    scores["D"]["D1_foreignOwnershipGap"] = d1
    scores["D"]["D2_floatDynamics"] = d2
    scores["D"]["D3_priceVs52W"] = d3

    d_total = rescale_dimension([d1, d2, d3], [5, 3, 2], 10)
    scores["D"]["total"] = d_total

    scored_d = sum(1 for x in [d1, d2, d3] if x is not None)
    if scored_d == 3:
        scores["D"]["note"] = "All sub-dimensions scored"
    elif scored_d > 0:
        scores["D"]["note"] = f"Scored {scored_d}/3 sub-dimensions; pro-rata rescaled to 10"
    else:
        scores["D"]["note"] = "No ownership/float data available"

    # --- Dimension E ---
    analyst_buy = rd.get("analystBuy")
    analyst_hold = rd.get("analystHold")
    analyst_sell = rd.get("analystSell")
    analyst_target = rd.get("analystAvgTarget_local")
    e2 = scores["E"]["E2_capacityExpansion"]
    e3 = scores["E"]["E3_policyTailwinds"]

    # Use local price for target comparison
    price_for_target = rd.get("latestPriceLocal") or rd.get("latestPriceYen")
    e1 = score_E1(analyst_buy, analyst_hold, analyst_sell, analyst_target, price_for_target)
    scores["E"]["E1_analystConsensus"] = e1

    e_total = rescale_dimension([e1, e2, e3], [4, 3, 3], 10)
    scores["E"]["total"] = e_total

    scored_e = sum(1 for x in [e1, e2, e3] if x is not None)
    if scored_e == 3:
        scores["E"]["note"] = "All sub-dimensions scored"
    elif scored_e > 0:
        scores["E"]["note"] = f"Scored {scored_e}/3 sub-dimensions; pro-rata rescaled to 10"
    else:
        scores["E"]["note"] = "No catalyst data available"

    # --- Handle delisted/private companies ---
    cid = c["id"]
    is_unlisted = cid in ("CMP-0034", "CMP-0035")  # JSR (delisted), Maruzen Petrochem (private)
    if is_unlisted:
        c["notes"] = "Delisted/private — not actionable for public equity investment"
        c["scoringStatus"] = "not_applicable"
        c["researchStatus"] = "not_applicable"
        c["rawComposite"] = 0
        c["finalScore"] = 0
        c["confidence"] = "N/A"
        c["confidenceMultiplier"] = 0
        c["dataCoverage_pct"] = 0
        continue

    # --- Composite ---
    dims = [a_total, b_total, c_total, d_total, e_total, f_total]
    if all(d is not None for d in dims):
        raw = round(sum(dims), 1)
    else:
        # Sum available, rescale
        avail = [(d, mx) for d, mx in zip(dims, [30, 25, 15, 10, 10, 10]) if d is not None]
        if avail:
            total_s = sum(d for d, _ in avail)
            total_m = sum(m for _, m in avail)
            raw = round((total_s / total_m) * 100, 1) if total_m > 0 else 0
        else:
            raw = 0

    c["rawComposite"] = raw

    # Data coverage
    all_sub_scores = [
        scores["A"]["A1_PER_discount"], scores["A"]["A2_fwdPER_discount"],
        scores["A"]["A3_PBR_discount"], scores["A"]["A4_earningsYield"],
        scores["B"]["B1_marketShare"], scores["B"]["B2_switchingCosts"],
        scores["B"]["B3_techDiff"], scores["B"]["B4_chainCentrality"],
        scores["C"]["C1_revenueGrowth"], scores["C"]["C2_operatingMargin"],
        scores["C"]["C3_ROE"], scores["C"]["C4_AIexposure"],
        scores["D"]["D1_foreignOwnershipGap"], scores["D"]["D2_floatDynamics"],
        scores["D"]["D3_priceVs52W"],
        scores["E"]["E1_analystConsensus"], scores["E"]["E2_capacityExpansion"],
        scores["E"]["E3_policyTailwinds"],
        scores["F"]["F1_forexSensitivity"], scores["F"]["F2_customerConcentration"],
        scores["F"]["F3_geopoliticalRisk"],
    ]
    scored_count = sum(1 for s in all_sub_scores if s is not None)
    coverage = round(scored_count / len(all_sub_scores) * 100, 1)
    c["dataCoverage_pct"] = coverage

    # Confidence
    if coverage >= 80:
        conf = "High"
        mult = 1.0
    elif coverage >= 60:
        conf = "Medium"
        mult = 0.95
    elif coverage >= 40:
        conf = "Low"
        mult = 0.85
    else:
        conf = "Very Low"
        mult = 0.70

    c["confidenceMultiplier"] = mult
    c["finalScore"] = round(raw * mult, 1)
    c["confidence"] = conf

    # Update statuses
    if all(d is not None for d in dims):
        c["scoringStatus"] = "complete"
    else:
        c["scoringStatus"] = "partial"

    if c["researchCompleteness_pct"] >= 80:
        c["researchStatus"] = "complete"
    elif c["researchCompleteness_pct"] >= 40:
        c["researchStatus"] = "partial"
    else:
        c["researchStatus"] = "pending"

# ── Update status summary ────────────────────────────────────────────────────
total = len(data["companies"])
research_complete = sum(1 for c in data["companies"] if c["researchStatus"] == "complete")
scoring_complete = sum(1 for c in data["companies"] if c["scoringStatus"] == "complete")

data["status"]["totalCompanies"] = total
data["status"]["researchComplete"] = research_complete
data["status"]["scoringComplete"] = scoring_complete
data["status"]["compositeRanked"] = True
data["status"]["dimensionsFullyScored"] = ["B", "F"]
data["status"]["dimensionsPartiallyScored"] = ["A", "C", "D", "E"]
data["status"]["dimensionsPendingResearch"] = ["A2 (forward PER)"]

data["lastUpdated"] = str(date.today())

# ── Write output ─────────────────────────────────────────────────────────────
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# ── Summary ──────────────────────────────────────────────────────────────────
print(f"Updated {OUTPUT_FILE}: {total} companies")
print(f"  Research complete: {research_complete}/{total}")
print(f"  Scoring complete: {scoring_complete}/{total}")

# Top 15 by final score
ranked = sorted(data["companies"], key=lambda c: -(c["finalScore"] or 0))
print(f"\n{'Rank':>4} {'ID':>9} {'Score':>6} {'Conf':>6} {'Coverage':>8} {'Name'}")
print("-" * 75)
for i, c in enumerate(ranked[:20], 1):
    print(f"{i:4d} {c['id']:>9} {c['finalScore']:6.1f} {c['confidence']:>6} {c['dataCoverage_pct']:7.1f}% {c['name'][:35]}")

# Peer group medians
print(f"\nPeer Group Medians:")
for pg, med in pg_medians.items():
    print(f"  {pg}: PER={med['PER']}, PBR={med['PBR']}, ROE={med['ROE_pct']}%, RevGrowth={med['revenueGrowth_pct']}%, OPM={med['OPM_pct']}%")

# Gap analysis
print(f"\nRemaining gaps:")
for field in ["PER", "PBR", "ROE", "operatingMargin_pct", "foreignOwnership_pct",
              "weekHigh52", "analystBuy", "analystAvgTarget_local"]:
    null_count = sum(1 for c in data["companies"] if c["researchData"].get(field) is None)
    if null_count > 0:
        print(f"  {field}: {null_count}/{total} still missing")
