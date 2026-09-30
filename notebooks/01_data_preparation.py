"""
01_data_preparation.py

Week 2 — Data preparation, wrangling, and feature design
Predictive Dairy Performance Analytics for Farm Consulting

This script records the Section III decisions. Quality counts come from a
JMP audit of the local table lactations_with_farmid. Raw farm rows are not
read from this repository.

Story:
1. Load (local path only)
2. Inspect documented size and grain
3. Identify quality problems
4. Cleaning rules
5. Integration (FarmID only)
6. Feature design
7. Leakage / time holdout
8. Do not write processed rows back to GitHub
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from preprocessing import (
    JMP_AUDIT,
    FIT_END,
    FIT_START,
    HOLDOUT_ELIGIBLE_FSH_END,
    HOLDOUT_END,
    HOLDOUT_START,
    MILK_SLOTS,
    TRANSITION_YN,
    MASTITIS_YN,
)


def section(title: str) -> None:
    print("\n" + title)
    print("-" * len(title))


def main() -> None:
    section("1. Load")
    data_path = os.environ.get("YIELDGAP_DATA")
    if data_path:
        print(f"Local analysis file: {data_path}")
        print("Do not commit this file.")
    else:
        print("YIELDGAP_DATA is not set.")
        print("Documented JMP audit will be printed. No farm rows will be read.")

    section("2. Inspect (JMP audit of the raw extract)")
    a = JMP_AUDIT
    print(f"Rows                {a['n_rows']:,}")
    print(f"Columns             {a['n_columns']}")
    print(f"Fresh-date window   {a['fshdate_min']} to {a['fshdate_max']}")
    print(f"Accounts            {a['n_accountname_unique']}")
    print(f"Herd codes          {a['n_herdcode_unique']}")
    print("Grain: cow-lactation. Farm key on the analysis copy is FarmID.")

    section("3. Quality problems")
    print(f"Missing HerdCode                  {a['n_missing_herdcode']:,}")
    print(f"Missing Bdate                     {a['n_missing_bdate']:,}")
    print(f"Lact missing, <1, or >19          {a['n_bad_lact']:,}")
    print(f"Extra key rows                    {a['n_extra_key_rows']:,}")
    print(f"Missing FshDate                   {a['n_missing_fshdate']}")
    print(f"Zero Milk1–Milk9 slots            {a['n_zero_milk_slots']:,} ({a['pct_zero_milk_slots']}%)")
    print(f"All nine slots filled             {a['n_nine_milk_slots']:,} ({a['pct_nine_milk_slots']}%)")
    print(f"Open lactations (no ArchDate)     {a['n_open_lactations']:,}")
    print(f"Archived lactations               {a['n_archived_lactations']:,}")
    print(f"Impossible milk or DIM            {a['n_impossible_milk_or_dim']}")
    print(f"Milk > 250 lb (kept)              {a['n_milk_gt_250']}")
    print(f"DIM > 800 d (kept)                {a['n_dim_gt_800']}")

    section("4. Cleaning rules (no imputation of milk)")
    print("Drop AccountName and HerdCode from every shared file.")
    print("Exclude bad Lact from expected-yield and gap calculations.")
    print("Drop exact duplicate keys after inspection; keep true re-fresh events.")
    print("Do not fill missing Milk1–Milk9. No test-day gap if all nine are empty.")
    print("Do not delete milk > 250 or DIM > 800.")
    print("Do not use Milk at Test, DIM at Test, 305-day ME, or lifetime yield in the fit.")
    print("YN health flags are complete; DIM* event dates are timing only.")
    print("Diet and housing are data-gap flags, not imputed causes.")

    section("5. Integration")
    print("No feed-delivery or shipment join this week.")
    print("FarmID comes from a 320-row private crosswalk. Crosswalk is not in this repo.")

    section("6. Feature design")
    print("Stack", ", ".join(MILK_SLOTS), "with aligned DIM and component slots.")
    print("Signed gap G = observed milk − expected(DIM, lactation group, month of FshDate).")
    print("Constraint flags:", ", ".join(TRANSITION_YN + MASTITIS_YN), "plus MASTCount, LAMECount.")
    print("Data-gap flags: diet, housing/stocking.")
    print("Month of FshDate is taken only from that lactation.")

    section("7. Leakage / time holdout")
    print(f"Fit window:     {FIT_START} through {FIT_END}")
    print(f"Holdout window: {HOLDOUT_START} through {HOLDOUT_END}")
    print("Score only holdout slots that exist (right-censored extract).")
    print(f"Whole-lactation check: FshDate through {HOLDOUT_ELIGIBLE_FSH_END} or at least two milk slots.")
    print("Summarize holdout gaps by month of calving.")

    section("8. Processed output")
    print("Processed tables stay next to the raw extract in the Elanco workspace.")
    print("This repository stores rules and encoded summaries only.")


if __name__ == "__main__":
    main()
