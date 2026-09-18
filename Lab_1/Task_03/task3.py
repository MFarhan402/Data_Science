# Task 3: Display the first few rows

import pandas as pd

# Load the dataset
df = pd.read_csv("../train.csv")

# Show first 5 rows
print("First 5 rows of the dataset:")
print(df.head())