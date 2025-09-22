# Boston-Bus-Equity-CS506-Final-Project


[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Made with ❤️ for BU Spark!](https://img.shields.io/badge/BU%20Spark!-Project-red.svg)]()

## Table of Contents
1. [Project Description](#project-description)
2. [Goals](#goals)
3. [Data](#data)
  3.1. [What we collect](#what-we-collect)
  3.2. [How we collect it](#how-we-collect-it)
4. [Modeling Plan](#modeling-plan)
5. [Visualization Plan](#visualization-plan)
6. [Test Plan](#test-plan)

---

## Project Description
This project looks at MBTA bus service performance and equity across Boston. We use ridership and reliability data to study trends in passenger demand, travel times, wait times, and delays. The analysis also examines whether service differences affect communities differently, considering factors like race, income, and age. We aim to highlight improvements and disparities in MBTA service by comparing the patterns before and after the pandemic and across key bus routes. 

---

## Goals of the Project
- Measure ridership patterns and travel times across MBTA bus routes.
- Evaluate wait times, delays, and overall service reliability.
- Identify disparities in service quality and see how they relate to community characteristics (e.g., race, income, age).
- Compare pre- and post-pandemic service trends to understand long-term changes.

---

## Data

### What we collect
- **Ridership**
  - Bus ridership by trip/season/route/stop
  - System-wide passenger survey (e.g., 2023)
- **Reliability**
  - Bus arrival & departure times (historical 2018–2024 where available)
- **Equity context**
  - Census/ACS (race, income, age, commute time)
  - Bus stop coordinates (PATI), route shapes
- **(Optional) Live/derived**
  - MBTA V3 API, MBTA performance feed
  - Weather data (if used for predictive delay models)

> 🔗 Put the exact dataset links from your project PDF into `data/README.md` (see repo structure below).

### How we collect it
- **Bulk downloads** from MBTA/MassDOT open data portals (CSV/GeoJSON).
- **Programmatic pulls** via small Python fetchers:
  - `src/data/download_mbta.py` (static datasets)
  - `src/data/fetch_mbta_api.py` (V3 API if used)
- **Census/ACS extracts** via pre-downloaded CSVs or API helpers.

All raw files live in `data/raw/` (read-only). Cleaning scripts write to `data/clean/` and analysis-ready tables to `data/processed/`.

---

## Modeling Plan
- **Descriptive + Time Series:** trends in ridership, headways, delays (per route, per season).
- **Geospatial joins:** routes/stops ↔ census tracts to compute equity metrics.
- **Regression (baseline):** linear/Poisson/negative binomial models for delay/ridership vs. features (route, time-of-day, headway, neighborhood indicators).
- **Clustering (optional):** group routes by reliability patterns.
- **Predictive (stretch):** gradient boosting / random forest / XGBoost to predict delay risk; feature importance to surface drivers.

> We’ll document model specs, assumptions, and diagnostics in `reports/final_report.md`.

---

## Visualization Plan
- **Time series**: pre- vs post-pandemic trends by route/line.
- **Heatmaps**: avg delay or on-time % by route × time-of-day.
- **Maps**: choropleths of service metrics overlaid with demographics; stop-level markers for extremes.
- **Comparative bars**: target routes vs. citywide average (with CIs).
- **Interactive (optional)**: Plotly/Power BI dashboards; t-SNE/UMAP for route clustering.

Each figure has a **caption, data source, and takeaway**. We’ll keep at least **5–7** core visuals to address base questions.

---

## Test Plan
- **Temporal holdout:** train on 2018–2022, validate on 2023–2024.
- **Route holdout (robustness):** withhold 20% of routes when fitting predictive models; report generalization.
- **Cross-validation:** k-fold where applicable.
- **Fairness checks:** compare residuals/MAE across demographic strata to ensure conclusions aren’t artifacts of sampling/coverage.
- **Sensitivity analyses:** alternative definitions of “on-time” (e.g., ±1, ±3, ±5 min), alternate aggregation levels (stop vs. route).

---

## Reproducibility

### Quickstart (Python / Colab)
```bash
# clone
git clone https://github.com/<your-org>/<your-repo>.git
cd <your-repo>

# create env
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# populate data folders (put dataset links in data/README.md)
# then run the pipeline
python -m src.data.make_dataset           # raw -> clean
python -m src.features.build_features     # clean -> processed
python -m src.models.run_baselines        # fits + metrics
python -m src.visualization.make_figures  # saves plots to reports/figures/
