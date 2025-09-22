# Boston-Bus-Equity-CS506-Final-Project

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
- Measure ridership patterns and travel times across MBTA bus routes.
- Evaluate wait times, delays, and overall service reliability.
- Identify disparities in service quality and see how they relate to community characteristics (e.g., race, income, age).
- Compare pre- and post-pandemic service trends to understand long-term changes.

---

## Data

1. **Ridership**  
   - [MBTA Bus Ridership by Trip, Season, Route, Line, and Stop](https://mbta-massdot.opendata.arcgis.com/datasets/8daf4a33925a4df59183f860826d29ee/about)  
     Provides detailed ridership counts broken down by trip, route, stop, and season.

2. **Reliability**  
   - [MBTA Bus Arrival Departure Times (2018–2025)](https://mbta-massdot.opendata.arcgis.com/search?q=MBTA%20Bus%20Arrival%20Departure%20Times)  
     Contains historical arrival and departure records for MBTA buses. 

3. **Interactive tool for our "Rider Census"**  
   - [MBTA 2024 System-Wide Passenger Survey Data](https://mbta-massdot.opendata.arcgis.com/datasets/7da1f62034f64cb4bc9e2afefe9a1fdc_0/explore)  
     A survey-based dataset capturing passenger demographics (e.g., age, race, income, commute purpose).

4. **(If time permits) Live/derived**  
   - [MBTA V3 API](https://www.mbta.com/developers/v3-api)  
     Real-time API providing current vehicle positions, trip updates, and predictions.
     
   - [MBTA Performance Feed](https://www.mbta.com/performance-metrics)  
     Aggregated performance metrics published by MBTA, summarizing service quality indicators such as reliability and ridership trends.  
    
---

## Modeling the Data
We will begin with exploratory data analysis to identify key trends and relationships. Potential approaches include clustering to group routes with similar ridership or delay patterns, linear or regression models to study how service performance relates to demographic factors, and tree-based methods such as decision trees or XGBoost for predicting delays or reliability. As we gain more experience in class, the modeling approach will be refined to best match the data.


------

## Data Visualization 
Our visualizations will focus on making trends easy to understand and compare. We plan to use route maps to show delays across neighborhoods, scatter plots to highlight relationships between service performance and community factors, and time-series charts to track ridership changes before and after the pandemic. Interactive dashboards may also be developed to allow users to explore bus route performance and equity patterns directly.


---



## Test Plan
- Train the model on earlier time periods and test on more recent data to evaluate performance over time.
- Withhold 20% of the routes during training to assess how well the model generalizes to unseen routes.
- Compare prediction errors (e.g., residuals or MAE) across different demographic groups to ensure results are not biased.


---

