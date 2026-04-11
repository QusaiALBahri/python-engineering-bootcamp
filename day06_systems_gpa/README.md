# Day 6: Systems Engineering & GPA System

## Learning Outcomes

By the end of this day, you will understand:

| Topic | Skill | File |
|-------|-------|------|
| **Real-World Problem Solving** | Breaking down complex problems into modules | gpa_*.py |
| **Error Handling** | Try/except/finally, custom errors, validation | gpa_hardened_v2.py |
| **File Persistence** | JSON I/O, data serialization, safe writes | gpa_hardened_v2.py |
| **Debugging Strategy** | Finding bugs, root cause analysis, logging | TICKETS.md |
| **Code Quality Evolution** | Naive code → Professional code | gpa_buggy_v1.py → gpa_hardened_v2.py |
| **Professional Practices** | Type hints, logging, docstrings, validation | gpa_hardened_v2.py |

---

## Overview

This lesson teaches you how to write **production-ready code** by:

1. **Seeing naive code** (`gpa_buggy_v1.py`) - Shows common mistakes
2. **Finding bugs** - Use TICKETS.md to identify 5 real bugs
3. **Fixing bugs** - Apply engineering practices
4. **Studying hardened code** (`gpa_hardened_v2.py`) - Learn professional patterns

---

## Key Concepts

### ✅ Lesson Structure

```
day06_systems_gpa/
├── gpa_buggy_v1.py        # Naive implementation with 5 intentional bugs
├── gpa_hardened_v2.py     # Professional implementation (the goal)
├── TICKETS.md             # Bug descriptions & fixing guide
└── README.md              # This file
```

### ✅ The GPA System

**What it does:**
- Store student names and grades
- Calculate GPA on 0-4 scale
- Save/load from JSON file
- Generate reports

**Learning approach:**
- Version 1 (buggy): Shows how NOT to do it
- Version 2 (hardened): Shows how professionals do it

---

## Key Concepts at a Glance

### 1. Input Validation (Bug #704)

❌ **WRONG** - Accept anything:
```python
def add_student(self, name, grades):
    self.students[name] = grades  # What if grades is -50? Or a string?
```

✅ **RIGHT** - Validate everything:
```python
def add_student(self, name, grades):
    if not name or not isinstance(name, str):
        logging.error("Invalid name")
        return False
    
    for grade in grades:
        if grade < 0 or grade > 100:
            logging.error(f"Grade {grade} out of range")
            return False
    
    self.students.append({"name": name, "grades": grades})
    return True
```

### 2. Correct Math (Bug #701)

❌ **WRONG** - Wrong scale:
```python
gpa = sum(grades) / len(grades)  # 85, 90, 92 → GPA of ~89 ❌
```

✅ **RIGHT** - Convert to 0-4:
```python
gpa_points = [grade * 4.0 / 100 for grade in grades]  # Convert to 0-4 scale
gpa = sum(gpa_points) / len(gpa_points)  # 85, 90, 92 → GPA of 3.53 ✅
```

### 3. File Persistence (Bug #702)

❌ **WRONG** - Just prints:
```python
def save_to_file(self, filename):
    print(f"Saving to {filename}")  # Stops here - never actually saves!
```

✅ **RIGHT** - Actually writes JSON:
```python
def save_to_file(self):
    try:
        with open(self.grade_file, 'w') as f:
            json.dump(self.students, f, indent=2)
        logging.info(f"Saved {len(self.students)} students")
    except IOError as e:
        logging.error(f"Failed to save: {e}")
        return False
    return True
```

### 4. Data Structure (Bug #703)

❌ **WRONG** - Dictionary, hard to extend:
```python
self.students = {}  # {"Alice": [85, 90]}
```

✅ **RIGHT** - List of dictionaries, easy to extend:
```python
self.students = []  # [{"name": "Alice", "grades": [85, 90], "gpa": 3.5}]
```

### 5. Clear Error Messages (Bug #705)

❌ **WRONG** - Vague:
```python
print("File not found")
```

✅ **RIGHT** - Specific and logged:
```python
logging.error("Failed to load grades.json: File does not exist")
logging.debug(f"Expected file at: {os.path.abspath(self.grade_file)}")
```

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| ❌ No input validation | Crashes with invalid data | Use `if` checks + type hints |
| ❌ No file error handling | Crashes on missing file | Use `try/except` + `json.JSONDecodeError` |
| ❌ Wrong data scale | Math is wrong (85 ≠ GPA 3.5) | Know your units: 0-100 vs 0-4 |
| ❌ No logging | Can't debug production issues | Use `logging.info/error/debug` |
| ❌ String keys only | Hard to add more data | Use list of dicts: `[{"name": "...", "grades": [...]}]` |

---

## Practice Flow

### Step 1: Study Buggy Version
```bash
# Open and read gpa_buggy_v1.py
# Notice: It looks simple but has problems
# Find: Can you spot the 5 bugs?
```

### Step 2: Read Bug Descriptions
```bash
# Open TICKETS.md
# For each bug #701-705:
#   - Understand the problem
#   - See the fix
#   - Learn the principle
```

### Step 3: Fix the Bugs
```bash
# Copy gpa_buggy_v1.py to gpa_fixed.py
# Apply each fix from TICKETS.md
# Test after each fix
```

### Step 4: Study Hardened Version
```bash
# Compare your gpa_fixed.py with gpa_hardened_v2.py
# Notice: It has MORE than just bug fixes
# Learn: Type hints, docstrings, constants, class design
```

### Step 5: Solve Exercises
```bash
# See EXERCISES.md for practice challenges
```

---

## Self-Assessment Checklist

Check off each item after completing it:

- [ ] Ran `gpa_buggy_v1.py` and saw errors
- [ ] Found Bug #701 (wrong GPA formula)
- [ ] Found Bug #702 (missing file I/O)
- [ ] Found Bug #703 (wrong data structure)
- [ ] Found Bug #704 (no validation)
- [ ] Found Bug #705 (poor error messages)
- [ ] Fixed all 5 bugs in your own version
- [ ] Your fixed version matches hardened_v2 behavior
- [ ] Understand why each bug matters
- [ ] Could explain to a colleague: "Never trust user input"
- [ ] Could explain to a colleague: "Test with bad data"

---

## Key Takeaways

1. **Real code has bugs** - Expect them, don't blame yourself
2. **Validation is critical** - Never assume input is valid
3. **Test with bad data** - Empty strings, negative numbers, wrong types
4. **Use logging** - Helps you debug in the field
5. **Evolution matters** - Buggy → Fixed → Hardened is normal
6. **Type hints help** - `grades: List[float]` prevents mistakes
7. **JSON is simple** - `json.dump()` and `json.load()` just work
8. **Compare implementations** - Learn from professional code

---

## Next Steps

After this day:
- [ ] Commit your fixed code to git
- [ ] Push to GitHub
- [ ] Read gpa_hardened_v2.py and learn from it
- [ ] Repeat pattern on Day 8 (Agile sprint with more bugs)

---

## Understanding the Pattern: Naive → Professional

This day shows you a **critical pattern in real-world engineering**:

### The Reality
- Junior developers write **buggy_v1.py** (missing validation, no error handling)
- Code works 95% of the time in testing
- Production fails when given unexpected input

### The Professional Path
- Write the naive version first (get it working)
- Find bugs through testing
- Add validation and error handling
- Add logging and type hints
- Test with bad data
- Result: hardened_v2.py (production-ready)

### Why It Matters
- Fortune 500 companies run on version 2.x code
- Version 1 code costs $$ in fixes and debugging
- Your job: Always be moving toward version 2

---

## Resources

- TICKETS.md - Detailed bug descriptions and fixes
- gpa_buggy_v1.py - See the bugs in action
- gpa_hardened_v2.py - Learn from production code
- EXERCISES.md - Practice fixing bugs
- SOLUTIONS.md - Solutions after you try
