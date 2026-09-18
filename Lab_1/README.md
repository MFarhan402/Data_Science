# Lab 1: Exploratory Data Analysis (EDA) on Titanic Dataset

## What is this Lab about?

This lab is about learning how to perform Exploratory Data Analysis (EDA) on a real dataset using Python. EDA means looking at the data carefully before doing any further analysis or building any machine learning model.

The goal is not just to run Python code, but to understand the dataset — what it contains, what is missing, what patterns exist, and what the data tells us.

---

## Dataset Used

**Titanic Passenger Dataset**

This dataset contains information about passengers who were on the Titanic ship. It includes details such as:

| Column | Meaning |
|--------|---------|
| PassengerId | Unique number for each passenger |
| Survived | 0 = Did not survive, 1 = Survived |
| Pclass | Passenger class (1 = First, 2 = Second, 3 = Third) |
| Name | Passenger name |
| Sex | Gender (male/female) |
| Age | Passenger age |
| SibSp | Number of siblings/spouses travelling with the passenger |
| Parch | Number of parents/children travelling with the passenger |
| Ticket | Ticket number |
| Fare | Amount paid for the ticket |
| Cabin | Cabin number |
| Embarked | Port from which the passenger boarded (C = Cherbourg, Q = Queenstown, S = Southampton) |

- **Rows:** 891
- **Columns:** 12

---

## What Was Done in This Lab?

The lab was divided into several parts, and each part focused on a different aspect of EDA.

### Part A: Setting Up Python
Imported the required libraries:
- **NumPy** — for numerical operations
- **Pandas** — for working with tables and datasets
- **Matplotlib** — for creating basic graphs
- **Seaborn** — for statistical graphs like boxplots, bar plots, and heatmaps

### Part B: Loading the Dataset
Loaded the CSV file into Python using `pd.read_csv()` and converted it into a Pandas DataFrame.

### Part C: Initial Dataset Inspection
Looked at the first few rows and some random rows to understand how the data is organized. Used `df.head()` and `df.sample(10)`.

### Part D: Technical Summary
Used `df.info()`, `df.shape()`, and `df.dtypes` to understand:
- How many columns are present
- What data types each column has
- Which columns contain missing values
- How many rows and columns the dataset has

### Part E: Missing and Duplicate Data
Counted non-missing values (`df.notnull().sum()`) and checked for duplicate rows (`df.duplicated().sum()`).

### Part F: Understanding Unique Values
Checked the values of the target variable (`Survived`) and counted unique values in every column using `df.nunique()`.

### Part G: Statistical Summary
Used `df.describe()` to get basic statistics of numerical columns — count, mean, standard deviation, min, quartiles, and max.

### Part H: Detailed Missing-Value Analysis
Counted missing values (`df.isnull().sum()`), displayed only columns with missing values, and calculated the missing-value percentage.

### Part I: Data Cleaning
- Removed duplicate rows using `df.drop_duplicates()`
- Filled missing Age values with the median age
- Filled missing Embarked values with the most common value (mode)
- Left the Cabin column unchanged because it has too many missing values

### Part J: Group-Level Analysis
Calculated the overall survival rate and compared survival rates by Sex and Pclass using `df.groupby()`.

### Part K: Data Visualization
Created histograms and boxplots for numerical features like Age, Fare, SibSp, and Parch.

### Part M: Correlation Analysis
Created a correlation matrix and displayed it as a heatmap to see relationships between numerical variables.

### Part O: Sorting and Finding Extreme Values
Found the five highest-paying passengers using `df.sort_values()` and visualized them with a bar plot.

---

## Key Findings

After completing the entire EDA, here are the most important findings:

1. **Missing Data is Significant**
   - The Cabin column has about 77% missing values — too incomplete to fill reliably.
   - The Age column has about 20% missing values — filled with the median age.
   - The Embarked column has only 2 missing values — filled with the most common port.

2. **Survival Patterns**
   - The overall survival rate is about **38%**.
   - **Females** had a much higher survival rate (about **74%**) than males (about **19%**).
   - **First-class** passengers had the highest survival rate (about **63%**), followed by second class (about **47%**) and third class (about **24%**).

3. **Fare Distribution is Skewed**
   - Most passengers paid low fares, but a few paid very high fares (up to 512).
   - The median fare is about 14, but the maximum is 512 — a huge difference.
   - This shows the Fare column has extreme outliers.

4. **No Duplicate Rows**
   - The dataset contains no duplicate rows — each row is a unique passenger.

---

## Purpose of This Lab

The main purpose of this lab was to learn how to:

- Load and inspect a real dataset
- Identify and handle missing values
- Identify and remove duplicate records
- Perform group-based analysis
- Create meaningful visualizations
- Interpret patterns found during EDA

EDA is not just about generating Python output. Its real goal is to **understand the dataset** before doing any further statistical analysis or building a machine learning model.

---

## Tools Used

- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code
- Git Bash

---

## Author

**MFarhan402**
GitHub: [https://github.com/MFarhan402/Data_Science](https://github.com/MFarhan402/Data_Science)