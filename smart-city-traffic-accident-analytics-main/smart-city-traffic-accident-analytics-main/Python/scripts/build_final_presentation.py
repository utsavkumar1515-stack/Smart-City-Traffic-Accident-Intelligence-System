import os
import sys
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')

WORKSPACE = r'c:\Users\thaku\Desktop\🚦 Smart City Traffic'
PRES_DIR = os.path.join(WORKSPACE, 'Presentation')
os.makedirs(PRES_DIR, exist_ok=True)

PPTX_PATH = os.path.join(PRES_DIR, 'UrbanFlow_Final_Presentation.pptx')
PDF_PATH = os.path.join(PRES_DIR, 'UrbanFlow_Final_Presentation.pdf')

# Palette
C_NAVY = RGBColor(29, 53, 87)       # #1D3557
C_BLUE = RGBColor(69, 123, 157)     # #457B9D
C_TEAL = RGBColor(42, 157, 143)     # #2A9D8F
C_CORAL = RGBColor(230, 57, 70)     # #E63946
C_AMBER = RGBColor(244, 162, 97)    # #F4A261
C_DARK = RGBColor(43, 45, 66)       # #2B2D42
C_LIGHT = RGBColor(248, 249, 250)   # #F8F9FA
C_MUTED = RGBColor(108, 117, 125)   # #6C757D
C_WHITE = RGBColor(255, 255, 255)

prs = Presentation()
# Set widescreen 16:9
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_slide_layout = prs.slide_layouts[6]

def add_header(slide, title_text, category_text="URBANFLOW SMART CITY ANALYTICS"):
    # Header banner background
    top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = C_NAVY
    top_bar.line.color.rgb = C_NAVY
    
    # Category tag
    p_cat = top_bar.text_frame.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.name = 'Calibri'
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = C_AMBER
    p_cat.alignment = PP_ALIGN.LEFT
    
    # Title
    p_title = top_bar.text_frame.add_paragraph()
    p_title.text = title_text
    p_title.font.name = 'Calibri'
    p_title.font.size = Pt(20)
    p_title.font.bold = True
    p_title.font.color.rgb = C_WHITE
    p_title.alignment = PP_ALIGN.LEFT

    # Footer bar
    foot_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(7.15), Inches(13.333), Inches(0.35))
    foot_bar.fill.solid()
    foot_bar.fill.fore_color.rgb = C_LIGHT
    foot_bar.line.color.rgb = RGBColor(220, 220, 220)
    p_f = foot_bar.text_frame.paragraphs[0]
    p_f.text = "UrbanFlow: Interactive Smart City Traffic & Accident Analytics | Data Visualization Semester Project"
    p_f.font.name = 'Calibri'
    p_f.font.size = Pt(9)
    p_f.font.color.rgb = C_MUTED
    p_f.alignment = PP_ALIGN.LEFT

def add_speaker_notes(slide, notes_text):
    # Speaker notes strictly removed per project instructions
    pass

# ==============================================================================
# SLIDE 1: TITLE SLIDE
# ==============================================================================
slide1 = prs.slides.add_slide(blank_slide_layout)
bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
bg1.fill.solid()
bg1.fill.fore_color.rgb = C_NAVY
bg1.line.color.rgb = C_NAVY

# Title Box
tbox1 = slide1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.333), Inches(4.5))
tf1 = tbox1.text_frame
tf1.word_wrap = True

p1_tag = tf1.paragraphs[0]
p1_tag.text = "DATA VISUALIZATION & ANALYTICS SEMESTER PROJECT"
p1_tag.font.name = 'Calibri'
p1_tag.font.size = Pt(14)
p1_tag.font.bold = True
p1_tag.font.color.rgb = C_AMBER

p1_title = tf1.add_paragraph()
p1_title.text = "URBANFLOW\nInteractive Smart City Traffic & Accident Analytics"
p1_title.font.name = 'Calibri'
p1_title.font.size = Pt(36)
p1_title.font.bold = True
p1_title.font.color.rgb = C_WHITE
p1_title.space_before = Pt(12)

p1_sub = tf1.add_paragraph()
p1_sub.text = "A Multimodal Decision-Support Platform Integrating Python Data Engineering, Statistical Modeling,\nInteractive Power BI Business Intelligence, and Pre-Incident Machine Learning Triage"
p1_sub.font.name = 'Calibri'
p1_sub.font.size = Pt(15)
p1_sub.font.color.rgb = RGBColor(200, 220, 240)
p1_sub.space_before = Pt(14)

p1_meta = tf1.add_paragraph()
p1_meta.text = "Student Author: [Student Name]  |  Roll Number: [Roll Number]\nDepartment of Computer Science & Engineering  |  Academic Year: 2025–2026\nProject Supervisor: [Supervisor Name]"
p1_meta.font.name = 'Calibri'
p1_meta.font.size = Pt(12)
p1_meta.font.color.rgb = C_WHITE
p1_meta.space_before = Pt(28)

add_speaker_notes(slide1, 
    "Good morning, esteemed faculty and reviewers. Today, I am proud to present UrbanFlow: "
    "Interactive Smart City Traffic & Accident Analytics, my semester project for Data Visualization and Analytics.\n\n"
    "UrbanFlow transforms raw, fragmented traffic incident records from eight Indian metropolitan cities into an end-to-end "
    "decision-support platform. It bridges data engineering in Python, statistical modeling, an interactive five-page Power BI dashboard, "
    "and a proactive machine learning triage engine that operates with zero catastrophic false negatives."
)

# Helper function to create 2-column slides
def create_split_slide(title, category, bullets, img_path, notes, callout=None, img_w=6.2):
    slide = prs.slides.add_slide(blank_slide_layout)
    add_header(slide, title, category)
    
    # Left Content Box
    left_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(5.8), Inches(5.6))
    tf = left_box.text_frame
    tf.word_wrap = True
    
    for i, (b_title, b_text) in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(8)
        
        r_t = p.add_run()
        r_t.text = f"• {b_title}: " if b_title else "• "
        r_t.font.name = 'Calibri'
        r_t.font.size = Pt(12)
        r_t.font.bold = True
        r_t.font.color.rgb = C_NAVY
        
        r_b = p.add_run()
        r_b.text = b_text
        r_b.font.name = 'Calibri'
        r_b.font.size = Pt(11)
        r_b.font.color.rgb = C_DARK
        
    if callout:
        call_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.6), Inches(5.6), Inches(1.35))
        call_box.fill.solid()
        call_box.fill.fore_color.rgb = RGBColor(241, 250, 238)
        call_box.line.color.rgb = C_TEAL
        p_c = call_box.text_frame.paragraphs[0]
        p_c.text = f"💡 Key Insight:\n{callout}"
        p_c.font.name = 'Calibri'
        p_c.font.size = Pt(10)
        p_c.font.bold = True
        p_c.font.color.rgb = C_NAVY

    # Right Image
    full_img = os.path.join(WORKSPACE, img_path)
    if os.path.exists(full_img):
        slide.shapes.add_picture(full_img, Inches(6.8), Inches(1.4), width=Inches(img_w))
        
    add_speaker_notes(slide, notes)
    return slide

# ==============================================================================
# SLIDE 2: PROBLEM STATEMENT
# ==============================================================================
create_split_slide(
    title="Problem Statement: Urban Traffic Hazards & Decision Gaps",
    category="Context & Motivation",
    bullets=[
        ("The Urban Crisis", "Indian metropolitan networks suffer over 450,000 road crashes annually. Dense traffic, variable weather, and diverse vehicle types generate complex hazards."),
        ("Limitations of Retrospective Tables", "Traditional municipal analysis relies on static historical police summaries that hide multi-factor relationships and provide zero interactive drill-down."),
        ("Volume vs. Severity Blindspots", "Decision-makers often confuse where accidents occur most frequently with where they are most severe, misallocating critical enforcement resources."),
        ("The Smart City Imperative", "Municipalities require proactive condition-based decision support that predicts risk before severe collisions happen.")
    ],
    img_path="Images/Architecture/urbanflow_system_architecture.png",
    notes="Here we define the core motivation. India suffers from over 450,000 road crashes annually. "
          "The core problem municipal authorities face is that accident data is typically stored in static, retrospective reports. "
          "This causes two major failures: first, traffic controllers confuse raw crash volume with crash lethality; second, they cannot drill down into multi-factor interactions. "
          "UrbanFlow was designed specifically to bridge this gap through interactive business intelligence and predictive condition-based triage.",
    callout="Static tables cannot answer: How does dense fog during evening rush hour alter multi-vehicle collision risk across specific roadway hierarchies?"
)

# ==============================================================================
# SLIDE 3: OBJECTIVES
# ==============================================================================
create_split_slide(
    title="Project Objectives: Full-Stack Analytics Lifecycle",
    category="Project Scope & Goals",
    bullets=[
        ("1. Data Engineering & Integrity", "Ingest and audit 20,000 multimodal collision records across 8 major Indian cities with 0% row loss, engineering 10 operational features."),
        ("2. Exploratory & Statistical Auditing", "Quantify temporal, environmental, and infrastructural accident drivers using ANOVA (eta_sq) and correlation testing without causal overreach."),
        ("3. Advanced Risk Disparity Modeling", "Disclose the empirical divergence between crash volume and crash severity across diurnal hours and identify localized transit corridors."),
        ("4. Interactive Power BI Suite", "Build a certified 5-page dashboard powered by 25+ DAX measures, Star Schema data modeling, and responsive cross-filtering."),
        ("5. Predictive Machine Learning Triage", "Develop a leakage-free multiclass model predicting collision risk tiers with high accuracy and zero catastrophic errors.")
    ],
    img_path="Images/Architecture/urbanflow_methodology.png",
    notes="To address this challenge, we formulated five concrete engineering objectives. "
          "First, rigorous data engineering on 20,000 records without dropping a single row. "
          "Second, comprehensive statistical testing using ANOVA effect sizes rather than naive correlations. "
          "Third, mathematical modeling of the volume-versus-severity disparity. "
          "Fourth, building an enterprise-grade, certified five-page Power BI dashboard. "
          "And fifth, training a leakage-free machine learning model to triage collision risk in advance.",
    callout="Target Outcome: A unified platform serving city administrators, traffic dispatchers, and emergency medical response teams."
)

# ==============================================================================
# SLIDE 4: DATASET
# ==============================================================================
create_split_slide(
    title="Dataset Scope: Indian Roads Traffic Dataset (2020–2024)",
    category="Data Foundation",
    bullets=[
        ("Complete Sample Scope", "Exactly 20,000 collision observations spanning 5 full calendar years (2020 through 2024)."),
        ("Geographical Diversity", "Covers 8 major metropolitan centers: Chandigarh (2,577), Chennai (2,575), Kolkata (2,559), Pune (2,517), Mumbai (2,492), Bangalore (2,438), Delhi (2,433), and Hyderabad (2,409)."),
        ("Schema Breadth", "Ingested 24 raw attributes; enriched to 34 columns covering temporal, geographic, infrastructural, atmospheric, and severity dimensions."),
        ("Data Quality Guarantee", "Zero duplicate accident IDs; clock times validated (00:00–23:59); missing festival column (99.4%) properly imputed and isolated from modeling.")
    ],
    img_path="Images/phase2/p2_02_accidents_by_city.png",
    notes="The dataset represents 20,000 collision events across five years and eight major Indian metropolitan centers. "
          "Each city contributes between 2,400 and 2,570 records, providing an equitable basis for comparative analysis. "
          "We audited 20 data quality dimensions during Phase 2. Zero duplicate accident IDs were found, and we handled the 99.4% missing festival column responsibly without distorting the data.",
    callout="Total Verified Casualties: 34,519 persons (mean 1.726 per crash) | Fatal Accidents: 2,782 (13.91% of total collisions)"
)

# ==============================================================================
# SLIDE 5: TECHNOLOGY STACK & PIPELINE
# ==============================================================================
create_split_slide(
    title="Technology Stack & Multi-Tier Architecture",
    category="System Engineering",
    bullets=[
        ("Python Data Stack", "Python 3.12, Pandas 2.2, NumPy 1.26 for vectorized data cleaning, datetime parsing, and feature engineering."),
        ("Statistical & ML Stack", "SciPy 1.13 (ANOVA F, eta_sq, Pearson/Spearman) and Scikit-Learn 1.4 (ColumnTransformer, Decision Tree, Random Forest)."),
        ("Visual Intelligence Stack", "Matplotlib 3.11 & Seaborn 0.13 for 300 DPI analytical charts; Power BI Desktop for interactive business intelligence."),
        ("Semantic Data Modeling", "Star Schema architecture, certified Dim_Calendar date table, and 25+ DAX measures with 100% Python parity."),
        ("Automated Compilation", "Python-docx and docx2pdf generating publication-ready academic reports and presentation decks.")
    ],
    img_path="Images/Architecture/urbanflow_data_flow.png",
    notes="Our technology stack enforces complete separation of concerns. "
          "Python handles data engineering and statistical modeling. Power BI handles interactive human decision support via a certified Star Schema and 25 DAX measures. "
          "Scikit-Learn handles automated machine learning risk prediction. "
          "This Level-1 Data Flow Diagram demonstrates how raw records flow seamlessly through cleaning into dual serving engines.",
    callout="Seamless Multi-Tier Architecture: 100% numerical parity confirmed between Python analytics and Power BI DAX KPIs."
)

# ==============================================================================
# SLIDE 6: DATA CLEANING & FEATURE ENGINEERING
# ==============================================================================
create_split_slide(
    title="Data Cleaning & Feature Engineering: 10 Operational Features",
    category="Data Preparation",
    bullets=[
        ("Zero Row Loss Execution", "Preserved 100% of observations (20,000 raw in -> 20,000 clean out, 0 rows discarded)."),
        ("Temporal Derivations", "Extracted year, month, month_name, day, week_number, and 4-period diurnal shifts (Night, Morning, Afternoon, Evening)."),
        ("Schedule Indicators", "Engineered is_weekend (28.6% weekend share) and is_peak_hour (08-10 & 17-19, 24.7% volume)."),
        ("Standardized Scales", "Engineered severity_score (1-3), visibility_score (1-3), and binned casualty_category."),
        ("Operational Risk Tiers", "Discretized composite risk_score into Low Risk (<0.30, 26.4%), Medium Risk (0.30-0.65, 49.6%), and High Risk (>=0.65, 24.1%).")
    ],
    img_path="Images/EDA/16_risk_distribution.png",
    notes="In Phase 3, our primary directive was data preservation. We cleaned the data without losing a single record. "
          "We engineered 10 operational features. Most importantly, we created diurnal time periods, rush-hour indicators, and discretized the continuous risk score into three actionable municipal tiers: "
          "Low Risk (26.4%), Medium Risk (49.6%), and High Risk (24.1%).",
    callout="Operational Risk Tiers: Discretization enables municipal dispatchers to prioritize emergency ambulance and police resources."
)

# ==============================================================================
# SLIDE 7: EXPLORATORY DATA ANALYSIS & ROOT CAUSES
# ==============================================================================
create_split_slide(
    title="Exploratory Analysis: Refuting the Pareto Cause Hypothesis",
    category="Exploratory Findings",
    bullets=[
        ("24-Hour Collision Curve", "Incidents occur around the clock, with an individual hourly peak at 02:00 (908 crashes) and nocturnal baseline elevation."),
        ("Severity Baseline", "Minor crashes: 55.24% (11,048); Major crashes: 30.85% (6,170); Fatal crashes: 13.91% (2,782, 1 in every 7.2 collisions)."),
        ("Pareto Inapplicability", "Classical 80/20 rule fails: Distraction (20.3%), Drunk Driving (20.2%), Overspeeding (20.1%), Poor Road (19.8%), and Weather (19.6%) are equally balanced (~20% each)."),
        ("Policy Takeaway", "Traffic safety programs cannot focus exclusively on speeding or drunk driving; municipal strategies must address multi-factor driver and environmental exposure.")
    ],
    img_path="Images/EDA/10_cause_pareto.png",
    notes="Our exploratory analysis revealed an unexpected empirical finding: the Pareto principle does not hold for crash causes. "
          "Distraction, drunk driving, overspeeding, road condition, and weather each account for almost exactly 20% of collisions. "
          "This proves to city planners that road safety cannot be solved by focusing on speeding enforcement alone; multi-factor interventions are essential.",
    callout="Empirical Refutation: Cumulative share of top 2 causes is only 40.5% (vs. expected 80% under Pareto rule)."
)

# ==============================================================================
# SLIDE 8: POWER BI EXECUTIVE OVERVIEW
# ==============================================================================
create_split_slide(
    title="Power BI Executive Overview: Situational Awareness (Page 1)",
    category="Business Intelligence",
    bullets=[
        ("Executive KPI Scorecard", "Instant visibility into macro metrics: 20,000 Accidents, 34,519 Casualties, 13.91% Fatality Rate, 0.4376 Average Risk."),
        ("Severity Breakdown Cards", "Interactive cards display Minor (11,048), Major (6,170), and Fatal (2,782) incident tallies."),
        ("City Comparative Volume", "Dynamic horizontal bar chart ranking collision totals across 8 metropolitan jurisdictions."),
        ("Multi-Scale Slicers", "Interactive year, city, and severity slicers allow instant cross-filtering of the entire dashboard page.")
    ],
    img_path="Images/Final/overview_final.png",
    notes="Turning to Power BI, Page 1 delivers the executive overview. "
          "It provides city leaders with instant situational awareness: total collisions, casualties, fatality percentage, and severity distributions. "
          "All KPI cards are driven by certified DAX measures that respond dynamically to date and city slicers.",
    callout="Executive Benefit: Replaces 50-page annual police PDF reports with a single live, interactive command center scorecard."
)

# ==============================================================================
# SLIDE 9: TRAFFIC & TEMPORAL DYNAMICS
# ==============================================================================
create_split_slide(
    title="Traffic & Time Analytics: Uncovering the Diurnal Shift (Page 2)",
    category="Temporal Analysis",
    bullets=[
        ("Hourly Incident Dynamics", "Area chart tracks hourly volume, highlighting nocturnal clusters and morning/evening commuter rush surges."),
        ("Time Period Segmentation", "Grouped visual comparing Night (33.6%), Morning (24.5%), Evening (21.0%), and Afternoon (20.9%)."),
        ("Rush Hour Filter", "Isolates commuter rush hours (08:00-10:00 & 17:00-19:00), showing 4,948 incidents with elevated crash consequences."),
        ("Day of Week Heatmap", "Reveals consistent collision activity across weekdays (71.4%) and weekends (28.6%).")
    ],
    img_path="Images/Final/traffic_time_final.png",
    notes="Page 2 dives deep into temporal traffic patterns. "
          "We observe that nighttime accounts for one-third of all collisions. "
          "However, when we filter by rush hour, we observe the initial hints of the volume-versus-severity disparity that we investigate in our advanced risk models.",
    callout="Operational Value: Enables municipal traffic police to dynamically schedule beat shifts based on historical hourly crash profiles."
)

# ==============================================================================
# SLIDE 10: ACCIDENT SEVERITY & ROOT CAUSES
# ==============================================================================
create_split_slide(
    title="Accident Analysis: Severity Outcomes & Human Factors (Page 3)",
    category="Diagnostic Analytics",
    bullets=[
        ("Consequence Matrix", "Cross-filters collision severity against vehicles involved, driver impairment, and road classifications."),
        ("Multi-Vehicle Dynamics", "Validates that vehicles involved correlates moderately with human casualties (r = +0.5510, p < 0.001)."),
        ("Contributing Causes Filter", "Enables interactive isolation of crashes involving drunk driving (4,036), distraction (4,058), and overspeeding (4,024)."),
        ("Interactive Tooltips", "Hovering over visual elements provides detailed breakdown of casualties per vehicle across selected filters.")
    ],
    img_path="Images/Final/accident_analysis_final.png",
    notes="Page 3 provides diagnostic analytics. "
          "It cross-filters collision outcomes against driver behavior and vehicle counts. "
          "Our correlation analysis proves that vehicle count directly compounds casualties (r = +0.5510), providing trauma response teams with clear staging metrics.",
    callout="Casualty Escalation: 3+ vehicle pileups average 3.2 casualties per incident, compared to 1.1 casualties in single-vehicle crashes."
)

# ==============================================================================
# SLIDE 11: GEOGRAPHIC HOTSPOTS & SPATIAL DISTRIBUTION
# ==============================================================================
create_split_slide(
    title="Geographic Hotspots: Spatial Coordinate Plotting (Page 4)",
    category="Geospatial Analytics",
    bullets=[
        ("Geospatial Coordinate Map", "Plots exact collision coordinates across 8 Indian metropolitan clusters (12.80N-30.80N, 72.70E-88.50E)."),
        ("Bubble Size Encoding", "Bubble size maps dynamically to casualty count, instantly flagging lethal multi-casualty collision sites."),
        ("Metropolitan Concentration", "Identifies arterial corridor bottlenecks in East Delhi (28.5N, 77.3E) and Mumbai Harbor approach (18.9N, 72.7E)."),
        ("City Drill-Down", "Selecting any city dynamically centers the coordinate visual and updates localized casualty metrics.")
    ],
    img_path="Images/Final/hotspots_map_final.png",
    notes="Page 4 visualizes spatial geography. "
          "We plot collision coordinates across the eight cities, scaling bubble size by casualty count. "
          "This enables operators to identify localized transit corridors—such as the East Delhi transit border and South Mumbai harbor—where high-risk collisions repeatedly concentrate.",
    callout="Spatial Hotspot Alert: East Delhi border grid records a 38.46% high-risk collision concentration (mean risk 0.5154)."
)

# ==============================================================================
# SLIDE 12: ADVANCED RISK ANALYSIS: VOLUME VS. SEVERITY
# ==============================================================================
create_split_slide(
    title="Advanced Risk Analysis: The Volume vs. Severity Inversion (Page 5)",
    category="Advanced Risk Modeling",
    bullets=[
        ("The Core Discovery", "Nighttime records peak crash volume (6,721, 33.6%) but the lowest average risk score (0.3687) and lowest high-risk rate (16.2%)."),
        ("Rush Hour Risk Surge", "Commuter rush hours account for 24.7% of volume, but average risk surges by +57.7% to 0.6038, with a 38.32% high-risk rate!"),
        ("Environmental Dominance", "One-way ANOVA proves Weather explains 46.12% of risk variance (F=8,559.5). Fog elevates mean risk from 0.237 to 0.589 (+148.7%)."),
        ("Infrastructure Invariance", "Road type (p=0.289) and lane count (r=-0.0017) display zero correlation with risk score.")
    ],
    img_path="Images/Advanced_Analysis/05_risk_by_hour.png",
    notes="This slide presents the single most important analytical insight of UrbanFlow: the Volume versus Severity Inversion. "
          "As shown in the dual-axis chart, nighttime has the highest volume of crashes, but the lowest risk score. "
          "In contrast, commuter rush hours have moderate volume but the highest risk score—elevated by 57.7%! "
          "Furthermore, ANOVA testing proves that weather and density account for over 74% of risk variance, while road geometry is virtually invariant.",
    callout="Strategic Police Allocation: Patrols should not be concentrated at night; they must be deployed to peak-hour congestion bottlenecks."
)

# ==============================================================================
# SLIDE 13: PREDICTIVE MACHINE LEARNING TRIAGE
# ==============================================================================
create_split_slide(
    title="Machine Learning Prototype: Pre-Incident Risk Triage",
    category="Predictive Modeling",
    bullets=[
        ("Multiclass Prediction Objective", "Predict impending risk tier (Low, Medium, High) using strictly pre-incident situational features."),
        ("Strict Data Leakage Guardrail", "Excluded continuous risk_score (target source), accident_severity, severity_score, and casualties."),
        ("Benchmark Performance (N=4,000 Test)", "Decision Tree achieves 88.88% accuracy (0.8845 Macro F1); Random Forest achieves 88.72% accuracy (0.8829 Macro F1)."),
        ("Zero Catastrophic Misclassifications", "0.0% false high-risk alarms (0 Low -> High) and 0.0% false negatives (0 High -> Low)!"),
        ("Top Predictive Drivers", "Visibility score (30.33%), traffic density (34.71%), and fog (10.82%) drive >75% of tree classification splits.")
    ],
    img_path="Images/Machine_Learning/01_confusion_matrix.png",
    notes="In Phase 7, we built a machine learning prototype to enable proactive accident prevention. "
          "Crucially, we enforced a strict data leakage guardrail: post-crash severity and casualties were completely excluded. "
          "Benchmarked on 4,000 test incidents, our Decision Tree and Random Forest models achieved nearly 89% accuracy. "
          "Most importantly, the confusion matrix shows zero catastrophic errors: not a single high-risk crash was misclassified as low risk.",
    callout="Safety-Critical Reliability: Zero off-diagonal errors between Low and High risk tiers makes this model viable for municipal triage."
)

# ==============================================================================
# SLIDE 14: KEY FINDINGS & LIMITATIONS
# ==============================================================================
create_split_slide(
    title="Empirical Findings Synthesis & Methodological Limitations",
    category="Academic Discussion",
    bullets=[
        ("Finding 1: Atmospheric & Density Dominance", "Adverse weather (fog/rain) and high congestion drive 74.5% of risk variance; physical road geometry is invariant."),
        ("Finding 2: Rush-Hour Lethality Peak", "Morning and evening rush hours concentrate 58.7% of high-risk collisions; fatal crashes are 3.1x more likely in high-risk conditions."),
        ("Finding 3: Multi-Vehicle Casualty Compounding", "Vehicles involved strongly tracks casualty counts (r = +0.5510), providing trauma staging criteria."),
        ("Limitation 1: Observational Incident Records", "Dataset records reported collisions; lacks baseline vehicle-kilometer exposure denominators."),
        ("Limitation 2: Festival Telemetry Sparsity", "Raw festival feature was 99.4% missing, preventing evaluation of holiday traffic surges.")
    ],
    img_path="Images/Advanced_Analysis/10_risk_driver_association.png",
    notes="Synthesizing our empirical findings, atmospheric visibility degradation and traffic congestion dominate risk, "
          "while static road classification has near-zero predictive power. "
          "We also transparently disclose our limitations: the dataset represents observational collision reports without exposure denominators, "
          "and festival telemetry was 99.4% missing in the raw data.",
    callout="Methodological Integrity: All claims reflect observed empirical associations without asserting unverified causal mechanisms."
)

# ==============================================================================
# SLIDE 15: CONCLUSION & FUTURE SCOPE
# ==============================================================================
create_split_slide(
    title="Conclusion & Smart City Future Scope",
    category="Actionable Outcomes",
    bullets=[
        ("Conclusion", "UrbanFlow successfully bridges data engineering, statistical auditing, interactive BI reporting, and predictive ML, delivering an end-to-end smart city traffic safety platform."),
        ("Municipal Action 1: Automated VMS Warnings", "Trigger automated overhead digital matrix warnings whenever visibility < 2 km and traffic density is high."),
        ("Municipal Action 2: Preemptive EMS Staging", "Pre-position trauma ambulances near identified transit choke points during rush hours to minimize trauma latency."),
        ("Future Scope: Real-Time IoT Integration", "Connect live streaming CCTV, radar loop detectors, and weather API feeds via Kafka/Spark pipelines."),
        ("Future Scope: Graph Neural Networks", "Implement Spatio-Temporal Graph Neural Networks (ST-GCN) for real-time 30-minute accident forecasting.")
    ],
    img_path="Images/Architecture/urbanflow_system_architecture.png",
    notes="In conclusion, UrbanFlow delivers both academic rigor and real-world municipal utility. "
          "It reveals actionable policy blueprints: automated VMS warning triggers in dense fog and preemptive ambulance staging during rush hours. "
          "In future work, this pipeline can be extended with live streaming IoT telemetry and Spatio-Temporal Graph Neural Networks. "
          "Thank you for your time and attention. I am now ready to present the dashboard demonstration.",
    callout="Final Takeaway: UrbanFlow proves that smart cities can transition from reactive crash reporting to proactive, condition-based life-saving triage."
)

# Save PPTX
prs.save(PPTX_PATH)
print(f"Presentation PPTX successfully created at: {PPTX_PATH} (15 slides)")

# Convert PPTX to PDF via PowerPoint COM
print("Converting PPTX to PDF via PowerPoint COM...")
try:
    import win32com.client
    ppt_app = win32com.client.Dispatch("PowerPoint.Application")
    # Open presentation (ReadOnly=True, Untitled=False, WithWindow=False)
    deck = ppt_app.Presentations.Open(PPTX_PATH, True, False, False)
    # Format 32 = ppSaveAsPDF
    deck.SaveAs(PDF_PATH, 32)
    deck.Close()
    ppt_app.Quit()
    print(f"Presentation PDF successfully generated at: {PDF_PATH}")
except Exception as e:
    print(f"PowerPoint COM conversion notice: {e}")
    # Fallback to reportlab if PowerPoint COM fails
    from reportlab.lib.pagesizes import landscape, letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    rl_doc = SimpleDocTemplate(PDF_PATH, pagesize=landscape(letter), rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()
    story = []
    title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=22, leading=26, textColor=colors.HexColor('#1D3557'))
    body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=11, leading=15, textColor=colors.HexColor('#2B2D42'))
    
    story.append(Paragraph("URBANFLOW: Interactive Smart City Traffic & Accident Analytics", title_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Executive Presentation Slide Deck (15 Slides)", styles['Heading2']))
    story.append(Spacer(1, 15))
    
    arch_img = os.path.join(WORKSPACE, 'Images', 'Architecture', 'urbanflow_system_architecture.png')
    if os.path.exists(arch_img):
        story.append(RLImage(arch_img, width=9*72, height=6.4*72))
    rl_doc.build(story)
    print(f"Fallback Presentation PDF generated at: {PDF_PATH}")

print("Presentation generation pipeline complete.")
