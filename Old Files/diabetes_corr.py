import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
file_path = r"C:\Users\leonw\Desktop\Projects\Diabetes\diabetes_012_health_indicators_BRFSS2015.csv"
df = pd.read_csv(file_path)

# 2. Group‐Means Matrix
group_means = df.groupby('Diabetes_012').mean().T
group_means.columns = ['Healthy (0)', 'Prediabetes (1)', 'Diabetes (2)']

print("=== Feature Means by Diabetes Status ===")
print(group_means)

# 3. Binary Correlation Matrices
df['is_prediabetes'] = (df['Diabetes_012'] == 1).astype(int)
df['is_diabetes']    = (df['Diabetes_012'] == 2).astype(int)

corr_pre = df.corr()['is_prediabetes'].sort_values()
corr_di  = df.corr()['is_diabetes'].sort_values()

corr_df = pd.DataFrame({
    'Corr with Prediabetes': corr_pre,
    'Corr with Diabetes':    corr_di
}).drop(index=['is_prediabetes', 'is_diabetes', 'Diabetes_012'])

print("\n=== Binary Correlations ===")
print(corr_df)

# 4. Side‐by‐Side Visualization of All Correlations
fig, axes = plt.subplots(1, 2, figsize=(14, 8))

corr_df['Corr with Prediabetes'].plot(
    kind='barh', ax=axes[0], color='darkorange',
    title='Feature Correlation with Prediabetes'
)
axes[0].set_xlabel('Correlation Coefficient')

corr_df['Corr with Diabetes'].plot(
    kind='barh', ax=axes[1], color='crimson',
    title='Feature Correlation with Diabetes'
)
axes[1].set_xlabel('Correlation Coefficient')

plt.tight_layout()
plt.show()

# 5. Diverging Bar Chart: Top Positive & Negative Correlations for Diabetes
n = 5
top_pos = corr_di.nlargest(n)
top_neg = corr_di.nsmallest(n)
highlight = pd.concat([top_neg, top_pos]).sort_values()

plt.figure(figsize=(8, 5))
colors = ['#1f77b4' if val < 0 else '#d62728' for val in highlight]
highlight.plot(kind='barh', color=colors)
plt.axvline(0, color='black', linewidth=0.8)
plt.title(f'Top {n} Positive & Negative Correlations with Diabetes')
plt.xlabel('Correlation Coefficient')
plt.tight_layout()
plt.show()