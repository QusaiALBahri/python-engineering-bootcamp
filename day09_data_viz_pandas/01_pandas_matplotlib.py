# Day 9: Data Science with Pandas & Matplotlib

## Learning Outcomes

- Load, clean, and analyze data with **Pandas**
- Create professional visualizations with **Matplotlib**
- Understand data pipelines
- Perform basic statistical analysis

---

## Part 1: Pandas Basics

### Loading Data
```python
import pandas as pd

# From CSV
df = pd.read_csv("data.csv")

# From Dictionary
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "salary": [50000, 60000, 75000]
}
df = pd.DataFrame(data)
```

### Exploring Data
```python
df.head()       # First 5 rows
df.info()       # Column info
df.describe()   # Statistics
df.shape        # (rows, columns)
```

### Selecting Data
```python
df["age"]                   # Select column
df[["name", "age"]]        # Multiple columns
df[df["age"] > 25]         # Filter rows
df.loc[0]                  # Row by index
df.iloc[0]                 # Row by position
```

### Data Manipulation
```python
df["age_group"] = pd.cut(df["age"], bins=[0, 30, 40, 50])
df["salary_thousands"] = df["salary"] / 1000
df.sort_values("salary", ascending=False)
df.groupby("age_group")["salary"].mean()
```

---

## Part 2: Matplotlib Basics

### Line Plot
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, label="y=x²")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.show()
```

### Bar Chart
```python
categories = ["A", "B", "C"]
values = [10, 24, 36]
plt.bar(categories, values)
plt.ylabel("Count")
plt.show()
```

### Histogram
```python
scores = [72, 85, 90, 78, 88, 92, 75, 81, 87, 95]
plt.hist(scores, bins=5)
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()
```

### Scatter Plot
```python
ages = [25, 30, 35, 40, 45]
salaries = [50000, 60000, 75000, 85000, 100000]
plt.scatter(ages, salaries)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()
```

---

## Part 3: Real-World Example

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load student data
students = pd.read_csv("students.csv")

# Analysis 1: Average score by subject
avg_by_subject = students.groupby("subject")["score"].mean()
print(avg_by_subject)

# Analysis 2: Grade distribution
grades = pd.cut(students["score"], bins=[0, 60, 70, 80, 90, 100], 
                labels=["F", "D", "C", "B", "A"])

# Visualization 1: Bar chart of grade distribution
plt.figure(figsize=(10, 6))
grades.value_counts().plot(kind="bar")
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Visualization 2: Scatter plot of study hours vs score
plt.scatter(students["study_hours"], students["score"])
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.title("Study Hours vs Score")
plt.show()

# Statistics
print(f"Average score: {students['score'].mean():.2f}")
print(f"Median score: {students['score'].median():.2f}")
print(f"Std deviation: {students['score'].std():.2f}")
```

---

## Key Concepts

| Concept | Purpose |
|---------|---------|
| **DataFrame** | Table with rows and columns |
| **Series** | Single column of data |
| **groupby()** | Aggregate by categories |
| **merge()** | Join multiple datasets |
| **plot()** | Visualize data |
| **describe()** | Quick statistics |

---

## Common Tasks

```python
# Filter
df[df["age"] > 30]

# Sort
df.sort_values("salary", ascending=False)

# Group and aggregate
df.groupby("department")["salary"].mean()

# Create new column
df["bonus"] = df["salary"] * 0.1

# Handle missing data
df.fillna(0)
df.dropna()

# Merge datasets
merged = pd.merge(df1, df2, on="id")
```

---

## Next Steps

- [ ] Install pandas: `pip install pandas matplotlib`
- [ ] Load a CSV file
- [ ] Create at least 3 visualizations
- [ ] Calculate basic statistics
- [ ] See EXERCISES.md for challenges
