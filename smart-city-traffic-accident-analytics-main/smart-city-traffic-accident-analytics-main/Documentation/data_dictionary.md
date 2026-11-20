# UrbanFlow Data Dictionary

## Comprehensive Master Attribute Dictionary (34 Columns)

| Field Name | Description & Meaning | Source | Data Type | Permissible Range / Categories | Operational / Analytical Use |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `accident_id` | Unique sequential collision record index. | Raw | Integer | 0 to 19,999 | Primary key / entity tracking. |
| `city` | Metropolitan urban jurisdiction where incident occurred. | Raw | Categorical (String) | `bangalore`, `chandigarh`, `chennai`, `delhi`, `hyderabad`, `kolkata`, `mumbai`, `pune` | Geographic slicer, regional comparative analysis. |
| `state` | State or union territory governing the accident location. | Raw | Categorical (String) | `delhi`, `karnataka`, `maharashtra`, `punjab`, `tamil nadu`, `telangana`, `west bengal` | State-level policy assessment. |
| `latitude` | GPS latitude coordinate in decimal degrees. | Raw | Float | 12.800172 to 30.799960 | Geospatial map plotting, spatial concentration. |
| `longitude` | GPS longitude coordinate in decimal degrees. | Raw | Float | 72.700017 to 88.499861 | Geospatial map plotting, spatial concentration. |
| `date` | Calendar date of collision occurrence. | Raw | Date (`YYYY-MM-DD`) | 2020-01-01 to 2024-12-31 | Relationship link to Date Table (`Dim_Calendar`). |
| `time` | Clock timestamp of collision occurrence. | Raw | Time (`HH:MM:SS`) | 00:00:00 to 23:59:00 | Temporal profiling, diurnal cycle modeling. |
| `hour` | Discrete hour of collision (24-hour clock). | Raw | Integer | 0 to 23 | Hourly collision curves, peak hour derivation. |
| `day_of_week` | Day name on which incident occurred. | Raw | Categorical (String) | `Monday` through `Sunday` | Day-of-week risk and volume comparison. |
| `is_weekend` | Binary flag indicating weekend occurrence. | Raw | Binary (0 / 1) | 0 (Weekday: Mon–Fri), 1 (Weekend: Sat–Sun) | Weekend vs. weekday traffic behavior analysis. |
| `road_type` | Physical roadway hierarchy classification. | Raw | Categorical (String) | `highway`, `rural`, `urban` | Infrastructure risk comparison. |
| `lanes` | Physical lane count of the roadway segment. | Raw | Integer | 1, 2, 3, 4, 5, 6 | Capacity and throughput safety analysis. |
| `traffic_signal` | Signalized intersection indicator. | Raw | Binary (0 / 1) | 0 (No signal), 1 (Traffic signal present) | Intersection control safety audit. |
| `weather` | Atmospheric condition at time of crash. | Raw | Categorical (String) | `clear`, `fog`, `rain` | Environmental hazard driver analysis. |
| `visibility` | Categorical sight distance classification. | Raw | Categorical (String) | `low`, `medium`, `high` | Driver sight restriction evaluation. |
| `temperature` | Ambient atmospheric temperature in Celsius. | Raw | Float | 15.0 to 40.0 °C | Weather correlation analysis. |
| `traffic_density` | Ambient road congestion level at collision time. | Raw | Categorical (String) | `low`, `medium`, `high` | Multi-vehicle collision hazard modeling. |
| `cause` | Primary reported contributing human or road factor. | Raw | Categorical (String) | `distraction`, `drunk driving`, `overspeeding`, `poor road`, `weather` | Root cause Pareto analysis, policy intervention. |
| `accident_severity` | Human and physical collision damage outcome. | Raw | Categorical (String) | `minor`, `major`, `fatal` | Core severity KPI, fatality rate analysis. |
| `vehicles_involved` | Number of motor vehicles involved in collision. | Raw | Integer | 1 to 5 | Multi-vehicle crash dynamics, pile-up analysis. |
| `casualties` | Total injured or deceased persons. | Raw | Integer | 0 to 5 | Human injury KPI, EMS dispatch planning. |
| `is_peak_hour` | Rush-hour commuter surge flag. | Raw | Binary (0 / 1) | 1 (08–10 & 17–19), 0 (Off-Peak) | Rush-hour traffic triage, patrol scheduling. |
| `festival` | Cultural or national holiday celebration flag. | Raw | String | `"None"` (99.4% missing in raw; imputed) | Documented data limitation. |
| `risk_score` | Calculated multi-factor composite risk index. | Raw | Float | 0.1000 to 1.0000 | Primary quantitative severity and risk metric. |
| `year` | Calendar year extracted from date. | Engineered | Integer | 2020, 2021, 2022, 2023, 2024 | Multi-year longitudinal trend tracking. |
| `month` | Numerical month of incident. | Engineered | Integer | 1 to 12 | Seasonal pattern analysis, date sorting. |
| `month_name` | Full alphabetical month name. | Engineered | String | `January` through `December` | Power BI time slicers, monthly charts. |
| `day` | Day of month. | Engineered | Integer | 1 to 31 | Calendar granularity. |
| `week_number` | ISO calendar week index. | Engineered | Integer | 1 to 53 | Weekly operational reporting. |
| `time_period` | 4-part day segment grouping. | Engineered | Categorical (String) | `Morning`, `Afternoon`, `Evening`, `Night` | Diurnal shift analysis, volume vs risk disparity. |
| `severity_score` | Standardized ordinal ranking of crash severity. | Engineered | Integer (Ordinal) | 1 (Minor), 2 (Major), 3 (Fatal) | Weighted severity calculations, correlation testing. |
| `risk_category` | Discretized municipal risk operational tier. | Engineered | Categorical (String) | `Low Risk`, `Medium Risk`, `High Risk` | Target for ML classification, executive filters. |
| `casualty_category`| Binned grouping of casualty count. | Engineered | Categorical (String) | `0 Casualties`, `1-2 Casualties`, `3-5 Casualties` | Injury severity distribution visuals. |
| `visibility_score` | Numerical rank of sight distance. | Engineered | Integer (Ordinal) | 1 (Low), 2 (Medium), 3 (High) | Quantitative visibility correlation & ML input. |
