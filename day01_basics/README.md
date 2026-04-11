# 🎯 Day 1: Python Basics (3 hours)

## 📚 Topics Covered

| Topic | File | Duration | What You'll Learn |
|-------|------|----------|-------------------|
| **Hello World & Input/Output** | `01_hello.py` | 30min | `print()`, `input()`, basic I/O |
| **Variables & Data Types** | `02_variables.py` | 45min | Variable assignment, int/float/str/bool, `type()` |
| **Strings & F-Strings** | `03_strings_fstrings.py` | 45min | String manipulation, methods, f-strings |
| **Exercises & Solutions** | `EXERCISES.md`, `SOLUTIONS.md` | 60min | Hands-on practice |

---

## 🎓 Learning Outcomes

By the end of Day 1, you should understand:

✅ How `print()` outputs information to the console  
✅ How `input()` captures user responses   
✅ The 4 main data types: **str, int, float, bool**  
✅ How to convert between types (int(), float(), str())  
✅ How to use f-strings to create readable output  
✅ Basic string operations (.upper(), .lower(), .strip(), indexing)  

---

## 🚀 Quick Start

### Run the examples:
```bash
python 01_hello.py
python 02_variables.py
python 03_strings_fstrings.py
```

### Try the exercises:
```bash
# Read EXERCISES.md and solve them
# Check your solutions against SOLUTIONS.md
```

---

## 🧠 Key Concepts at a Glance

### **print() vs input()**
```python
print("Output text")           # You → Output
name = input("Your name: ")    # Input ← User
```

### **Data Types**
```python
text = "Hello"           # str (string - text)
count = 42              # int (integer - whole number)
price = 19.99          # float (float - decimal)
active = True          # bool (boolean - true/false)
```

### **Type Conversion**
```python
age_str = "25"
age_int = int(age_str)      # Convert string to number
price_float = float("9.99")  # Convert to decimal
text = str(123)             # Convert to text
```

### **F-Strings (Modern Python)**
```python
name = "Alice"
age = 25
print(f"{name} is {age} years old")  # Alice is 25 years old
print(f"Next year: {age + 1}")        # Next year: 26
```

### **String Methods**
```python
text = "  Hello World  "
text.upper()    # "  HELLO WORLD  "
text.lower()    # "  hello world  "
text.strip()    # "Hello World" (removes spaces)
text[0]         # "H" (first character)
text[-1]        # "d" (last character)
len(text)       # 15 (total characters)
```

---

## 💡 Common Mistakes to Avoid

❌ **Don't do this:**
```python
age = input("Age: ")           # age is a STRING "25"
print(age + 5)                 # ERROR! Can't add string + number
```

✅ **Do this instead:**
```python
age = int(input("Age: "))      # Convert to int first
print(age + 5)                 # Works! 25 + 5 = 30
```

---

❌ **Don't do this:**
```python
name = "John"
print("Hello " + name + "!")   # Works but is hard to read
```

✅ **Do this instead:**
```python
name = "John"
print(f"Hello {name}!")        # Cleaner and easier
```

---

## 🎯 Practice Flow

1. **Read** each lesson file (01_hello.py, 02_variables.py, 03_strings_fstrings.py)
2. **Run** the examples to see them in action
3. **Modify** the code: change variables, add prints, experiment
4. **Solve** the 5 exercises in EXERCISES.md
5. **Check** your answers against SOLUTIONS.md
6. **Understand** why the solutions work

---

## 📝 Self-Assessment

Can you answer these without looking at code?

- [ ] What's the difference between `"42"` and `42`?
- [ ] Why do we need `int(input())`?
- [ ] How do f-strings know what variables to use?
- [ ] What does `"hello"[0]` return?
- [ ] When would you use `.strip()`?

---

## 🔗 Next Steps

**Ready for Day 2?** You'll learn:
- **Conditional logic** (if/else)
- **Comparison operators** (==, !=, <, >)
- **Boolean logic** (and, or, not)
- **Functions** for reusable code

---

## 📚 Resources

- **Python Docs:** https://docs.python.org/3/
- **W3Schools:** https://www.w3schools.com/python/
- **Type Conversions:** https://docs.python.org/3/library/stdtypes.html

---

**⏱️ Time Estimate: 3 hours**  
**💪 Difficulty: Beginner-friendly**  
**✅ Status: Ready to teach**
