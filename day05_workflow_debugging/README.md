# Day 5: Debugging, Professional Development & Workflow

**Focus:** Master debugging techniques, code style, and professional development practices

## 📚 Learning Outcomes

By the end of Day 5, you will understand:

- **Debugging Techniques** (print debugging, pdb, logging)
- **PEP 8 Style Guide** (code formatting, naming conventions)
- **Code Quality Tools** (linters, formatters, type hints)
- **Testing Basics** (unit tests, assertions)
- **Documentation** (docstrings, comments)
- **Version Control** (git workflow)
- **Virtual Environments** (project isolation)
- **Professional Practices** (code organization, best practices)

## 🚀 Quick Start

```bash
# Run individual lessons
python 01_debugging_pep8.py
python 02_testing_quality.py

# Run tests
python -m pytest test_examples.py

# Format code
python -m black script.py

# Check style
python -m pylint script.py
```

## 📖 Lesson Breakdown

### Lesson 1: Debugging & Code Style
Learn to find and fix bugs, and write clean, professional code.

**Topics:**
- Print debugging
- Python debugger (pdb)
- Logging module
- PEP 8 style guide
- Naming conventions
- Code formatting
- Comments and docstrings

**Key Concepts:**
```python
# Logging instead of print
import logging
logging.debug("Debug message")
logging.error("Error occurred")

# PEP 8 style
def calculate_sum(numbers):  # function_names are snake_case
    """Calculate sum of numbers."""
    return sum(numbers)

# Docstrings
class Person:
    """A person class."""
    
    def greet(self):
        """Return a greeting."""
        return "Hello"
```

### Lesson 2: Testing & Code Quality
Ensure code reliability through testing and quality checks.

**Topics:**
- Assertions
- Unit testing with pytest/unittest
- Test structure
- Code quality metrics
- Type hints
- Documentation practices
- Refactoring

**Key Concepts:**
```python
# Type hints
def add(a: int, b: int) -> int:
    return a + b

# Unit test
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

# Logging
import logging
logger = logging.getLogger(__name__)
logger.info("Operation completed")
```

## 🎯 Mini-Project: Quality Python Module

Build a professional module:

```python
"""Database module for user management."""

import logging
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)

class UserNotFoundError(Exception):
    """Raised when user is not found."""
    pass

class UserDatabase:
    """Manage user data with validation.
    
    Attributes:
        users: Dictionary of user records
    """
    
    def __init__(self):
        """Initialize empty database."""
        self.users: Dict[str, Dict] = {}
    
    def add_user(self, user_id: str, name: str, email: str) -> None:
        """Add a user to database.
        
        Args:
            user_id: Unique user identifier
            name: User's full name
            email: User's email address
        
        Raises:
            ValueError: If user_id already exists
        """
        if user_id in self.users:
            raise ValueError(f"User {user_id} already exists")
        
        self.users[user_id] = {"name": name, "email": email}
        logger.info(f"User {user_id} added")
    
    def get_user(self, user_id: str) -> Dict:
        """Get user by ID.
        
        Args:
            user_id: User identifier
        
        Returns:
            User data dictionary
        
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        if user_id not in self.users:
            raise UserNotFoundError(f"User {user_id} not found")
        
        return self.users[user_id]
```

## 💡 Pro Tips

1. **Use Logging:** Replace print() with logging in production
   ```python
   import logging
   logging.basicConfig(level=logging.INFO)
   logger = logging.getLogger(__name__)
   logger.info("Starting application")
   ```

2. **Type Hints:** Document parameter and return types
   ```python
   def process(data: List[int]) -> str:
       return ", ".join(map(str, data))
   ```

3. **PEP 8 Compliance:** Use tools to check automatically
   ```bash
   pip install black pylint flake8
   black your_file.py
   ```

4. **Virtual Environments:** Keep projects isolated
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install requirements.txt
   ```

5. **Write Tests:** Test-driven development improves quality
   ```python
   # test_module.py
   from module import add
   
   def test_add():
       assert add(2, 3) == 5
   ```

## 📝 Practice Exercises

See [EXERCISES.md](EXERCISES.md) for:
- 🔵 Beginner: PEP 8 formatting, simple debugging
- 🟢 Intermediate: Writing unit tests, type hints
- 🔴 Advanced: Test suites, code refactoring, logging setup

## 🔗 Resources

- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Python Debugging](https://docs.python.org/3/library/pdb.html)
- [Pytest Documentation](https://docs.pytest.org/)
- [Type Hints](https://docs.python.org/3/library/typing.html)
- [Logging Module](https://docs.python.org/3/library/logging.html)

## ✅ Checklist for Day 5

- [ ] Completed Lesson 1: Debugging & PEP 8
- [ ] Completed Lesson 2: Testing & Quality
- [ ] Written code following PEP 8
- [ ] Created at least 3 unit tests
- [ ] Used type hints in functions
- [ ] Implemented logging in a program
- [ ] Debugged a problem using pdb
- [ ] Solved 5+ exercises

---

**Congratulations!** You've completed the Python fundamentals course. You now have:
- Strong Python basics (Days 1-5)
- Advanced OOP and data structures (Days 1-3)
- Professional coding practices (Day 5)
- Ready to learn web development, data science, or other specializations!
