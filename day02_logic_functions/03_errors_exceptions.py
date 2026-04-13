"""
Day 2, Lesson 3: Error Handling & Exception Management
Covers:
  - Try/except/finally blocks
  - Different exception types
  - Raising exceptions
  - Custom error messages
"""

# ============================================
# 1. Basic Try/Except
# ============================================

print("=" * 50)
print("Basic Error Handling")
print("=" * 50)

# Without error handling - crashes!
# number = int(input("Enter a number: "))

# With error handling - graceful!
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("⚠️ That's not a valid number!")

# ============================================
# 2. Multiple Exception Types
# ============================================

print("\n" + "=" * 50)
print("Handling Different Error Types")
print("=" * 50)

def divide_numbers(a, b):
    """Divide two numbers with error handling"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("❌ Error: Both inputs must be numbers!")
        return None

print(divide_numbers(10, 2))   # Works: 5.0
print(divide_numbers(10, 0))   # Handles ZeroDivisionError
print(divide_numbers("10", 2)) # Handles TypeError

# ============================================
# 3. Try/Except/Finally
# ============================================

print("\n" + "=" * 50)
print("Try/Except/Finally")
print("=" * 50)

try:
    file = open("nonexistent.txt", "r")  # Will fail
    data = file.read()
except FileNotFoundError:
    print("⚠️ File not found!")
finally:
    print("✓ Cleanup code runs regardless of error")
    # In real code, would close file here

# ============================================
# 4. Catching Generic Exceptions
# ============================================

print("\n" + "=" * 50)
print("Generic Exception Handling")
print("=" * 50)

try:
    list_data = [1, 2, 3]
    print(list_data[5])  # Index out of range
except IndexError as e:
    print(f"⚠️ Index Error: {e}")
except Exception as e:  # Catch any exception
    print(f"⚠️ Unexpected error: {e}")

# ============================================
# 5. Raising Exceptions
# ============================================

print("\n" + "=" * 50)
print("Raising Custom Exceptions")
print("=" * 50)

def validate_age(age):
    """Validate that age is reasonable"""
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative!")
        if age > 150:
            raise ValueError("Age seems unrealistic!")
        return age
    except ValueError as e:
        print(f"❌ Invalid age: {e}")
        return None

validate_age(-5)    # Raises custom error
validate_age("abc") # Raises ValueError from int()
validate_age(25)    # Works!

# ============================================
# 6. Else Clause (runs if no error)
# ============================================

print("\n" + "=" * 50)
print("Try/Except/Else")
print("=" * 50)

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
else:
    print(f"✓ Successfully converted to: {number}")

# ============================================
# 7. Nested Try/Except
# ============================================

print("\n" + "=" * 50)
print("Nested Error Handling")
print("=" * 50)

def safe_calculation(values):
    """Calculate with nested error handling"""
    try:
        # Outer try
        numbers = []
        for val in values:
            try:
                # Inner try
                num = float(val)
                numbers.append(num)
            except ValueError:
                print(f"  ⚠️ Skipping invalid value: {val}")
        
        if numbers:
            average = sum(numbers) / len(numbers)
            print(f"✓ Average: {average:.2f}")
        else:
            print("No valid numbers provided")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

safe_calculation([1, 2, "three", 4, "five"])

# ============================================
# 8. Common Exception Types
# ============================================

print("\n" + "=" * 50)
print("Common Exception Types")
print("=" * 50)

print("""
Common Exceptions:
  - ValueError: Wrong type/value
  - TypeError: Wrong data type
  - IndexError: List index out of range
  - KeyError: Dictionary key not found
  - FileNotFoundError: File doesn't exist
  - ZeroDivisionError: Division by zero
  - NameError: Variable not defined
  - AttributeError: Object has no attribute
  - ImportError: Cannot import module
  - RuntimeError: General execution error
""")

# ============================================
# 9. Practical Example: Safe Input
# ============================================

print("\n" + "=" * 50)
print("Practical: Safe User Input")
print("=" * 50)

def get_valid_number(prompt, min_val=None, max_val=None):
    """Get a valid number from user with validation"""
    while True:
        try:
            value = float(input(prompt))
            
            if min_val is not None and value < min_val:
                print(f"⚠️ Number must be >= {min_val}")
                continue
            
            if max_val is not None and value > max_val:
                print(f"⚠️ Number must be <= {max_val}")
                continue
            
            return value
        except ValueError:
            print("⚠️ Please enter a valid number!")

# Example (commented out so script doesn't hang)
# age = get_valid_number("Enter your age (0-150): ", 0, 150)
# print(f"Your age: {age}")

# ============================================
# 10. Best Practices
# ============================================

print("\n" + "=" * 50)
print("Error Handling Best Practices")
print("=" * 50)

print("""
✓ DO:
  - Catch specific exceptions first
  - Provide informative error messages
  - Clean up resources in finally
  - Log errors for debugging
  - Validate input early

✗ DON'T:
  - Catch generic Exception except when needed
  - Hide errors silently
  - Leave try blocks with too much code
  - Ignore exceptions
  - Use exceptions for normal control flow
""")

print("\n✅ Lesson 3 Complete!")
