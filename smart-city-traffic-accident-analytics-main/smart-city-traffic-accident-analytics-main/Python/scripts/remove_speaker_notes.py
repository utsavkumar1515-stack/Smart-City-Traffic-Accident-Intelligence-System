import os
import sys
import pptx
from pptx import Presentation
import zipfile
import shutil

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr.encoding != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8')

WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PRES_DIR = os.path.join(WORKSPACE, 'Presentation')
PPTX_PATH = os.path.join(PRES_DIR, 'UrbanFlow_Final_Presentation.pptx')
PDF_PATH = os.path.join(PRES_DIR, 'UrbanFlow_Final_Presentation.pdf')
SUBMISSION_DIR = os.path.join(WORKSPACE, 'UrbanFlow_Final_Submission')
ZIP_PATH = os.path.join(WORKSPACE, 'UrbanFlow_Final_Submission.zip')

print(f"Loading presentation: {PPTX_PATH}")
prs = Presentation(PPTX_PATH)

# Remove all speaker notes from every slide
print("Removing all speaker notes from all slides...")
for i, slide in enumerate(prs.slides):
    if slide.has_notes_slide:
        notes_tf = slide.notes_slide.notes_text_frame
        notes_tf.text = ""
        # Also clear any additional paragraphs in notes_text_frame
        while len(notes_tf.paragraphs) > 1:
            p_elem = notes_tf.paragraphs[-1]._p
            p_elem.getparent().remove(p_elem)
        if len(notes_tf.paragraphs) == 1:
            notes_tf.paragraphs[0].text = ""

# Save corrected PPTX
prs.save(PPTX_PATH)
print(f"Saved corrected presentation without speaker notes: {PPTX_PATH}")

# Verification Step: Verify that EVERY slide has an empty notes section
print("\n--- VERIFICATION: Checking notes on each slide ---")
prs_verify = Presentation(PPTX_PATH)
all_empty = True
for i, slide in enumerate(prs_verify.slides):
    notes_text = ""
    if slide.has_notes_slide:
        notes_text = slide.notes_slide.notes_text_frame.text.strip()
    print(f"Slide {i+1:>2}: Notes length = {len(notes_text)} characters. {'[EMPTY - OK]' if len(notes_text) == 0 else '[ERROR - NOT EMPTY]'}")
    if len(notes_text) != 0:
        all_empty = False

if all_empty:
    print("SUCCESS: 100% of slides have completely EMPTY speaker notes!")
else:
    raise ValueError("ERROR: Some slides still contain speaker notes!")

# Re-export to PDF via PowerPoint COM
print("\nRe-exporting presentation to PDF via PowerPoint COM...")
import win32com.client
ppt_app = win32com.client.Dispatch("PowerPoint.Application")
deck = ppt_app.Presentations.Open(PPTX_PATH, True, False, False)
# Format 32 = ppSaveAsPDF
deck.SaveAs(PDF_PATH, 32)
deck.Close()
ppt_app.Quit()
print(f"Re-exported PDF successfully to: {PDF_PATH}")

# Replace presentation files in UrbanFlow_Final_Submission/
print("\nReplacing presentation files in UrbanFlow_Final_Submission/...")
sub_pres_dir = os.path.join(SUBMISSION_DIR, 'Presentation')
os.makedirs(sub_pres_dir, exist_ok=True)
shutil.copy2(PPTX_PATH, sub_pres_dir)
shutil.copy2(PDF_PATH, sub_pres_dir)
print(f"Updated presentation files in {sub_pres_dir}")

# Regenerate UrbanFlow_Final_Submission.zip
print(f"\nRegenerating ZIP archive: {ZIP_PATH}...")
if os.path.exists(ZIP_PATH):
    os.remove(ZIP_PATH)

with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(SUBMISSION_DIR):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, os.path.dirname(SUBMISSION_DIR))
            zipf.write(full_path, rel_path)

zip_size_mb = os.path.getsize(ZIP_PATH) / (1024 * 1024)
print(f"Regenerated ZIP size: {zip_size_mb:.2f} MB")

# Validate the ZIP
print("\nValidating ZIP archive integrity...")
with zipfile.ZipFile(ZIP_PATH, 'r') as zipf:
    bad_file = zipf.testzip()
    namelist = zipf.namelist()
    if bad_file is None:
        print(f"ZIP Validation PASS! Exactly {len(namelist)} files cleanly packaged.")
    else:
        raise ValueError(f"ZIP validation error on file: {bad_file}")

print("\nAll correction steps completed successfully!")
