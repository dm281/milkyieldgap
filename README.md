# YieldGap

**Predictive Dairy Performance Analytics for Farm Consulting**

D. Darren McGee  
Mississippi State University — Master of Applied Data Science Capstone (DSCI 8413, Fall 2026)

## Research objective

Estimate signed milk-production gaps at cow-lactation and herd level from an Elanco Knowledge Solutions Dairy Data Access System extract, and rank only those bottleneck classes the records can support.

## Data sources

- Primary: Elanco EKS Dairy Data Access System, table `EKS_Dairy_36_month_2026-09-01_090118_Lactations` (4,803,135 cow-lactation rows; 250 columns; 320 farms after dropping missing HerdCode; fresh dates 29 Aug 2023–29 Aug 2026).
- Farm names and herd codes are **not** in this repository. Analysis uses a random `FarmID` from a private crosswalk stored only in the Elanco workspace.
- Later (not this week): optional herd-level feed-delivery and milk-shipment files for a subset of farms.

## Repository layout

    milkyieldgap/
    ├── README.md
    ├── data/
    │   ├── README.md
    │   ├── raw/          # empty on GitHub — raw extract stays at Elanco
    │   └── processed/    # empty on GitHub — processed tables stay at Elanco
    ├── notebooks/
    │   └── 01_data_preparation.py
    ├── src/
    │   └── preprocessing.py
    └── figures/

## Status

- Week 1: research design, data description, governance.
- Week 2: data assessment, cleaning rules, feature design, temporal holdout. Quality counts were produced in JMP on the local analysis table `lactations_with_farmid`. The scripts here record those rules so they can be reproduced without putting farm rows on GitHub.

## How to run (local Elanco workspace only)

    export YIELDGAP_DATA=/path/to/lactations_with_farmid.csv
    python notebooks/01_data_preparation.py

If `YIELDGAP_DATA` is not set, the script prints the documented quality counts from the JMP audit and exits without reading a file.

## License / use

Course repository. Elanco-housed records remain internal. No raw extracts, `AccountName`, `HerdCode`, or `herd_crosswalk`.
