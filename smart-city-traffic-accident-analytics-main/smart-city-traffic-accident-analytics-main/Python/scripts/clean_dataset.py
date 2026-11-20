"""
UrbanFlow: Smart City Traffic & Accident Analytics
Phase 3: Data Cleaning, Preprocessing, and Feature Engineering Script
File: Python/scripts/clean_dataset.py
"""

import pandas as pd
import numpy as np
import os

def clean_dataset(raw_path, output_path):
    print("="*75)
    print("URBANFLOW DATA CLEANING & PREPROCESSING PIPELINE")
    print("="*75)

    # 1. Load raw dataset
    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Raw dataset not found at: {raw_path}")
    
    df = pd.read_csv(raw_path)
    original_rows, original_cols = df.shape
    print(f"1. Loaded Raw Dataset: {original_rows:,} rows x {original_cols} columns")

    # 2. Validate columns
    expected_cols = [
        'accident_id', 'city', 'state', 'latitude', 'longitude', 'date', 'time',
        'hour', 'day_of_week', 'is_weekend', 'road_type', 'lanes', 'traffic_signal',
        'weather', 'visibility', 'temperature', 'traffic_density', 'cause',
        'accident_severity', 'vehicles_involved', 'casualties', 'is_peak_hour',
        'festival', 'risk_score'
    ]
    missing_expected = [c for c in expected_cols if c not in df.columns]
    if missing_expected:
        raise ValueError(f"Missing expected columns in raw data: {missing_expected}")
    print("2. Column Validation: All 24 expected attributes present.")

    # 3. Handle Duplicates
    dup_rows = df.duplicated().sum()
    dup_ids = df['accident_id'].duplicated().sum()
    df = df.drop_duplicates()
    print(f"3. Duplicate Handling: Found {dup_rows} duplicate rows, {dup_ids} duplicate accident_ids.")
    print(f"   Rows retained after deduplication: {len(df):,}")

    # 4. Handle Missing Values
    print("4. Missing Value Analysis:")
    null_summary = df.isnull().sum()
    for col, null_c in null_summary[null_summary > 0].items():
        pct = (null_c / len(df)) * 100
        print(f"   - {col}: {null_c:,} missing ({pct:.3f}%)")
    
    # festival field handling: 99.425% missing
    # Documented decision: Impute nulls with 'None' (representing regular, non-holiday traffic)
    # Exclude from primary statistical models to prevent severe sample bias.
    df['festival'] = df['festival'].fillna('None').astype(str).str.strip()

    # 5. Standardize Text Formatting
    text_columns = ['city', 'state', 'road_type', 'weather', 'visibility', 'traffic_density', 'cause', 'accident_severity']
    for col in text_columns:
        df[col] = df[col].astype(str).str.strip().str.lower()
    print("5. Categorical Standardization: Stripped whitespace and normalized casing to lowercase.")

    # 6. Standardize and Validate Data Types
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df['hour'] = df['hour'].astype(int)
    df['lanes'] = df['lanes'].astype(int)
    df['traffic_signal'] = df['traffic_signal'].astype(int)
    df['temperature'] = df['temperature'].astype(int)
    df['vehicles_involved'] = df['vehicles_involved'].astype(int)
    df['casualties'] = df['casualties'].astype(int)
    df['is_weekend'] = df['is_weekend'].astype(int)
    df['is_peak_hour'] = df['is_peak_hour'].astype(int)
    df['latitude'] = df['latitude'].astype(float)
    df['longitude'] = df['longitude'].astype(float)
    df['risk_score'] = df['risk_score'].astype(float)
    print("6. Data Type Conversion: Dates parsed to datetime64; integers and floats explicitly cast.")

    # 7. Validate Numeric Boundaries (Assertions)
    assert df['latitude'].between(8.0, 37.0).all(), "Invalid latitude coordinates found!"
    assert df['longitude'].between(68.0, 98.0).all(), "Invalid longitude coordinates found!"
    assert df['hour'].between(0, 23).all(), "Hour out of 0-23 range!"
    assert df['lanes'].between(1, 6).all(), "Lanes out of 1-6 range!"
    assert (df['vehicles_involved'] >= 1).all(), "Vehicle count less than 1!"
    assert (df['casualties'] >= 0).all(), "Negative casualties count!"
    assert df['risk_score'].between(0.0, 1.0).all(), "Risk score outside [0, 1]!"
    print("7. Numeric Boundary Validation: All coordinate, hour, vehicle, casualty, and risk ranges verified.")

    # 8. Temporal & Date Feature Engineering
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['month_name'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['week_number'] = df['date'].dt.isocalendar().week.astype(int)

    # 9. Time-of-Day Feature Engineering
    # Defensible ranges:
    # Night: 22:00 - 05:59 (Hours 22, 23, 0, 1, 2, 3, 4, 5) - Low illumination, high speed, fatigue/DUI
    # Morning: 06:00 - 11:59 (Hours 6, 7, 8, 9, 10, 11) - Commuter influx & morning rush
    # Afternoon: 12:00 - 16:59 (Hours 12, 13, 14, 15, 16) - Commercial logistics & school dismissals
    # Evening: 17:00 - 21:59 (Hours 17, 18, 19, 20, 21) - Evening return rush & dusk transition
    def get_time_period(h):
        if h in [22, 23, 0, 1, 2, 3, 4, 5]:
            return 'Night'
        elif h in [6, 7, 8, 9, 10, 11]:
            return 'Morning'
        elif h in [12, 13, 14, 15, 16]:
            return 'Afternoon'
        else:
            return 'Evening'

    df['time_period'] = df['hour'].apply(get_time_period)

    # 10. Severity Score (Ordinal Numeric Mapping)
    # minor -> 1, major -> 2, fatal -> 3
    sev_map = {'minor': 1, 'major': 2, 'fatal': 3}
    df['severity_score'] = df['accident_severity'].map(sev_map)

    # 11. Empirical Risk Category (Distribution-Grounded)
    # Low Risk: < 0.30 (Bottom quartile ~26.4%)
    # Medium Risk: 0.30 to < 0.65 (Middle ~49.6%)
    # High Risk: >= 0.65 (Top quartile ~24.1%)
    def get_risk_category(score):
        if score < 0.30:
            return 'Low Risk'
        elif score < 0.65:
            return 'Medium Risk'
        else:
            return 'High Risk'

    df['risk_category'] = df['risk_score'].apply(get_risk_category)

    # 12. Casualty Category (Distribution-Grounded)
    # 0 Casualties (24.6%), 1-2 Casualties (46.9%), 3-5 Casualties (28.5%)
    def get_casualty_category(c):
        if c == 0:
            return '0 Casualties'
        elif c in [1, 2]:
            return '1-2 Casualties'
        else:
            return '3-5 Casualties'

    df['casualty_category'] = df['casualties'].apply(get_casualty_category)

    # 13. Visibility Score (Ordinal Numeric)
    # low -> 1, medium -> 2, high -> 3
    vis_map = {'low': 1, 'medium': 2, 'high': 3}
    df['visibility_score'] = df['visibility'].map(vis_map)

    # 14. Export Cleaned Dataset
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    
    # 15. Verify Reload
    df_reloaded = pd.read_csv(output_path)
    assert len(df_reloaded) == len(df), "Reloaded row count mismatch!"
    assert df_reloaded.shape[1] == df.shape[1], "Reloaded column count mismatch!"

    print("="*75)
    print("CLEANING PIPELINE EXECUTION SUMMARY")
    print("="*75)
    print(f"Original rows:                {original_rows:,}")
    print(f"Removed duplicates:           {dup_rows}")
    print(f"Rows after duplicate removal: {len(df):,}")
    print(f"Missing-value actions:        festival (19,885 nulls replaced with 'None')")
    print(f"New columns created:          year, month, month_name, day, week_number,")
    print(f"                              time_period, severity_score, risk_category,")
    print(f"                              casualty_category, visibility_score (10 new)")
    print(f"Final rows:                   {df_reloaded.shape[0]:,}")
    print(f"Final columns:                {df_reloaded.shape[1]}")
    print(f"Output file:                  {output_path}")
    print("="*75)
    return df_reloaded

if __name__ == '__main__':
    raw_csv = 'Dataset/raw/indian_roads_dataset.csv'
    clean_csv = 'Dataset/cleaned/urbanflow_cleaned.csv'
    clean_dataset(raw_csv, clean_csv)
