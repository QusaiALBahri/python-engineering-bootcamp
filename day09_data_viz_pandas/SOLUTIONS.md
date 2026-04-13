# ✅ Day 9: Data Analysis & Visualization - SOLUTIONS

## Solution 1: Loading and Exploring Data

```python
import pandas as pd

# Load the CSV
df = pd.read_csv('students.csv')

# Print shape
print("Shape:", df.shape)  # (5, 4)

# Print data types
print("\nData types:")
print(df.dtypes)

# Print summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Print first 3 rows
print("\nFirst 3 rows:")
print(df.head(3))
```

**Expected Output:**
```
Shape: (5, 4)

Data types:
name      object
age        int64
gpa      float64
major     object
dtype: object

Summary Statistics:
           age       gpa
count   5.0  5.0
mean   22.4  3.64
std     1.14 0.18
min    21.0  3.40
25%    22.0  3.50
50%    22.0  3.60
75%    23.0  3.80
max    24.0  3.90
```

---

## Solution 2: Data Cleaning

```python
import pandas as pd

# Load the messy data
df = pd.read_csv('messy_sales.csv')

print("Original shape:", df.shape)
print(df)

# Step 1: Remove duplicates
df = df.drop_duplicates()
print("\nAfter removing duplicates:")
print(df)

# Step 2: Remove rows with missing amount
df = df.dropna(subset=['amount'])
print("\nAfter removing missing amounts:")
print(df)

# Step 3: Convert amount to numeric
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df = df.dropna(subset=['amount'])  # Remove rows where conversion failed

# Step 4: Standardize status column
df['status'] = df['status'].str.lower().str.strip()
df['status'] = df['status'].replace('completed', 'complete')

# Step 5: Filter for complete status
df = df[df['status'] == 'complete']

print("\nCleaned data:")
print(df)

# Save cleaned data
df.to_csv('sales_clean.csv', index=False)
print("\n✅ Saved to sales_clean.csv")
```

**Expected Output:**
```
Original shape: (6, 4)
   date      city amount     status
0  2024-01-15  Amman   5000.0   Complete
1  2024-01-16  Zarqa    NaN    Pending
2  2024-01-17  Irbid   3000.0   Complete
3  2024-01-17  Irbid   3000.0  Completed
4  2024-01-18  Amman    invalid  Process
5  2024-01-19  Aqaba   2000.0   Complete

Cleaned data: (4 rows)
```

---

## Solution 3: Grouping and Aggregation

```python
import pandas as pd

# Load cleaned data
df = pd.read_csv('sales_clean.csv')

# Group by city
city_stats = df.groupby('city')['amount'].agg([
    ('Total Sales', 'sum'),
    ('Avg Sales', 'mean'),
    ('Transactions', 'count')
]).round(2)

# Sort by Total Sales descending
city_stats = city_stats.sort_values('Total Sales', ascending=False)

print(city_stats)

# Alternative: prettier output
print("\n{:<12} {:>12} {:>12} {:>12}".format("City", "Total Sales", "Avg Sales", "Transactions"))
print("-" * 50)
for city, row in city_stats.iterrows():
    print("{:<12} ${:>11,.2f} ${:>11,.2f} {:>12.0f}".format(
        city, row['Total Sales'], row['Avg Sales'], row['Transactions']))
```

**Expected Output:**
```
           Total Sales  Avg Sales  Transactions
city                                           
Amman         10000.0   5000.00             2.0
Irbid          3000.0   3000.00             1.0
Aqaba          2000.0   2000.00             1.0
```

---

## Solution 4: Simple Line Plot

```python
import matplotlib.pyplot as plt

# Create data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [12000, 15000, 18000, 16000, 22000, 25000]

# Create figure
plt.figure(figsize=(10, 6))
plt.plot(months, revenue, marker='o', linewidth=2, markersize=8, color='#2E86AB')

# Customize
plt.title("Monthly Revenue", fontsize=14, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)
plt.grid(True, alpha=0.3)

# Save and show
plt.tight_layout()
plt.savefig('revenue_chart.png', dpi=300)
print("Chart saved successfully")
plt.show()
```

---

## Solution 5: Bar Chart Comparison

```python
import matplotlib.pyplot as plt
import numpy as np

# Data
cities = ["Amman", "Zarqa", "Irbid", "Aqaba"]
sales = [45000, 32000, 28000, 18000]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']

# Create figure
plt.figure(figsize=(10, 6))
bars = plt.bar(cities, sales, color=colors, edgecolor='black', linewidth=1.5)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'${height:,.0f}',
             ha='center', va='bottom', fontsize=11, fontweight='bold')

# Customize
plt.title("Sales by City", fontsize=14, fontweight='bold')
plt.xlabel("City", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)
plt.grid(True, alpha=0.3, axis='y')

# Save and show
plt.tight_layout()
plt.savefig('sales_by_city.png', dpi=300)
print("Chart saved successfully")
plt.show()
```

---

## Solution 6: Multiple Subplots

```python
import matplotlib.pyplot as plt
import numpy as np

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [12000, 15000, 18000, 16000, 22000, 25000]
cities = ["Amman", "Zarqa", "Irbid", "Aqaba"]
city_sales = [45000, 32000, 28000, 18000]

# Create 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Top-left: Line chart
axes[0, 0].plot(months, revenue, marker='o', color='green', linewidth=2)
axes[0, 0].set_title("Monthly Revenue", fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel("Revenue ($)")
axes[0, 0].grid(True, alpha=0.3)

# Top-right: Bar chart
axes[0, 1].bar(cities, city_sales, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'])
axes[0, 1].set_title("Sales by City", fontsize=12, fontweight='bold')
axes[0, 1].set_ylabel("Sales ($)")
axes[0, 1].tick_params(axis='x', rotation=45)

# Bottom-left: Pie chart
axes[1, 0].pie(city_sales, labels=cities, autopct='%1.1f%%', 
               colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'])
axes[1, 0].set_title("Sales Distribution", fontsize=12, fontweight='bold')

# Bottom-right: Histogram
np.random.seed(42)
daily_sales = np.random.uniform(15000, 30000, 20)
axes[1, 1].hist(daily_sales, bins=8, color='#95E1D3', edgecolor='black')
axes[1, 1].set_title("Daily Sales Distribution", fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel("Sales ($)")
axes[1, 1].set_ylabel("Frequency")

# Overall adjustments
fig.suptitle("Sales Dashboard", fontsize=16, fontweight='bold', y=1.00)
plt.tight_layout()
plt.savefig('dashboard.png', dpi=300, bbox_inches='tight')
print("Dashboard saved successfully")
plt.show()
```

---

## Solution 7: Real Data Analysis Pipeline

```python
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load data
df = pd.read_csv('orders.csv')
print("Original data:")
print(df)
print(f"Shape: {df.shape}")

# Step 2: Clean data
# Remove duplicates
df = df.drop_duplicates()
print(f"\nAfter removing duplicates: {df.shape}")

# Fill missing amounts with mean
df['amount'] = df['amount'].fillna(df['amount'].mean())
print("\nAfter filling missing amounts:")
print(df)

# Step 3: Analysis
# By category
category_sales = df.groupby('category')['amount'].sum().sort_values(ascending=False)
print("\nSales by Category:")
print(category_sales)

# By customer
customer_orders = df.groupby('customer').size().sort_values(ascending=False)
print("\nOrders per Customer:")
print(customer_orders)

# Step 4: Visualizations
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar chart
category_sales.plot(kind='bar', ax=axes[0], color='#4ECDC4')
axes[0].set_title("Sales by Category")
axes[0].set_ylabel("Sales ($)")
axes[0].tick_params(axis='x', rotation=45)

# Pie chart
axes[1].pie(category_sales, labels=category_sales.index, autopct='%1.1f%%',
            colors=['#FF6B6B', '#4ECDC4', '#45B7D1'])
axes[1].set_title("Sales Distribution")

plt.tight_layout()
plt.savefig('orders_analysis.png', dpi=300)
print("\n✅ Visualizations saved")

# Step 5: Save cleaned data
df.to_csv('orders_clean.csv', index=False)
print("✅ Cleaned data saved to orders_clean.csv")
```

---

## Solution 8: Challenge - EDA Notebook

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('products.csv')

# 1. Display basic info
print("=" * 50)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 50)
print("\nDataset Shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

# 2. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 3. Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# 4. Group by category
print("\nProducts per Category:")
category_count = df.groupby('category').size()
print(category_count)

print("\nAverage Price by Category:")
avg_price = df.groupby('category')['price'].mean()
print(avg_price)

print("\nTotal Stock by Category:")
total_stock = df.groupby('category')['stock'].sum()
print(total_stock)

# 5. Answer questions
print("\n" + "=" * 50)
print("ANSWERS TO QUESTIONS")
print("=" * 50)
print(f"Q1. Category with most products: {category_count.idxmax()} ({category_count.max()} products)")
print(f"Q2. Average price by category:\n{avg_price}")
print(f"Q3. Product with highest stock: {df.loc[df['stock'].idxmax(), 'name']} ({df['stock'].max()} units)")

# 6. Visualizations
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Scatter: Price vs Stock
axes[0].scatter(df['price'], df['stock'], s=100, color='#45B7D1', alpha=0.6)
axes[0].set_xlabel("Price ($)")
axes[0].set_ylabel("Stock")
axes[0].set_title("Price vs Stock")
axes[0].grid(True, alpha=0.3)

# Bar: Products per category
category_count.plot(kind='bar', ax=axes[1], color='#FF6B6B')
axes[1].set_title("Products per Category")
axes[1].set_ylabel("Count")
axes[1].tick_params(axis='x', rotation=45)

# Histogram: Price distribution
axes[2].hist(df['price'], bins=8, color='#95E1D3', edgecolor='black')
axes[2].set_xlabel("Price ($)")
axes[2].set_ylabel("Frequency")
axes[2].set_title("Price Distribution")

plt.tight_layout()
plt.savefig('eda_analysis.png', dpi=300)
print("\n✅ Visualizations saved to eda_analysis.png")
plt.show()
```

---

## Key Takeaways

✅ **Data Loading:** Use `pd.read_csv()` to load CSV files  
✅ **Data Cleaning:** Remove duplicates, handle NaN values, type conversion  
✅ **Aggregation:** Use `groupby()` and `agg()` for analysis  
✅ **Visualization:** Use matplotlib for charts and pandas `.plot()` method  
✅ **Best Practices:** Always explore data first, clean before analysis, save results  

---

## Common Pitfalls to Avoid

❌ Not checking for missing values before analysis  
❌ Forgetting to convert data types  
❌ Not removing duplicates  
❌ Plotting without proper labels or legends  
❌ Not saving visualizations with good DPI for clarity  
❌ Ignoring outliers that might skew analysis  
