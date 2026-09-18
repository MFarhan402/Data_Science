# Task 13: Count missing values in each column

import pandas as pd

df = pd.read_csv("../train.csv")

print("Missing values in each column:")
print(df.isnull().sum())