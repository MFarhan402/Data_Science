# Task 17: Handle missing Age values

import pandas as pd

df = pd.read_csv("../train.csv")

print("Missing Age values before:", df["Age"].isnull().sum())

median_age = df["Age"].median()
print("Median Age:", median_age)

df["Age"] = df["Age"].fillna(median_age)

print("Missing Age values after:", df["Age"].isnull().sum())