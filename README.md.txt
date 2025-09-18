# 🩺 Diabetes Risk and Protective Factor Analysis

## 📌 Project Overview
This project analyzes data from the **2015 Behavioral Risk Factor Surveillance System (BRFSS)** to identify the factors most strongly associated with diabetes.  
The goal was not only to build a predictive model, but also to uncover **actionable insights** that can guide public health strategies.

Key contributions of this project include:
- Identifying **risk and protective factors** for diabetes  
- Creating a **composite RiskScore** to quantify individual-level risk  
- Stratifying risk across **income, age, and sex groups**  
- Highlighting **socioeconomic disparities** in diabetes prevalence  
- Providing **policy-ready recommendations** for intervention  

---

## 🔎 Key Insights

### 1. Strongest Risk Factors
- Difficulty walking (`DiffWalk`)  
- Poor physical health days (`PhysHlth`)  
- Self-rated general health (`GenHlth`)  
- High blood pressure (`HighBP`)  
- Heart disease or attack (`HeartDiseaseorAttack`)  
- Stroke history (`Stroke`)  

📊 See [Correlation Heatmap](images/correlation_matrix.png)

---

### 2. Protective Factors
- **Income** and **Education**: stronger protection than any single lifestyle habit  
- **Lifestyle behaviors** (fruits, vegetables, physical activity) provided modest but consistent benefits  

📋 See [Protective Factors Table](tables/protective_factors.html)

---

### 3. Heavy Alcohol Consumption
- Highest in **non-diabetics (6–7%)**, dropping to **~4–5% in pre-diabetes** and **~2–4% in diabetes**  
- Declines are sharpest in younger and higher-income groups  
- Men consistently reported higher consumption  

📊 See charts:  
- [Alcohol by Status](images/heavy_alcohol_by_status.png)  
- [Alcohol by Income](images/heavy_alcohol_by_income.png)  
- [Alcohol by Age](images/heavy_alcohol_by_age.png)  
- [Alcohol by Sex](images/heavy_alcohol_by_sex.png)  

---

### 4. Composite Risk Scoring
I created a **RiskScore** by standardizing and summing key features:  
- Risk factors (e.g., `HighBP`, `GenHlth`, `PhysHlth`)  
- Minus protective factors (e.g., `Income`, `Education`, `PhysActivity`)  

Risk Levels:  
- **Low**: bottom 50%  
- **Medium**: 50th–90th percentile  
- **High**: top 10%  

📊 See [Risk Score Distribution](images/high_risk_distribution.png)

---

### 5. RiskScore by Diabetes Status
- **No Diabetes**: lowest scores  
- **Pre-Diabetes**: closer to Diabetes than to No Diabetes  
- **Diabetes**: highest risk  

📊 See [Average Risk Score by Group](images/avg_risk_by_status.png)

---

### 6. High-Risk Individuals
The top 10% of individuals by RiskScore accounted for the majority of diabetes prevalence.  
Most common risk drivers: poor general health, poor physical health, difficulty walking.  

📊 See [High Risk Distribution](images/high_risk_distribution.png)  
📋 See [Top 10 High-Risk Individuals Table](tables/top10_highrisk.html)

---

### 7. Stratified Risk Profiles
- **High-Risk Non-Diabetics** → preventive screening  
- **High-Risk Pre-Diabetics** → prevention programs  
- **High-Risk Diabetics** → integrated care  

📋 See [Stratified Profiles Table](tables/stratified_risk_profiles.html)

---

### 8. Income and Inequality
- Higher income → lower risk scores and lower diabetes prevalence  
- Lower income → higher prevalence and concentration of high-risk individuals  

📊 See charts:  
- [Risk by Income](images/income_risk.png)  
- [Diabetes by Income](images/income_diabetes_status.png)

---

### 9. Model Performance
Baseline Logistic Regression:  
- **Accuracy**: 84%  
- **ROC AUC**: 0.76  
- **High precision, low recall** — good at confirming positives, but under-detects diabetes  

📊 See [ROC Curve](images/roc_curve.png)

---

## 🏥 Public Health Recommendation
Healthcare systems can use this framework to:
1. Identify **top-decile RiskScore individuals**  
2. Proactively reach out with **tailored screening and coaching**  
3. Address not just clinical markers, but also **structural barriers** like income and education  

This **data-driven triage system** can reduce new diabetes cases and improve long-term health equity.  

---

## 🛠️ Tools Used
- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Statsmodels)  
- **Jupyter Notebook** for reproducible analysis  
- **Portfolio-focused structure** with modular code and clear markdowns  

---

## 📌 Why This Project Matters
This analysis reflects a **full-cycle data science workflow**:
- Data exploration  
- Feature engineering  
- Risk scoring  
- Model evaluation  
- Public health recommendations  

It demonstrates my ability to move beyond code into **insightful, decision-ready analysis** — the kind of work that bridges **data and impact**.
