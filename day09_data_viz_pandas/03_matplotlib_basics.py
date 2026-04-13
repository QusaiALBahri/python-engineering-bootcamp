"""
Day 9, Lesson 3: Matplotlib Basics
Covers:
  - Line plots
  - Bar charts
  - Scatter plots
  - Histograms
  - Basic customization (labels, titles, legends)
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create sample data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [15000, 18000, 16000, 22000, 25000, 28000]
expenses = [10000, 11000, 12000, 14000, 15000, 16000]

# ============================================
# 1. Line Plot
# ============================================

print("=" * 50)
print("Line Plot")
print("=" * 50)

plt.figure(figsize=(10, 5))
plt.plot(months, revenue, marker='o', label='Revenue', color='green', linewidth=2)
plt.plot(months, expenses, marker='s', label='Expenses', color='red', linewidth=2)

plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.title("Revenue vs Expenses Over Time")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("01_line_plot.png")
print("✅ Saved: 01_line_plot.png")
plt.show()

# ============================================
# 2. Bar Chart
# ============================================

print("\n" + "=" * 50)
print("Bar Chart")
print("=" * 50)

cities = ["Amman", "Zarqa", "Irbid", "Aqaba"]
sales = [45000, 32000, 28000, 18000]

plt.figure(figsize=(10, 5))
bars = plt.bar(cities, sales, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'])

# Add value labels on bars
for i, (city, sale) in enumerate(zip(cities, sales)):
    plt.text(i, sale + 1000, f"${sale:,}", ha='center', fontsize=10, fontweight='bold')

plt.xlabel("City")
plt.ylabel("Sales ($)")
plt.title("Sales by City")
plt.tight_layout()
plt.savefig("02_bar_chart.png")
print("✅ Saved: 02_bar_chart.png")
plt.show()

# ============================================
# 3. Scatter Plot
# ============================================

print("\n" + "=" * 50)
print("Scatter Plot")
print("=" * 50)

# Generate random data for simplicity
np.random.seed(42)
x = np.random.randn(100) * 2 + 5
y = x * 1.5 + np.random.randn(100) * 2 + 3

plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, s=100, color='#45B7D1')

plt.xlabel("Feature X")
plt.ylabel("Feature Y")
plt.title("Scatter Plot Example")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("03_scatter_plot.png")
print("✅ Saved: 03_scatter_plot.png")
plt.show()

# ============================================
# 4. Histogram
# ============================================

print("\n" + "=" * 50)
print("Histogram")
print("=" * 50)

# Generate test scores
np.random.seed(42)
scores = np.random.normal(loc=75, scale=12, size=200)

plt.figure(figsize=(10, 6))
plt.hist(scores, bins=20, color='#95E1D3', edgecolor='black', alpha=0.7)

plt.xlabel("Score")
plt.ylabel("Frequency")
plt.title("Distribution of Student Scores")
plt.axvline(np.mean(scores), color='red', linestyle='--', linewidth=2, label=f'Mean: {np.mean(scores):.1f}')
plt.axvline(np.median(scores), color='green', linestyle='--', linewidth=2, label=f'Median: {np.median(scores):.1f}')
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig("04_histogram.png")
print("✅ Saved: 04_histogram.png")
plt.show()

# ============================================
# 5. Multiple Series Bar Chart
# ============================================

print("\n" + "=" * 50)
print("Grouped Bar Chart")
print("=" * 50)

quarters = ["Q1", "Q2", "Q3", "Q4"]
product_a = [45000, 52000, 48000, 61000]
product_b = [38000, 41000, 39000, 45000]
product_c = [32000, 35000, 40000, 42000]

x_pos = np.arange(len(quarters))
width = 0.25

plt.figure(figsize=(12, 6))
plt.bar(x_pos - width, product_a, width, label='Product A', color='#FF6B6B')
plt.bar(x_pos, product_b, width, label='Product B', color='#4ECDC4')
plt.bar(x_pos + width, product_c, width, label='Product C', color='#45B7D1')

plt.xlabel("Quarter")
plt.ylabel("Sales ($)")
plt.title("Sales by Product and Quarter")
plt.xticks(x_pos, quarters)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig("05_grouped_bar.png")
print("✅ Saved: 05_grouped_bar.png")
plt.show()

# ============================================
# 6. Using DataFrames Directly
# ============================================

print("\n" + "=" * 50)
print("Plotting from DataFrames")
print("=" * 50)

df = pd.DataFrame({
    "Month": months,
    "Revenue": revenue,
    "Expenses": expenses
})

# Pandas makes plotting easy
df.plot(x="Month", y=["Revenue", "Expenses"], kind="line", figsize=(10, 5))
plt.title("DataFrame Plot Example")
plt.ylabel("Amount ($)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("06_dataframe_plot.png")
print("✅ Saved: 06_dataframe_plot.png")
plt.show()

# ============================================
# 7. Customization Tips
# ============================================

print("\n" + "=" * 50)
print("Customization Tips")
print("=" * 50)

print("""
Useful matplotlib functions:
  - plt.figure(figsize=(w, h))    : Set figure size
  - plt.title(), plt.xlabel(), plt.ylabel()  : Add labels
  - plt.legend()                  : Show legend
  - plt.grid()                    : Add grid
  - plt.tight_layout()            : Adjust spacing
  - plt.savefig("name.png")       : Save figure
  - plt.show()                    : Display figure
  
Color options:
  - Named colors: 'red', 'blue', 'green', etc.
  - Hex colors: '#FF6B6B', '#4ECDC4'
  - CSS colors: 'lightcoral', 'steelblue'
  
Marker styles:
  - 'o' : circle, 's' : square, '^' : triangle
  - 'd' : diamond, '*' : star, 'x' : X mark
""")

print("\n✅ Lesson 3 Complete!")
