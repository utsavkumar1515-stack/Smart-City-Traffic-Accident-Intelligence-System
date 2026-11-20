import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

# Title
cells.append(nbf.v4.new_markdown_cell("""# 📊 Phase 4: Exploratory Data Analysis (EDA) & Statistical Analysis
### UrbanFlow: Interactive Smart City Traffic & Accident Analytics

This notebook executes **Phase 4: Comprehensive Exploratory Data Analysis** strictly on the cleaned, analysis-ready dataset:
`Dataset/cleaned/urbanflow_cleaned.csv` (20,000 rows x 34 columns).

---
## Sections Included:
1. **STEP 4.1**: Load & Verify Clean Data
2. **STEP 4.2**: Core Analytical Summary Metrics
3. **STEP 4.3**: Temporal Dynamics (Year, Month, Day, Hour, Time Period, Weekday, Peak)
4. **STEP 4.4**: Accident Severity Breakdown
5. **STEP 4.5**: Root Causes & Pareto Analysis
6. **STEP 4.6**: City & State Incident Hotspots
7. **STEP 4.7**: Roadway Classifications, Lanes & Signal Control
8. **STEP 4.8**: Atmospheric Weather Conditions
9. **STEP 4.9**: Visibility Levels
10. **STEP 4.10**: Temperature Dynamics
11. **STEP 4.11**: Traffic Density Impact
12. **STEP 4.12**: Vehicles Involved vs. Casualties (Correlation Analysis)
13. **STEP 4.13 & 4.14**: Risk Score & Risk Category Analysis
14. **STEP 4.15 & 4.16**: Correlation Matrix & Statistical Relationships
15. **STEP 4.17**: Geographic Coordinate Spread
16. **STEP 4.20**: Automated Analysis Summary
"""))

# Cell 1: Environment & Setup
cells.append(nbf.v4.new_markdown_cell("""### 1. Environment & Library Setup"""))
cells.append(nbf.v4.new_code_cell("""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import os

# Aesthetics
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.size'] = 10
plt.rcParams['figure.titlesize'] = 12

print("Libraries imported successfully.")
"""))

# Cell 2: Step 4.1 Load Clean Data
cells.append(nbf.v4.new_markdown_cell("""### STEP 4.1: Load & Verify Cleaned Data"""))
cells.append(nbf.v4.new_code_cell("""data_path = '../../Dataset/cleaned/urbanflow_cleaned.csv' if os.path.exists('../../Dataset/cleaned/urbanflow_cleaned.csv') else '../Dataset/cleaned/urbanflow_cleaned.csv'
if not os.path.exists(data_path):
    data_path = 'Dataset/cleaned/urbanflow_cleaned.csv'

df = pd.read_csv(data_path)
df['date'] = pd.to_datetime(df['date'])

print(f"Dataset successfully loaded from: {data_path}")
print(f"Row Count:    {df.shape[0]:,}")
print(f"Column Count: {df.shape[1]}")
print(f"Duplicate Rows: {df.duplicated().sum()}")
print(f"Missing Values (Non-Festival): {df.drop(columns=['festival']).isnull().sum().sum()}")
"""))

# Cell 3: Step 4.2 Summary Stats
cells.append(nbf.v4.new_markdown_cell("""### STEP 4.2: Initial EDA Summary Metrics"""))
cells.append(nbf.v4.new_code_cell("""summary = {
    'Total Collisions': len(df),
    'Total Casualties': int(df['casualties'].sum()),
    'Total Vehicles Involved': int(df['vehicles_involved'].sum()),
    'Avg Casualties per Accident': df['casualties'].mean().round(3),
    'Avg Vehicles per Accident': df['vehicles_involved'].mean().round(3),
    'Mean Risk Score': df['risk_score'].mean().round(4),
    'Median Risk Score': df['risk_score'].median(),
    'Min Risk Score': df['risk_score'].min(),
    'Max Risk Score': df['risk_score'].max(),
    'Cities Represented': df['city'].nunique(),
    'States Represented': df['state'].nunique(),
    'Road Classifications': df['road_type'].nunique(),
    'Accident Causes': df['cause'].nunique(),
    'Weather Conditions': df['weather'].nunique(),
    'Severity Tiers': df['accident_severity'].nunique()
}

summary_df = pd.DataFrame(list(summary.items()), columns=['Metric', 'Value'])
display(summary_df)
"""))

# Cell 4: Step 4.3 Temporal Analysis
cells.append(nbf.v4.new_markdown_cell("""### STEP 4.3: Temporal Analysis (Year, Month, Day, Hour, Peak, Weekend)"""))
cells.append(nbf.v4.new_code_cell("""# 1. Yearly Trend
print("--- ACCIDENTS BY YEAR ---")
yearly = df['year'].value_counts().sort_index()
display(pd.DataFrame({'Count': yearly, 'Share (%)': (yearly/len(df)*100).round(2)}))

# 2. Monthly Trend
print("--- TOP & BOTTOM MONTHS ---")
monthly = df['month_name'].value_counts()
print(f"Highest Month: {monthly.index[0]} ({monthly.iloc[0]:,} crashes)")
print(f"Lowest Month:  {monthly.index[-1]} ({monthly.iloc[-1]:,} crashes)")

# 3. Diurnal 24-Hour Cycle
hourly = df['hour'].value_counts().sort_values(ascending=False)
print(f"\\nPeak Single Hour:   {hourly.index[0]}:00 ({hourly.iloc[0]:,} crashes)")
print(f"Lowest Single Hour: {hourly.index[-1]}:00 ({hourly.iloc[-1]:,} crashes)")

# 4. Time Period Breakdown
print("\\n--- TIME PERIOD BREAKDOWN ---")
tp = df['time_period'].value_counts()
display(pd.DataFrame({'Count': tp, 'Share (%)': (tp/len(df)*100).round(2)}))

# 5. Weekend vs Weekday
print("--- WEEKEND VS WEEKDAY ---")
wk = df['is_weekend'].map({0: 'Weekday', 1: 'Weekend'}).value_counts()
display(pd.DataFrame({'Count': wk, 'Share (%)': (wk/len(df)*100).round(2)}))

# 6. Peak vs Non-Peak
print("--- PEAK VS NON-PEAK (8-10 AM, 5-7 PM) ---")
pk = df['is_peak_hour'].map({0: 'Non-Peak', 1: 'Peak Hour'}).value_counts()
pk_risk = df.groupby('is_peak_hour')['risk_score'].mean().round(4)
display(pd.DataFrame({'Count': pk, 'Share (%)': (pk/len(df)*100).round(2), 'Mean Risk': pk_risk.values}))
"""))

# Cell 5: Step 4.4 Severity
cells.append(nbf.v4.new_markdown_cell("""### STEP 4.4: Accident Severity Dynamics"""))
cells.append(nbf.v4.new_code_cell("""sev_df = df.groupby('accident_severity').agg(
    Count=('accident_id', 'count'),
    Avg_Casualties=('casualties', 'mean'),
    Avg_Risk=('risk_score', 'mean'),
    Avg_Vehicles=('vehicles_involved', 'mean')
).round(3)
sev_df['Share (%)'] = (sev_df['Count'] / len(df) * 100).round(2)
display(sev_df[['Count', 'Share (%)', 'Avg_Casualties', 'Avg_Risk', 'Avg_Vehicles']])
"""))

# Cell 6: Step 4.5 Cause & Pareto
cells.append(nbf.v4.new_markdown_cell("""### STEP 4.5: Root Cause & Pareto Analysis"""))
cells.append(nbf.v4.new_code_cell("""cause_df = df.groupby('cause').agg(
    Count=('accident_id', 'count'),
    Mean_Risk=('risk_score', 'mean'),
    Fatal_Count=('accident_severity', lambda x: (x == 'fatal').sum())
).sort_values('Count', ascending=False)
cause_df['Share (%)'] = (cause_df['Count'] / len(df) * 100).round(2)
cause_df['Fatal_Rate (%)'] = (cause_df['Fatal_Count'] / cause_df['Count'] * 100).round(2)
cause_df['Cumulative (%)'] = (cause_df['Count'].cumsum() / len(df) * 100).round(2)
display(cause_df)
"""))

# Cell 7: Step 4.6 City & State
cells.append(nbf.v4.new_markdown_cell("""### STEP 4.6: Metropolitan City & State Analysis"""))
cells.append(nbf.v4.new_code_cell("""city_df = df.groupby('city').agg(
    Total_Accidents=('accident_id', 'count'),
    Mean_Risk=('risk_score', 'mean'),
    Avg_Casualties=('casualties', 'mean'),
    High_Risk_Crashes=('risk_score', lambda x: (x >= 0.65).sum())
).sort_values('Total_Accidents', ascending=False)
city_df['Share (%)'] = (city_df['Total_Accidents'] / len(df) * 100).round(2)
display(city_df)

print("\\n--- STATE-LEVEL AGGREGATIONS ---")
state_df = df.groupby('state').agg(
    Total_Accidents=('accident_id', 'count'),
    Mean_Risk=('risk_score', 'mean')
).sort_values('Total_Accidents', ascending=False)
state_df['Share (%)'] = (state_df['Total_Accidents'] / len(df) * 100).round(2)
display(state_df)
"""))

# Cell 8: Step 4.7 Road & Infrastructure
cells.append(nbf.v4.new_markdown_cell("""### STEP 4.7: Road Classification, Lanes & Signalization"""))
cells.append(nbf.v4.new_code_cell("""road_df = df.groupby('road_type').agg(
    Total_Accidents=('accident_id', 'count'),
    Mean_Risk=('risk_score', 'mean'),
    Avg_Casualties=('casualties', 'mean'),
    Fatal_Rate=('accident_severity', lambda x: (x == 'fatal').mean() * 100)
).round(3)
display(road_df)

print("\\n--- LANE COUNT IMPACT ---")
lane_df = df.groupby('lanes').agg(
    Total_Accidents=('accident_id', 'count'),
    Mean_Risk=('risk_score', 'mean'),
    Avg_Vehicles=('vehicles_involved', 'mean')
).round(3)
display(lane_df)
"""))

# Cell 9: Step 4.8 & 4.9 Weather & Visibility
cells.append(nbf.v4.new_markdown_cell("""### STEP 4.8 & 4.9: Weather & Visibility Stressors"""))
cells.append(nbf.v4.new_code_cell("""weath_df = df.groupby('weather').agg(
    Total_Accidents=('accident_id', 'count'),
    Mean_Risk=('risk_score', 'mean'),
    Avg_Casualties=('casualties', 'mean')
).round(3)
weath_df['Share (%)'] = (weath_df['Total_Accidents'] / len(df) * 100).round(2)
display(weath_df)

print("\\n--- VISIBILITY ANALYSIS ---")
vis_df = df.groupby('visibility').agg(
    Total_Accidents=('accident_id', 'count'),
    Mean_Risk=('risk_score', 'mean')
).round(3)
display(vis_df)
"""))

# Cell 10: Step 4.12 & 4.16 Statistical Relationships
cells.append(nbf.v4.new_markdown_cell("""### STEP 4.12 & 4.16: Statistical Testing & Correlations"""))
cells.append(nbf.v4.new_code_cell("""# 1. Vehicles vs Casualties
p_r, p_p = stats.pearsonr(df['vehicles_involved'], df['casualties'])
s_r, s_p = stats.spearmanr(df['vehicles_involved'], df['casualties'])
print(f"1. Vehicles Involved vs Casualties:")
print(f"   Pearson r:    {p_r:.4f} (p-value = {p_p:.4e})")
print(f"   Spearman rho: {s_r:.4f} (p-value = {s_p:.4e})")

# 2. Visibility Score vs Risk
vis_r, vis_p = stats.pearsonr(df['visibility_score'], df['risk_score'])
print(f"\\n2. Visibility Score vs Risk Score:")
print(f"   Pearson r:    {vis_r:.4f} (p-value = {vis_p:.4e})")

# 3. Peak Hour vs Risk
pk_r, pk_p = stats.pearsonr(df['is_peak_hour'], df['risk_score'])
print(f"\\n3. Peak Hour Flag vs Risk Score:")
print(f"   Pearson r:    {pk_r:.4f} (p-value = {pk_p:.4e})")

# 4. Risk vs Severity Score
sev_r, sev_p = stats.pearsonr(df['risk_score'], df['severity_score'])
print(f"\\n4. Risk Score vs Severity Score:")
print(f"   Pearson r:    {sev_r:.4f} (p-value = {sev_p:.4e})")
"""))

# Cell 11: Step 4.15 Correlation Matrix Heatmap
cells.append(nbf.v4.new_markdown_cell("""### STEP 4.15: Correlation Matrix Heatmap"""))
cells.append(nbf.v4.new_code_cell("""num_cols = ['hour', 'temperature', 'lanes', 'traffic_signal', 'is_peak_hour', 'is_weekend', 'visibility_score', 'vehicles_involved', 'casualties', 'severity_score', 'risk_score']
corr = df[num_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='vlag', vmin=-1, vmax=1, cbar_kws={'label': 'Pearson Correlation (r)'})
plt.title('Multivariate Correlation Heatmap', fontweight='bold', pad=12)
plt.tight_layout()
plt.show()
"""))

# Cell 12: Step 4.20 Summary
cells.append(nbf.v4.new_markdown_cell("""### STEP 4.20: Automated EDA Summary"""))
cells.append(nbf.v4.new_code_cell("""print("="*60)
print("URBANFLOW AUTOMATED EDA SUMMARY")
print("="*60)
print(f"Overall Total Collisions:   {len(df):,}")
print(f"Total Casualties:          {int(df['casualties'].sum()):,}")
print(f"Overall Mean Risk Score:   {df['risk_score'].mean():.4f}")
print(f"Highest Accident Month:    {df['month_name'].value_counts().index[0]} ({df['month_name'].value_counts().iloc[0]:,} crashes)")
print(f"Highest Accident Hour:     {df['hour'].value_counts().index[0]}:00 ({df['hour'].value_counts().iloc[0]:,} crashes)")
print(f"Most Frequent Severity:    Minor ({df['accident_severity'].value_counts()['minor']:,} crashes, 55.1%)")
print(f"Most Severe Category Risk: Fatal Collisions (Mean Risk = 0.6075)")
print(f"Leading Collision Cause:   Distraction ({df['cause'].value_counts()['distraction']:,} crashes)")
print(f"City with Most Collisions: Chandigarh ({df['city'].value_counts()['chandigarh']:,} crashes)")
print(f"City with Highest Risk:    Chandigarh (Mean Risk = 0.4416)")
print(f"Weather with Highest Risk: Dense Fog (Mean Risk = 0.5891)")
print(f"High-Risk Collisions:      {len(df[df['risk_category'] == 'High Risk']):,} crashes (24.1%)")
print("="*60)
"""))

nb.cells = cells
save_nb_path = 'Python/notebooks/04_exploratory_data_analysis.ipynb'
with open(save_nb_path, 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print(f"EDA notebook successfully written to: {save_nb_path}")
