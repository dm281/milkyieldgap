"""
05_models.py

Week 6 — Candidate models
Predictive Dairy Performance Analytics for Farm Consulting

Models were fit in JMP on the local table lactations_with_farmid.
This script records the Section VI specifications and holdout counts.
It does not read farm rows.
"""

from __future__ import annotations

FIT_END = "2026-02-28"
HOLDOUT_START = "2026-03-01"
HOLDOUT_END = "2026-08-29"
SEED = 42

RESULTS = [
    ("Stratified mean (baseline)", 1_456_157, 17.03, 22.00, 1.52),
    ("Linear regression", 1_459_739, 19.49, 24.74, 1.45),
    ("Wilmink curve", 1_459_739, 17.95, 23.04, 0.61),
    ("Decision tree (18 splits)", 1_459_739, 17.22, 22.13, 2.97),
]


def section(title: str) -> None:
    print("\n" + title)
    print("-" * len(title))


def main() -> None:
    section("1. Shared design")
    print("Features: DIM, lactation group, month of fresh date.")
    print(f"Fit window ends {FIT_END}.")
    print(f"Holdout: {HOLDOUT_START} through {HOLDOUT_END}.")
    print("No 305-day ME, weekly milk, or FarmID in the expected-yield fit.")
    print(f"Random seed for the tree: {SEED}.")

    section("2. Model settings fixed before holdout")
    print("Baseline: mean within LactGrp, month, 10-day DIM bin.")
    print("Linear: additive DIM + LactGrp + month; ordinary least squares.")
    print("Wilmink: k = 0.05 fixed; additive LactGrp and month.")
    print("Tree: 18 splits; minimum split size 5,000; Partition platform.")

    section("3. Holdout results (preliminary)")
    print(f"{'Model':<32} {'Slots':>12} {'MAE':>8} {'RMSE':>8} {'Signed':>8}")
    for name, n, mae, rmse, signed in RESULTS:
        print(f"{name:<32} {n:>12,} {mae:>8.2f} {rmse:>8.2f} {signed:>+8.2f}")
    print("No model is declared best. Baseline remains the reference.")

    section("4. What is not claimed")
    print("No constraint ranking has been performed.")
    print("Diet and housing remain data gaps.")
    print("Full residual and robustness analysis remain for later weeks.")


if __name__ == "__main__":
    main()
