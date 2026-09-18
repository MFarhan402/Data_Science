# Task 27: Compare survival by sex using a bar plot

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../train.csv")

sns.barplot(x="Sex", y="Survived", data=df, hue="Sex", legend=False)
plt.title("Sex vs Survival")
plt.xlabel("Sex")
plt.ylabel("Average Survival Rate")
plt.show()