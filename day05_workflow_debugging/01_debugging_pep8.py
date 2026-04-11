"""Day 5 - Professional Workflow & Debugging"""

import logging

# ============================================================================
# DEBUGGING TECHNIQUES
# ============================================================================

# 1. PRINT DEBUGGING - Basic but effective
def calculate_discount(price, discount_rate):
    print(f"DEBUG: price={price}, discount_rate={discount_rate}")
    discount = price * discount_rate
    print(f"DEBUG: discount={discount}")
    return price - discount

result = calculate_discount(100, 0.1)
print(f"Final: {result}")

# 2. LOGGING - Professional debugging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def divide(a, b):
    logging.debug(f"Dividing {a} by {b}")
    if b == 0:
        logging.error("Cannot divide by zero")
        return None
    result = a / b
    logging.info(f"Result: {result}")
    return result

divide(10, 2)
divide(10, 0)

# 3. ASSERT - Test assumptions
def set_age(age):
    assert age >= 0, "Age must be non-negative"
    assert age <= 150, "Age seems unrealistic"
    return age

try:
    set_age(25)      # OK
    #set_age(-5)     # Would raise AssertionError
except AssertionError as e:
    print(f"Assertion failed: {e}")

# ============================================================================
# PEP 8 - Code Style Guide
# ============================================================================

# GOOD: Clear naming, proper spacing
def calculate_total_price(items, tax_rate):
    subtotal = sum(items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

# BAD: Poor naming, no spaces
#def ct(i,t):
# st=sum(i)
# tx=st*t
# return st+tx

# Use meaningful variable names
users = ["Alice", "Bob", "Charlie"]
for user in users:
    print(user)

# ============================================================================
# GIT BASICS - Version Control
# ============================================================================

# Commands to know:
"""
git init              # Create repo
git add file.py       # Stage file
git commit -m "msg"   # Save changes
git log               # View history
git branch            # List branches
git checkout -b name  # Create new branch
git push origin main  # Send to GitHub
"""

# ============================================================================
# TEST WRITING - Ensure code works
# ============================================================================

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("All tests passed!")

def add(a, b):
    return a + b

# test_add()

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
# 1. Use logging for production code
# 2. Use assert for development
# 3. Follow PEP 8 style guide
# 4. Use meaningful names
# 5. commit often with clear messages
# 6. Write tests for critical functions
