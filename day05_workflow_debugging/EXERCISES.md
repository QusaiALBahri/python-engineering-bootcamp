# Day 5 Exercises: Debugging, Testing & Professional Practices

## Exercise 1: PEP 8 Code Formatting
Rewrite the following code to follow PEP 8:

```python
def calc(x,y,z):return (x+y)*z if x>0 and y>0 else 0
class user:
    def __init__(self,nm,ag):
        self.nm=nm
        self.ag=ag
API_KEY="secret123"
myList = [1,2,3,4,5]
```

**Requirements:**
- Fix naming (functions, classes, constants)
- Add proper spacing
- Add docstrings
- Improve readability

---

## Exercise 2: Add Type Hints
Add type hints to these functions:

```python
def get_average(numbers):
    return sum(numbers) / len(numbers)

def process_user(name, age):
    return {"name": name, "age": age}

def find_item(items, target):
    for item in items:
        if item == target:
            return item
    return None
```

---

## Exercise 3: Write Unit Tests
Write unit tests for this Calculator class:

```python
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
```

Test cases needed:
- Basic operations (add, subtract, multiply, divide)
- Edge cases (zero, negative numbers)
- Error handling (division by zero)

---

## Exercise 4: Debug the Code
Find and fix bugs in this function:

```python
def find_duplicates(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] = numbers[j]:  # BUG 1: = instead of ==
                duplicates.append(numbers[i])
    return duplicates

result = find_duplicates([1, 2, 2, 3, 3, 3, 4])
print(result)  # Expected: [2, 3, 3]
```

**Bugs to find:**
- Syntax errors
- Logic errors
- Efficiency issues

---

## Exercise 5: Add Logging
Add logging to this program instead of print():

```python
def authenticate(username, password):
    if username == "admin" and password == "pass123":
        return True
    return False

def login_user(attempts_max=3):
    for attempt in range(1, attempts_max + 1):
        username = input("Username: ")
        password = input("Password: ")
        if authenticate(username, password):
            print("Login successful")
            return True
        else:
            print(f"Login failed. {attempts_max - attempt} attempts remaining")
    
    print("Login failed - too many attempts")
    return False
```

---

## Challenge 1: Complete Test Suite
Write comprehensive tests for a `BankAccount` class:

```python
class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
    
    def get_balance(self):
        return self.balance
```

Test all:
- Deposits
- Withdrawals
- Invalid withdrawals
- Edge cases (zero, negative)

---

## Challenge 2: Code Quality Report
Write a quality checking script that:
- Checks function length (< 50 lines)
- Checks variable names (snake_case)
- Checks for docstrings
- Counts lines of code
- Reports code metrics

---

## Challenge 3: Refactoring Exercise
Refactor this code to be more professional:

```python
def p(x):
    return x*0.1

def c(x,d):
    x2=x*(1-d)
    return x2

def r(lst):
    s=0
    for i in lst:
        s+=i
    return s/len(lst)

def v(e):
    return "@" in e and "." in e
```

Requirements:
- Use descriptive names
- Add docstrings
- Add type hints
- Improve clarity
- Add error handling

---

## Solutions Checklist
- [ ] PEP 8 code passes style check
- [ ] All functions have type hints
- [ ] Test suite has 100% pass rate
- [ ] All bugs found and fixed
- [ ] Logging replaces print statements
- [ ] Code is professional and maintainable
- [ ] Tests cover edge cases
- [ ] Documentation is clear
