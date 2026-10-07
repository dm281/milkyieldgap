# YieldGap

**Predictive Dairy Performance Analytics for Farm Consulting**

D. Darren McGee 
Mississippi State University — Master of Applied Data Science Capstone (DSCI 8413, Fall 2026)

## Research objective

Estimate signed milk-production gaps at cow-lactation and herd level from an Elanco Knowledge Solutions Dairy Data Access System extract, and rank only those bottleneck classes the records can support.

## Data sources

- Primary: Elanco EKS Dairy Data Access System, table `EKS_Dairy_36_month_2026-09-01_090118_Lactations` (4,803,135 cow-lactation rows; 250 columns; 320 coded farms after dropping 10,875 rows with a missing herd code; fresh dates 29 Aug 2023–29 Aug 2026).
- Farm names and herd codes are **not** in this repository. Analysis uses a random `FarmID` from a private crosswalk stored only in the Elanco workspace.
- Later (not this week): optional herd-level feed-delivery and milk-shipment files for the DDAS+ subset.

## Repository layout

    milkyieldgap/
    ├── README.md
    ├── data/
    │   ├── README.md
    │   ├── raw/          # empty on GitHub — raw extract stays at Elanco
    │   └── processed/    # empty on GitHub — processed tables stay at Elanco
    ├── notebooks/
    │   ├── 01_data_preparation.py
    │   └── 02_exploratory_analysis.py
    ├── src/
    │   └── preprocessing.py
    └── figures/
        ├── fig4_lactation_curve.png
        └── fig5_event_rates.png

## Status

- Week 1: research design, data description, governance.
- Week 2: data assessment, cleaning rules, feature design, temporal holdout.
- Week 3: exploratory summaries from JMP on the local table `lactations_with_farmid`. The notebook records those counts and the two manuscript figures. The signed gap has not been fit. No accuracy is reported.

## How to run (no farm rows required)

    python notebooks/02_exploratory_analysis.py

The script prints the Section IV counts. It does not read the extract.

## License / use

Course repository. Elanco-housed records remain internal. Do not commit raw extracts, `AccountName`, `HerdCode`, or `herd_crosswalk`.
