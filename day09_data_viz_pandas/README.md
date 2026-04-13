# 🎯 Day 9: Data Analysis & Visualization with Pandas & Matplotlib (3 hours)

## 📚 Topics Covered

| Topic | File | Duration | What You'll Learn |
|-------|------|----------|-------------------|
| **Pandas Intro & DataFrames** | `01_pandas_intro.py` | 30min | Series, DataFrames, basic operations |
| **Data Cleaning** | `02_data_cleaning.py` | 45min | Handling NaN, duplicates, type conversion |
| **Matplotlib Basics** | `03_matplotlib_basics.py` | 30min | Line plots, bar charts, scatter plots |
| **Advanced Charting** | `04_advanced_charts.py` | 30min | Subplots, annotations, styling |
| **Exercises & Solutions** | `EXERCISES.md`, `SOLUTIONS.md` | 45min | Hands-on data projects |

---

## 🎓 Learning Outcomes

By the end of Day 9, you should understand:

✅ What DataFrames are and how to create them  
✅ How to load CSV files with `pd.read_csv()`  
✅ How to filter, select, and group data  
✅ How to handle missing values (NaN) and duplicates  
✅ How to create line, bar, and scatter plots  
✅ How to save processed data and charts as files  

---

## 🚀 Quick Start

### Run the examples:
```bash
python 01_pandas_intro.py
python 02_data_cleaning.py
python 03_matplotlib_basics.py
python 04_advanced_charts.py
```

### Try the exercises:
```bash
# Read EXERCISES.md and solve them
# Check your solutions against SOLUTIONS.md
```

---

## 🧠 Key Concepts at a Glance

### **Creating a DataFrame**
```python
import pandas as pd

# From dictionary
data = {"name": ["Ali", "Hana", "Omar"], "age": [25, 30, 28]}
df = pd.DataFrame(data)

# From CSV
df = pd.read_csv("sales.csv")
```

### **Filtering & Grouping**
```python
# Filter rows where age > 25
filtered = df[df["age"] > 25]

# Group by city and sum sales
summary = df.groupby("city")["sales"].sum()
```

### **Handling Missing Data**
```python
# Drop rows with NaN
df_clean = df.dropna()

# Fill NaN with default value
df.fillna(0, inplace=True)
```

### **Creating Charts**
```python
import matplotlib.pyplot as plt

# Line plot
plt.plot(df["month"], df["revenue"])
plt.show()

# Bar chart
df.plot(kind="bar", x="city", y="sales")
plt.savefig("sales_chart.png")
```

---

## 📊 Mini Project: Sales Data Analysis

**Scenario:** You have sales data for multiple cities. Clean it, analyze trends, and create charts.

**Steps:**
1. Load `sales.csv` into a DataFrame
2. Remove NaN values and duplicates
3. Group by city and calculate total revenue
4. Create a bar chart of revenue by city
5. Save the cleaned data as `sales_clean.csv`
6. Save the chart as `revenue_chart.png`

---

## 🎯 Focus Areas

- **Data Integrity:** Always check data shape and dtypes first
- **Readable Output:** Use `.head()`, `.info()`, `.describe()` to explore
- **Proper Export:** Save results with meaningful filenames
- **Chart Clarity:** Label axes, add titles, use color wisely
