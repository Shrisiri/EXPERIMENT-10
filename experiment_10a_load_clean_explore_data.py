"""
Experiment 10(a): Load, clean, and explore data using Python.

Aim:
To create a sample dataset, handle missing values, and explore
the dataset using Pandas.
"""

import pandas as pd

# Sample dataset
data = {
    "Name": ["John", "Alice", "Bob", "David"],
    "Age": [20, 21, None, 22],
    "Marks": [85, 90, 78, None],
}

# Load data into a DataFrame
df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Clean the data by replacing missing values with column averages
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nCleaned Dataset:")
print(df)

# Explore the dataset
print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nFirst Two Rows:")
print(df.head(2))
