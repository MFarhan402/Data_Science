# Task 5: Technical summary of dataset

import pandas as pd

df = pd.read_csv("../train.csv")

print("Dataset info:")
df.info()