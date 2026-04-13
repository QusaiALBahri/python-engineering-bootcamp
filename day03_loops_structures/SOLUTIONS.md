# Day 3 Solutions: Loops, Data Structures & OOP

## Exercise 1: List Operations & Iteration

**Problem:** Perform various operations on a list of integers.

**Solution:**

```python
# Create list
numbers = [10, 25, 15, 30, 20]

# Find max and min
max_num = max(numbers)
min_num = min(numbers)

# Calculate sum and average
total = sum(numbers)
average = total / len(numbers)

# Print results
print(f"List: {numbers}")
print(f"Max: {max_num}, Min: {min_num}")
print(f"Sum: {total}, Average: {average:.1f}")

# Print with indices
for index, value in enumerate(numbers):
    print(f"Index {index}: {value}")
```

**Output:**
```
List: [10, 25, 15, 30, 20]
Max: 30, Min: 10
Sum: 100, Average: 20.0
Index 0: 10
Index 1: 25
Index 2: 15
Index 3: 30
Index 4: 20
```

---

## Exercise 2: Dictionary Operations

**Problem:** Manage a dictionary of people and their ages.

**Solution:**

```python
# Create dictionary
people = {
    "Ali": 25,
    "Sara": 22,
    "Mona": 28,
    "Hassan": 24,
    "Layla": 26
}

# Print all
print("Original:")
for name, age in people.items():
    print(f"  {name}: {age}")

# Add new person
people["Zain"] = 27
print("\nAfter adding Zain:")
print(f"  {people}")

# Find oldest
oldest_name = max(people, key=people.get)
oldest_age = people[oldest_name]
print(f"\nOldest: {oldest_name} ({oldest_age})")

# Increase all ages by 1
for name in people:
    people[name] += 1

print("\nAfter birthday:")
for name, age in people.items():
    print(f"  {name}: {age}")

# Check if name exists
search_name = "Ali"
if search_name in people:
    print(f"\n✓ {search_name} exists (age: {people[search_name]})")
else:
    print(f"\n✗ {search_name} not found")
```

**Output:**
```
Original:
  Ali: 25
  Sara: 22
  Mona: 28
  Hassan: 24
  Layla: 26

After adding Zain:
  {'Ali': 25, 'Sara': 22, 'Mona': 28, 'Hassan': 24, 'Layla': 26, 'Zain': 27}

Oldest: Mona (28)

After birthday:
  Ali: 26
  Sara: 23
  Mona: 29
  Hassan: 25
  Layla: 27
  Zain: 28

✓ Ali exists (age: 26)
```

---

## Exercise 3: List Comprehension

**Problem:** Use list comprehension for various list operations.

**Solution:**

```python
# List of squares from 1-10
squares = [x**2 for x in range(1, 11)]
print(f"Squares: {squares}")

# List of even numbers 1-20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers (1-20): {evens}")

# Numbers divisible by 3 (1-30)
div_by_3 = [x for x in range(1, 31) if x % 3 == 0]
print(f"Divisible by 3 (1-30): {div_by_3}")

# Convert numbers to strings
numbers = [1, 2, 3, 4, 5]
str_numbers = [str(x) for x in numbers]
print(f"As strings: {str_numbers}")
```

**Output:**
```
Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Even numbers (1-20): [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Divisible by 3 (1-30): [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
As strings: ['1', '2', '3', '4', '5']
```

---

## Exercise 4: Simple Class - Student

**Problem:** Create a Student class with grade management.

**Solution:**

```python
class Student:
    """Student class with grade tracking"""
    
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        """Add a grade"""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return f"✓ Added grade: {grade}"
        return "Invalid grade (0-100)"
    
    def calculate_average(self):
        """Return average grade"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def __str__(self):
        """String representation"""
        avg = self.calculate_average()
        return (f"Student: {self.name} (ID: {self.student_id})\n"
                f"Age: {self.age}\n"
                f"Grades: {self.grades}\n"
                f"Average: {avg:.2f}")

# Test with students
student1 = Student("Ali", 20, 101)
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(88)

student2 = Student("Sara", 21, 102)
student2.add_grade(92)
student2.add_grade(95)
student2.add_grade(89)

print(student1)
print("\n" + "="*40 + "\n")
print(student2)
```

**Output:**
```
Student: Ali (ID: 101)
Age: 20
Grades: [85, 90, 88]
Average: 87.67

========================================

Student: Sara (ID: 102)
Age: 21
Grades: [92, 95, 89]
Average: 92.00
```

---

## Exercise 5: Set Operations

**Problem:** Work with sets for finding relationships between groups.

**Solution:**

```python
# First 10 even numbers
evens = set(range(2, 21, 2))  # {2, 4, 6, ..., 20}

# First 10 odd numbers
odds = set(range(1, 20, 2))   # {1, 3, 5, ..., 19}

print(f"Even numbers: {evens}")
print(f"Odd numbers: {odds}")

# Union (all unique)
union = evens | odds  # or: evens.union(odds)
print(f"\nUnion: {union}")
print(f"Union size: {len(union)}")

# Intersection (common elements)
intersection = evens & odds  # or: evens.intersection(odds)
print(f"\nIntersection: {intersection}")
print(f"Intersection size: {len(intersection)}")

# Difference (in first but not second)
difference = evens - odds  # or: evens.difference(odds)
print(f"\nDifference (even - odd): {difference}")
print(f"Difference size: {len(difference)}")

# Symmetric difference (in either but not both)
sym_diff = evens ^ odds  # or: evens.symmetric_difference(odds)
print(f"\nSymmetric difference: {sym_diff}")
```

**Output:**
```
Even numbers: {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Odd numbers: {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}

Union: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
Union size: 20

Intersection: set()
Intersection size: 0

Difference (even - odd): {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Difference size: 10

Symmetric difference: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
```

---

## Challenge 1: Bank Account Class

**Problem:** Create a full-featured BankAccount class.

**Solution:**

```python
class BankAccount:
    """Bank account with transaction history"""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        
        if initial_balance > 0:
            self.transaction_history.append(
                f"Initial deposit: ${initial_balance:.2f}"
            )
    
    def deposit(self, amount):
        """Deposit money"""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(
                f"Deposit: +${amount:.2f}"
            )
            return f"✓ Deposited ${amount:.2f}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        """Withdraw money"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(
                f"Withdrawal: -${amount:.2f}"
            )
            return f"✓ Withdrew ${amount:.2f}"
        return "Insufficient funds or invalid amount"
    
    def get_statement(self):
        """Get transaction history"""
        statement = f"\n{self.account_holder}'s Account Statement:\n"
        statement += "-" * 40 + "\n"
        for transaction in self.transaction_history:
            statement += f"  {transaction}\n"
        statement += "-" * 40 + "\n"
        statement += f"Current Balance: ${self.balance:.2f}\n"
        return statement
    
    def __str__(self):
        """String representation"""
        return (f"Account: {self.account_holder}\n"
                f"Balance: ${self.balance:.2f}")

# Test
account = BankAccount("Ali Ahmed", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.deposit(300))
print(account.get_statement())
```

**Output:**
```
✓ Deposited $500.00
✓ Withdrew $200.00
✓ Deposited $300.00

Ali Ahmed's Account Statement:
----------------------------------------
  Initial deposit: $1000.00
  Deposit: +$500.00
  Withdrawal: -$200.00
  Deposit: +$300.00
----------------------------------------
Current Balance: $1600.00
```

---

## Challenge 2: Tuple Unpacking Game

**Problem:** Work with tuples and unpacking.

**Solution:**

```python
# Create list of tuples
people = [
    ("Ali", 25, "Baghdad"),
    ("Sara", 22, "Baghdad"),
    ("Mona", 28, "Basra"),
    ("Hassan", 24, "Baghdad"),
    ("Layla", 26, "Mosul"),
]

print("People List:")
print("-" * 40)

# Unpack and display
for name, age, city in people:
    print(f"  {name:10} Age: {age:2} City: {city}")

# Count by city
cities = {}
for name, age, city in people:
    cities[city] = cities.get(city, 0) + 1

print("\nPeople by City:")
print("-" * 40)
for city, count in cities.items():
    print(f"  {city}: {count} people")

# Find all from Baghdad
baghdad_people = [name for name, age, city in people if city == "Baghdad"]
print(f"\nFrom Baghdad: {', '.join(baghdad_people)}")
```

**Output:**
```
People List:
----------------------------------------
  Ali        Age: 25 City: Baghdad
  Sara       Age: 22 City: Baghdad
  Mona       Age: 28 City: Basra
  Hassan     Age: 24 City: Baghdad
  Layla      Age: 26 City: Mosul

People by City:
----------------------------------------
  Baghdad: 3 people
  Basra: 1 people
  Mosul: 1 people

From Baghdad: Ali, Sara, Hassan
```

---

## Challenge 3: Nested Data Structures

**Problem:** Work with nested dicts and lists for complex data.

**Solution:**

```python
# Nested data
students = {
    "Ali": [85, 90, 88],
    "Sara": [92, 88, 95],
    "Mona": [78, 82, 80]
}

print("Student Report")
print("=" * 50)

# Calculate averages
averages = {}
for name, grades in students.items():
    avg = sum(grades) / len(grades)
    averages[name] = avg
    print(f"{name:10}: {grades} → Average: {avg:.2f}")

# Find top student
top_student = max(averages, key=averages.get)
print(f"\n🏆 Top Student: {top_student} ({averages[top_student]:.2f})")

# Add new student
students["Zain"] = [91, 89, 93]
averages["Zain"] = sum(students["Zain"]) / len(students["Zain"])

# Create ranking
print("\nRankings:")
print("-" * 50)
sorted_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)

for rank, (name, avg) in enumerate(sorted_students, 1):
    print(f"  {rank}. {name}: {avg:.2f}")
```

**Output:**
```
Student Report
==================================================
Ali       : [85, 90, 88] → Average: 87.67
Sara      : [92, 88, 95] → Average: 91.67
Mona      : [78, 82, 80] → Average: 80.00

🏆 Top Student: Sara (91.67)

Rankings:
--------------------------------------------------
  1. Sara: 91.67
  2. Ali: 87.67
  3. Zain: 91.00
  4. Mona: 80.00
```

---

## Summary

Key concepts demonstrated:

✓ **Data Structures:** Lists, tuples, dicts, sets and their operations  
✓ **Iteration:** For/while loops, enumerate() for indexed iteration  
✓ **List Operations:** Slicing, comprehensions, methods (append, extend)  
✓ **Dict Operations:** .items(), .get(), .keys(), .values()  
✓ **Set Operations:** Union, intersection, difference  
✓ **OOP Basics:** Classes, __init__, __str__, methods  
✓ **Unpacking:** Tuples and lists with multiple assignment  

All solutions include:
- ✅ Complete working code
- ✅ Proper data structure selection
- ✅ Meaningful variable names
- ✅ Expected output examples
- ✅ Comments where needed
