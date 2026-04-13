"""
Day 9, Lesson 4: Advanced Charting
Covers:
  - Subplots
  - Multiple charts in one figure
  - Annotations and arrows
  - Custom styling
  - 3D-like effects with pie charts
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ============================================
# 1. Subplots (Multiple charts in one figure)
# ============================================

print("=" * 50)
print("Subplots")
print("=" * 50)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [15000, 18000, 16000, 22000, 25000, 28000]
expenses = [10000, 11000, 12000, 14000, 15000, 16000]
profit = [x - y for x, y in zip(revenue, expenses)]

# Create a 1x3 grid of subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: Revenue
axes[0].plot(months, revenue, marker='o', color='green', linewidth=2)
axes[0].set_title("Revenue Trend")
axes[0].set_ylabel("Amount ($)")
axes[0].grid(True, alpha=0.3)

# Plot 2: Expenses
axes[1].plot(months, expenses, marker='s', color='red', linewidth=2)
axes[1].set_title("Expenses Trend")
axes[1].set_ylabel("Amount ($)")
axes[1].grid(True, alpha=0.3)

# Plot 3: Profit
axes[2].plot(months, profit, marker='^', color='blue', linewidth=2)
axes[2].set_title("Profit Trend")
axes[2].set_ylabel("Amount ($)")
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("07_subplots.png")
print("✅ Saved: 07_subplots.png")
plt.show()

# ============================================
# 2. Different chart types in subplots
# ============================================

print("\n" + "=" * 50)
print("Mixed Chart Types")
print("=" * 50)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top-left: Line
axes[0, 0].plot(months, revenue, marker='o', color='green')
axes[0, 0].set_title("Line Plot")
axes[0, 0].grid(True, alpha=0.3)

# Top-right: Bar
cities = ["Amman", "Zarqa", "Irbid", "Aqaba"]
sales = [45000, 32000, 28000, 18000]
axes[0, 1].bar(cities, sales, color='#4ECDC4')
axes[0, 1].set_title("Bar Chart")
axes[0, 1].tick_params(axis='x', rotation=45)

# Bottom-left: Scatter
np.random.seed(42)
x = np.random.randn(50) * 2 + 5
y = x * 1.5 + np.random.randn(50) * 2
axes[1, 0].scatter(x, y, color='#FF6B6B', alpha=0.6)
axes[1, 0].set_title("Scatter Plot")

# Bottom-right: Histogram
scores = np.random.normal(75, 12, 200)
axes[1, 1].hist(scores, bins=15, color='#95E1D3', edgecolor='black')
axes[1, 1].set_title("Histogram")

plt.tight_layout()
plt.savefig("08_mixed_charts.png")
print("✅ Saved: 08_mixed_charts.png")
plt.show()

# ============================================
# 3. Pie Chart
# ============================================

print("\n" + "=" * 50)
print("Pie Chart")
print("=" * 50)

budget = [35000, 25000, 20000, 15000, 5000]
categories = ["Salaries", "Marketing", "Operations", "Technology", "Other"]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(budget, labels=categories, autopct='%1.1f%%',
                                     colors=colors, startangle=90, textprops={'fontsize': 11})

# Make percentage text bold
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

plt.title("Budget Distribution", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig("09_pie_chart.png")
print("✅ Saved: 09_pie_chart.png")
plt.show()

# ============================================
# 4. Annotations and Arrows
# ============================================

print("\n" + "=" * 50)
print("Annotations and Highlights")
print("=" * 50)

fig, ax = plt.subplots(figsize=(11, 6))

# Plot line
ax.plot(months, revenue, marker='o', color='green', linewidth=2, label='Revenue')

# Annotate peaks
max_idx = revenue.index(max(revenue))
ax.annotate('Peak Sales!',
            xy=(max_idx, revenue[max_idx]),
            xytext=(max_idx + 0.5, revenue[max_idx] + 3000),
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=12, fontweight='bold', color='red')

# Highlight a specific point
ax.scatter([max_idx], [revenue[max_idx]], color='red', s=200, zorder=5)

ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Revenue ($)", fontsize=12)
ax.set_title("Revenue with Annotations", fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("10_annotations.png")
print("✅ Saved: 10_annotations.png")
plt.show()

# ============================================
# 5. Styling and Colors
# ============================================

print("\n" + "=" * 50)
print("Custom Styling")
print("=" * 50)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Dark background style
axes[0].set_facecolor('#f0f0f0')
axes[0].plot(months, revenue, marker='o', color='#2E86AB', linewidth=3, markersize=8)
axes[0].set_title("Modern Style", fontsize=14, fontweight='bold')
axes[0].grid(True, alpha=0.2, color='white')
axes[0].set_ylabel("Revenue ($)")

# Minimalist style
axes[1].plot(months, revenue, color='black', linewidth=2)
axes[1].set_title("Minimalist Style", fontsize=14, fontweight='bold')
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)
axes[1].grid(True, alpha=0.2, axis='y')
axes[1].set_ylabel("Revenue ($)")

plt.tight_layout()
plt.savefig("11_styling.png")
print("✅ Saved: 11_styling.png")
plt.show()

# ============================================
# 6. DataFrame Grouping and Plotting
# ============================================

print("\n" + "=" * 50)
print("Group and Plot")
print("=" * 50)

# Create sample sales data
df = pd.DataFrame({
    "City": ["Amman", "Zarqa", "Irbid", "Amman", "Zarqa", "Irbid"],
    "Q": ["Q1", "Q1", "Q1", "Q2", "Q2", "Q2"],
    "Sales": [45000, 32000, 28000, 52000, 38000, 31000]
})

# Pivot for easier plotting
pivot = df.pivot(index='City', columns='Q', values='Sales')

fig, ax = plt.subplots(figsize=(10, 6))
pivot.plot(kind='bar', ax=ax, color=['#FF6B6B', '#4ECDC4'])

ax.set_title("Quarterly Sales by City", fontsize=14, fontweight='bold')
ax.set_ylabel("Sales ($)")
ax.set_xlabel("City")
ax.legend(title="Quarter")
plt.tight_layout()
plt.savefig("12_grouped_data.png")
print("✅ Saved: 12_grouped_data.png")
plt.show()

print("\n✅ Lesson 4 Complete!")
print("\nCharts saved in current directory:")
print("  - 07_subplots.png through 12_grouped_data.png")
