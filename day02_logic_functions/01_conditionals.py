"""
Day 2 - Session 1: Conditional Logic (if/elif/else)
=====================================================

LEARNING OBJECTIVES:
- Use if/elif/else to make decisions
- Compare values with ==, !=, <, >, <=, >=
- Combine conditions with 'and', 'or', 'not'
- Create branching logic

KEY CONCEPTS:
- if: Check a condition, run code if True
- elif: Check another condition if first is False
- else: Run if all conditions are False
"""

# ============================================================================
# EXAMPLE 1: Basic if statement
# ============================================================================
age = 20
if age >= 18:
    print("You are an adult")
print("Done")  # This always runs

# ============================================================================
# EXAMPLE 2: if/else (two paths)
# ============================================================================
score = 75
if score >= 60:
    print("You passed!")
else:
    print("You failed. Try again.")

# ============================================================================
# EXAMPLE 3: elif (multiple conditions)
# ============================================================================
grade_points = 85

if grade_points >= 90:
    grade = "A"
elif grade_points >= 80:
    grade = "B"
elif grade_points >= 70:
    grade = "C"
elif grade_points >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

# ============================================================================
# EXAMPLE 4: Comparison operators
# ============================================================================
x = 10
y = 5

print(f"{x} == {y}: {x == y}")      # False (equal)
print(f"{x} != {y}: {x != y}")      # True (not equal)
print(f"{x} > {y}: {x > y}")        # True (greater)
print(f"{x} < {y}: {x < y}")        # False (less)
print(f"{x} >= {y}: {x >= y}")      # True (greater or equal)
print(f"{x} <= {y}: {x <= y}")      # False (less or equal)

# ============================================================================
# EXAMPLE 5: AND operator (both conditions must be True)
# ============================================================================
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")
else:
    print("You cannot drive")

# ============================================================================
# EXAMPLE 6: OR operator (at least one must be True)
# ============================================================================
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today!")
else:
    print("Work day")

# ============================================================================
# EXAMPLE 7: NOT operator (reverse true/false)
# ============================================================================
is_raining = False

if not is_raining:
    print("Let's go outside")
else:
    print("Stay inside")

# ============================================================================
# EXAMPLE 8: Discount calculator - practical use
# ============================================================================
purchase_amount = 150
customer_type = "VIP"

if customer_type == "VIP" and purchase_amount > 100:
    discount = purchase_amount * 0.2  # 20% discount
    print(f"VIP Discount! You save ${discount:.2f}")
elif purchase_amount > 100:
    discount = purchase_amount * 0.1  # 10% discount
    print(f"Loyalty discount! You save ${discount:.2f}")
else:
    print("No discount available")

# ============================================================================
# KEY TAKEAWAYS:
# ============================================================================
# 1. if: runs code if condition is True
# 2. elif: check another condition if first is False
# 3. else: runs if all above conditions are False
# 4. ==: equal to
# 5. !=: not equal to
# 6. >: greater than
# 7. <: less than
# 8. and: both must be True
# 9. or: at least one must be True
# 10. not: flips True/False
