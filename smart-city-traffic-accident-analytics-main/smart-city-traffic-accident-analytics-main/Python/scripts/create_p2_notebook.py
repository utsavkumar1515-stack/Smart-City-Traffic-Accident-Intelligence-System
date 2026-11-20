import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

# Title
cells.append(nbf.v4.new_markdown_cell("""# 🔍 Phase 2: Systematic Data Exploration & Data Quality Analysis
### UrbanFlow - Smart City Traffic & Accident Analytics

This notebook executes **Phase 2: Data Exploration & Data Quality Analysis** strictly on the raw dataset: `Dataset/raw/indian_roads_dataset.csv`.

---
## Notebook Structure
1. **STEP 2.1**: Complete Dataset Inspection (Dimensions, Schema, Summary Statistics, Ranges)
2. **STEP 2.2**: Data Quality & Boundary Checks (Duplicates, Coordinates, Impossible Values)
3. **STEP 2.3**: Missing Data Analysis (Special Investigation of the `festival` column)
4. **STEP 2.4**: Data Quality Matrix
5. **STEP 2.5**: Initial Frequency & Risk Distributions
6. **STEP 2.6**: Initial Exploratory Visualizations
7. **STEP 2.7**: Output Summary & Key Insights
"""))

# Cell 1: Environment Setup
cells.append(nbf.v4.new_markdown_cell("""### 1. Environment Setup & Data Loading"""))
cells.append(nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.size'] = 10

# Load raw dataset
data_path = '../../Dataset/raw/indian_roads_dataset.csv' if os.path.exists('../../Dataset/raw/indian_roads_dataset.csv') else '../Dataset/raw/indian_roads_dataset.csv'
if not os.path.exists(data_path):
    data_path = 'Dataset/raw/indian_roads_dataset.csv'

df = pd.read_csv(data_path)
print(f"Dataset successfully loaded from: {data_path}")
print(f"Dimensions: {df.shape[0]:,} rows x {df.shape[1]} columns")
"""))

# Cell 2: Step 2.1 Inspection
cells.append(nbf.v4.new_markdown_cell("""### STEP 2.1: Complete Dataset Inspection"""))
cells.append(nbf.v4.new_code_cell("""# 1. First 10 Rows
print("--- FIRST 10 ROWS ---")
display(df.head(10))

# 2. Last 10 Rows
print("--- LAST 10 ROWS ---")
display(df.tail(10))

# 3. Data Types & Column Inventory
print("--- COLUMN DATA TYPES ---")
display(pd.DataFrame({'Column': df.columns, 'Dtype': df.dtypes.values, 'Non-Null Count': df.notnull().sum().values}))

# 4. Descriptive Statistics for Numerical Attributes
print("--- NUMERICAL ATTRIBUTES SUMMARY STATISTICS ---")
display(df.describe().round(3).T)

# 5. Missing Values & Percentages
null_counts = df.isnull().sum()
null_pct = (null_counts / len(df)) * 100
missing_df = pd.DataFrame({'Missing Count': null_counts, 'Missing %': null_pct.round(3)})
display(missing_df[missing_df['Missing Count'] > 0])

# 6. Duplication Check
print(f"Total Duplicate Rows: {df.duplicated().sum()}")
print(f"Duplicate Accident IDs: {df['accident_id'].duplicated().sum()}")

# 7. Boundary Ranges
print(f"Date Range: {df['date'].min()} to {df['date'].max()}")
print(f"Latitude Range:  {df['latitude'].min():.6f}° N to {df['latitude'].max():.6f}° N")
print(f"Longitude Range: {df['longitude'].min():.6f}° E to {df['longitude'].max():.6f}° E")
print(f"Risk Score Range: {df['risk_score'].min()} to {df['risk_score'].max()}")
print(f"Casualties Range: {df['casualties'].min()} to {df['casualties'].max()}")
print(f"Vehicles Range:   {df['vehicles_involved'].min()} to {df['vehicles_involved'].max()}")
"""))

# Cell 3: Step 2.2 Quality Checks
cells.append(nbf.v4.new_markdown_cell("""### STEP 2.2: Data Quality & Boundary Checks"""))
cells.append(nbf.v4.new_code_cell("""# Check validity of categorical unique values
categorical_cols = ['city', 'state', 'road_type', 'weather', 'visibility', 'traffic_density', 'cause', 'accident_severity']

print("--- UNIQUE CATEGORICAL VALUES ---")
for col in categorical_cols:
    print(f"{col:<18} ({df[col].nunique()} values): {df[col].unique().tolist()}")

# Verify City to State Mapping consistency
print("\\n--- CITY TO STATE CORRESPONDENCE ---")
city_state = df.groupby(['city', 'state']).size().unstack().fillna(0).astype(int)
display(city_state)

# Boundary condition tests
print("\\n--- DATA INTEGRITY ASSERTION CHECKS ---")
print(f"Invalid hour values (<0 or >23): {((df['hour'] < 0) | (df['hour'] > 23)).sum()}")
print(f"Negative casualties count:       {(df['casualties'] < 0).sum()}")
print(f"Invalid vehicle count (<1):      {(df['vehicles_involved'] < 1).sum()}")
print(f"Invalid lane count (<1):         {(df['lanes'] < 1).sum()}")
print(f"Out-of-range risk scores:        {((df['risk_score'] < 0.0) | (df['risk_score'] > 1.0)).sum()}")
"""))

# Cell 4: Step 2.3 Festival Investigation
cells.append(nbf.v4.new_markdown_cell("""### STEP 2.3: Deep Dive on Missing Data - `festival` Column"""))
cells.append(nbf.v4.new_code_cell("""fest_nulls = df['festival'].isnull().sum()
fest_pct = (fest_nulls / len(df)) * 100
print(f"Total Missing in 'festival': {fest_nulls:,} out of {len(df):,} records ({fest_pct:.3f}%)")

print("\\nNon-null entries count by festival:")
display(df['festival'].value_counts())
"""))

# Cell 5: Step 2.5 Frequency Distributions
cells.append(nbf.v4.new_markdown_cell("""### STEP 2.5: Initial Frequency & Risk Distributions"""))
cells.append(nbf.v4.new_code_cell("""print("--- 1. ACCIDENTS BY SEVERITY ---")
display(df['accident_severity'].value_counts())

print("--- 2. ACCIDENTS BY CITY ---")
display(df['city'].value_counts())

print("--- 3. ACCIDENTS BY WEATHER ---")
display(df['weather'].value_counts())

print("--- 4. ACCIDENTS BY ROAD TYPE ---")
display(df['road_type'].value_counts())

print("--- 5. ACCIDENTS BY ROOT CAUSE ---")
display(df['cause'].value_counts())

print("--- 6. ACCIDENTS BY TRAFFIC DENSITY ---")
display(df['traffic_density'].value_counts())

print("--- 7. ACCIDENTS BY DAY OF WEEK ---")
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
display(df['day_of_week'].value_counts()[days_order])

print("--- 8. ACCIDENTS BY PEAK HOUR ---")
display(df['is_peak_hour'].value_counts().rename({0: 'Off-Peak', 1: 'Peak'}))

print("--- 9. ACCIDENTS BY WEEKDAY / WEEKEND ---")
display(df['is_weekend'].value_counts().rename({0: 'Weekday', 1: 'Weekend'}))

print("--- 10. AVERAGE RISK SCORE BY CITY ---")
display(df.groupby('city')['risk_score'].mean().round(4).sort_values(ascending=False))

print("--- 11. AVERAGE RISK SCORE BY SEVERITY ---")
display(df.groupby('accident_severity')['risk_score'].mean().round(4).sort_values(ascending=False))
"""))

# Cell 6: Step 2.6 Visualizations
cells.append(nbf.v4.new_markdown_cell("""### STEP 2.6: Initial Exploratory Visualizations"""))
cells.append(nbf.v4.new_code_cell("""# 1. Severity Distribution
plt.figure(figsize=(7, 4))
sev_counts = df['accident_severity'].value_counts()
plt.bar(sev_counts.index.str.capitalize(), sev_counts.values, color=['#2ecc71', '#f39c12', '#e74c3c'], edgecolor='black', width=0.5)
for i, v in enumerate(sev_counts.values):
    plt.text(i, v + 120, f"{v:,} ({v/len(df)*100:.1f}%)", ha='center', fontweight='bold')
plt.title("Accident Severity Distribution", fontweight='bold')
plt.ylabel("Incident Count"); plt.ylim(0, max(sev_counts.values) * 1.15)
plt.tight_layout(); plt.show()

# 2. Accidents by City
plt.figure(figsize=(8, 4.5))
city_counts = df['city'].value_counts().sort_values()
plt.barh(city_counts.index, city_counts.values, color='#2980b9', edgecolor='black')
for i, v in enumerate(city_counts.values):
    plt.text(v + 25, i, f"{v:,}", va='center', fontweight='bold', fontsize=9)
plt.title("Accidents Across 8 Metropolitan Cities", fontweight='bold')
plt.xlabel("Incident Count"); plt.xlim(0, city_counts.max() * 1.15)
plt.tight_layout(); plt.show()

# 3. Hourly Diurnal Curve
plt.figure(figsize=(10, 4))
hourly = df['hour'].value_counts().sort_index()
plt.plot(hourly.index, hourly.values, marker='o', color='#2c3e50', linewidth=2)
plt.fill_between(hourly.index, hourly.values, color='#3498db', alpha=0.25)
plt.title("Diurnal 24-Hour Accident Distribution", fontweight='bold')
plt.xlabel("Hour of Day (0 to 23)"); plt.ylabel("Accidents")
plt.xticks(range(0, 24))
plt.tight_layout(); plt.show()

# 4. Risk Score Distribution
plt.figure(figsize=(8, 4))
sns.histplot(df['risk_score'], bins=20, kde=True, color='#d35400', edgecolor='black')
plt.title("Accident Risk Score Distribution", fontweight='bold')
plt.xlabel("Calculated Risk Score (0.1 to 1.0)"); plt.ylabel("Frequency")
plt.tight_layout(); plt.show()
"""))

nb.cells = cells
save_path = 'Python/notebooks/02_data_exploration.ipynb'
with open(save_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print(f"Notebook successfully written to: {save_path}")
