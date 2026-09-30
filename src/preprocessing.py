"""
YieldGap Week 2 preprocessing rules.

These functions encode the decisions in Section III of the capstone paper.
They do not load Elanco rows. Call them from a local script that reads
lactations_with_farmid in the Elanco workspace.
"""

from __future__ import annotations

FIT_START = "2023-08-29"
FIT_END = "2026-02-28"
HOLDOUT_START = "2026-03-01"
HOLDOUT_END = "2026-08-29"
HOLDOUT_ELIGIBLE_FSH_END = "2026-05-31"

MILK_SLOTS = [f"Milk{i}" for i in range(1, 10)]
DIM_SLOTS = [f"DIM{i}" for i in range(1, 10)]

TRANSITION_YN = [
    "Metr1st30DaysYN",
    "RP1st30DaysYN",
    "Ket1st30DaysYN",
    "DA1st30DaysYN",
    "MilkFev1st30DaysYN",
]
MASTITIS_YN = ["Mast1st30DaysYN"]

# JMP audit on EKS_Dairy_36_month_2026-09-01_090118_Lactations
JMP_AUDIT = {
    "n_rows": 4_803_135,
    "n_columns": 250,
    "fshdate_min": "2023-08-29",
    "fshdate_max": "2026-08-29",
    "n_accountname_unique": 321,
    "n_herdcode_unique": 320,
    "n_missing_herdcode": 10_875,
    "n_missing_bdate": 22_167,
    "n_bad_lact": 758,
    "n_extra_key_rows": 1_364,
    "n_missing_fshdate": 0,
    "n_zero_milk_slots": 905_154,
    "pct_zero_milk_slots": 18.8,
    "n_nine_milk_slots": 1_994_398,
    "pct_nine_milk_slots": 41.5,
    "n_open_lactations": 1_599_777,
    "n_archived_lactations": 3_203_358,
    "n_milk_gt_250": 273,
    "n_dim_gt_800": 3,
    "n_impossible_milk_or_dim": 0,
}


def n_milk_slots(row: dict) -> int:
    return sum(row.get(c) is not None for c in MILK_SLOTS)


def is_bad_lact(lact) -> bool:
    if lact is None:
        return True
    try:
        value = float(lact)
    except (TypeError, ValueError):
        return True
    return value < 1 or value > 19


def slot_impossible(milk, dim) -> bool:
    if milk is not None and (milk < 0 or milk > 500):
        return True
    if dim is not None and (dim < 0 or dim > 5000):
        return True
    return False


def time_window(fshdate: str) -> str:
    """Return 'fit', 'holdout', or 'out_of_range' from an ISO fresh date."""
    if fshdate is None:
        return "out_of_range"
    if FIT_START <= fshdate <= FIT_END:
        return "fit"
    if HOLDOUT_START <= fshdate <= HOLDOUT_END:
        return "holdout"
    return "out_of_range"


def holdout_eligible_for_lactation_check(fshdate: str, n_slots: int) -> bool:
    if time_window(fshdate) != "holdout":
        return False
    if fshdate <= HOLDOUT_ELIGIBLE_FSH_END:
        return True
    return n_slots >= 2
