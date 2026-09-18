# Task 8: Count non-missing values in each column

import pandas as pd

df = pd.read_csv("../train.csv")

print("Non-missing values in each column:")
print(df.notnull().sum())