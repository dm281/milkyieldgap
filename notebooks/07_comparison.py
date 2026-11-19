"""
07_comparison.py
Week 8 — Comparative results and explainability notes.
Records the holdout ranking and the root split of the decision tree.
Does not read the raw extract.
"""

import pandas as pd
from pathlib import Path

# Holdout performance (same 1,459,739 slots for all models)
results = pd.DataFrame([
    {"Model": "Stratified mean (baseline)", "N": 1459739, "MAE_lb": 17.00, "RMSE_lb": 21.95, "R2": 0.333},
    {"Model": "Decision tree (18 splits)",   "N": 1459739, "MAE_lb": 17.22, "RMSE_lb": 22.13, "R2": 0.322},
    {"Model": "Wilmink curve",               "N": 1459739, "MAE_lb": 17.88, "RMSE_lb": 22.93, "R2": 0.272},
    {"Model": "Linear regression",           "N": 1459739, "MAE_lb": 19.49, "RMSE_lb": 24.74, "R2": 0.153},
])

print("Holdout comparison (fresh dates 1 Mar 2026 – 29 Aug 2026)")
print(results.to_string(index=False))
print()

# Root split of the fit-window tree on Milk1
print("Decision-tree root split (fit window, response = Milk1)")
print("  All rows:      N = 3,388,480   mean = 82.7 lb")
print("  LactGrp(0,1):  N = 1,212,554   mean = 65.4 lb")
print("  LactGrp(2,3):  N = 2,175,926   mean = 92.3 lb")
print()
print("The tree recovered the same parity grouping already used by the stratified-mean baseline.")
print("Subsequent splits continued to use days in milk and fresh month.")
print("Predictive importance is not evidence of causality.")

# Write a small results file that can be committed
out = Path(__file__).resolve().parent.parent / "data" / "processed" / "model_comparison.csv"
out.parent.mkdir(parents=True, exist_ok=True)
results.to_csv(out, index=False)
print(f"\nWrote {out}")
