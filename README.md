# Boston-Bus-Equity-CS506-Final-Project

[![BU Spark!](https://img.shields.io/badge/BU%20Spark!-Project-red.svg)]()

## Presentation Link

* **Youtube:** [Click Here](https://youtu.be/rE_8_-GRwgw)


## Reproducing the Results
### a. Download the Dataset
The cleaned dataset used for this analysis is hosted on Kaggle.

* **Kaggle Dataset:** [Boston MBTA Bus Equity and Reliability Dataset](https://www.kaggle.com/datasets/manaswiyadamreddy/boston-mbta-bus-equity-and-reliability-dataset/data)

### b. Set Up the Project Directory
1.  From the Kaggle link, download the files from the `data_cleaned_capped` directory.
2.  In the root of this project repository, create a folder named `data_cleaned_capped`.
3.  Place the downloaded data files (e.g., `arrival_departure.parquet`, `ridership.csv`, `survey.csv`) directly into this `data_cleaned_capped` folder.

The final project structure should look like this:

<!-- Boston-Bus-Equity-CS506-Final-Project/
├── data/
│   ├── MBTA_GTFS/
│   ├── ACS_Race/
│   └── census_shapefiles/
├── data_cleaned_capped/
│   ├── arrival_departure.parquet
│   ├── ridership.csv
│   └── survey.csv
├── notebooks/clustering/
│   ├── clustering.ipynb
│   └── hierarchical_clustering.ipynb
└── README.md -->
<img width="603" height="208" alt="Screenshot 2025-10-27 at 5 10 39 PM" src="https://github.com/user-attachments/assets/5a663047-fac7-413b-ac74-597445d1f62a" />

### c. Run the Analysis Notebooks
All clustering analysis is conducted within Jupyter Notebooks located in the `clustering/` directory.

# Mid-term Report

## Table of Contents
1. [Preliminary Visualizations of Data](#1-preliminary-visualizations-of-data)  
2. [Data Processing](#2-data-processing)  
3. [Data Modeling Methods](#3-data-modeling-methods)  
4. [Final Results](#4-preliminary-results)

---
## 1. Preliminary Visualizations of Data

*(new stuff begins here)*

- ### Demography Analysis
<br>
The choropleth maps visualize the proportion of residents based on race within each census tract across the city of Boston. The color gradient ranges from dark red, indicating a lower percentage of  residents, to dark blue, representing a higher percentage. The accompanying legend quantifies this range, with values from 0 (0%) to 1 (100%). As it will be shown below spatial variation is evident across the city.
<br>

<br>
The map reveals clear spatial variation, with:

- Higher concentrations of White residents in the more peripheral areas and lower percentages in the southern and central parts of the city.
- Black residents are more concentrated in the southern neighborhoods, with central and northern tracts displaying comparatively lower proportions.
- Asian residents are most concentrated in selected areas near the city center and western parts, with lower proportions elsewhere.
- Hispanic residents in specific northern and central tracts, with generally lower proportions in other parts of the city.
<br>

<table>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/a41592ab-6b48-4da8-9b66-20862ba00d93" width="350">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/a2af4d5c-e9e7-46e9-8cc5-58db3389a031" width="350">
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/7964752a-8977-4aee-9183-6814d888126e" width="350">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/60c11bff-b2be-42b8-b944-408f62da985d" width="350">
    </td>
  </tr>
</table>



*(new stuff ends here)*

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

<img width="700" height="300" alt="Most late routes in 2025 (late by more than 5 mins)" src="https://github.com/user-attachments/assets/4613c31a-e987-41d8-896c-01c4262fc094" />

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

### **I. Data Loading**
*(new stuff begins here)*

The project uses the following datasets: 

**1. MBTA GTFS Data:**
  - Files: `stops.txt`, `stop_times.txt`, `trips.txt`.
  - Source: [MBTA GTFS Feed](https://www.mbta.com/developers/gtfs) (download the latest static GTFS zip and extract relevant files).
**2. MBTA Data**
  - Files: Ridership data and Arrival–Departure time data
  - Description: Ridership data contains stop-level boarding, alighting, and load observations across several years and seasons from 2016 to 2024. While Arrival–Departure time data stored detailed service-level information such as headways, scheduled times, and earliness or lateness of bus arrivals for each route and direction.
  - Source:

**2. Census Tract Shapefiles:**
  - File: `tl_2024_25_tract.shp` (and associated files like `.shx`, `.dbf`).
  - Source: [U.S. Census Bureau TIGER/Line Shapefiles](https://www2.census.gov/geo/tiger/TIGER2024/TRACT/)(select Massachusetts tracts for 2024).
  - Filtered to Suffolk County (Boston, COUNTYFP = "025").

**3. ACS Race Demographics (Table B03002):**
  - File: Data.csv.
  - Source: [U.S. Census Bureau American Community Survey (ACS) 5-Year Estimates](https://data.census.gov/table/ACSDT1Y2024.B03002?q=B03002:+Hispanic+or+Latino+Origin+by+Race) (download for Massachusetts census tracts; select variables for total population and racial groups).
  - Variables used:
  `B03002_001E`: Total population.
  `B03002_003E`: White alone (not Hispanic).
  `B03002_004E`: Black alone (not Hispanic).
  `B03002_006E`: Asian alone (not Hispanic).
  `B03002_012E`: Hispanic or Latino.

### **II. Data Cleaning and Type Conversion**
Demographic columns in ACS and tracts DataFrames were converted to numeric using coercion to handle string headers and invalid values, replacing them with NaN. Unnecessary join indices were dropped to avoid conflicts. Diagnostics confirmed 1621 unique `GEOID`s, varying population distributions, and no duplicates, ensuring clean numeric data for analysis.

### **III. Spatial Operations and Joins**
Stops were reprojected to match tracts' `CRS (EPSG:4269)`, then spatially joined (inner, "within") to filter Boston stops. Race data was merged onto tracts via `GEOID`, with tracts reprojected to `EPSG:4326`. A final left spatial join assigned demographics to stops, creating an enriched stops_with_tract DataFrame.

### **IV. Data Integration and Aggregation**
Stop times were merged with enriched stops on stop_id, then with trips on trip_id to add routes. Data was grouped by route_id to compute demographic means, with percentages calculated by dividing racial means by total population. 

*(new stuff ends here)*

### **II. Route ID Normalization**

Each dataset represented MBTA routes in slightly different ways — for instance, `"01"`, `"1"`, `"1-0-0"`, and `"34E"` could all appear as route identifiers. A custom normalization process was implemented to make them comparable across datasets. All route IDs were converted to uppercase strings, extra whitespace and underscores were stripped, and leading zeros were removed for numeric-only IDs. This ensured that all datasets referred to each route consistently (e.g., `"01"` and `"1"` were treated as the same route).  

New normalized columns (such as `route_id_norm`) were created to store these standardized identifiers while keeping the raw data intact. This step was critical for accurate merging and comparison later in the pipeline.



### **III. Correction of Route Naming Errors**

Some route entries included inconsistencies such as suffix underscores (e.g., `"746_"`) or formatting anomalies. These were manually corrected using simple replacement rules. The normalization process was re-run afterward to ensure the corrections propagated consistently across all datasets.  

Unique route sets were then extracted from each dataset, and the intersections and differences were computed to identify:  
- Routes that appeared in all datasets, and  
- Routes that were missing from one or more datasets.

This comparison provided an early check on coverage and revealed a manageable overlap suitable for merging.


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

*(new stuff begins here)*
### I. Data Analysis

With all datasets merged, the notebook applies several modeling and analytical approaches to examine the relationship between transit performance and neighborhood demographics. The first step involves characterizing each route based on the demographic composition of the stops it serves. This is done by averaging the demographic attributes of the tracts linked to each stop.

Next, the lateness metrics are connected to these demographic profiles to identify associations between route performance and the racial composition of the areas they traverse. The analysis focuses on uncovering whether routes serving higher percentages of minority residents experience greater delays, and whether lateness patterns vary systematically across the city.

Visual models, including route-level comparisons, scatterplots, and mapped performance layers, are used to highlight these patterns. While the notebook does not use predictive machine learning models, it applies structured exploratory and statistical approaches to reveal relationships between service reliability and demographic factors.

*(new stuff ends here)*


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



### V. Final Results
*(new stuff begins here)*

The final results of the analysis show clear and measurable disparities in MBTA lateness across different demographic areas of Boston. Routes that serve neighborhoods with higher proportions of non-white residents tend to exhibit higher average lateness, while routes operating primarily in predominantly white neighborhoods generally show lower delays. These patterns are consistent at both the stop and route levels.

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/c7122502-6345-4917-9974-5b13ee576397" width="300"></td>
    <td><img src="https://github.com/user-attachments/assets/9b409d54-eb17-4ad7-8096-5d42db617533" width="300"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/72c087fa-03e3-452b-9658-628173a8a670" width="300"></td>
    <td><img src="https://github.com/user-attachments/assets/0361149f-25d1-48bd-925a-0ae0d88430ef" width="300"></td>
  </tr>
</table>

This heatmap displays the Pearson correlation coefficients between lateness and the proportions of different racial and ethnic groups across Boston census tracts. Lateness tends to be higher in areas with more Black residents and a bit lower in areas with more White residents. Census tracts with more White residents usually have fewer Black and Hispanic residents, and vice versa. The percentages of Asian and Hispanic residents show weaker relationships with lateness and with the other groups. Overall, the map highlights some clear patterns in how demographics and lateness are connected in different parts of the city.

<img src="https://github.com/user-attachments/assets/e5f0af72-f7af-4063-a8de-70738011803e" width="500">

This boxplot compares lateness on routes in Boston census tracts based on aggregated demographics. Areas were classified as either “majority White” or “majority non-White,” with the non-White category combining Black, Hispanic, and Asian residents. The chart shows that routes in majority non-White areas tend to have higher lateness compared to those in majority White areas. The median lateness is greater for majority non-White neighborhoods, and there are also some outliers with especially high lateness. Overall, this suggests that lateness is more common on routes serving areas where Black, Hispanic, and Asian populations are the majority.

<img width="500" alt="{79B43393-9950-4ECD-B713-5D76544F00D2}" src="https://github.com/user-attachments/assets/1fe3e57e-f6b0-4988-93b6-e390cbdd84e3" />


Spatial visualizations reinforce these findings: clusters of higher lateness frequently appear in parts of the city with larger minority populations, whereas areas with more consistent service tend to align with predominantly white tracts. The demographic–performance relationship is not random; it shows a notable association between race composition and transit reliability.

These maps show MBTA routes in Boston, colored by average lateness (in minutes), with different backgrounds representing the proportion of White, Black, Asian, or Hispanic residents in each census tract. Redder routes indicate higher average lateness, while yellow routes indicate less lateness. In each map, the darker blue regions in the background reveal census tracts with a higher proportion of the given demographic group (White, Black, Asian, or Hispanic).

By comparing the maps, you can see how routes with greater lateness often pass through neighborhoods with higher proportions of Black, Hispanic, or Asian residents, while routes in areas with a higher percentage of White residents generally show less lateness. This visual highlights patterns in MBTA route lateness in relation to neighborhood demographics across the city.

<table>
  <tr>
    <td><img width="400" alt="{1A4DCC02-64A1-454E-95D4-1937226A9969}" src="https://github.com/user-attachments/assets/cb234249-236b-492d-800d-2802618db465" /></td>
    <td><img width="400" alt="{65669C75-5267-4042-B81A-1CB5842C730B}" src="https://github.com/user-attachments/assets/3a69795c-401d-4a85-acb1-89d3b5e2d21d" /></td>
  </tr>
  <tr>
    <td><img width="400" alt="{779CBCA4-E1B1-410D-8FB7-A66271F027CC}" src="https://github.com/user-attachments/assets/3a98c313-db3f-49bd-be23-b37ed3668307" /></td>
    <td><img width="400" alt="{451C4157-E8E8-4419-9DB0-287EE04051FE}" src="https://github.com/user-attachments/assets/f7aa0ca4-78b6-4b4d-bc68-2027af7568b9" /></td>
  </tr>
</table>


The same observation applies when the visualization is done using the bus stops.


<table>
  <tr>
    <td><img width="400" alt="{E6EDCF71-D2C7-4E8A-BB8C-92466967EFFA}" src="https://github.com/user-attachments/assets/90aded7f-f9c1-44b6-9425-e5e2596024bd" />
</td>
    <td><img width="400" alt="{6B4E23B1-B009-4C3F-9557-F2A41AB6848C}" src="https://github.com/user-attachments/assets/48bb2973-e0c5-41f6-a2f9-9c88f5afd2a8" />
</td>
  </tr>
  <tr>
    <td><img width="400" alt="{8CCB1CD1-0131-4FDC-9575-631F8285AA81}" src="https://github.com/user-attachments/assets/61abc1fe-12cd-4a48-84b1-e3bed04c4ecb" />
</td>
    <td><img width="400"  alt="{51BB8B1C-51E9-46C5-B03C-898F3915E9FC}" src="https://github.com/user-attachments/assets/827c1ae6-c703-4cb3-968d-f30c3b8ec5e7" />
</td>
  </tr>
</table>


Now lets take a closer look at each routes and stops:

Below is the Top 10 late and early routes 
<table>
  <tr> 
    <td><img width="600"  alt="{FFEB1CCD-5F26-4FE5-9660-99F36B48FA8D}" src="https://github.com/user-attachments/assets/4b58009b-b758-4f58-a5c3-356c977679c5" /></td> 
    <td><img width="600"  alt="{06EC8BD7-4507-4312-99F2-F48493DAE456}" src="https://github.com/user-attachments/assets/56a45d27-88b2-419d-8890-0db1c0f06dd8" /></td>
  </tr>  
</table>

Below is the Top 10 late and early stops 

<table>
  <tr> 
    <td><img width="600"  alt="{7C7B5D21-B336-477F-858E-06E1AD89FC68}" src="https://github.com/user-attachments/assets/01b80cdf-c43a-4f2d-8fcb-140e52d59b87" /></td> 
    <td><img width="600" alt="{F7B7BE78-C4B0-423D-B786-606F86A783DB}" src="https://github.com/user-attachments/assets/eae9f33a-eac2-45f9-acb2-b760195b0b94" /></td>
  </tr>  
</table>

Below is the Top 10 late and early routes with minority groups aggregated
<table>
  <tr> 
    <td><img width="600" alt="{9034BCB3-E927-484A-A5DD-DC5E3B57B7D6}" src="https://github.com/user-attachments/assets/ba13f096-fdb9-4d5e-92cb-419d3b7aa19b" /></td> 
    <td><img width="600" alt="{487D6589-37F7-41A8-A861-3851038C90B7}" src="https://github.com/user-attachments/assets/19c24b75-9815-4613-9d89-06612d44fa33" /></td>
  </tr>  
</table>

Below is the Top 10 late and early stops with minority groups aggregated
<table>
  <tr> 
    <td><img width="600"  alt="{1BB6E6CA-EEC2-4E35-AFB7-AA028545611F}" src="https://github.com/user-attachments/assets/b427d458-1f7d-4d95-a344-b139106fedba" /></td> 
    <td><img width="600" alt="{9A320CBD-F4B6-48ED-88EB-B424E4FE0816}" src="https://github.com/user-attachments/assets/c42939ea-3ca1-430c-b5fb-52bb7297a57d" /></td>
  </tr>  
</table>

Boston is predominantly White, so looking at raw lateness alone could underestimate the impact on minority communities. By computing the population-weighted percentage of underserved individuals, we can highlight disparities in transit service and identify which groups are disproportionately affected, providing a basis for equitable improvements. Directly comparing raw counts of late stops would bias the analysis toward the majority population. By converting to percentages, we measure the relative burden on each community.

To assess which communities are disproportionately affected by transit delays, we define a lateness threshold (e.g., 5 minutes) to identify stops that are considered underserved. For each stop exceeding this threshold, we calculate the number of individuals from each racial group affected, using population counts from census data. Summing these values across all stops and dividing by the total population of each group in Boston gives the percentage of the community that is underserved. This population-weighted approach accounts for differences in group sizes, highlights disparities between White and minority communities, and provides a basis for equitable transit planning.

<img width="700"  alt="{D2320C60-646A-4423-A978-5BF1433504B7}" src="https://github.com/user-attachments/assets/1db157e0-f20a-4116-8676-ef3a3f7e4fba" />





Overall, the analysis demonstrates that lateness is unevenly distributed across the city and is more severe in minority communities. These findings highlight important equity concerns and suggest that demographic factors play a meaningful role in transit performance outcomes within Boston’s MBTA system.

*(new stuff ends here)*




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

<img width="900" height="600" alt="Income dis per cluster" src="https://github.com/user-attachments/assets/bedf63c8-8b48-4a68-a76f-2f339bf15ca3" />

<br><br>

### Ethnicity Distribution obtained from K means

<br>

<img width="900" height="600" alt="Ethnicity dis per cluster" src="https://github.com/user-attachments/assets/073c28fd-0141-4d1f-954b-7e7a86bf03a5" />

<br><br>

### Income Distribution obtained from Hierarchical Clustering

<br>

<img width="900" height="600" alt="Income dis per hierarchical cluster" src="https://github.com/user-attachments/assets/00a73f29-4dad-4b70-a6d4-91a6edb5548b" />

<br><br>
### Ethnicity Distribution obtained from Hierarchical Clustering
<img width="900" height="600" alt="Ethnicity dis per hierarchical cluster" src="https://github.com/user-attachments/assets/08041fef-5666-4da6-b634-58ed6c2bddb8" />

<br><br>

**Preliminary Insight:**  
Overall, the clustering results did not reveal clear or promising patterns.  
This suggests the need for **improved feature extraction**, potentially incorporating additional operational metrics (e.g., temporal demand variation, stop-level reliability) or refining existing ones to better represent the behavioral and service-level diversity among MBTA routes.





REMOVED STUFF


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

<img width="900" height="600" alt="Hierarchical cluster dendogram" src="https://github.com/user-attachments/assets/db004e42-19bd-4797-a75c-32e8fe97a581" />

<br><br>

<img width="900" height="600" alt="Hierarchical cluster - pca projection" src="https://github.com/user-attachments/assets/dfc062ae-dbd2-4e3c-8475-95fc31c2a671" />

<br><br>


### IV. Demographic Correlation Analysis
To examine potential relationships between operational clusters and rider demographics:

- The **survey_df** was transformed into a long-form dataset (`survey_long`), exploding route arrays (e.g., `['114', '116', '117']`) into individual rows.  
- Routes were normalized to consistent identifiers (e.g., “1”, “34E”, “SL4”).  
- From `survey_long`, income-related and ethnicity-related categories were isolated using keyword-based filters.  
- For each demographic subset, **pivot tables (route × category)** were computed to capture mean weighted proportions, normalized to represent percentage distributions.  
- These tables were merged with cluster assignments (from both K-Means and Hierarchical Clustering) to evaluate demographic composition per cluster.  
- The results were visualized as **grouped bar charts** comparing proportions of income and ethnicity categories across clusters.




