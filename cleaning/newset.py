import pandas as pd
import numpy as np

# 1. Load dataset
file_path = r"E:\war\fatalities_isr_pse_conflict_2000_to_2023.csv"
df = pd.read_csv(file_path)

# 2. Drop unwanted columns
cols_to_drop = ['date_of_death', 'place_of_residence_district']
df.drop(columns=[col for col in cols_to_drop if col in df.columns], inplace=True)

# 3. Replace common missing value strings with NaN
df.replace(['<unset>', 'Unknown', 'unknown', 'NA', 'N/A', ''], np.nan, inplace=True)

# 4. Separate numeric and categorical columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = df.select_dtypes(include=['object']).columns

# 5. Fill numeric columns with MEDIAN
for col in numeric_cols:
    df[col].fillna(df[col].median(), inplace=True)

# 6. Fill categorical columns with MODE
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# 7. Final check (no nulls)
print("Remaining null values per column:")
print(df.isnull().sum())
# 8. Save cleaned file
cleaned_path = "E:\war\cleaned.csv"
df.to_csv(cleaned_path, index=False)
