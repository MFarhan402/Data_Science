# Task 18: Handle missing Embarked values

import pandas as pd

df = pd.read_csv("../train.csv")

print("Missing Embarked values before:", df["Embarked"].isnull().sum())

mode_embarked = df["Embarked"].mode()[0]
print("Most common Embarked:", mode_embarked)

df["Embarked"] = df["Embarked"].fillna(mode_embarked)

print("Missing Embarked values after:", df["Embarked"].isnull().sum())