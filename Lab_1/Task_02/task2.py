# Task 2: Load the CSV file

import pandas as pd

# Go one folder back and load train.csv
df = pd.read_csv("../train.csv")

# Check if dataset loaded
print("Dataset loaded successfully!")

# Show first 5 rows
print("First 5 rows:")
print(df.head())