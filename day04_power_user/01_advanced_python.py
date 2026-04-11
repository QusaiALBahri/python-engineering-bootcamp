"""Day 4 -Advanced Python: Files, Comprehensions, Decorators"""

import os
from datetime import datetime

# ============================================================================
# FILE HANDLING: Read, write, append
# ============================================================================

# WRITE to file
with open("notes.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

# READ from file
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

# APPEND to file
with open("notes.txt", "a") as f:
    f.write("Line 3 - appended\n")

# READ line by line
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

# ============================================================================
# ADVANCED LIST COMPREHENSIONS
# ============================================================================

# Nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for row in matrix for x in row]
print(flattened)

# Dictionary comprehension
words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)

# ============================================================================
# EXCEPTION HANDLING: Try/Except
# ============================================================================

try:
    age = int(input("Age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Valid age: {age}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("Done")

# ============================================================================
# DECORATORS: Functions that modify functions
# ============================================================================

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done {func.__name__}")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# ============================================================================
# GENERATORS: Functions that yield values one at a time
# ============================================================================

def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1

for num in count_up(5):
    print(num)

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
# 1. Use 'with' for file handling (automatic close)
# 2. "r" = read, "w" = write (overwrites), "a" = append
# 3. List comprehensions: [x for x in list if condition]
# 4. Exception handling: try/except/finally
# 5. @decorator modifies function behavior
# 6. yield in generator pauses and resumes
