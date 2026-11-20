import os
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, BoxStyle

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')

WORKSPACE = r'c:\Users\thaku\Desktop\🚦 Smart City Traffic'
ARCH_DIR = os.path.join(WORKSPACE, 'Images', 'Architecture')
os.makedirs(ARCH_DIR, exist_ok=True)

# Aesthetics
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['figure.dpi'] = 300

# Color Palette
C_NAVY = '#1D3557'
C_BLUE = '#457B9D'
C_TEAL = '#2A9D8F'
C_AMBER = '#F4A261'
C_CORAL = '#E63946'
C_DARK = '#2B2D42'
C_LIGHT = '#F8F9FA'
C_BORDER = '#343A40'

# ==============================================================================
# DIAGRAM 1: URBANFLOW SYSTEM ARCHITECTURE (urbanflow_system_architecture.png)
# ==============================================================================
print("Generating Diagram 1: System Architecture...")
fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Title & Header
ax.text(50, 96, "UrbanFlow: End-to-End System Architecture", ha='center', va='center', fontsize=18, fontweight='bold', color=C_NAVY)
ax.text(50, 93, "Interactive Smart City Traffic & Accident Analytics Architecture Pipeline", ha='center', va='center', fontsize=12, color='#6C757D')

# Function to draw a styled tier container
def draw_tier(y_bottom, height, title, color_bg, border_color):
    p = FancyBboxPatch((4, y_bottom), 92, height, boxstyle="round,pad=1", ec=border_color, fc=color_bg, lw=1.5, alpha=0.15)
    ax.add_patch(p)
    ax.text(6, y_bottom + height - 2.5, title.upper(), fontsize=10, fontweight='bold', color=border_color)

# Function to draw process nodes
def draw_node(x, y, w, h, text, subtext, color_fill, text_color='white'):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.8", ec=C_BORDER, fc=color_fill, lw=1.2)
    ax.add_patch(p)
    ax.text(x + w/2, y + h/2 + (1.0 if subtext else 0), text, ha='center', va='center', fontsize=9.5, fontweight='bold', color=text_color)
    if subtext:
        ax.text(x + w/2, y + h/2 - 1.8, subtext, ha='center', va='center', fontsize=7.5, color=text_color, alpha=0.9)

# Arrow helper
def draw_arrow(x1, y1, x2, y2, color=C_DARK, style='simple', lw=1.5):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color=color, lw=lw, shrinkA=3, shrinkB=3))

# Tier 1: Data Ingestion & Engineering (y: 73 to 89)
draw_tier(73, 16, "Tier 1: Data Ingestion & Feature Engineering (Python / Pandas)", C_BLUE, C_NAVY)
draw_node(6, 75.5, 18, 9, "Raw Dataset", "indian_roads_dataset.csv\n(20,000 × 24 cols)", C_NAVY)
draw_node(28, 75.5, 18, 9, "Data Cleaning", "0 Lost Rows, Type Cast\nOutlier & Anomaly Audit", C_BLUE)
draw_node(50, 75.5, 18, 9, "Feature Engineering", "10 Engineered Features\n(Risk, Severity, Time)", C_TEAL)
draw_node(72, 75.5, 20, 9, "Cleaned Dataset", "urbanflow_cleaned.csv\n(20,000 × 34 cols)", C_DARK)

draw_arrow(24, 80, 28, 80)
draw_arrow(46, 80, 50, 80)
draw_arrow(68, 80, 72, 80)

# Tier 2: Analytical & Statistical Engine (y: 52 to 68)
draw_tier(52, 16, "Tier 2: Exploratory & Statistical Risk Analysis", C_TEAL, C_TEAL)
draw_node(6, 54.5, 20, 9, "Exploratory EDA", "Temporal, Severity, Cause\n(18 High-DPI Visuals)", C_NAVY)
draw_node(30, 54.5, 20, 9, "Statistical Testing", "Pearson r, Spearman rho\nANOVA F & eta_sq Effect", C_BLUE)
draw_node(54, 54.5, 20, 9, "Risk Analysis", "Volume vs Severity Gap\nNight vs Peak Contrast", C_CORAL)
draw_node(78, 54.5, 16, 9, "Hotspot Grid", "0.1 deg Concentration\nSpatial Aggregation", C_AMBER)

draw_arrow(82, 75.5, 16, 63.5) # From Cleaned dataset down to EDA
draw_arrow(26, 59, 30, 59)
draw_arrow(50, 59, 54, 59)
draw_arrow(74, 59, 78, 59)

# Tier 3: Business Intelligence & Machine Learning (y: 28 to 47)
draw_tier(28, 19, "Tier 3: Dual Serving Engine (Power BI & Machine Learning)", C_AMBER, C_AMBER)
# Power BI Branch (Left)
draw_node(8, 30.5, 38, 12.5, "Interactive Power BI Dashboard", "5 Specialized Pages (Overview, Time, Severity, Hotspots, Risk)\n25+ DAX Measures | Star Schema Data Model", C_NAVY)
# ML Branch (Right)
draw_node(54, 30.5, 38, 12.5, "Predictive Machine Learning Engine", "Multiclass Risk Classifier (Low, Medium, High)\nZero Catastrophic Errors | 88.9% Acc | 0.885 F1", C_CORAL)

draw_arrow(40, 54.5, 27, 43) # Down to Power BI
draw_arrow(64, 54.5, 73, 43) # Down to ML

# Tier 4: Smart City Decision Support (y: 6 to 23)
draw_tier(6, 17, "Tier 4: Smart City Decision Support & Operational Outcomes", C_CORAL, C_CORAL)
draw_node(8, 8.5, 26, 11, "Preemptive Police Patrols", "Dynamic beat scheduling\nduring high-risk rush hours", C_BLUE)
draw_node(37, 8.5, 26, 11, "Automated VMS Alerts", "Dynamic speed & hazard\nwarnings in dense fog", C_AMBER)
draw_node(66, 8.5, 26, 11, "EMS Strategic Staging", "Ambulance pre-positioning\nnear high-risk transit grids", C_CORAL)

draw_arrow(27, 30.5, 21, 19.5)
draw_arrow(50, 30.5, 50, 19.5)
draw_arrow(73, 30.5, 79, 19.5)

plt.tight_layout()
fig1_path = os.path.join(ARCH_DIR, 'urbanflow_system_architecture.png')
plt.savefig(fig1_path, dpi=300)
plt.close()
print("Saved:", fig1_path)

# ==============================================================================
# DIAGRAM 2: DATA FLOW DIAGRAM (urbanflow_data_flow.png)
# ==============================================================================
print("Generating Diagram 2: Data Flow Diagram...")
fig, ax = plt.subplots(figsize=(13, 8))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

ax.text(50, 96, "UrbanFlow: Data Flow Diagram (DFD Level-1)", ha='center', va='center', fontsize=18, fontweight='bold', color=C_NAVY)
ax.text(50, 92.5, "Information Transformation from Raw Telemetry to Operational Action", ha='center', va='center', fontsize=11.5, color='#6C757D')

# External Entities (Squares)
def draw_entity(x, y, w, h, text, color=C_NAVY):
    p = patches.Rectangle((x, y), w, h, ec=C_BORDER, fc=color, lw=1.5)
    ax.add_patch(p)
    ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=9.5, fontweight='bold', color='white')

# Processes (Circles/Rounded Rectangles)
def draw_process(x, y, w, h, num, text, color=C_BLUE):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=1", ec=C_BORDER, fc=color, lw=1.2)
    ax.add_patch(p)
    ax.text(x + w/2, y + h/2 + 2, f"[{num}]", ha='center', va='center', fontsize=8, fontweight='bold', color='yellow')
    ax.text(x + w/2, y + h/2 - 1.5, text, ha='center', va='center', fontsize=8.5, fontweight='bold', color='white')

# Data Stores (Open Rectangle)
def draw_datastore(x, y, w, h, id_str, text):
    # Top and bottom lines
    ax.plot([x, x + w], [y + h, y + h], color=C_BORDER, lw=1.5)
    ax.plot([x, x + w], [y, y], color=C_BORDER, lw=1.5)
    ax.plot([x, x], [y, y + h], color=C_BORDER, lw=1.5)
    p = patches.Rectangle((x, y), w, h, fc='#E9ECEF', alpha=0.5)
    ax.add_patch(p)
    ax.text(x + 3, y + h/2, id_str, ha='left', va='center', fontsize=8.5, fontweight='bold', color=C_NAVY)
    ax.text(x + w/2 + 3, y + h/2, text, ha='center', va='center', fontsize=8.5, fontweight='bold', color=C_DARK)

# Layout DFD Elements
# 1. Source Entity
draw_entity(4, 70, 16, 12, "Traffic Police &\nMunicipal Sensors\n(Raw Ingestion)")

# 2. Process 1.0: Cleaning & Feature Engineering
draw_process(26, 68.5, 20, 15, "1.0", "Data Cleaning &\nFeature Engineering\n(Python Script)", C_NAVY)

# 3. Data Store D1: Cleaned Data
draw_datastore(54, 71, 24, 10, "D1", "urbanflow_cleaned.csv\n(34 Columns)")

# 4. Process 2.0: Business Intelligence (Power BI)
draw_process(18, 38, 24, 15, "2.0", "DAX Modeling &\nInteractive Reporting\n(Power BI Service)", C_TEAL)

# 5. Process 3.0: Machine Learning Pipeline
draw_process(58, 38, 24, 15, "3.0", "Pre-Incident ML\nTriage Classification\n(Scikit-Learn)", C_CORAL)

# 6. Dashboard Sink
draw_entity(18, 10, 24, 14, "UrbanFlow BI Dashboard\n(5 Executive Pages)", C_NAVY)

# 7. Action Engine Sink
draw_entity(58, 10, 24, 14, "Smart City Action Engine\n(Alerts, Staging, Patrols)", C_DARK)

# 8. Data Flow Arrows & Labels
def draw_flow(x1, y1, x2, y2, label="", rad=0.0):
    connectionstyle = f"arc3,rad={rad}" if rad != 0.0 else "arc3,rad=0"
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color=C_DARK, lw=1.5, shrinkA=3, shrinkB=3, connectionstyle=connectionstyle))
    if label:
        mx, my = (x1 + x2)/2, (y1 + y2)/2
        ax.text(mx, my + 1.5, label, fontsize=7.5, ha='center', va='bottom', bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8, ec='none'))

draw_flow(20, 76, 26, 76, "Raw CSV Records")
draw_flow(46, 76, 54, 76, "Validated Data")
draw_flow(66, 71, 30, 53, "Import / Refresh", rad=0.15)
draw_flow(66, 71, 70, 53, "Pre-Incident Features", rad=-0.1)
draw_flow(30, 38, 30, 24, "Visual Analytics")
draw_flow(70, 38, 70, 24, "Triage Flags")

plt.tight_layout()
fig2_path = os.path.join(ARCH_DIR, 'urbanflow_data_flow.png')
plt.savefig(fig2_path, dpi=300)
plt.close()
print("Saved:", fig2_path)

# ==============================================================================
# DIAGRAM 3: METHODOLOGY FLOWCHART (urbanflow_methodology.png)
# ==============================================================================
print("Generating Diagram 3: Methodology Flowchart...")
fig, ax = plt.subplots(figsize=(11, 14))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

ax.text(50, 98, "UrbanFlow: 14-Step Research & Engineering Methodology", ha='center', va='center', fontsize=16, fontweight='bold', color=C_NAVY)
ax.text(50, 95.5, "Systematic End-to-End Implementation Framework", ha='center', va='center', fontsize=11, color='#6C757D')

steps = [
    ("1. Problem Definition", "Traffic fatalities, congestion, and need for interactive visual decision support", C_NAVY),
    ("2. Data Collection", "Ingestion of 20,000 multimodal collision records spanning 8 Indian cities", C_NAVY),
    ("3. Data Understanding", "Inspection of 24 schema attributes, data types, and initial distribution audit", C_BLUE),
    ("4. Data Cleaning", "Zero row loss, datetime parsing, datatype casting, and categorical normalization", C_BLUE),
    ("5. Feature Engineering", "Derivation of 10 features: risk categories, time periods, severity indices", C_TEAL),
    ("6. Exploratory Data Analysis", "Temporal dynamics, collision severity, root cause Pareto, and city distributions", C_TEAL),
    ("7. Visualization Methodology", "Creation of 18 high-resolution analytical charts applying visual encoding best practices", C_BLUE),
    ("8. Geographic Analysis", "Spatial coordinate bounding and 0.1 degree grid concentration assessment", C_AMBER),
    ("9. Advanced Risk Analysis", "Disclosing Volume vs. Risk disparity, ANOVA effect sizes, and high-risk signatures", C_CORAL),
    ("10. Power BI Dashboard Build", "5-page interactive report, Star Schema, 25+ DAX KPIs, and dynamic filters", C_NAVY),
    ("11. Machine Learning Prototype", "Pre-incident multiclass risk triage with zero catastrophic misclassifications", C_CORAL),
    ("12. Model & Pipeline Evaluation", "Accuracy (88.9%), Macro F1 (0.885), cross-validation, and leakage guardrail checks", C_BLUE),
    ("13. Empirical Findings Synthesis", "Verification that atmospheric and density factors dominate physical road geometry", C_TEAL),
    ("14. Conclusion & Recommendations", "Actionable smart city blueprints: automated VMS warning triggers and EMS staging", C_NAVY)
]

y_start = 91
box_height = 4.2
spacing = 6.2

for i, (title, desc, color) in enumerate(steps):
    y = y_start - i * spacing
    
    # Step Number circle
    c = plt.Circle((12, y + box_height/2), 2.2, color=color, ec=C_BORDER, lw=1.2)
    ax.add_patch(c)
    ax.text(12, y + box_height/2, str(i+1), color='white', fontweight='bold', fontsize=9.5, ha='center', va='center')
    
    # Text box
    p = FancyBboxPatch((17, y), 75, box_height, boxstyle="round,pad=0.6", ec=C_BORDER, fc='#F8F9FA', lw=1.1)
    ax.add_patch(p)
    ax.text(19, y + box_height/2 + 0.9, title, color=color, fontweight='bold', fontsize=9.5, va='center')
    ax.text(19, y + box_height/2 - 1.1, desc, color=C_DARK, fontsize=8, va='center')
    
    # Connecting arrow (except last)
    if i < len(steps) - 1:
        y_next = y - spacing
        ax.annotate('', xy=(12, y), xytext=(12, y - (spacing - box_height)),
                    arrowprops=dict(arrowstyle="<-", color='#ADB5BD', lw=1.8, shrinkA=0, shrinkB=0))

plt.tight_layout()
fig3_path = os.path.join(ARCH_DIR, 'urbanflow_methodology.png')
plt.savefig(fig3_path, dpi=300)
plt.close()
print("Saved:", fig3_path)
print("All architecture diagrams successfully generated.")
