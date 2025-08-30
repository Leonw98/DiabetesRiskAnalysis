import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# 1. Human-readable descriptions for each feature
column_key = {
    'HighBP':               'High blood pressure (1 = yes; 0 = no)',
    'HighChol':             'High cholesterol (1 = yes; 0 = no)',
    'CholCheck':            'Cholesterol check (1 = yes; 0 = no)',
    'BMI':                  'Body Mass Index',
    'Smoker':               'Smoked >=100 cigarettes (1 = yes; 0 = no)',
    'Stroke':               'Ever had a stroke? (1 = yes; 0 = no)',
    'HeartDiseaseorAttack': 'CHD/MI diagnosis (1 = yes; 0 = no)',
    'PhysActivity':         'Physical activity past 30 days (1 = yes; 0 = no)',
    'Fruits':               'Fruit >=1/day (1 = yes; 0 = no)',
    'Veggies':              'Veggies >=1/day (1 = yes; 0 = no)',
    'HvyAlcoholConsump':    'Heavy alcohol consumption (1 = yes; 0 = no)',
    'AnyHealthcare':        'Has health coverage (1 = yes; 0 = no)',
    'NoDocbcCost':          'Skipped doctor due to cost (1 = yes; 0 = no)',
    'GenHlth':              'General health rating (1=excellent…5=poor)',
    'MentHlth':             'Unhealthy mental days past 30',
    'PhysHlth':             'Unhealthy physical days past 30',
    'DiffWalk':             'Difficulty walking (1 = yes; 0 = no)',
    'Sex':                  'Sex (0=female; 1=male)',
    'Age':                  'Age group (1=18–24…13=80+)',
    'Education':            'Education level (1=none…6=graduate)',
    'Income':               'Income bracket (1=<10k…8=>75k)'
}

# 2. Utility to pop out a table in Matplotlib, rounding to 2 decimals
def show_table(df: pd.DataFrame, title: str):
    rows, _ = df.shape
    height = max(2, rows * 0.3)
    fig, ax = plt.subplots(figsize=(9, height))
    ax.axis('off')
    tbl = ax.table(
        cellText=df.round(2).values,
        rowLabels=df.index,
        colLabels=df.columns,
        cellLoc='center',
        loc='center'
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(10)
    tbl.scale(1, 1.5)
    plt.title(title, pad=20)
    plt.tight_layout()
    plt.show()

# 3. Load the dataset (update path as needed)
file_path = r"C:\Users\leonw\Desktop\Projects\Diabetes\diabetes_012_health_indicators_BRFSS2015.csv"
df = pd.read_csv(file_path)

# 4. Compute feature means by Diabetes_012 and round
group_means = df.groupby('Diabetes_012').mean().T.round(2)
group_means.columns = ['Healthy (0)', 'Prediabetes (1)', 'Diabetes (2)']

# 5. Insert descriptions into the first column
group_means_desc = group_means.copy()
group_means_desc.insert(
    0,
    'Description',
    [column_key.get(feat, '') for feat in group_means_desc.index]
)

# 6. Display and pop-out the Feature-Means table
print("=== Average Health Indicators by Diabetes Status ===")
print(group_means_desc)
show_table(group_means_desc, "Average Health Indicators by Diabetes Status")

# 7. Create binary flags for prediabetes and diabetes
df['is_prediabetes'] = (df['Diabetes_012'] == 1).astype(int)
df['is_diabetes']    = (df['Diabetes_012'] == 2).astype(int)

# 8. Compute and round correlations
corr_pre = df.corr()['is_prediabetes'].sort_values().round(2)
corr_di  = df.corr()['is_diabetes'].sort_values().round(2)

# 9. Build a clean correlation DataFrame and add descriptions
corr_df = pd.DataFrame({
    'Corr w/ Prediabetes': corr_pre,
    'Corr w/ Diabetes':    corr_di
}).drop(index=['Diabetes_012', 'is_prediabetes', 'is_diabetes'], errors='ignore')

corr_df_desc = corr_df.copy()
corr_df_desc.insert(
    0,
    'Description',
    [column_key.get(feat, '') for feat in corr_df_desc.index]
)

# 10. Display and pop-out the Correlations table
print("\n=== Feature Correlations with Prediabetes & Diabetes ===")
print(corr_df_desc)
show_table(corr_df_desc, "Feature Correlations with Prediabetes & Diabetes")

# 11. Side-by-side correlation bar charts
fig, axes = plt.subplots(1, 2, figsize=(14, 8))

corr_df['Corr w/ Prediabetes'].plot(
    kind='barh', ax=axes[0], color='darkorange',
    title='Correlation w/ Prediabetes'
)
axes[0].set_xlabel('Correlation Coefficient')

corr_df['Corr w/ Diabetes'].plot(
    kind='barh', ax=axes[1], color='crimson',
    title='Correlation w/ Diabetes'
)
axes[1].set_xlabel('Correlation Coefficient')

plt.tight_layout()
plt.show()

# 12. Diverging bar chart: top ±5 correlations with Diabetes
corr_di_clean = corr_di.drop(index=['Diabetes_012', 'is_prediabetes', 'is_diabetes'], errors='ignore')
n = 5
top_pos = corr_di_clean.nlargest(n)
top_neg = corr_di_clean.nsmallest(n)
highlight = pd.concat([top_neg, top_pos]).sort_values().round(2)

plt.figure(figsize=(8, 5))
colors = ['#1f77b4' if v < 0 else '#d62728' for v in highlight]
highlight.plot(kind='barh', color=colors)
plt.axvline(0, color='black', linewidth=0.8)
plt.title(f'Top {n} Positive & Negative Correlations with Diabetes')
plt.xlabel('Correlation Coefficient')
plt.tight_layout()
plt.show()

# 13. Define high-risk vs secondary-risk features by threshold
high_thresh, mod_thresh = 0.30, 0.10
high_risk_feats = highlight[highlight.abs() >= high_thresh].index.tolist()
mod_risk_feats  = highlight[(highlight.abs() >= mod_thresh) &
                            (highlight.abs() <  high_thresh)].index.tolist()

print("\nHigh-risk factors:", high_risk_feats)
print("Secondary-risk factors:", mod_risk_feats)

# 14. Compute and display risk scores for healthy individuals
healthy = df[df['Diabetes_012'] == 0].copy()
all_feats = high_risk_feats + mod_risk_feats

# 14a. Standardize continuous features
cont_feats = [f for f in all_feats if healthy[f].nunique() > 2]
scaler = StandardScaler()
healthy[cont_feats] = scaler.fit_transform(healthy[cont_feats])

# 14b. Sum up standardized + binary features to create the risk_score
healthy['risk_score'] = healthy[all_feats].sum(axis=1).round(2)

# 15. Show top 10 healthy individuals by risk_score
top10 = healthy.sort_values('risk_score', ascending=False).head(10)
print("\nTop 10 Healthy Individuals by Risk Score")
print(top10[['risk_score'] + high_risk_feats + mod_risk_feats].round(2))
