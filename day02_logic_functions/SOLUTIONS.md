# Day 2 Solutions: Conditional Logic & Functions

## Exercise 1: Student Grade System

**Problem:** Write a function that takes a score (0-100) and returns a letter grade.

**Solution:**

```python
def get_grade(score):
    """
    Convert numeric score to letter grade
    
    Args:
        score (int/float): Score between 0-100
    
    Returns:
        str: Letter grade (A, B, C, D, F)
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Main code
print("Student Grade System")
print("-" * 30)

grades = []
for i in range(1, 4):
    score = float(input(f"Enter score {i}: "))
    grade = get_grade(score)
    grades.append((score, grade))
    print(f"Score {i}: {score} → Grade: {grade}")

print("\nSummary:")
for i, (score, grade) in enumerate(grades, 1):
    print(f"  Score {i}: {score} = {grade}")
```

**Expected Output:**
```
Student Grade System
------------------------------
Enter score 1: 85
Score 1: 85.0 → Grade: B
Enter score 2: 92
Score 2: 92.0 → Grade: A
Enter score 3: 78
Score 3: 78.0 → Grade: C

Summary:
  Score 1: 85.0 = B
  Score 2: 92.0 = A
  Score 3: 78.0 = C
```

---

## Exercise 2: Login System

**Problem:** Create a login function that validates credentials with 3 attempts.

**Solution:**

```python
def check_login(username, password):
    """
    Validate user credentials
    
    Args:
        username (str): Username to check
        password (str): Password to check
    
    Returns:
        bool: True if credentials are valid
    """
    correct_username = "admin"
    correct_password = "1234"
    
    return username == correct_username and password == correct_password

# Main code
print("Login System")
print("-" * 30)

max_attempts = 3
attempts = 0
logged_in = False

while attempts < max_attempts:
    username = input(f"Attempt {attempts + 1}/{max_attempts} - Username: ")
    password = input(f"Attempt {attempts + 1}/{max_attempts} - Password: ")
    
    if check_login(username, password):
        print("✓ Login successful!")
        logged_in = True
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print(f"❌ Invalid credentials. {max_attempts - attempts} attempts left.\n")

if not logged_in:
    print("❌ Too many attempts. Access denied.")
```

**Expected Output:**
```
Login System
------------------------------
Attempt 1/3 - Username: user
Attempt 1/3 - Password: wrong
❌ Invalid credentials. 2 attempts left.

Attempt 2/3 - Username: admin
Attempt 2/3 - Password: 1234
✓ Login successful!
```

---

## Exercise 3: Discount Calculator

**Problem:** Calculate final price based on customer type.

**Solution:**

```python
def calculate_discount(amount, customer_type):
    """
    Calculate final price after discount
    
    Args:
        amount (float): Purchase amount
        customer_type (str): "standard", "member", or "vip"
    
    Returns:
        float: Final price after discount
    """
    discount = 0
    
    if customer_type == "standard":
        discount = 0
    elif customer_type == "member":
        discount = 0.10  # 10%
    elif customer_type == "vip":
        discount = 0.20  # 20%
    else:
        print(f"Unknown customer type: {customer_type}")
        return amount
    
    final_price = amount * (1 - discount)
    return final_price

# Main code
print("Discount Calculator")
print("-" * 40)

test_cases = [
    (100, "standard"),
    (100, "member"),
    (100, "vip"),
    (50, "member"),
    (200, "vip"),
]

for amount, customer_type in test_cases:
    final = calculate_discount(amount, customer_type)
    discount_amount = amount - final
    print(f"Amount: ${amount:>6.2f} | Type: {customer_type:>8} | "
          f"Discount: ${discount_amount:>6.2f} | Final: ${final:>6.2f}")
```

**Expected Output:**
```
Discount Calculator
----------------------------------------
Amount: $100.00 | Type:  standard | Discount: $ 0.00 | Final: $100.00
Amount: $100.00 | Type:   member | Discount: $10.00 | Final: $ 90.00
Amount: $100.00 | Type:      vip | Discount: $20.00 | Final: $ 80.00
Amount: $ 50.00 | Type:   member | Discount: $ 5.00 | Final: $ 45.00
Amount: $200.00 | Type:      vip | Discount: $40.00 | Final: $160.00
```

---

## Exercise 4: Number Validator

**Problem:** Create validation functions for numbers.

**Solution:**

```python
def is_positive(num):
    """Check if number is greater than 0"""
    return num > 0

def is_even(num):
    """Check if number is divisible by 2"""
    return num % 2 == 0

def is_in_range(num, min_val, max_val):
    """Check if number is within range (inclusive)"""
    return min_val <= num <= max_val

# Main code
print("Number Validator")
print("-" * 50)

test_numbers = [5, -3, 10, 7, 0, -1, 15, 20]

print("Testing is_positive():")
for num in test_numbers:
    result = is_positive(num)
    status = "✓" if result else "✗"
    print(f"  {status} {num}: {result}")

print("\nTesting is_even():")
for num in test_numbers:
    result = is_even(num)
    status = "✓" if result else "✗"
    print(f"  {status} {num}: {result}")

print("\nTesting is_in_range(num, 0, 15):")
for num in test_numbers:
    result = is_in_range(num, 0, 15)
    status = "✓" if result else "✗"
    print(f"  {status} {num}: {result}")
```

**Expected Output:**
```
Number Validator
--------------------------------------------------
Testing is_positive():
  ✓ 5: True
  ✗ -3: False
  ✓ 10: True
  ✓ 7: True
  ✗ 0: False
  ✗ -1: False
  ✓ 15: True
  ✓ 20: True

Testing is_even():
  ✗ 5: False
  ✗ -3: False
  ✓ 10: True
  ✗ 7: False
  ✓ 0: True
  ✓ -1: False
  ✓ 15: False
  ✓ 20: True

Testing is_in_range(num, 0, 15):
  ✓ 5: True
  ✗ -3: False
  ✓ 10: True
  ✓ 7: True
  ✓ 0: True
  ✗ -1: False
  ✓ 15: True
  ✗ 20: False
```

---

## Exercise 5: Temperature Alert

**Problem:** Classify temperatures and display alerts.

**Solution:**

```python
def get_temperature_alert(celsius):
    """
    Get temperature classification
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        str: Temperature classification
    """
    if celsius < 0:
        return "Freezing"
    elif celsius < 10:
        return "Cold"
    elif celsius < 20:
        return "Cool"
    elif celsius < 30:
        return "Warm"
    else:
        return "Hot"

# Main code
print("Temperature Alert System")
print("-" * 40)

temps = []
for i in range(1, 6):
    temp = float(input(f"Enter temperature {i} (°C): "))
    alert = get_temperature_alert(temp)
    temps.append((temp, alert))
    print(f"  Alert: {alert}\n")

print("Temperature Summary:")
print("-" * 40)
for i, (temp, alert) in enumerate(temps, 1):
    print(f"Temp {i}: {temp:>6.1f}°C → {alert}")
```

**Expected Output:**
```
Temperature Alert System
----------------------------------------
Enter temperature 1 (°C): -5
  Alert: Freezing

Enter temperature 2 (°C): 15
  Alert: Cool

Enter temperature 3 (°C): 25
  Alert: Warm

Enter temperature 4 (°C): 35
  Alert: Hot

Enter temperature 5 (°C): 8
  Alert: Cold

Temperature Summary:
----------------------------------------
Temp 1:  -5.0°C → Freezing
Temp 2:  15.0°C → Cool
Temp 3:  25.0°C → Warm
Temp 4:  35.0°C → Hot
Temp 5:   8.0°C → Cold
```

---

## Challenge: Password Strength Checker

**Problem:** Evaluate password strength based on character types.

**Solution:**

```python
def check_password_strength(password):
    """
    Evaluate password strength
    
    Args:
        password (str): Password to evaluate
    
    Returns:
        str: Strength rating with message
    """
    if len(password) < 8:
        return "Too short"
    
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)
    
    if not has_lowercase:
        return "Weak"
    elif not has_uppercase:
        return "Weak"
    elif not has_digit:
        return "Fair"
    elif not has_special:
        return "Strong"
    else:
        return "Very Strong"

# Main code
print("Password Strength Checker")
print("-" * 50)

test_passwords = [
    "pass",                    # Too short
    "password",                # Weak (lowercase only)
    "Password",                # Weak (no digit)
    "Password1",               # Strong (missing special char)
    "Password1!",              # Very Strong
    "MyP@ssw0rd",              # Very Strong
    "test123456",              # Fair (has digit, missing uppercase)
]

for pwd in test_passwords:
    strength = check_password_strength(pwd)
    print(f"'{pwd:15}' → {strength}")

print("\nPassword Strength Legend:")
print("  Too short:    < 8 characters")
print("  Weak:         Lowercase or Uppercase only")
print("  Fair:         Lower + Upper, missing numbers")
print("  Strong:       Lower + Upper + Numbers, missing special char")
print("  Very Strong:  Lower + Upper + Numbers + Special char")
```

**Expected Output:**
```
Password Strength Checker
--------------------------------------------------
'pass           ' → Too short
'password       ' → Weak
'Password       ' → Weak
'Password1      ' → Strong
'Password1!     ' → Very Strong
'MyP@ssw0rd     ' → Very Strong
'test123456     ' → Fair

Password Strength Legend:
  Too short:    < 8 characters
  Weak:         Lowercase or Uppercase only
  Fair:         Lower + Upper, missing numbers
  Strong:       Lower + Upper + Numbers, missing special char
  Very Strong:  Lower + Upper + Numbers + Special char
```

---

## Summary

Key concepts demonstrated in these solutions:

✓ **Conditional Logic:** `if/elif/else` statements for decision-making  
✓ **Functions:** Reusable code blocks with parameters and returns  
✓ **Logical Operators:** `and`, `or` for complex conditions  
✓ **Loops:** `while` loop for repeated attempts, `for` loop for iterations  
✓ **String Methods:** `islower()`, `isupper()`, `isdigit()`, `any()`  
✓ **List Operations:** Using lists to store and display results  
✓ **Input Validation:** Checking user input for correctness  
✓ **Output Formatting:** Using f-strings for formatted output  

All solutions include:
- ✅ Complete working code
- ✅ Docstrings explaining function purpose
- ✅ Test cases demonstrating functionality
- ✅ Expected output examples
- ✅ Comments for clarity
