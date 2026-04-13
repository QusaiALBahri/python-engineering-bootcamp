# Day 3: Loops, Data Structures & OOP Basics

**Focus:** Master iteration, container data types, and object-oriented programming fundamentals

## 📚 Learning Outcomes

By the end of Day 3, you will understand:

- **For loops** (iteration, ranges, break/continue)
- **While loops** (conditional iteration, sentinel values)
- **Lists** (creation, indexing, methods, slicing)
- **Tuples** (immutable sequences, unpacking)
- **Dictionaries** (key-value pairs, methods)
- **Sets** (unique elements, operations)
- **Object-Oriented Programming (OOP)** basics (classes, objects, attributes)

## 🚀 Quick Start

```bash
# Run individual lessons
python 01_loops_lists_dicts.py
python 02_oop_intro.py

# Complete exercises
python -m pytest EXERCISES.md
```

## 📖 Lesson Breakdown

### Lesson 1: Loops, Lists & Dictionaries
Deep dive into iterative structures and essential data containers used in Python daily.

**Topics:**
- For loops with ranges and iterables
- While loops for conditional iteration
- Loop control (break, continue, else)
- Lists: operations, iteration, comprehensions
- Tuples: unpacking and use cases
- Dictionaries: accessing, modifying, iterating
- Sets: unique elements and operations

**Key Concepts:**
```python
# For loops
for i in range(5):
    print(i)

# While loops
while count < 10:
    count += 1

# List operations
numbers = [1, 2, 3]
numbers.append(4)

# Dictionary access
user = {"name": "Ali", "age": 25}
print(user["name"])

# Set operations
unique = {1, 2, 2, 3}  # {1, 2, 3}
```

### Lesson 2: Object-Oriented Programming Intro
Introduction to classes, objects, attributes, and methods - fundamental to modern Python programming.

**Topics:**
- Classes vs Objects
- Creating classes with `__init__`
- Instance attributes
- Instance methods
- Special method `__str__`
- Inheritance basics
- Object composition

**Key Concepts:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"

person = Person("Ali", 25)
print(person.greet())
```

## 🎯 Mini-Project: Personal Library Manager

Build a simple library system:

```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        for book in self.books:
            print(book)

# Usage
lib = Library()
lib.add_book(Book("Python Basics", "Ali", 2024))
lib.add_book(Book("Web Dev", "Sara", 2023))
lib.list_books()
```

## 💡 Pro Tips

1. **List Comprehensions:** Write clean, efficient list creation
   ```python
   squares = [x**2 for x in range(10)]
   ```

2. **Dictionary Comprehensions:** Create dictionaries elegantly
   ```python
   word_lengths = {word: len(word) for word in ["code", "python"]}
   ```

3. **Unpacking:** Extract values from tuples/lists
   ```python
   x, y = (10, 20)
   a, *rest = [1, 2, 3, 4]  # a=1, rest=[2,3,4]
   ```

4. **Loop Control:** Use `break` and `continue` wisely
   ```python
   for num in range(10):
       if num == 5:
           break  # Exit loop
   ```

5. **Type Checking:** Use `isinstance()` to check object types
   ```python
   if isinstance(obj, MyClass):
       # obj is an instance of MyClass
   ```

## 📝 Practice Exercises

See [EXERCISES.md](EXERCISES.md) for:
- 🔵 Beginner: Find items in lists, count elements, basic dictionaries
- 🟢 Intermediate: List comprehensions, dictionary operations, OOP basics
- 🔴 Advanced: Nested structures, class inheritance, set operations

## 🔗 Resources

- [Python Lists Documentation](https://docs.python.org/3/tutorial/datastructures.html)
- [Classes in Python](https://docs.python.org/3/tutorial/classes.html)
- [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Dictionaries Deep Dive](https://realpython.com/python-dicts/)

## ✅ Checklist for Day 3

- [ ] Completed Lesson 1: Loops & Data Structures
- [ ] Completed Lesson 2: OOP Basics
- [ ] Practiced with lists, tuples, dicts, sets
- [ ] Created at least one class with methods
- [ ] Solved 5+ exercises
- [ ] Understand when to use which data structure

---

**Next:** Day 4 builds on these concepts with advanced patterns and file I/O
