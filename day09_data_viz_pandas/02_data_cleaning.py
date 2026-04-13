"""
Day 9, Lesson 2: Data Cleaning & Preprocessing
Covers:
  - Handling missing values (NaN)
  - Removing duplicates
  - Data type conversions
  - String cleaning
  - Outlier detection basics
"""

import pandas as pd
import numpy as np

# ============================================
# 1. Creating Messy Data
# ============================================

print("=" * 50)
print("Working with Messy Data")
print("=" * 50)

# Create a DataFrame with missing values
messy_data = {
    "student": ["Ali", "Hana", None, "Omar", "Fatima", "Ahmed"],
    "score": [85, None, 92, 78, 88, 85],
    "grade": ["A", "B", "A", "C", "A", "B"]
}

df = pd.DataFrame(messy_data)
print("\nOriginal (messy) data:")
print(df)
print(f"\nShape: {df.shape}")

# ============================================
# 2. Detecting Missing Values
# ============================================

print("\n" + "=" * 50)
print("Detecting Missing Values")
print("=" * 50)

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nTotal missing values:", df.isnull().sum().sum())

print("\nRows with any missing value:")
print(df[df.isnull().any(axis=1)])

# ============================================
# 3. Handling Missing Values
# ============================================

print("\n" + "=" * 50)
print("Handling Missing Values")
print("=" * 50)

# Option 1: Drop rows with any missing value
print("\nOption 1: Drop rows with missing values")
df_dropped = df.dropna()
print(df_dropped)

# Option 2: Drop rows where all values are missing
print("\nOption 2: Drop rows if all values are NaN (rare in this case)")
df_dropped_all = df.dropna(how='all')
print(df_dropped_all)

# Option 3: Fill missing values
print("\nOption 3: Fill missing values with default")
df_filled = df.fillna("Unknown")
print(df_filled)

# Option 4: Forward fill (copy previous value)
print("\nOption 4: Forward fill")
df_ffill = df.fillna(method='ffill')
print(df_ffill)

# Option 5: Fill specific column with mean (for numbers)
print("\nOption 5: Fill numeric column with mean")
df_mean = df.copy()
df_mean["score"] = df_mean["score"].fillna(df_mean["score"].mean())
print(df_mean)

# ============================================
# 4. Removing Duplicates
# ============================================

print("\n" + "=" * 50)
print("Removing Duplicates")
print("=" * 50)

# Create data with duplicates
dup_data = pd.DataFrame({
    "name": ["Ali", "Hana", "Ali", "Omar"],
    "age": [25, 30, 25, 28]
})

print("\nData with duplicates:")
print(dup_data)

print("\nDuplicate rows:")
print(dup_data.duplicated())

print("\nRemove duplicates:")
df_clean = dup_data.drop_duplicates()
print(df_clean)

# ============================================
# 5. Data Type Conversions
# ============================================

print("\n" + "=" * 50)
print("Data Type Conversions")
print("=" * 50)

# Create data with mixed types
mixed_data = pd.DataFrame({
    "age": ["25", "30", "28"],
    "salary": ["35000.50", "42000", "38500"]
})

print("\nOriginal types:")
print(mixed_data.dtypes)
print(mixed_data)

# Convert to numeric
print("\nAfter type conversion:")
mixed_data["age"] = pd.to_numeric(mixed_data["age"])
mixed_data["salary"] = pd.to_numeric(mixed_data["salary"])
print(mixed_data.dtypes)
print(mixed_data)

# ============================================
# 6. String Cleaning
# ============================================

print("\n" + "=" * 50)
print("String Cleaning")
print("=" * 50)

# Data with string issues
string_data = pd.DataFrame({
    "city": ["  Amman  ", "ZARQA", "irbid", "  AQABA  "],
    "status": ["Active ", "inactive", " ACTIVE", "Inactive"]
})

print("\nOriginal strings:")
print(string_data)

# Clean whitespace
print("\nAfter stripping whitespace:")
string_data["city"] = string_data["city"].str.strip()
string_data["status"] = string_data["status"].str.strip()
print(string_data)

# Standardize case
print("\nAfter standardizing case:")
string_data["city"] = string_data["city"].str.capitalize()
string_data["status"] = string_data["status"].str.lower()
print(string_data)

# ============================================
# 7. Outlier Detection (Basics)
# ============================================

print("\n" + "=" * 50)
print("Outlier Detection (Basics)")
print("=" * 50)

# Create data with outlier
outlier_data = pd.DataFrame({
    "score": [85, 88, 92, 78, 88, 150, 87]  # 150 is outlier
})

print("\nOriginal data:")
print(outlier_data)

# Method: Z-score (values > 3 std dev are outliers)
mean = outlier_data["score"].mean()
std = outlier_data["score"].std()
z_scores = abs((outlier_data["score"] - mean) / std)

print(f"\nMean: {mean:.2f}, Std Dev: {std:.2f}")
print("\nZ-scores:", z_scores.values)

outliers = outlier_data[z_scores > 2]  # threshold = 2
print("\nPotential outliers (z-score > 2):")
print(outliers)

# ============================================
# 8. Practical Cleaning Pipeline
# ============================================

print("\n" + "=" * 50)
print("Practical Cleaning Pipeline")
print("=" * 50)

# Create realistic messy data
raw_data = pd.DataFrame({
    "id": [1, 2, 2, 3, 4, 5],
    "name": ["Ali", "Hana", "Hana", "Omar", None, "Ahmed"],
    "age": ["25", "30", "30", "28", "26", "invalid"],
    "score": [85, None, 92, 78, None, 95]
})

print("\nRaw data:")
print(raw_data)

# Pipeline:
# 1. Remove duplicates
df_clean = raw_data.drop_duplicates()
print("\n1. After removing duplicates:")
print(df_clean)

# 2. Remove rows with missing names
df_clean = df_clean[df_clean["name"].notna()]
print("\n2. After removing rows with missing names:")
print(df_clean)

# 3. Convert age to numeric (drop invalid)
df_clean["age"] = pd.to_numeric(df_clean["age"], errors='coerce')
df_clean = df_clean[df_clean["age"].notna()]
print("\n3. After converting age and dropping invalid:")
print(df_clean)

# 4. Fill remaining missing scores with mean
df_clean["score"] = df_clean["score"].fillna(df_clean["score"].mean())
print("\n4. Final cleaned data:")
print(df_clean)

print("\n✅ Lesson 2 Complete!")
