# Boston-Bus-Equity-CS506-Final-Project

## Table of Contents
1. [Project Description](#project-description)  
2. [Goals of the Project](#goals)  
3. [Data](#data)  
   3.1 [What we collect](#what-we-collect)  
   3.2 [How we collect it](#how-we-collect-it)  
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
- **(If time permits) Live/derived**
  - MBTA V3 API, MBTA performance feed
  - Weather data (if used for predictive delay models)


### How we collect it
- **Bulk downloads** from MBTA/MassDOT open data portals (CSV/GeoJSON).
- **Programmatic pulls** via small Python fetchers:
  - `src/data/download_mbta.py` (static datasets)
  - `src/data/fetch_mbta_api.py` (V3 API if used)
- **Census/ACS extracts** via pre-downloaded CSVs or API helpers.


---

## Modeling Plan
We will begin with exploratory data analysis to identify key trends and relationships. Potential approaches include clustering to group routes with similar ridership or delay patterns, linear or regression models to study how service performance relates to demographic factors, and tree-based methods such as decision trees or XGBoost for predicting delays or reliability. As we gain more experience in class, the modeling approach will be refined to best match the data.


---

## Visualization Plan
Our visualizations will focus on making trends easy to understand and compare. We plan to use route maps to show delays across neighborhoods, scatter plots to highlight relationships between service performance and community factors, and time-series charts to track ridership changes before and after the pandemic. Interactive dashboards may also be developed to allow users to explore bus route performance and equity patterns directly.
---

## Test Plan
- **Temporal holdout:** train on 2018–2022, validate on 2023–2024.
- **Route holdout (robustness):** withhold 20% of routes when fitting predictive models; report generalization.
- **Cross-validation:** k-fold where applicable.
- **Fairness checks:** compare residuals/MAE across demographic strata to ensure conclusions aren’t artifacts of sampling/coverage.
- **Sensitivity analyses:** alternative definitions of “on-time” (e.g., ±1, ±3, ±5 min), alternate aggregation levels (stop vs. route).

---

