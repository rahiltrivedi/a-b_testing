# 🧪 A/B Testing Project – Customer Conversion Analysis

This project showcases a complete A/B testing pipeline using Python. It includes data analysis, statistical testing, interactive dashboards, and automated reporting in Word and PDF formats.

---

## 🎯 Objective

To determine whether a new variant (Group B) improves customer conversion compared to the control group (Group A) using hypothesis testing and visualization techniques.

---


## 📊 Features

- ✅ Clean and analyze A/B test data
- 📈 Visualize conversion rates (Seaborn + Matplotlib)
- 🧪 Run hypothesis test using `proportions_ztest`
- 📄 Generate Word report with results and plot
- 🖥️ Interactive dashboard with Plotly & Dash
- 📤 Export final report as PDF (optional)

---

## 📌 Dataset Description

- `user_id`: Unique identifier for each user  
- `group`: A (control) or B (variant)  
- `converted`: 1 = converted, 0 = not converted

---

## 🚀 How to Run

### 1. Install Requirements

```bash
pip install pandas seaborn matplotlib statsmodels python-docx dash plotly docx2pdf
```
### 2. To Open/Run Testing File
```bash
python ab_testing.py
```
### 3. To Open/Run Dashboard
```bash
python dashboard.py
```
- Then open your browser and go to:
-- http://127.0.0.1:8050

