# Task 11: Count unique values in every column

import pandas as pd

df = pd.read_csv("../train.csv")

print("Unique values in each column:")
print(df.nunique())