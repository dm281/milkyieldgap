## Repository layout

    milkyieldgap/
    ├── README.md
    ├── data/
    │   ├── README.md
    │   ├── raw/
    │   └── processed/
    ├── notebooks/
    │   ├── 01_data_preparation.py
    │   ├── 02_exploratory_analysis.py
    │   ├── 03_statistics_visualization.py
    │   ├── 04_baseline.py
    │   ├── 05_models.py
    │   └── 06_evaluation.py
    ├── src/
    │   └── preprocessing.py
    └── figures/
        ├── fig4_lactation_curve.png
        ├── fig5_event_rates.png
        ├── fig6_farm_size.png
        ├── fig7_milk1_dist.png
        ├── fig8_milk1_by_month.png
        └── fig9_mae_by_lactgrp.png

## Status

- Week 1: research design, data description, governance.
- Week 2: data assessment, cleaning rules, feature design, temporal holdout.
- Week 3: exploratory summaries from JMP on the local table `lactations_with_farmid`.
- Week 4: visualization and interpretation. Figures 6–8 are in `figures/`.
- Week 5: baseline. Stratified mean within lactation group, month, and 10-day DIM bin.
- Week 6: candidate models (linear, Wilmink, decision tree). None beat the baseline on holdout MAE.
- Week 7: evaluation and validation. Same 1,459,739 holdout slots. MAE: baseline 17.00 lb, tree 17.22, Wilmink 17.88, linear 19.49. R²: 0.333, 0.322, 0.272, 0.153. Baseline error rises with parity (14.01 / 17.47 / 19.56 lb). No model is declared best. Figure 9 is in `figures/`.

## How to run (no farm rows required)

    python notebooks/02_exploratory_analysis.py
    python notebooks/03_statistics_visualization.py
    python notebooks/04_baseline.py
    python notebooks/05_models.py
    python notebooks/06_evaluation.py
