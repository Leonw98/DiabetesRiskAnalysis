import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
file_path = r"C:\Users\leonw\Desktop\Projects\Diabetes\diabetes_012_health_indicators_BRFSS2015.csv"
df = pd.read_csv(file_path)

# 1) Compute means and transpose
group_means = df.groupby('Diabetes_012').mean().T

# 2) Rename columns for clarity
group_means.columns = ['Healthy (0)', 'Prediabetes (1)', 'Diabetes (2)']

# 3) Print the full table (no KeyError)
print("=== Mean values by Diabetes Status ===")
print(group_means)

# 4) Correlations with the target
corr = df.corr()['Diabetes_012'].sort_values()

# 5) Plot heatmap
plt.figure(figsize=(6,8))
sns.heatmap(corr.to_frame(), annot=True, cmap='vlag')
plt.title('Correlation with Diabetes Status')
plt.show()
