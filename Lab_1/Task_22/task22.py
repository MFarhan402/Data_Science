# Task 22: Compare survival rate by passenger class

import pandas as pd

df = pd.read_csv("../train.csv")

print("Survival rate by Pclass:")
print(df.groupby("Pclass")["Survived"].mean() * 100)