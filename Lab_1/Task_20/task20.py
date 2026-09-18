# Task 20: Calculate overall survival rate

import pandas as pd

df = pd.read_csv("../train.csv")

survival_rate = df["Survived"].mean() * 100

print(f"Overall Survival Rate: {survival_rate:.2f}%")