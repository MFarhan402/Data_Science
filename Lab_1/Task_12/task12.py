# Task 12: Descriptive statistics

import pandas as pd

df = pd.read_csv("../train.csv")

print("Descriptive statistics of numerical columns:")
print(df.describe())