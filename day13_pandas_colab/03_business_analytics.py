#!/usr/bin/env python3
"""Day 13, Lesson 3: Business Analytics - Real-World Data Insights

Transform data into actionable business intelligence:
- Customer segmentation
- Cohort analysis
- Revenue forecasting
- Trend detection
- Performance metrics
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("=== Business Analytics: From Data to Insights ===\n")

# 1. Generate realistic e-commerce dataset
print("1. Loading E-Commerce Dataset:")
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=365, freq='D')

transactions = []
for date in dates:
    n_transactions = np.random.randint(10, 50)
    for _ in range(n_transactions):
        transactions.append({
            'date': date,
            'customer_id': np.random.randint(1, 200),
            'product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard']),
            'quantity': np.random.randint(1, 5),
            'unit_price': np.random.choice([1000, 800, 500, 300, 100]),
            'region': np.random.choice(['North', 'South', 'East', 'West'])
        })

df = pd.DataFrame(transactions)
df['total_amount'] = df['quantity'] * df['unit_price']

print(f"Dataset: {len(df)} transactions, {df['date'].min().date()} to {df['date'].max().date()}")
print(f"Unique customers: {df['customer_id'].nunique()}")
print(f"Products: {df['product'].unique()}")

# 2. Key performance metrics
print("\n2. Key Performance Indicators:")
total_revenue = df['total_amount'].sum()
avg_transaction = df['total_amount'].mean()
transactions_count = len(df)

print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Average Transaction: ${avg_transaction:.2f}")
print(f"Total Transactions: {transactions_count:,}")
print(f"Daily Average: ${total_revenue/365:,.2f}")

# 3. Revenue by product
print("\n3. Product Performance:")
product_revenue = df.groupby('product').agg({
    'total_amount': ['sum', 'mean', 'count'],
    'quantity': 'sum'
}).round(2)

product_revenue.columns = ['Revenue', 'Avg Trans', 'Transactions', 'Units Sold']
product_revenue = product_revenue.sort_values('Revenue', ascending=False)
print(product_revenue)

# 4. Geographic analysis
print("\n4. Regional Performance:")
regional = df.groupby('region').agg({
    'total_amount': 'sum',
    'customer_id': 'nunique',
    'quantity': 'sum'
}).round(2)
regional.columns = ['Revenue', 'Customers', 'Units']
regional['Avg Revenue per Customer'] = (regional['Revenue'] / regional['Customers']).round(2)
print(regional)

# 5. Customer segmentation
print("\n5. Customer Segmentation (RFM Analysis):")
# Recency, Frequency, Monetary
customer_stats = df.groupby('customer_id').agg({
    'date': ['min', 'max'],
    'total_amount': ['sum', 'count'],
    'quantity': 'sum'
})

customer_stats.columns = ['First Purchase', 'Last Purchase', 'Total Spent', 'Transactions', 'Units']
customer_stats['Days Since Last'] = (df['date'].max() - customer_stats['Last Purchase']).dt.days

# Segment by spending
customer_stats['Segment'] = pd.cut(customer_stats['Total Spent'], 
                                    bins=[0, 2000, 5000, 100000],
                                    labels=['Bronze', 'Silver', 'Gold'])

print("\nCustomer Segments:")
print(customer_stats.groupby('Segment').agg({
    'Total Spent': 'mean',
    'Transactions': 'mean',
    'Days Since Last': 'mean'
}).round(2))

# 6. Time-series analysis
print("\n6. Monthly Trends:")
df['year_month'] = df['date'].dt.to_period('M')
monthly = df.groupby('year_month')['total_amount'].agg(['sum', 'count', 'mean'])
monthly.columns = ['Revenue', 'Transactions', 'Avg Order']
print(monthly.tail(6))

# 7. Cohort analysis
print("\n7. Cohort Analysis (Customer retention):")
df['cohort_month'] = df.groupby('customer_id')['date'].transform('min').dt.to_period('M')
df['months_since_first'] = (df['date'].dt.to_period('M') - df['cohort_month']).apply(lambda x: x.n)

cohort = df.groupby(['cohort_month', 'months_since_first'])['customer_id'].nunique().unstack(fill_value=0)
print("Customers by cohort (sample - first 3 cohorts):")
print(cohort.iloc[:3, :6])

# 8. Trend detection
print("\n8. Trend Analysis:")
daily_revenue = df.groupby('date')['total_amount'].sum()

# 7-day moving average
ma_7 = daily_revenue.rolling(window=7).mean()
trend = "📈 UP" if daily_revenue.iloc[-1] > daily_revenue.iloc[-30] else "📉 DOWN"

print(f"Last 7 days average: ${ma_7.iloc[-1]:,.2f}")
print(f"30-day trend: {trend}")
print(f"Volatility (std dev): ${daily_revenue.std():,.2f}")

# 9. Customer lifetime value (CLV)
print("\n9. Customer Lifetime Value:")
clv = df.groupby('customer_id')['total_amount'].sum().describe()
print(f"Average CLV: ${clv['mean']:,.2f}")
print(f"Median CLV: ${clv['50%']:,.2f}")
print(f"Top 10% threshold: ${clv['75%']:,.2f}")

top_customers = df.groupby('customer_id')['total_amount'].sum().nlargest(5)
print("\nTop 5 Customers:")
for cid, value in top_customers.items():
    print(f"  Customer {cid}: ${value:,.2f}")

# 10. Forecasting (simple)
print("\n10. Simple Revenue Forecast:")
from sklearn.linear_model import LinearRegression

X = np.arange(len(daily_revenue)).reshape(-1, 1)
y = daily_revenue.values
model = LinearRegression().fit(X, y)

# Predict next 30 days
future_X = np.arange(len(daily_revenue), len(daily_revenue) + 30).reshape(-1, 1)
forecast = model.predict(future_X)
forecast_revenue = forecast.sum()

print(f"30-day forecast: ${forecast_revenue:,.2f}")
print(f"Daily average forecast: ${forecast.mean():,.2f}")

print("\n✅ Business analytics lesson complete!")
print("\n📊 Key Insights Generated:")
print(f"  • Top product: {product_revenue.index[0]}")
print(f"  • Top region: {regional['Revenue'].idxmax()}")
print(f"  • Customer segments identified: 3")
print(f"  • Revenue forecast available ✓")
