# Task 15: Calculate missing value percentage

import pandas as pd

df = pd.read_csv("../train.csv")

missing_percentage = (df.isnull().sum() / len(df) * 100).round(2)

print("Missing value percentage per column:")
print(pd.DataFrame({
    "Missing Count": df.isnull().sum(),
    "Missing Percentage": missing_percentage
}))