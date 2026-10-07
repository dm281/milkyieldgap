"""
02_exploratory_analysis.py

Week 3 — Exploratory data analysis
Predictive Dairy Performance Analytics for Farm Consulting

Counts were produced in JMP on the local table lactations_with_farmid.
This script records those results and can redraw Figure 4 and Figure 5.
It does not read farm rows.
"""

from __future__ import annotations

import os
from pathlib import Path

N_ROWS = 4_803_135
N_MISSING_HERD = 10_875
N_CODED_ROWS = N_ROWS - N_MISSING_HERD
N_FARMS = 320

FARM_SIZE = {
    "median": 10199,
    "mean": 14976,
    "p25": 4100,
    "p75": 20972,
    "min": 1,
    "max": 96998,
    "n_lt_100": 8,
    "top20_share_pct": 26.5,
}

LACT_GRP = {
    0: 724,
    1: 1_734_749,
    2: 1_206_110,
    3: 1_861_552,
}

MILK1 = {"n": 3_884_829, "missing": 918_306, "mean": 82.8, "sd": 27.9, "median": 82, "min": 1, "max": 372}
DIM1 = {"n": 3_902_151, "missing": 900_984, "mean": 24.9, "sd": 16.3, "median": 23, "min": 1, "max": 568}

# Mean milk (lb) by test-day slot for lactation groups 1, 2, and 3. Group 0 omitted.
CURVE = {
    1: [65.44, 75.71, 77.54, 77.48, 77.84, 75.85, 74.55, 73.04, 71.30],
    2: [90.32, 99.60, 97.60, 94.87, 90.89, 87.22, 83.47, 79.48, 75.37],
    3: [94.00, 105.23, 102.94, 99.02, 90.82, 90.62, 86.24, 81.63, 76.78],
}

EVENTS = [
    ("Metritis", 326_447, 6.80),
    ("Mastitis", 180_743, 3.76),
    ("Retained placenta", 167_289, 3.48),
    ("Ketosis", 106_025, 2.21),
    ("Milk fever", 43_877, 0.91),
    ("Displaced abomasum", 27_286, 0.57),
]


def section(title: str) -> None:
    print("\n" + title)
    print("-" * len(title))


def main() -> None:
    section("1. Population")
    print(f"Rows in analysis table     {N_ROWS:,}")
    print(f"Missing HerdCode excluded  {N_MISSING_HERD:,}")
    print(f"Coded farms                {N_FARMS}")
    print(f"Coded-farm rows            {N_CODED_ROWS:,}")
    print(f"Lactations per farm        median {FARM_SIZE['median']:,}, mean {FARM_SIZE['mean']:,}")
    print(f"Farms with <100 lactations {FARM_SIZE['n_lt_100']}")

    section("2. Lactation group")
    for g, n in LACT_GRP.items():
        print(f"  group {g}: {n:,} ({100 * n / N_ROWS:.2f}%)")
    print("Group 0 is excluded from the baseline.")

    section("3. First test-day slot")
    print(f"Milk1  n={MILK1['n']:,}  mean={MILK1['mean']}  median={MILK1['median']}  missing={MILK1['missing']:,}")
    print(f"DIM1   n={DIM1['n']:,}  mean={DIM1['mean']}  median={DIM1['median']}  missing={DIM1['missing']:,}")

    section("4. Mean milk by slot (lb)")
    print("slot  " + "  ".join(f"g{g}" for g in (1, 2, 3)))
    for i in range(9):
        print(f"{i+1:>4}  " + "  ".join(f"{CURVE[g][i]:6.2f}" for g in (1, 2, 3)))

    section("5. First-30-day events recorded Yes")
    for name, n, pct in EVENTS:
        print(f"{name:<22} {n:>10,}  {pct:5.2f}%")
    print("A No is not recorded, not confirmed absence.")

    section("6. Findings used in Section IV")
    print("Expected milk must depend on lactation group.")
    print("Metritis, mastitis, and retained placenta are the usable constraint classes.")
    print("Herd briefs use 320 coded farms; tiny farms are not interpretable.")
    print("The signed gap has not been fit. No accuracy is reported.")

    if os.environ.get("YIELDGAP_DATA"):
        print("\nYIELDGAP_DATA is set. This script does not read it.")
    else:
        print("\nNo local extract read. Figures can be redrawn from the constants above.")


if __name__ == "__main__":
    main()
