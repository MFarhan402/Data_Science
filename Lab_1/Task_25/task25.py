# Task 25: Create a correlation matrix

import pandas as pd

df = pd.read_csv("../train.csv")

selected_cols = ["Age", "SibSp", "Parch", "Pclass", "Fare"]

print("Correlation matrix:")
print(df[selected_cols].corr())