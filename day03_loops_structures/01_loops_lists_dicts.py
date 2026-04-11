"""Day 3 - Loops & Data Structures"""

# ============================================================================
# FOR LOOPS: Repeat code a specific number of times
# ============================================================================

# Loop through numbers 0-4
for i in range(5):
    print(f"Number: {i}")

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with index
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# ============================================================================
# WHILE LOOPS: Repeat until condition is false
# ============================================================================

count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

password = ""
while password != "1234":
    password = input("Enter password: ")
if password == "1234":
    print("Correct!")

# ============================================================================
# LISTS: Ordered, changeable, allows duplicates
# ============================================================================

numbers = [1, 2, 3, 4, 5]
numbers.append(6)           # Add to end
numbers.insert(0, 0)        # Insert at position
numbers.remove(3)           # Remove first occurrence
numbers[0] = 10             # Change first element
print(numbers[0] + numbers[1])  # Access and math

# ============================================================================
# DICTIONARIES: Key-value pairs (like a real dictionary)
# ============================================================================

person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC"
}

print(person["name"])       # Access value by key
person["age"] = 26          # Change value
person["email"] = "alice@example.com"  # Add new key
print(person)

for key in person:
    print(f"{key}: {person[key]}")

# ============================================================================
# LIST COMPREHENSION: Concise way to create lists
# ============================================================================

# Traditional way
squares = []
for i in range(5):
    squares.append(i ** 2)

# List comprehension (shorter)
squares = [i ** 2 for i in range(5)]
print(squares)

# With conditions
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
# 1. for loops: for item in collection
# 2. while loops: while condition is True
# 3. Lists: [1, 2, 3]  - use .append(), .remove()
# 4. Dicts: {"key": "value"}  - access with ["key"]
# 5. List comprehension: [expression for item in list if condition]
