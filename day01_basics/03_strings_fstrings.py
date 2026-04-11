"""
Day 1 - Session 3: Strings & F-Strings
=======================================

LEARNING OBJECTIVES:
- Manipulate and format strings
- Use f-strings for embedding variables
- Practice string methods
- Output formatted text

KEY CONCEPTS:
- Strings are text (enclosed in quotes)
- F-strings use {} to insert variables
- Strings have methods like .upper(), .lower(), .strip()
"""

# ============================================================================
# EXAMPLE 1: Creating strings
# ============================================================================
message = "Hello, Python!"
name = 'Alice'  # Both " and ' work for strings

print(message)
print(name)

# ============================================================================
# EXAMPLE 2: String concatenation (combining strings)
# ============================================================================
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# ============================================================================
# EXAMPLE 3: F-strings (modern Python way)
# ============================================================================
age = 25
city = "New York"
# Use f before the quote, then {} for variables
print(f"{first_name} is {age} years old and lives in {city}")

# ============================================================================
# EXAMPLE 4: F-strings with expressions
# ============================================================================
price = 50
quantity = 3
print(f"Item price: ${price}")
print(f"Quantity: {quantity}")
print(f"Total: ${price * quantity}")

# ============================================================================
# EXAMPLE 5: String methods (.upper(), .lower(), .strip())
# ============================================================================
text = "  Hello World  "
print(f"Original: '{text}'")
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print(f"Stripped: '{text.strip()}'")

# ============================================================================
# EXAMPLE 6: String indexing (getting specific characters)
# ============================================================================
word = "Python"
print(f"First letter: {word[0]}")          # P
print(f"Second letter: {word[1]}")         # y
print(f"Last letter: {word[-1]}")          # n
print(f"Last 3 letters: {word[-3:]}")      # hon

# ============================================================================
# EXAMPLE 7: String length
# ============================================================================
text = "Hello"
print(f"Length of '{text}': {len(text)} characters")

# ============================================================================
# EXAMPLE 8: Checking if text contains something
# ============================================================================
sentence = "Python is awesome"
print("Python" in sentence)        # True
print("Java" in sentence)          # False

# ============================================================================
# KEY TAKEAWAYS:
# ============================================================================
# 1. Strings are text in quotes ("text" or 'text')
# 2. Use + to combine strings
# 3. F-strings: f"Message {variable}" to embed variables
# 4. .upper() makes UPPERCASE
# 5. .lower() makes lowercase
# 6. .strip() removes spaces at start/end
# 7. [0] gets first character, [-1] gets last
# 8. len() counts characters
# 9. Use 'in' to check if text contains something
