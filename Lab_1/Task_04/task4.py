# Task 4: Display random records

import pandas as pd

df = pd.read_csv("../train.csv")

print("10 random records from the dataset:")
print(df.sample(10))