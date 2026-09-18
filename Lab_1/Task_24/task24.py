# Task 24: Create boxplots for numerical features

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../train.csv")

numeric_cols = ["Age", "Fare", "SibSp", "Parch"]

plt.figure(figsize=(10, 6))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(y=df[col])
    plt.title(col)

plt.tight_layout()
plt.show()