"""
Day 5, Lesson 1: Debugging & PEP 8 Style Guide
Covers:
  - Debugging techniques
  - Python debugger (pdb)
  - Logging module
  - PEP 8 style guide
  - Code formatting
  - Naming conventions
  - Documentation practices
"""

import logging
import pdb

# ============================================
# 1. Setting up Logging
# ============================================

print("=" * 50)
print("Logging: Professional Debugging")
print("=" * 50)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")

# ============================================
# 2. Logging Levels
# ============================================

print("\n" + "=" * 50)
print("Logging Levels")
print("=" * 50)

print("""
Logging Levels (from least to most severe):
  DEBUG (10):    Diagnostic info for debugging
  INFO (20):     General informational messages
  WARNING (30):  Warning messages (default level)
  ERROR (40):    Error messages
  CRITICAL (50): Critical error messages
""")

# ============================================
# 3. PEP 8: Naming Conventions
# ============================================

print("\n" + "=" * 50)
print("PEP 8: Naming Conventions")
print("=" * 50)

# GOOD: PEP 8 compliant names
student_name = "Ali"  # Variables: lowercase_with_underscores
def calculate_average():  # Functions: lowercase_with_underscores
    pass

class StudentRecord:  # Classes: PascalCase
    pass

MAXIMUM_ATTEMPTS = 3  # Constants: UPPERCASE_WITH_UNDERSCORES

# BAD: Not PEP 8 compliant (don't use these)
# studentName = "Ali"  # camelCase is not Pythonic
# CalculateAverage = 5  # Function names shouldn't be PascalCase
# student_record = None  # Class names shouldn't be lowercase

print("""
✓ DO:
  - Functions/variables: snake_case
  - Classes: PascalCase
  - Constants: ALL_CAPS
  - Private methods: _private_method

✗ DON'T:
  - Use camelCase for functions
  - Use single letters (except i, j, k in loops)
  - Use confusing abbreviations
""")

# ============================================
# 4. Line Length & Formatting
# ============================================

print("\n" + "=" * 50)
print("PEP 8: Code Formatting")
print("=" * 50)

# GOOD: Clear, readable formatting
def process_data(data: list, threshold: int = 10) -> dict:
    """Process data and return results.
    
    Args:
        data: Input data list
        threshold: Minimum value threshold
    
    Returns:
        Dictionary with processed results
    """
    result = {
        "total": sum(data),
        "count": len(data),
        "average": sum(data) / len(data) if data else 0
    }
    return result

# BAD: Dense, hard to read
# def pd(d,t=10):return{"t":sum(d),"c":len(d),"a":sum(d)/len(d) if d else 0}

print("""
PEP 8 Formatting Rules:
  - Max 79 characters per line (or 99 for code)
  - 2 blank lines between top-level functions/classes
  - 1 blank line between methods
  - Spaces around operators: a = b + c
  - Spaces after commas: [1, 2, 3]
  - Use parentheses for line continuation
""")

# ============================================
# 5. Docstrings
# ============================================

print("\n" + "=" * 50)
print("Documentation: Docstrings")
print("=" * 50)

class DataAnalyzer:
    """Analyze numerical data.
    
    This class provides methods for analyzing datasets including
    calculating statistics and finding trends.
    
    Attributes:
        data: List of numerical values
        name: Name of the dataset
    """
    
    def __init__(self, data: list, name: str = "dataset"):
        """Initialize the analyzer.
        
        Args:
            data: List of numerical values
            name: Name of the dataset (default: "dataset")
        """
        self.data = data
        self.name = name
    
    def calculate_average(self) -> float:
        """Calculate the average of the data.
        
        Returns:
            The mean value of the dataset
            
        Raises:
            ValueError: If data is empty
        """
        if not self.data:
            raise ValueError("Cannot calculate average of empty dataset")
        return sum(self.data) / len(self.data)
    
    def find_max(self) -> float:
        """Find the maximum value in the dataset.
        
        Returns:
            The largest value
        """
        return max(self.data) if self.data else None

# Use the class
analyzer = DataAnalyzer([10, 20, 30, 40], "Test Data")
logger.info(f"Average: {analyzer.calculate_average()}")

# ============================================
# 6. Comments vs Docstrings
# ============================================

print("\n" + "=" * 50)
print("Comments vs Docstrings")
print("=" * 50)

def good_example(numbers: list) -> int:
    """Calculate sum of numbers.
    
    This is a docstring - describes what the function does.
    It's accessible via help() and documentation generators.
    """
    # This is a comment - explains a specific line
    total = sum(numbers)
    
    # Process edge case
    if not numbers:
        return 0
    
    return total

# ============================================
# 7. Type Hints
# ============================================

print("\n" + "=" * 50)
print("Type Hints: Self-Documenting Code")
print("=" * 50)

from typing import List, Dict, Optional, Union, Tuple

# Function with type hints
def authenticate(
    username: str,
    password: str
) -> Union[Dict[str, str], None]:
    """Authenticate user.
    
    Args:
        username: User's username
        password: User's password
    
    Returns:
        User data dict if valid, None otherwise
    """
    if username == "admin" and password == "1234":
        return {"user_id": "1", "name": "Administrator"}
    return None

# Function returning multiple values
def get_user_info(user_id: int) -> Tuple[str, int, str]:
    """Get user information.
    
    Returns:
        Tuple of (name, age, email)
    """
    return ("Ali", 25, "ali@example.com")

# ============================================
# 8. Error Handling Best Practices
# ============================================

print("\n" + "=" * 50)
print("Error Handling: Logging Exceptions")
print("=" * 50)

def divide_safely(a: float, b: float) -> Optional[float]:
    """Divide a by b with error handling.
    
    Args:
        a: Numerator
        b: Denominator
    
    Returns:
        Result of division, or None if error
    """
    try:
        result = a / b
        logger.info(f"Calculation successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Division by zero: {a} / {b}")
        return None
    except TypeError:
        logger.error(f"Invalid types: {type(a).__name__}, {type(b).__name__}")
        return None

# Test
divide_safely(10, 2)
divide_safely(10, 0)

# ============================================
# 9. Using Python Debugger (pdb)
# ============================================

print("\n" + "=" * 50)
print("Python Debugger (pdb)")
print("=" * 50)

print("""
Using pdb debugger:

  import pdb

  def function():
      x = 5
      pdb.set_trace()  # Execution pauses here
      y = x * 2
      return y

Commands:
  l (list):     Show surrounding code
  n (next):     Execute next line
  s (step):     Step into functions
  c (continue): Continue execution
  p varname:    Print variable value
  w (where):    Show call stack
  h (help):     Show help
""")

# Example (commented out so script doesn't pause)
# def debug_example():
#     x = 10
#     y = 20
#     pdb.set_trace()  # Debugger pauses here
#     z = x + y
#     return z

print("\n(Uncomment to use pdb.set_trace())")

# ============================================
# 10. Best Practices Summary
# ============================================

print("\n" + "=" * 50)
print("Best Practices")
print("=" * 50)

print("""
✓ DO:
  - Use logging instead of print()
  - Write clear docstrings
  - Follow PEP 8 style guide
  - Use type hints
  - Keep functions focused
  - Write meaningful variable names
  - Use constants for magic values
  - Document complex algorithms

✗ DON'T:
  - Use single-letter variables (except in loops)
  - Write functions longer than 20-30 lines
  - Ignore error messages
  - Use bare except clauses
  - Hardcode values
  - Write confusing comments
  - Skip documentation
  - Violate PEP 8 without reason

PEP 8 Tools:
  pip install black       # Auto-formatter
  pip install pylint      # Code analyzer
  pip install flake8      # Style checker
  pip install mypy        # Type checker
""")

print("\n✅ Lesson 1 Complete!")
