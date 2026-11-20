# UrbanFlow: Smart City Traffic & Accident Analytics — Dashboard User Guide
**Audience**: Municipal Commissioners, Traffic Police Leaders, Urban Planners, and University Evaluators  
**Report Package**: `PowerBI/UrbanFlow.pbix`  
**Author**: UrbanFlow Traffic Safety Analytics Team  
**Date**: September 2026  

---

## 1. Getting Started: How to Open the Dashboard
1. Ensure **Microsoft Power BI Desktop** is installed on your computer.
2. Navigate to your project folder:  
   `c:\Users\thaku\Desktop\🚦 Smart City Traffic\PowerBI\`
3. Double-click **`UrbanFlow.pbix`**.
4. Once the report loads, you will see the **Overview** page on a modern dark smart-city canvas.

---

## 2. Navigating Between Report Pages
At the very top of each page, you will find five clickable navigation buttons:
* **[ Overview ]**: Executive summary showing high-level KPIs, monthly volume trends, and city totals.
* **[ Traffic & Time ]**: Hourly diurnal cycles, weekday vs. weekend ratios, and day-hour heatmap matrix.
* **[ Accident Analysis ]**: Root cause Pareto chart, weather impacts, and road infrastructure breakdowns.
* **[ Hotspots & Map ]**: Interactive geospatial collision map and city/corridor danger rankings.
* **[ Risk & Insights ]**: Target risk gauge, predictive factors, and municipal policy recommendations.

Simply click any button to switch pages instantly.

---

## 3. How to Use Slicers & Filters
At the top-right of each report page, you will find interactive dropdown slicers:
* **City Slicer**: Click to filter the entire dashboard to a specific metropolitan area (e.g., *Delhi, Mumbai, Bengaluru*).
* **Year Slicer**: Select *2022, 2023, 2024*, or *2025* to view temporal changes.
* **Accident Severity**: Click *Minor, Major*, or *Fatal* to isolate specific collision outcomes.
* **Weather Slicer**: Filter by *Clear, Rain*, or *Fog* to observe environmental impacts.

### How to Select Multiple Items:
* Hold the **Ctrl** key on your keyboard while clicking items to select multiple cities or years.

---

## 4. Understanding the Color System (Risk Semantics)
Throughout all pages, charts, and maps, colors always follow a strict traffic-safety meaning:
* 🟢 **Green (Low Risk)**: Composite risk score below **0.30**. Represents safe, baseline operating conditions (typically clear daylight with low traffic density).
* 🟡 **Amber / Orange (Medium Risk)**: Composite risk score between **0.30 and 0.65**. Represents elevated operational friction (moderate traffic congestion, evening rush).
* 🔴 **Red (High Risk / Danger)**: Composite risk score **0.65 or above**, or fatal collisions. Indicates critical collision hazard (dense fog, multi-vehicle pileups, high speed).

---

## 5. How to Inspect the Interactive Map (Page 4)
* **Hover (Tooltip)**: Hover your mouse over any circular bubble on the map to view a summary tooltip displaying City, Road Type, Casualties, and Average Risk.
* **Bubble Size**: Larger circles represent collisions that caused a higher number of injuries or fatalities.
* **Bubble Color**: Circles are color-coded Green, Amber, or Red according to their Risk Category.
* **Zoom & Pan**: Use your mouse scroll wheel to zoom in on specific urban clusters, and click-and-drag to pan across India.

---

## 6. How to Use Drill-Through (Location Deep-Dive)
* On the **Hotspots & Map** page, right-click on any city name in the bar chart or table.
* Select **Drill-through** $\rightarrow$ **Location Details**.
* Power BI will take you to a dedicated deep-dive view filtered exclusively to that city, showing its hourly crash distribution, leading causes, and specific high-risk corridors.

---

## 7. How to Reset All Filters to Default
If you have applied multiple filters and want to return to the original full-dataset view:
* Look at the top-right header for the **[ Reset Filters ]** button (or click the bookmark reset icon).
* Alternatively, click the small eraser icon on the top-right corner of each slicer box.
* The dashboard will immediately reset to display all 20,000 incident records.

---

## 8. Interpreting Executive KPIs
* **Total Accidents (20,000)**: Total number of verified collision events recorded.
* **Total Casualties (34,529)**: Cumulative count of individuals injured or killed (averaging 1.73 per collision).
* **Average Risk Score (0.438)**: Overall hazard score on a 0.10 to 1.00 scale.
* **Fatal Incident Rate (14.9%)**: Percentage of collisions that resulted in at least one fatality.
* **Peak Hour Accident % (24.7%)**: Share of collisions that occurred during morning (8–10 AM) or evening (5–7 PM) rush hours.
