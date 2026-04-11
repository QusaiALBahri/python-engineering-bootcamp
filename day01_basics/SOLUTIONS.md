# Day 1 Solutions: Basics

## Exercise 1: Age Calculator

**Basic Solution:**
```python
name = input("What is your name? ")
birth_year = int(input("What year were you born? "))
age = 2024 - birth_year
print(f"Hello {name}! You are {age} years old.")
```

**Challenge Solution (asks for current year):**
```python
name = input("What is your name? ")
birth_year = int(input("What year were you born? "))
current_year = int(input("What is the current year? "))
age = current_year - birth_year
print(f"Hello {name}! You are {age} years old.")
```

---

## Exercise 2: Rectangle Area

**Basic Solution:**
```python
length = int(input("Length: "))
width = int(input("Width: "))
area = length * width
print(f"Area: {area} square units")
```

**Challenge Solution (with perimeter):**
```python
length = int(input("Length: "))
width = int(input("Width: "))
area = length * width
perimeter = 2 * length + 2 * width
print(f"Area: {area} square units")
print(f"Perimeter: {perimeter} units")
```

---

## Exercise 3: Temperature Converter

**Basic Solution:**
```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")
```

**Challenge Solution (bidirectional):**
```python
print("Temperature Converter")
celsius = float(input("Enter Celsius (or 0 to skip): "))
if celsius != 0:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is {fahrenheit}°F")

fahrenheit = float(input("Enter Fahrenheit (or 0 to skip): "))
if fahrenheit != 0:
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is {celsius}°C")
```

---

## Exercise 4: String Manipulation

**Solution:**
```python
name = input("Your name: ")
print(f"UPPERCASE: {name.upper()}")
print(f"lowercase: {name.lower()}")
print(f"Length: {len(name)}")
print(f"First 3 letters: {name[:3]}")
print(f"Last 3 letters: {name[-3:]}")
```

---

## Exercise 5: Simple Banking

**Basic Solution:**
```python
name = input("Customer name: ")
balance = float(input("Starting balance: $"))
deposit = float(input("Deposit amount: $"))
new_balance = balance + deposit

print("=== Bank Receipt ===")
print(f"Customer: {name}")
print(f"Starting Balance: ${balance:.2f}")
print(f"Deposit: ${deposit:.2f}")
print(f"New Balance: ${new_balance:.2f}")
```

---

## Answers to Tricky Questions

1. **`"25"` is text (string), `25` is a number (integer)**
   - "25" is just characters that look like a number
   - 25 is an actual number you can do math with

2. **`input()` always returns a STRING**
   - Even if user types 25, it comes back as "25"
   - You must convert with int() or float() to do math

3. **Use `float("3.14")`**
   - `float(string)` converts text to decimal number

4. **`text[0:-1]` gets everything EXCEPT the last character**
   - [0:-1] means "from first (0) to second-to-last (-1)"

5. **F-strings are cleaner and easier to read**
   - `f"Total: {price * 3}"` is better than `"Total: " + str(price * 3)`
   - F-strings handle type conversion automatically

---

## Key Takeaways

✅ Always convert `input()` results with `int()` or `float()` before math  
✅ Use f-strings for readable output with variables  
✅ Remember: ".upper()" & ".lower()" return NEW strings  
✅ Index with [n] to get specific characters  
✅ Negative indexing counts from the end: [-1] is last  
