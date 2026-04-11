"""
Day 1 - Session 2: Variables & Data Types
============================================

LEARNING OBJECTIVES:
- Understand variables (containers for values)
- Learn Python data types: int, float, str, bool
- Practice type conversion
- Use type() to check data types

VOCABULARY:
- Variable: A named container that stores a value
- Data Type: The kind of data (int=whole number, float=decimal, str=text, bool=true/false)
- Assignment: Using = to put value into variable
"""

# ============================================================================
# EXAMPLE 1: Creating variables
# ============================================================================
name = "Alice"          # str (string/text)
age = 25                # int (integer/whole number)
height = 5.6            # float (decimal number)
is_student = True       # bool (true or false)

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student?", is_student)

# ============================================================================
# EXAMPLE 2: Using type() to check data type
# ============================================================================
print("\n--- Type Checking ---")
print(type(name))           # <class 'str'>
print(type(age))            # <class 'int'>
print(type(height))         # <class 'float'>
print(type(is_student))     # <class 'bool'>

# ============================================================================
# EXAMPLE 3: Type conversion (changing types)
# ============================================================================
age_str = "30"          # This is text that LOOKS like a number
age_int = int(age_str)  # Convert text to actual number
print(f"String age: {age_str} (type: {type(age_str).__name__})")
print(f"Integer age: {age_int} (type: {type(age_int).__name__})")

# ============================================================================
# EXAMPLE 4: Math with converted types
# ============================================================================
number_str = "10"
result = int(number_str) + 5  # Convert to int, then add
print(f"10 + 5 = {result}")

# ============================================================================
# EXAMPLE 5: String to float
# ============================================================================
price_str = "19.99"
price_float = float(price_str)
print(f"Price as text: {price_str}")
print(f"Price as number: {price_float}")
print(f"Total for 3 items: {price_float * 3}")

# ============================================================================
# KEY TAKEAWAYS:
# ============================================================================
# 1. Create variables with: name = value
# 2. Every value has a type (str, int, float, bool)
# 3. type() shows what type something is
# 4. int() converts to whole number
# 5. float() converts to decimal number
# 6. str() converts anything to text
