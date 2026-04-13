#!/usr/bin/env python3
"""Day 12, Lesson 4: DuckDB - SQL for Data Analysis

DuckDB: In-process SQL OLAP database engine
Perfect for analyzing data without setting up a server!

Learn:
- Create tables from Python data
- Run SQL queries
- Export to CSV/Parquet
- Aggregate and transform data
"""

import duckdb
import pandas as pd

print("=== DuckDB: SQL Queries on Data ===\n")

# 1. Create sample data
print("1. Creating Sample Sales Data:")
sales_data = {
    'date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse'],
    'quantity': [1, 5, 2, 3, 10],
    'price': [1000, 25, 1000, 75, 25],
    'region': ['US', 'US', 'EU', 'US', 'EU']
}

df = pd.DataFrame(sales_data)
print(df)

# 2. Create DuckDB connection
print("\n2. Creating DuckDB Database:")
conn = duckdb.connect(database=':memory:')

# Register the dataframe as a table
conn.register('sales', df)
print("✓ Created 'sales' table from DataFrame")

# 3. Run SQL queries
print("\n3. SQL Queries:")

# Simple SELECT
print("\nQuery: SELECT all columns")
result = conn.execute("SELECT * FROM sales").fetchall()
for row in result[:3]:
    print(f"  {row}")

# Aggregation
print("\nQuery: Total revenue by product")
result = conn.execute("""
    SELECT product, SUM(quantity * price) as revenue
    FROM sales
    GROUP BY product
    ORDER BY revenue DESC
""").fetchall()
for row in result:
    print(f"  {row[0]}: ${row[1]:,.2f}")

# Complex query
print("\nQuery: Average price by region")
result = conn.execute("""
    SELECT region, AVG(price) as avg_price, COUNT(*) as transactions
    FROM sales
    GROUP BY region
""").fetchdf()
print(result)

# 4. Subqueries & Filters
print("\n4. Filtering & Aggregation:")
high_value = conn.execute("""
    SELECT date, product, (quantity * price) as total
    FROM sales
    WHERE (quantity * price) > 100
    ORDER BY total DESC
""").fetchdf()
print("High-value transactions (> $100):")
print(high_value)

# 5. Joins (with created table)
print("\n5. Working with Multiple Tables:")

# Create another table
regions = pd.DataFrame({
    'region': ['US', 'EU'],
    'population': [331000000, 447706209]
})

conn.register('regions', regions)

# Join query
joined = conn.execute("""
    SELECT s.region, s.product, SUM(s.quantity) as units_sold, r.population
    FROM sales s
    JOIN regions r ON s.region = r.region
    GROUP BY s.region, s.product, r.population
""").fetchdf()
print("Sales by region with population data:")
print(joined)

# 6. Export results
print("\n6. Export Results:")

# To CSV
conn.execute("COPY (SELECT * FROM sales) TO 'sales_export.csv' (FORMAT CSV, HEADER)")
print("✓ Exported to sales_export.csv")

# To Parquet
conn.execute("COPY (SELECT * FROM sales) TO 'sales_export.parquet'")
print("✓ Exported to sales_export.parquet")

# 7. Performance stats
print("\n7. Query Performance:")
print("DuckDB Uses EXPLAIN to show query plans:")
plan = conn.execute("EXPLAIN SELECT COUNT(*) FROM sales").fetchall()
print("Query optimization available for complex queries")

# 8. Window functions
print("\n8. Advanced: Window Functions")
window_result = conn.execute("""
    SELECT 
        date,
        product,
        quantity,
        SUM(quantity) OVER (PARTITION BY product ORDER BY date) as running_total
    FROM sales
""").fetchdf()
print("Running total by product:")
print(window_result)

print("\n✅ DuckDB lesson complete!")
print("\n🎯 Key Takeaways:")
print("  • DuckDB = SQL without database setup")
print("  • Faster than pandas for many operations")
print("  • Perfect for data analysis and reporting")
print("  • Easy integration with Python DataFrames")
