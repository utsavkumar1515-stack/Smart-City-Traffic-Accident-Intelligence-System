# UrbanFlow: Power BI Dashboard Technical Documentation & Model Architecture
**Report Specification**: `UrbanFlow.pbix` (Manual Build Guide: `Documentation/POWERBI_BUILD_INSTRUCTIONS.md`)  
**Fact Table**: `urbanflow_cleaned` (20,000 incident rows, 34 columns)  
**Dimension Table**: `Dim_Calendar` (1,461 dates, 2022 to 2025)  
**Measures Catalog**: 25+ Production DAX Measures (`PowerBI/DAX_Measures.dax`)  
**Theme Palette**: Dark Smart City Executive Interface (`PowerBI/urbanflow_theme.json`)  
**Visual Reference Renders**: `Images/Final/` (5 publication-quality 16:9 dashboard pages)  
**Deployment Note**: Due to Power BI's proprietary VertiPaq Analysis Services columnar database engine, native `.pbix` documents cannot be compiled headlessly. The `.pbix` file on disk is a structural placeholder (931 B). Follow `POWERBI_BUILD_INSTRUCTIONS.md` to load and compile the dashboard in Microsoft Power BI Desktop.  
**Date**: September 2026  

---

## 1. Dashboard Purpose & Strategic Vision
The **UrbanFlow Power BI Dashboard** transforms 20,000 raw municipal traffic incident logs into an interactive, multi-layered decision-support system. It empowers city commissioners, urban infrastructure engineers, and traffic police departments to:
1. Track city-wide safety Key Performance Indicators (KPIs).
2. Isolate diurnal and weekly traffic friction peaks.
3. Quantify compounding environmental risk multipliers (such as fog and low visibility).
4. Pinpoint geographic collision hotspots and high-risk arterial corridors.
5. Formulate data-backed infrastructure remediation and enforcement policies.

---

## 2. Multi-Page Architecture & Page Descriptions

### Page 1: Overview (Executive Command Center)
* **Objective**: Delivers high-level situational awareness for city directors and municipal leaders.
* **Header / Filter Strip**: Synchronized global slicers for `Year`, `City`, and `Accident Severity`.
* **Top 5 KPI Cards**:
  * `Total Accidents`: **20,000**
  * `Total Casualties`: **34,529**
  * `Average Risk Score`: **0.4376**
  * `Fatal Incident Rate`: **14.94%**
  * `Peak Hour Accident %`: **24.74%**
* **Core Visuals**:
  * *Accident Trend (Line Chart)*: Continuous monthly volume curve across the 3.5-year span.
  * *Severity Breakdown (Donut Chart)*: Clean proportional breakdown (Minor: 55.1%, Major: 29.9%, Fatal: 14.9%).
  * *Top Cities (Horizontal Bar Chart)*: Volume ranking across all 8 metropolises (Chandigarh: 2,577 down to Hyderabad: 2,409).
  * *Geographic Overview (Scatter / Point Map)*: Macro coordinate distribution colored by risk tier.
  * *Key Insights Panel*: Dynamic text card highlighting verified Phase 4 findings.

### Page 2: Traffic & Time (Diurnal & Commuter Analytics)
* **Objective**: Analyzes temporal rhythms to optimize police shift scheduling and traffic signal timing.
* **Core Visuals**:
  * *24-Hour Diurnal Curve (Line Chart with Area Fill)*: Visualizes hourly volume with shaded rush-hour bands.
  * *Day-of-Week Distribution (Bar Chart)*: Monday high (2,966 crashes) to Wednesday low (2,726 crashes).
  * *Weekday vs. Weekend KPI Card*: 14,277 weekday crashes (71.39%) vs. 5,723 weekend crashes (28.62%).
  * *Peak vs. Non-Peak Comparison*: Contrasting crash count vs. situational risk score (0.604 in rush hours vs. 0.383 in off-peak).
  * *Time-of-Day Breakdown (Bar Chart)*: Night (6,721, 33.6%), Morning (4,907, 24.5%), Evening (4,192, 21.0%), Afternoon (4,180, 20.9%).
  * *Day-Hour Heatmap Matrix (Matrix Visual)*: Cross-tabulation of Day of Week vs. Hour of Day with conditional color gradient from white to deep crimson.
  * *Traffic Density vs. Risk (Column Chart)*: Low (0.339), Medium (0.368), High (0.595).

### Page 3: Accident Analysis (Causality & Environmental Dynamics)
* **Objective**: Uncovers behavioral failure modes, weather stressors, and roadway geometries.
* **Core Visuals**:
  * *Root Causes Ranking (Horizontal Bar)*: Distraction (4,026), Overspeeding (4,025), Weather (3,997), DUI (3,978), Poor Road (3,974).
  * *Causes Pareto Chart (Line & Clustered Column)*: Frequency bars with cumulative percentage line.
  * *Weather vs. Average Risk (Clustered Column)*: Side-by-side comparison showing risk surging from 0.237 (Clear) to 0.589 (Fog).
  * *Road Type vs. Severity (Stacked Bar)*: Severity composition across Highway, Rural, and Urban corridors.
  * *Vehicles Involved vs. Casualties (Scatter Plot)*: Visualizing the moderate-to-strong positive correlation ($r = +0.5510$).
  * *Visibility Distribution & Risk Curve*: Frequency across Low, Medium, and High visibility vs. mean risk score.

### Page 4: Hotspots & Map (Geospatial & Corridor Intelligence)
* **Objective**: Pinpoints high-risk spatial clusters and ranks dangerous road segments.
* **Core Visuals**:
  * *Main Geospatial Collision Map*: Point map plotting latitude and longitude, bubble size driven by `[Total Casualties]`, bubble color dynamically mapped to `risk_category` (🟢 Green = Low Risk, 🟡 Amber = Medium Risk, 🔴 Red = High Risk).
  * *Hotspot Ranking 1 (Volume)*: Cities ordered by raw collision count.
  * *Hotspot Ranking 2 (Mean Risk)*: Cities ordered by average composite risk score.
  * *Hotspot Ranking 3 (Critical High-Risk Crashes)*: Cities ordered by count of severe incidents (score $\ge 0.65$).
  * *Road Corridor Matrix Table*: Cross-tabulation of City and Road Type with in-line data bars on average risk.

### Page 5: Risk & Insights (Executive Strategy & Predictive Governance)
* **Objective**: Translates empirical risk metrics into municipal policy interventions.
* **Core Visuals**:
  * *Risk Score Target Gauge*: Evaluates current average risk (0.438) against the municipal target threshold (0.300).
  * *Risk Category Share (Donut Chart)*: Low Risk (26.36%), Medium Risk (49.59%), High Risk (24.05%).
  * *Average Risk by Severity (Bar Chart)*: Illustrates the dramatic jump in fatal collision risk (0.608 vs. 0.407).
  * *Risk vs. Casualties (Box Plot / Scatter)*: Visualizes distribution of risk across casualty counts ($r = +0.1200$).
  * *7-Pillar Data Story Panel*: Structured narrative summarizing What, When, Where, Conditions, Severity, Risk, and Action.
  * *Municipal Recommendations Panel*: Concrete action items for automated radar enforcement, dynamic VMS signs, and signal optimization.

---

## 3. Core KPI & DAX Measure Definitions

| Measure Name | DAX Expression | Business / Analytical Meaning |
| :--- | :--- | :--- |
| **Total Accidents** | `COUNTROWS('urbanflow_cleaned')` | Counts total collision events in current filter context. |
| **Total Casualties** | `SUM('urbanflow_cleaned'[casualties])` | Aggregates all human injuries and fatalities. |
| **Total Vehicles** | `SUM('urbanflow_cleaned'[vehicles_involved])` | Counts all motor vehicles damaged or involved. |
| **Average Risk Score** | `AVERAGE('urbanflow_cleaned'[risk_score])` | Computes composite environmental/situational hazard index. |
| **Fatal Accident Rate**| `DIVIDE([Fatal Accidents], [Total Accidents], 0)` | Proportion of collisions resulting in loss of life (target: <10%). |
| **Peak Hour %** | `DIVIDE([Peak Hour Accidents], [Total Accidents], 0)` | Proportion of crashes occurring in rush hours (8–10 AM, 5–7 PM). |
| **High Risk %** | `DIVIDE([High Risk Accidents], [Total Accidents], 0)` | Proportion of crashes with risk score $\ge 0.65$. |
| **Severity Index** | `DIVIDE(([Fatal]*3)+([Major]*2)+([Minor]*1), [Total], 0)` | Weighted composite severity metric (Min: 1.0, Max: 3.0). |

---

## 4. Filter Context & Interactive Slicer Strategy
* **Global Slicers (Synchronized across all 5 pages via Sync Slicers)**:
  * `Year` (from `Dim_Calendar[Year]`)
  * `City` (from `urbanflow_cleaned[city]`)
  * `Accident Severity` (from `urbanflow_cleaned[accident_severity]`)
* **Page-Specific Slicers**:
  * Page 2: `time_period`, `is_weekend`
  * Page 3: `cause`, `road_type`
  * Page 4: `risk_category`, `weather`
  * Page 5: `traffic_density`
* **Visual Interaction Setting**: All visuals are configured to **Filter** rather than **Highlight** to guarantee crisp, clean cross-filtering.

---

## 5. Design, Accessibility & Color Integrity
* **Consistent Semantic Color Coding**:
  * 🟢 **Low Risk (`< 0.30`)**: Emerald Green (`#10B981`)
  * 🟡 **Medium Risk (`0.30 - 0.65`)**: Amber Orange (`#F59E0B`)
  * 🔴 **High Risk (`>= 0.65`)**: Crimson Red (`#EF4444`)
* **Dark Interface Theme**: Dark navy canvas (`#0B132B`) with elevated slate containers (`#111827`) provides high contrast against electric cyan (`#38BDF8`) data elements, reducing eye fatigue during continuous control-room monitoring.
* **Colorblind Accessibility**: All color-coded elements are accompanied by explicit text labels, category badges, and numerical metrics to avoid relying solely on color hue.
