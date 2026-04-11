"""
Day 2 - Session 2: Functions (Reusable Code)
==============================================

LEARNING OBJECTIVES:
- Define functions to avoid code repetition
- Understand parameters (inputs) and return values (outputs)
- Practice calling functions with different arguments
- Write clean, reusable code

KEY CONCEPTS:
- def: Define a new function
- parameters/arguments: Inputs to a function
- return: Send output back to caller
- Call: Execute the function
"""

# ============================================================================
# EXAMPLE 1: Simple function (no parameters)
# ============================================================================
def greet():
    """Says hello"""
    print("Hello, World!")

# Call the function
greet()
greet()
greet()

# ============================================================================
# EXAMPLE 2: Function with parameters
# ============================================================================
def greet_person(name):
    """Greet someone by name"""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")

# ============================================================================
# EXAMPLE 3: Function with return value
# ============================================================================
def add(a, b):
    """Add two numbers"""
    result = a + b
    return result

sum_result = add(5, 3)
print(f"5 + 3 = {sum_result}")

print(f"10 + 20 = {add(10, 20)}")

# ============================================================================
# EXAMPLE 4: Function with multiple parameters
# ============================================================================
def calculate_total(price, quantity, tax_rate=0.08):
    """Calculate total with tax"""
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

print(f"Total: ${calculate_total(50, 2):.2f}")        # Uses default 8% tax
print(f"Total: ${calculate_total(50, 2, 0.1):.2f}")   # 10% tax

# ============================================================================
# EXAMPLE 5: Function that performs validation
# ============================================================================
def is_age_valid(age):
    """Check if age is reasonable"""
    if age < 0:
        return False
    elif age > 150:
        return False
    else:
        return True

print(is_age_valid(25))      # True
print(is_age_valid(-5))      # False
print(is_age_valid(200))     # False

# ============================================================================
# EXAMPLE 6: Function with if/else logic
# ============================================================================
def get_grade(score):
    """Convert score to letter grade"""
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

print(get_grade(85))
print(get_grade(65))

# ============================================================================
# EXAMPLE 7: Function calling another function
# ============================================================================
def calculate_discount(price, customer_type):
    """Calculate discounted price"""
    if customer_type == "VIP":
        discount_rate = 0.2
    elif customer_type == "regular":
        discount_rate = 0.1
    else:
        discount_rate = 0.0
    
    discount = price * discount_rate
    final_price = price - discount
    return final_price

def display_purchase(price, customer_type):
    """Display the purchase with discount"""
    final = calculate_discount(price, customer_type)
    print(f"Original: ${price:.2f}")
    print(f"Final: ${final:.2f}")

display_purchase(100, "VIP")

# ============================================================================
# EXAMPLE 8: Function with multiple return scenarios
# ============================================================================
def validate_password(password):
    """Check if password is strong"""
    if len(password) < 8:
        return "Too short (min 8 characters)"
    elif " " in password:
        return "Cannot contain spaces"
    elif not any(c.isupper() for c in password):
        return "Must contain uppercase letter"
    else:
        return "Valid"

print(validate_password("abc"))              # Too short
print(validate_password("pass word"))        # Spaces
print(validate_password("password"))         # No uppercase
print(validate_password("Password123"))      # Valid

# ============================================================================
# KEY TAKEAWAYS:
# ============================================================================
# 1. Functions start with 'def functionname():'
# 2. Parameters are inputs
# 3. return sends data back
# 4. Call by writing functionname(arguments)
# 5. Functions avoid code repetition
# 6. Default parameters: def func(x, y=5):
# 7. Functions with if/else make powerful logic
