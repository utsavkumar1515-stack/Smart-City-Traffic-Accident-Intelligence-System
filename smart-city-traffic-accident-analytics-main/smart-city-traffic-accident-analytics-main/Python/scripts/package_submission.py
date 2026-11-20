import os
import sys
import shutil
import zipfile

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')

# Dynamically resolve workspace root
WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DEST_DIR = os.path.join(WORKSPACE, 'UrbanFlow_Final_Submission')
ZIP_PATH = os.path.join(WORKSPACE, 'UrbanFlow_Final_Submission.zip')

# Clean existing destination if any
if os.path.exists(DEST_DIR):
    shutil.rmtree(DEST_DIR)
os.makedirs(DEST_DIR, exist_ok=True)

print(f"Assembling UrbanFlow Final Submission Package in: {DEST_DIR}...")

# 1. Dataset (Cleaned and Raw)
dst_dataset = os.path.join(DEST_DIR, 'Dataset')
os.makedirs(os.path.join(dst_dataset, 'raw'), exist_ok=True)
os.makedirs(os.path.join(dst_dataset, 'cleaned'), exist_ok=True)

shutil.copy2(os.path.join(WORKSPACE, 'Dataset', 'raw', 'indian_roads_dataset.csv'), os.path.join(dst_dataset, 'raw'))
shutil.copy2(os.path.join(WORKSPACE, 'Dataset', 'cleaned', 'urbanflow_cleaned.csv'), os.path.join(dst_dataset, 'cleaned'))

# 2. Python (Notebooks and Key Scripts)
dst_python = os.path.join(DEST_DIR, 'Python')
os.makedirs(os.path.join(dst_python, 'notebooks'), exist_ok=True)
os.makedirs(os.path.join(dst_python, 'scripts'), exist_ok=True)

for nb in ['02_data_exploration.ipynb', '04_exploratory_data_analysis.ipynb', '07_risk_machine_learning.ipynb']:
    src = os.path.join(WORKSPACE, 'Python', 'notebooks', nb)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(dst_python, 'notebooks'))

for sc in ['clean_dataset.py', 'generate_phase7_artifacts.py', 'generate_architecture_diagrams.py', 'build_final_report.py', 'build_final_presentation.py']:
    src = os.path.join(WORKSPACE, 'Python', 'scripts', sc)
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(dst_python, 'scripts'))

# 3. Power BI
dst_pbi = os.path.join(DEST_DIR, 'PowerBI')
os.makedirs(dst_pbi, exist_ok=True)
shutil.copy2(os.path.join(WORKSPACE, 'PowerBI', 'UrbanFlow.pbix'), dst_pbi)
shutil.copy2(os.path.join(WORKSPACE, 'PowerBI', 'DAX_Measures.dax'), dst_pbi)
shutil.copy2(os.path.join(WORKSPACE, 'PowerBI', 'PowerQuery_Transformations.m'), dst_pbi)
shutil.copy2(os.path.join(WORKSPACE, 'PowerBI', 'urbanflow_theme.json'), dst_pbi)
shutil.copy2(os.path.join(WORKSPACE, 'PowerBI', 'PowerBI_Dashboard_Guide.md'), dst_pbi)

# 4. Images (Architecture, Final, EDA, PowerBI, Advanced_Analysis, Machine_Learning)
dst_img = os.path.join(DEST_DIR, 'Images')
for sub in ['Architecture', 'Final', 'EDA', 'PowerBI', 'Advanced_Analysis', 'Machine_Learning']:
    src_sub = os.path.join(WORKSPACE, 'Images', sub)
    if os.path.exists(src_sub):
        shutil.copytree(src_sub, os.path.join(dst_img, sub))

# 5. Documentation
dst_doc = os.path.join(DEST_DIR, 'Documentation')
os.makedirs(dst_doc, exist_ok=True)
for doc_file in os.listdir(os.path.join(WORKSPACE, 'Documentation')):
    if doc_file.endswith('.md'):
        shutil.copy2(os.path.join(WORKSPACE, 'Documentation', doc_file), dst_doc)

# 6. Report
dst_rep = os.path.join(DEST_DIR, 'Report')
os.makedirs(dst_rep, exist_ok=True)
for rep_file in ['UrbanFlow_Final_Report.docx', 'UrbanFlow_Final_Report.pdf', 'Project_Report.md']:
    src = os.path.join(WORKSPACE, 'Report', rep_file)
    if os.path.exists(src):
        shutil.copy2(src, dst_rep)

# 7. Presentation
dst_pres = os.path.join(DEST_DIR, 'Presentation')
os.makedirs(dst_pres, exist_ok=True)
for pres_file in ['UrbanFlow_Final_Presentation.pptx', 'UrbanFlow_Final_Presentation.pdf']:
    src = os.path.join(WORKSPACE, 'Presentation', pres_file)
    if os.path.exists(src):
        shutil.copy2(src, dst_pres)

# 8. README.md
shutil.copy2(os.path.join(WORKSPACE, 'README.md'), DEST_DIR)

print("Final submission folder successfully assembled at:", DEST_DIR)

# 9. Create ZIP archive
print("Compressing ZIP package:", ZIP_PATH)
if os.path.exists(ZIP_PATH):
    os.remove(ZIP_PATH)

with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(DEST_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, os.path.dirname(DEST_DIR))
            zipf.write(full_path, rel_path)

zip_size_mb = os.path.getsize(ZIP_PATH) / (1024 * 1024)
print(f"ZIP package created successfully! Size: {zip_size_mb:.2f} MB")

# Verify ZIP
print("Verifying ZIP integrity...")
with zipfile.ZipFile(ZIP_PATH, 'r') as zipf:
    bad_file = zipf.testzip()
    namelist = zipf.namelist()
    if bad_file is None:
        print(f"ZIP Integrity 100% Verified! Exactly {len(namelist)} files packaged cleanly.")
    else:
        print(f"ZIP Error detected in file: {bad_file}")
