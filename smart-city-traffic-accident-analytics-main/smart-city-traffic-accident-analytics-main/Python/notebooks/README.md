# UrbanFlow — Jupyter Notebooks

This directory contains the analytical notebooks for the **UrbanFlow Smart City Traffic & Accident Analytics** project.

## Notebook Execution Order

| # | Notebook | Phase | Description |
|---|----------|-------|-------------|
| 1 | [`01_data_exploration.ipynb`](01_data_exploration.ipynb) | Phase 2 | Complete dataset inspection, data quality analysis, missing value audit, boundary checks |
| 2 | [`02_exploratory_data_analysis.ipynb`](02_exploratory_data_analysis.ipynb) | Phase 4 | EDA, statistical analysis, Python visualizations (weather, time, road, geography) |
| 3 | [`03_risk_machine_learning.ipynb`](03_risk_machine_learning.ipynb) | Phase 7 | Advanced risk analysis, ML classification (Logistic Regression, Decision Tree, Random Forest) |
| 4 | [`04_urbanflow_analysis.ipynb`](04_urbanflow_analysis.ipynb) | Phase 3–4 | Combined data cleaning, preprocessing, feature engineering, and analysis pipeline |

## Running the Notebooks

### Prerequisites

```bash
pip install -r ../../requirements.txt
```

### Execute All (recommended)

```bash
# From the project root
jupyter nbconvert --to notebook --execute --inplace Python/notebooks/01_data_exploration.ipynb
jupyter nbconvert --to notebook --execute --inplace Python/notebooks/02_exploratory_data_analysis.ipynb
jupyter nbconvert --to notebook --execute --inplace Python/notebooks/03_risk_machine_learning.ipynb
jupyter nbconvert --to notebook --execute --inplace Python/notebooks/04_urbanflow_analysis.ipynb
```

### Interactive Exploration

```bash
# From the project root
jupyter notebook Python/notebooks/
```

## Data Dependencies

All notebooks expect data at the following relative paths (relative to `Python/notebooks/`):

- `../../Dataset/raw/indian_roads_dataset.csv` — Original raw dataset (20,000 rows × 24 columns)
- `../../Dataset/cleaned/urbanflow_cleaned.csv` — Cleaned dataset (20,000 rows × 34 columns, Phase 3 output)

If the raw dataset path is missing, notebooks fall back to `../Dataset/...`.

## Key Results

| Metric | Value |
|--------|-------|
| Dataset size | 20,000 accidents × 34 features |
| Total casualties | 34,519 |
| Fatal incidents | 2,782 (13.91%) |
| Mean risk score | 0.4376 |
| Weather ANOVA η² | 46.12% variance explained |
| ML best model | Decision Tree — 88.88% accuracy |
| Random Forest | 88.72% accuracy, zero catastrophic errors |
