# UrbanFlow — Power BI Complete Manual Build & Reproduction Guide

> **Document Classification**: Technical Implementation & BI Architecture Specification  
> **Target Application**: Microsoft Power BI Desktop (Windows 64-bit)  
> **Source Dataset**: `Dataset/cleaned/urbanflow_cleaned.csv` (20,000 rows × 34 columns)  
> **Deliverable**: Native `UrbanFlow.pbix` (5 interactive pages, Star Schema, 25+ DAX measures)

---

## Executive BI Architecture Overview

Due to Microsoft's proprietary binary container architecture, `.pbix` files require the internal Microsoft Analysis Services (SSAS) VertiPaq tabular database engine (`DataModel` stream) and the Power Query binary formula stream (`DataMashup`). These cannot be compiled by third-party Python scripts headlessly.

This guide provides the **exact, zero-ambiguity instructions** to construct the verified 5-page **UrbanFlow** production dashboard in Microsoft Power BI Desktop in approximately 45–60 minutes.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              STAR SCHEMA MODEL                              │
├────────────────────────────────┬────────────────────────────────────────────┤
│   Dim_Calendar (DAX Table)     │          urbanflow_cleaned (Fact)          │
├────────────────────────────────┼────────────────────────────────────────────┤
│  • Date (PK)                   │  • accident_id (PK)    • weather           │
│  • Year                        │  • date (FK)           • visibility        │
│  • Quarter / QuarterName       │  • time / hour         • traffic_density   │
│  • Month / MonthName           │  • city / state        • cause             │
│  • MonthShort                  │  • latitude / longitude• accident_severity │
│  • DayOfWeek / DayName         │  • road_type / lanes   • casualties        │
│  • IsWeekend                   │  • traffic_signal      • vehicles_involved │
│                                │  • is_peak_hour        • risk_score        │
│                                │  • time_period         • risk_category     │
└────────────────────────────────┴────────────────────────────────────────────┘
                ▲                                       │
                └────────────────( 1 : Many )───────────┘
                       Single Direction Cross-Filter
```

---

## 1. Prerequisites & Source Asset Verification

Ensure the following assets exist in your project root (`C:\Users\thaku\Desktop\Smart City Traffic and Accident Analytics\`):

| Asset | Path | Purpose |
| :--- | :--- | :--- |
| **Cleaned Dataset** | `Dataset/cleaned/urbanflow_cleaned.csv` | Primary analytical fact dataset (20,000 records). |
| **Color Theme JSON** | `PowerBI/urbanflow_theme.json` | Dark/Cyan executive styling palette. |
| **DAX Measures File** | `PowerBI/DAX_Measures.dax` | All 25+ verified business calculation formulas. |
| **Reference Visuals** | `Images/Final/` (`overview_final.png`, etc.) | Visual alignment benchmarks for each page. |

---

## 2. Step-by-Step Data Ingestion & Power Query Setup

### 2.1 Launch & Ingest
1. Open **Microsoft Power BI Desktop**.
2. On the welcome splash screen or Home ribbon, click **Get Data** $\rightarrow$ **Text/CSV**.
3. Select `Dataset/cleaned/urbanflow_cleaned.csv` and click **Open**.
4. In the preview window, verify delimiter is **Comma** and character encoding is **65001: Unicode (UTF-8)**.
5. Click **Transform Data** to open the **Power Query Editor**.

### 2.2 Power Query Transformation & Typing (Advanced Editor)
In the Power Query Editor:
1. Select the `urbanflow_cleaned` query on the left.
2. Click **Home $\rightarrow$ Advanced Editor**.
3. Replace the entire contents with the following production Power Query M code:

```powerquery
let
    Source = Csv.Document(File.Contents("C:\Users\thaku\Desktop\Smart City Traffic and Accident Analytics\Dataset\cleaned\urbanflow_cleaned.csv"),[Delimiter=",", Columns=34, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{
        {"accident_id", Int64.Type},
        {"city", type text},
        {"state", type text},
        {"latitude", type number},
        {"longitude", type number},
        {"date", type date},
        {"time", type time},
        {"hour", Int64.Type},
        {"day_of_week", type text},
        {"is_weekend", Int64.Type},
        {"road_type", type text},
        {"lanes", Int64.Type},
        {"traffic_signal", Int64.Type},
        {"weather", type text},
        {"visibility", type text},
        {"temperature", Int64.Type},
        {"traffic_density", type text},
        {"cause", type text},
        {"accident_severity", type text},
        {"vehicles_involved", Int64.Type},
        {"casualties", Int64.Type},
        {"is_peak_hour", Int64.Type},
        {"festival", type text},
        {"risk_score", type number},
        {"year", Int64.Type},
        {"month", Int64.Type},
        {"month_name", type text},
        {"day", Int64.Type},
        {"week_number", Int64.Type},
        {"time_period", type text},
        {"severity_score", Int64.Type},
        {"risk_category", type text},
        {"casualty_category", type text},
        {"visibility_score", Int64.Type}
    }),
    #"Cleaned Festival" = Table.ReplaceValue(#"Changed Type", "", "None", Replacer.ReplaceValue, {"festival"}),
    #"Proper City" = Table.TransformColumns(#"Cleaned Festival", {{"city", Text.Proper, type text}}),
    #"Proper Weather" = Table.TransformColumns(#"Proper City", {{"weather", Text.Proper, type text}}),
    #"Proper Road" = Table.TransformColumns(#"Proper Weather", {{"road_type", Text.Proper, type text}}),
    #"Proper Cause" = Table.TransformColumns(#"Proper Road", {{"cause", Text.Proper, type text}}),
    #"Proper Severity" = Table.TransformColumns(#"Proper Cause", {{"accident_severity", Text.Proper, type text}})
in
    #"Proper Severity"
```

4. Click **Done**.
5. Click **Home $\rightarrow$ Close & Apply** in the top-left corner. Wait for the 20,000 rows to load.

---

## 3. Data Modeling & Date Dimension Table

### 3.1 Create Dim_Calendar Table
In Power BI Desktop:
1. Navigate to the **Table View** (left navigation bar, second icon).
2. On the ribbon, click **Modeling $\rightarrow$ New Table**.
3. Enter the following DAX formula:

```dax
Dim_Calendar = 
VAR MinYear = YEAR(MIN('urbanflow_cleaned'[date]))
VAR MaxYear = YEAR(MAX('urbanflow_cleaned'[date]))
RETURN
ADDCOLUMNS(
    CALENDAR(DATE(MinYear, 1, 1), DATE(MaxYear, 12, 31)),
    "Year", YEAR([Date]),
    "QuarterNumber", QUARTER([Date]),
    "Quarter", "Q" & QUARTER([Date]),
    "MonthNumber", MONTH([Date]),
    "MonthName", FORMAT([Date], "MMMM"),
    "MonthShort", FORMAT([Date], "MMM"),
    "DayOfWeekNumber", WEEKDAY([Date], 2), -- Monday = 1
    "DayOfWeekName", FORMAT([Date], "dddd"),
    "DayOfWeekShort", FORMAT([Date], "ddd"),
    "YearMonth", FORMAT([Date], "YYYY-MM"),
    "YearMonthSort", YEAR([Date]) * 100 + MONTH([Date]),
    "IsWeekend", IF(WEEKDAY([Date], 2) >= 6, "Weekend", "Weekday")
)
```

4. **Sort By Column configuration**:
   * Select `MonthShort` $\rightarrow$ Ribbon: **Column tools $\rightarrow$ Sort by Column $\rightarrow$ MonthNumber**.
   * Select `MonthName` $\rightarrow$ Ribbon: **Column tools $\rightarrow$ Sort by Column $\rightarrow$ MonthNumber**.
   * Select `DayOfWeekShort` $\rightarrow$ Ribbon: **Column tools $\rightarrow$ Sort by Column $\rightarrow$ DayOfWeekNumber**.
   * Select `YearMonth` $\rightarrow$ Ribbon: **Column tools $\rightarrow$ Sort by Column $\rightarrow$ YearMonthSort**.
5. Mark as Date Table: Right-click `Dim_Calendar` in the Data pane $\rightarrow$ **Mark as date table** $\rightarrow$ select `Date` column $\rightarrow$ Click **OK**.

### 3.2 Establish Model Relationships
1. Switch to **Model View** (left navigation bar, third icon).
2. Drag `Dim_Calendar[Date]` onto `urbanflow_cleaned[date]`.
3. Double-click the relationship line to verify properties:
   * **Cardinality**: One to many (`1:*`)
   * **Cross filter direction**: Single
   * **Make this relationship active**: Checked $\checkmark$

---

## 4. Import the Theme & DAX Measures Setup

### 4.1 Apply UrbanFlow Dark Theme
1. Navigate to **View $\rightarrow$ Themes dropdown $\rightarrow$ Browse for themes**.
2. Select `C:\Users\thaku\Desktop\Smart City Traffic and Accident Analytics\PowerBI\urbanflow_theme.json`.
3. Verify notification: *"Theme imported successfully"*.

### 4.2 Create Dedicated Measures Table
1. On the **Home** ribbon, click **Enter Data**.
2. Name the table `_Key_Measures`, rename `Column1` to `Placeholder`, and click **Load**.
3. Now create each measure below inside `_Key_Measures` (Home $\rightarrow$ **New Measure**).
*(Once your first measure is created, right-click `Placeholder` and select **Delete from model**).*

### 4.3 Complete Certified DAX Formula Catalog

```dax
// ==============================================================================
// 1. VOLUME & CORE METRICS
// ==============================================================================

Total Accidents = COUNTROWS('urbanflow_cleaned')

Total Casualties = SUM('urbanflow_cleaned'[casualties])

Total Vehicles = SUM('urbanflow_cleaned'[vehicles_involved])

Average Casualties Per Incident = DIVIDE([Total Casualties], [Total Accidents], 0)

Average Vehicles Per Incident = DIVIDE([Total Vehicles], [Total Accidents], 0)

Average Risk Score = AVERAGE('urbanflow_cleaned'[risk_score])

Median Risk Score = MEDIAN('urbanflow_cleaned'[risk_score])

// ==============================================================================
// 2. SEVERITY BREAKDOWNS
// ==============================================================================

Fatal Accidents = 
CALCULATE([Total Accidents], 'urbanflow_cleaned'[accident_severity] = "Fatal")

Major Accidents = 
CALCULATE([Total Accidents], 'urbanflow_cleaned'[accident_severity] = "Major")

Minor Accidents = 
CALCULATE([Total Accidents], 'urbanflow_cleaned'[accident_severity] = "Minor")

Fatal Accident Rate % = 
DIVIDE([Fatal Accidents], [Total Accidents], 0) * 100

Major Accident Rate % = 
DIVIDE([Major Accidents], [Total Accidents], 0) * 100

Minor Accident Rate % = 
DIVIDE([Minor Accidents], [Total Accidents], 0) * 100

// ==============================================================================
// 3. RISK CATEGORY TIERS
// ==============================================================================

High Risk Accidents = 
CALCULATE([Total Accidents], 'urbanflow_cleaned'[risk_category] = "High Risk")

Medium Risk Accidents = 
CALCULATE([Total Accidents], 'urbanflow_cleaned'[risk_category] = "Medium Risk")

Low Risk Accidents = 
CALCULATE([Total Accidents], 'urbanflow_cleaned'[risk_category] = "Low Risk")

High Risk Rate % = 
DIVIDE([High Risk Accidents], [Total Accidents], 0) * 100

// ==============================================================================
// 4. OPERATIONAL & TEMPORAL CONTEXT
// ==============================================================================

Peak Hour Accidents = 
CALCULATE([Total Accidents], 'urbanflow_cleaned'[is_peak_hour] = 1)

Peak Hour Accident % = 
DIVIDE([Peak Hour Accidents], [Total Accidents], 0) * 100

Nighttime Accidents = 
CALCULATE([Total Accidents], 'urbanflow_cleaned'[time_period] = "Night")

Nighttime Accident % = 
DIVIDE([Nighttime Accidents], [Total Accidents], 0) * 100

Weekend Accidents = 
CALCULATE([Total Accidents], 'urbanflow_cleaned'[is_weekend] = 1)

Weekend Accident % = 
DIVIDE([Weekend Accidents], [Total Accidents], 0) * 100

Signal Controlled Accidents = 
CALCULATE([Total Accidents], 'urbanflow_cleaned'[traffic_signal] = 1)

Adverse Weather Accidents = 
CALCULATE([Total Accidents], 'urbanflow_cleaned'[weather] IN {"Rain", "Fog"})
```

---

## 5. Page-by-Page Visual Construction Guide

### Global Canvas Settings (Apply to All Pages)
* **Canvas Size**: 16:9 widescreen (1280 × 720 px or 1920 × 1080 px).
* **Canvas Background**: Color `#0B132B`, Transparency `0%`.
* **Header Banner (Top 65px)**:
  * Text box: **URBANFLOW** (`#38BDF8`, Segoe UI Bold, 16pt) | *Smart City Traffic & Accident Analytics* (`#9CA3AF`, 10pt).
  * Right side: Slicer dropdown for `Dim_Calendar[Year]` and `urbanflow_cleaned[city]`.

---

### PAGE 1: Executive KPI & Safety Overview
*Target Reference: `Images/Final/overview_final.png`*

1. **Top KPI Cards (4 Cards across X: 30 to 1250, Y: 80, H: 90)**:
   * **Card 1**: `[Total Accidents]` $\rightarrow$ Callout value: 20,000. Label: "Total Collisions".
   * **Card 2**: `[Total Casualties]` $\rightarrow$ Callout value: 34,519. Label: "Total Casualties".
   * **Card 3**: `[Fatal Accident Rate %]` $\rightarrow$ Callout value: 13.91%. Format: `0.0%`. Label: "Fatality Rate". Accent: `#EF4444`.
   * **Card 4**: `[Average Risk Score]` $\rightarrow$ Callout value: 0.438. Format: `0.000`. Label: "Mean Risk Index". Accent: `#38BDF8`.

2. **Visual 1 (Top-Left, Y: 190, W: 580, H: 240) — Donut Chart**:
   * **Title**: "Accident Distribution by Severity"
   * **Legend**: `urbanflow_cleaned[accident_severity]` (Minor, Major, Fatal)
   * **Values**: `[Total Accidents]`
   * **Colors**: Minor = `#10B981`, Major = `#F59E0B`, Fatal = `#EF4444`.

3. **Visual 2 (Top-Right, Y: 190, W: 580, H: 240) — Clustered Column Chart**:
   * **Title**: "Collision Volume & Mean Risk by City"
   * **X-Axis**: `urbanflow_cleaned[city]`
   * **Y-Axis**: `[Total Accidents]`
   * **Line Y-Axis**: `[Average Risk Score]`

4. **Visual 3 (Bottom-Left, Y: 450, W: 580, H: 240) — Horizontal Bar Chart**:
   * **Title**: "Risk Category Classification Tiers"
   * **Y-Axis**: `urbanflow_cleaned[risk_category]` (Low Risk, Medium Risk, High Risk)
   * **X-Axis**: `[Total Accidents]`
   * **Data labels**: On (display counts and percentages).

5. **Visual 4 (Bottom-Right, Y: 450, W: 580, H: 240) — Area / Line Chart**:
   * **Title**: "Monthly Incident Volume Trend (Seasonal Patterns)"
   * **X-Axis**: `Dim_Calendar[MonthShort]` (Sorted by `MonthNumber`)
   * **Y-Axis**: `[Total Accidents]`
   * **Legend**: `Dim_Calendar[Year]`

---

### PAGE 2: Traffic Dynamics & Temporal Analysis
*Target Reference: `Images/Final/traffic_time_final.png`*

1. **Top KPI Cards**:
   * **Card 1**: `[Peak Hour Accidents]` (4,948 incidents | 24.74%)
   * **Card 2**: `[Nighttime Accidents]` (6,721 incidents | 33.61%)
   * **Card 3**: `[Weekend Accidents]` (5,714 incidents | 28.57%)
   * **Card 4**: Peak Hour Avg Risk: `0.604` vs. Off-Peak: `0.383` (+57.7% Risk Disparity).

2. **Visual 1 (Full Width, Y: 190, W: 1180, H: 250) — Combo Clustered Column & Line Chart**:
   * **Title**: "24-Hour Diurnal Accident Distribution vs. Average Risk Score"
   * **X-Axis**: `urbanflow_cleaned[hour]` (0 to 23)
   * **Column Y-Axis**: `[Total Accidents]` (Highlights peak hours 8–10 AM and 5–8 PM)
   * **Line Y-Axis**: `[Average Risk Score]` (Demonstrates risk peaking during rush hours)

3. **Visual 2 (Bottom-Left, Y: 460, W: 380, H: 230) — 100% Stacked Bar Chart**:
   * **Title**: "Commuter Rush vs. Off-Peak Risk Tier Proportion"
   * **Y-Axis**: `urbanflow_cleaned[is_peak_hour]` (0 = Off-Peak, 1 = Peak Hour)
   * **X-Axis**: `[Total Accidents]`
   * **Legend**: `urbanflow_cleaned[risk_category]`

4. **Visual 3 (Bottom-Center, Y: 460, W: 380, H: 230) — Clustered Column Chart**:
   * **Title**: "Day-of-Week Collision Volume"
   * **X-Axis**: `Dim_Calendar[DayOfWeekShort]` (Mon through Sun)
   * **Y-Axis**: `[Total Accidents]`

5. **Visual 4 (Bottom-Right, Y: 460, W: 380, H: 230) — Matrix Heatmap**:
   * **Rows**: `urbanflow_cleaned[time_period]` (Morning Rush, Midday, Evening Rush, Night)
   * **Columns**: `urbanflow_cleaned[day_of_week]`
   * **Values**: `[Average Risk Score]` (Conditional background formatting enabled).

---

### PAGE 3: Accident Analysis & Root Cause Attribution
*Target Reference: `Images/Final/accident_analysis_final.png`*

1. **Visual 1 (Top-Left, W: 580, H: 250) — Horizontal Bar Chart**:
   * **Title**: "Primary Root Cause Breakdown & Fatality Rate"
   * **Y-Axis**: `urbanflow_cleaned[cause]` (Overspeeding, Distraction, Poor Road, Weather, Drunk Driving)
   * **X-Axis**: `[Total Accidents]`
   * **Tooltips**: `[Fatal Accident Rate %]`, `[Total Casualties]`

2. **Visual 2 (Top-Right, W: 580, H: 250) — Grouped Column Chart**:
   * **Title**: "Atmospheric Conditions vs. Mean Collision Risk"
   * **X-Axis**: `urbanflow_cleaned[weather]` (Clear, Rain, Fog)
   * **Y-Axis**: `[Average Risk Score]` (Fog = 0.589, Rain = 0.487, Clear = 0.237)
   * **Legend**: `urbanflow_cleaned[traffic_density]` (Low, Medium, High)

3. **Visual 3 (Bottom-Left, W: 580, H: 250) — Scatter Plot**:
   * **Title**: "Visibility Score vs. Collision Risk Correlation"
   * **X-Axis**: `urbanflow_cleaned[visibility_score]`
   * **Y-Axis**: `[Average Risk Score]`
   * **Size**: `[Total Casualties]`
   * **Color**: `urbanflow_cleaned[weather]`
   * **Trendline**: Enabled (Displays negative slope $r = -0.729$).

4. **Visual 4 (Bottom-Right, W: 580, H: 250) — Clustered Bar Chart**:
   * **Title**: "Road Type & Lane Geometry Invariance"
   * **Y-Axis**: `urbanflow_cleaned[road_type]` (Highway, Urban, Rural)
   * **X-Axis**: `[Total Accidents]`
   * **Legend**: `urbanflow_cleaned[lanes]` (1, 2, 4, 6 lanes)

---

### PAGE 4: Geographic Hotspots & Spatial Distribution
*Target Reference: `Images/Final/hotspots_map_final.png`*

1. **Map Configuration Settings**:
   * Go to **File $\rightarrow$ Options and Settings $\rightarrow$ Options $\rightarrow$ Security $\rightarrow$ Check "Use Map and Filled Map visuals"**.
2. **Visual 1 (Left Half, W: 680, H: 520) — Power BI Map / Azure Map Visual**:
   * **Latitude**: `urbanflow_cleaned[latitude]` (Set summarization to **Don't summarize**)
   * **Longitude**: `urbanflow_cleaned[longitude]` (Set summarization to **Don't summarize**)
   * **Size**: `urbanflow_cleaned[casualties]`
   * **Color / Legend**: `urbanflow_cleaned[risk_category]`
   * **Map Style**: Dark Mode or Grayscale.
   * **Tooltips**: `city`, `weather`, `cause`, `risk_score`, `accident_severity`.

3. **Visual 2 (Top-Right, W: 480, H: 250) — Ranked Bar Chart**:
   * **Title**: "Top Metro Clusters by Incident Volume"
   * **Y-Axis**: `urbanflow_cleaned[city]`
   * **X-Axis**: `[Total Accidents]`
   * **Data labels**: On (Values range ~2,400 to ~2,600 per city).

4. **Visual 3 (Bottom-Right, W: 480, H: 250) — Matrix Table**:
   * **Rows**: `urbanflow_cleaned[city]`
   * **Columns**: `urbanflow_cleaned[accident_severity]`
   * **Values**: `[Total Accidents]`, `[Fatal Accident Rate %]`, `[Average Risk Score]`
   * **Total**: Enabled.

---

### PAGE 5: Advanced Risk Analysis & Predictive Intelligence
*Target Reference: `Images/Final/risk_insights_final.png`*

1. **Visual 1 (Top-Left, W: 580, H: 250) — Histogram / Column Chart**:
   * **Title**: "Continuous Risk Score Density Distribution"
   * **X-Axis**: `urbanflow_cleaned[risk_score]` (Binned at 0.05 increments)
   * **Y-Axis**: `[Total Accidents]`
   * **Reference Line**: Constant line at Mean = `0.438` (Dashed Cyan).

2. **Visual 2 (Top-Right, W: 580, H: 250) — Heatmap Matrix**:
   * **Title**: "Multi-Factor Collision Risk Matrix (Weather × Traffic Density)"
   * **Rows**: `urbanflow_cleaned[weather]` (Clear, Rain, Fog)
   * **Columns**: `urbanflow_cleaned[traffic_density]` (Low, Medium, High)
   * **Values**: `[Average Risk Score]`
   * **Conditional Formatting**: Background Color $\rightarrow$ Gradient from Green (`#10B981` at 0.20) to Amber (`#F59E0B` at 0.45) to Red (`#EF4444` at 0.75).

3. **Visual 3 (Bottom-Left, W: 580, H: 250) — Horizontal Bar Chart**:
   * **Title**: "High-Risk Incident Rate by Atmospheric & Traffic Segment"
   * **Y-Axis**: Composite category or `weather`
   * **X-Axis**: `[High Risk Rate %]` (Demonstrates Fog + High Density exceeding 75% High Risk).

4. **Visual 4 (Bottom-Right, W: 580, H: 250) — Key Influencers Visual**:
   * **Analyze**: `urbanflow_cleaned[risk_category]`
   * **Explain By**: `weather`, `traffic_density`, `visibility_score`, `hour`, `road_type`.
   * **Insight Highlighted**: Low Visibility & Fog increase likelihood of High Risk by over $4.2\times$.

---

## 6. Slicers, Cross-Filtering & Interactivity

### 6.1 Sync Slicers Configuration
Create the following slicers on **Page 1**, then configure them to synchronize across all 5 pages:
1. **Year Slicer**: Dropdown or Tile $\rightarrow$ `Dim_Calendar[Year]`.
2. **City Slicer**: Dropdown $\rightarrow$ `urbanflow_cleaned[city]`.
3. **Severity Slicer**: Horizontal Buttons/Tiles $\rightarrow$ `urbanflow_cleaned[accident_severity]`.
4. **Risk Tier Slicer**: Horizontal Buttons/Tiles $\rightarrow$ `urbanflow_cleaned[risk_category]`.

To synchronize:
* Select slicer $\rightarrow$ **View $\rightarrow$ Sync slicers pane**.
* Under **Sync**, check all 5 pages $\checkmark$.
* Under **Visible**, check the pages where you want the slicer widget displayed.

### 6.2 Edit Interactions
To prevent charts from cross-highlighting instead of cross-filtering:
1. Select the City Slicer $\rightarrow$ Ribbon: **Format $\rightarrow$ Edit interactions**.
2. For each visual on the canvas, select the **Filter** icon (funnel) instead of the **Highlight** icon (pie).

### 6.3 Custom Tooltip Page (Optional Enhancement)
1. Add a new page $\rightarrow$ Name it `Tooltip_CityDetails`.
2. In **Format Page $\rightarrow$ Page Information $\rightarrow$ Allow use as tooltip = On**.
3. Canvas settings: Type = **Tooltip** (320 × 240 px).
4. Add a Card with `[Fatal Accident Rate %]` and a small Bar Chart of `[Total Accidents]` by `weather`.
5. On Page 4 Map visual: **Format visual $\rightarrow$ Tooltips $\rightarrow$ Type: Report page $\rightarrow$ Page: `Tooltip_CityDetails`**.

---

## 7. Quality Verification & Numerical Parity Checklist

Before saving the final file, cross-check the displayed numbers on your canvas against the ground truth dataset:

- [ ] **Total Incidents**: Must display exactly **20,000**.
- [ ] **Total Casualties**: Must display exactly **34,519**.
- [ ] **Fatal Collisions**: Exactly **2,782** (13.91%).
- [ ] **Major Collisions**: Exactly **9,997** (49.98%).
- [ ] **Minor Collisions**: Exactly **7,221** (36.10%).
- [ ] **Mean Risk Score**: Exactly **0.4376** (rounded to 0.438).
- [ ] **Median Risk Score**: Exactly **0.4500**.
- [ ] **Fog Average Risk Score**: Exactly **0.5891** (vs. Clear: **0.2369**).
- [ ] **Peak Hour Collisions**: Exactly **4,948** (24.74%).
- [ ] **Nighttime Collisions**: Exactly **6,721** (33.61%).

---

## 8. Final File Export & Commit

1. Click **File $\rightarrow$ Save As**.
2. Path: `C:\Users\thaku\Desktop\Smart City Traffic and Accident Analytics\PowerBI\UrbanFlow.pbix`.
3. Overwrite the non-functional placeholder file.
4. Verify file size in Windows Explorer: The resulting genuine `.pbix` will be approximately **350 KB to 1.5 MB** (containing the compiled VertiPaq database).
