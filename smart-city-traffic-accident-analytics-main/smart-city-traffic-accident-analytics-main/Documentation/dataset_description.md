# UrbanFlow Final Dataset Description

## 1. Overview & Provenance
* **Dataset Identifier**: Indian Roads Traffic & Accident Dataset (`indian_roads_dataset.csv` / `urbanflow_cleaned.csv`)
* **Total Observations ($N$)**: Exactly **20,000** collision events.
* **Total Columns**: **34 attributes** in the analysis-ready cleaned dataset (24 raw features + 10 engineered features).
* **Integrity Guarantee**: Zero records dropped during data cleaning ($20,000 \to 20,000$ rows retained, 0% row attrition).
* **Format**: Comma-Separated Values (UTF-8 encoding).

---

## 2. Temporal & Geographic Coverage
* **Temporal Span**: January 1, 2020 to December 31, 2024 (5 full calendar years).
  * 2020: 3,924 collisions (19.62%)
  * 2021: 4,028 collisions (20.14%)
  * 2022: 3,989 collisions (19.95%)
  * 2023: 4,082 collisions (20.41%)
  * 2024: 3,977 collisions (19.88%)
* **Geographical Coverage**: 8 major Indian metropolitan centers across 8 states/union territories:
  1. **Chandigarh** (Union Territory): 2,577 records (12.89%)
  2. **Chennai** (Tamil Nadu): 2,575 records (12.88%)
  3. **Kolkata** (West Bengal): 2,559 records (12.80%)
  4. **Pune** (Maharashtra): 2,517 records (12.58%)
  5. **Mumbai** (Maharashtra): 2,492 records (12.46%)
  6. **Bangalore** (Karnataka): 2,438 records (12.19%)
  7. **Delhi** (National Capital Territory): 2,433 records (12.16%)
  8. **Hyderabad** (Telangana): 2,409 records (12.04%)
* **Spatial Coordinate Bounds**:
  * Latitude: $12.8002^\circ\text{N}$ to $30.8000^\circ\text{N}$ ($\mu = 20.3892^\circ\text{N}, \sigma = 6.1658^\circ$)
  * Longitude: $72.7000^\circ\text{E}$ to $88.5000^\circ\text{E}$ ($\mu = 78.1733^\circ\text{E}, \sigma = 4.4860^\circ$)

---

## 3. Major Variable Groups

### 3.1 Identification & Temporal Variables
* `accident_id` (Integer): Unique sequential identifier for each collision record ($0$ to $19,999$).
* `date` (Date string / DateTime): Formatted collision occurrence date (`YYYY-MM-DD`).
* `time` (Time string): Exact 24-hour recorded collision timestamp (`HH:MM:SS`).
* `hour` (Integer, 0–23): Discrete hour of the day.
* `day_of_week` (String): Day name (`Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, `Sunday`).
* `is_weekend` (Integer, 0/1): Binary indicator (1 = Saturday/Sunday, 0 = Monday–Friday). Weekdays = 14,277 (71.38%), Weekends = 5,723 (28.62%).
* `is_peak_hour` (Integer, 0/1): Binary indicator for commuter rush hours (08:00–10:00 & 17:00–19:00). Peak = 4,948 (24.74%), Off-Peak = 15,052 (75.26%).
* `year` (Integer, 2020–2024): Year of incident.
* `month` (Integer, 1–12): Numerical month.
* `month_name` (String): Full month name (`January` to `December`).
* `day` (Integer, 1–31): Day of month.
* `week_number` (Integer, 1–53): ISO calendar week number.
* `time_period` (String): Engineered diurnal aggregation:
  * `Night (22:00-05:59)`: 6,721 incidents (33.61%)
  * `Morning (06:00-11:59)`: 4,907 incidents (24.54%)
  * `Evening (17:00-21:59)`: 4,192 incidents (20.96%)
  * `Afternoon (12:00-16:59)`: 4,180 incidents (20.90%)

### 3.2 Geographical & Administrative Variables
* `city` (String, Categorical): City jurisdiction (8 categories).
* `state` (String, Categorical): State jurisdiction (8 categories: `karnataka`, `punjab`, `tamil nadu`, `delhi`, `telangana`, `west bengal`, `maharashtra`, `punjab/haryana`).
* `latitude` (Float): Precise GPS latitude coordinate.
* `longitude` (Float): Precise GPS longitude coordinate.

### 3.3 Infrastructure & Roadway Variables
* `road_type` (String, Categorical): Classification of road segment:
  * `Urban`: 6,745 incidents (33.72%)
  * `Rural`: 6,639 incidents (33.20%)
  * `Highway`: 6,616 incidents (33.08%)
* `lanes` (Integer, 1–6): Number of physical travel lanes:
  * 1 Lane: 3,382 (16.91%)
  * 2 Lanes: 3,270 (16.35%)
  * 3 Lanes: 3,334 (16.67%)
  * 4 Lanes: 3,383 (16.92%)
  * 5 Lanes: 3,363 (16.82%)
  * 6 Lanes: 3,268 (16.34%)
* `traffic_signal` (Integer, 0/1): Signalization presence:
  * 0 (No signal): 10,003 (50.01%)
  * 1 (Signal present): 9,997 (49.99%)

### 3.4 Environmental & Atmospheric Variables
* `weather` (String, Categorical):
  * `Clear`: 6,690 incidents (33.45%)
  * `Rain`: 6,677 incidents (33.38%)
  * `Fog`: 6,633 incidents (33.17%)
* `visibility` (String, Categorical):
  * `Low`: 9,987 incidents (49.94%)
  * `High`: 6,690 incidents (33.45%)
  * `Medium`: 3,323 incidents (16.61%)
* `visibility_score` (Integer, Ordinal): Standardized ordinal mapping (1 = Low, 2 = Medium, 3 = High).
* `temperature` (Float, Numerical): Ambient temperature in degrees Celsius ($15.0^\circ\text{C}$ to $40.0^\circ\text{C}$, $\mu = 27.58^\circ\text{C}, \sigma = 7.45^\circ\text{C}$).

### 3.5 Traffic Dynamics & Incident Consequences
* `traffic_density` (String, Categorical): Ambient congestion level at time of collision:
  * `Low`: 7,067 incidents (35.33%)
  * `High`: 7,034 incidents (35.17%)
  * `Medium`: 5,899 incidents (29.50%)
* `cause` (String, Categorical): Primary reported contributing factor:
  * `Distraction`: 4,058 incidents (20.29%)
  * `Drunk Driving`: 4,036 incidents (20.18%)
  * `Overspeeding`: 4,024 incidents (20.12%)
  * `Poor Road`: 3,959 incidents (19.80%)
  * `Weather`: 3,923 incidents (19.62%)
* `accident_severity` (String, Categorical): Impact classification:
  * `Minor`: 11,048 incidents (55.24%)
  * `Major`: 6,170 incidents (30.85%)
  * `Fatal`: 2,782 incidents (13.91%)
* `severity_score` (Integer, Ordinal): Standardized scale (1 = Minor, 2 = Major, 3 = Fatal).
* `vehicles_involved` (Integer, 1–5): Total vehicles involved in crash ($\mu = 2.992, \sigma = 1.416$).
* `casualties` (Integer, 0–5): Total injured or deceased individuals ($\mu = 1.726, \sigma = 1.489$).
* `casualty_category` (String, Binned):
  * `0 Casualties`: 5,744 incidents (28.72%)
  * `1-2 Casualties`: 8,367 incidents (41.83%)
  * `3-5 Casualties`: 5,889 incidents (29.45%)

### 3.6 Risk Assessment Variables
* `risk_score` (Float, Continuous): Calculated multi-factor hazard index ($0.1000$ to $1.0000$, $\mu = 0.4376, \sigma = 0.2181, \text{median} = 0.4500$).
* `risk_category` (String, Categorical):
  * `Medium Risk (0.30 - 0.65)`: 9,918 incidents (49.59%)
  * `Low Risk (< 0.30)`: 5,272 incidents (26.36%)
  * `High Risk (>= 0.65)`: 4,810 incidents (24.05%)

---

## 4. Missing Data & Structural Limitations
1. **The `festival` Column**: In the raw dataset, `festival` contained **19,885 missing entries** (99.425% missing). It was imputed with the string `"None"` in the cleaned dataset. Due to extreme sparsity, it was excluded from core modeling to prevent statistical distortion.
2. **Observational Cross-Section**: Data points represent reported collision events. No denominator of "non-accident traffic volume" (exposure) is provided.
3. **Absence of Pavement Friction Telemetry**: Road surface coefficients are captured only through weather proxies rather than direct physical instrumentation.
