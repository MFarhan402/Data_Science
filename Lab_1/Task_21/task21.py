# Task 21: Compare survival rate by sex

import pandas as pd

df = pd.read_csv("../train.csv")

print("Survival rate by Sex:")
print(df.groupby("Sex")["Survived"].mean() * 100)