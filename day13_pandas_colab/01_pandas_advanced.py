"""Day 13, Lessons 1-3: Advanced Pandas"""
import pandas as pd
import numpy as np

print("=== Advanced Pandas ===\n")

# Create sample data
sales = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=10),
    'product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'A', 'B', 'C'],
    'quantity': [10, 20, 15, 30, 25, 12, 18, 14, 22, 28],
    'price': [100, 200, 100, 150, 200, 100, 150, 100, 200, 150]
})

sales['total'] = sales['quantity'] * sales['price']

print("Dataset:")
print(sales.head())

print("\n=== Groupby & Pivot ===")

# Groupby
product_sales = sales.groupby('product')['total'].sum()
print("\nSales by product:")
print(product_sales)

# Pivot table
pivot = sales.pivot_table(
    values='quantity',
    index='product',
    columns=pd.Grouper(key='date', freq='5D'),
    aggfunc='sum'
)
print("\nPivot table:")
print(pivot)

print("\n=== Time Series Analysis ===")

sales_by_date = sales.groupby('date')['total'].sum()
print("\nDaily sales:")
print(sales_by_date)

# Moving average
print("\n7-day moving average:")
print(sales_by_date.rolling(window=3).mean())

print("\n✅ Day 13 lessons complete!")
