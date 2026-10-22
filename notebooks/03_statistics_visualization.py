"""
03_statistics_visualization.py

Week 4 — Data visualization and interpretation
Predictive Dairy Performance Analytics for Farm Consulting

Counts were produced in JMP on the local table lactations_with_farmid.
This script records the Section V results and can redraw Figures 6–8.
It does not read farm rows.
"""

from __future__ import annotations

N_ROWS = 4_803_135
N_CODED_FARMS = 320

# Farm size bins (exact)
FARM_BINS = {
    "<100": 8,
    "100–999": 12,
    "1,000–19,999": 217,
    "≥20,000": 83,
}
TOP20_SHARE_PCT = 26.5

# Milk1 summary (non-missing)
MILK1 = {
    "n": 3_884_829,
    "missing": 918_306,
    "mean": 82.8,
    "sd": 27.9,
    "median": 82,
    "q25": 64,
    "q75": 102,
    "min": 1,
    "max": 372,
}

# Mean Milk1 by calendar month of fresh date
MONTH_MEANS = {
    1: 82.34, 2: 82.05, 3: 83.59, 4: 83.50,
    5: 84.14, 6: 84.00, 7: 82.84, 8: 81.82,
    9: 82.13, 10: 82.36, 11: 82.27, 12: 83.16,
}


def section(title: str) -> None:
    print("\n" + title)
    print("-" * len(title))


def main() -> None:
    section("1. Farm size (Figure 6)")
    for k, v in FARM_BINS.items():
        print(f"  {k}: {v} farms")
    print(f"Top 20 farms share of coded rows: {TOP20_SHARE_PCT}%")
    print("Herd briefs are reported within farm.")

    section("2. Milk1 distribution (Figure 7)")
    print(f"N non-missing: {MILK1['n']:,}")
    print(f"Mean {MILK1['mean']}  Median {MILK1['median']}  IQR {MILK1['q25']}–{MILK1['q75']}")
    print("Roughly symmetric; no transformation indicated for the baseline.")

    section("3. Mean Milk1 by month of fresh date (Figure 8)")
    for m, val in MONTH_MEANS.items():
        print(f"  Month {m:2d}: {val:.2f} lb")
    print("Range across months ≈ 2.3 lb. Month stays in the baseline.")

    section("4. Modeling implications recorded in Section V")
    print("- Expected milk depends on lactation group (Figure 4).")
    print("- Rank metritis, mastitis, retained placenta; ketosis less complete (Figure 5).")
    print("- Report within farm (Figure 6).")
    print("- Keep calendar month of fresh date (Figure 8).")
    print("Signed gap has not been fit. No accuracy is reported.")


if __name__ == "__main__":
    main()
