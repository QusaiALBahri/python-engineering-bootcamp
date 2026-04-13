# ✅ Day 12: Advanced Libraries - SOLUTIONS

## Solution 1: NumPy Matrix Operations

```python
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Matrix multiplication
result = A @ B
print("A @ B:", result)

# Eigenvalues
eigenvalues = np.linalg.eigvals(A)
print("Eigenvalues:", eigenvalues)

# Inverse (if non-singular)
inverse = np.linalg.inv(np.array([[1, 2], [3, 4]], dtype=float))
print("Inverse:", inverse)

# Determinant
det = np.linalg.det(A)
print("Determinant:", det)
```

## Solution 2: Regular Expression

```python
import re

text = "Contact us at admin@example.com or john@test.org. Call 555-1234 or visit https://example.com"

# Extract emails
emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
print("Emails:", emails)

# Extract phone
phones = re.findall(r'\d{3}-\d{4}', text)
print("Phones:", phones)

# Extract URLs
urls = re.findall(r'https?://[\w/-]+', text)
print("URLs:", urls)
```

## Solution 3: DuckDB

```python
import duckdb

# Create database and table
conn = duckdb.connect('students.db')

students = [
    (1, 'Ali', 95),
    (2, 'Hana', 87),
    (3, 'Omar', 92),
    (4, 'Fatima', 88)
]

conn.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name VARCHAR, score INTEGER)")
conn.execute("INSERT INTO students VALUES (?, ?, ?)", students)

# Queries
result = conn.execute("SELECT * FROM students WHERE score > 90").fetchall()
print(result)

avg = conn.execute("SELECT AVG(score) as avg FROM students").fetchone()
print(f"Average: {avg[0]}")

conn.close()
```
