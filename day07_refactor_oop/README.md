# Day 7: Object-Oriented Programming (OOP) Advanced

## Learning Outcomes

By the end of this day, you will understand:

| Topic | Skill | Example |
|-------|-------|---------|
| **Classes & Objects** | Create reusable templates | `class Dog` with methods  |
| **Inheritance** | Share code across similar classes | `Dog` inherits from `Animal` |
| **Polymorphism** | Same method, different behavior | `speak()` works for Dog and Cat |
| **Encapsulation** | Protect data with private attributes | `@property`, `_balance` |
| **Abstract Classes** | Define interfaces that must be implemented | `ABC`, `@abstractmethod` |
| **Composition vs Inheritance** | Know when to use HAS-A vs IS-A | Car HAS-A Engine vs Dog IS-A Animal |

---

## Key Concepts at a Glance

| Concept | Use Case | Example |
|---------|----------|---------|
| **Inheritance** | IS-A relationship | `Dog` IS-A `Animal` |
| **Composition** | HAS-A relationship | `Car` HAS-A `Engine` |
| **Polymorphism** | Same interface, different behavior | `Dog.speak()` vs `Cat.speak()` |
| **Encapsulation** | Hide internal details | `@property` for read-only access |
| **Abstract** | Enforce implementation | `ABC` forces subclass override |

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| ❌ Repeating code in subclasses | Maintenance nightmare | Use `super()` to call parent |
| ❌ Accessing private data directly | Breaks encapsulation | Use `@property` instead |
| ❌ Not calling `super().__init__()` | Lost parent's initialization | Always call in subclass `__init__` |
| ❌ Using inheritance when composition fits | Tight coupling | Ask: IS-A or HAS-A? |
| ❌ Forgetting `@abstractmethod` | Subclasses don't implement required methods | Use `ABC` for interface contracts |

---

## DRY Principle (Don't Repeat Yourself)

### ❌ BAD - Copy-paste code in 3 classes
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        return f"{self.name} is eating"

class Cat:
    def __init__(self, name, age):  # SAME CODE!
        self.name = name
        self.age = age
    def eat(self):  # SAME CODE!
        return f"{self.name} is eating"

class Bird:
    def __init__(self, name, age):  # SAME CODE!
        self.name = name
        self.age = age
    def eat(self):  # SAME CODE!
        return f"{self.name} is eating"
```

### ✅ GOOD - Write once, inherit everywhere
```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        return f"{self.name} is eating"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

class Bird(Animal):
    def speak(self):
        return f"{self.name} chirps"
```

---

## super() - Respect Your Parent

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal {name} created")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # ← Call parent's __init__
        self.breed = breed
        print(f"Dog {name} ({breed}) created")

dog = Dog("Buddy", "Golden Retriever")
# Output:
# Animal Buddy created
# Dog Buddy (Golden Retriever) created
```

---

## Practice Flow

### Step 1: Read the Lesson
- Read `01_oop_advanced.py` - 7 complete examples
- Understand: classes, inheritance, polymorphism, encapsulation

### Step 2: Run Examples
```bash
python 01_oop_advanced.py
```

### Step 3: Solve Exercises
- Start with Exercise 1 (Vehicle hierarchy)
- Progress to Exercise 4 (Game characters)
- Try the Challenge (Paladin)

### Step 4: Compare with Solutions
- See `SOLUTIONS.md` for complete code
- Understand design decisions

---

## Self-Assessment Checklist

- [ ] Understand class definition and `__init__`
- [ ] Can write a subclass that inherits from parent
- [ ] Call `super().__init__()` in subclass
- [ ] Can use polymorphism (different `speak()` in each class)
- [ ] Understand private attributes (`_balance`)
- [ ] Can use `@property` for encapsulation
- [ ] Know when to use inheritance (IS-A) vs composition (HAS-A)
- [ ] Can create abstract classes with `ABC`
- [ ] Solved all 4 exercises
- [ ] Could explain to a colleague: "Inheritance avoids code duplication"

---

## Key Takeaways

1. **Inheritance is powerful** - Write once, use many times
2. **Polymorphism is the point** - Same method name, different behavior
3. **Always call `super().__init__()`** - Don't break the parent class
4. **Protect your data** - Use `_` and `@property`
5. **Abstract classes define contracts** - Forces subclasses to implement
6. **IS-A vs HAS-A** - Inheritance or composition? Know the difference!
7. **Real code is full of inheritance** - Every professional codebase uses this

---

## Next Steps

- [ ] Complete all exercises
- [ ] Compare your code with SOLUTIONS.md
- [ ] Modify one exercise: add a new subclass
- [ ] Day 8: Agile sprints with more systems engineering
