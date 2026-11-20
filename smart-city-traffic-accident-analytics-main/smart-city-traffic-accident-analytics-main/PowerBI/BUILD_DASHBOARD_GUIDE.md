# UrbanFlow Power BI Dashboard — Step-by-Step Build Guide

> **Why this guide exists**: The `.pbix` file in this folder (`UrbanFlow.pbix`) is a structural placeholder created during project setup. Power BI Desktop does not expose a public API for programmatic dashboard construction. This guide walks you through building the real interactive dashboard in under 60 minutes, using the exact DAX measures, data model, and visual specifications from the UrbanFlow project.

---

## Prerequisites

| Requirement | Version | Notes |
|---|---|---|
| Power BI Desktop | Latest (free) | [Download here](https://www.microsoft.com/en-us/download/details.aspx?id=58494) |
| Cleaned dataset | `Dataset/cleaned/urbanflow_cleaned.csv` | Must exist — produced in Phase 3 |
| Theme file | `PowerBI/urbanflow_theme.json` | Applies UrbanFlow color palette |
| DAX measures | `PowerBI/DAX_Measures.dax` | Copy-paste ready |

---

## Step 1 — Import the Dataset

1. Open **Power BI Desktop** → **Get Data → Text/CSV**
2. Navigate to `Dataset/cleaned/urbanflow_cleaned.csv`
3. Click **Load** (do NOT use "Transform Data" yet)

---

## Step 2 — Apply Data Types

Go to **Home → Transform Data** (Power Query editor):

| Column | Set Type To |
|---|---|
| `accident_id` | Text |
| `date` | Date |
| `time` | Time |
| `latitude` | Decimal Number |
| `longitude` | Decimal Number |
| `casualties` | Whole Number |
| `vehicles_involved` | Whole Number |
| `risk_score` | Decimal Number |
| `visibility_score` | Decimal Number |
| `hour` | Whole Number |
| `is_peak_hour` | Whole Number |
| `is_night` | Whole Number |
| `accident_month` | Whole Number |
| `accident_day_of_week` | Whole Number |
| `risk_category` | Text |
| All other text columns | Text |

Click **Close & Apply**.

---

## Step 3 — Apply the Theme

1. Go to **View → Themes → Browse for themes**
2. Select `PowerBI/urbanflow_theme.json`
3. Click **Import theme**

---

## Step 4 — Create the Date Table

In the **Model** view, click **New table** and paste:

```dax
DateTable = 
ADDCOLUMNS(
    CALENDAR(DATE(2020,1,1), DATE(2024,12,31)),
    "Year", YEAR([Date]),
    "Month", MONTH([Date]),
    "MonthName", FORMAT([Date], "MMM"),
    "Quarter", QUARTER([Date]),
    "QuarterName", "Q" & QUARTER([Date]),
    "DayOfWeek", WEEKDAY([Date], 2),
    "DayName", FORMAT([Date], "ddd"),
    "WeekNumber", WEEKNUM([Date]),
    "YearMonth", FORMAT([Date], "YYYY-MM")
)
```

Then mark it as a Date Table:  
**Right-click DateTable → Mark as date table → Date column = Date**

Create a relationship:  
`urbanflow_cleaned[date]` → `DateTable[Date]` (Many-to-One)

---

## Step 5 — Add All DAX Measures

Open `PowerBI/DAX_Measures.dax` in any text editor.

In Power BI Desktop:
1. Click **Home → New measure** (or right-click the table)
2. Copy-paste each measure from `DAX_Measures.dax`

The key measures to add (also in the `.dax` file):

```dax
Total Accidents = COUNTROWS(urbanflow_cleaned)

Total Casualties = SUM(urbanflow_cleaned[casualties])

Avg Risk Score = AVERAGE(urbanflow_cleaned[risk_score])

Fatal Accidents = COUNTROWS(FILTER(urbanflow_cleaned, urbanflow_cleaned[severity] = "Fatal"))

Fatal Rate % = DIVIDE([Fatal Accidents], [Total Accidents]) * 100

High Risk Count = COUNTROWS(FILTER(urbanflow_cleaned, urbanflow_cleaned[risk_category] = "High"))

High Risk Rate % = DIVIDE([High Risk Count], [Total Accidents]) * 100

Avg Casualties Per Accident = DIVIDE([Total Casualties], [Total Accidents])

Peak Hour Accidents = COUNTROWS(FILTER(urbanflow_cleaned, urbanflow_cleaned[is_peak_hour] = 1))

Night Accidents = COUNTROWS(FILTER(urbanflow_cleaned, urbanflow_cleaned[is_night] = 1))

Fog Accidents = COUNTROWS(FILTER(urbanflow_cleaned, urbanflow_cleaned[weather_condition] = "Fog"))
```

---

## Step 6 — Build the 5 Report Pages

### Page 1: Executive Overview

| Visual | Type | Fields |
|---|---|---|
| Total Accidents | KPI Card | `[Total Accidents]` |
| Total Casualties | KPI Card | `[Total Casualties]` |
| Fatal Rate | KPI Card | `[Fatal Rate %]` |
| Avg Risk Score | KPI Card | `[Avg Risk Score]` |
| Accidents by Severity | Donut Chart | severity (Legend), Total Accidents (Values) |
| Accidents by Risk Category | Bar Chart | risk_category (Y), Total Accidents (X) |
| Monthly Trend | Line Chart | DateTable[MonthName] (X), Total Accidents (Y) |

### Page 2: Traffic & Time Analysis

| Visual | Type | Fields |
|---|---|---|
| Hourly Accidents | Column Chart | hour (X), Total Accidents (Y) |
| Peak vs Off-Peak | Stacked Bar | is_peak_hour (Legend), Total Accidents |
| Day of Week | Bar Chart | accident_day_of_week (X), Total Accidents (Y) |
| Night vs Day | Donut | is_night (Legend), Total Accidents |

### Page 3: Accident Analysis

| Visual | Type | Fields |
|---|---|---|
| Accidents by Weather | Bar Chart | weather_condition (Y), Total Accidents (X) |
| Accidents by Road Type | Bar Chart | road_type (Y), Total Accidents (X) |
| Casualties by Cause | Bar Chart | accident_cause (Y), Total Casualties (X) |
| Vehicles Involved | Histogram | vehicles_involved |
| Visibility vs Risk | Scatter | visibility_score (X), risk_score (Y) |

### Page 4: Geographic Hotspots

| Visual | Type | Fields |
|---|---|---|
| Accident Map | Map or ArcGIS | latitude (Lat), longitude (Long), Total Accidents (Size) |
| Accidents by City | Bar Chart | city (Y), Total Accidents (X), top 10 |
| Accidents by State | Filled Map | state (Location), Total Accidents (Color) |

### Page 5: Risk Insights

| Visual | Type | Fields |
|---|---|---|
| Risk Score Distribution | Histogram | risk_score |
| Risk by Weather | Grouped Bar | weather_condition (X), Avg Risk Score (Y) |
| Risk by Time | Line | hour (X), Avg Risk Score (Y) |
| Risk Category Breakdown | Donut | risk_category (Legend), Total Accidents |
| High Risk Rate by Road Type | Bar | road_type (Y), High Risk Rate % (X) |

---

## Step 7 — Add Slicers (All Pages)

Add these slicers to every page:

- `DateTable[Year]` — Year selector
- `weather_condition` — Weather filter
- `city` — City filter
- `severity` — Severity filter
- `risk_category` — Risk category filter

Set all slicers to **sync across pages**: **View → Sync Slicers → select all pages**

---

## Step 8 — Add Titles and Branding

On each page:
1. Insert → Text Box → Type the page title
2. Set font: Segoe UI, 18pt, Bold, color `#1A3A5C` (UrbanFlow dark blue)
3. Insert → Image → `Images/Architecture/urbanflow_system_architecture.png` on the cover page

---

## Step 9 — Save the File

**File → Save As → `PowerBI/UrbanFlow.pbix`**

This overwrites the placeholder with the real dashboard file.

---

## Step 10 — Export Screenshots

After building, take screenshots of each page for `Images/Final/`:

1. Right-click each page tab → Export → PNG  
   *Or* use Snipping Tool / Win + Shift + S  
2. Save as:
   - `Images/Final/overview_final.png`
   - `Images/Final/traffic_time_final.png`
   - `Images/Final/accident_analysis_final.png`
   - `Images/Final/hotspots_map_final.png`
   - `Images/Final/risk_insights_final.png`

---

## Step 11 — Repackage Submission

After saving the real `.pbix` and new screenshots, run:

```powershell
cd "C:\Users\thaku\Desktop\Smart City Traffic and Accident Analytics"
python Python/scripts/package_submission.py
```

This will rebuild `UrbanFlow_Final_Submission.zip` with the real Power BI file.

---

## Estimated Time

| Task | Time |
|---|---|
| Import + data types | 10 min |
| Date table + relationships | 5 min |
| DAX measures | 10 min |
| Page 1 (Overview) | 10 min |
| Pages 2–5 | 20 min |
| Slicers + sync | 5 min |
| Save + export | 5 min |
| **Total** | **~65 minutes** |

---

## Reference Files

- [`DAX_Measures.dax`](DAX_Measures.dax) — All pre-written DAX measures
- [`PowerQuery_Transformations.m`](PowerQuery_Transformations.m) — Power Query M code
- [`urbanflow_theme.json`](urbanflow_theme.json) — Color theme
- [`PowerBI_Dashboard_Guide.md`](PowerBI_Dashboard_Guide.md) — Original dashboard guide from Phase 5
