# Day 1 Exercises: Basics (Input, Variables, Data Types, Strings)

## Warm-up Exercises

### Exercise 1: Age Calculator
Write a program that:
- Asks the user for their name
- Asks the user for their birth year
- Calculates their age (2024 - birth_year)
- Prints: "Hello [name]! You are [age] years old."

**Hint:** Use input(), int(), and f-strings

**Challenge:** Ask what year it currently is instead of hardcoding 2024

---

### Exercise 2: Rectangle Area
Write a program that:
- Asks for length of rectangle
- Asks for width of rectangle
- Calculates the area (length × width)
- Prints result with proper label

**Example Output:**
```
Length: 5
Width: 3
Area: 15 square units
```

**Challenge:** Also calculate and display the perimeter (2 × length + 2 × width)

---

### Exercise 3: Temperature Converter
Write a program that converts Celsius to Fahrenheit:
- Formula: F = (C × 9/5) + 32
- Ask user for Celsius temperature
- Display the Fahrenheit equivalent

**Example:**
```
Enter temperature in Celsius: 0
0°C is 32°F
```

**Challenge:** Also convert Fahrenheit to Celsius (C = (F - 32) × 5/9)

---

### Exercise 4: String Manipulation
Given the string operations, write a program that:
- Asks user for their name
- Displays it in UPPERCASE
- Displays it in lowercase
- Displays the number of characters
- Displays first 3 letters
- Displays last 3 letters

**Example Output:**
```
Your name: Alice
UPPERCASE: ALICE
lowercase: alice
Length: 5
First 3 letters: Ali
Last 3 letters: ice
```

---

### Exercise 5: Simple Banking
Write a program that:
- Asks for customer name
- Asks for starting balance
- Asks for deposit amount
- Calculates new balance
- Displays formatted receipt

**Example Output:**
```
=== Bank Receipt ===
Customer: Muhammad
Starting Balance: $1000.50
Deposit: $250.00
New Balance: $1250.50
```

**Challenge:** Ask for multiple transactions (deposit and withdrawal)

---

## Tricky Questions (Test Your Understanding)

1. What's the difference between `"25"` and `25`?
2. When you do `input()`, what type does it return?
3. How would you convert the string `"3.14"` to a decimal number?
4. What does `text[0:-1]` do?
5. Why might you use f-strings instead of concatenation with +?

---

## Bonus Challenges

- Create a Mad Libs game (ask for words, substitute into a story)
- Create a simple password strength checker
- Calculate compound interest (given principal, rate, years)
