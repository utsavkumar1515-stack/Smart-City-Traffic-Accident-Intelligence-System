# UrbanFlow Machine Learning Documentation: Predictive Collision Risk Classification

## Executive Summary
This document provides complete technical, mathematical, and operational documentation for the **UrbanFlow Predictive Collision Risk Classification Engine** developed during Phase 7. While retrospective analytics highlight historical incident counts, this machine learning prototype enables proactive smart city governance by predicting the impending risk tier (**Low Risk**, **Medium Risk**, or **High Risk**) based strictly on **pre-incident situational context**.

---

## 1. Machine Learning Objective
* **Task Formulation**: Supervised multiclass classification.
* **Target Mapping**: Given an ambient situational vector $\mathbf{x}$, predict the risk category $\hat{y} \in \{\text{Low Risk}, \text{Medium Risk}, \text{High Risk}\}$.
* **Operational Application**:
  1. **Preemptive Police Deployment**: Positioning traffic enforcement units ahead of peak congestion hours in low-visibility zones.
  2. **Intelligent Transportation Systems (ITS)**: Dynamically alerting motorists via overhead Variable Message Signs (VMS) and connected navigation apps when weather and congestion thresholds breach safe operational limits.
  3. **Emergency Medical Services (EMS) Staging**: Pre-positioning trauma ambulances within 3 km of predicted high-risk arterial corridors.

---

## 2. Target Variable Definition: `risk_category`
The target variable is the operational classification derived during Phase 3 feature engineering from the continuous `risk_score` (ranging from $0.100$ to $1.000$, $\mu = 0.4376$, $\sigma = 0.2181$, $\text{median} = 0.4500$):

| Risk Category | Discretization Threshold | Overall Count ($N=20,000$) | Overall Share (%) | Test Set Support ($N=4,000$) |
| :--- | :--- | :--- | :--- | :--- |
| **Low Risk** | $\text{risk\_score} < 0.30$ | 5,272 | 26.36% | 1,054 |
| **Medium Risk** | $0.30 \le \text{risk\_score} < 0.65$ | 9,918 | 49.59% | 1,984 |
| **High Risk** | $\text{risk\_score} \ge 0.65$ | 4,810 | 24.05% | 962 |

---

## 3. Data Leakage Audit & Feature Selection
To preserve predictive validity and prevent artificial 100% accuracy from post-incident information, a strict data leakage audit was conducted:

### 3.1 Excluded Features (Data Leakage & Redundancies)
* **`risk_score`**: **Excluded**. Direct mathematical source of the target; inclusion causes 100% label leakage.
* **`accident_severity` & `severity_score`**: **Excluded**. Post-crash investigation outcome; collision severity cannot be known before a collision occurs.
* **`casualties` & `casualty_category`**: **Excluded**. Post-crash human injury outcome; unavailable during pre-incident risk assessment.
* **`accident_id`**: **Excluded**. Arbitrary database key with zero physical relationship to risk.
* **`festival`**: **Excluded**. 99.425% missing; uninformative.
* **`date` & `time`**: **Excluded**. Redundant with engineered temporal features (`hour`, `day_of_week`, `is_weekend`, `month`).

### 3.2 Included Features (Pre-Incident Situational Context)
1. **Atmospheric / Environmental**:
   * `weather` (`fog`, `rain`, `clear`) — Categorical
   * `visibility_score` (Ordinal proxy: 1 = Low, 2 = Medium, 3 = High) — Continuous / Ordinal
   * `temperature` (Continuous °C, 15.0°C to 40.0°C) — Continuous
2. **Traffic Dynamics**:
   * `traffic_density` (`low`, `medium`, `high`) — Categorical
3. **Road Infrastructure**:
   * `road_type` (`highway`, `urban`, `rural`) — Categorical
   * `lanes` (Physical lane count: 1, 2, 3, 4, 5, 6) — Discrete Numerical
   * `traffic_signal` (Binary presence: 0 = No, 1 = Yes) — Binary
4. **Temporal Context**:
   * `hour` (0 to 23) — Discrete Numerical
   * `day_of_week` (Monday through Sunday) — Categorical
   * `month` (1 to 12) — Discrete Numerical
   * `is_weekend` (0 = Weekday, 1 = Weekend) — Binary
   * `is_peak_hour` (1 = 08:00–10:00 & 17:00–19:00, 0 = Off-Peak) — Binary
5. **Geographic Jurisdiction**:
   * `city` (8 major metropolitan areas) — Categorical

---

## 4. Preprocessing & Partitioning Pipeline
1. **Partitioning**: Stratified 80/20 train-test split (`random_state=42`, stratify on `risk_category`).
   * Training Set: 16,000 incidents (80%)
   * Testing Set: 4,000 incidents (20%)
2. **ColumnTransformer Pipeline**:
   * **Categorical Features** (`weather`, `road_type`, `traffic_density`, `city`, `day_of_week`): One-Hot Encoded (`drop='first'`).
   * **Numerical Features** (`hour`, `is_weekend`, `is_peak_hour`, `month`, `visibility_score`, `temperature`, `lanes`, `traffic_signal`): Scaled to $\mu=0, \sigma=1$ using `StandardScaler`.
   * **Leakage Prevention**: All transformations are fitted strictly on `X_train` and applied out-of-sample to `X_test`.

---

## 5. Model Evaluation & Benchmark Comparison

Three distinct model families were trained on the training partition and benchmarked on the held-out test partition ($N=4,000$):

| Model | Test Accuracy | Macro Precision | Macro Recall | Macro F1 | Weighted F1 | Model Characteristics |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Multinomial Logistic Regression** | 87.68% | 0.8964 | 0.8711 | 0.8738 | 0.8751 | Linear baseline with balanced class weights; convex log-odds formulation. |
| **Decision Tree (`max_depth=6`)** | **88.88%** | **0.9081** | **0.8789** | **0.8845** | **0.8867** | Highly interpretable hierarchical partitioning; captures non-linear thresholds. |
| **Random Forest (`n_est=100`, `depth=12`)** | 88.72% | 0.9045 | 0.8782 | 0.8829 | 0.8851 | Bagged ensemble; minimizes variance and provides robust generalization. |

### 5.1 Per-Class Performance Breakdown (Decision Tree & Random Forest)
Both non-linear models achieve over 88.7% overall accuracy. Looking at the class-specific metrics for the best tree-based models:

* **High Risk Class**:
  * Precision: **98.9% – 100.0%** (When the model alerts for High Risk, it is virtually never a false positive).
  * Recall: **73.18%** (Detects 704 out of 962 actual high-risk collisions using pre-incident data alone).
  * F1-Score: **0.8411 – 0.8451**.
* **Low Risk Class**:
  * Precision: **85.0% – 85.1%**.
  * Recall: **99.8% – 100.0%** (Virtually zero low-risk events misclassified as severe).
  * F1-Score: **0.9184 – 0.9193**.
* **Medium Risk Class**:
  * Precision: **87.4%**.
  * Recall: **90.3% – 90.7%**.
  * F1-Score: **0.8882 – 0.8899**.

### 5.2 Critical Safety Property: Zero Catastrophic Misclassifications
Inspection of the confusion matrix reveals an essential real-world safety finding:
$$\text{Actual Low Risk} \to \text{Predicted High Risk} = \mathbf{0}$$
$$\text{Actual High Risk} \to \text{Predicted Low Risk} = \mathbf{0}$$

Across all 4,000 test incidents, there was **zero overlap between Low Risk and High Risk**. All classification uncertainty is confined strictly to adjacent operational boundaries (`Low` $\leftrightarrow$ `Medium` or `Medium` $\leftrightarrow$ `High`). This confirms the model is safe for operational decision-making.

---

## 6. Feature Importance Analysis
Using the Random Forest Mean Decrease in Impurity (MDI) metric, the top 10 contributing features are:

| Rank | Feature | Importance Share (%) | Physical Interpretation |
| :--- | :--- | :--- | :--- |
| 1 | `visibility_score` | **30.33%** | Dominant individual predictor. Low atmospheric visibility directly limits driver reaction distance. |
| 2 | `traffic_density_medium` | **17.64%** | Inter-vehicle proximity threshold; moderate congestion bounds high-risk exposure. |
| 3 | `traffic_density_low` | **17.07%** | Free-flow traffic strongly predicts lower risk tiers. |
| 4 | `weather_fog` | **10.82%** | Thick fog compounds visual degradation and slick road surfaces. |
| 5 | `hour` | **4.18%** | Diurnal traffic variation and ambient lighting conditions. |
| 6 | `is_peak_hour` | **3.62%** | Morning and evening rush hour congestion surges. |
| 7 | `temperature` | **2.95%** | Ambient thermal conditions. |
| 8 | `month` | **2.42%** | Seasonal weather and monsoon cycles. |
| 9 | `weather_rain` | **2.36%** | Reduced tire friction and spray visibility degradation. |
| 10 | `lanes` | **1.83%** | Roadway capacity. |

**Key Takeaway**: Atmospheric conditions and traffic density account for **over 78%** of total predictive importance. In contrast, static infrastructure (`road_type`, `traffic_signal`, `city`) contributes under 3% combined, proving that environmental and operational dynamics drive accident risk far more than road geometry.

---

## 7. Model Validation & Sanity Checklist
* [x] Target classes present and properly formatted (`Low Risk`, `Medium Risk`, `High Risk`).
* [x] Stratified 80/20 train/test split strictly preserves class balance (49.6% Med, 26.4% Low, 24.1% High).
* [x] Zero data leakage: `risk_score`, `accident_severity`, `severity_score`, and `casualties` completely isolated.
* [x] Preprocessing transformers fitted strictly on training data (`X_train`).
* [x] All evaluations performed on out-of-sample test partition (`X_test`).
* [x] Fixed random seed (`random_state=42`) guarantees 100% exact reproducibility.
* [x] Multiclass metrics evaluated using both Macro and Weighted averaging.

---

## 8. Limitations & Methodological Caveats
1. **Cross-Sectional Collision Records**: The model is trained on incident records rather than continuous vehicle trajectories. It predicts collision risk *conditional on an incident occurring or developing*, not baseline exposure (traffic volume per lane-km).
2. **Discretization Boundary Artifacts**: Classifying continuous scores into discrete tiers introduces threshold sensitivity near cutoffs (e.g., $0.649$ is Medium Risk while $0.651$ is High Risk).
3. **Behavioral Telematics Gap**: Driver behavioral factors (speeding, distraction, intoxication) are reported post-crash and excluded to maintain leakage integrity. Future IoT-connected telematics can provide real-time behavioral proxies.

---

## 9. Conclusion
The UrbanFlow Phase 7 Machine Learning prototype successfully bridges descriptive analysis and predictive smart city intelligence. With **88.9% accuracy**, **0.885 Macro F1**, and **zero catastrophic false negatives**, it establishes a robust baseline for municipal traffic management systems.
