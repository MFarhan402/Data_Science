# Task 14: Display only columns with missing values

import pandas as pd

df = pd.read_csv("../train.csv")

missing_values = df.isnull().sum()

print("Columns with missing values (highest to lowest):")
print(missing_values[missing_values > 0].sort_values(ascending=False))