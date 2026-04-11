# Day 2 Exercises: Conditional Logic & Functions

## Exercise 1: Student Grade System
Write a program with a function that:
- Takes a score (0-100) as parameter
- Returns grade: A (90+), B (80+), C (70+), D (60+), F (below 60)
- In main code, ask user for 3 scores and display all grades

**Example:**
```
Score 1: 85
Score 2: 92
Score 3: 78
Grade 1: B
Grade 2: A
Grade 3: C
```

---

## Exercise 2: Login System
Create a login function that:
- Takes username and password as parameters
- Checks if username == "admin" AND password == "1234"
- Returns True if correct, False otherwise
- In main code, ask user for credentials 3 times
- If any attempt is correct, print "Login successful"
- If all 3 fail, print "Too many attempts"

---

## Exercise 3: Discount Calculator
Write a function that:
- Takes purchase amount and customer type ("standard", "member", "vip")
- standard: no discount
- member: 10% discount
- vip: 20% discount
- Returns final price after discount
- Test with 3 different purchase amounts and customer types

---

## Exercise 4: Number Validator
Create functions to validate user input:
- `is_positive(num)`: Returns True if num > 0
- `is_even(num)`: Returns True if num is divisible by 2
- `is_in_range(num, min, max)`: Returns True if min <= num <= max

Test each function with different values

---

## Exercise 5: Temperature Alert
Write a function that:
- Takes temperature in Celsius
- Returns "Freezing" if < 0
- Returns "Cold" if 0-10
- Returns "Cool" if 10-20
- Returns "Warm" if 20-30
- Returns "Hot" if 30+
- Ask user for 5 temperatures and display alerts

---

## Challenge: Password Strength Checker
Create a function that evaluates password strength and returns a message:
- "Too short" if < 8 characters
- "Weak" if only lowercase
- "Fair" if has lowercase + uppercase
- "Strong" if has lowercase + uppercase + number
- "Very Strong" if has lowercase + uppercase + number + special character (!@#$%^&*)

Test with different passwords

---

## Solutions Checklist
- [ ] All exercises completed
- [ ] Code runs without errors
- [ ] Functions have meaningful names
- [ ] Functions have docstrings
- [ ] Used if/elif/else correctly
- [ ] Used logical operators (and, or) where needed

