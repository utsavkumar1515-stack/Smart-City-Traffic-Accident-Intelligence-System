# UrbanFlow: Data Cleaning, Preprocessing & Feature Engineering Notes
**Dataset Source**: `Dataset/raw/indian_roads_dataset.csv`  
**Output Target**: `Dataset/cleaned/urbanflow_cleaned.csv`  
**Pipeline Author**: UrbanFlow Smart City Traffic Intelligence Team  
**Date**: September 2026  

---

## 1. Problems Found During Raw Audit
1. **Unparsed Dates**: The `date` column was stored as a raw text string (`object`), preventing time-intelligence grouping, date slicing, and seasonal trend analysis.
2. **Severe Missingness in `festival`**: The `festival` column had 19,885 null values out of 20,000 rows (99.425% missing).
3. **Unstandardized Categorical Text**: Potential leading/trailing whitespaces or inconsistent string casing across categories like `weather`, `road_type`, `city`, and `accident_severity`.
4. **Absence of Analytical Dimensions**: Lack of high-level time groupings (e.g., Morning Rush, Night), risk tiers (Low/Medium/High), or ordinal severity rankings needed for executive dashboard reporting and machine learning.

---

## 2. Cleaning Decisions & Rationale

| Column | Observed State | Cleaning Action | Methodological Rationale |
| :--- | :--- | :--- | :--- |
| `date` | String format (`YYYY-MM-DD`) | Parsed to native `datetime64[ns]` | Enables temporal extraction (`year`, `month`, `day`, `week_number`) and Power BI calendar relationships. |
| `festival` | 99.425% nulls (115 non-null) | Replaced nulls with string `'None'` | A null in this column does not indicate missing data; it signifies an ordinary, non-holiday traffic day. Imputing `'None'` documents this fact without fabricating fake holiday dates or dropping rows. |
| Categorical strings | Varying casing / whitespace | Stripped whitespace, lowered case | Ensures cross-filtering in Power BI and grouping in Python does not treat `"Rain"` and `"rain "` as distinct categories. |
| `accident_id` | Unique integers (0 to 19,999) | Retained as integer primary key | Verified 0 duplicate IDs. Retained for row-level granularity. |
| Coordinates | `latitude`, `longitude` | Validated within India bounds | Bounded within 12.80°N–30.80°N and 72.70°E–88.50°E. No invalid coordinates found. |
| Numeric bounds | Hour (0–23), Lanes (1–6), Vehicles (1–5), Casualties (0–5) | Verified via boundary assertions | Confirmed no negative values, zero-vehicle collisions, or invalid hours exist. |

---

## 3. Columns Excluded from Primary Analysis

1. **`festival`**:
   * *Reason*: With **99.425% missingness**, using this column in multivariate regressions, decision trees, or correlation matrices would introduce extreme selection bias. It is retained as a descriptive record in the cleaned CSV, but excluded from primary statistical modeling.
2. **`accident_id`**:
   * *Reason*: Arbitrary sequential identifier; carries no analytical or predictive information.

---

## 4. Newly Engineered Analytical Features (10 New Columns)

| New Feature | Data Type | Logic / Derivation | Analytical Purpose |
| :--- | :---: | :--- | :--- |
| `year` | `int64` | `df['date'].dt.year` (2022 to 2025) | Annual trend comparison and multi-year KPIs. |
| `month` | `int64` | `df['date'].dt.month` (1 to 12) | Chronological monthly ordering in charts. |
| `month_name` | `object` | `df['date'].dt.month_name()` | Human-readable month labels for report charts. |
| `day` | `int64` | `df['date'].dt.day` (1 to 31) | Day-of-month incident distribution. |
| `week_number` | `int64` | `df['date'].dt.isocalendar().week` | Weekly surge and seasonality tracking. |
| `time_period` | `object` | 4-tier diurnal grouping (Night, Morning, Afternoon, Evening) | Evaluates collision rates across natural human activity cycles. |
| `severity_score` | `int64` | Ordinal mapping: `minor`=1, `major`=2, `fatal`=3 | Enables weighted Severity Index calculation in Power BI DAX. |
| `risk_category` | `object` | Empirical 3-tier cutoffs (`Low Risk`, `Medium Risk`, `High Risk`) | Categorical segmentation for KPI cards, slicers, and map coloring. |
| `casualty_category` | `object` | `0 Casualties`, `1-2 Casualties`, `3-5 Casualties` | Facilitates multi-casualty collision drill-downs. |
| `visibility_score` | `int64` | Ordinal mapping: `low`=1, `medium`=2, `high`=3 | Allows numerical correlation testing against severity. |

---

## 5. Methodology for Time-of-Day & Risk Categories

### 5.1 Time-of-Day Grouping (`time_period`)
Selected based on urban mobility rhythms and ambient daylight cycles:
* **Night (22:00 to 05:59)**: Hours 22, 23, 0, 1, 2, 3, 4, 5 (6,721 records, 33.6%). Captures reduced lighting, elevated speeding, and late-night alcohol impairment.
* **Morning (06:00 to 11:59)**: Hours 6, 7, 8, 9, 10, 11 (4,907 records, 24.5%). Encompasses early commuter movements and the morning rush peak (8–10 AM).
* **Afternoon (12:00 to 16:59)**: Hours 12, 13, 14, 15, 16 (4,180 records, 20.9%). Covers intercity transit, commercial delivery traffic, and school dismissals.
* **Evening (17:00 to 21:59)**: Hours 17, 18, 19, 20, 21 (4,192 records, 21.0%). Covers the evening return commute rush (5–8 PM) and dusk visibility decline.

### 5.2 Risk Category Threshold Methodology (`risk_category`)
Rather than arbitrarily guessing cutoffs, the thresholds are grounded in the empirical distribution of `risk_score` (Min: 0.10, 25%: 0.25, Median: 0.45, 75%: 0.60, Max: 1.00):
* **Low Risk (`< 0.30`)**: **5,272 records (26.36%)** $\rightarrow$ Corresponds to the lower quartile (crashes under clear skies and low traffic density).
* **Medium Risk (`0.30 <= score < 0.65`)**: **9,918 records (49.59%)** $\rightarrow$ Represents the central 50% interquartile operational baseline.
* **High Risk (`>= 0.65`)**: **4,810 records (24.05%)** $\rightarrow$ Corresponds to the upper quartile (incidents compounded by fog, high traffic density, and severe outcomes).

---

## 6. Data Limitations Introduced by Missing Data
* **Festival Inferences**: Because 99.425% of rows do not record a festival, we cannot evaluate holiday traffic surges. The remaining 115 records provide anecdotal rather than statistically representative samples.
* **Granular Vehicle Classes**: The dataset does not distinguish between two-wheelers, auto-rickshaws, private cars, or commercial heavy vehicles, requiring road classification (`highway`, `urban`, `rural`) to serve as a proxy for transit profile.
