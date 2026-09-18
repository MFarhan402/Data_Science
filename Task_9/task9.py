# Task 9: Check duplicate rows

import pandas as pd

df = pd.read_csv("../train.csv")

print("Duplicate rows:", df.duplicated().sum())