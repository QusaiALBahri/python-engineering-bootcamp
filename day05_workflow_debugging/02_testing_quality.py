"""
Day 5, Lesson 2: Testing & Code Quality
Covers:
  - Unit testing with pytest/unittest
  - Assertions
  - Test structure and organization
  - Code refactoring
  - Type hints
  - Test-driven development
  - Code coverage
"""

import unittest
from typing import List, Dict, Optional

# ============================================
# 1. Basic Assertions
# ============================================

print("=" * 50)
print("Assertions: Quick Tests")
print("=" * 50)

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

# Tests using assertions
assert add(2, 3) == 5, "add(2, 3) should equal 5"
assert add(-1, 1) == 0, "add(-1, 1) should equal 0"
assert add(0, 0) == 0, "add(0, 0) should equal 0"

print("✓ All assertions passed!")

# ============================================
# 2. Testing Functions
# ============================================

print("\n" + "=" * 50)
print("Functions to Test")
print("=" * 50)

def calculate_grade(score: float) -> str:
    """Convert score to letter grade.
    
    Args:
        score: Score between 0-100
    
    Returns:
        Letter grade (A, B, C, D, F)
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def is_valid_email(email: str) -> bool:
    """Check if email format is valid.
    
    Args:
        email: Email address to validate
    
    Returns:
        True if valid, False otherwise
    """
    return "@" in email and "." in email

def reverse_string(text: str) -> str:
    """Reverse a string.
    
    Args:
        text: String to reverse
    
    Returns:
        Reversed string
    """
    return text[::-1]

# ============================================
# 3. Using unittest Framework
# ============================================

print("\n" + "=" * 50)
print("Unit Testing with unittest")
print("=" * 50)

class TestGradeCalculator(unittest.TestCase):
    """Test suite for grade calculator."""
    
    def test_excellent_score(self):
        """Test grade A (90+)."""
        self.assertEqual(calculate_grade(95), "A")
        self.assertEqual(calculate_grade(90), "A")
    
    def test_good_score(self):
        """Test grade B (80-89)."""
        self.assertEqual(calculate_grade(85), "B")
        self.assertEqual(calculate_grade(80), "B")
    
    def test_failing_score(self):
        """Test grade F (<60)."""
        self.assertEqual(calculate_grade(50), "F")
        self.assertEqual(calculate_grade(0), "F")
    
    def test_edge_case_passing(self):
        """Test edge cases."""
        self.assertEqual(calculate_grade(100), "A")
        self.assertEqual(calculate_grade(60), "D")

class TestEmailValidator(unittest.TestCase):
    """Test suite for email validation."""
    
    def test_valid_emails(self):
        """Test valid email addresses."""
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("test@gmail.co.uk"))
    
    def test_invalid_emails(self):
        """Test invalid email addresses."""
        self.assertFalse(is_valid_email("invalid@"))
        self.assertFalse(is_valid_email("no-at-sign.com"))
        self.assertFalse(is_valid_email("user"))

class TestStringReversal(unittest.TestCase):
    """Test suite for string reversal."""
    
    def test_simple_string(self):
        """Test reversing simple string."""
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_palindrome(self):
        """Test reversing palindrome."""
        self.assertEqual(reverse_string("racecar"), "racecar")
    
    def test_empty_string(self):
        """Test reversing empty string."""
        self.assertEqual(reverse_string(""), "")
    
    def test_single_character(self):
        """Test reversing single character."""
        self.assertEqual(reverse_string("a"), "a")

# Run tests (commented out to avoid output)
# if __name__ == '__main__':
#     unittest.main()

print("""
To run unittest tests:
  python -m unittest test_module.py

To run specific test:
  python -m unittest test_module.TestClass.test_method
""")

# ============================================
# 4. Type Hints for Quality
# ============================================

print("\n" + "=" * 50)
print("Type Hints: Self-Documenting Code")
print("=" * 50)

# Good: Type hints make code clear
def find_average(numbers: List[float]) -> Optional[float]:
    """Calculate average of numbers.
    
    Args:
        numbers: List of numbers
    
    Returns:
        Average value, or None if list is empty
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# Function with complex types
def process_user_data(
    user_dict: Dict[str, str],
    include_age: bool = False
) -> Dict[str, any]:
    """Process user dictionary.
    
    Args:
        user_dict: User data
        include_age: Whether to include age info
    
    Returns:
        Processed user data
    """
    result = {"name": user_dict.get("name", "Unknown")}
    if include_age:
        result["age"] = user_dict.get("age", "N/A")
    return result

# ============================================
# 5. Test-Driven Development (TDD)
# ============================================

print("\n" + "=" * 50)
print("Test-Driven Development (TDD)")
print("=" * 50)

print("""
TDD Process:
  1. Write test for desired functionality
  2. Run test (it will fail - RED)
  3. Write code to pass test (GREEN)
  4. Refactor code if needed (REFACTOR)
  5. Repeat

Example: Testing a Calculator class

Step 1: Write test
class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)

Step 2: Test fails (RED)
Step 3: Write implementation (GREEN)

class Calculator:
    def add(self, a, b):
        return a + b

Step 4: Refactor if needed
Step 5: Repeat for more features
""")

# ============================================
# 6. Code Refactoring
# ============================================

print("\n" + "=" * 50)
print("Code Refactoring: Improve Without Changing Behavior")
print("=" * 50)

# BEFORE: Hard to understand
# def p(x):
#     return x*0.9 if x>100 else x

# AFTER: Clear and readable
def apply_discount(price: float, discount_threshold: float = 100) -> float:
    """Apply 10% discount if price exceeds threshold.
    
    Args:
        price: Item price
        discount_threshold: Minimum price for discount
    
    Returns:
        Final price after discount if applicable
    """
    discount_rate = 0.1
    if price > discount_threshold:
        return price * (1 - discount_rate)
    return price

print(f"Price before refactoring: Same function, but now readable!")

# ============================================
# 7. Common Testing Patterns
# ============================================

print("\n" + "=" * 50)
print("Common Testing Patterns")
print("=" * 50)

class TestingPatterns(unittest.TestCase):
    """Common testing patterns."""
    
    def setUp(self):
        """Run before each test."""
        self.test_list = [1, 2, 3, 4, 5]
    
    def tearDown(self):
        """Run after each test."""
        # Cleanup code here
        pass
    
    def test_exact_value(self):
        """Assert exact value."""
        self.assertEqual(2 + 2, 4)
    
    def test_boolean(self):
        """Assert boolean."""
        self.assertTrue(True)
        self.assertFalse(False)
    
    def test_membership(self):
        """Assert item in collection."""
        self.assertIn(2, self.test_list)
        self.assertNotIn(10, self.test_list)
    
    def test_exception(self):
        """Assert exception is raised."""
        with self.assertRaises(ZeroDivisionError):
            1 / 0
    
    def test_list_length(self):
        """Assert collection length."""
        self.assertEqual(len(self.test_list), 5)

print("""
Common Assertions:
  assertEqual(a, b):         a == b
  assertNotEqual(a, b):      a != b
  assertTrue(x):             x is True
  assertFalse(x):            x is False
  assertIn(a, b):            a in b
  assertNotIn(a, b):         a not in b
  assertIsNone(x):           x is None
  assertIsNotNone(x):        x is not None
  assertRaises(exc, func):   func raises exc
  assertGreater(a, b):       a > b
  assertLess(a, b):          a < b
""")

# ============================================
# 8. Best Practices
# ============================================

print("\n" + "=" * 50)
print("Testing Best Practices")
print("=" * 50)

print("""
✓ DO:
  - Write tests BEFORE code (TDD)
  - Test edge cases and error conditions
  - Use descriptive test names
  - Test one thing per test
  - Use setUp/tearDown for common setup
  - Aim for 80%+ code coverage
  - Test boundary conditions
  - Use type hints

✗ DON'T:
  - Skip testing "simple" code
  - Write tests that are too complex
  - Test implementation details
  - Ignore test failures
  - Use vague test names
  - Test multiple things at once
  - Write tests you don't understand

Code Coverage Tools:
  pip install coverage
  coverage run -m unittest discover
  coverage report
  coverage html
""")

# ============================================
# 9. Running Tests
# ============================================

print("\n" + "=" * 50)
print("Running Tests")
print("=" * 50)

print("""
Different ways to run tests:

1. Using unittest:
   python -m unittest test_module.py
   python -m unittest test_module.TestClass
   python -m unittest discover

2. Using pytest:
   pip install pytest
   pytest test_module.py
   pytest test_module.py::TestClass::test_method

3. Using unittest with verbose:
   python -m unittest test_module.py -v

4. Using pytest with coverage:
   pip install pytest-cov
   pytest --cov test_module.py
""")

# ============================================
# 10. Summary
# ============================================

print("\n" + "=" * 50)
print("Testing Summary")
print("=" * 50)

print("""
Why Write Tests?
  ✓ Catch bugs early
  ✓ Prevent regressions
  ✓ Make refactoring safe
  ✓ Document expected behavior
  ✓ Improve code quality
  ✓ Enable confident deployment

Test Types:
  - Unit Tests: Individual functions
  - Integration Tests: Multiple components
  - Acceptance Tests: Full features
  - Performance Tests: Speed/efficiency

Coverage Levels:
  - Line coverage: % of lines executed
  - Branch coverage: % of conditionals tested
  - Function coverage: % of functions tested
  - Statement coverage: % of statements executed

Aim for 80%+ code coverage in production code!
""")

print("\n✅ Lesson 2 Complete!")
