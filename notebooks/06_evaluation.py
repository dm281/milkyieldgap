"""
06_evaluation.py

Week 7 — Model evaluation and validation
Predictive Dairy Performance Analytics for Farm Consulting

Models were fit in JMP on the local table lactations_with_farmid.
This script records the Section VII holdout metrics and the
lactation-group error breakdown. It does not read farm rows.
"""

from __future__ import annotations

RESULTS = [
    ("Stratified mean (baseline)", 1_459_739, 17.00, 481.59, 21.95, 0.333),
    ("Decision tree (18 splits)", 1_459_739, 17.22, 489.76, 22.13, 0.322),
    ("Wilmink curve", 1_459_739, 17.88, 525.84, 22.93, 0.272),
    ("Linear regression", 1_459_739, 19.49, 611.89, 24.74, 0.153),
]

BY_GROUP = [
    (1, 523_909, 14.01, 18.18),
    (2, 398_028, 17.47, 22.34),
    (3, 537_802, 19.56, 24.81),
]


def section(title: str) -> None:
    print("\n" + title)
    print("-" * len(title))


def main() -> None:
    section("1. Holdout performance (same 1,459,739 slots)")
    print(f"{'Model':<32} {'N':>12} {'MAE':>8} {'MSE':>10} {'RMSE':>8} {'R2':>8}")
    for name, n, mae, mse, rmse, r2 in RESULTS:
        print(f"{name:<32} {n:>12,} {mae:>8.2f} {mse:>10.2f} {rmse:>8.2f} {r2:>8.3f}")
    print("No model is declared best. Baseline remains the reference.")

    section("2. Baseline error by lactation group")
    print(f"{'Group':>6} {'N':>12} {'MAE':>8} {'RMSE':>8}")
    for g, n, mae, rmse in BY_GROUP:
        print(f"{g:>6} {n:>12,} {mae:>8.2f} {rmse:>8.2f}")
    print("Error increases from first to third-and-later lactations.")

    section("3. What is not claimed")
    print("No constraint ranking has been performed.")
    print("Diet and housing remain data gaps.")
    print("No seed test for the deterministic models.")


if __name__ == "__main__":
    main()
