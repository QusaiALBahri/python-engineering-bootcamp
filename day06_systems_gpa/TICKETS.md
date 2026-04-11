# Day 6 - Tickets #701-705: GPA System Bugs

## Overview
Your job is to take `gpa_buggy_v1.py` and fix all bugs to match the professional version in `gpa_hardened_v2.py`.

Follow the **Create → Break → Fix → Harden** workflow:
1. Run buggy code and see it fail
2. Find each bug
3. Fix and test
4. Compare with v2-hardened

---

## Ticket #701: Logic Error in GPA Calculation

**Severity:** HIGH  
**Impact:** Grades are calculated incorrectly

### Description
The `calculate_gpa()` method uses the wrong formula.

### Current Code (WRONG):
```python
gpa = sum(grades) / len(grades)  # Just averages 0-100 grades
```

### Problem
- Input grades are 0-100 scale (e.g., 85, 90, 92)
- Output should be 0-4 scale (e.g., 3.4)
- Current code returns wrong scale: 89/3 = 29.67 ❌

### Fix
```python
gpa_points = [grade * 4.0 / 100 for grade in grades]
gpa = sum(gpa_points) / len(gpa_points)
```

### Test
- Input: [85, 90, 92]
- Expected GPA: 3.53
- Current (wrong): 89.00

---

## Ticket #702: Missing File Handling

**Severity:** CRITICAL  
**Impact:** Grades are never actually saved or loaded

### Description
The `save_to_file()` and `load_from_file()` methods are incomplete.

### Current Code (BUG):
```python
def save_to_file(self, filename="grades.json"):
    print(f"Saving to {filename}")
    # STOPS HERE - never actually saves!

def load_from_file(self, filename="grades.json"):
    if not os.path.exists(filename):
        print(f"File {filename} not found")
        return
    # STOPS HERE - never actually loads!
```

### Fix
Use `json.dump()` and `json.load()`:
```python
def save_to_file(self):
    with open(self.grade_file, 'w') as f:
        json.dump(self.students, f, indent=2)
    logging.info(f"Saved to {self.grade_file}")

def load_from_file(self):
    if not os.path.exists(self.grade_file):
        return False
    with open(self.grade_file, 'r') as f:
        self.students = json.load(f)
    return True
```

---

## Ticket #703: Wrong Data Structure

**Severity:** MEDIUM  
**Impact:** Code doesn't scale; hard to manage multiple students

### Description
Students are stored in a dictionary, but should be a list.

### Current Code (WRONG):
```python
self.students = {}  # Dictionary
self.students[name] = grades  # Access by name only
```

### Problem
- Can'teasily iterate all students
- Hard to add more fields (GPA, email, etc.)
- Not scalable

### Fix
```python
self.students = []  # List of dictionaries
self.students.append({"name": name, "grades": grades})

# Now iterate easily
for student in self.students:
    print(student["name"], student["grades"])
```

---

## Ticket #704: No Input Validation

**Severity:** MEDIUM  
**Impact:** Invalid data crashes program

### Description
`add_student()` accepts invalid input without checking.

### Current Code (PROBLEM):
```python
def add_student(self, name, grades):
    self.students[name] = grades  # No checks!
```

### What Can Go Wrong
```python
gpa_sys.add_student("", [])  # Empty - crashes
gpa_sys.add_student(None, [85, 90])  # None - crashes
gpa_sys.add_student("Bob", [200, -5])  # Invalid grades
gpa_sys.add_student("Bob", "notalist")  # Wrong type
```

### Fix
```python
def add_student(self, name, grades):
    if not name or not isinstance(name, str):
        return False  # Reject invalid name
    
    if not isinstance(grades, list):
        return False  # Must be list
    
    for grade in grades:
        if grade < 0 or grade > 100:
            return False  # Grades out of range
    
    self.students.append({"name": name, "grades": grades})
    return True
```

---

## Ticket #705: Poor Error Messages

**Severity:** LOW  
**Impact:** Hard to debug when things fail

### Description
Error messages are vague or missing.

### Current Code (UNHELPFUL):
```python
if not os.path.exists(filename):
    print(f"File {filename} not found")  # Just mentions file
    return
```

### Problem
- Doesn't say WHY it matters
- Can't debug why system isn't loading
- No logging for audit trail

### Fix
```python
import logging

if not os.path.exists(filename):
    logging.info(f"File {filename} not found - starting fresh")
    return False

try:
    with open(filename, 'r') as f:
        self.students = json.load(f)
    logging.info(f"Loaded {len(self.students)} students")
except json.JSONDecodeError as e:
    logging.error(f"Invalid JSON: {e}")  # Clear error
    return False
```

---

## Your Task

1. **Study** `gpa_buggy_v1.py` and find each bug
2. **Fix** each bug according to the descriptions above
3. **Test** with the provided test code
4. **Compare** with `gpa_hardened_v2.py` to verify
5. **Document** what you learned

---

## Testing Your Fixes

```bash
# Run buggy version - see it fail
python gpa_buggy_v1.py

# After fixing, run your fixed version
python gpa_fixed.py  # should now work!

# Compare with hardened version
python gpa_hardened_v2.py
```

---

## Acceptance Criteria (How to know you fixed it)

- [ ] GPA calculation uses correct 0-4 scale (not 0-100)
- [ ] Grades save to JSON file correctly
- [ ] Grades load from JSON file correctly
- [ ] Invalid input is rejected with clear errors
- [ ] All errors logged appropriately
- [ ] Code matches hardened v2 functionality

---

## Bonus Challenge

Add these features to make it even more professional:
- [ ] Calculate letter grades (A, B, C, D, F)
- [ ] Track GPA history over multiple semesters
- [ ] Add student ID numbers
- [ ] Export reports as CSV
- [ ] Command-line interface (CLI) for adding students
