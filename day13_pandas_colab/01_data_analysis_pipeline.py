# Day 13: Data Analysis Workshop

## Learning Outcomes

- Complete data analysis pipeline
- Clean and prepare data
- Perform exploratory analysis
- Create insights from data

---

## The Data Pipeline

1. **Load** - Read raw data
2. **Inspect** - Check for issues
3. **Clean** - Fix problems
4. **Analyze** - Find insights
5. **Visualize** - Create charts
6. **Report** - Communicate results

---

## Complete Example: Student Performance Analysis

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. LOAD
df = pd.read_csv("student_data.csv")

# 2. INSPECT
print(df.head())
print(df.info())
print(df.describe())

# 3. CLEAN
# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df["score"] = df["score"].fillna(df["score"].mean())

# Remove outliers
Q1 = df["score"].quantile(0.25)
Q3 = df["score"].quantile(0.75)
IQR = Q3 - Q1
df = df[(df["score"] >= Q1 - 1.5*IQR) & (df["score"] <= Q3 + 1.5*IQR)]

# 4. ANALYZE
print("\n=== Analysis ===")
print(f"Average score: {df['score'].mean():.2f}")
print(f"Median score: {df['score'].median():.2f}")
print(f"Std Dev: {df['score'].std():.2f}")

# By major
by_major = df.groupby("major")["score"].agg(["mean", "count", "std"])
print(by_major)

# Correlations
print(df[["study_hours", "score", "attendance"]].corr())

# 5. VISUALIZE
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Histogram
axes[0, 0].hist(df["score"], bins=20)
axes[0, 0].set_title("Score Distribution")

# Box plot by major
df.boxplot(column="score", by="major", ax=axes[0, 1])
axes[0, 1].set_title("Score by Major")

# Scatter: study hours vs score
axes[1, 0].scatter(df["study_hours"], df["score"])
axes[1, 0].set_xlabel("Study Hours")
axes[1, 0].set_ylabel("Score")

# Correlation heatmap
corr_matrix = df[["study_hours", "score", "attendance"]].corr()
axes[1, 1].imshow(corr_matrix, cmap="coolwarm")
axes[1, 1].set_title("Correlation Matrix")

plt.tight_layout()
plt.show()

# 6. REPORT
print("\n=== Report ===")
print(f"Total students: {len(df)}")
print(f"Average score: {df['score'].mean():.2f}")
print(f"Best major: {df.groupby('major')['score'].mean().idxmax()}")
print(f"Correlation (study vs score): {df['study_hours'].corr(df['score']):.3f}")
```

---

## Common Cleaning Tasks

### Handle Missing Data
```python
df.dropna()  # Remove rows with NaN
df.fillna(0)  # Replace with 0
df.fillna(method='ffill')  # Forward fill
```

### Remove Duplicates
```python
df.drop_duplicates()
df.drop_duplicates(subset=['id'])
```

### Fix Data Types
```python
df['date'] = pd.to_datetime(df['date'])
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
```

### Create Categories
```python
df['grade'] = pd.cut(df['score'], 
                     bins=[0, 60, 70, 80, 90, 100],
                     labels=['F', 'D', 'C', 'B', 'A'])
```

---

## Statistical Analysis

```python
# Basic stats
df['score'].mean()
df['score'].median()
df['score'].std()
df['score'].min()
df['score'].max()

# Percentiles
df['score'].quantile(0.25)  # Q1
df['score'].quantile(0.75)  # Q3

# Correlation
df[['col1', 'col2']].corr()

# Grouping
df.groupby('major')['score'].mean()
df.groupby('major').agg({'score': ['mean', 'count', 'std']})
```

---

## Key Visualization Types

| Chart | Use |
|-------|-----|
| **Histogram** | Distribution of values |
| **Box Plot** | Compare distributions |
| **Scatter** | Relationship between 2 variables |
| **Line** | Trends over time |
| **Bar** | Compare categories |

---

## Practice Problems

1. Load a dataset, describe it
2. Clean missing/invalid data
3. Calculate statistics
4. Find correlations
5. Create at least 3 visualizations
6. Write conclusions

---

## Next Steps

- [ ] Find a real dataset (Kaggle, UCI)
- [ ] Complete the full pipeline
- [ ] Create a report with visualizations
- [ ] Practice statistical analysis
