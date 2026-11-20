# 🚦 UrbanFlow: Smart City Traffic & Accident Analysis
## Data-Driven Urban Safety, Predictive Risk Modeling & BI Executive Report

**Project**: UrbanFlow Intelligent Transportation Analytics  
**Scope**: 20,000 Verified Incident Records Across 8 Major Indian Metros  
**Version**: 1.0 (Production Release)  
**Publication Date**: September 2026  

---

## Executive Summary

Urban traffic accidents represent an urgent public health crisis and an enormous economic burden on metropolitan municipal corporations. The **UrbanFlow** initiative delivers an end-to-end computational intelligence framework for traffic safety departments, municipal planners, and law enforcement agencies across eight major Indian metropolitan regions: **Delhi, Mumbai, Bengaluru, Pune, Kolkata, Chandigarh, Chennai, and Hyderabad**.

Through empirical examination of 20,000 incident records, statistical hypothesis testing, and supervised machine learning classification, UrbanFlow isolates key friction points:
- **55.1% (11,025 cases)**: Minor damage collisions.
- **29.9% (5,988 cases)**: Major structural or vehicular harm.
- **14.9% (2,987 cases)**: Fatal accidents resulting in catastrophic loss of life.

The platform pinpoints rush-hour congestion, adverse weather visibility, driver distraction, alcohol impairment, and high-speed multi-lane arterials as predominant compounding risk factors.

### Key Performance Indicators (KPIs)

| Metric | Measured Value | Significance |
| :--- | :--- | :--- |
| **Total Incidents Analyzed** | **20,000** | Full population sample across 8 tier-1/tier-2 metropolitan corridors |
| **Total Casualties Recorded** | **34,529** | An average of 1.73 casualties per collision incident |
| **Vehicles Involved** | **59,840** | An average of 2.99 vehicles involved per collision |
| **Catastrophic Fatality Rate** | **14.9%** | 2,987 fatal incidents requiring high-priority Vision Zero intervention |
| **Average Accident Risk Score** | **0.438 / 1.00** | Composite index evaluating environmental and operational hazards |
| **Peak Hour Concentration** | **29.1%** | 5,821 collisions occurring within morning and evening rush hours |

---

## 1. Problem Statement & Objectives

Rapid urbanization across India's premier metropolitan centers has fueled exponential growth in motor vehicle volume. Traditional municipal traffic management has historically been reactive—mobilizing emergency resources only after collisions occur.

### UrbanFlow Strategic Objectives:
1. **Multivariate Pattern Discovery**: Identify temporal, geospatial, and infrastructural accident determinants.
2. **Environmental Risk Quantification**: Quantify the impact of rainfall, dense fog, and degraded visibility.
3. **Behavioral Causality Analysis**: Evaluate the mortality rates of overspeeding, distraction, drunk driving, and infrastructure defects.
4. **Predictive Severity Modeling**: Train supervised machine learning models to classify accident severity.
5. **Operational Business Intelligence**: Deliver an executive Power BI dashboard with production DAX metrics for real-time traffic monitoring.

---

## 2. Dataset Architecture & Schema

The analytical backbone of the project is `Dataset/accident_data.csv`, containing 20,000 incident rows and 24 attributes:

| Category | Field Names | Description |
| :--- | :--- | :--- |
| **Geospatial** | `city`, `state`, `latitude`, `longitude` | Geographic coordinates across 8 Indian metropolises |
| **Temporal** | `date`, `time`, `hour`, `day_of_week`, `is_weekend`, `is_peak_hour`, `festival` | Temporal breakdown mapping rush hours and festival surges |
| **Infrastructure** | `road_type`, `lanes`, `traffic_signal` | Classification (`Highway`, `Urban`, `Rural`), lane counts (1-6), signalization |
| **Environmental** | `weather`, `visibility`, `temperature`, `traffic_density` | Weather conditions (`Rain`, `Fog`, `Clear`), visibility levels, ambient temp (°C) |
| **Incident & Behavioral** | `cause`, `vehicles_involved`, `casualties`, `accident_severity`, `risk_score` | Root cause, casualty counts, severity tier (`Minor`, `Major`, `Fatal`), risk index |

---

## 3. Exploratory Data Analysis & Empirical Findings

### 3.1 Severity Distribution
- **Minor Collisions**: 11,025 (55.13%)
- **Major Collisions**: 5,988 (29.94%)
- **Fatal Collisions**: 2,987 (14.94%)

While minor incidents form the numerical majority, major and fatal incidents account for **44.87%** of all traffic events, demonstrating the necessity of systematic infrastructure safeguards.

![Accident Severity Distribution](../Images/accident_severity_distribution.png)

### 3.2 Temporal Dynamics: Hourly Spikes & Peak Hour Surges
- Traffic collisions exhibit a bi-modal diurnal distribution:
  - **Morning Rush (08:00 - 10:00)**: Commuter congestion and merging friction.
  - **Evening Rush (17:00 - 20:00)**: Fatigue, congestion, and nightfall transition.
- **Late-Night Lethality**: Despite lower traffic volume between 23:00 and 04:00, the **mean risk score and fatality rate spike sharply** due to higher travel speeds and alcohol impairment.

![Hourly Accident Trends](../Images/hourly_accidents_peak_hours.png)

### 3.3 Geospatial Distribution Across Indian Metros
Accident volumes are broadly distributed across the 8 cities:
- **Chandigarh**: 2,577 incidents (394 fatal)
- **Chennai**: 2,575 incidents (408 fatal)
- **Kolkata**: 2,559 incidents (372 fatal)
- **Pune**: 2,517 incidents (378 fatal)
- **Mumbai**: 2,492 incidents (362 fatal)
- **Bangalore**: 2,456 incidents (351 fatal)
- **Delhi**: 2,434 incidents (368 fatal)
- **Hyderabad**: 2,390 incidents (354 fatal)

![City-Wise Breakdown](../Images/city_accident_severity.png)

### 3.4 Root Causes vs. Fatality Rates
Analysis reveals that behavioral and infrastructure causes occur in comparable volumes but yield differing casualty outcomes:
1. **Driver Distraction**: 4,026 incidents
2. **Overspeeding**: 4,025 incidents (Highest fatality rate among vehicle causes)
3. **Adverse Weather**: 3,997 incidents
4. **Drunk Driving**: 3,978 incidents (Significant nighttime fatality concentration)
5. **Poor Road Infrastructure**: 3,974 incidents

![Accident Root Causes](../Images/accident_causes_breakdown.png)

### 3.5 Weather & Visibility Impact
Atmospheric hazards act as compounding risk multipliers:
- Under **Clear Weather & High Visibility**, mean risk score averages **0.38**.
- Under **Rain & Low Visibility**, mean risk score elevates to **0.50**.
- Under **Dense Fog & Low Visibility**, mean risk score peaks at **0.54**, driving multi-vehicle highway chain-reaction crashes.

![Weather & Visibility Impact](../Images/weather_visibility_impact.png)

### 3.6 Road Infrastructure & Lane Geometries
- **Urban Streets**: 6,745 incidents (Intersectional conflicts, pedestrian friction)
- **Rural Connectors**: 6,639 incidents (Lack of median physical separation, high head-on impact rate)
- **Multi-Lane Highways**: 6,616 incidents (High-speed impacts, heavy commercial vehicle involvement)

![Road Type & Lanes](../Images/road_type_lanes_severity.png)

---

## 4. Machine Learning & Predictive Modeling

A **Random Forest Classifier** was trained to predict accident severity (`Minor`, `Major`, `Fatal`) using an 80/20 stratified split.

### Top Feature Importances (Gini Impurity)
1. **Casualties Count (18.5%)**: Primary signal of structural collapse and emergency severity.
2. **Ambient Temperature (12.3%)**: Strong seasonal proxy for monsoon downpours, summer tire blowouts, and winter fog.
3. **Hour of Day (11.5%)**: Reflects lighting conditions, commuter density, and nocturnal speeding patterns.
4. **Vehicles Involved (8.4%)**: Differentiates multi-vehicle collisions from single-vehicle skids.
5. **Number of Lanes (7.5%)**: Strongly influences travel velocities and overtaking maneuvers.

![Feature Importance](../Images/feature_importance.png)

### Normalized Confusion Matrix
The model demonstrates balanced classification performance with high recall on high-frequency classes and clear boundary separation for fatal events.

![Confusion Matrix](../Images/model_confusion_matrix.png)

---

## 5. Power BI Business Intelligence Architecture

The project delivers a dedicated Power BI suite:
- **`PowerBI/UrbanFlow.pbix`**: Power BI project package.
- **`PowerBI/DAX_Measures.dax`**: Comprehensive suite of 25+ DAX calculations covering volume, casualty rates, severity indices, and temporal intelligence.
- **`PowerBI/PowerQuery_Transformations.m`**: Automated ETL and date dimension scripts.
- **`PowerBI/PowerBI_Dashboard_Guide.md`**: Complete 4-page dashboard wireframe blueprint.

---

## 6. Smart City Strategic Action Plan

| Timeframe | Intervention | Mechanism | Expected Impact |
| :--- | :--- | :--- | :--- |
| **Immediate (0-6 Months)** | **Automated Speed Enforcement** | Radar and ANPR camera networks on arterial highways | 25-30% reduction in high-speed fatal collisions |
| **Immediate (0-6 Months)** | **Targeted Nocturnal DUI Checkpoints** | High-visibility enforcement between 22:00 and 04:00 | 18-22% drop in late-night alcohol-related crashes |
| **Medium-Term (6-18 Months)** | **Dynamic Variable Message Signs (VMS)** | Automated speed limit reductions during fog and rain | 15% drop in adverse weather pileups |
| **Medium-Term (6-18 Months)** | **Adaptive Traffic Signal Controllers (ATSC)** | Dynamic green-phase adjustment during peak rush | 12-15% decrease in intersectional fender benders |
| **Long-Term (18-36 Months)** | **Road Safety Civil Engineering** | Median dividers, rumble strips, and illuminated signage | 35-40% reduction in single-lane head-on crashes |

---

## 7. Conclusion

UrbanFlow proves that data science and interactive business intelligence can bridge the gap between municipal planning and real-world road safety. By adopting the predictive models and strategic recommendations outlined in this report, municipal authorities can accelerate their transition toward **Vision Zero** traffic environments.
