# Task 7: Check data type of every column

import pandas as pd

df = pd.read_csv("../train.csv")

print("Data types of each column:")
print(df.dtypes)