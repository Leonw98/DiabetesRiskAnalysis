
---

## Key Findings

### 1. Correlation Matrix of Health Indicators
The correlation matrix visualizes how each health variable relates to diabetes. Strongly positive correlations highlight major risk factors, while negative correlations indicate protective factors.  
![Correlation Matrix](images/correlation_matrix.png)

### 2. Risk and Protective Factors
- **Major Risk Factors:** BMI, High Blood Pressure, Heart Disease, Age, Smoking, and Cholesterol issues.  
- **Protective Factors:** Physical activity, fruit and vegetable intake, education, and income.  

These factors are identified based on their statistical correlation with diabetes in the dataset.

### 3. Individual Risk Scores
Each person is assigned a **Risk Score**, summarizing their overall diabetes risk based on the identified factors.  

- **Distribution of Risk Scores:** Shows the spread of risk across all individuals; most fall in the middle, while some are much higher.  
![Risk Score Distribution](images/risk_score_distribution.png)

- **Average Risk Score by Diabetes Status:** Visual comparison of risk scores between non-diabetic, pre-diabetic, and diabetic groups.  
![Average Risk by Diabetes Status](images/average_risk_by_diabetes.png)

### 4. Top At-Risk Individuals
The top 10 high-risk non-diabetic or pre-diabetic individuals are highlighted. This helps identify who might benefit most from interventions.  
![Top 10 High-Risk Individuals](images/top10_risk.png)  
*Commentary:* Individuals with high BMI, smoking, or high blood pressure tend to dominate this group.

### 5. Risk vs Protective Factors
Visual comparison of **risk and protective factors** shows which has the greatest effect on overall risk.  

- **Risk Factors Distribution:** Red bars show that BMI and age are the largest contributors to risk.  
![Risk Factors](images/risk_factors_distribution.png)

- **Protective Factors Distribution:** Green bars show that physical activity and healthy diet can mitigate some risk, though their effect is smaller than the top risk factors.  
![Protective Factors](images/protective_factors_distribution.png)

### 6. Income Analysis
Income is a fixed factor but helps contextualize risk.  

- **Average Risk Score by Income Group:** Shows that lower income groups have slightly higher risk scores on average.  
![Income Risk](images/income_risk.png)

- **Diabetes Status Distribution by Income Group:** Stacked bar chart shows prevalence of diabetes and pre-diabetes across income groups.  
![Income Diabetes Status](images/income_diabetes_status.png)  
*Commentary:* While income is associated with risk, lifestyle changes remain the most actionable way to reduce diabetes risk.

---

## Recommendations

- **Target modifiable risk factors**: Reducing BMI, quitting smoking, managing blood pressure, and controlling cholesterol can significantly lower risk.  
- **Enhance protective factors**: Regular physical activity and increasing fruit/vegetable intake can offset some risk.  
- **Income-related risk** cannot be easily changed, but lifestyle improvements can meaningfully reduce diabetes risk.

---

## Methodology

- **Data Cleaning & Exploration:** Loaded the BRFSS 2015 dataset, checked for missing values, and explored correlations.  
- **Risk Score Calculation:** Combined standardized risk factors and protective factors into a single score.  
- **Visualization:** Used plots to highlight distributions, top contributors, and income effects.  
- **High-Risk Identification:** Filtered the top 10% of individuals by Risk Score and examined modifiable factors.

---

## Tools Used

- Python 3.13  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn (StandardScaler)  
- Jupyter Notebook for interactive analysis  

---

## References

1. **BRFSS 2015 Dataset** – Behavioral Risk Factor Surveillance System, Centers for Disease Control and Prevention (CDC).  
2. Python Libraries: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/), [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/), [Scikit-learn](https://scikit-learn.org/)  
3. Portfolio Inspiration: [Tianna Parris – Movie Success Analysis](https://github.com/tiannaparris/PortfolioProjects/blob/main/Analyzing%20the%20Factors%20Contributing%20to%20the%20Success%20of%20a%20Movie.ipynb)

---

This project demonstrates how **data-driven insights can inform lifestyle choices** to reduce diabetes risk and highlights the most influential factors for intervention.
