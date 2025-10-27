# Boston-Bus-Equity-CS506-Final-Project

[![BU Spark!](https://img.shields.io/badge/BU%20Spark!-Project-red.svg)]()

# Mid-term Report

## Table of Contents
1. [Preliminary Visualizations of Data](#1-preliminary-visualizations-of-data)  
2. [Data Processing](#2-data-processing)  
3. [Data Modeling Methods](#3-data-modeling-methods)  
4. [Preliminary Results](#4-preliminary-results)

---
## 1. Preliminary Visualizations of Data

- ### Top Routes

<br>

This visualization shows a bar chart of the top 20 bus routes with the highest number of records in the dataset. Each bar represents a route’s record count, labeled with exact values, and the y-axis is formatted for readability (in thousands). It highlights which routes have the most data entries in the sample.

<br>

<img width="700" height="300" alt="Top 20 routes by record count" src="https://github.com/user-attachments/assets/47cd60f9-591a-40cd-b0af-c6a89612070d" />

<br><br>

- ### Distribution of Scheduled Headways and Arrival Delays

<br>

This visualization presents two side-by-side histograms:
1. The left plot shows the distribution of scheduled headways (time gaps between buses), with vertical lines marking the mean and median values for comparison.
2. The right plot displays the distribution of arrival delays in minutes, highlighting reference lines at 0 minutes, 5 minutes, and the median delay.
Together, these plots illustrate how frequently different headway and delay values occur, revealing overall service regularity and punctuality.

<br>

<img width="700" height="300" alt="Scheduled Headway and Arrival Delay" src="https://github.com/user-attachments/assets/7a125b48-9923-490a-97b9-437e101cb0da" />

<br><br>

- ### Top Bus Routes by Late Arrival Rate

<br>

This visualization highlights the 15 bus routes with the highest percentage of late arrivals (delays greater than 5 minutes). Each bar represents a route’s late rate, expressed as a percentage of total recorded trips. The chart helps identify routes with consistent punctuality issues, while the accompanying table provides details such as average delay, data source used (“endpoint” or “all”), and the number of observations per route.

<br>

<img width="700" height="300" alt="top 15 lines which are late more often (by late rate more than 5 mins)" src="https://github.com/user-attachments/assets/25f3bc3d-4365-44cb-b4d9-c89c935a3f16" />

<br><br>

- ### Most-Late Routes in the Latest Year

<br>

This horizontal bar chart highlights the top 15 bus routes with the highest percentage of late trips (over 5 minutes delay) in the most recent year. It provides a quick view of which routes currently experience the most punctuality issues.

<br>

<img width="1175" height="700" alt="Most late routes in 2025 (late by more than 5 mins)" src="https://github.com/user-attachments/assets/4613c31a-e987-41d8-896c-01c4262fc094" />

<br><br>

- ### Yearly Late-Rate Trends

<br>

This line chart tracks the year-by-year lateness trends for the five worst-performing routes. It helps visualize whether each route’s performance is improving, worsening, or remaining consistent over time.

<br>

<img width="700" height="300" alt="late rate trends by year (top 5 worst routes)" src="https://github.com/user-attachments/assets/f423f38d-ca4f-42b1-8781-344b16f400fa" />

<br><br>

- ### Annual Lateness Heatmap for the Worst-Performing Routes

<br>

This heatmap compares lateness percentages across multiple years for the 20 routes with the highest overall late rates. Darker colors indicate higher lateness, revealing long-term patterns and consistently delayed routes.

<br>

<img width="700" height="300" alt="late rate percentage by route vs year (worst 20 routes overall)" src="https://github.com/user-attachments/assets/13cccbd7-9bd6-4fa7-ad54-be0c847176a6" />

<br><br>

---

## **2. Data Processing**

The data processing workflow was designed to clean, standardize, and align three large datasets from the Massachusetts Bay Transportation Authority (MBTA): the ridership data, the arrival–departure time data, and the 2024 system-wide passenger survey. The goal was to prepare a unified, high-quality dataset suitable for downstream modeling and clustering analysis.



### **I. Data Loading**

Three primary sources were used in this project.  
- **Passenger Survey Data** contained aggregated information from the MBTA’s 2024 System-Wide Passenger Survey, capturing respondents’ demographic attributes (e.g., income, race, travel mode, purpose).  
- **Bus Ridership Data** contained stop-level boarding, alighting, and load observations across several years and seasons from 2016 to 2024.  
- **Arrival–Departure Data** stored detailed service-level information such as headways, scheduled times, and earliness or lateness of bus arrivals for each route and direction.

Because of the large file sizes, each dataset was partially loaded (up to 30 million rows) to balance memory efficiency and coverage. The data was read using the pandas and PyArrow libraries, with all three dataframes printed and inspected to verify structure, column types, and consistency of key identifiers.



### **II. Route ID Normalization**

Each dataset represented MBTA routes in slightly different ways — for instance, `"01"`, `"1"`, `"1-0-0"`, and `"34E"` could all appear as route identifiers. A custom normalization process was implemented to make them comparable across datasets. All route IDs were converted to uppercase strings, extra whitespace and underscores were stripped, and leading zeros were removed for numeric-only IDs. This ensured that all datasets referred to each route consistently (e.g., `"01"` and `"1"` were treated as the same route).  

New normalized columns (such as `route_id_norm`) were created to store these standardized identifiers while keeping the raw data intact. This step was critical for accurate merging and comparison later in the pipeline.



### **III. Correction of Route Naming Errors**

Some route entries included inconsistencies such as suffix underscores (e.g., `"746_"`) or formatting anomalies. These were manually corrected using simple replacement rules. The normalization process was re-run afterward to ensure the corrections propagated consistently across all datasets.  

Unique route sets were then extracted from each dataset, and the intersections and differences were computed to identify:  
- Routes that appeared in all datasets, and  
- Routes that were missing from one or more datasets.

This comparison provided an early check on coverage and revealed a manageable overlap suitable for merging.



### **IV. Handling Multi-Route Entries in the Survey Data**

In the survey data, certain responses were grouped under combined route identifiers such as `"114&116&117"`, representing riders who used multiple closely related routes. These combined entries needed to be decomposed into separate route identifiers to allow one-to-one linkage with the operational data.

A regular expression pattern was developed to extract valid route codes (covering both numeric and alphanumeric patterns like `"SL1"`, `"CT2"`, and `"34E"`). Each multi-route entry was expanded into a Python list (for example, `"114&116&117"` became `["114", "116", "117"]`). The survey dataframe was then exploded so that each individual route received its own row. This ensured that demographic information could be accurately mapped to specific route identifiers.



### **V. Data Cleaning and Filtering**

Invalid or empty route entries were removed from the survey dataframe to maintain data integrity. Only rows containing at least one valid route ID were retained. Next, the intersection of route identifiers across all three datasets was calculated, leaving only the subset of routes that were present in the ridership, arrival–departure, and survey data simultaneously. This filtering step eliminated inconsistencies and ensured that subsequent analysis compared truly common routes.

The datasets were capped at a maximum of 30 million records each to prevent excessive memory usage. This cap was sufficient to capture all relevant data while ensuring smooth processing.



### **VI. Efficient Slicing and Indexing**

Since the datasets were large and Arrow-backed dataframes can trigger kernel crashes during boolean indexing, the filtering operations were optimized using NumPy-based indexing. Instead of traditional pandas filtering, boolean masks were converted into NumPy arrays of row indices, which were then used to slice the data directly. This approach improved stability and performance on large data volumes.  

Three masks were created:
- One for arrival–departure records (`mask_arr`)  
- One for ridership records (`mask_rid`)  
- One for survey entries (`mask_svy`)  

These masks identified rows associated with route IDs present in the intersection of all datasets. Using this approach, only relevant rows were retained, significantly reducing the size of the working data.



### **VII. Final Output Generation and Cleaned Data Summary**

After cleaning and aligning all datasets, the final step was to store them in a structured, analysis-ready format within a new directory named `data_cleaned_capped`.  

- **Arrival–departure data** was saved as a **Parquet file** to preserve data types and support large-scale I/O.  
- **Ridership** and **survey data** were saved as **CSV files** for easy inspection and compatibility with other tools.  

A **chunked writing approach** (50,000 rows per batch) was used to prevent memory overload during saving.  

All three datasets now share a **standardized route ID system**, ensuring full compatibility for integration. Invalid, duplicate, and malformed routes were removed, leaving only valid overlapping routes.  

**Final Outputs:**
- `arrival_departure.parquet` — stop-level operational metrics (headway, earliness).  
- `ridership.csv` — aggregated route-level boardings, alightings, and load data.  
- `survey.csv` — demographic and behavioral insights linked to valid routes.



### **VIII. Key Outcomes of Data Processing**

This data cleaning pipeline successfully integrated three disparate MBTA data sources into a consistent and scalable analytical base. The processed data now supports detailed route-level exploration of operational efficiency and rider demographics. It also establishes a reliable framework for advanced modeling tasks such as clustering, regression, or predictive analytics.  

By standardizing route identifiers, correcting inconsistencies, expanding multi-route survey entries, and efficiently filtering records, the pipeline ensures that all subsequent analyses are performed on harmonized, high-quality data.

---

## 3. Data Modeling Methods

Our goal was to explore whether operational and ridership characteristics of MBTA bus routes exhibit natural groupings and, subsequently, whether those groups correlate with demographic or socioeconomic patterns derived from the MBTA passenger survey data.



### I. Feature Construction
Three datasets were used:

- **Ridership Data (`ridership_df`)**  
- **Arrival–Departure Data (`arrival_departure_df`) **  
- **Survey Data (`survey_df`) **

From the ridership and arrival–departure datasets, we constructed route-level operational feature vectors.  
For each route, the following aggregated statistics were computed:

- **Ridership metrics:** mean and median boardings, alightings, and passenger load, as well as total record count and directional balance.  
- **Service metrics:** mean and standard deviation of headway, mean scheduled headway, mean earliness, number of unique stops, total observations, and a derived on-time performance rate (fraction of arrivals within ±60 seconds of schedule).

These features were merged into a single dataframe (`route_feat`), forming the analytical basis for clustering.



### II. Data Standardization
All numeric features were standardized using **z-score normalization** via `StandardScaler` from scikit-learn.  
This ensured that variables with different scales (e.g., “headway_mean” in minutes vs. “boardings_mean” in passenger counts) contributed equally to the clustering process.



### III. Clustering Approach

We applied **two unsupervised clustering methods**: **K-Means and Hierarchical Clustering** to identify homogeneous groups of routes based on their operational characteristics.

#### **K-Means Clustering**
- The number of clusters (*K*) was optimized by computing **silhouette scores** for values from 2 to 8.  
- The optimal *K=3* was selected for achieving the best balance between compactness and separation.
- The final model assigned a **cluster label** to each route and computed **centroids** in both scaled and original feature spaces.  
- A **PCA projection** (2D scatter plot) was used to visualize separability and density among clusters.
<br>

<img width="900" height="600" alt="Silhoutte vs K" src="https://github.com/user-attachments/assets/e54b226d-b0cc-4fc8-8c55-2e75f1d6e807" />

<br><br>

<img width="900" height="600" alt="K means cluster" src="https://github.com/user-attachments/assets/5befc26d-9a0d-40f3-9fbb-e8e6b4cc0cf4" />

<br><br>

#### **Hierarchical Clustering**
In addition to K-Means, we applied **agglomerative hierarchical clustering** to validate and compare the natural structure of route groupings.  
- Using the **Ward linkage** method (which minimizes within-cluster variance), we constructed a **dendrogram** illustrating the hierarchical relationships among routes.  
- Based on the dendrogram inspection and inconsistency coefficients, we cut the hierarchy into **4 major clusters**.  
- The cluster memberships from hierarchical clustering were compared to those from K-Means to assess **consistency and stability** of grouping patterns.
- Both approaches produced largely overlapping route clusters, confirming that the primary segmentation was robust to the choice of clustering algorithm.

<br>

<img width="700" height="300" alt="Hierarchical cluster dendogram" src="https://github.com/user-attachments/assets/db004e42-19bd-4797-a75c-32e8fe97a581" />

<br><br>

<img width="700" height="300" alt="Hierarchical cluster - pca projection" src="https://github.com/user-attachments/assets/dfc062ae-dbd2-4e3c-8475-95fc31c2a671" />

<br><br>


### IV. Demographic Correlation Analysis
To examine potential relationships between operational clusters and rider demographics:

- The **survey_df** was transformed into a long-form dataset (`survey_long`), exploding route arrays (e.g., `['114', '116', '117']`) into individual rows.  
- Routes were normalized to consistent identifiers (e.g., “1”, “34E”, “SL4”).  
- From `survey_long`, income-related and ethnicity-related categories were isolated using keyword-based filters.  
- For each demographic subset, **pivot tables (route × category)** were computed to capture mean weighted proportions, normalized to represent percentage distributions.  
- These tables were merged with cluster assignments (from both K-Means and Hierarchical Clustering) to evaluate demographic composition per cluster.  
- The results were visualized as **grouped bar charts** comparing proportions of income and ethnicity categories across clusters.



### V. Preliminary Results

**Cluster Formation:**  
K-Means identified **three** operationally distinct route groups, while Hierarchical Clustering revealed **four clusters**, indicating possible sub-patterns in route characteristics.

- **Cluster 1:** High passenger load and short headways — dense, high-frequency urban routes.  
- **Cluster 2:** Moderate load and balanced headways — regular city routes with steady ridership.  
- **Cluster 3:** Longer headways and lower passenger counts — typically suburban or low-demand routes.  
- **Cluster 4 (Hierarchical-only):** Transitional or hybrid routes showing moderate ridership but higher variability in headway and punctuality metrics.

**Visualization:**  
The **PCA scatter plot** and **dendrogram** showed partial separation between clusters, though overlaps were frequent.  
Cluster boundaries were not strongly distinct, suggesting that current feature combinations may not fully capture the underlying differences in route performance.

**Demographic Correlation:**  
No strong or systematic correlation was observed between route clusters and demographic distributions.  
Income and ethnicity proportions remained largely similar across all clusters, with only minor variations.

<br>

### Income Distribution obtained from K means

<br>

<img width="700" height="300" alt="Income dis per cluster" src="https://github.com/user-attachments/assets/bedf63c8-8b48-4a68-a76f-2f339bf15ca3" />

<br><br>

### Ethnicity Distribution obtained from K means

<br>

<img width="700" height="300" alt="Ethnicity dis per cluster" src="https://github.com/user-attachments/assets/073c28fd-0141-4d1f-954b-7e7a86bf03a5" />

<br><br>

### Income Distribution obtained from Hierarchical Clustering

<br>

<img width="1089" height="590" alt="Income dis per hierarchical cluster" src="https://github.com/user-attachments/assets/00a73f29-4dad-4b70-a6d4-91a6edb5548b" />

<br><br>
### Ethnicity Distribution obtained from Hierarchical Clustering
<img width="700" height="300" alt="Ethnicity dis per hierarchical cluster" src="https://github.com/user-attachments/assets/08041fef-5666-4da6-b634-58ed6c2bddb8" />

<br><br>

**Preliminary Insight:**  
Overall, the clustering results did not reveal clear or promising patterns.  
This suggests the need for **improved feature extraction**, potentially incorporating additional operational metrics (e.g., temporal demand variation, stop-level reliability) or refining existing ones to better represent the behavioral and service-level diversity among MBTA routes.





