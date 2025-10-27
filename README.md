# Boston-Bus-Equity-CS506-Final-Project

[![BU Spark!](https://img.shields.io/badge/BU%20Spark!-Project-red.svg)]()

## Table of Contents
1. [Project Description](#project-description)  
2. [Goals of the Project](#goals)  
3. [Data](#data)   
4. [Modeling Plan](#modeling-plan)  
5. [Visualization Plan](#visualization-plan)  
6. [Test Plan](#test-plan)  

---

## Project Description

This project looks at MBTA bus service performance and equity across Boston. We use ridership and reliability data to study trends in passenger demand, travel times, wait times, and delays. The analysis also examines whether service differences affect communities differently, considering factors like race, income, and age. We aim to highlight improvements and disparities in MBTA service by comparing the patterns before and after the pandemic and across key bus routes.

---

## Goals of the Project
1.	Measure ridership patterns and travel times across MBTA bus routes.
2.	Evaluate wait times, delays, and overall service reliability.
3.	Identify disparities in service quality and analyze how they relate to community characteristics (e.g., race, income, age). This will primarily involve regression and explanatory modeling.
4.	Compare service trends in the pre-pandemic (2018–2019), pandemic (2020–2021), and post-pandemic (2022–2025) periods to better understand how travel behavior and service reliability have shifted.

---

## Data

We will focus on the datasets most relevant to our objectives, and once cleaned and finalized, we plan to upload them to Kaggle or Hugging Face for reproducibility.
1.	**Ridership**
	•	MBTA Bus Ridership by Trip, Season, Route, Line, and Stop
Provides detailed ridership counts broken down by trip, route, stop, and season.
2.	**Reliability**
	•	MBTA Bus Arrival Departure Times (2018–2025)
Contains historical arrival and departure records for MBTA buses. Essential for analyzing delays, wait times, and travel time reliability.
3.	**Passenger Demographics**
	•	MBTA 2024 System-Wide Passenger Survey Data
A survey-based dataset capturing passenger demographics (e.g., age, race, income, commute purpose). Key for connecting service disparities to community characteristics.
4.	**(Optional, if time permits) Live/Derived Data**
	•	MBTA V3 API — Real-time vehicle positions, trip updates, and predictions.
	•	MBTA Performance Feed — Aggregated performance metrics summarizing service quality indicators such as reliability and ridership trends.

---

## Modeling the Data

We will begin with exploratory data analysis to identify key trends and relationships.
1. Time Series Models: Since bus arrivals and ridership are sequential data, models such as RNNs or LSTMs may be more effective than standard regression in capturing temporal dynamics.
2. Regression / Explanatory Models: Used to identify how service quality relates to community demographics.
3. Tree-Based Methods (e.g., Decision Trees, XGBoost): Helpful for predicting delays or classifying reliability patterns.
4. Clustering: To group bus routes with similar ridership or delay patterns.

The modeling approach will be refined as the project progresses, depending on data quality and complexity.

---

## Data Visualization

Our visualizations will focus on making trends easy to understand and compare. We plan to use:
1. Route maps to show delays across neighborhoods.
2. Scatter plots to highlight relationships between service performance and community factors.
3. Time-series charts to track ridership changes across pre-, during-, and post-pandemic periods.
4. Interactive dashboards (if time allows) to explore bus route performance and equity patterns.

---

## Test Plan
1.	Train the model on earlier time periods and test on more recent data to evaluate performance over time.
2.	Withhold 20% of the routes during training to assess how well the model generalizes to unseen routes.
3.	Compare prediction errors (e.g., residuals or MAE) across different demographic groups to ensure results are not biased.

---

# Mid-term Report

---

## Preliminary Visualizations of Data
[![BU Spark] (images/<img width="1481" height="884" alt="Top 20 routes by record count" src="https://github.com/user-attachments/assets/47cd60f9-591a-40cd-b0af-c6a89612070d" />)


