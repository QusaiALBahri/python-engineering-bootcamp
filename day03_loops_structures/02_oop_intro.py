"""
Day 3, Lesson 2: Object-Oriented Programming (OOP) Basics
Covers:
  - Classes and objects
  - Attributes and methods
  - __init__ constructor
  - __str__ method
  - Inheritance
  - Class vs instance attributes
"""

# ============================================
# 1. Basic Class Definition
# ============================================

print("=" * 50)
print("Basic Classes and Objects")
print("=" * 50)

class Dog:
    """A simple Dog class"""
    
    def __init__(self, name, age, breed):
        """Initialize dog attributes"""
        self.name = name
        self.age = age
        self.breed = breed
    
    def describe(self):
        """Return dog description"""
        return f"{self.name} is a {self.age}-year-old {self.breed}"
    
    def birthday(self):
        """Increment age by 1"""
        self.age += 1
        return f"Happy birthday {self.name}! Now {self.age} years old."

# Create instances
dog1 = Dog("Buddy", 3, "Golden Retriever")
dog2 = Dog("Max", 1, "Beagle")

print(dog1.describe())
print(dog2.describe())
print(dog1.birthday())

# ============================================
# 2. __str__ Method (String Representation)
# ============================================

print("\n" + "=" * 50)
print("Using __str__ for Better Output")
print("=" * 50)

class Person:
    """Person class with __str__ method"""
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __str__(self):
        """Return a readable string representation"""
        return f"{self.first_name} {self.last_name} (Age: {self.age})"
    
    def greet(self):
        """Return a greeting"""
        return f"Hello, I'm {self.first_name}"

person1 = Person("Ali", "Ahmed", 25)
print(person1)  # Calls __str__ automatically
print(person1.greet())

# ============================================
# 3. Instance vs Class Attributes
# ============================================

print("\n" + "=" * 50)
print("Instance vs Class Attributes")
print("=" * 50)

class Car:
    """Car class demonstrating attributes"""
    
    wheels = 4  # Class attribute (shared by all instances)
    
    def __init__(self, brand, model, year):
        # Instance attributes (unique to each instance)
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
    
    def accelerate(self, amount):
        """Increase speed"""
        self.speed += amount
        return f"{self.brand} {self.model} now going {self.speed} km/h"
    
    def brake(self):
        """Decrease speed to zero"""
        self.speed = 0
        return "Car stopped"

car1 = Car("Toyota", "Camry", 2023)
car2 = Car("Honda", "Civic", 2022)

print(f"Car 1: {car1.brand} {car1.model}")
print(f"Car 2: {car2.brand} {car2.model}")
print(f"Both have {car1.wheels} wheels (class attribute)")
print(car1.accelerate(50))
print(car1.brake())

# ============================================
# 4. Methods: Instance, Behavior, Calculations
# ============================================

print("\n" + "=" * 50)
print("Methods and Object Behavior")
print("=" * 50)

class BankAccount:
    """Simple bank account class"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Add money to account"""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance:.2f}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        """Remove money from account"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance:.2f}"
        return "Insufficient funds"
    
    def check_balance(self):
        """Check current balance"""
        return f"Balance: ${self.balance:.2f}"

account = BankAccount("Ali", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.check_balance())

# ============================================
# 5. Inheritance (Class hierarchy)
# ============================================

print("\n" + "=" * 50)
print("Inheritance - Extending Classes")
print("=" * 50)

class Animal:
    """Base/Parent class"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """Generic animal sound"""
        return f"{self.name} makes a sound"
    
    def __str__(self):
        return f"Animal: {self.name}"

class Cat(Animal):
    """Derived/Child class - inherits from Animal"""
    
    def speak(self):
        """Override parent method"""
        return f"{self.name} meows"

class Dog(Animal):
    """Another derived class"""
    
    def speak(self):
        """Override parent method"""
        return f"{self.name} barks"

# Create instances of child classes
cat = Cat("Whiskers")
dog = Dog("Rex")

print(cat)
print(cat.speak())
print(dog)
print(dog.speak())
print(Animal("Generic").speak())

# ============================================
# 6. Composition (Objects containing objects)
# ============================================

print("\n" + "=" * 50)
print("Composition - Objects Containing Objects")
print("=" * 50)

class Engine:
    """Engine component"""
    
    def __init__(self, fuel_type, horsepower):
        self.fuel_type = fuel_type
        self.horsepower = horsepower
    
    def __str__(self):
        return f"{self.fuel_type} engine ({self.horsepower} HP)"

class Vehicle:
    """Vehicle containing an Engine"""
    
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model
        self.engine = engine  # Composition: Vehicle HAS-A Engine
    
    def __str__(self):
        return f"{self.brand} {self.model} with {self.engine}"

# Create engine
engine = Engine("Diesel", 150)

# Create vehicle with engine
vehicle = Vehicle("BMW", "X5", engine)
print(vehicle)

# ============================================
# 7. Practical Example: Library
# ============================================

print("\n" + "=" * 50)
print("Practical Example: Library System")
print("=" * 50)

class Book:
    """Represents a book"""
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

class Library:
    """Manages a collection of books"""
    
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        """Add a book to library"""
        self.books.append(book)
        return f"✓ Added: {book}"
    
    def find_book(self, title):
        """Find book by title"""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def list_all_books(self):
        """Display all books"""
        if not self.books:
            return "Library is empty"
        
        result = f"\n{self.name} Library ({len(self.books)} books):\n"
        for book in self.books:
            result += f"  • {book}\n"
        return result

# Create library
lib = Library("City Library")

# Add books
print(lib.add_book(Book("Python Basics", "Guido van Rossum", 2020)))
print(lib.add_book(Book("Algorithms", "Thomas Cormen", 2009)))
print(lib.add_book(Book("Clean Code", "Robert Martin", 2008)))

# List books
print(lib.list_all_books())

# Find book
found = lib.find_book("Python Basics")
print(f"✓ Found: {found}" if found else "Book not found")

# ============================================
# 8. Special Attributes and self
# ============================================

print("\n" + "=" * 50)
print("Understanding 'self'")
print("=" * 50)

class Counter:
    """Demonstrates self and special attributes"""
    
    def __init__(self, start=0):
        self.value = start
    
    def increment(self):
        """Increase counter (modifies self)"""
        self.value += 1
    
    def get_double(self):
        """Return double of self.value (doesn't modify)"""
        return self.value * 2
    
    def reset(self, new_value=0):
        """Reset counter to new value"""
        self.value = new_value

counter = Counter(5)
print(f"Initial value: {counter.value}")
counter.increment()
print(f"After increment: {counter.value}")
print(f"Double: {counter.get_double()}")
counter.reset(10)
print(f"After reset: {counter.value}")

# ============================================
# 9. Best Practices
# ============================================

print("\n" + "=" * 50)
print("OOP Best Practices")
print("=" * 50)

print("""
✓ DO:
  - Use descriptive class names (PascalCase)
  - Define __init__ to initialize attributes
  - Use __str__ for readable output
  - Use meaningful method names
  - Keep methods focused and small
  - Use inheritance for IS-A relationships
  - Use composition for HAS-A relationships
  - Add docstrings to classes and methods

✗ DON'T:
  - Create overly complex classes
  - Mix too many responsibilities in one class
  - Use __init__ for complex logic
  - Expose internal attributes without need
  - Ignore inheritance when it fits
  - Create deep inheritance hierarchies
""")

print("\n✅ Lesson 2 Complete!")
