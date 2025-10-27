# Boston-Bus-Equity-CS506-Final-Project

[![BU Spark!](https://img.shields.io/badge/BU%20Spark!-Project-red.svg)]()

# Mid-term Report

## Table of Contents
1. Preliminary Visualizations of Data (#data visualization)  
2. Data Processing (#description of data processing)  
3. Data modeling methods (#description of data modeling methods)   
4. Preliminary Results (#Preliminary results)   

---

## 1. Preliminary Visualizations of Data

<br><br>

- ### Top Routes

<br>

This visualization shows a bar chart of the top 20 bus routes with the highest number of records in the dataset. Each bar represents a route’s record count, labeled with exact values, and the y-axis is formatted for readability (in thousands). It highlights which routes have the most data entries in the sample.

<br>

<img width="1481" height="884" alt="Top 20 routes by record count" src="https://github.com/user-attachments/assets/47cd60f9-591a-40cd-b0af-c6a89612070d" />

<br><br><br>

- ### Distribution of Scheduled Headways and Arrival Delays

<br>

This visualization presents two side-by-side histograms:
1. The left plot shows the distribution of scheduled headways (time gaps between buses), with vertical lines marking the mean and median values for comparison.
2. The right plot displays the distribution of arrival delays in minutes, highlighting reference lines at 0 minutes, 5 minutes, and the median delay.
Together, these plots illustrate how frequently different headway and delay values occur, revealing overall service regularity and punctuality.

<br>

<img width="1935" height="735" alt="Scheduled Headway and Arrival Delay" src="https://github.com/user-attachments/assets/7a125b48-9923-490a-97b9-437e101cb0da" />

<br><br><br>

- ### Top Bus Routes by Late Arrival Rate

<br>

This visualization highlights the 15 bus routes with the highest percentage of late arrivals (delays greater than 5 minutes). Each bar represents a route’s late rate, expressed as a percentage of total recorded trips. The chart helps identify routes with consistent punctuality issues, while the accompanying table provides details such as average delay, data source used (“endpoint” or “all”), and the number of observations per route.

<br>

<img width="1175" height="700" alt="top 15 lines which are late more often (by late rate more than 5 mins)" src="https://github.com/user-attachments/assets/25f3bc3d-4365-44cb-b4d9-c89c935a3f16" />

<br><br><br>

- ### Most-Late Routes in the Latest Year

<br>

This horizontal bar chart highlights the top 15 bus routes with the highest percentage of late trips (over 5 minutes delay) in the most recent year. It provides a quick view of which routes currently experience the most punctuality issues.

<br>

<img width="1175" height="700" alt="Most late routes in 2025 (late by more than 5 mins)" src="https://github.com/user-attachments/assets/4613c31a-e987-41d8-896c-01c4262fc094" />

<br><br><br>

- ### Yearly Late-Rate Trends

<br>

This line chart tracks the year-by-year lateness trends for the five worst-performing routes. It helps visualize whether each route’s performance is improving, worsening, or remaining consistent over time.

<br>

<img width="1300" height="700" alt="late rate trends by year (top 5 worst routes)" src="https://github.com/user-attachments/assets/f423f38d-ca4f-42b1-8781-344b16f400fa" />

<br><br><br>

- ### Annual Lateness Heatmap for the Worst-Performing Routes

<br>

This heatmap compares lateness percentages across multiple years for the 20 routes with the highest overall late rates. Darker colors indicate higher lateness, revealing long-term patterns and consistently delayed routes.

<br>

<img width="1318" height="820" alt="late rate percentage by route vs year (worst 20 routes overall)" src="https://github.com/user-attachments/assets/13cccbd7-9bd6-4fa7-ad54-be0c847176a6" />

<br><br>

---

<!-- ## 3. Data Modeling Methods -->

<!-- - ### K-Means Variants

<br>

This line chart compares silhouette scores across different numbers of clusters (K = 2–6) for both standard k-means and k-means++ initializations.
It helps identify the optimal cluster count and shows which initialization method provides better-defined groupings of bus routes based on lateness and delay behavior.

<br>

<img width="1180" height="700" alt="Silhouette vs K" src="https://github.com/user-attachments/assets/001020bf-51ef-4d51-9733-259d04209140" />

<br><br><br>

- ### DBSCAN

<br>

This heatmap visualizes DBSCAN clustering performance for various combinations of eps and min_samples parameters.
Each cell’s color indicates the silhouette score, allowing quick assessment of how clustering quality changes with different neighborhood sizes and density thresholds.

<br>

<img width="902" height="556" alt="DBSCAN Silhouette heatmap" src="https://github.com/user-attachments/assets/41910437-e8ff-4a1d-a73a-e1e7306ea6bb" />

<br><br><br>

- ### Cluster Scatter Plots for Best Models

<br>

For each clustering method, this scatter plot displays routes grouped into clusters using their late rate (%) and average delay (minutes).
Clusters are color-coded and labeled from Low to High lateness, illustrating how routes naturally group based on punctuality and delay severity.

<br>

<img width="1180" height="700" alt="K means" src="https://github.com/user-attachments/assets/d3aa001a-5bea-458f-816e-da61174ad36e" />

<br><br>

<img width="1180" height="700" alt="K means ++" src="https://github.com/user-attachments/assets/f587d702-113f-4cc0-b686-71943fafe16e" />

<br><br>

<img width="1180" height="700" alt="DBSCAN" src="https://github.com/user-attachments/assets/9ab19890-89df-4036-84f8-fcfcc5f60e09" />

<br><br><br>

- ### Cluster Size Distribution per Method

<br>

These bar charts show the number of routes within each cluster for the best-performing model of each method (k-means, k-means++, and DBSCAN).
They provide insight into cluster balance, helping assess whether certain clusters dominate or if the segmentation is evenly distributed.

<br>

<img width="820" height="460" alt="Kmeans cluster size" src="https://github.com/user-attachments/assets/a40cac60-2c2f-494b-92a1-f48d32305ae1" />

<br>

<img width="820" height="460" alt="K means ++ cluster size" src="https://github.com/user-attachments/assets/0b9e20c9-bc43-48f0-85b8-d125d9db024d" />

<br>

<img width="820" height="460" alt="DBSCAN cluster size" src="https://github.com/user-attachments/assets/ad61d2e2-8573-4564-8d9d-afdaa0419ae6" />

<br><br><br>

- ### Overall Best Clustering Model (Highest Silhouette Score)

<br>

This final scatter plot visualizes the globally best clustering configuration across all tested models and parameters.
It highlights how routes are separated in lateness–delay space under the most effective model, representing the clearest and most meaningful route groupings in the analysis.

<br>

<img width="1255" height="700" alt="Overall Best - DBSCAN" src="https://github.com/user-attachments/assets/6271eb8b-ff54-453c-8899-6e3979e28d71" />

<br> -->


## **3. Data Modeling Methods**

Our goal was to explore whether operational and ridership characteristics of MBTA bus routes exhibit natural groupings and, subsequently, whether those groups correlate with demographic or socioeconomic patterns derived from the MBTA passenger survey data.

### **1. Feature Construction**
Three datasets were used:
- **Ridership Data** (`ridership_df`) — contained stop-level records of boardings, alightings, passenger loads, direction identifiers, and seasonal attributes.
- **Arrival–Departure Data** (`arrival_departure_df`) — included service reliability metrics such as headway, scheduled headway, and earliness (deviation from schedule) for each route and stop.
- **Survey Data** (`survey_df`) — summarized rider demographics and behaviors, including income levels, racial/ethnic background, and travel characteristics, aggregated by route reporting group.

From the ridership and arrival–departure datasets, we constructed **route-level operational feature vectors**.  
For each route, the following aggregated statistics were computed:
- *Ridership metrics:* mean and median boardings, alightings, and passenger load, as well as total record count and directional balance.
- *Service metrics:* mean and standard deviation of headway, mean scheduled headway, mean earliness, number of unique stops, total observations, and a derived on-time performance rate (fraction of arrivals within ±60 seconds of schedule).

These features were merged into a single dataframe (`route_feat`), forming the analytical basis for clustering.

### **2. Data Standardization**
All numeric features were standardized using **z-score normalization** via `StandardScaler` from *scikit-learn*.  
This ensured that variables with different scales (e.g., “headway_mean” in minutes vs. “boardings_mean” in passenger counts) contributed equally to the clustering process.

### **3. Clustering Approach**
We applied **K-Means clustering** to identify homogeneous groups of routes based on their ridership and service characteristics.  
To determine the optimal number of clusters (K), we computed **silhouette scores** for values of K = 2–8.  
The best-performing K=3 was selected as the one yielding the highest silhouette coefficient, balancing intra-cluster compactness and inter-cluster separation.

The final K-Means model was then trained on the standardized features, producing:
- A `cluster` label for each route.
- Cluster centroids (in both scaled and original feature space) for interpretability.

To visualize the clusters, a **Principal Component Analysis (PCA)** was conducted to project the high-dimensional route features into two principal components. The resulting 2D scatterplot illustrated separability and relative density among clusters.

### **4. Demographic Correlation Analysis**
To examine potential relationships between operational clusters and rider demographics:
1. The `survey_df` was transformed into a **long-form dataset** (`survey_long`), exploding routes listed as arrays (e.g., `['114','116','117']`) into individual rows.
2. Routes were normalized to consistent string identifiers (e.g., “1”, “34E”, “SL4”).
3. From `survey_long`, we isolated records containing *income-related* and *ethnicity-related* categories using keyword-based filters (`INCOME`, `RACE`, `ETHNIC`).
4. For each demographic subset, we built **pivot tables** (route × category) of mean weighted percentages and normalized them to represent proportional distributions.
5. These pivot tables were then merged with the cluster assignments, allowing us to compute **average demographic composition per cluster**.

Finally, the distributions were visualized via grouped bar charts comparing proportions of income and ethnicity categories across clusters.

---

## **Preliminary Results**

- **Cluster Formation:**  
  The K-Means model identified three distinct clusters (`K=3`) as optimal based on silhouette analysis.  
  Examination of the cluster centroids revealed that:
  - One cluster primarily represented routes with **higher passenger loads and shorter headways** (frequent, busy urban routes).
  - Another represented **moderate headway and ridership routes**.
  - The third contained **routes with lower frequency or more variability in headway**, likely corresponding to suburban or less-trafficked lines.

- **Visualization:**  
  The PCA plot showed that while clusters were not perfectly separable, they formed reasonably compact groups, confirming the existence of operationally distinct route categories.

- **Demographic Correlation:**  
  When comparing route clusters with income and ethnicity distributions from the passenger survey, **no strong or systematic demographic pattern** was observed.  
  - Income proportions were relatively uniform across clusters, with only minor variations — e.g., Cluster 2 had a slightly higher share of respondents in the 30–60% of Area Median Income bracket.  
  - Ethnic composition was also broadly similar, though Cluster 0/1 showed marginally higher proportions of Black or African American riders, and Cluster 2 slightly higher proportions of White riders.

- **Interpretation:**  
  These preliminary findings suggest that **service and ridership characteristics alone do not clearly separate routes by demographic patterns**.  
  The K-Means model effectively grouped routes by **operational performance** rather than by the socioeconomic composition of their riders — indicating that service differences (frequency, load, punctuality) are not strictly determined by demographic factors at the route level.



