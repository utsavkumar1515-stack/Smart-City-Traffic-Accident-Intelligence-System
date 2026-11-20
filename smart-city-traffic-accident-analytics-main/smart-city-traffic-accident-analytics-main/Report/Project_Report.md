# URBANFLOW
## Interactive Smart City Traffic & Accident Analytics
### Comprehensive Academic Semester Project Report

---

**Course**: Data Visualization & Analytics Semester Project  
**Academic Year**: 2025–2026 | Semester VI  
**Author**: [Student Name]  
**Roll Number**: [Roll Number]  
**Department**: Department of Computer Science & Engineering / Data Science  
**Institution**: [College / University Name]  
**Supervisor**: [Supervisor Name], Project Supervisor  

---

## Certificate of Originality
This is to certify that the project entitled **"URBANFLOW: Interactive Smart City Traffic & Accident Analytics"** submitted by **[Student Name]** (Roll No: **[Roll Number]**) in partial fulfillment of the requirements for the *Data Visualization & Analytics* course during Academic Year 2025–2026 is an authentic record of original project work carried out under my supervision.

To the best of my knowledge, the matter embodied in this project report has not been submitted elsewhere for the award of any other degree or diploma.

*Date*: September 2026  
*Supervisor*: [Supervisor Name]  
*Head of Department*: [Head of Department Name]  

---

## Declaration of Authorship
I hereby declare that this semester project report entitled **"URBANFLOW: Interactive Smart City Traffic & Accident Analytics"** is entirely my own work. All analytical computations, data processing steps, visualizations, Power BI dashboard models, and machine learning scripts were developed using the designated project dataset. Wherever external literature, frameworks, or principles have been referenced, appropriate academic citations are provided in the references section.

**[Student Name]**  
Roll Number: [Roll Number]  
Department of Computer Science & Engineering  

---

## Acknowledgements
I would like to express my deepest gratitude to my project supervisor, **[Supervisor Name]**, for their invaluable guidance, constructive critique, and continuous encouragement throughout the conceptualization and development of UrbanFlow. I am also grateful to the faculty and course instructors of Data Visualization & Analytics for providing the computational resources, tools, and theoretical foundation required to execute this comprehensive data analytics initiative.

---

## Abstract
Rapid urbanization and increasing motor vehicle volumes in metropolitan India have significantly elevated road traffic hazards, resulting in substantial casualties, economic disruption, and municipal strain. Traditional traffic safety analysis relies on fragmented retrospective tables and static police reports, restricting the ability of traffic managers to proactively mitigate high-risk conditions. This semester project presents **UrbanFlow**, an end-to-end data analytics, interactive visual intelligence, and predictive machine learning system developed to transform raw traffic collision records into actionable smart city decision support.

Operating on a validated multimodal dataset comprising exactly **20,000 recorded collision events** across eight major Indian metropolitan centers (Chandigarh, Chennai, Kolkata, Pune, Mumbai, Bangalore, Delhi, and Hyderabad) spanning 2020 through 2024, UrbanFlow executes a rigorous 14-step research methodology. A Python data engineering pipeline conducts comprehensive quality auditing, data type casting, and feature engineering, preserving 100% of observations with zero row attrition while engineering 10 operational attributes including diurnal time segments, rush-hour flags, and risk classifications.

Exploratory and advanced risk analysis reveals an empirical divergence between collision volume and incident severity: while nighttime hours (22:00–05:59) record the highest overall volume (6,721 collisions, 33.61%), commuter rush hours exhibit a **+57.7% higher average risk score** ($0.6038$ vs $0.3830$) and an elevated high-risk collision rate of **38.32%**. One-way ANOVA and correlation testing prove that atmospheric degradation (fog $\eta^2 = 0.4612$, visibility $r = -0.7291$) and ambient traffic density ($\eta^2 = 0.2844$) dominate collision risk, whereas physical road geometry (lane count $r = -0.0017$) and metropolitan city ($p = 0.918$) show statistical invariance. An interactive five-page Power BI dashboard suite backed by 25+ certified DAX measures provides dynamic multi-scale filtering, geospatial coordinate plotting, and risk triage.

To enable proactive safety governance, a supervised machine learning prototype was trained strictly on pre-incident situational variables, enforcing zero data leakage. Benchmarked on a held-out test partition ($N = 4,000$), a Random Forest classifier achieved **88.72% accuracy** and **0.8829 Macro F1**, while completely eliminating catastrophic misclassifications between Low and High risk tiers ($0.0\%$ false negatives). UrbanFlow bridges retrospective visual analytics and proactive machine learning, providing a validated blueprint for automated municipal warning systems and emergency dispatch.

---

## 1. Introduction & Background
Urban road transportation networks in rapidly developing economies represent both vital economic arteries and severe public safety vulnerabilities. According to official reports by the Ministry of Road Transport and Highways (MoRTH), India experiences over 450,000 road traffic crashes annually, resulting in more than 150,000 fatalities and extensive socioeconomic harm. Dense urban centers such as Delhi, Mumbai, Bengaluru, and Chennai face unique compounded hazards: intense vehicular congestion, heterogeneous traffic composition, fluctuating tropical weather events, and variable road infrastructure.

Historically, municipal traffic authorities and urban planning departments have analyzed traffic safety through static, retrospective tabular summaries. These traditional records categorize accidents long after they occur, primarily for insurance processing and statutory reporting. While informative at an aggregate level, retrospective tables suffer from three severe practical shortcomings:
1. **Inability to Disentangle Incident Volume from Severity**: High crash counts often cluster during night hours due to speed and visibility, but high-lethality multi-vehicle emergencies peak during morning and evening commuter rush hours.
2. **Lack of Interactive Drill-Down Capability**: Decision makers cannot seamlessly isolate how environmental factors alter risk across specific roadway hierarchies in individual cities.
3. **Absence of Predictive Decision Support**: Static reports provide no mechanism to forecast impending risk levels based on real-time ambient conditions, precluding proactive interventions.

---

## 2. Problem Statement, Motivation & Objectives
### 2.1 Problem Statement
Modern smart cities generate vast quantities of multimodal traffic telemetry and accident incident reports. However, municipal traffic managers, police dispatchers, and emergency services lack an integrated, interactive analytical platform capable of visualizing multidimensional collision patterns, identifying localized high-risk corridors, and predicting operational risk levels from pre-incident ambient conditions. Without such intelligence, traffic safety interventions remain predominantly reactive, delaying emergency medical response and misallocating municipal enforcement patrols.

### 2.2 Project Objectives
1. **Data Engineering & Integrity**: Ingest, audit, and clean 20,000 multimodal collision records spanning 8 Indian metropolitan centers, guaranteeing zero row loss while engineering 10 operational features.
2. **Exploratory & Statistical Analysis**: Quantify temporal, infrastructural, environmental, and behavioral drivers of collision frequency and severity using rigorous parametric and non-parametric tests.
3. **Advanced Risk Disparity Modeling**: Mathematically evaluate the divergence between crash volume and crash severity across diurnal cycles and identify localized geographic high-risk concentrations.
4. **Interactive Business Intelligence Suite**: Design and deploy a certified 5-page Power BI dashboard featuring star-schema data modeling, 25+ DAX measures, and seamless cross-filtering.
5. **Predictive Machine Learning Triage**: Formulate, train, and evaluate a leakage-free multiclass risk classification prototype to predict impending risk tiers with high accuracy and zero catastrophic errors.

---

## 3. Technology Stack & System Architecture
UrbanFlow adopts an enterprise-grade data science and business intelligence stack:
* **Python 3.12**: Core programming runtime.
* **Pandas 2.2 & NumPy 1.26**: Ingestion, vectorization, and data transformations.
* **SciPy 1.13**: One-Way ANOVA, Pearson and Spearman statistical calculations.
* **Scikit-Learn 1.4**: Machine learning pipeline, preprocessing, Decision Tree, Random Forest.
* **Matplotlib 3.11 & Seaborn 0.13**: High-resolution 300 DPI visualization engine.
* **Power BI Desktop & Service**: Star-schema data modeling, DAX measures, 5 interactive dashboard pages.
* **Microsoft Word & docx2pdf**: Automated compilation of publication-ready academic reports.

### Architecture Overview
The system is organized into four interconnected tiers:
* **Tier 1 (Data Ingestion & Engineering)**: Cleans raw CSV records, audits 20 data quality checks, and enriches dataset to 34 columns.
* **Tier 2 (Analytical Engine)**: Computes descriptive distributions, ANOVA effect sizes, correlation heatmaps, and spatial grids.
* **Tier 3 (Dual Serving Layer)**: Serves executive human operators via Power BI and automated triage via Scikit-Learn.
* **Tier 4 (Smart City Decision Support)**: Connects analytical intelligence to police beat scheduling, dynamic VMS warning signs, and EMS staging.

---

## 4. Data Pipeline: Cleaning, Preprocessing & Feature Engineering
* **Dataset Scope**: Exactly 20,000 observations across 8 cities spanning 2020–2024.
* **Quality Auditing**: Zero duplicate accident IDs; validated clock times (00:00–23:59); standardized lowercase categoricals.
* **The Festival Limitation**: Raw `festival` had 19,885 nulls (99.425% missing). Imputed with `"None"`; excluded from predictive modeling to avoid noise.
* **10 Engineered Attributes**: `year`, `month`, `month_name`, `day`, `week_number`, `time_period`, `severity_score`, `risk_category`, `casualty_category`, `visibility_score`.
* **Zero Attrition**: 20,000 raw rows in $\to$ 20,000 cleaned rows out (0 rows lost).

---

## 5. Exploratory Data Analysis & Empirical Findings
* **Temporal Dynamics**: Collision volume peaks at Night (6,721 collisions, 33.61%), with 02:00 recording the individual hourly peak (908 crashes). Rush hours represent 24.74% of crashes (4,948 incidents).
* **Severity Breakdown**: Minor collisions constitute 55.24% (11,048), Major collisions 30.85% (6,170), and Fatal collisions 13.91% (2,782). Approximately 1 in every 7.2 reported crashes resulted in lost lives.
* **Pareto Inapplicability**: Reported causes show equal distribution (~20% each): Distraction (20.29%), Drunk Driving (20.18%), Overspeeding (20.12%), Poor Road (19.80%), Weather (19.62%).
* **Numerical Correlations**: Vehicles Involved correlates with Casualties ($r = +0.5510, p < 0.001$). Visibility Score correlates inversely with Risk Score ($r = -0.7291, p < 0.001$).

---

## 6. Advanced Collision Risk & Hotspot Concentration Analysis
* **Volume vs. Severity Disparity**: Nighttime accounts for 33.61% of crashes but only 16.19% of high-risk incidents (mean risk 0.3687). Rush hours account for 24.74% of crashes but 38.32% of high-risk incidents (mean risk 0.6038, a **+57.7% increase**).
* **Dominant Risk Drivers**:
  * Weather condition explains **46.12% of risk variance** ($F = 8,559.5, p < 0.001, \eta^2 = 0.4612$). Fog elevates mean risk from 0.2369 (clear) to 0.5891.
  * Ambient traffic density explains **28.44% of risk variance** ($F = 3,973.7, \eta^2 = 0.2844$). High density raises high-risk collision rate to 54.65% vs 7.32% in low density.
  * Physical roadway type ($p = 0.289$), lane count ($p = 0.808$), and city jurisdiction ($p = 0.918$) display zero statistically significant association with risk score.
* **High-Risk Collision Profile**: 61.98% occur in fog; 79.92% in dense traffic; 58.73% during commuter rush hours; 37.30% result in fatal outcomes (averaging 2.075 casualties).
* **Geographic Concentration**: $0.1^\circ \times 0.1^\circ$ grid aggregation reveals high-risk transit corridors reaching 34%–38.5% concentration in East Delhi, South Mumbai Harbor, and Hinjawadi Pune.

---

## 7. Interactive Power BI Dashboard Suite
The Power BI solution (`PowerBI/UrbanFlow.pbix`) features 5 dedicated operational pages:
1. **Overview (Page 1)**: Situational awareness scorecard (20,000 Crashes, 34,519 Casualties, 13.91% Fatality Rate, 0.4376 Mean Risk).
2. **Traffic & Time (Page 2)**: 24-hour diurnal curves, peak hour volume surges, and weekday/weekend comparisons.
3. **Accident Severity & Causes (Page 3)**: Deep-dive diagnostic matrix cross-filtering driver behavior, vehicles involved, and road classification.
4. **Hotspots & Spatial Distribution (Page 4)**: Interactive geospatial coordinate map plotting casualty density across 8 metropolitan areas.
5. **Advanced Risk Insights (Page 5)**: Multi-factor risk matrix combining visibility restriction, traffic density, and time tiers.

---

## 8. Predictive Machine Learning Risk Classification Prototype
* **Objective**: Predict operational risk tier (`Low Risk`, `Medium Risk`, `High Risk`) conditional on pre-incident situational variables.
* **Leakage Guardrail**: Continuous `risk_score` (target source), `accident_severity`, `severity_score`, `casualties`, and `casualty_category` were strictly excluded.
* **Benchmark Results** (Held-Out Test Set $N = 4,000$):
  * *Multinomial Logistic Regression*: Accuracy = 87.68%, Macro F1 = 0.8738.
  * *Decision Tree (`depth=6`)*: Accuracy = **88.88%**, Macro F1 = **0.8845**.
  * *Random Forest (`100 trees, depth=12`)*: Accuracy = 88.72%, Macro F1 = 0.8829.
* **Safety-Critical Zero Catastrophic Errors**:
  * Actual Low Risk $\to$ Predicted High Risk: **0 / 1,054 (0.0%)**
  * Actual High Risk $\to$ Predicted Low Risk: **0 / 962 (0.0%)**
* **Top Features**: `visibility_score` (30.33%), `traffic_density` (34.71%), `weather_fog` (10.82%) drive >75% of model decisions.

---

## 9. Critical Discussion & Municipal Policy Implications
1. **Dynamic Variable Message Signs (VMS)**: Configure automated triggers to alert drivers and reduce speed limits when ambient visibility drops below 2 km during peak rush hours.
2. **Preemptive Emergency Medical Staging**: Pre-position trauma ambulances near identified transit corridors (East Delhi, Mumbai Harbor approach) during morning/evening commute windows.
3. **Police Patrol Rescheduling**: Reallocate municipal enforcement from routine night patrols to peak-hour congestion bottlenecks.

---

## 10. Limitations & Future Scope
* **Limitations**: Cross-sectional incident records lack vehicle-kilometer exposure denominators; 99.4% missing festival column; binned diurnal periods.
* **Future Work**: Live IoT video feeds, connected vehicle telematics, and Spatio-Temporal Graph Neural Networks (ST-GCN) for real-time 30-minute accident probability forecasting.

---

## 11. Conclusion
UrbanFlow successfully bridges retrospective descriptive analytics and proactive machine learning, providing a validated, 100% reproducible decision-support system for smart city traffic safety.

---

## 12. References
1. Ministry of Road Transport and Highways (MoRTH). (2023). *Road Accidents in India 2022*. Government of India Transport Research Wing, New Delhi.
2. World Health Organization (WHO). (2023). *Global Status Report on Road Safety 2023*. WHO, Geneva.
3. Few, S. (2012). *Show Me the Numbers: Designing Tables and Graphs to Enlighten*. Analytics Press.
4. Cairo, A. (2016). *The Truthful Art: Data, Charts, and Maps for Communication*. New Riders.
5. McKinney, W. (2022). *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter (3rd ed.)*. O'Reilly Media.
6. Ferrari, A., & Russo, M. (2020). *The Definitive Guide to DAX: Business Intelligence with Microsoft Power BI (2nd ed.)*. Microsoft Press.
7. Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.
8. Breiman, L. (2001). Random Forests. *Machine Learning*, 45(1), 5-32.
