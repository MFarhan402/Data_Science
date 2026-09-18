# Task 19: Check missing values after cleaning

import pandas as pd

df = pd.read_csv("../train.csv")

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("Missing values after cleaning:")
print(df.isnull().sum())