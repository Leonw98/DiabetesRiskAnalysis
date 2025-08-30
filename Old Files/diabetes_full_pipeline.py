# ===============================
# Diabetes Risk/Protective Factor Analysis - Full Pipeline
# Includes Income Groups (4)
# ===============================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# =====================================
# 1) Load dataset
# =====================================
file_path = r"C:\Users\leonw\Desktop\Projects\Diabetes\diabetes_012_health_indicators_BRFSS2015.csv"

if not os.path.exists(file_path):
    print(f"Error: File not found at {file_path}")
    exit()

df = pd.read_csv(file_path)
print(f"Successfully loaded dataset from: {file_path}")
print(df.shape)
print(df.head())

# =====================================
# 2) Correlation matrix
# =====================================
corr = df.corr(numeric_only=True)
plt.figure(figsize=(12, 10))
sns.heatmap(corr, cmap="RdBu_r", center=0)
plt.title("Correlation Matrix of Health Indicators", fontsize=14)
plt.show()

# =====================================
# 3) Identify risk and protective factors
# =====================================
target = 'Diabetes_012'
correlations = corr[target].drop(target).sort_values()

risk_factors = correlations[correlations > 0].index.tolist()
protective_factors = correlations[correlations < 0].index.tolist()

print("\n" + "="*60)
print("RISK AND PROTECTIVE FACTORS")
print("="*60)
print(f"{'RISK FACTORS:':<30}")
for i, factor in enumerate(risk_factors, 1):
    print(f"  {i:2d}. {factor}")
print(f"\n{'PROTECTIVE FACTORS:':<30}")
for i, factor in enumerate(protective_factors, 1):
    print(f"  {i:2d}. {factor}")
print("="*60)

# =====================================
# 4) Standardize features and compute RiskScore
# =====================================
scaler = StandardScaler()
scaled = pd.DataFrame(scaler.fit_transform(df[risk_factors + protective_factors]),
                      columns=risk_factors + protective_factors)

df['RiskScore'] = scaled[risk_factors].sum(axis=1) - scaled[protective_factors].sum(axis=1)

# =====================================
# 5) Distribution of RiskScore
# =====================================
plt.figure(figsize=(8, 5))
sns.histplot(df['RiskScore'], bins=50, kde=True, color="purple")
plt.title("Distribution of Risk Scores")
plt.xlabel("Risk Score")
plt.ylabel("Count")
plt.show()

# =====================================
# 6) Average RiskScore by Diabetes Status
# =====================================
group_scores = df.groupby(target)['RiskScore'].mean()
plt.figure(figsize=(6, 4))
group_scores.plot(kind="bar", color=["green", "orange", "red"])
plt.title("Average Risk Score by Diabetes Status")
plt.ylabel("Average Risk Score")
plt.xticks([0, 1, 2], ["No Diabetes (0)", "Pre-diabetes (1)", "Diabetes (2)"], rotation=30)
plt.show()

print("\n" + "="*60)
print("AVERAGE RISK SCORES BY DIABETES STATUS")
print("="*60)
scores_df = pd.DataFrame({
    'Diabetes Status': ['No Diabetes (0)', 'Pre-diabetes (1)', 'Diabetes (2)'],
    'Average Risk Score': group_scores.values
})
print(scores_df.to_string(index=False, float_format='%.3f'))
print("="*60)

# =====================================
# 7) High-risk individuals (top 10%)
# =====================================
threshold = df['RiskScore'].quantile(0.90)
high_risk_individuals = df[df['RiskScore'] >= threshold]

def top_risk_features(row, n=3):
    risk_vals = row[risk_factors]
    top_risks = risk_vals.sort_values(ascending=False).head(n).index.tolist()
    return ', '.join(top_risks)

high_risk_individuals['Top_Risk_Features'] = high_risk_individuals.apply(top_risk_features, axis=1)

plt.figure(figsize=(10, 6))
sns.histplot(high_risk_individuals['RiskScore'], bins=20, kde=True, color="red")
plt.title("Distribution of Risk Scores for Top 10% At-Risk Individuals")
plt.xlabel("Risk Score")
plt.ylabel("Count")
plt.show()

# =====================================
# 8) High-risk non-diabetic / pre-diabetic
# =====================================
high_risk_non_diabetic = high_risk_individuals[high_risk_individuals[target] != 2]
high_risk_non_diabetic['Top_Risk_Features'] = high_risk_non_diabetic.apply(top_risk_features, axis=1)

plt.figure(figsize=(10, 6))
sns.histplot(high_risk_non_diabetic['RiskScore'], bins=20, kde=True, color="orange")
plt.title("Distribution of Risk Scores for High-Risk Non-Diabetic/Pre-diabetic Individuals")
plt.xlabel("Risk Score")
plt.ylabel("Count")
plt.show()

# =====================================
# 9) Top 10 High-Risk Non-Diabetic / Pre-Diabetic Individuals
# =====================================
top_leaderboard = high_risk_non_diabetic.sort_values('RiskScore', ascending=False).head(10)
leaderboard_display = top_leaderboard[['RiskScore', 'Top_Risk_Features', target]].copy()
leaderboard_display.columns = ['Risk Score', 'Top Risk Features', 'Diabetes Status']
leaderboard_display = leaderboard_display.reset_index(drop=True)
leaderboard_display.index = leaderboard_display.index + 1
print("\n" + "="*80)
print("TOP 10 HIGH-RISK NON-DIABETIC/PRE-DIABETIC INDIVIDUALS")
print("="*80)
print(leaderboard_display.to_string(float_format='%.2f'))

plt.figure(figsize=(10, 6))
top_leaderboard_sorted = top_leaderboard.sort_values('RiskScore')
colors = ['skyblue' if x == 0 else 'orange' for x in top_leaderboard_sorted[target]]
bars = plt.barh(range(len(top_leaderboard_sorted)), top_leaderboard_sorted['RiskScore'], color=colors)
for i, score in enumerate(top_leaderboard_sorted['RiskScore']):
    plt.text(score + 0.1, i, f'{score:.2f}', va='center')
plt.yticks(range(len(top_leaderboard_sorted)), top_leaderboard_sorted['Top_Risk_Features'])
plt.xlabel("Risk Score")
plt.title("Top 10 High-Risk Non-Diabetic/Pre-diabetic Individuals")
plt.legend(handles=[plt.Rectangle((0,0),1,1,color='skyblue'), plt.Rectangle((0,0),1,1,color='orange')],
           labels=['No Diabetes','Pre-diabetes'])
plt.tight_layout()
plt.show()

# =====================================
# 10) Income Analysis (4 groups)
# =====================================
if 'Income' in df.columns:
    # Use qcut with duplicates='drop' and generate matching labels
    income_groups = pd.qcut(df['Income'], q=4, duplicates='drop')
    n_groups = income_groups.cat.categories.size
    labels = ['Low', 'Medium', 'High', 'Very High'][:n_groups]
    df['IncomeGroup'] = income_groups.cat.rename_categories(labels)
    
    # Average risk score by income group
    income_risk = df.groupby('IncomeGroup')['RiskScore'].mean()
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x=income_risk.index, y=income_risk.values, color='teal')
    plt.title("Average Risk Score by Income Group")
    plt.xlabel("Income Group")
    plt.ylabel("Average Risk Score")
    plt.show()
    
    # Diabetes prevalence by income group
    income_diabetes = df.groupby(['IncomeGroup', target]).size().unstack(fill_value=0)
    income_diabetes_prop = income_diabetes.div(income_diabetes.sum(axis=1), axis=0)
    income_diabetes_prop.plot(kind='bar', stacked=True, figsize=(8,5), color=['green','orange','red'])
    plt.title("Diabetes Status Distribution by Income Group")
    plt.ylabel("Proportion")
    plt.xlabel("Income Group")
    plt.xticks(rotation=0)
    plt.show()
