# 🎯 Day 2: Logic, Functions & Error Handling (3 hours)

## 📚 Topics Covered

| Topic | File | Duration | What You'll Learn |
|-------|------|----------|-------------------|
| **Conditionals & Operators** | `01_conditionals.py` | 45min | if/elif/else, comparison operators, logic |
| **Functions Basics** | `02_functions.py` | 45min | Function definition, parameters, return values |
| **Error Handling** | `03_errors_exceptions.py` | 45min | Try/except, raising errors, debugging |
| **Exercises & Solutions** | `EXERCISES.md`, `SOLUTIONS.md` | 60min | Hands-on practice |

---

## 🎓 Learning Outcomes

By the end of Day 2, you should understand:

✅ How to use **if/elif/else** for decision-making  
✅ Logical operators: **and**, **or**, **not**  
✅ How to **define and call functions**  
✅ Function **parameters and return values**  
✅ How to **handle errors** gracefully  
✅ When to **raise exceptions**  
✅ Basic **troubleshooting** techniques  

---

## 🚀 Quick Start

### Run the examples:
```bash
python 01_conditionals.py
python 02_functions.py
python 03_errors_exceptions.py
```

### Try the exercises:
```bash
# Read EXERCISES.md and solve them
# Check your solutions against SOLUTIONS.md
```

---

## 🧠 Key Concepts at a Glance

### **Conditional Statements**
```python
age = 20
if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")
```

### **Logical Operators**
```python
age = 25
has_license = True
if age >= 18 and has_license:  # Both must be True
    print("Can drive")

if age < 13 or age > 65:  # At least one must be True
    print("Special age group")

if not has_license:  # Reverses the condition
    print("Cannot drive")
```

### **Functions**
```python
def greet(name, greeting="Hello"):
    """A simple greeting function"""
    return f"{greeting}, {name}!"

message = greet("Ali")
print(message)  # Hello, Ali!
```

### **Error Handling**
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")
```

---

## 📊 Mini Project: Login System

**Scenario:** Create a login system that validates user input.

**Features:**
1. Ask for username and password
2. Validate inputs (not empty, correct credentials)
3. Check password strength
4. Handle wrong attempts gracefully
5. Show success/error messages

---

## 🎯 Focus Areas

- **Decision Logic:** Use conditionals to make programs intelligent
- **Function Design:** Write reusable code blocks
- **Error Prevention:** Anticipate user mistakes
- **Error Recovery:** Handle errors gracefully
