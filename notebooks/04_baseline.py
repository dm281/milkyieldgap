"""
04_baseline.py

Week 5 — Baseline and experimental design
Predictive Dairy Performance Analytics for Farm Consulting

The baseline was estimated in JMP on the local table lactations_with_farmid.
This script records the Section VI result. It does not read farm rows.
"""

from __future__ import annotations

FIT_END = "2026-02-28"
HOLDOUT_START = "2026-03-01"
HOLDOUT_END = "2026-08-29"

N_HOLDOUT = 1_456_157
MAE = 17.03
RMSE = 22.00
MEAN_SIGNED = 1.52


def section(title: str) -> None:
    print("\n" + title)
    print("-" * len(title))


def main() -> None:
    section("1. Baseline specification")
    print("Expected milk = mean within lactation group,")
    print("calendar month of fresh date, and 10-day DIM bin.")
    print(f"Fit window ends {FIT_END}.")
    print(f"Holdout: {HOLDOUT_START} through {HOLDOUT_END}.")
    print("Baseline is deterministic. Later stochastic steps use seed 42.")

    section("2. Holdout result")
    print(f"Slots scored: {N_HOLDOUT:,}")
    print(f"MAE: {MAE:.2f} lb")
    print(f"RMSE: {RMSE:.2f} lb")
    print(f"Mean signed error: {MEAN_SIGNED:+.2f} lb")
    print("A later model must reduce holdout MAE below 17.03 lb.")

    section("3. What is not claimed")
    print("No constraint ranking has been performed.")
    print("Diet and housing remain data gaps.")
    print("No advanced model has been fit.")


if __name__ == "__main__":
    main()
