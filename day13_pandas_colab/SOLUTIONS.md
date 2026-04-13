# ✅ Day 13: Pandas & Analytics - SOLUTIONS

## Solution 1: Advanced Grouping

```python
import pandas as pd

df = pd.read_csv('sales.csv')

# Group by product and calculate
summary = df.groupby('product').agg({
    'quantity': 'sum',
    'price': ['mean', 'max'],
    'order_id': 'count'
}).round(2)

print(summary)

# Pivot table
pivot = df.pivot_table(
    values='quantity',
    index='product',
    columns='month',
    aggfunc='sum'
)
print(pivot)
```

## Solution 2: Data Merging

```python
customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')

# Merge on customer_id
merged = pd.merge(customers, orders, on='customer_id', how='inner')

# Group to find top customers
top_customers = merged.groupby('name')['amount'].sum().sort_values(ascending=False).head(5)
print(top_customers)
```

## Solution 3: Business Analytics

```python
sales = pd.read_csv('sales.csv')

# Daily trends
sales['date'] = pd.to_datetime(sales['date'])
daily_sales = sales.groupby(sales['date'].dt.date)['amount'].sum()
print(daily_sales)

# Top products
top_products = sales.groupby('product')['amount'].sum().nlargest(5)
print(top_products)

# Profit margin
sales['profit_margin'] = ((sales['price'] - sales['cost']) / sales['price'] * 100).round(2)
print(sales[['product', 'profit_margin']])
```
