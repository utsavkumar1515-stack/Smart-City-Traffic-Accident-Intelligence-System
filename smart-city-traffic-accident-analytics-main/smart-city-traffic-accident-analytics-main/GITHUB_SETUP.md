# UrbanFlow — GitHub Setup Guide

Git is not currently installed on this machine. Follow these steps to publish UrbanFlow to GitHub.

---

## Step 1 — Install Git

1. Go to [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. Download the **64-bit** installer and run it (keep all defaults)
3. Open a **new** PowerShell window after installation to pick up the updated PATH

Verify:
```powershell
git --version
# git version 2.x.x.windows.x
```

---

## Step 2 — Create a GitHub Repository

1. Go to [https://github.com/new](https://github.com/new)
2. Set:
   - **Repository name**: `UrbanFlow-Smart-City-Traffic-Analytics`
   - **Description**: `Smart City Traffic & Accident Analytics — 20,000 records, Power BI dashboard, Python EDA, ML classification (88.88% accuracy)`
   - **Visibility**: Public (recommended for CV/LinkedIn exposure)
   - **Do NOT** check "Add a README file" (the project already has one)
3. Click **Create repository**
4. Copy the repository URL (e.g. `https://github.com/YOUR_USERNAME/UrbanFlow-Smart-City-Traffic-Analytics.git`)

---

## Step 3 — Initialize and Push from PowerShell

Open PowerShell and run these commands from the project root:

```powershell
cd "C:\Users\thaku\Desktop\Smart City Traffic and Accident Analytics"

# Initialize git
git init
git config user.email "your@email.com"
git config user.name "Your Name"

# Add all files
git add .

# First commit
git commit -m "feat: complete UrbanFlow Smart City Traffic Analytics project

- 20,000 accident records across 8 Indian cities
- Phase 1-9 complete: data cleaning, EDA, statistical analysis, ML, Power BI
- Random Forest classifier: 88.88% accuracy, zero catastrophic errors
- 34 engineered features, advanced risk analysis
- Full report, presentation, and submission package"

# Link to GitHub remote
git remote add origin https://github.com/YOUR_USERNAME/UrbanFlow-Smart-City-Traffic-Analytics.git
git branch -M main

# Push
git push -u origin main
```

> **Note**: GitHub will prompt for authentication. Use your GitHub username and a [Personal Access Token](https://github.com/settings/tokens) (not your password) when prompted.

---

## Step 4 — Verify on GitHub

After pushing:
1. Visit your repository at `https://github.com/YOUR_USERNAME/UrbanFlow-Smart-City-Traffic-Analytics`
2. The `README.md` will render automatically as the homepage
3. Verify all folders are visible: `Dataset/`, `Python/`, `PowerBI/`, `Report/`, `Presentation/`, `Documentation/`, `Images/`

---

## Step 5 — Update README Badges

After the repo is live, update the badge URLs in [`README.md`](../README.md):

Replace the placeholder badge URLs (if any) with your actual GitHub repo URL:

```markdown
[![GitHub](https://img.shields.io/badge/GitHub-UrbanFlow-blue?logo=github)](https://github.com/YOUR_USERNAME/UrbanFlow-Smart-City-Traffic-Analytics)
```

---

## Step 6 — Add Repo Link to Your CV and LinkedIn

Copy this link and paste it on your CV and LinkedIn project description:

```
https://github.com/YOUR_USERNAME/UrbanFlow-Smart-City-Traffic-Analytics
```

---

## Notes

- The `.gitignore` is already configured to exclude `__pycache__`, `.ipynb_checkpoints`, `.venv`, temp files, etc.
- `requirements.txt` is present so collaborators can reproduce the environment with `pip install -r requirements.txt`
- `LICENSE` (MIT) is present
- The submission ZIP (`UrbanFlow_Final_Submission.zip`, ~29 MB) is included in the repo. If GitHub rejects it due to file size, add it to `.gitignore` and distribute separately.
