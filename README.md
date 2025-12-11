# Boston-Bus-Equity-CS506-Final-Project

[![BU Spark!](https://img.shields.io/badge/BU%20Spark!-Project-red.svg)]()

## Presentation Link

* **Youtube:** [Click Here](https://youtu.be/rE_8_-GRwgw)


## Reproducing the Results
### a. Clone and Install Dependencies

```bash
git clone https://github.com/Chava-Sai/Boston-Bus-Equity-CS506-Final-Project.git
cd Boston-Bus-Equity-CS506-Final-Project

make install

```

For Windows:

```bash
.venv\Scripts\activate

```
For Mac/Linux

```bash
source .venv/bin/activate
```


### b. Download the Dataset
The cleaned dataset used for this analysis is hosted on Kaggle.

* **Kaggle Dataset:** [Boston MBTA Bus Equity and Reliability Dataset](https://www.kaggle.com/datasets/manaswiyadamreddy/boston-mbta-bus-equity-and-reliability-dataset/data)

### c. Set Up the Project Directory
1.  From the Kaggle link, download all the data.
2.  In the root of this project repository, create a folder named `data`.
3.  Extract the folders and place the downloaded data files based on the structure shown below.

The final project structure should look something like this:
<pre>
  ```
├── data/
    ├── data_cleaned_capped/
│       ├── arrival_departure.parquet
│       ├── ridership.csv
│       └── survey.csv
|   ├── arr_dep_demo.csv
│   ├── MBTA_GTFS/
│   ├── MBTA_Bus_Parquet/
│   ├── tl_2024_25_tract/
│   └── B03002/
├── notebooks/
│   ├── clustering/
│   ├── analysis/
│   └── data_preprocessing/
├── libs/
├── scripts/
└── README.md 
  ```
</pre>


### d. Run the Analysis Notebooks
All analysis and modeling is conducted within Jupyter Notebooks located in the `notebooks/` directory.

# Final Report

## Project Scope and Operational Metrics

This project is designed primarily as an equity and reliability analysis of MBTA bus service, rather than a full operational performance dashboard. Using three integrated datasets—ridership, arrival–departure records, and passenger survey data—we focus on how bus lateness is distributed across the city and how that distribution relates to neighborhood demographics, particularly race.

Ridership data from 2016–2024 are incorporated to build route-level features such as mean and median boardings, alightings, and passenger load. These aggregated statistics help describe how intensively each route is used and support downstream analyses, but the report does not present detailed ridership time series for individual routes. In particular, changes in ridership from pre-pandemic to post-pandemic periods are not separately summarized; they remain implicit in the historical data rather than highlighted as explicit trend plots or tables.

The temporal richness of the GTFS and arrival–departure data would allow reconstruction of end-to-end travel times for each trip on each route. However, the analysis here emphasizes service regularity and punctuality instead of full origin–destination travel times. We work primarily with headways, scheduled times, and measures of earliness and lateness at stops, and we identify routes and stops with systematically higher delay, rather than reporting average end-to-end travel durations for every line.

Passenger experience is examined through the lens of scheduled headways, distributions of arrival delays, and derived on-time performance rates (for example, the share of trips arriving within a short window of their scheduled time). We do not translate these service-side metrics into explicit estimates of average rider wait time, and we do not distinguish between the typical wait when buses run on schedule and the additional wait induced by delays. As a result, wait time appears indirectly through headways and delays, rather than as a standalone quantity.

At the system level, lateness is characterized by full delay distributions, route-level late-arrival rates, and identification of the worst-performing routes and stops. The report does not compress these patterns into a single global figure such as “average delay across all routes,” preferring instead to show how delays vary across space and demographics. Likewise, while particular bus lines (including important routes such as 22, 29, 15, 45, 28, 44, and 42) may appear among the worst performers in our visualizations, they are treated within the broader set of routes rather than receiving individual operational profiles or dedicated average-delay summaries. Producing such targeted statistics is feasible with the cleaned datasets, but lies beyond the equity-centered scope of this mid-term analysis.

## Table of Contents
1. [Datasets Used](#1-datasets-used)
2. [Data Processing](#2-data-processing) 
3. [Visualizations of Data](#3-visualizations-of-data)  
4. [Data Modeling Methods](#4-data-modeling-methods)  
5. [Final Results](#5-final-results)

---
## 1. Datasets Used

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

---

## 2. Data Processing


### **I. Data Cleaning and Type Conversion**
Demographic columns in ACS and tracts DataFrames were converted to numeric using coercion to handle string headers and invalid values, replacing them with NaN. Unnecessary join indices were dropped to avoid conflicts. Diagnostics confirmed 1621 unique `GEOID`s, varying population distributions, and no duplicates, ensuring clean numeric data for analysis.

### **II. Spatial Operations and Joins**
Stops were reprojected to match tracts' `CRS (EPSG:4269)`, then spatially joined (inner, "within") to filter Boston stops. Race data was merged onto tracts via `GEOID`, with tracts reprojected to `EPSG:4326`. A final left spatial join assigned demographics to stops, creating an enriched stops_with_tract DataFrame.

### **III. Data Integration and Aggregation**
Stop times were merged with enriched stops on stop_id, then with trips on trip_id to add routes. Data was grouped by route_id to compute demographic means, with percentages calculated by dividing racial means by total population. 


### **IV. Route ID Normalization**

Routes appeared in inconsistent formats across datasets (e.g., `"01"`, `"1"`, `"1-0-0"`, `"34E"`). All route IDs were standardized by converting to uppercase, stripping whitespace/underscores, and removing leading zeros for numeric-only IDs. A new `route_id_norm` column stored these cleaned identifiers while preserving raw values, ensuring consistent merging across datasets.

### **V. Correction of Route Naming Errors**

Formatting anomalies (e.g., `"746_"`) were corrected with simple replacement rules, followed by re-running normalization. Unique route sets were compared across datasets to identify:
- Routes common to all sources  
- Routes missing from one or more datasets  

This confirmed sufficient overlap for effective integration.

### **VI. Data Cleaning and Filtering**

Invalid or empty survey route entries were removed. Only routes present simultaneously in ridership, arrival–departure, and survey datasets were kept. To prevent memory overload, each dataset was capped at 30M rows while still retaining all relevant information.

### **VII. Efficient Slicing and Indexing**

To avoid kernel crashes when filtering Arrow-backed dataframes, boolean masks were converted into NumPy index arrays. Three masks (`mask_arr`, `mask_rid`, `mask_svy`) extracted rows corresponding to valid intersecting routes. This stabilized processing and reduced dataset size significantly.

### **VIII. Route-Level Feature Construction**

Two datasets were used for route-level operational features:

- **Ridership Data (`ridership_df`)**  
- **Arrival–Departure Data (`arrival_departure_df`)**

For each route, aggregated features were computed:

- **Ridership metrics:**  
  mean/median boardings, alightings, passenger load, total record count, directional balance  
- **Service metrics:**  
  mean/std headway, mean scheduled headway, mean earliness, number of unique stops, total observations, on-time performance rate (arrivals within ±60 seconds)

These statistics were merged into a unified dataframe (`route_feat`), providing the analytical foundation for clustering and downstream modeling.

### **IX. Final Output Generation**

Cleaned data was saved in `data_cleaned_capped`:
- Arrival–departure → **Parquet**  
- Ridership → **CSV**  
- Survey → **CSV**  

Chunked writing (50k rows) ensured memory-safe exporting. All outputs now share standardized route IDs, with invalid and malformed entries removed.

### **X. Key Outcomes**

The pipeline harmonizes three disparate MBTA datasets into a consistent analytical foundation. Through standardized route IDs, corrected inconsistencies, efficient filtering, and route-level feature construction, the final data supports reliable clustering, operational analysis, and advanced modeling.

---

## 3. Visualizations of Data

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

## 4. Data Modeling Methods

Our goal was to explore whether operational and ridership characteristics of MBTA bus routes exhibit natural groupings and, subsequently, whether those groups correlate with demographic or socioeconomic patterns derived from the MBTA passenger survey data.

### I. Data Analysis

With all datasets merged, the notebook applies several modeling and analytical approaches to examine the relationship between transit performance and neighborhood demographics. The first step involves characterizing each route based on the demographic composition of the stops it serves. This is done by averaging the demographic attributes of the tracts linked to each stop.

Next, the lateness metrics are connected to these demographic profiles to identify associations between route performance and the racial composition of the areas they traverse. The analysis focuses on uncovering whether routes serving higher percentages of minority residents experience greater delays, and whether lateness patterns vary systematically across the city.

Visual models, including route-level comparisons, scatterplots, and mapped performance layers, are used to highlight these patterns. While the notebook does not use predictive machine learning models, it applies structured exploratory and statistical approaches to reveal relationships between service reliability and demographic factors.


### II. Data Standardization
All numeric features were standardized using **z-score normalization** via `StandardScaler` from scikit-learn.  
This ensured that variables with different scales (e.g., “headway_mean” in minutes vs. “boardings_mean” in passenger counts) contributed equally to the clustering process.

### III. Lateness Prediction: XGBoost + SHAP Explainability

This module develops an interpretable ML pipeline to estimate **bus arrival lateness** using operational, temporal, and demographic predictors. We pair an XGBoost model with SHAP explainability tools to uncover feature contributions and evaluate potential fairness concerns.


#### 1. Model Overview

We train an **XGBoost Regressor** on engineered features including:

- **Operational:** scheduled_headway, time_point_order, route_length  
- **Temporal:** scheduled_hour, peak/off-peak indicator  
- **Geodemographic:** pct_white, pct_black, pct_asian, pct_hispanic, pct_minority_stop, pct_minority_route  
- **Stop Characteristics:** point_type (Startpoint/Midpoint), direction_outbound  

Model performance:

- **Train RMSE:** ~0.43  
- **Test RMSE:** ~1.12  
- **Test R²:** ~0.48  

The model explains about half of observed lateness variance, which is reasonable for transportation systems with high stochastic noise.
<img width="400" height="400" alt="Screenshot 2025-12-10 at 9 39 16 PM" src="https://github.com/user-attachments/assets/66cd8cb1-a595-4117-b79a-150f2588a9d6" />

<img width="400" height="400" alt="Screenshot 2025-12-10 at 9 39 27 PM" src="https://github.com/user-attachments/assets/314d376a-d3b8-412a-9f32-6933b1d5062c" />

#### 2. SHAP Global Feature Importance

Using `shap.TreeExplainer`, we compute SHAP values to quantify each feature’s average contribution.

**Top predictors:**

1. **time_point_order** — later stops tend to accumulate more delay  
2. **scheduled_headway** — longer headways drive higher lateness volatility  
3. **point_type_Midpoint** — mid-route timing behaves differently than endpoints  
4. **pct_asian**, **pct_minority_route**, **pct_black** — demographic exposure shows measurable effect  
5. **scheduled_hour & direction_outbound** — temporal and directional factors influence delay patterns

<img width="400" height="350" alt="Screenshot 2025-12-10 at 9 39 49 PM" src="https://github.com/user-attachments/assets/212dfcc8-f0a4-4fcf-b15b-775977e248a8" />


**Summary:** Operational structure explains the majority of lateness, but demographic features still appear as influential, motivating deeper fairness evaluation.


#### 3. SHAP Beeswarm Interpretation

The SHAP beeswarm provides directional insight:

- **High time_point_order** consistently increases lateness.  
- **High scheduled_headway** shifts predictions upward.  
- **Demographic variables** show mixed positive/negative contributions, indicating **context-dependent interactions** rather than uniform effects.  
- Certain clusters show that increases in pct_asian, pct_black, or pct_minority_route can lead to higher predicted lateness in specific contexts.

<img width="400" height="270" alt="Screenshot 2025-12-10 at 9 40 06 PM" src="https://github.com/user-attachments/assets/01ca53e0-c839-4db4-b136-4ec1397bdfcd" />


These findings highlight complex interaction effects, not direct linear bias.


#### 4. Counterfactual Fairness Analysis

To test whether demographic values unfairly influence predictions, we vary each demographic feature from **0 → 1** while holding all other attributes constant.

#### Key patterns:

- **pct_minority_route:** slight upward trend, with a steep jump near 0.9–1.0  
- **pct_white:** lateness decreases from 0 → ~0.2, then stabilizes  
- **pct_black & pct_asian:** non-linear increases around mid-range values, with pct_asian showing the strongest effect  
- **pct_hispanic:** modest rise at low values, then flattening


<img width="450" height="290" alt="pct_min" src="https://github.com/user-attachments/assets/2f80ca08-10b2-4ded-b4c7-86a222012bc4" />


<!-- <img width="615" height="442" alt="pct_hispanic" src="https://github.com/user-attachments/assets/65096d76-ebc7-44b1-833b-99bb4bbb45e5" />
<img width="617" height="429" alt="pct_asian" src="https://github.com/user-attachments/assets/27614caa-8fcd-4131-8d88-d638d09147b8" />
<img width="614" height="438" alt="pct_black" src="https://github.com/user-attachments/assets/31a93a9f-f95e-4e03-968f-9b1ad96df3bb" />
<img width="619" height="439" alt="pct_white" src="https://github.com/user-attachments/assets/3b0456a1-a738-4699-a0cc-09a5e8e54163" /> -->

<table>
  <tr>
    <td width="50%">
      <img src="https://github.com/user-attachments/assets/65096d76-ebc7-44b1-833b-99bb4bbb45e5" alt="pct_hispanic" />
    </td>
    <td width="50%">
      <img src="https://github.com/user-attachments/assets/27614caa-8fcd-4131-8d88-d638d09147b8" alt="pct_asian" />
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="https://github.com/user-attachments/assets/31a93a9f-f95e-4e03-968f-9b1ad96df3bb" alt="pct_black" />
    </td>
    <td width="50%">
      <img src="https://github.com/user-attachments/assets/3b0456a1-a738-4699-a0cc-09a5e8e54163" alt="pct_white" />
    </td>
  </tr>
</table>


**Interpretation:**  
Demographic changes do shift predictions, but:

- Effects are **generally small** (< 0.5 minutes)  
- Relationships are **non-monotonic**, suggesting complex learned structure  
- Largest effects occur at **extreme demographic values**, not across typical ranges  

These results support further fairness investigation but do not indicate strong, uniform demographic bias.


## 5. Final Results

### 5.1 Pre and Post-Pandemic Analysis

#### **Overarching question:** How did ridership change before and after the pandemic, across routes, and time periods?
- **Did average ridership drop after COVID-19?**
- **Which routes were most affected? Which were least affected?**
- **Which routes had a high recovery rate post-pandemic? Which had the least recovery?**

Bus ridership and average load were relatively stable between 2016 and 2019. Both metrics experienced a sharp decline in 2020, coinciding with the pandemic's onset. Following this, both ridership and average load began to recover, showing a clear upward trend from 2021 onwards. However, as of 2024, neither metric has fully returned to pre-pandemic levels, illustrating the significant and lasting impact of the pandemic on public transit usage in Boston.


<img width="600"  alt="{E07ED614-B209-4CEB-B644-B341FE280F4D}" src="https://github.com/user-attachments/assets/acfafc2a-7686-4aa1-af1f-773570a25f38" />

Across all time periods, average onboardings decreased following the pandemic. The most pronounced declines can be seen during PM PEAK, AM PEAK, MIDDAY SCHOOL, and EVENING periods. Even during traditionally busy periods such as the morning (AM PEAK) and afternoon (PM PEAK) commute times, post-pandemic ridership remains noticeably lower than pre-pandemic levels.

<img width="600"  alt="{C95F8121-CB41-4CF8-B7D8-494FE5B746C0}" src="https://github.com/user-attachments/assets/2a022618-9a4c-48eb-9cf9-8e1fe837d65b" />

Looks like the 11 least affected routes have actually increased in ridership after the pandemic. Possible reasons could be an error in the data(outliers) or actual travel pattern shifts. Eg. routes serving residential or suburban areas might see more use as remote workers commute locally. 

<table>
  <tr>
<td><img width="600" alt="{99508320-908F-4D2A-A831-69BEF316EA66}" src="https://github.com/user-attachments/assets/81e74b1b-df0e-4bc2-a7b8-c0bcb307a436" /></td>
<td><img width="600" alt="{79A769CB-AD1B-4CF4-B271-1BBE81B42BF0}" src="https://github.com/user-attachments/assets/6a740034-43e4-4101-b766-6fb214106742" /></td>
  </tr>
</table>


Overall, the figure highlights significant variation in ridership recovery across routes, with some routes rebounding strongly while others continue to lag behind, illustrating the uneven impact of the pandemic on different parts of Boston’s bus network.

<table>
<tr>
<td><img width="1232" height="490" alt="{A3F2AC0F-39A9-403E-B3CD-CFBC4DF9DDAE}" src="https://github.com/user-attachments/assets/6c38b2ec-fb03-45a3-bcc8-da6813ccb1ab" /></td>
<td><img width="1223" height="503" alt="{A9E936AE-212E-4B0B-8E25-9780B574580E}" src="https://github.com/user-attachments/assets/a62abdf6-6862-4e9e-ad29-ffa77f7d378c" /></td>
  </tr>
</table>

- **Statistical Analysis Report**: A t-test was conducted to compare the average bus loads before and after the pandemic. The results ($t = 209.57$, $p < 0.001$) indicate a statistically significant difference between the pre-pandemic and post-pandemic average load values. The extremely low p-value confirms that the change in average bus load observed between these two periods is unlikely to be due to random chance, providing strong evidence that the pandemic had a significant and lasting effect on bus ridership loads in Boston.



### 5.2 Bus Equity Analysis
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


### 5.3 Key Takeaways from Predictive Modeling

- XGBoost captures structural lateness patterns effectively.  
- SHAP provides transparent explanations of operational and demographic impacts.  
- Counterfactual sweeps reveal **moderate but non-uniform** demographic influence.  
- This interpretability pipeline strengthens both **model trust** and **equity assessment**, enabling responsible use of ML in transportation analytics.
