#!/usr/bin/env python3
"""Day 13, Lesson 2: Data Wrangling - Cleaning & Transforming Real Data

Real-world data is MESSY. Learn to:
- Handle missing values
- Fix data types
- Rename columns
- Detect and handle outliers
- Combine datasets
"""

import pandas as pd
import numpy as np

print("=== Data Wrangling: Cleaning Messy Data ===\n")

# 1. Create messy dataset (realistic!)
print("1. Creating Messy Dataset:")
messy_data = {
    'customer_id': [1, 2, None, 4, 5, 6, 7, 8, 9, 10],
    'name': ['John', 'Jane', 'Bob', 'ALICE', 'charlie', None, 'Frank', 'Grace', 'henry', 'Iris'],
    'email': ['john@example.com', 'jane@example', 'bob@example.com', 'alice@test.com', 'charlie@example.com', 
              'dave@example.com', 'frank@example.com', 'grace@example.com', 'henry@example.com', 'iris@example.com'],
    'signup_date': ['2024-01-15', '2024-01-16', '2024-01-17', '2024/01/18', '2024-01-19', 
                    '2024-01-20', '2024-01-21', 'yesterday', '2024-01-23', '2024-01-24'],
    'revenue': [100, 200, 150, '250', 300, -50, 1000, 175, 180, 190],
    'age': [25, 30, 35, 28, 32, 150, 29, 31, 27, 29]
}

df = pd.DataFrame(messy_data)
print("Raw data (with issues):")
print(df)
print(f"\nData types:\n{df.dtypes}")

# 2. Handle missing values
print("\n2. Handling Missing Values:")
print(f"Missing values:\n{df.isnull().sum()}")

# Remove rows with missing IDs (critical)
df_clean = df[df['customer_id'].notna()].copy()
print(f"✓ Removed {len(df) - len(df_clean)} rows with missing IDs")

# Fill missing names
df_clean['name'] = df_clean['name'].fillna('Unknown')
print("✓ Filled missing names with 'Unknown'")

# 3. Standardize names
print("\n3. Standardizing Text Data:")
df_clean['name'] = df_clean['name'].str.title()
print(f"Standardized names:\n{df_clean['name'].unique()}")

# 4. Fix data types
print("\n4. Converting Data Types:")

# Convert revenue to numeric (handle string values)
df_clean['revenue'] = pd.to_numeric(df_clean['revenue'], errors='coerce')
print("✓ Converted revenue to numeric")

# Parse dates (handle different formats)
df_clean['signup_date'] = pd.to_datetime(df_clean['signup_date'], errors='coerce')
print("✓ Parsed dates (some invalid -> NaT)")

print(f"\nCleaned data types:\n{df_clean.dtypes}")

# 5. Outlier detection
print("\n5. Detecting Outliers:")
print(f"Age range: {df_clean['age'].min()} - {df_clean['age'].max()}")

# Flag outliers (age > 100)
outliers = df_clean[df_clean['age'] > 100]
print(f"Found {len(outliers)} outlier(s) in age:")
print(outliers[['name', 'age']])

# Fix outlier
df_clean.loc[df_clean['age'] > 100, 'age'] = df_clean[df_clean['age'] <= 100]['age'].median()
print(f"✓ Fixed outliers with median value: {df_clean[df_clean['name'] == 'Frank']['age'].values[0]}")

# 6. Remove invalid records
print("\n6. Removing Invalid Records:")
print(f"Negative revenue records: {(df_clean['revenue'] < 0).sum()}")
df_clean = df_clean[df_clean['revenue'] >= 0]
print("✓ Removed negative revenue")

# 7. Add derived columns
print("\n7. Feature Engineering (Creating New Columns):")
df_clean['customer_age_days'] = (pd.Timestamp.now() - df_clean['signup_date']).dt.days
df_clean['revenue_per_day'] = df_clean['revenue'] / (df_clean['customer_age_days'] + 1)
print("✓ Created: customer_age_days, revenue_per_day")

# 8. Duplicate handling
print("\n8. Checking for Duplicates:")
duplicates = df_clean.duplicated(subset=['email']).sum()
print(f"Duplicate emails: {duplicates}")

# 9. Summary statistics
print("\n9. Quality Report:")
print(f"Total records: {len(df_clean)}")
print(f"Missing values remaining: {df_clean.isnull().sum().sum()}")
print(f"Revenue avg: ${df_clean['revenue'].mean():.2f}")
print(f"Age avg: {df_clean['age'].mean():.1f} years")

print("\nCleaned data (first 5 rows):")
print(df_clean.head())

# 10. Save cleaned data
df_clean.to_csv('cleaned_customers.csv', index=False)
print("\n✓ Saved to cleaned_customers.csv")

print("\n✅ Data wrangling lesson complete!")
print("\n🎯 Wrangling Checklist:")
print("  ✓ Identify and handle missing values")
print("  ✓ Fix data types and formats")
print("  ✓ Standardize text data")
print("  ✓ Detect and fix outliers")
print("  ✓ Remove duplicates")
print("  ✓ Create useful features")
print("  ✓ Validate final dataset")
