# Day 7: Object-Oriented Programming (OOP) Advanced

## Learning Outcomes

| Topic | Skill | Example |
|-------|-------|---------|
| **Classes & Inheritance** | Write reusable code with OOP | `Animal` → `Dog`, `Cat` |
| **Polymorphism** | Same method, different behavior | `speak()` in Dog vs Cat |
| **Encapsulation** | Private attributes with properties | `_balance`, `@property` |
| **Abstract Classes** | Define interface contracts | `ABC`, `@abstractmethod` |
| **Composition vs Inheritance** | Know when to use which | Engine in Car vs Car is Vehicle |

---

## Part 1: Classes & Objects Basics

### Class Definition

```python
class Dog:
    """A dog is a domestic animal that barks."""
    
    def __init__(self, name, age):
        """Initialize a dog with name and age."""
        self.name = name
        self.age = age
        self.tricks = []
    
    def add_trick(self, trick):
        """Teach the dog a new trick."""
        self.tricks.append(trick)
        print(f"{self.name} learned {trick}!")
    
    def speak(self):
        """Make the dog speak."""
        return f"{self.name} says: Woof!"


# Creating instances
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

dog1.add_trick("sit")
dog1.add_trick("fetch")

print(dog1.speak())  # Output: Buddy says: Woof!
print(dog1.tricks)   # Output: ['sit', 'fetch']
```

---

## Part 2: Inheritance

### The Problem
You have Dogs, Cats, and Birds. They all:
- Have `name` and `age`
- Can `speak()`
- Can `eat()`

Do you write the same code 3 times? **NO! Use inheritance.**

### The Solution

```python
class Animal:
    """Base class for all animals."""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        """All animals eat."""
        return f"{self.name} is eating..."
    
    def speak(self):
        """Override in subclasses."""
        raise NotImplementedError("Subclasses must implement speak()")


class Dog(Animal):  # Dog inherits from Animal
    """A dog is a type of animal."""
    
    def speak(self):
        """Dogs bark."""
        return f"{self.name} says: Woof!"


class Cat(Animal):  # Cat also inherits from Animal
    """A cat is a type of animal."""
    
    def speak(self):
        """Cats meow."""
        return f"{self.name} says: Meow!"


class Bird(Animal):
    """A bird is a type of animal."""
    
    def speak(self):
        """Birds chirp."""
        return f"{self.name} says: Chirp!"


# All without repeating __init__ or eat()!
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)
bird = Bird("Tweety", 1)

print(dog.speak())    # Woof!
print(cat.speak())    # Meow!
print(bird.speak())   # Chirp!

print(dog.eat())      # Buddy is eating...
print(cat.eat())      # Whiskers is eating...
print(bird.eat())     # Tweety is eating...
```

---

## Part 3: Polymorphism

**Polymorphism** = "Many forms" = Same method name, different behavior

```python
# From above: Dog, Cat, Bird all have speak()
# Each does it DIFFERENTLY, but we call it the SAME way

animals = [dog, cat, bird]

# This works on ALL animals, even though they speak differently!
for animal in animals:
    print(animal.speak())

# Output:
# Buddy says: Woof!
# Whiskers says: Meow!
# Tweety says: Chirp!
```

---

## Part 4: Encapsulation (Private Attributes)

### The Problem
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.balance = balance  # Anyone can change this!

account = BankAccount("Alice", 1000)
account.balance = -999999  # OOPS! Negative balance!
```

### The Solution: Private Attributes

```python
class BankAccount:
    """A bank account with protected balance."""
    
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # Convention: _ means "private"
    
    def deposit(self, amount):
        """Add money safely."""
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        return self._balance
    
    def withdraw(self, amount):
        """Remove money safely."""
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return self._balance
    
    @property
    def balance(self):
        """Read balance (no direct access)."""
        return self._balance


account = BankAccount("Alice", 1000)
print(account.balance)      # OK: 1000
account.deposit(500)        # OK: 1500
account.withdraw(200)       # OK: 1300

# These now fail properly:
# account.balance = -999  # Error!
# account.withdraw(-50)   # Error!
```

---

## Part 5: Abstract Classes (Interface Contracts)

### The Problem
Someone might forget to implement `speak()` in their Animal subclass

### The Solution: Abstract Base Class

```python
from abc import ABC, abstractmethod

class Animal(ABC):  # ABC = Abstract Base Class
    """All animals must implement speak()."""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def speak(self):
        """Every subclass MUST implement this."""
        pass  # No implementation - subclass must do it


class Dog(Animal):
    def speak(self):
        return f"{self.name} barks: Woof!"


# This will fail:
# animal = Animal("Generic")  # Error! Can't instantiate abstract class

# But this works:
dog = Dog("Buddy")
print(dog.speak())


# If you forget speak() in a subclass:
class BadDog(Animal):
    pass  # Forgot to implement speak()

# bad = BadDog("Bad")  # Error! Must implement speak()
```

---

## Part 6: Composition vs Inheritance

### Inheritance: "IS-A"
`Dog` **IS-A** `Animal`

```python
class Dog(Animal):
    pass
```

### Composition: "HAS-A"
`Car` **HAS-A** `Engine`

```python
class Engine:
    def __init__(self, power):
        self.power = power
    
    def start(self):
        return f"Engine started ({self.power}hp)"


class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # HAS-A engine
    
    def drive(self):
        return f"{self.brand} is driving with {self.engine.start()}"


my_engine = Engine(200)
my_car = Car("Toyota", my_engine)
print(my_car.drive())
# Output: Toyota is driving with Engine started (200hp)
```

### When to Use Which?

| Use Inheritance | Use Composition |
|-----------------|-----------------|
| `Dog` IS-A `Animal` | `Car` HAS-A `Engine` |
| Behavior is similar | Behavior is different |
| Natural hierarchy | Flexible relationships |
| Limited depth (2-3) | Can be complex |

---

## Part 7: Real-World Example: Zoo Management System

```python
from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    """Abstract animal for all zoo animals."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.health = 100
    
    @abstractmethod
    def speak(self):
        """Every animal makes a sound."""
        pass
    
    def eat(self, food):
        """All animals eat."""
        self.health = min(100, self.health + 10)
        return f"{self.name} ate {food}"


class Mammal(Animal):
    """Mammals are warm-blooded."""
    
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color


class Lion(Mammal):
    def speak(self):
        return f"{self.name} roars: RAAAWWWWRRR!"


class Elephant(Mammal):
    def speak(self):
        return f"{self.name} trumpets: PAAHHH!"


class Zoo:
    """Zoo manages a collection of animals."""
    
    def __init__(self, name):
        self.name = name
        self.animals: List[Animal] = []
    
    def add_animal(self, animal):
        """Add animal to zoo."""
        self.animals.append(animal)
        print(f"Added {animal.name} to {self.name}")
    
    def show_all(self):
        """Display all animals and their sounds."""
        print(f"\n{self.name} Exhibit:")
        for animal in self.animals:
            print(f"  - {animal.name} ({animal.species}): {animal.speak()}")
    
    def feed_all(self, food):
        """Feed all animals."""
        for animal in self.animals:
            print(animal.eat(food))


# Usage
zoo = Zoo("Safari Park")

lion = Lion("Simba", "African Lion", "golden")
elephant = Elephant("Dumbo", "Asian Elephant", "gray")

zoo.add_animal(lion)
zoo.add_animal(elephant)

zoo.show_all()
# Output:
# Safari Park Exhibit:
#   - Simba (African Lion): Simba roars: RAAAWWWWRRR!
#   - Dumbo (Asian Elephant): Dumbo trumpets: PAAHHH!

zoo.feed_all("grass")
# Output:
# Simba ate grass
# Dumbo ate grass
```

---

## Exercises

1. **Create a Vehicle Hierarchy**
   - Base class: `Vehicle` with `speed`, `start()`, `stop()`
   - Subclasses: `Car`, `Motorcycle`, `Bus`
   - Each has different `start()` messages

2. **Bank Account, Enhanced**
   - Create a `SavingsAccount` subclass
   - Add interest calculation
   - Protect balance with `@property`

3. **Zoo Manager, Extended**
   - Add `Reptile` class
   - Add `Snake` and `Lizard` subclasses
   - Add `Zookeeper` class with `feed_animal()` method

4. **Game Characters**
   - Base: `Character` with `health`, `attack()`
   - Subclasses: `Warrior`, `Mage`, `Archer`
   - Each has different attack behavior

---

## Key Takeaways

1. **OOP prevents code duplication** - Inheritance = DRY principle
2. **Polymorphism is powerful** - Same code works on different types
3. **Private attributes protect data** - Use `_` and `@property`
4. **Abstract classes define contracts** - Force subclasses to implement methods
5. **IS-A vs HAS-A** - Know the difference for good design
6. **Real code follows these patterns** - Every professional codebase uses this

---

## Next Steps

- [ ] Run all code examples above
- [ ] Complete exercises 1-4
- [ ] Compare your code with professional patterns
- [ ] Day 8: Agile sprints with more systems engineering
