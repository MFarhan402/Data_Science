# Task 16: Remove duplicate rows

import pandas as pd

df = pd.read_csv("../train.csv")

print("Before removing duplicates:", df.shape)

df = df.drop_duplicates().copy()

print("After removing duplicates:", df.shape)