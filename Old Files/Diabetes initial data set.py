import pandas as pd

# 1. Show all columns when printing
pd.set_option('display.max_columns', None)

# 2. Load the CSV file
file_path = r"C:\Users\leonw\Desktop\Projects\Diabetes\diabetes_012_health_indicators_BRFSS2015.csv"
df = pd.read_csv(file_path)

# 3. Preview data
print("=== Top 5 rows ===")
print(df.head(), "\n")

print("=== Column names ===")
print(df.columns.tolist(), "\n")

# 4. Define the full column-key dictionary
column_key = {
    'Diabetes_012':          'Diabetes status (0 = no, 1 = prediabetes, 2 = diabetes)',
    'HighBP':                'High blood pressure (1 = yes, 0 = no)',
    'HighChol':              'High cholesterol (1 = yes, 0 = no)',
    'CholCheck':             'Cholesterol check in past 5 years (1 = yes, 0 = no)',
    'BMI':                   'Body Mass Index',
    'Smoker':                'Smoked ≥100 cigarettes lifetime (1 = yes, 0 = no)',
    'Stroke':                'Ever had a stroke? (1 = yes, 0 = no)',
    'HeartDiseaseorAttack':  'Coronary heart disease or myocardial infarction (1 = yes, 0 = no)',
    'PhysActivity':          'Physical activity in past 30 days (1 = yes, 0 = no)',
    'Fruits':                'Consumes fruit ≥1 times/day (1 = yes, 0 = no)',
    'Veggies':               'Consumes vegetables ≥1 times/day (1 = yes, 0 = no)',
    'HvyAlcoholConsump':     'Heavy drinkers (men >14 drinks/week; women >7 drinks/week) (0 = no, 1 = yes)',
    'AnyHealthcare':         'Have any kind of health care coverage (0 = no, 1 = yes)',
    'NoDocbcCost':           'Needed to see a doctor but could not because of cost in past 12 months (0 = no, 1 = yes)',
    'GenHlth':               'General health rating on scale 1–5 (1 = excellent, 5 = poor)',
    'MentHlth':              'Days mental health not good in past 30 days (0–30)',
    'PhysHlth':              'Days physical health not good in past 30 days (0–30)',
    'DiffWalk':              'Serious difficulty walking or climbing stairs (0 = no, 1 = yes)',
    'Sex':                   'Sex (0 = female, 1 = male)',
    'Age':                   '13-level age category (_AGEG5YR): 1 = 18–24, …, 13 = 80+',
    'Education':             'Education level (EDUCA): 1 = no school, …, 6 = college graduate',
    'Income':                'Income scale (INCOME2): 1 = < $10,000, …, 8 = $75,000+'
}

# 5. Print the human-readable key
print("=== Column Key ===")
for col, desc in column_key.items():
    print(f"{col}: {desc}")