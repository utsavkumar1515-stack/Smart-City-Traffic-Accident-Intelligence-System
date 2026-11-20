# UrbanFlow: Exploratory Data Analysis (EDA) & Statistical Findings
**Dataset**: `Dataset/cleaned/urbanflow_cleaned.csv`  
**Records Analyzed**: 20,000 Verified Collisions | **Attributes**: 34 Features  
**Temporal Span**: January 1, 2022 to April 15, 2025  
**Audit Date**: September 2026  

---

## 1. Overall Findings
* **Total Collisions Analyzed**: Exactly **20,000** incident records.
* **Total Human Casualties**: **34,529** injuries and fatalities recorded (Mean: **1.726** casualties per crash).
* **Total Vehicles Involved**: **59,840** vehicles (Mean: **2.992** vehicles per crash).
* **Overall Composite Risk Score**: Mean = **0.4376**, Median = **0.4500**, Minimum = **0.1000**, Maximum = **1.0000**, Std Dev = **0.2181**.
* **Geographic Scope**: 8 Premier Metropolitan Centers spanning 7 Indian States.

---

## 2. Time-Based Findings
* **Annual Trends**:
  * 2022: 6,117 crashes (30.59%)
  * 2023: 6,088 crashes (30.44%)
  * 2024: 6,061 crashes (30.31%)
  * 2025: 1,734 crashes (8.67% — partial year data through April 15, 2025).
  * *Observation*: Annual crash frequency across full years (2022–2024) remains exceptionally stable at ~6,080 crashes per year.
* **Monthly Distribution**:
  * Highest Month: **January** (2,044 crashes, 10.22%) and **March** (2,043 crashes, 10.22%).
  * Lowest Month: **September** (1,475 crashes, 7.38%).
* **Day-of-Week Distribution**:
  * Highest Day: **Monday** (2,966 crashes, 14.83%).
  * Friday (2,879, 14.40%), Tuesday (2,871, 14.36%), Saturday (2,867, 14.34%), Sunday (2,856, 14.28%), Thursday (2,835, 14.18%).
  * Lowest Day: **Wednesday** (2,726 crashes, 13.63%).
* **Diurnal 24-Hour Cycle**:
  * Peak Single Hour: **2:00 AM (888 crashes)** and **1:00 PM (878 crashes)**.
  * Trough Single Hour: **7:00 AM (786 crashes)** and **9:00 AM (786 crashes)**.
* **Time-of-Day Segments**:
  * **Night (22:00–05:59)**: **6,721 crashes (33.61%)** — Highest single period.
  * **Morning (06:00–11:59)**: **4,907 crashes (24.54%)**.
  * **Evening (17:00–21:59)**: **4,192 crashes (20.96%)**.
  * **Afternoon (12:00–16:59)**: **4,180 crashes (20.90%)**.
* **Weekday vs. Weekend**:
  * Weekdays (Mon–Fri): **14,277 crashes (71.39%)**.
  * Weekends (Sat–Sun): **5,723 crashes (28.62%)**.
  * Daily Average: ~2,855 crashes/weekday vs ~2,861 crashes/weekend day (nearly identical daily rates).
* **Peak Hour Analysis**:
  * Non-Peak Hours: **15,052 crashes (75.26%)**.
  * Commuter Peak Hours (8–10 AM & 5–7 PM): **4,948 crashes (24.74%)**.
  * *Crucial Observation*: Peak hours represent 6 out of 24 hours (25.0% of the day) and account for 24.74% of crashes, showing steady hourly volume, but **peak hour collisions carry an average risk score of 0.604 vs 0.383 for non-peak hours (+57.7% risk elevation)**.

---

## 3. Severity Findings
* **Severity Distribution**:
  * Minor Collisions: **11,025 (55.13%)**
  * Major Collisions: **5,988 (29.94%)**
  * Fatal Collisions: **2,987 (14.94%)**
* **Casualties by Severity**:
  * Fatal Collisions: Mean = **3.002 casualties per incident** (Double that of non-fatal crashes!).
  * Minor Collisions: Mean = **1.507 casualties**.
  * Major Collisions: Mean = **1.495 casualties**.
* **Risk Score by Severity**:
  * Fatal Collisions: Mean Risk = **0.6075** (Elevated by +49.1% over minor collisions).
  * Minor Collisions: Mean Risk = **0.4082**.
  * Major Collisions: Mean Risk = **0.4068**.

---

## 4. Cause Findings
* **Root Causes Breakdown**:
  * Distraction: **4,026 crashes (20.13%)**
  * Overspeeding: **4,025 crashes (20.13%)**
  * Weather Conditions: **3,997 crashes (19.99%)**
  * Drunk Driving: **3,978 crashes (19.89%)**
  * Poor Road Maintenance: **3,974 crashes (19.87%)**
* **Pareto Principle Assessment**:
  * The 5 causes each contribute almost exactly 20% of incident volume. This indicates that municipal safety cannot focus on a single silver-bullet intervention; enforcement (speed, DUI), technology (distraction), and civil works (road quality) must be deployed simultaneously.

---

## 5. City/State Findings
* **City Volume Ranking**:
  1. Chandigarh: 2,577 (12.89%)
  2. Chennai: 2,575 (12.88%)
  3. Kolkata: 2,559 (12.80%)
  4. Pune: 2,517 (12.59%)
  5. Mumbai: 2,492 (12.46%)
  6. Bangalore: 2,438 (12.19%)
  7. Delhi: 2,433 (12.17%)
  8. Hyderabad: 2,409 (12.05%)
* **Average Risk Score by City**:
  1. Chandigarh: **0.4416**
  2. Bangalore: **0.4402**
  3. Hyderabad: **0.4395**
  4. Chennai: **0.4376**
  5. Delhi: **0.4371**
  6. Pune: **0.4358**
  7. Kolkata: **0.4346**
  8. Mumbai: **0.4343**
* **High-Risk Incidents (Score >= 0.65) by City**:
  1. Chandigarh: **643 high-risk crashes**
  2. Bangalore: **624 high-risk crashes**
  3. Hyderabad: **618 high-risk crashes**
  4. Chennai: **604 high-risk crashes**
  5. Delhi: **597 high-risk crashes**
  6. Pune: **588 high-risk crashes**
  7. Kolkata: **573 high-risk crashes**
  8. Mumbai: **563 high-risk crashes**
* **State Volume Ranking**:
  * Maharashtra: **5,009 crashes (25.05%)** (Combined volume of Mumbai & Pune).
  * Punjab: **2,577 crashes (12.89%)**.
  * Tamil Nadu: **2,575 crashes (12.88%)**.
  * West Bengal: **2,559 crashes (12.80%)**.
  * Karnataka: **2,438 crashes (12.19%)**.
  * Delhi: **2,433 crashes (12.17%)**.
  * Telangana: **2,409 crashes (12.05%)**.

---

## 6. Road Findings
* **Roadway Class Volume**:
  * Urban Streets: **6,745 crashes (33.73%)**
  * Rural Connectors: **6,639 crashes (33.20%)**
  * Multi-lane Highways: **6,616 crashes (33.08%)**
* **Risk Score across Road Types**:
  * Urban: **0.4406**
  * Highway: **0.4372**
  * Rural: **0.4349**
* **Lanes Breakdown**:
  * 1 Lane: 3,365 crashes (16.83%)
  * 2 Lanes: 3,307 crashes (16.54%)
  * 3 Lanes: 3,328 crashes (16.64%)
  * 4 Lanes: 3,354 crashes (16.77%)
  * 5 Lanes: 3,332 crashes (16.66%)
  * 6 Lanes: 3,314 crashes (16.57%)
* **Traffic Signal Presence**:
  * No Signal Present (`0`): **10,034 crashes (50.17%)** — Mean Risk: **0.4371**
  * Signal Present (`1`): **9,966 crashes (49.83%)** — Mean Risk: **0.4380**

---

## 7. Weather Findings
* **Weather Volume Distribution**:
  * Clear Skies: **6,690 crashes (33.45%)**
  * Rainfall: **6,677 crashes (33.39%)**
  * Dense Fog: **6,633 crashes (33.17%)**
* **Compounding Risk by Weather**:
  * Clear Weather: Mean Risk = **0.2370**
  * Rainy Weather: Mean Risk = **0.4876** (+105.7% risk increase over clear skies)
  * Foggy Weather: Mean Risk = **0.5891** (+148.6% risk increase over clear skies!)

---

## 8. Traffic Findings
* **Traffic Density Distribution**:
  * Low Density: **7,067 crashes (35.34%)**
  * High Density: **7,034 crashes (35.17%)**
  * Medium Density: **5,899 crashes (29.50%)**
* **Risk by Traffic Density**:
  * Low Density: Mean Risk = **0.3392**
  * Medium Density: Mean Risk = **0.3683**
  * High Density: Mean Risk = **0.5954** (+75.5% hazard increase)

---

## 9. Risk Findings
* **Empirical Risk Categorization**:
  * **Low Risk (< 0.30)**: **5,272 crashes (26.36%)**
  * **Medium Risk (0.30 to < 0.65)**: **9,918 crashes (49.59%)**
  * **High Risk (>= 0.65)**: **4,810 crashes (24.05%)**

---

## 10. Correlation Findings
* **`vehicles_involved` vs. `casualties`**:
  * Pearson $r = \mathbf{+0.5510}$ ($p < 0.0001$, statistically significant).
  * Spearman $\rho = \mathbf{+0.5134}$ ($p < 0.0001$).
  * *Interpretation*: A moderate-to-strong positive linear relationship. Collisions with more vehicles are strongly associated with higher casualty counts.
* **`visibility_score` vs. `risk_score`**:
  * Pearson $r = \mathbf{-0.7291}$ ($p < 0.0001$, statistically significant).
  * *Interpretation*: Strong negative correlation. As visibility deteriorates from high to low, collision risk escalates steeply.
* **`is_peak_hour` vs. `risk_score`**:
  * Pearson $r = \mathbf{+0.4371}$ ($p < 0.0001$, statistically significant).
  * *Interpretation*: Commuter rush hours correlate strongly with higher composite risk.
* **`risk_score` vs. `severity_score`**:
  * Pearson $r = \mathbf{+0.2595}$ ($p < 0.0001$, statistically significant).

---

## 11. Geographic Findings
* Coordinates strictly span the Indian subcontinent: Latitude 12.800172°N to 30.799960°N, Longitude 72.700017°E to 88.499861°E.
* Each city features a cluster of ~2,400 to 2,580 incidents distributed across urban roads, rural fringes, and arterial highway corridors.

---

## 12. Data Limitations
* **Macro Coordinates**: GPS coordinates reflect metropolitan regional bounding envelopes rather than surveyed physical intersections.
* **Festival Column**: 99.425% missing values limits holiday traffic analysis.
* **Omission of Demographics**: No data on driver age, license class, or specific vehicle category (two-wheelers vs. heavy trucks).
