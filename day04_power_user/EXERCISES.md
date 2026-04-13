# Day 4 Exercises: Advanced Patterns & File I/O

## Exercise 1: List Comprehensions
Use list comprehensions to:
- Create a list of squares from 1-20
- Create a list of even numbers
- Create a list of tuples: [(1, 1), (2, 4), (3, 9), ...]
- Filter a list to only numbers > 10
- Create nested list: [[1,2,3], [4,5,6], ...]

---

## Exercise 2: Lambda & Map/Filter
- Use `map()` with lambda to convert strings to integers
- Use `filter()` with lambda to find numbers divisible by 3
- Sort a list of dictionaries by a value using lambda
- Find minimum/maximum using lambda key

**Example:**
```python
words = ["123", "456", "789"]
numbers = list(map(lambda x: int(x), words))  # [123, 456, 789]
```

---

## Exercise 3: Simple Decorator
Create a decorator that:
- Prints "Function is starting" before function call
- Prints "Function finished" after function call
- Must work with functions of any number of arguments

**Example:**
```python
@my_decorator
def greet(name):
    print(f"Hello {name}")

greet("Ali")
# Output:
# Function is starting
# Hello Ali
# Function finished
```

---

## Exercise 4: Generator Function
Create a generator that:
- Yields numbers from 1 to n
- Yields squares of numbers from 1 to n  
- Yields even numbers from a list
- Yields lines from a file one at a time

Test that it's memory efficient compared to lists.

---

## Exercise 5: File Operations
Write a program that:
- Creates a text file with 5 lines
- Reads the file line by line
- Appends 3 new lines
- Counts total lines
- Saves line count to a new file

**Example:**
```
Original file:
  Line 1
  Line 2
  Line 3
  Line 4
  Line 5

After append:
  8 total lines

stats.txt contains: "8 lines"
```

---

## Challenge 1: JSON Data Manager
Create a class to manage a JSON file:
- `load()`: Load data from JSON file
- `save()`: Save data to JSON file
- `add(key, value)`: Add a new entry
- `get(key)`: Retrieve an entry
- `delete(key)`: Remove an entry
- `list_all()`: Show all entries

Test with student data.

---

## Challenge 2: CSV Report Generator
Write a program that:
- Reads data from a CSV file
- Processes the data (filtering/sorting)
- Generates a report with statistics
- Saves report to a new CSV file

**Example:**
```
Input: sales.csv (product, price, quantity)
Output: report.csv (product, total_revenue, status)
```

---

## Challenge 3: Logging Decorator
Create a decorator that:
- Logs function name and arguments
- Logs return value
- Logs execution time
- Logs any exceptions

**Example:**
```python
@logger
def calculate(a, b):
    return a + b

calculate(5, 3)
# [2024-01-15 10:30:45] calculate called with (5, 3)
# [2024-01-15 10:30:45] Returned: 8
# [2024-01-15 10:30:45] Execution time: 0.002ms
```

---

## Solutions Checklist
- [ ] All list comprehensions work correctly
- [ ] Map/filter operations return expected results
- [ ] Decorator preserves original function behavior
- [ ] Generator is memory efficient
- [ ] File operations handle errors gracefully
- [ ] JSON manager works with nested data
- [ ] CSV processing handles headers correctly
