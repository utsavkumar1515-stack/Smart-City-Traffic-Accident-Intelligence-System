# UrbanFlow: Data Quality Report & Audit Matrix
**Dataset Source**: `Dataset/raw/indian_roads_dataset.csv`  
**Total Records**: 20,000 | **Total Features**: 24  
**Audit Date**: September 2026  

---

## 1. Comprehensive Attribute Audit Table

| Column Name | Data Type | Missing Count | Missing % | Unique Values | Status / Cleaning Action |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `accident_id` | `int64` | 0 | 0.00% | 20,000 | **Pristine**. Primary key verified; 0 duplicates found. Retain as-is. |
| `city` | `object` | 0 | 0.00% | 8 | **Clean**. Standardize lowercase string strip. Retain for spatial slicing. |
| `state` | `object` | 0 | 0.00% | 7 | **Clean**. 1-to-1 correspondence with cities confirmed. Standardize strings. |
| `latitude` | `float64` | 0 | 0.00% | 19,907 | **Clean**. Bounds [12.80°N, 30.80°N] verified within India. Set as Latitude in BI. |
| `longitude` | `float64` | 0 | 0.00% | 19,927 | **Clean**. Bounds [72.70°E, 88.50°E] verified within India. Set as Longitude in BI. |
| `date` | `object` | 0 | 0.00% | 1,201 | **Type conversion needed**. Parse to native `datetime64[ns]` for calendar modeling. |
| `time` | `object` | 0 | 0.00% | 24 | **Clean**. Formatted as `H:00` (e.g., 5:00 to 23:00). Retain for reference. |
| `hour` | `int64` | 0 | 0.00% | 24 | **Clean**. Bounded between 0 and 23. Retain for diurnal analysis. |
| `day_of_week` | `object` | 0 | 0.00% | 7 | **Clean**. Monday through Sunday. Standardize casing and order chronologically. |
| `is_weekend` | `int64` | 0 | 0.00% | 2 | **Clean**. Binary (0 = Weekday, 1 = Weekend). 14,277 weekdays, 5,723 weekends. |
| `road_type` | `object` | 0 | 0.00% | 3 | **Clean**. Categories: `urban` (6,745), `rural` (6,639), `highway` (6,616). |
| `lanes` | `int64` | 0 | 0.00% | 6 | **Clean**. Integer values 1 to 6. No negative or 0 lane counts. |
| `traffic_signal` | `int64` | 0 | 0.00% | 2 | **Clean**. Binary flag (0 = No signal, 1 = Signal present). |
| `weather` | `object` | 0 | 0.00% | 3 | **Clean**. Categories: `clear` (6,690), `rain` (6,677), `fog` (6,633). |
| `visibility` | `object` | 0 | 0.00% | 3 | **Clean**. Categories: `high` (6,690), `medium` (6,677), `low` (6,633). |
| `temperature` | `int64` | 0 | 0.00% | 26 | **Clean**. Ranges from 15°C to 40°C. Typical tropical / sub-tropical Indian span. |
| `traffic_density`| `object` | 0 | 0.00% | 3 | **Clean**. Categories: `low` (7,067), `high` (7,034), `medium` (5,899). |
| `cause` | `object` | 0 | 0.00% | 5 | **Clean**. Root causes: `distraction`, `overspeeding`, `weather`, `drunk driving`, `poor road`. |
| `accident_severity`| `object` | 0 | 0.00% | 3 | **Clean**. `minor` (11,025), `major` (5,988), `fatal` (2,987). Map to ordinal score in Phase 4. |
| `vehicles_involved`| `int64` | 0 | 0.00% | 5 | **Clean**. Values 1 to 5. Minimum 1 vehicle confirmed (no 0 vehicle accidents). |
| `casualties` | `int64` | 0 | 0.00% | 6 | **Clean**. Values 0 to 5. Mean 1.73 casualties per collision. No negative values. |
| `is_peak_hour` | `int64` | 0 | 0.00% | 2 | **Clean**. Binary flag. 15,052 Non-Peak (75.3%), 4,948 Peak (24.7%). |
| `festival` | `object` | 19,885 | **99.43%** | 4 | **Severe missingness**. Impute nulls with `'None'`. Exclude from core statistical models. |
| `risk_score` | `float64` | 0 | 0.00% | 18 | **Clean**. Bounded in [0.10, 1.00]. Mean: 0.438, Median: 0.450. Use for risk tiers. |

---

## 2. Special Investigation: The `festival` Column

- **Total Records**: 20,000
- **Missing Values**: 19,885 records (99.425%)
- **Present Values**: 115 records (0.575%)
  - `Holi`: 38
  - `Eid`: 34
  - `Diwali`: 31
  - `New Year`: 12

### Academic Evaluation of Action Options:
* **Option A (Remove entirely from dataset)**: Pragmatic, but loses the contextual record that 115 incidents did occur on high-profile holiday celebrations.
* **Option B (Retain but strictly exclude from primary statistical modeling)**: **RECOMMENDED**. Replace nulls with `'None'` or `'Regular Day'`. This documents that 99.4% of crashes occur during non-festival operations without fabricating data or dropping rows.
* **Option C (Fabricate or Impute festival names)**: **UNACCEPTABLE**. Imputing festival labels for 99.4% of data would constitute scientific misconduct and introduce severe artificial bias.
