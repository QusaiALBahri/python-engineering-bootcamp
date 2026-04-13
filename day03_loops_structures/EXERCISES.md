# Day 3 Exercises: Loops, Data Structures & OOP

## Exercise 1: List Operations & Iteration
Write a program that:
- Creates a list of 5 integers: [10, 25, 15, 30, 20]
- Finds and prints the maximum and minimum values
- Calculates the sum and average
- Prints each element with its index

**Example Output:**
```
List: [10, 25, 15, 30, 20]
Max: 30, Min: 10
Sum: 100, Average: 20
Index 0: 10
Index 1: 25
...
```

---

## Exercise 2: Dictionary Operations
Create a dictionary of 5 people with their ages:
- Print all names and ages
- Add a new person
- Find and print the oldest person
- Increase everyone's age by 1
- Check if a specific name exists

**Example:**
```
Original: {"Ali": 25, "Sara": 22, ...}
Added: {"Ali": 25, "Sara": 22, ..., "Zain": 28}
Oldest: Sara (23)
After birthday: {"Ali": 26, "Sara": 23, ...}
```

---

## Exercise 3: List Comprehension
Use list comprehension to:
- Create a list of squares: [1, 4, 9, 16, ..., 100]
- Create a list of even numbers from 1-20
- Create a list of numbers divisible by 3 from 1-30
- Convert a list of numbers to strings

---

## Exercise 4: Simple Class - Student
Create a `Student` class with:
- Attributes: name, age, student_id, grades (list)
- Method `add_grade(grade)`: Add a grade to the list
- Method `calculate_average()`: Return average of grades
- Method `__str__()`: Return readable format

Test with 2 students and add some grades.

**Example:**
```
Student: Ali (ID: 101)
Age: 20
Grades: [85, 90, 88]
Average: 87.67
```

---

## Exercise 5: Set Operations
- Create a set of first 10 even numbers: {2, 4, 6, ...}
- Create a set of first 10 odd numbers: {1, 3, 5, ...}
- Find union (combine both)
- Find intersection (common elements)
- Find difference (even - odd)

**Example:**
```
Even: {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Odd: {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
Union: 20 elements
Intersection: 0 elements
Difference: {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
```

---

## Challenge 1: Bank Account Class
Create a `BankAccount` class:
- Attributes: account_holder, balance, transaction_history (list)
- Method `__init__`: Initialize account
- Method `deposit(amount)`: Add money and record transaction
- Method `withdraw(amount)`: Remove money if available
- Method `get_statement()`: Show all transactions and balance
- Method `__str__()`: Return account info

Test with various transactions.

---

## Challenge 2: Tuple Unpacking Game
Write a program that:
- Creates a list of tuples: [(name, age, city), ...]
- Unpacks each tuple
- Displays them in a formatted way
- Finds all people from a specific city
- Counts people in each city

**Example:**
```
People:
  Ali, 25, Baghdad
  Sara, 22, Baghdad
  Mona, 28, Basra
From Baghdad: 2 people
```

---

## Challenge 3: Nested Data Structures
Work with nested lists/dicts:
```python
students = {
    "Ali": [85, 90, 88],
    "Sara": [92, 88, 95],
    "Mona": [78, 82, 80]
}
```

Tasks:
- Calculate each student's average
- Find the top student
- Add a new student with grades
- Print a report with rankings

---

## Solutions Checklist
- [ ] All exercises use correct data structures
- [ ] Code runs without errors
- [ ] Used for/while loops appropriately
- [ ] Created at least 1 custom class
- [ ] Used __str__ method
- [ ] Used list/dict/set operations
- [ ] Proper error handling for invalid inputs
