"""
Day 4, Lesson 1: Generators, Decorators & Advanced Patterns
Covers:
  - Generator functions with yield
  - Memory efficiency vs lists
  - Basic and advanced decorators
  - Function wrappers
  - Lambda functions
  - Map, filter, reduce patterns
"""

import time
import functools

# ============================================
# 1. Generators - Efficient Iteration
# ============================================

print("=" * 50)
print("Generators vs Lists")
print("=" * 50)

def count_up_list(n):
    """Returns all numbers as a list (memory-intensive)"""
    result = []
    for i in range(n):
        result.append(i)
    return result

def count_up_generator(n):
    """Yields numbers one at a time (memory-efficient)"""
    for i in range(n):
        yield i

# Compare memory usage
print("List approach (creates all at once):")
list_result = count_up_list(5)
print(f"  Result: {list_result}")

print("\nGenerator approach (creates on demand):")
gen = count_up_generator(5)
print(f"  Generator object: {gen}")
for value in gen:
    print(f"  Value: {value}")

# ============================================
# 2. Generator Examples
# ============================================

print("\n" + "=" * 50)
print("Generator Examples")
print("=" * 50)

def fibonacci(limit):
    """Generate Fibonacci sequence"""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print("Fibonacci numbers < 100:")
for fib in fibonacci(100):
    print(fib, end=" ")

print("\n\nInfinite counter (first 5):")
def infinite_counter():
    """Generate infinite sequence"""
    count = 0
    while True:
        yield count
        count += 1

counter = infinite_counter()
for _ in range(5):
    print(next(counter), end=" ")

# ============================================
# 3. Basic Decorators
# ============================================

print("\n\n" + "=" * 50)
print("Basic Decorators")
print("=" * 50)

def simple_decorator(func):
    """Simple decorator that wraps a function"""
    def wrapper():
        print("  [Decorator] Before function call")
        func()
        print("  [Decorator] After function call")
    return wrapper

@simple_decorator
def say_hello():
    print("  Hello!")

say_hello()

# ============================================
# 4. Decorators with Arguments
# ============================================

print("\n" + "=" * 50)
print("Decorators with Arguments")
print("=" * 50)

def repeat_decorator(times):
    """Decorator that repeats function output"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"  [{i+1}]", end=" ")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_decorator(3)
def greet(name):
    print(f"Hello {name}!")

greet("Ali")

# ============================================
# 5. Timing Decorator (Practical Example)
# ============================================

print("\n" + "=" * 50)
print("Timing Decorator")
print("=" * 50)

def timing_decorator(func):
    """Decorator that measures function execution time"""
    @functools.wraps(func)  # Preserves original function name
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  ⏱️ {func.__name__} took {(end-start)*1000:.2f}ms")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """Simulate slow operation"""
    total = 0
    for i in range(1000000):
        total += i
    return total

@timing_decorator
def fast_function():
    """Quick operation"""
    return sum(range(100))

slow_function()
fast_function()

# ============================================
# 6. Lambda Functions
# ============================================

print("\n" + "=" * 50)
print("Lambda Functions (Anonymous Functions)")
print("=" * 50)

# Simple lambdas
square = lambda x: x ** 2
add = lambda x, y: x + y
is_positive = lambda x: x > 0

print(f"square(5) = {square(5)}")
print(f"add(3, 7) = {add(3, 7)}")
print(f"is_positive(-5) = {is_positive(-5)}")

# Lambda with sorting
students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "Mona", "score": 78}
]

sorted_by_score = sorted(students, key=lambda s: s["score"], reverse=True)
print("\nSorted by score:")
for student in sorted_by_score:
    print(f"  {student['name']}: {student['score']}")

# ============================================
# 7. Map Function
# ============================================

print("\n" + "=" * 50)
print("Map Function (Apply function to items)")
print("=" * 50)

numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x**2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# Convert to strings
as_strings = list(map(str, numbers))
print(f"As strings: {as_strings}")

# ============================================
# 8. Filter Function
# ============================================

print("\n" + "=" * 50)
print("Filter Function (Select matching items)")
print("=" * 50)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Original: {numbers}")
print(f"Evens only: {evens}")

# Get numbers > 5
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"Greater than 5: {greater_than_5}")

# ============================================
# 9. Reduce Function
# ============================================

print("\n" + "=" * 50)
print("Reduce Function (Combine items)")
print("=" * 50)

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum using reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Numbers: {numbers}")
print(f"Product: {product}")  # 1*2*3*4*5 = 120

# Combine strings
words = ["Hello", " ", "Python", "!"]
combined = reduce(lambda x, y: x + y, words)
print(f"Combined: {combined}")

# ============================================
# 10. Advanced Decorators (Practical)
# ============================================

print("\n" + "=" * 50)
print("Advanced: Logging Decorator")
print("=" * 50)

def logging_decorator(func):
    """Decorator that logs function calls"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  📝 Calling: {func.__name__}")
        print(f"     Args: {args}, Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"     Result: {result}")
        return result
    return wrapper

@logging_decorator
def divide(a, b):
    return a / b

divide(10, 2)

# ============================================
# 11. Best Practices
# ============================================

print("\n" + "=" * 50)
print("Best Practices")
print("=" * 50)

print("""
✓ DO:
  - Use generators for large datasets
  - Use @functools.wraps in decorators
  - Keep lambda functions simple
  - Use map/filter for functional operations
  - Document decorators clearly

✗ DON'T:
  - Overuse decorators
  - Chain too many decorators
  - Use lambda for complex logic
  - Ignore generator memory benefits
  - Forget to handle decorator arguments
""")

print("\n✅ Lesson 1 Complete!")
