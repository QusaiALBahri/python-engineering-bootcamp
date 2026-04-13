# 📝 Day 9: Data Analysis & Visualization - EXERCISES

## Exercise 1: Loading and Exploring Data

**Scenario:** Create a CSV file with student data and analyze it.

**Task:**
1. Create a file called `students.csv` with the following data:
   ```
   name,age,gpa,major
   Ali,22,3.8,Computer Science
   Hana,21,3.6,Engineering
   Omar,23,3.4,Business
   Fatima,22,3.9,Medicine
   Ahmed,24,3.5,Law
   ```

2. Load this CSV into a DataFrame using `pd.read_csv()`
3. Print the following:
   - DataFrame shape
   - Column data types
   - Summary statistics (`.describe()`)
   - First 3 rows

**Expected Output:**
- Shape: (5, 4)
- Data types: name (object), age (int), gpa (float), major (object)
- Mean age, mean GPA, etc.

---

## Exercise 2: Data Cleaning

**Scenario:** Clean a messy dataset.

**Task:**
1. Create a file called `messy_sales.csv` with:
   ```
   date,city,amount,status
   2024-01-15,Amman,5000,Complete
   2024-01-16,Zarqa,,Pending
   2024-01-17,Irbid,3000,Complete
   2024-01-17,Irbid,3000,Completed
   2024-01-18,Amman,invalid,Process
   2024-01-19,Aqaba,2000,Complete
   ```

2. Load the CSV and clean it:
   - Remove duplicate rows
   - Handle missing values in the `amount` column (drop them)
   - Standardize the `status` column (make it lowercase and consistent)
   - Convert `amount` to numeric type
   - Filter for only "complete" status

3. Save the cleaned data to `sales_clean.csv`

**Expected Result:**
- 4 rows of clean data with valid amounts and consistent status
- File saved with correct format

---

## Exercise 3: Grouping and Aggregation

**Scenario:** Analyze sales by city.

**Task:**
1. Use the cleaned `sales_clean.csv` from Exercise 2
2. Group by city and calculate:
   - Total sales per city
   - Average sales per city
   - Number of transactions per city
3. Sort by total sales (descending)
4. Print formatted results

**Expected Output:**
```
City      Total Sales  Avg Sales  Transactions
Amman         10000     5000.00       2
Aqaba          2000     2000.00       1
Irbid          3000     3000.00       1
```

---

## Exercise 4: Simple Line Plot

**Scenario:** Visualize monthly revenue.

**Task:**
1. Create sample data:
   ```
   Month: Jan, Feb, Mar, Apr, May, Jun
   Revenue: 12000, 15000, 18000, 16000, 22000, 25000
   ```

2. Create a line plot with:
   - X-axis: Month
   - Y-axis: Revenue ($)
   - Title: "Monthly Revenue"
   - Grid enabled
   - Markers on data points
   - Legend if plotting multiple series

3. Save as `revenue_chart.png`
4. Print: "Chart saved successfully"

---

## Exercise 5: Bar Chart Comparison

**Scenario:** Compare sales across cities.

**Task:**
1. Create a dictionary with city sales:
   ```
   Amman: 45000
   Zarqa: 32000
   Irbid: 28000
   Aqaba: 18000
   ```

2. Create a bar chart:
   - Use different colors for each bar
   - Add value labels on top of bars
   - Title: "Sales by City"
   - Proper axis labels

3. Save as `sales_by_city.png`

**Hint:** Use `plt.text()` to add value labels above bars.

---

## Exercise 6: Multiple Subplots

**Scenario:** Create a dashboard with multiple charts.

**Task:**
1. Use the revenue and city sales data from exercises 4 and 5
2. Create a 2x2 subplot grid:
   - Top-left: Line chart of monthly revenue
   - Top-right: Bar chart of city sales
   - Bottom-left: Pie chart of city sales distribution
   - Bottom-right: Histogram of simulated daily sales (20 random values 15000-30000)

3. Customize each subplot with appropriate titles and labels
4. Save as `dashboard.png`

---

## Exercise 7: Real Data Analysis

**Scenario:** Complete data pipeline (cleanup → analysis → visualization).

**Task:**
1. Create `orders.csv`:
   ```
   order_id,date,customer,amount,category
   1,2024-01-15,Ali,1500,Electronics
   2,2024-01-16,Hana,,Electronics
   3,2024-01-17,Omar,2500,Clothing
   4,2024-01-17,Omar,2500,Clothing
   5,2024-01-18,Fatima,1200,Books
   6,2024-01-19,Ahmed,3000,Electronics
   7,2024-01-20,Ali,800,Books
   ```

2. Load and clean:
   - Remove duplicates
   - Handle missing amounts (use mean of column)
   - Convert amount to numeric

3. Analyze:
   - Total sales by category
   - Number of orders per customer

4. Visualize:
   - Create a bar chart for sales by category
   - Create a pie chart for sales distribution

5. Save cleaned data as `orders_clean.csv`

**Expected Result:**
- Clean CSV file with 6 rows
- 2 visualization PNG files
- Summary statistics printed

---

## Exercise 8: Challenge - Data Exploration Notebook

**Scenario:** Given a dataset, perform complete exploratory data analysis.

**Task:**
1. Create `products.csv` with:
   ```
   product_id,name,price,stock,category
   1,Laptop,999,15,Electronics
   2,Mouse,25,100,Electronics
   3,Keyboard,75,50,Electronics
   4,T-Shirt,20,200,Clothing
   5,Jeans,60,80,Clothing
   6,Novel,15,45,Books
   ```

2. Perform EDA:
   - Load and display basic info
   - Check for missing values
   - Calculate summary statistics
   - Group by category and sum/count

3. Create visualizations:
   - Scatter: Price vs Stock
   - Bar: Count of products per category
   - Histogram: Price distribution

4. Answer these questions:
   - Which category has the most products?
   - What is the average price by category?
   - Which product has the highest stock level?

---

## Submission Checklist

✅ All CSV files created correctly  
✅ Data loaded successfully with pandas  
✅ Cleaning applied (dropna, duplicates, type conversion)  
✅ Grouping and aggregation working  
✅ All visualizations created and saved as PNG  
✅ Titles, labels, and legends present on charts  
✅ Clean data saved to new CSV files  
✅ Code runs without errors  

---

## Tips

- Use `pd.read_csv()` to load CSV files
- Use `.dropna()` to remove missing values
- Use `.drop_duplicates()` to remove duplicates
- Use `df.groupby('column').agg({'col2': 'sum'})` for aggregation
- Use `plt.savefig('name.png')` before `plt.show()`
- Always check data types with `.dtypes`
- Use `.describe()` for quick statistics
