# UrbanFlow Report Screenshot & Figure Insertion Plan

## Master Academic Report Visual Index

This document defines the exact visual assets, figure numbers, captions, report sections, and analytical purposes for every figure embedded in the final semester project report (`Report/UrbanFlow_Final_Report.docx` and `Report/UrbanFlow_Final_Report.pdf`).

---

### Part 1: System Architecture & Methodology Figures

| Fig # | File Path | Formal Caption | Target Section | Analytical & Academic Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Figure 1** | `Images/Architecture/urbanflow_system_architecture.png` | **Figure 1**: UrbanFlow End-to-End System Architecture Pipeline. | Chapter 3: Technology Stack & System Architecture | Illustrates the 4-tier pipeline connecting data ingestion, statistical analysis, Power BI serving, and decision support. |
| **Figure 2** | `Images/Architecture/urbanflow_data_flow.png` | **Figure 2**: Level-1 Data Flow Diagram (DFD) of the UrbanFlow Pipeline. | Chapter 4: Data Pipeline & Methodology | Details information flow across external entities, Python cleaning processes, data stores, and analytical outputs. |
| **Figure 3** | `Images/Architecture/urbanflow_methodology.png` | **Figure 3**: The 14-Step Research and Engineering Methodology Framework. | Chapter 4: Data Pipeline & Methodology | Establishes the systematic academic research lifecycle from problem definition to decision-support recommendations. |

---

### Part 2: Exploratory Data Analysis & Statistical Figures

| Fig # | File Path | Formal Caption | Target Section | Analytical & Academic Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Figure 4** | `Images/EDA/04_accidents_by_hour.png` | **Figure 4**: Hourly Collision Volume Distribution Across 24-Hour Cycle. | Chapter 5: Exploratory Data Analysis (Time) | Displays the diurnal collision volume progression and identifies nighttime collision concentrations. |
| **Figure 5** | `Images/EDA/08_accident_severity.png` | **Figure 5**: Collision Severity Breakdown (Minor, Major, Fatal). | Chapter 5: Exploratory Data Analysis (Severity) | Establishes baseline collision severity shares (55.2% Minor, 30.8% Major, 13.9% Fatal). |
| **Figure 6** | `Images/EDA/10_cause_pareto.png` | **Figure 6**: Pareto Analysis of Primary Reported Accident Causes. | Chapter 5: Exploratory Data Analysis (Causes) | Demonstrates equal ~20% distribution across all 5 reported causes, showing Pareto inapplicability. |
| **Figure 7** | `Images/EDA/12_weather_analysis.png` | **Figure 7**: Accident Distribution and Severity Breakdown Across Weather Conditions. | Chapter 5: Exploratory Data Analysis (Weather) | Details collision volumes across Clear, Rain, and Foggy atmospheric conditions. |
| **Figure 8** | `Images/EDA/18_correlation_heatmap.png` | **Figure 8**: Correlation Heatmap Across Numerical Features. | Chapter 5: Exploratory Data Analysis (Correlations) | Highlights key correlations ($r=+0.5510$ for vehicles vs. casualties; $r=-0.7291$ for visibility vs. risk). |

---

### Part 3: Advanced Risk Analysis Figures

| Fig # | File Path | Formal Caption | Target Section | Analytical & Academic Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Figure 9** | `Images/Advanced_Analysis/01_risk_by_city.png` | **Figure 9**: Collision Risk Score and High-Risk Incidents Across 8 Metropolitan Areas. | Chapter 6: Advanced Risk Analysis (Geography) | Distinguishes raw accident volume from average risk severity across metropolitan jurisdictions. |
| **Figure 10**| `Images/Advanced_Analysis/03_risk_by_weather.png` | **Figure 10**: Empirical Risk Score Distribution by Weather Condition. | Chapter 6: Advanced Risk Analysis (Environment) | Proves the +148.7% elevation in mean risk under fog ($0.5891$) vs. clear weather ($0.2369$). |
| **Figure 11**| `Images/Advanced_Analysis/05_risk_by_hour.png` | **Figure 11**: Collision Volume vs. Average Risk Score Hourly Disparity Curve. | Chapter 6: Advanced Risk Analysis (Temporal) | Demonstrates the fundamental divergence between nighttime volume and rush-hour severity. |
| **Figure 12**| `Images/Advanced_Analysis/09_high_risk_profile.png`| **Figure 12**: High-Risk Collision Signature Across Weather, Density, and Severity. | Chapter 6: Advanced Risk Analysis (Profiles) | Establishes the high-risk operational archetype (dense traffic + low visibility + peak commuting hours). |
| **Figure 13**| `Images/Advanced_Analysis/10_risk_driver_association.png` | **Figure 13**: Statistical Driver Association Matrix (ANOVA $\eta^2$ & Pearson $\|r\|$). | Chapter 6: Advanced Risk Analysis (Drivers) | Ranks relative strength of risk factors; proves atmospheric conditions dominate road geometry. |
| **Figure 14**| `Images/Advanced_Analysis/11_geographic_risk_concentration.png` | **Figure 14**: Spatial Distribution of High-Risk Collisions Across Metropolitan Clusters. | Chapter 6: Advanced Risk Analysis (Hotspots) | Maps localized high-risk transit corridors reaching 31%–38.5% concentration in East Delhi and Mumbai. |

---

### Part 4: Interactive Power BI Dashboard Figures

| Fig # | File Path | Formal Caption | Target Section | Analytical & Academic Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Figure 15**| `Images/PowerBI/01_overview.png` | **Figure 15**: Executive Overview Dashboard (Page 1). | Chapter 7: Power BI Dashboard & Visual Analytics | High-level municipal KPI scorecard: total crashes, casualties, fatality rate, and severity distribution. |
| **Figure 16**| `Images/PowerBI/02_traffic_time.png` | **Figure 16**: Traffic & Temporal Dynamics Dashboard (Page 2). | Chapter 7: Power BI Dashboard & Visual Analytics | Interactive exploration of diurnal curves, rush-hour volume surges, and day-of-week patterns. |
| **Figure 17**| `Images/PowerBI/03_accident_analysis.png` | **Figure 17**: Accident Severity & Root Causes Dashboard (Page 3). | Chapter 7: Power BI Dashboard & Visual Analytics | Deep-dive cross-filtering of crash outcomes, driver behavioral factors, and road infrastructure. |
| **Figure 18**| `Images/PowerBI/04_hotspots_map.png` | **Figure 18**: Geographic Hotspots & Spatial Distribution Dashboard (Page 4). | Chapter 7: Power BI Dashboard & Visual Analytics | Interactive geospatial coordinate plotting identifying severe localized metropolitan cluster points. |
| **Figure 19**| `Images/PowerBI/05_risk_insights.png` | **Figure 19**: Advanced Risk Insights & Triage Dashboard (Page 5). | Chapter 7: Power BI Dashboard & Visual Analytics | Strategic risk matrix combining atmospheric visibility degradation, congestion, and time tiers. |

---

### Part 5: Machine Learning Prototype Figures

| Fig # | File Path | Formal Caption | Target Section | Analytical & Academic Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Figure 20**| `Images/Machine_Learning/01_confusion_matrix.png` | **Figure 20**: Random Forest Multiclass Confusion Matrix ($N=4,000$). | Chapter 8: Machine Learning Risk Classification | Proves safety-critical zero catastrophic error property ($0.0\%$ false high/low risk alarms). |
| **Figure 21**| `Images/Machine_Learning/02_model_comparison.png` | **Figure 21**: Machine Learning Algorithm Performance Benchmark. | Chapter 8: Machine Learning Risk Classification | Compares Accuracy, Macro F1, Weighted F1, and Recall across Logistic Regression, Decision Tree, and RF. |
| **Figure 22**| `Images/Machine_Learning/03_feature_importance.png` | **Figure 22**: Random Forest Gini Feature Importance (MDI) Ranking. | Chapter 8: Machine Learning Risk Classification | Quantifies predictive contribution: visibility ($30.3\%$) and traffic density ($34.7\%$) dominate. |
| **Figure 23**| `Images/Machine_Learning/05_multiclass_roc_curves.png` | **Figure 23**: Multiclass One-vs-Rest ROC Curves for Risk Categories. | Chapter 8: Machine Learning Risk Classification | Confirms outstanding discrimination capacity ($\text{AUC} > 0.94$ across all 3 operational tiers). |
