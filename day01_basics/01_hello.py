"""
Day 1 - Session 1: Hello World & Input/Output
================================================

LEARNING OBJECTIVES:
- Use print() for output
- Use input() for getting user input
- Understand strings (text)
- Get started with Python

KEY CONCEPTS:
- print() sends text to the console
- input() pauses and waits for user typing
- Everything in quotes is a string
"""

# ============================================================================
# EXAMPLE 1: Basic print()
# ============================================================================
print("Hello, World!")
print("Welcome to Python!")

# ============================================================================
# EXAMPLE 2: Multiple prints on same line (use end parameter)
# ============================================================================
print("Hello", end=" ")
print("Python!")

# ============================================================================
# EXAMPLE 3: Getting user input
# ============================================================================
name = input("What is your name? ")
print("Nice to meet you,", name, "!")

# ============================================================================
# EXAMPLE 4: Using input() output in a sentence
# ============================================================================
age_str = input("How old are you? ")
print(f"You are {age_str} years old. Next year you'll be {int(age_str) + 1}!")

# ============================================================================
# KEY TAKEAWAYS:
# ============================================================================
# 1. print() outputs text to console
# 2. input() asks user for text and stores it
# 3. Text in quotes is a STRING (str type)
# 4. f-strings let you put variables inside text with {}
# 5. Variables store information for later use
