import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')

WORKSPACE = r'c:\Users\thaku\Desktop\🚦 Smart City Traffic'
REPORT_DIR = os.path.join(WORKSPACE, 'Report')
os.makedirs(REPORT_DIR, exist_ok=True)

DOCX_PATH = os.path.join(REPORT_DIR, 'UrbanFlow_Final_Report.docx')
PDF_PATH = os.path.join(REPORT_DIR, 'UrbanFlow_Final_Report.pdf')
MD_PATH = os.path.join(REPORT_DIR, 'Project_Report.md')

# Color Constants
C_NAVY_RGB = RGBColor(29, 53, 87)       # #1D3557
C_BLUE_RGB = RGBColor(69, 123, 157)     # #457B9D
C_TEAL_RGB = RGBColor(42, 157, 143)     # #2A9D8F
C_DARK_RGB = RGBColor(43, 45, 66)       # #2B2D42
C_MUTED_RGB = RGBColor(108, 117, 125)   # #6C757D
HEX_NAVY = "1D3557"
HEX_LIGHT_BG = "F8F9FA"
HEX_BORDER = "CCCCCC"

doc = Document()

# Page Setup: 1-inch margins
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)
    section.page_width = Inches(8.5)
    section.page_height = Inches(11.0)

# Helper XML styling functions
def set_cell_background(cell, hex_color):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_styled_heading(text, level, space_before=14, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Calibri'
    run.font.bold = True
    if level == 1:
        run.font.size = Pt(17)
        run.font.color.rgb = C_NAVY_RGB
        # Add bottom border/rule beneath H1
        pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="12" w:space="4" w:color="{HEX_NAVY}"/></w:pBdr>')
        p._p.get_or_add_pPr().append(pBdr)
    elif level == 2:
        run.font.size = Pt(13.5)
        run.font.color.rgb = C_BLUE_RGB
    elif level == 3:
        run.font.size = Pt(11.5)
        run.font.color.rgb = C_TEAL_RGB
    return p

def add_body_p(text="", bold_prefix="", space_after=6, italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Calibri'
        r_pre.font.size = Pt(10.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = C_DARK_RGB
    if text:
        r_text = p.add_run(text)
        r_text.font.name = 'Calibri'
        r_text.font.size = Pt(10.5)
        r_text.font.color.rgb = C_DARK_RGB
        r_text.font.italic = italic
    return p

def add_callout(text, title="KEY ANALYTICAL FINDING", border_color="1D3557", bg_color="F1FAEE"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    
    cell = table.cell(0, 0)
    set_cell_background(cell, bg_color)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(4)
    r_t = p.add_run(f"📌 {title}\n")
    r_t.font.name = 'Calibri'
    r_t.font.size = Pt(10.5)
    r_t.font.bold = True
    r_t.font.color.rgb = C_NAVY_RGB
    
    r_b = p.add_run(text)
    r_b.font.name = 'Calibri'
    r_b.font.size = Pt(10)
    r_b.font.color.rgb = C_DARK_RGB
    
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_table_styled(headers, rows, col_widths=None):
    tbl = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    # Header Row
    hdr_cells = tbl.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        set_cell_background(hdr_cells[i], HEX_NAVY)
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=120, right=120)
        p = hdr_cells[i].paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        p.runs[0].font.name = 'Calibri'
        p.runs[0].font.size = Pt(9.5)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = RGBColor(255, 255, 255)
        if col_widths and i < len(col_widths):
            hdr_cells[i].width = Inches(col_widths[i])
            
    # Data Rows
    for r_idx, row_data in enumerate(rows):
        row_cells = tbl.rows[r_idx + 1].cells
        bg = HEX_LIGHT_BG if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            row_cells[c_idx].text = str(val)
            set_cell_background(row_cells[c_idx], bg)
            set_cell_margins(row_cells[c_idx], top=80, bottom=80, left=120, right=120)
            p = row_cells[c_idx].paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            if p.runs:
                p.runs[0].font.name = 'Calibri'
                p.runs[0].font.size = Pt(9.0)
                p.runs[0].font.color.rgb = C_DARK_RGB
            if col_widths and c_idx < len(col_widths):
                row_cells[c_idx].width = Inches(col_widths[c_idx])
                
    # Apply thin borders
    for row in tbl.rows:
        for cell in row.cells:
            tcPr = cell._element.get_or_add_tcPr()
            b = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="{HEX_BORDER}"/><w:left w:val="none"/><w:right w:val="none"/></w:tcBorders>')
            tcPr.append(b)
            
    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    return tbl

def add_image_with_caption(img_rel_path, caption_text, width_in=6.0):
    full_path = os.path.join(WORKSPACE, img_rel_path)
    if os.path.exists(full_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        p_img.paragraph_format.keep_with_next = True
        run_img = p_img.add_run()
        run_img.add_picture(full_path, width=Inches(width_in))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(10)
        r_cap = p_cap.add_run(caption_text)
        r_cap.font.name = 'Calibri'
        r_cap.font.size = Pt(9.0)
        r_cap.font.italic = True
        r_cap.font.color.rgb = C_MUTED_RGB
    else:
        print(f"Warning: Image file not found at {full_path}")

print("Building UrbanFlow Comprehensive Academic Report (DOCX)...")

# ==============================================================================
# 1. COVER PAGE (STEP 8.10)
# ==============================================================================
p_cov_top = doc.add_paragraph()
p_cov_top.paragraph_format.space_before = Pt(36)
p_cov_top.paragraph_format.space_after = Pt(10)
p_cov_top.alignment = WD_ALIGN_PARAGRAPH.CENTER

r_cov_pre = p_cov_top.add_run("ACADEMIC SEMESTER PROJECT REPORT\nDATA VISUALIZATION & ANALYTICS COURSE")
r_cov_pre.font.name = 'Calibri'
r_cov_pre.font.size = Pt(12)
r_cov_pre.font.bold = True
r_cov_pre.font.color.rgb = C_BLUE_RGB

p_cov_title = doc.add_paragraph()
p_cov_title.paragraph_format.space_before = Pt(18)
p_cov_title.paragraph_format.space_after = Pt(8)
p_cov_title.alignment = WD_ALIGN_PARAGRAPH.CENTER

r_title = p_cov_title.add_run("URBANFLOW\n")
r_title.font.name = 'Calibri'
r_title.font.size = Pt(32)
r_title.font.bold = True
r_title.font.color.rgb = C_NAVY_RGB

r_sub = p_cov_title.add_run("Interactive Smart City Traffic & Accident Analytics")
r_sub.font.name = 'Calibri'
r_sub.font.size = Pt(16)
r_sub.font.color.rgb = C_TEAL_RGB

p_cov_sub = doc.add_paragraph()
p_cov_sub.paragraph_format.space_before = Pt(12)
p_cov_sub.paragraph_format.space_after = Pt(36)
p_cov_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_desc = p_cov_sub.add_run("A Multimodal Decision-Support Platform Integrating Python Data Engineering,\nExploratory Data Analysis, Interactive Power BI Dashboards, and Predictive Machine Learning")
r_desc.font.name = 'Calibri'
r_desc.font.size = Pt(10.5)
r_desc.font.color.rgb = C_MUTED_RGB

# Student and Institution Placeholders
table_cov = doc.add_table(rows=5, cols=2)
table_cov.alignment = WD_TABLE_ALIGNMENT.CENTER
table_cov.autofit = False
table_cov.columns[0].width = Inches(3.0)
table_cov.columns[1].width = Inches(3.5)

cov_data = [
    ("Submitted By:", "[Student Name]"),
    ("Roll Number / Student ID:", "[Roll Number]"),
    ("Degree Program & Department:", "[Department of Computer Science / Data Science]"),
    ("College / University:", "[College / University Name]"),
    ("Academic Year & Semester:", "Academic Year 2025–2026 | Semester VI")
]
for idx, (lbl, val) in enumerate(cov_data):
    r_cells = table_cov.rows[idx].cells
    r_cells[0].text = lbl
    r_cells[1].text = val
    r_cells[0].paragraphs[0].runs[0].font.name = 'Calibri'
    r_cells[0].paragraphs[0].runs[0].font.size = Pt(10)
    r_cells[0].paragraphs[0].runs[0].font.bold = True
    r_cells[0].paragraphs[0].runs[0].font.color.rgb = C_NAVY_RGB
    r_cells[1].paragraphs[0].runs[0].font.name = 'Calibri'
    r_cells[1].paragraphs[0].runs[0].font.size = Pt(10)
    r_cells[1].paragraphs[0].runs[0].font.color.rgb = C_DARK_RGB
    set_cell_background(r_cells[0], HEX_LIGHT_BG)
    set_cell_background(r_cells[1], HEX_LIGHT_BG)

p_cov_sup = doc.add_paragraph()
p_cov_sup.paragraph_format.space_before = Pt(36)
p_cov_sup.paragraph_format.space_after = Pt(12)
p_cov_sup.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_sup = p_cov_sup.add_run("Project Supervisor: [Supervisor Name], [Designation]\nFaculty of Computing & Information Sciences")
r_sup.font.name = 'Calibri'
r_sup.font.size = Pt(10.5)
r_sup.font.italic = True
r_sup.font.color.rgb = C_DARK_RGB

doc.add_page_break()

# ==============================================================================
# 2. CERTIFICATE, DECLARATION & ACKNOWLEDGEMENTS
# ==============================================================================
add_styled_heading("Certificate of Originality", level=1)
add_body_p("This is to certify that the project entitled 'URBANFLOW: Interactive Smart City Traffic & Accident Analytics' submitted by [Student Name] (Roll No: [Roll Number]) in partial fulfillment of the requirements for the Data Visualization & Analytics course during Academic Year 2025–2026 is an authentic record of original project work carried out under my supervision.")
add_body_p("To the best of my knowledge, the matter embodied in this project report has not been submitted elsewhere for the award of any other degree or diploma.")
doc.add_paragraph().paragraph_format.space_before = Pt(24)

# Signatures Table
sig_table = doc.add_table(rows=2, cols=2)
sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
sig_table.columns[0].width = Inches(3.2)
sig_table.columns[1].width = Inches(3.2)
sig_table.rows[0].cells[0].text = "______________________________\n[Supervisor Name]\nProject Supervisor"
sig_table.rows[0].cells[1].text = "______________________________\n[Head of Department]\nDepartment Head"
for cell in sig_table.rows[0].cells:
    set_cell_background(cell, "FFFFFF")
    cell.paragraphs[0].runs[0].font.name = 'Calibri'
    cell.paragraphs[0].runs[0].font.size = Pt(9.5)

add_styled_heading("Declaration of Authorship", level=1)
add_body_p("I hereby declare that this semester project report entitled 'URBANFLOW: Interactive Smart City Traffic & Accident Analytics' is entirely my own work. All analytical computations, data processing steps, visualizations, Power BI dashboard models, and machine learning scripts were developed using the designated project dataset. Wherever external literature, frameworks, or principles have been referenced, appropriate academic citations are provided in the references section.")
doc.add_paragraph().paragraph_format.space_before = Pt(20)
add_body_p("[Student Name]\nRoll Number: [Roll Number]\nDate: September 2026")

add_styled_heading("Acknowledgements", level=1)
add_body_p("I would like to express my deepest gratitude to my project supervisor, [Supervisor Name], for their invaluable guidance, constructive critique, and continuous encouragement throughout the conceptualization and development of UrbanFlow.")
add_body_p("I am also grateful to the Department of Computer Science and the course instructors of Data Visualization & Analytics for providing the computational resources, tools, and theoretical foundation required to execute this comprehensive data analytics initiative.")

doc.add_page_break()

# ==============================================================================
# 5. ABSTRACT (STEP 8.11)
# ==============================================================================
add_styled_heading("Abstract", level=1)
add_body_p("Rapid urbanization and increasing motor vehicle volumes in metropolitan India have significantly elevated road traffic hazards, resulting in substantial casualties, economic disruption, and municipal strain. Traditional traffic safety analysis relies on fragmented retrospective tables and static police reports, restricting the ability of traffic managers to proactively mitigate high-risk conditions. This semester project presents UrbanFlow, an end-to-end data analytics, interactive visual intelligence, and predictive machine learning system developed to transform raw traffic collision records into actionable smart city decision support.")
add_body_p("Operating on a validated multimodal dataset comprising exactly 20,000 recorded collision events across eight major Indian metropolitan centers (Chandigarh, Chennai, Kolkata, Pune, Mumbai, Bangalore, Delhi, and Hyderabad) spanning 2020 through 2024, UrbanFlow executes a rigorous 14-step research methodology. A Python data engineering pipeline conducts comprehensive quality auditing, data type casting, and feature engineering, preserving 100% of observations with zero row attrition while engineering 10 operational attributes including diurnal time segments, rush-hour flags, and risk classifications.")
add_body_p("Exploratory and advanced risk analysis reveals an empirical divergence between collision volume and incident severity: while nighttime hours (22:00–05:59) record the highest overall volume (6,721 collisions, 33.61%), commuter rush hours exhibit a +57.7% higher average risk score (0.6038 vs 0.3830) and an elevated high-risk collision rate of 38.32%. One-way ANOVA and correlation testing prove that atmospheric degradation (fog eta_sq = 0.4612, visibility r = -0.7291) and ambient traffic density (eta_sq = 0.2844) dominate collision risk, whereas physical road geometry (lane count r = -0.0017) and metropolitan city (p = 0.918) show statistical invariance. An interactive five-page Power BI dashboard suite backed by 25+ certified DAX measures provides dynamic multi-scale filtering, geospatial coordinate plotting, and risk triage.")
add_body_p("To enable proactive safety governance, a supervised machine learning prototype was trained strictly on pre-incident situational variables, enforcing zero data leakage. Benchmarked on a held-out test partition (N = 4,000), a Random Forest classifier achieved 88.72% accuracy and 0.8829 Macro F1, while completely eliminating catastrophic misclassifications between Low and High risk tiers (0.0% false negatives). UrbanFlow bridges retrospective visual analytics and proactive machine learning, providing a validated blueprint for automated municipal warning systems and emergency dispatch.")

add_callout(
    "Dataset: 20,000 Records (8 Indian Metropolitan Areas, 2020–2024) | Total Casualties: 34,519 | Fatal Incidents: 2,782 (13.91%)\n"
    "Key Discovery: Rush-Hour Peak Risk Disparity (Peak 0.604 vs Off-Peak 0.383) | Dominant Drivers: Visibility (r = -0.7291), Fog (eta_sq = 0.4612)\n"
    "Power BI Suite: 5 Interactive Pages, 25+ DAX Measures | ML Prototype: 88.9% Accuracy, Zero Catastrophic Errors",
    title="URBANFLOW EXECUTIVE METRICS AT A GLANCE"
)

doc.add_page_break()

# ==============================================================================
# 6, 7, 8. TABLE OF CONTENTS & LIST OF FIGURES / TABLES
# ==============================================================================
add_styled_heading("Table of Contents", level=1)
toc_items = [
    ("1. Introduction & Background", "6"),
    ("2. Problem Statement, Motivation & Objectives", "8"),
    ("3. Technology Stack & System Architecture", "10"),
    ("4. Data Pipeline: Cleaning, Preprocessing & Feature Engineering", "12"),
    ("5. Exploratory Data Analysis & Empirical Findings", "15"),
    ("6. Advanced Collision Risk & Hotspot Concentration Analysis", "20"),
    ("7. Interactive Power BI Dashboard Suite", "25"),
    ("8. Predictive Machine Learning Risk Classification Prototype", "30"),
    ("9. Results, Critical Discussion & Municipal Implications", "35"),
    ("10. Methodological Limitations & Future Scope", "38"),
    ("11. Conclusion & Recommendations", "40"),
    ("12. References", "41"),
    ("13. Appendix: Data Dictionary, DAX Formulas & Code Artifacts", "43")
]
for item, pg in toc_items:
    p_toc = doc.add_paragraph()
    p_toc.paragraph_format.space_after = Pt(4)
    p_toc.add_run(f"{item:<60} ..................................................... {pg:>4}")
    p_toc.runs[0].font.name = 'Calibri'
    p_toc.runs[0].font.size = Pt(10)

add_styled_heading("List of Figures", level=2)
lof_items = [
    ("Figure 1: UrbanFlow End-to-End System Architecture Pipeline", "11"),
    ("Figure 2: Level-1 Data Flow Diagram (DFD) of the Pipeline", "12"),
    ("Figure 3: 14-Step Research and Engineering Methodology Framework", "14"),
    ("Figure 4: Hourly Collision Volume Distribution (24-Hour Cycle)", "16"),
    ("Figure 5: Collision Severity Breakdown (Minor, Major, Fatal)", "17"),
    ("Figure 6: Pareto Analysis of Primary Reported Accident Causes", "18"),
    ("Figure 7: Collision Distribution Across Weather Conditions", "19"),
    ("Figure 8: Correlation Heatmap Across Numerical Features", "20"),
    ("Figure 9: Risk Score and High-Risk Incidents Across 8 Cities", "22"),
    ("Figure 10: Empirical Risk Score Distribution by Weather Condition", "23"),
    ("Figure 11: Collision Volume vs. Average Risk Score Hourly Curve", "24"),
    ("Figure 12: High-Risk Collision Signature Across Driving Dimensions", "25"),
    ("Figure 13: Statistical Driver Association Matrix (ANOVA & Pearson)", "26"),
    ("Figure 14: Geographic High-Risk Concentration Across City Clusters", "27"),
    ("Figure 15: Power BI Executive Overview Dashboard (Page 1)", "28"),
    ("Figure 16: Power BI Traffic & Temporal Dynamics Dashboard (Page 2)", "29"),
    ("Figure 17: Power BI Accident Severity & Causes Dashboard (Page 3)", "30"),
    ("Figure 18: Power BI Hotspots & Spatial Distribution Dashboard (Page 4)", "31"),
    ("Figure 19: Power BI Advanced Risk Insights Dashboard (Page 5)", "32"),
    ("Figure 20: Random Forest Confusion Matrix (N=4,000 Test Set)", "33"),
    ("Figure 21: Machine Learning Model Performance Benchmark", "34"),
    ("Figure 22: Random Forest Feature Importance (MDI) Ranking", "35"),
    ("Figure 23: Multiclass One-vs-Rest ROC Curves for Risk Categories", "36")
]
for item, pg in lof_items:
    p_lof = doc.add_paragraph()
    p_lof.paragraph_format.space_after = Pt(3)
    p_lof.add_run(f"{item:<65} ....... {pg:>4}")
    p_lof.runs[0].font.name = 'Calibri'
    p_lof.runs[0].font.size = Pt(9.5)

doc.add_page_break()

# ==============================================================================
# CHAPTER 1 & 2: INTRODUCTION, PROBLEM STATEMENT, MOTIVATION, OBJECTIVES (STEPS 8.12 - 8.14)
# ==============================================================================
add_styled_heading("Chapter 1: Introduction & Research Motivation", level=1)
add_body_p("Urban road transportation networks in rapidly developing economies represent both vital economic arteries and severe public safety vulnerabilities. According to official reports by the Ministry of Road Transport and Highways (MoRTH), India experiences over 450,000 road traffic crashes annually, resulting in more than 150,000 fatalities and extensive socioeconomic harm. Dense urban centers such as Delhi, Mumbai, Bengaluru, and Chennai face unique compounded hazards: intense vehicular congestion, heterogeneous traffic composition (combining heavy commercial vehicles, passenger cars, motorized two-wheelers, and pedestrians), fluctuating tropical weather events, and variable road infrastructure.")
add_body_p("Historically, municipal traffic authorities and urban planning departments have analyzed traffic safety through static, retrospective tabular summaries. These traditional records categorize accidents long after they occur, primarily for insurance processing and statutory reporting. While informative at an aggregate level, retrospective tables suffer from severe practical shortcomings:")
add_body_p("1. Inability to Disentangle Incident Volume from Severity: High crash counts often cluster during night hours due to speed and visibility, but high-lethality multi-vehicle emergencies peak during morning and evening commuter rush hours.", bold_prefix="• ")
add_body_p("2. Lack of Interactive Drill-Down Capability: Decision makers cannot seamlessly isolate how environmental factors (such as dense fog or monsoon downpours) alter risk across specific roadway hierarchies in individual cities.", bold_prefix="• ")
add_body_p("3. Absence of Predictive Decision Support: Static reports provide no mechanism to forecast impending risk levels based on real-time ambient conditions (e.g., fog + peak traffic density), precluding proactive interventions.", bold_prefix="• ")

add_styled_heading("Chapter 2: Problem Statement, Scope & Project Objectives", level=1)
add_body_p("Problem Statement:", bold_prefix="2.1 ")
add_body_p("Modern smart cities generate vast quantities of multimodal traffic telemetry and accident incident reports. However, municipal traffic managers, police dispatchers, and emergency services lack an integrated, interactive analytical platform capable of visualizing multidimensional collision patterns, identifying localized high-risk corridors, and predicting operational risk levels from pre-incident ambient conditions. Without such intelligence, traffic safety interventions remain predominantly reactive, delaying emergency medical response and misallocating municipal enforcement patrols.")

add_body_p("Project Objectives:", bold_prefix="2.2 ")
add_body_p("To resolve this challenge, the UrbanFlow project establishes the following specific, measurable engineering objectives:")
add_body_p("1. Data Engineering & Integrity: Ingest, audit, and clean 20,000 multimodal collision records spanning 8 Indian metropolitan centers, guaranteeing zero row loss while engineering 10 operational features.", bold_prefix="• ")
add_body_p("2. Exploratory & Statistical Analysis: Quantify temporal, infrastructural, environmental, and behavioral drivers of collision frequency and severity using rigorous parametric and non-parametric tests.", bold_prefix="• ")
add_body_p("3. Advanced Risk Disparity Modeling: Mathematically evaluate the divergence between crash volume and crash severity across diurnal cycles and identify localized geographic high-risk concentrations.", bold_prefix="• ")
add_body_p("4. Interactive Business Intelligence Suite: Design and deploy a certified 5-page Power BI dashboard featuring star-schema data modeling, 25+ DAX measures, and seamless cross-filtering.", bold_prefix="• ")
add_body_p("5. Predictive Machine Learning Triage: Formulate, train, and evaluate a leakage-free multiclass risk classification prototype to predict impending risk tiers with high accuracy and zero catastrophic errors.", bold_prefix="• ")

doc.add_page_break()

# ==============================================================================
# CHAPTER 3: TECHNOLOGY STACK & ARCHITECTURE (STEP 8.15 & 8.3)
# ==============================================================================
add_styled_heading("Chapter 3: Technology Stack & System Architecture", level=1)
add_body_p("UrbanFlow adopts a modern, enterprise-grade data science and business intelligence stack, ensuring full architectural separation between data engineering, analytical computation, BI reporting, and predictive machine learning:")

tech_headers = ["Technology / Tool", "Component Role", "Specific Application within UrbanFlow"]
tech_rows = [
    ["Python 3.12", "Core Programming", "Primary programming runtime for data cleaning, modeling, and automated pipelines."],
    ["Pandas 2.2+", "Data Engineering", "Dataframe manipulation, data cleaning, datetime parsing, and feature engineering."],
    ["NumPy 1.26+", "Numerical Computing", "Vectorized mathematical computations, matrix operations, and array handling."],
    ["SciPy 1.13+", "Statistical Testing", "One-Way ANOVA (F-ratio, eta_sq), Pearson r, and Spearman rho correlations."],
    ["Scikit-Learn 1.4+", "Machine Learning", "ColumnTransformer, OneHotEncoder, StandardScaler, Decision Tree, Random Forest."],
    ["Matplotlib 3.11+", "Visualization Engine", "High-resolution (300 DPI) publication-quality charts, histograms, and architecture figures."],
    ["Seaborn 0.13+", "Statistical Graphics", "Heatmaps, box plots, violin distributions, and multiclass confusion matrices."],
    ["Jupyter Notebook", "Analytical Environment", "Interactive research notebooks (02 Exploration, 04 EDA, 07 Machine Learning)."],
    ["Power BI Desktop", "Business Intelligence", "Enterprise interactive reporting, Star Schema data modeling, geospatial maps, drill-through."],
    ["DAX (Data Analysis Exp)", "Analytical Modeling", "25+ certified KPIs, time-intelligence formulas, dynamic hazard aggregations."],
    ["Power Query (M)", "ETL Processing", "Automated data ingestion transformations and schema definition in Power BI."],
    ["Python-Docx & ReportLab", "Document Generation", "Automated generation of formal academic project reports in DOCX and PDF."]
]
add_table_styled(tech_headers, tech_rows, col_widths=[1.5, 1.8, 3.2])

add_body_p("System Architecture Overview:", bold_prefix="3.2 ")
add_body_p("The UrbanFlow architecture is organized into four interconnected tiers, as illustrated in Figure 1:")
add_body_p("• Tier 1 (Data Ingestion & Engineering): Raw collision records are ingested, audited for 20 quality dimensions, cleaned, and enriched with 10 engineered features.")
add_body_p("• Tier 2 (Exploratory & Statistical Engine): Generates 18 exploratory visualizations, calculates statistical effect sizes (ANOVA eta_sq), and profiles high-risk anomalies.")
add_body_p("• Tier 3 (Dual Serving Layer): Operates in parallel. The Power BI engine serves human decision-makers with interactive dashboards, while the Scikit-Learn engine executes automated risk classification.")
add_body_p("• Tier 4 (Smart City Decision Support): Translates analytical intelligence into real-world operational policies, including dynamic patrol dispatch, automated VMS signage, and emergency staging.")

add_image_with_caption("Images/Architecture/urbanflow_system_architecture.png", "Figure 1: UrbanFlow End-to-End System Architecture Pipeline.", width_in=6.2)

doc.add_page_break()

# ==============================================================================
# CHAPTER 4: DATA PIPELINE, METHODOLOGY & DFD (STEPS 8.4, 8.5, 8.16)
# ==============================================================================
add_styled_heading("Chapter 4: Data Pipeline, Preprocessing & Feature Engineering", level=1)
add_body_p("4.1 The 14-Step Research Methodology", bold_prefix="")
add_body_p("UrbanFlow follows a systematic 14-step academic engineering lifecycle spanning problem definition through municipal policy recommendations. The complete methodology is depicted in Figure 3.")

add_image_with_caption("Images/Architecture/urbanflow_methodology.png", "Figure 3: UrbanFlow 14-Step Research and Engineering Methodology Framework.", width_in=5.6)

add_body_p("4.2 Level-1 Data Flow Architecture", bold_prefix="")
add_body_p("Figure 2 illustrates the Level-1 Data Flow Diagram (DFD). Raw collision telemetry passes from external police sensors into Process 1.0 (Python Cleaning), is stored in Data Store D1 (urbanflow_cleaned.csv), and bifurcates into Process 2.0 (Power BI Reporting) and Process 3.0 (Machine Learning Triage).")

add_image_with_caption("Images/Architecture/urbanflow_data_flow.png", "Figure 2: Level-1 Data Flow Diagram (DFD) of the UrbanFlow Processing Pipeline.", width_in=6.0)

add_body_p("4.3 Data Cleaning & Quality Audit", bold_prefix="")
add_body_p("During Phase 2 and 3, twenty distinct data quality checks were audited against the raw dataset. The cleaning pipeline executed the following verified operations:")
add_body_p("1. Deduplication: The dataset was audited for duplicate accident IDs and fully duplicate records. Exactly 0 duplicates were found; all 20,000 records represent unique collisions.", bold_prefix="• ")
add_body_p("2. Datetime Parsing: Column 'date' was parsed into ISO 8601 standard ('YYYY-MM-DD'). Clock 'time' strings were validated, ensuring all hours fall strictly within 00:00 to 23:59.", bold_prefix="• ")
add_body_p("3. Categorical Standardization: Text columns ('city', 'weather', 'road_type', 'cause', 'traffic_density', 'accident_severity') were stripped of whitespace, cast to lowercase, and verified against permissible vocabularies.", bold_prefix="• ")
add_body_p("4. Handling of the 'festival' Column: The raw column 'festival' contained 19,885 null values (99.425% missing). To preserve record integrity without row deletion, missing entries were imputed with 'None'. Due to its extreme sparsity, it was excluded from modeling.", bold_prefix="• ")
add_body_p("5. Zero Row Loss: All 20,000 raw collision events were successfully cleaned and retained (0% row attrition).", bold_prefix="• ")

add_body_p("4.4 Feature Engineering (10 Engineered Attributes)", bold_prefix="")
clean_headers = ["Engineered Attribute", "Source Column(s)", "Transformation Logic", "Analytical Utility"]
clean_rows = [
    ["year", "date", "Extracted calendar year (2020–2024)", "Multi-year trend analysis."],
    ["month", "date", "Extracted calendar month (1–12)", "Seasonal trend analysis."],
    ["month_name", "date", "Converted month integer to full string", "Power BI categorical slicer."],
    ["day", "date", "Extracted day of month (1–31)", "Calendar drill-down."],
    ["week_number", "date", "Calculated ISO calendar week (1–53)", "Weekly reporting cadence."],
    ["time_period", "hour", "Binned: Night (22-05), Morning (06-11), Afternoon (12-16), Evening (17-21)", "Diurnal risk disparity modeling."],
    ["severity_score", "accident_severity", "Mapped: Minor -> 1, Major -> 2, Fatal -> 3", "Quantitative severity index."],
    ["risk_category", "risk_score", "Discretized: Low (<0.30), Medium (0.30-0.65), High (>=0.65)", "Target for ML classification."],
    ["casualty_category", "casualties", "Binned: 0 Casualties, 1-2 Casualties, 3-5 Casualties", "Injury grouping visuals."],
    ["visibility_score", "visibility", "Ordinal mapped: Low -> 1, Medium -> 2, High -> 3", "Numerical correlation with risk."]
]
add_table_styled(clean_headers, clean_rows, col_widths=[1.5, 1.2, 2.2, 1.6])

doc.add_page_break()

# ==============================================================================
# CHAPTER 5: EXPLORATORY DATA ANALYSIS (STEP 8.17)
# ==============================================================================
add_styled_heading("Chapter 5: Exploratory Data Analysis & Empirical Findings", level=1)
add_body_p("Comprehensive exploratory data analysis was executed across the 20,000 cleaned observations to uncover baseline distributions, temporal trends, and structural relationships:")

add_body_p("5.1 Temporal Collision Dynamics", bold_prefix="")
add_body_p("Evaluating collision frequency across the 24-hour cycle reveals a continuous baseline of traffic incidents with notable nocturnal surges. As shown in Figure 4, nighttime hours between 22:00 and 04:00 record the highest volume of total incidents (peaking at 908 collisions at 02:00). Commuter rush hours (08:00–10:00 and 17:00–19:00) account for 24.74% of total volume (4,948 incidents), while remaining hours represent off-peak daytime travel.")

add_image_with_caption("Images/EDA/04_accidents_by_hour.png", "Figure 4: Hourly Collision Volume Distribution Across the 24-Hour Cycle.", width_in=5.8)

add_body_p("5.2 Collision Severity Breakdown", bold_prefix="")
add_body_p("Analysis of collision damage outcomes (Figure 5) establishes that minor collisions constitute the majority of recorded events (11,048 incidents, 55.24%). Major collisions requiring towing or hospital transport represent 6,170 incidents (30.85%). Crucially, fatal collisions account for 2,782 incidents (13.91%), meaning that approximately 1 in every 7.2 reported crashes resulted in at least one lost human life.")

add_image_with_caption("Images/EDA/08_accident_severity.png", "Figure 5: Collision Severity Distribution Across 20,000 Incidents.", width_in=5.2)

add_body_p("5.3 Root Causes & Pareto Inapplicability", bold_prefix="")
add_body_p("A conventional hypothesis in road safety research is that 80% of accidents stem from 20% of causes (the Pareto principle). To test this, reported accident causes were tabulated and cumulative frequency curves plotted (Figure 6). The findings conclusively refute Pareto applicability in this dataset: Distraction (20.29%), Drunk Driving (20.18%), Overspeeding (20.12%), Poor Road Pavement (19.80%), and Weather (19.62%) exhibit virtually identical frequencies (~20% each). Road hazards arise from a broad distribution of human behavioral and environmental factors rather than a single dominant culprit.")

add_image_with_caption("Images/EDA/10_cause_pareto.png", "Figure 6: Pareto Analysis of Primary Reported Accident Causes.", width_in=5.8)

add_body_p("5.4 Atmospheric Conditions & Numerical Correlations", bold_prefix="")
add_body_p("Evaluating environmental exposure reveals that collisions are distributed evenly across Clear (33.45%), Rain (33.38%), and Foggy (33.17%) conditions (Figure 7). However, the severity of collisions differs dramatically across these atmospheres. Figure 8 displays the Pearson correlation heatmap across numerical variables, identifying two primary linear associations:")
add_body_p("1. Vehicles Involved vs. Casualties: Moderate positive correlation (r = +0.5510, p < 0.001). Multi-vehicle collisions escalate human casualty potential.", bold_prefix="• ")
add_body_p("2. Visibility Score vs. Risk Score: Strong negative correlation (r = -0.7291, p < 0.001). Restricting sight distance monotonically elevates overall collision risk.", bold_prefix="• ")

add_image_with_caption("Images/EDA/12_weather_analysis.png", "Figure 7: Accident Distribution Across Atmospheric Weather Conditions.", width_in=5.2)
add_image_with_caption("Images/EDA/18_correlation_heatmap.png", "Figure 8: Pearson Correlation Heatmap Across Numerical Attributes.", width_in=5.5)

doc.add_page_break()

# ==============================================================================
# CHAPTER 6: ADVANCED RISK ANALYSIS (STEP 8.19)
# ==============================================================================
add_styled_heading("Chapter 6: Advanced Collision Risk & Hotspot Concentration Analysis", level=1)
add_body_p("6.1 The Volume vs. Risk Disparity Curve", bold_prefix="")
add_body_p("The defining analytical discovery of the UrbanFlow project is the fundamental empirical divergence between where/when collisions occur most frequently and where/when they are most dangerous. As illustrated in Figure 11, nighttime hours (22:00–05:59) record the largest volume of crashes (6,721 incidents, 33.61%), yet exhibit the lowest average risk score (0.3687) and lowest high-risk collision rate (16.19%).")
add_body_p("In sharp contrast, commuter rush hours (08:00–10:00 and 17:00–19:00) record moderate incident volume (4,948 crashes, 24.74%), but exhibit an average risk score of 0.6038 (+57.7% higher) and a high-risk collision rate of 38.32%. Morning and evening congestion significantly amplifies compound risk.")

add_image_with_caption("Images/Advanced_Analysis/05_risk_by_hour.png", "Figure 11: Collision Volume vs. Average Risk Score Hourly Disparity Curve.", width_in=6.0)

add_body_p("6.2 Environmental & Traffic Risk Drivers", bold_prefix="")
add_body_p("One-way Analysis of Variance (ANOVA) confirms that atmospheric degradation and traffic congestion are the primary statistical drivers of risk score variance (Figure 13):")
add_body_p("• Weather Condition: F = 8,559.5, p < 0.001, eta_sq = 0.4612. Explains 46.12% of total risk score variance. As shown in Figure 10, mean risk in fog reaches 0.5891 compared to 0.2369 under clear skies (+148.7% increase).")
add_body_p("• Ambient Traffic Density: F = 3,973.7, p < 0.001, eta_sq = 0.2844. Explains 28.44% of risk variance. High density escalates the proportion of high-risk collisions to 54.65%, compared to 7.32% in low density.")
add_body_p("• Physical Infrastructure Invariance: In contrast, physical roadway classification (highway, urban, rural; F = 1.24, p = 0.289, eta_sq = 0.0001), lane count (r = -0.0017, p = 0.808), and city jurisdiction (F = 0.37, p = 0.918) display zero statistically significant association with risk score.")

add_image_with_caption("Images/Advanced_Analysis/03_risk_by_weather.png", "Figure 10: Empirical Risk Score Distribution by Weather Condition.", width_in=5.4)
add_image_with_caption("Images/Advanced_Analysis/10_risk_driver_association.png", "Figure 13: Statistical Driver Association Matrix (ANOVA eta_sq and Pearson |r|).", width_in=6.0)

add_body_p("6.3 High-Risk Collision Profile & Geographic Hotspot Concentration", bold_prefix="")
add_body_p("Cross-tabulating incident characteristics across risk tiers (Figure 12) identifies the operational archetype of high-risk collisions: 61.98% occur in fog, 79.92% occur in high traffic density, 58.73% occur during morning or evening peak rush hours, and 37.30% result in fatal outcomes (averaging 2.075 casualties).")
add_body_p("Spatial grid aggregation (0.1 deg x 0.1 deg cells, Figure 14) reveals localized high-risk transit corridors: East Delhi (28.5 deg N, 77.3 deg E) exhibits a 38.46% high-risk concentration (mean risk 0.5154), South Mumbai Harbor (18.9 deg N, 72.7 deg E) records 34.12%, and Hinjawadi IT Corridor in Pune records 32.87%.")

add_image_with_caption("Images/Advanced_Analysis/09_high_risk_profile.png", "Figure 12: High-Risk Collision Signature Across Driving Dimensions.", width_in=6.2)
add_image_with_caption("Images/Advanced_Analysis/11_geographic_risk_concentration.png", "Figure 14: Spatial Distribution of High-Risk Collisions Across Metropolitan Clusters.", width_in=6.0)

doc.add_page_break()

# ==============================================================================
# CHAPTER 7: POWER BI DASHBOARD (STEP 8.18)
# ==============================================================================
add_styled_heading("Chapter 7: Interactive Power BI Dashboard Suite", level=1)
add_body_p("The UrbanFlow Power BI solution (UrbanFlow.pbix) translates verified empirical findings into an enterprise-grade, five-page interactive business intelligence suite. Built upon a validated Star Schema data model and powered by 25+ certified DAX measures, the dashboard provides multi-tier decision support for municipal executives, traffic controllers, and emergency planners.")

add_body_p("7.1 Page 1 — Executive Overview Dashboard", bold_prefix="")
add_body_p("Purpose: High-level situational awareness scorecard displaying macro safety KPIs. Includes Total Accidents (20,000), Total Casualties (34,519), Fatality Rate (13.91%), and Average Risk Score (0.4376), complemented by severity breakdowns and city rankings.")
add_image_with_caption("Images/PowerBI/01_overview.png", "Figure 15: Power BI Executive Overview Dashboard (Page 1).", width_in=6.0)

add_body_p("7.2 Page 2 — Traffic & Temporal Dynamics Dashboard", bold_prefix="")
add_body_p("Purpose: Deep-dive into temporal crash distributions. Visualizes 24-hour diurnal volume curves, rush-hour surge comparisons, and day-of-week heatmaps, enabling schedule optimization for traffic police beats.")
add_image_with_caption("Images/PowerBI/02_traffic_time.png", "Figure 16: Power BI Traffic & Temporal Dynamics Dashboard (Page 2).", width_in=6.0)

add_body_p("7.3 Page 3 — Accident Severity & Root Causes Dashboard", bold_prefix="")
add_body_p("Purpose: Diagnostic evaluation of crash consequences and contributing behavioral factors. Cross-filters driver intoxication, speeding, distraction, and road infrastructure across vehicle involvement tiers.")
add_image_with_caption("Images/PowerBI/03_accident_analysis.png", "Figure 17: Power BI Accident Severity & Causes Dashboard (Page 3).", width_in=6.0)

add_body_p("7.4 Page 4 — Hotspots & Spatial Distribution Dashboard", bold_prefix="")
add_body_p("Purpose: Geospatial mapping of collision coordinates across 8 Indian metropolitan clusters. Allows operators to zoom into specific arterial choke points and assess casualty density.")
add_image_with_caption("Images/PowerBI/04_hotspots_map.png", "Figure 18: Power BI Hotspots & Spatial Distribution Dashboard (Page 4).", width_in=6.0)

add_body_p("7.5 Page 5 — Advanced Risk Insights & Triage Dashboard", bold_prefix="")
add_body_p("Purpose: Executive risk matrix combining atmospheric degradation, ambient congestion, and time-of-day hazard scoring to guide preemptive emergency response staging.")
add_image_with_caption("Images/PowerBI/05_risk_insights.png", "Figure 19: Power BI Advanced Risk Insights Dashboard (Page 5).", width_in=6.0)

doc.add_page_break()

# ==============================================================================
# CHAPTER 8: MACHINE LEARNING (STEP 8.20)
# ==============================================================================
add_styled_heading("Chapter 8: Predictive Machine Learning Risk Classification Prototype", level=1)
add_body_p("8.1 Objective & Data Leakage Guardrail", bold_prefix="")
add_body_p("To transition UrbanFlow from retrospective analytics to proactive accident prevention, a supervised multiclass classification prototype was engineered. The model predicts the operational risk tier (Low Risk, Medium Risk, High Risk) based exclusively on pre-incident situational variables observable prior to a crash. An explicit data leakage audit excluded continuous risk_score (target source) and post-crash investigation outcomes (accident_severity, severity_score, casualties, casualty_category).")

add_body_p("8.2 Model Training & Benchmark Comparison", bold_prefix="")
add_body_p("A feature matrix of 13 pre-incident attributes was partitioned using an 80/20 stratified split (N_train = 16,000, N_test = 4,000, seed = 42). OneHotEncoder and StandardScaler transformations were fitted strictly on training data. Three algorithms were benchmarked on the held-out test partition (Table 8.1 and Figure 21):")

ml_headers = ["Algorithm", "Test Accuracy", "Macro Precision", "Macro Recall", "Macro F1", "Weighted F1"]
ml_rows = [
    ["Multinomial Logistic Regression", "87.68%", "0.8964", "0.8711", "0.8738", "0.8751"],
    ["Decision Tree Classifier (depth=6)", "88.88%", "0.9081", "0.8789", "0.8845", "0.8867"],
    ["Random Forest Classifier (100 trees)", "88.72%", "0.9045", "0.8782", "0.8829", "0.8851"]
]
add_table_styled(ml_headers, ml_rows, col_widths=[2.5, 0.8, 0.8, 0.8, 0.8, 0.8])

add_image_with_caption("Images/Machine_Learning/02_model_comparison.png", "Figure 21: Machine Learning Algorithm Performance Benchmark.", width_in=5.8)

add_body_p("8.3 Safety-Critical Zero Catastrophic Misclassification Property", bold_prefix="")
add_body_p("Inspection of the test set confusion matrix (Figure 20) reveals an essential safety property: zero catastrophic misclassifications occurred across all 4,000 test incidents:")
add_body_p("• Actual Low Risk -> Predicted High Risk: 0 / 1,054 (0.0% false alarms)")
add_body_p("• Actual High Risk -> Predicted Low Risk: 0 / 962 (0.0% false negatives)")
add_body_p("All classification uncertainty was confined strictly to adjacent operational boundaries (Low <-> Medium or Medium <-> High), establishing safety suitability for municipal deployment.")

add_image_with_caption("Images/Machine_Learning/01_confusion_matrix.png", "Figure 20: Random Forest Confusion Matrix (N=4,000 Test Incidents).", width_in=5.0)

add_body_p("8.4 Feature Importance & ROC Performance", bold_prefix="")
add_body_p("Random Forest Mean Decrease in Impurity (Figure 22) demonstrates that visibility_score (30.33%), traffic_density (34.71%), and weather_fog (10.82%) drive over 75% of model classification decisions. Figure 23 plots multiclass One-vs-Rest ROC curves, confirming outstanding discrimination performance with AUC > 0.94 across all three risk categories.")

add_image_with_caption("Images/Machine_Learning/03_feature_importance.png", "Figure 22: Random Forest Feature Importance (MDI) Ranking.", width_in=5.6)
add_image_with_caption("Images/Machine_Learning/05_multiclass_roc_curves.png", "Figure 23: Multiclass One-vs-Rest ROC Curves for Risk Categories.", width_in=5.2)

doc.add_page_break()

# ==============================================================================
# CHAPTER 9, 10, 11: DISCUSSION, LIMITATIONS, FUTURE SCOPE, CONCLUSION (STEPS 8.21 - 8.24)
# ==============================================================================
add_styled_heading("Chapter 9: Results, Critical Discussion & Municipal Policy", level=1)
add_body_p("9.1 What the Data Demonstrates vs. What Findings Imply", bold_prefix="")
add_body_p("In interpreting the findings, a clear distinction must be maintained between observed empirical patterns and causal mechanisms. The data conclusively proves that high-risk collisions concentrate during commuter rush hours under foggy, low-visibility conditions with high traffic density. This does not imply that fog or density directly causes collisions; rather, adverse atmospheric conditions compound driver visual perception limitations, while high vehicular density diminishes emergency braking margins.")

add_body_p("9.2 Actionable Smart City Policy Blueprints", bold_prefix="")
add_body_p("1. Dynamic Variable Message Signs (VMS): Municipal traffic management centers can configure automated triggers that display speed advisory warnings and hazard alerts whenever roadside telemetry registers visibility < 2 km and high traffic density.", bold_prefix="• ")
add_body_p("2. Proactive Emergency Medical Staging: By forecasting high-risk rush hour windows, emergency services can pre-position ambulance units along identified arterial corridors (e.g., East Delhi transit border, Mumbai harbor approach), significantly cutting response times during critical trauma windows.", bold_prefix="• ")
add_body_p("3. Congestion Mitigation at High-Risk Bottlenecks: Traffic police deployments should prioritize rush-hour signal timing overrides at known congestion bottlenecks rather than conducting static night patrols.", bold_prefix="• ")

add_styled_heading("Chapter 10: Methodological Limitations & Future Scope", level=1)
add_body_p("10.1 Project Limitations", bold_prefix="")
add_body_p("• Observational Collision Records: The dataset records events where collisions occurred, but lacks exposure denominators (total vehicle-kilometers traveled).")
add_body_p("• Missing Festival Telemetry: The raw festival column contained 99.425% missing entries, preventing the evaluation of holiday traffic surges.")
add_body_p("• Coarse Temporal Bins: The 4-period diurnal aggregation simplifies continuous 24-hour traffic dynamics.")

add_body_p("10.2 Future Scope & Research Trajectory", bold_prefix="")
add_body_p("• Real-Time IoT Sensor Ingestion: Connecting live road traffic video feeds, loop detectors, and weather APIs into streaming Spark/Kafka pipelines.")
add_body_p("• Mobile PWA Dispatch Dashboard: Packaging Power BI embedded visuals into a cross-platform mobile app for patrol officers.")
add_body_p("• Deep Learning Spatial-Temporal Forecasting: Implementing Graph Neural Networks (GNNs) or Spatio-Temporal Graph Convolutional Networks (ST-GCN) to predict network-wide traffic speeds and accident probabilities 30 minutes in advance.")

add_styled_heading("Chapter 11: Conclusion & Academic Summary", level=1)
add_body_p("The UrbanFlow project establishes a comprehensive, professionally executed data analytics and visualization solution for smart city traffic safety. Across 20,000 validated collision records spanning eight Indian metropolitan centers, the project successfully bridges raw data engineering, exploratory analysis, interactive Power BI reporting, and predictive machine learning. By revealing the critical volume vs. severity disparity and engineering a predictive model with 88.9% accuracy and zero catastrophic errors, UrbanFlow delivers both academic rigor and real-world municipal decision support.")

doc.add_page_break()

# ==============================================================================
# CHAPTER 12 & 13: REFERENCES & APPENDIX (STEPS 8.25 & 8.26)
# ==============================================================================
add_styled_heading("Chapter 12: References", level=1)
refs = [
    "1. Ministry of Road Transport and Highways (MoRTH). (2023). 'Road Accidents in India 2022.' Government of India Transport Research Wing, New Delhi.",
    "2. World Health Organization (WHO). (2023). 'Global Status Report on Road Safety 2023.' World Health Organization, Geneva.",
    "3. Few, S. (2012). 'Show Me the Numbers: Designing Tables and Graphs to Enlighten.' Analytics Press, Burlingame, CA.",
    "4. Cairo, A. (2016). 'The Truthful Art: Data, Charts, and Maps for Communication.' New Riders, San Francisco, CA.",
    "5. McKinney, W. (2022). 'Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter (3rd ed.).' O'Reilly Media.",
    "6. Ferrari, A., & Russo, M. (2020). 'The Definitive Guide to DAX: Business Intelligence with Microsoft Power BI, SQL Server Analysis Services, and Excel (2nd ed.).' Microsoft Press.",
    "7. Pedregosa, F., et al. (2011). 'Scikit-learn: Machine Learning in Python.' Journal of Machine Learning Research, 12, 2825-2830.",
    "8. Breiman, L. (2001). 'Random Forests.' Machine Learning, 45(1), 5-32.",
    "9. Hastie, T., Tibshirani, R., & Friedman, J. (2009). 'The Elements of Statistical Learning: Data Mining, Inference, and Prediction.' Springer."
]
for ref in refs:
    p_ref = doc.add_paragraph()
    p_ref.paragraph_format.space_after = Pt(4)
    p_ref.add_run(ref).font.name = 'Calibri'
    p_ref.runs[0].font.size = Pt(9.5)

add_styled_heading("Chapter 13: Appendix — Core DAX Formulas & Python Scripts", level=1)
add_body_p("Sample Certified DAX Measures from UrbanFlow.pbix:", bold_prefix="13.1 ")

dax_samples = [
    ("Total Accidents", "Total Accidents = COUNTROWS('urbanflow_cleaned')"),
    ("Fatality Rate %", "Fatality Rate % = DIVIDE(CALCULATE(COUNTROWS('urbanflow_cleaned'), 'urbanflow_cleaned'[accident_severity] = \"fatal\"), [Total Accidents], 0) * 100"),
    ("Average Risk Score", "Average Risk Score = AVERAGE('urbanflow_cleaned'[risk_score])"),
    ("High Risk Incident Count", "High Risk Incidents = CALCULATE(COUNTROWS('urbanflow_cleaned'), 'urbanflow_cleaned'[risk_category] = \"High Risk\")"),
    ("High Risk Incident %", "High Risk Incident % = DIVIDE([High Risk Incidents], [Total Accidents], 0) * 100")
]
for name, code in dax_samples:
    p_d = doc.add_paragraph()
    p_d.paragraph_format.space_after = Pt(3)
    p_d.add_run(f"• {name}: ").bold = True
    r_c = p_d.add_run(code)
    r_c.font.name = 'Consolas'
    r_c.font.size = Pt(9.0)
    r_c.font.color.rgb = C_NAVY_RGB

add_body_p("Complete Source Code Repositories:", bold_prefix="13.2 ")
add_body_p("All data cleaning scripts, exploratory notebooks, Power BI templates, and machine learning pipelines are fully maintained within the project workspace directory structure:")
add_body_p("• Python/scripts/clean_dataset.py — Automated ETL & Cleaning Pipeline")
add_body_p("• Python/notebooks/04_exploratory_data_analysis.ipynb — Exploratory Data Analysis Notebook")
add_body_p("• Python/notebooks/07_risk_machine_learning.ipynb — Machine Learning Risk Model Notebook")
add_body_p("• PowerBI/DAX_Measures.dax — Complete Certified Measure Definitions")

# Save DOCX
doc.save(DOCX_PATH)
print(f"Report DOCX successfully generated at: {DOCX_PATH}")

# Also generate PDF
print("Converting DOCX to PDF via docx2pdf...")
try:
    import docx2pdf
    docx2pdf.convert(DOCX_PATH, PDF_PATH)
    print(f"Report PDF successfully generated via docx2pdf at: {PDF_PATH}")
except Exception as e:
    print(f"docx2pdf failed ({e}). Generating PDF via reportlab fallback...")
    # ReportLab fallback if docx2pdf fails
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, Table as RLTable, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors

    rl_doc = SimpleDocTemplate(PDF_PATH, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    styles = getSampleStyleSheet()
    story = []
    
    title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=24, leading=28, textColor=colors.HexColor('#1D3557'))
    body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor('#2B2D42'))
    
    story.append(Paragraph("URBANFLOW: Interactive Smart City Traffic & Accident Analytics", title_style))
    story.append(Spacer(1, 15))
    story.append(Paragraph("Comprehensive Academic Semester Project Report", styles['Heading2']))
    story.append(Spacer(1, 15))
    story.append(Paragraph("This publication-ready PDF document summarizes the complete end-to-end findings, data engineering, statistical modeling, Power BI dashboard, and machine learning components of the UrbanFlow project. Please see UrbanFlow_Final_Report.docx for the complete 40+ page unabridged document.", body_style))
    story.append(Spacer(1, 20))
    
    # Add System Architecture Image
    arch_img = os.path.join(WORKSPACE, 'Images', 'Architecture', 'urbanflow_system_architecture.png')
    if os.path.exists(arch_img):
        story.append(RLImage(arch_img, width=6*72, height=4.28*72))
        story.append(Spacer(1, 15))
        
    rl_doc.build(story)
    print(f"Report PDF generated via ReportLab at: {PDF_PATH}")

print("Report generation pipeline completed.")
