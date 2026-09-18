# Task 10: Check values of target variable

import pandas as pd

df = pd.read_csv("../train.csv")

print("Unique values in Survived column:")
print(df["Survived"].unique())