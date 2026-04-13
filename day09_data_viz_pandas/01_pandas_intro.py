"""
Day 9, Lesson 1: Pandas Basics and DataFrames
Covers:
  - What is a DataFrame
  - Creating DataFrames from lists, dicts, CSVs
  - Accessing rows and columns
  - Basic DataFrame operations
"""

import pandas as pd
import numpy as np

# ============================================
# 1. Creating DataFrames from Dictionaries
# ============================================

print("=" * 50)
print("Creating DataFrames from Dictionaries")
print("=" * 50)

# Simple dictionary → DataFrame
data = {
    "name": ["Ali", "Hana", "Omar", "Fatima"],
    "age": [25, 30, 28, 26],
    "salary": [35000, 42000, 38000, 40000]
}

df = pd.DataFrame(data)
print("\nBasic DataFrame:")
print(df)

# ============================================
# 2. DataFrame Information
# ============================================

print("\n" + "=" * 50)
print("DataFrame Information")
print("=" * 50)

print("\nShape (rows, columns):", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nBasic statistics:\n", df.describe())

# ============================================
# 3. Accessing Data
# ============================================

print("\n" + "=" * 50)
print("Accessing Data")
print("=" * 50)

# Access single column (Series)
print("\nNames column:")
print(df["name"])

# Access multiple columns
print("\nNames and ages:")
print(df[["name", "age"]])

# Access first N rows
print("\nFirst 2 rows:")
print(df.head(2))

# Access specific row by index
print("\nRow 1:")
print(df.iloc[1])

# Access specific cell
print("\nSalary of person at index 0:", df.iloc[0]["salary"])

# ============================================
# 4. Filtering Rows
# ============================================

print("\n" + "=" * 50)
print("Filtering Rows")
print("=" * 50)

# Filter: age > 27
print("\nPeople older than 27:")
print(df[df["age"] > 27])

# Filter: salary >= 40000
print("\nHigh earners (>= 40000):")
print(df[df["salary"] >= 40000])

# Multiple conditions
print("\nAge > 26 AND salary > 35000:")
print(df[(df["age"] > 26) & (df["salary"] > 35000)])

# ============================================
# 5. Adding Columns
# ============================================

print("\n" + "=" * 50)
print("Adding Columns")
print("=" * 50)

# Add a new column
df["bonus"] = df["salary"] * 0.1
print("\nWith bonus column:")
print(df)

# Add column with fixed value
df["department"] = "Engineering"
print("\nWith department column:")
print(df.head(2))

# ============================================
# 6. Creating DataFrame from Lists
# ============================================

print("\n" + "=" * 50)
print("Creating DataFrame from Lists")
print("=" * 50)

# Lists with column names
sales_data = pd.DataFrame(
    [[100, 200, 150], [250, 180, 220]],
    columns=["Q1", "Q2", "Q3"],
    index=["Product A", "Product B"]
)

print("\nQuarterly sales:")
print(sales_data)

# ============================================
# 7. Loading from CSV (Example Structure)
# ============================================

print("\n" + "=" * 50)
print("Loading from CSV (Example)")
print("=" * 50)

# Example (assumes sales.csv exists):
# df_sales = pd.read_csv("sales.csv")
# print(df_sales.head())

print("\nNote: Use pd.read_csv('filename.csv') to load CSV files")

# ============================================
# 8. Summary Statistics
# ============================================

print("\n" + "=" * 50)
print("Summary Statistics")
print("=" * 50)

print("\nMean salary:", df["salary"].mean())
print("Median age:", df["age"].median())
print("Min salary:", df["salary"].min())
print("Max age:", df["age"].max())
print("Salary std dev:", df["salary"].std())

print("\n✅ Lesson 1 Complete!")
