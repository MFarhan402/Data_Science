# Task 26: Display correlation as a heatmap

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../train.csv")

selected_cols = ["Age", "SibSp", "Parch", "Pclass", "Fare"]

plt.figure(figsize=(8, 6))
sns.heatmap(df[selected_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()