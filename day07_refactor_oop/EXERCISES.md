# Day 7: OOP Exercises

## Exercise 1: The Vehicle Hierarchy

### Your Task
Create a `Vehicle` class and three subclasses.

### Requirements
- **Vehicle** (base class):
  - Attributes: `brand`, `speed`, `is_running`
  - Methods: `start()`, `stop()`, `accelerate()`

- **Car** (inherits from Vehicle):
  - Additional attribute: `doors`
  - Override `start()`: Print "Car engine starts: Vroooom!"

- **Motorcycle** (inherits from Vehicle):
  - Additional attribute: `has_sidecar`
  - Override `start()`: Print "Motorcycle engine starts: Vrrrooooom!"

- **Bus** (inherits from Vehicle):
  - Additional attribute: `capacity`
  - Override `start()`: Print "Bus engine starts: Choo-choo!"

### Starter Code
```python
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        self.is_running = False
    
    def start(self):
        raise NotImplementedError("Subclasses must implement start()")
    
    def stop(self):
        self.is_running = False
        return f"{self.brand} stopped"
    
    def accelerate(self):
        if self.is_running:
            return f"{self.brand} is now going {self.speed} km/h"
        else:
            return f"Start the {self.brand} first!"


# Your code here:
class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

class Bus(Vehicle):
    pass


# Test it:
car = Car("Toyota", 200)
print(car.start())  # Should print: Car engine starts: Vroooom!

motorcycle = Motorcycle("Harley", 250)
print(motorcycle.start())  # Should print: Motorcycle engine starts: Vrrrooooom!

bus = Bus("Mercedes", 120)
print(bus.start())  # Should print: Bus engine starts: Choo-choo!
```

### Expected Output
```
Car engine starts: Vroooom!
Motorcycle engine starts: Vrrrooooom!
Bus engine starts: Choo-choo!
```

---

## Exercise 2: Bank Account with Encapsulation

### Your Task
Create a `BankAccount` class with protected balance and a `SavingsAccount` subclass.

### Requirements
- **BankAccount**:
  - Private attribute: `_balance`
  - Public property: `balance` (read-only)
  - Methods: `deposit(amount)`, `withdraw(amount)`
  - Validation: Reject negative amounts, overdrafts

- **SavingsAccount** (inherits from BankAccount):
  - Additional attribute: `interest_rate`
  - Method: `apply_interest()` - adds interest to balance
  - Validation: Minimum balance of $100

### Starter Code
```python
class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self._balance = initial_balance
    
    @property
    def balance(self):
        """Read balance (no direct modification)."""
        return self._balance
    
    def deposit(self, amount):
        """Add money validly."""
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        return f"Deposited ${amount}. New balance: ${self._balance}"
    
    def withdraw(self, amount):
        """Remove money validly."""
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return f"Withdrew ${amount}. New balance: ${self._balance}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, initial_balance, interest_rate):
        super().__init__(owner, initial_balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        """Add interest to balance."""
        # Your code here
        pass


# Test it:
savings = SavingsAccount("Alice", 1000, 0.05)
print(savings.balance)  # 1000
print(savings.deposit(500))  # 1500
print(savings.apply_interest())  # 1575 (1500 * 1.05)
```

### Expected Output
```
1000
Deposited $500. New balance: $1500
Interest added: $75. New balance: $1575
```

---

## Exercise 3: Zoo Manager (Extending the Example)

### Your Task
Add `Reptile`, `Snake`, and `Zookeeper` to the Zoo system from the lesson.

### Requirements
- **Reptile** class (inherits from Animal):
  - Additional attribute: `is_venomous`
  - Method: `shed_skin()` - returns message about shedding

- **Snake** (inherits from Reptile):
  - Override `speak()`: Return "hissing sound"

- **Zookeeper** class:
  - Attributes: `name`, `animals_fed` (count)
  - Method: `feed_animal(animal, food)` - feeds animal, increments counter
  - Method: `get_report()` - returns how many animals fed today

### Starter Code
```python
# Use the Animal and Zoo classes from the lesson
# Add your code here:

class Reptile(Animal):
    pass

class Snake(Reptile):
    pass

class Zookeeper:
    pass


# Test it:
zoo = Zoo("Safari Park")

snake = Snake("Sly", "Python", venomous=False)
zoo.add_animal(snake)

keeper = Zookeeper("Bob")
keeper.feed_animal(snake, "mice")

print(keeper.get_report())  # Output: Bob fed 1 animals today
```

---

## Exercise 4: Game Characters (OOP Design)

### Your Task
Create a game with different character types.

### Requirements
- **Character** (base class):
  - Attributes: `name`, `health`, `max_health`, `damage`
  - Method: `attack(target)` - reduces target health
  - Method: `take_damage(amount)` - reduces own health
  - Method: `is_alive()` - True if health > 0

- **Warrior** (inherits from Character):
  - Override `attack()`: Does 1.5x damage due to strength

- **Mage** (inherits from Character):
  - Additional attribute: `mana`
  - Override `attack()`: Uses mana (costs 10 mana, 2x damage)

- **Archer** (inherits from Character):
  - Additional attribute: `arrows`
  - Override `attack()`: Uses arrows (costs 1 arrow, range checks)

### Starter Code
```python
class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
    
    def attack(self, target):
        target.take_damage(self.damage)
        return f"{self.name} attacks {target.name}"
    
    def take_damage(self, amount):
        self.health -= amount
        return f"{self.name} took {amount} damage. Health: {self.health}"
    
    def is_alive(self):
        return self.health > 0


class Warrior(Character):
    def attack(self, target):
        damage = int(self.damage * 1.5)  # 50% stronger
        target.take_damage(damage)
        return f"{self.name} swings sword for {damage} damage!"


class Mage(Character):
    def __init__(self, name, health, damage, mana):
        super().__init__(name, health, damage)
        self.mana = mana
    
    def attack(self, target):
        if self.mana < 10:
            return f"{self.name} has no mana!"
        self.mana -= 10
        damage = self.damage * 2
        target.take_damage(int(damage))
        return f"{self.name} casts fireball for {int(damage)} damage!"


class Archer(Character):
    # Your code here
    pass


# Test it
warrior = Warrior("Conan", 100, 20)
mage = Mage("Gandalf", 80, 15, 50)
archer = Archer("Robin", 70, 15, 20)

enemy = Character("Goblin", 50, 5)

print(warrior.attack(enemy))  # Warrior deals 30 damage
print(mage.attack(enemy))     # Mage deals 30 damage
print(archer.attack(enemy))   # Archer deals 15 damage (uses 1 arrow)
print(enemy.is_alive())       # True (still has health)
```

---

## Challenge: Multi-Class System

### Your Task
Create a `PaladnKnight` that is both Warrior AND Mage (uses multiple inheritance or composition).

### Hint
This is tricky! You have options:
1. **Multiple Inheritance**: `class Paladin(Warrior, Mage)`
2. **Composition**: Give Paladin both warrior and mage abilities

### Requirements
- **Paladin**:
  - Warrior's 1.5x damage
  - Mage's mana and spells
  - Can choose to use sword (warrior) or spell (mage)

### Starter Code
```python
# Option 1: Multiple Inheritance
class Paladin(Warrior, Mage):
    def __init__(self, name):
        Character.__init__(self, name, 150, 20)
        self.mana = 30  # Paladins have mana too
    
    def attack_with_sword(self, target):
        return super().attack(target)  # Uses Warrior's 1.5x damage
    
    def attack_with_spell(self, target):
        # Your code: Use Mage's spell attack
        pass


# Option 2: Composition
class Paladin:
    def __init__(self, name):
        self.warrior = Warrior(name, 150, 20)
        self.mage = Mage(name, 150, 20, 30)
    
    def attack_with_sword(self, target):
        return self.warrior.attack(target)
    
    def attack_with_spell(self, target):
        return self.mage.attack(target)
```

---

## Solutions

After trying, check [SOLUTIONS.md](SOLUTIONS.md) for complete solutions.

---

## Checklist

- [ ] Exercise 1: Vehicle hierarchy works
- [ ] Exercise 2: Bank accounts with validation
- [ ] Exercise 3: Zoo with reptiles and keeper
- [ ] Exercise 4: Game characters with inheritance
- [ ] Challenge: Paladin with multiple abilities
