# Task 28: Find the five highest-paying passengers

import pandas as pd

df = pd.read_csv("../train.csv")

topFares = df.sort_values(by="Fare", ascending=False)
top5 = topFares.head(5)

print("Five highest-paying passengers:")
print(top5[["Name", "Sex", "Pclass", "Fare"]])