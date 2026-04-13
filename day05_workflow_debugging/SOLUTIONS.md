# Day 5 Solutions: Debugging, Testing & Professional Practices

## Exercise 1: PEP 8 Code Formatting

**Problem:** Rewrite poorly formatted code to follow PEP 8.

**Solution:**

```python
"""Module containing calculator and user management utilities."""

SECURITY_API_KEY = "secret123"


def calculate_compound_result(x: float, y: float, z: float) -> float:
    """Calculate compound result based on conditions.
    
    Args:
        x: First number
        y: Second number
        z: Multiplier
    
    Returns:
        (x + y) * z if both x and y are positive, 0 otherwise
    """
    if x > 0 and y > 0:
        return (x + y) * z
    return 0


class User:
    """Represent a user with name and age."""
    
    def __init__(self, name: str, age: int):
        """Initialize user.
        
        Args:
            name: User's full name
            age: User's age in years
        """
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        """Return string representation."""
        return f"User({self.name}, {self.age})"


# List of items
numbers = [1, 2, 3, 4, 5]
```

**Key Changes:**
- ✓ Function names: snake_case
- ✓ Class names: PascalCase
- ✓ Constants: ALL_CAPS
- ✓ Added proper spacing
- ✓ Added docstrings
- ✓ Added type hints

---

## Exercise 2: Add Type Hints

**Problem:** Add type hints to functions.

**Solution:**

```python
from typing import List, Dict, Optional

def get_average(numbers: List[float]) -> float:
    """Calculate average of numbers.
    
    Args:
        numbers: List of numerical values
    
    Returns:
        Average value
    """
    return sum(numbers) / len(numbers)


def process_user(name: str, age: int) -> Dict[str, any]:
    """Create user dictionary.
    
    Args:
        name: User's name
        age: User's age
    
    Returns:
        Dictionary with user data
    """
    return {"name": name, "age": age}


def find_item(items: List[str], target: str) -> Optional[str]:
    """Find item in list.
    
    Args:
        items: List of items
        target: Item to find
    
    Returns:
        Found item or None if not found
    """
    for item in items:
        if item == target:
            return item
    return None

# Test
print(get_average([10, 20, 30]))
print(process_user("Ali", 25))
print(find_item(["apple", "banana", "orange"], "banana"))
```

**Output:**
```
20.0
{'name': 'Ali', 'age': 25}
banana
```

---

## Exercise 3: Write Unit Tests

**Problem:** Write unit tests for a Calculator class.

**Solution:**

```python
import unittest


class Calculator:
    """Simple calculator for basic operations."""
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Divide a by b.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class TestCalculator(unittest.TestCase):
    """Test suite for Calculator class."""
    
    def setUp(self):
        """Create calculator instance for each test."""
        self.calc = Calculator()
    
    def test_add_positive(self):
        """Test adding positive numbers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(10, 20), 30)
    
    def test_add_negative(self):
        """Test adding with negative numbers."""
        self.assertEqual(self.calc.add(-5, 3), -2)
        self.assertEqual(self.calc.add(-10, -20), -30)
    
    def test_subtract_positive(self):
        """Test subtracting positive numbers."""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(5, 10), -5)
    
    def test_subtract_negative(self):
        """Test subtracting negative numbers."""
        self.assertEqual(self.calc.subtract(10, -5), 15)
    
    def test_multiply_positive(self):
        """Test multiplying positive numbers."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(10, 10), 100)
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
    
    def test_divide_positive(self):
        """Test dividing positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(15, 3), 5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def test_divide_negative(self):
        """Test dividing with negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
    
    def test_divide_fraction(self):
        """Test division resulting in fraction."""
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.333333, places=4)


if __name__ == '__main__':
    unittest.main()
```

**Run tests:**
```bash
python -m unittest solution3.py -v
```

---

## Exercise 4: Debug the Code

**Problem:** Find and fix bugs in a function.

**Solution:**

```python
def find_duplicates(numbers: list) -> list:
    """Find duplicate values in a list.
    
    Args:
        numbers: List of numbers
    
    Returns:
        List of duplicate values
    """
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # BUG FIX 1: Changed = to ==
            if numbers[i] == numbers[j]:
                # BUG FIX 2: Check if already added
                if numbers[i] not in duplicates:
                    duplicates.append(numbers[i])
    return duplicates


# Test
result = find_duplicates([1, 2, 2, 3, 3, 3, 4])
print(result)  # Output: [2, 3]
```

**Bugs Found & Fixed:**
1. ✓ `=` instead of `==` (assignment vs comparison)
2. ✓ Duplicate duplicates (same value added multiple times)

**Better Solution (More Efficient):**

```python
def find_duplicates(numbers: list) -> list:
    """Find duplicate values more efficiently."""
    seen = set()
    duplicates = set()
    
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return sorted(list(duplicates))

result = find_duplicates([1, 2, 2, 3, 3, 3, 4])
print(result)  # Output: [2, 3]
```

---

## Exercise 5: Add Logging

**Problem:** Replace print() with logging.

**Solution:**

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def authenticate(username: str, password: str) -> bool:
    """Authenticate user credentials.
    
    Args:
        username: Username
        password: Password
    
    Returns:
        True if credentials valid, False otherwise
    """
    logger.debug(f"Authenticating user: {username}")
    
    if username == "admin" and password == "pass123":
        logger.info(f"User {username} authenticated successfully")
        return True
    
    logger.warning(f"Failed authentication attempt for user: {username}")
    return False


def login_user(attempts_max: int = 3) -> bool:
    """Login user with retry logic.
    
    Args:
        attempts_max: Maximum login attempts
    
    Returns:
        True if login successful, False otherwise
    """
    logger.info("Starting login process")
    
    for attempt in range(1, attempts_max + 1):
        logger.debug(f"Login attempt {attempt}/{attempts_max}")
        
        username = input("Username: ")
        password = input("Password: ")
        
        if authenticate(username, password):
            logger.info("Login successful - user granted access")
            return True
        else:
            remaining = attempts_max - attempt
            if remaining > 0:
                logger.warning(f"Login failed. {remaining} attempts remaining")
            else:
                logger.error("Login failed - maximum attempts exceeded")
    
    logger.error("User locked out after multiple failed attempts")
    return False


# Test (commented out to avoid input prompts)
# if __name__ == "__main__":
#     login_user()
```

**Output:**
```
2024-01-15 10:30:45,123 - INFO - Starting login process
2024-01-15 10:30:45,124 - DEBUG - Login attempt 1/3
2024-01-15 10:30:50,456 - WARNING - Failed authentication
```

---

## Challenge 1: Complete Test Suite

**Problem:** Write comprehensive tests for BankAccount.

**Solution:**

```python
import unittest
from decimal import Decimal


class BankAccount:
    """Bank account with deposit/withdraw functionality."""
    
    def __init__(self, holder: str, balance: float = 0):
        """Initialize account.
        
        Args:
            holder: Account holder name
            balance: Initial balance (default 0)
        
        Raises:
            ValueError: If initial balance is negative
        """
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.holder = holder
        self.balance = Decimal(str(balance))
    
    def deposit(self, amount: float) -> None:
        """Deposit money to account.
        
        Args:
            amount: Amount to deposit
        
        Raises:
            ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += Decimal(str(amount))
    
    def withdraw(self, amount: float) -> None:
        """Withdraw money from account.
        
        Args:
            amount: Amount to withdraw
        
        Raises:
            ValueError: If amount exceeds balance or is negative
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= Decimal(str(amount))
    
    def get_balance(self) -> float:
        """Get current balance."""
        return float(self.balance)


class TestBankAccount(unittest.TestCase):
    """Test suite for BankAccount class."""
    
    def setUp(self):
        """Create account for each test."""
        self.account = BankAccount("Ali Ahmed", 1000)
    
    # Initialization tests
    def test_account_creation(self):
        """Test account creation."""
        self.assertEqual(self.account.holder, "Ali Ahmed")
        self.assertEqual(self.account.get_balance(), 1000)
    
    def test_account_with_zero_balance(self):
        """Test creating account with zero balance."""
        account = BankAccount("Sara", 0)
        self.assertEqual(account.get_balance(), 0)
    
    def test_invalid_initial_balance(self):
        """Test that negative initial balance raises error."""
        with self.assertRaises(ValueError):
            BankAccount("Test", -100)
    
    # Deposit tests
    def test_deposit_positive(self):
        """Test depositing positive amount."""
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)
    
    def test_deposit_zero(self):
        """Test depositing zero."""
        self.account.deposit(0)
        self.assertEqual(self.account.get_balance(), 1000)
    
    def test_deposit_small_amount(self):
        """Test depositing small decimal amount."""
        self.account.deposit(0.50)
        self.assertAlmostEqual(self.account.get_balance(), 1000.50, places=2)
    
    def test_deposit_negative(self):
        """Test depositing negative amount raises error."""
        with self.assertRaises(ValueError):
            self.account.deposit(-100)
    
    def test_multiple_deposits(self):
        """Test multiple deposits."""
        self.account.deposit(100)
        self.account.deposit(200)
        self.account.deposit(300)
        self.assertEqual(self.account.get_balance(), 1600)
    
    # Withdrawal tests
    def test_withdraw_positive(self):
        """Test withdrawing positive amount."""
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)
    
    def test_withdraw_all(self):
        """Test withdrawing entire balance."""
        self.account.withdraw(1000)
        self.assertEqual(self.account.get_balance(), 0)
    
    def test_withdraw_too_much(self):
        """Test withdrawing more than balance raises error."""
        with self.assertRaises(ValueError):
            self.account.withdraw(1500)
    
    def test_withdraw_negative(self):
        """Test withdrawing negative amount raises error."""
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)
    
    def test_withdraw_from_empty_account(self):
        """Test withdrawing from account with zero balance."""
        account = BankAccount("Empty", 0)
        with self.assertRaises(ValueError):
            account.withdraw(1)
    
    # Combined operation tests
    def test_deposit_then_withdraw(self):
        """Test deposit followed by withdrawal."""
        self.account.deposit(500)
        self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 1300)
    
    def test_multiple_operations(self):
        """Test multiple mixed operations."""
        self.account.deposit(200)
        self.account.withdraw(100)
        self.account.deposit(50)
        self.account.withdraw(25)
        self.assertEqual(self.account.get_balance(), 1125)


if __name__ == '__main__':
    unittest.main()
```

---

## Challenge 2: Code Quality Report

**Problem:** Write a script to check code quality.

**Solution:**

```python
"""Code quality checker."""

import ast
import re
from pathlib import Path
from typing import List, Dict


class CodeQualityChecker:
    """Check code quality metrics."""
    
    def __init__(self, filepath: str):
        """Initialize checker.
        
        Args:
            filepath: Path to Python file to analyze
        """
        self.filepath = Path(filepath)
        with open(self.filepath) as f:
            self.content = f.read()
        self.tree = ast.parse(self.content)
    
    def check_function_length(self, max_lines: int = 50) -> Dict:
        """Check function line counts.
        
        Args:
            max_lines: Maximum allowed lines per function
        
        Returns:
            Dictionary of functions and their line counts
        """
        results = {}
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                length = node.end_lineno - node.lineno + 1
                results[node.name] = {
                    "lines": length,
                    "exceeds": length > max_lines
                }
        return results
    
    def check_naming_conventions(self) -> Dict:
        """Check if names follow PEP 8.
        
        Returns:
            Dictionary of naming violations
        """
        violations = {"snake_case_issues": [], "PascalCase_issues": []}
        
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                if not re.match(r'^[a-z_][a-z0-9_]*$', node.name):
                    violations["snake_case_issues"].append(node.name)
            
            elif isinstance(node, ast.ClassDef):
                if not re.match(r'^[A-Z][a-zA-Z0-9]*$', node.name):
                    violations["PascalCase_issues"].append(node.name)
        
        return violations
    
    def check_docstrings(self) -> Dict:
        """Check for docstrings.
        
        Returns:
            Functions/classes with missing docstrings
        """
        missing = {"functions": [], "classes": []}
        
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                if not ast.get_docstring(node):
                    missing["functions"].append(node.name)
            
            elif isinstance(node, ast.ClassDef):
                if not ast.get_docstring(node):
                    missing["classes"].append(node.name)
        
        return missing
    
    def get_metrics(self) -> Dict:
        """Get overall code metrics.
        
        Returns:
            Dictionary of metrics
        """
        lines = self.content.split('\n')
        code_lines = [l for l in lines if l.strip() and not l.strip().startswith('#')]
        
        return {
            "total_lines": len(lines),
            "code_lines": len(code_lines),
            "comment_lines": len([l for l in lines if l.strip().startswith('#')]),
            "functions": len([n for n in ast.walk(self.tree) if isinstance(n, ast.FunctionDef)]),
            "classes": len([n for n in ast.walk(self.tree) if isinstance(n, ast.ClassDef)])
        }
    
    def generate_report(self) -> str:
        """Generate quality report.
        
        Returns:
            Formatted report string
        """
        report = f"\n{'='*50}\nCode Quality Report: {self.filepath}\n{'='*50}\n"
        
        # Metrics
        metrics = self.get_metrics()
        report += "\nMetrics:\n"
        for key, value in metrics.items():
            report += f"  {key}: {value}\n"
        
        # Function length
        report += "\nFunction Length Check:\n"
        lengths = self.check_function_length()
        for func, data in lengths.items():
            status = "✓" if not data["exceeds"] else "✗"
            report += f"  {status} {func}: {data['lines']} lines\n"
        
        # Naming
        report += "\nNaming Convention Check:\n"
        naming = self.check_naming_conventions()
        if naming["snake_case_issues"]:
            report += f"  ✗ Non-snake_case functions: {naming['snake_case_issues']}\n"
        if naming["PascalCase_issues"]:
            report += f"  ✗ Non-PascalCase classes: {naming['PascalCase_issues']}\n"
        if not naming["snake_case_issues"] and not naming["PascalCase_issues"]:
            report += "  ✓ All names follow conventions\n"
        
        # Docstrings
        report += "\nDocstring Check:\n"
        missing = self.check_docstrings()
        if missing["functions"]:
            report += f"  ✗ Functions without docstrings: {missing['functions']}\n"
        if missing["classes"]:
            report += f"  ✗ Classes without docstrings: {missing['classes']}\n"
        if not missing["functions"] and not missing["classes"]:
            report += "  ✓ All functions/classes have docstrings\n"
        
        return report


# Example usage
if __name__ == "__main__":
    checker = CodeQualityChecker("script_to_check.py")
    print(checker.generate_report())
```

---

## Challenge 3: Refactoring Exercise

**Problem:** Refactor poorly written code.

**Solution:**

```python
from typing import List, Optional


def calculate_discount(price: float, discount_rate: float = 0.1) -> float:
    """Calculate discount amount for a price.
    
    Args:
        price: Original price
        discount_rate: Discount percentage (default 10%)
    
    Returns:
        Discount amount
    """
    return price * discount_rate


def apply_discount(price: float, discount_rate: float) -> float:
    """Apply discount to price.
    
    Args:
        price: Original price
        discount_rate: Discount percentage (0.0-1.0)
    
    Returns:
        Final price after discount
    
    Raises:
        ValueError: If price or rate is negative
    """
    if price < 0 or discount_rate < 0:
        raise ValueError("Price and discount rate cannot be negative")
    
    discount = calculate_discount(price, discount_rate)
    return price - discount


def calculate_average(numbers: List[float]) -> Optional[float]:
    """Calculate average of a list of numbers.
    
    Args:
        numbers: List of numerical values
    
    Returns:
        Average value, or None if list is empty
    
    Raises:
        TypeError: If any element is not numeric
    """
    if not numbers:
        return None
    
    try:
        return sum(numbers) / len(numbers)
    except TypeError as e:
        raise TypeError(f"All elements must be numeric: {e}")


def validate_email(email: str) -> bool:
    """Validate email address format.
    
    Args:
        email: Email address to validate
    
    Returns:
        True if valid email format, False otherwise
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


# Tests
if __name__ == "__main__":
    # Test discount
    assert apply_discount(100, 0.1) == 90
    print("✓ Discount calculations work")
    
    # Test average
    assert calculate_average([10, 20, 30]) == 20
    assert calculate_average([]) is None
    print("✓ Average calculations work")
    
    # Test email
    assert validate_email("user@example.com") is True
    assert validate_email("invalid-email") is False
    print("✓ Email validation works")
    
    print("\n✅ All refactored code tests passed!")
```

---

## Summary

Key learning from Day 5:

✓ **Code Quality:** PEP 8, type hints, documentation  
✓ **Testing:** Unit tests, test structure, coverage  
✓ **Debugging:** Logging, assertions, debugger  
✓ **Refactoring:** Improve without changing behavior  
✓ **Best Practices:** Professional Python development  

All solutions include:
- ✅ Complete working code
- ✅ Type hints (where applicable)
- ✅ Comprehensive docstrings
- ✅ Error handling
- ✅ Test coverage
- ✅ PEP 8 compliance
