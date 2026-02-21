#!/usr/bin/env python3
"""Add investmentThesis fields to top 10 companies in evaluation_progress.json"""
import json

THESES = {
    "CMP-0024": (
        "Shin-Etsu Chemical is the world's largest producer of silicon wafers (>30% global share) "
        "and a dominant force in PVC and specialty silicones. Its semiconductor wafer business is "
        "deeply embedded in the global fab supply chain — every major logic and memory chipmaker "
        "relies on Shin-Etsu substrates, creating near-irreplaceable switching costs. The company "
        "holds a critical-node position (B4=5/5) reflecting its supply chain centrality. With 13 "
        "analyst buy ratings and capacity expansion underway to serve AI-driven wafer demand, the "
        "structural tailwinds are strong. The primary risk is USD/JPY sensitivity and lack of "
        "publicly available valuation data limiting score precision. Conviction is moat-driven "
        "pending financial data confirmation. [Confidence: Low — financial data incomplete]"
    ),
    "CMP-0013": (
        "Fuso Chemical holds a near-monopoly in high-purity colloidal silica abrasives used in "
        "chemical mechanical planarization (CMP), a mandatory step in semiconductor manufacturing. "
        "Its PER of 17.1x sits at a discount to the G2 materials peer median, while PBR of 2.01x "
        "is modest for a niche monopolist. OPM of 17.8% and 7% revenue growth are solid for a "
        "specialty materials producer. As the most reliably scored company in the top 10 "
        "(81.5% data coverage, High confidence), this is the highest-conviction pick: a "
        "structurally protected business at a reasonable valuation with no forex sensitivity, "
        "capacity expansion plans, and strong policy tailwinds from Japan's semiconductor "
        "industrial policy. Key risk: small market cap (JPY 220B) limits institutional liquidity. "
        "[Confidence: High]"
    ),
    "CMP-0044": (
        "Stella Chemifa is one of the world's few producers of electronics-grade hydrofluoric acid "
        "(HF) and fluorine compounds critical for semiconductor etching. Japan's 2019 export "
        "controls on HF to South Korea spotlighted the geopolitical leverage this supplies: "
        "Samsung and SK Hynix were forced to rapidly diversify away from Japanese HF, underscoring "
        "both the product's irreplaceability and Japan's supply control. Stella achieves a perfect "
        "moat score (B=25/25), combining dominant market share, maximum switching costs, and "
        "maximum technical differentiation. AI-driven fab expansion globally drives structural "
        "HF demand growth. The thesis is entirely moat-driven as financial data is unavailable; "
        "this is a 'buy the structure, confirm the valuation' situation. "
        "[Confidence: Very Low — research data required before sizing]"
    ),
    "CMP-0001": (
        "Tokyo Seimitsu (Accretech) occupies dual leadership positions: semiconductor probers "
        "(testing wafer-level ICs) and precision coordinate measuring machines (CMM). Its probers "
        "compete directly with Teradyne and form an oligopoly in advanced node testing. At PER "
        "21.3x vs the G1 equipment peer median of 26.3x, the stock trades at a meaningful "
        "discount despite 11.8% revenue growth and 50% foreign ownership — indicating "
        "institutional recognition of quality. The stock sits near its 52-week high "
        "(JPY 15,820 vs high JPY 16,170), signaling momentum. China revenue at 34% is an "
        "elevated geopolitical risk. No active buyback reduces near-term capital return appeal. "
        "Catalyst: continued AI-driven capex at TSMC and Samsung driving prober demand. "
        "[Confidence: High — scored on 81.5% data coverage]"
    ),
    "CMP-0035": (
        "Maruzen Petrochemical is a specialty chemical producer supplying base materials for "
        "semiconductor photoresists and other process chemicals. It achieves maximum scores on "
        "market share (10/10) and switching costs (5/5) within its niche — photoresist base "
        "chemicals are purity-critical and qualification cycles at fabs take years, making "
        "substitution prohibitively costly. As semiconductor lithography advances to EUV and "
        "beyond, demand for ultra-high-purity photoresist materials compounds. Policy tailwinds "
        "from Japan's semiconductor industrial policy (Rapidus, TSMC Kumamoto) provide domestic "
        "demand uplift. The thesis rests on structural moat; financial validation is the key "
        "next step to confirm valuation. "
        "[Confidence: Very Low — no financial data available]"
    ),
    "CMP-0056": (
        "Daifuku is the world's dominant provider of automated material handling systems (AMHS) "
        "and overhead transport (OHT) for semiconductor fabs — the internal logistics backbone "
        "that moves wafers between process steps. Every new fab built globally (TSMC Arizona, "
        "Samsung Texas, Intel Ohio, Rapidus Hokkaido) requires Daifuku's systems, creating a "
        "direct and durable leverage to the global fab construction boom driven by AI chip "
        "demand. Switching costs are maximal once a fab's AMHS is installed. The company scores "
        "perfectly on market share and switching costs. As the global fab capex cycle accelerates "
        "through 2026-2028, Daifuku's order backlog is structurally positioned to grow. "
        "Financial data needed to validate entry timing. "
        "[Confidence: Very Low — no financial data available]"
    ),
    "CMP-0006": (
        "Lasertec is the sole global supplier of EUV photomask inspection systems — there is no "
        "substitute. Every EUV-enabled chip (Apple, NVIDIA, AMD, Qualcomm at 7nm and below) "
        "requires masks inspected on Lasertec equipment before production. This creates an "
        "absolute monopoly with perfect moat scores (B=25/25) and a critical-node position. "
        "The financial profile validates the moat: OPM 42.88% (best-in-class for equipment), "
        "revenue growth 32.5% YoY, with the stock pulling back 23% from its 52-week high — "
        "creating an attractive re-entry point. PER 33.1x appears elevated but is modest for "
        "a secular monopolist growing at 30%+. The primary risks are customer concentration "
        "(TSMC and Samsung dominate demand) and USD/JPY forex exposure. "
        "[Confidence: High — 81.5% data coverage, complete scoring]"
    ),
    "CMP-0042": (
        "PILLAR Corporation is the leading manufacturer of ultra-high-purity fluoropolymer fluid "
        "control components — fittings, valves, and pumps — used in chemical delivery systems "
        "inside semiconductor fabs. These components handle aggressive acids, solvents, and "
        "ultra-pure water where contamination tolerance is essentially zero. Achieving maximum "
        "scores on market share, switching costs, and technical differentiation (B=21/25), "
        "PILLAR occupies a quiet but essential position in fab infrastructure. Every new fab "
        "built globally — and every tool installed — requires PILLAR's components, providing "
        "direct leverage to the AI-driven global capex boom. Low market visibility means this "
        "is under-researched relative to its structural moat. Financial validation is required "
        "before high-conviction sizing. "
        "[Confidence: Very Low — no financial data available]"
    ),
    "CMP-0004": (
        "Tokyo Electron (TEL) is Japan's largest semiconductor equipment company and the global "
        "#3 overall (after ASML and Applied Materials), with leading positions in "
        "coater-developers, thermal processing, and etch systems. Its critical-node score "
        "(B4=5/5) reflects the highest supply chain centrality among equipment makers in this "
        "database. Financially, TEL delivers exceptional results: JPY 17.4T market cap, 32.8% "
        "revenue growth, 28.7% OPM, with an active buyback program and 1.27% dividend yield. "
        "At PER 29.1x — only a modest premium to peers given the growth rate — the stock is "
        "reasonably priced for a secular compounder. Foreign ownership at 59.5% reflects global "
        "institutional conviction. China revenue at ~30% is the key geopolitical risk. "
        "The world's AI infrastructure buildout is TEL's multi-year structural tailwind. "
        "[Confidence: High — 86.2% data coverage, complete scoring]"
    ),
    "CMP-0028": (
        "NVIDIA is the essential AI infrastructure company: its H100/H200/Blackwell GPUs and "
        "the CUDA software ecosystem form an entrenched monopoly in AI compute that no "
        "competitor has successfully displaced despite massive investment from AMD, Intel, and "
        "hyperscaler custom silicon programs. In the context of this supply chain map, NVIDIA "
        "is the demand anchor — its GPU production drives demand for every company in this "
        "database: TEL for CVD/etch tools, Lasertec for mask inspection, Shin-Etsu for wafers, "
        "Stella Chemifa for HF etchants, Daifuku for fab logistics. Perfect moat score "
        "(B=25/25). The core investment thesis is that NVIDIA's dominance sustains elevated "
        "semiconductor equipment and materials demand for 3-5 years, making it the demand-side "
        "anchor of the entire supply chain thesis. As a USD-listed mega-cap ($4.65T), it "
        "represents a different risk/return profile from the Japanese names in this database. "
        "[Confidence: Very Low in JPY scoring context — financial data in USD, not JPY-native]"
    ),
}


def main():
    with open("evaluation_progress.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    companies = data["companies"]
    applied = 0
    for c in companies:
        cid = c["id"]
        if cid in THESES:
            c["investmentThesis"] = THESES[cid]
            applied += 1

    print(f"Applied investment theses to {applied} companies")

    with open("evaluation_progress.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Saved evaluation_progress.json")
    print()

    # Verify
    for c in companies:
        if c.get("investmentThesis"):
            print(f"  {c['id']} {c['ticker']:10s} finalScore={c.get('finalScore'):5.1f}  "
                  f"thesis={len(c['investmentThesis'])} chars")


if __name__ == "__main__":
    main()
