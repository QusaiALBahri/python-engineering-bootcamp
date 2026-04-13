# Day 4: Advanced Python Patterns & File I/O

**Focus:** Master advanced programming techniques and working with files

## 📚 Learning Outcomes

By the end of Day 4, you will understand:

- **List Comprehensions** (advanced syntax and nested)
- **Generators** (efficient iteration with yield)
- **Decorators** (modifying function behavior)
- **Lambda Functions** (anonymous functions)
- **Map, Filter, Reduce** (functional programming)
- **File I/O** (reading, writing, JSON)
- **Context Managers** (with statements)
- **Higher-order Functions** (functions that work with functions)

## 🚀 Quick Start

```bash
# Run individual lessons
python 01_generators_decorators.py
python 02_file_io_json.py

# Practice exercises
python -m pytest EXERCISES.md
```

## 📖 Lesson Breakdown

### Lesson 1: Generators, Decorators & Advanced Iteration
Learn powerful patterns for writing clean, efficient Python code.

**Topics:**
- Generator functions with `yield`
- Range vs generators (memory efficiency)
- Simple decorators
- Function wrappers
- Lambda functions for quick operations
- Map/filter/reduce patterns

**Key Concepts:**
```python
# Generator
def count_up(n):
    for i in range(n):
        yield i

# Decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

# Lambda
square = lambda x: x**2
```

### Lesson 2: File I/O & Data Persistence
Work with files and JSON for data storage and retrieval.

**Topics:**
- Opening/closing files
- Reading text files
- Writing to files
- Appending content
- Working with JSON
- CSV handling basics
- File paths and operations
- Context managers (with statement)

**Key Concepts:**
```python
# Reading file
with open("data.txt", "r") as file:
    content = file.read()

# Writing JSON
import json
data = {"name": "Ali", "age": 25}
with open("data.json", "w") as file:
    json.dump(data, file)
```

## 🎯 Mini-Project: Config File Manager

Build a configuration manager:

```python
class ConfigManager:
    def __init__(self, filename):
        self.filename = filename
        self.config = self.load()
    
    def load(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except:
            return {}
    
    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value):
        self.config[key] = value
        self.save()

# Usage
config = ConfigManager("app_config.json")
config.set("theme", "dark")
config.set("language", "en")
config.save()
```

## 💡 Pro Tips

1. **Efficient Iteration:** Use generators for large datasets
   ```python
   def read_large_file(filepath):
       with open(filepath) as file:
           for line in file:
               yield line.strip()
   ```

2. **Lambda for Simple Operations:** Keep it simple
   ```python
   numbers = [1, 2, 3, 4, 5]
   evens = list(filter(lambda x: x % 2 == 0, numbers))
   ```

3. **Decorators for Cross-Cutting Concerns:** Timing, logging, etc.
   ```python
   @timing_decorator
   def slow_function():
       pass  # Decorator adds timing automatically
   ```

4. **Context Managers:** Always use `with` for files
   ```python
   # Good - file auto-closes
   with open("file.txt") as f:
       data = f.read()
   
   # Bad - might not close
   f = open("file.txt")
   data = f.read()
   ```

5. **JSON for Data:** Store structured data easily
   ```python
   data = {"users": [{"name": "Ali", "age": 25}]}
   with open("users.json", "w") as f:
       json.dump(data, f, indent=2)
   ```

## 📝 Practice Exercises

See [EXERCISES.md](EXERCISES.md) for:
- 🔵 Beginner: List comprehensions, file reading/writing
- 🟢 Intermediate: Generators, decorators, JSON handling
- 🔴 Advanced: Complex decorators, CSV processing, data transformation

## 🔗 Resources

- [Python Generators](https://docs.python.org/3/howto/functional.html#generators)
- [Decorators Guide](https://realpython.com/primer-on-python-decorators/)
- [File I/O](https://docs.python.org/3/tutorial/inputoutput.html)
- [JSON Module](https://docs.python.org/3/library/json.html)
- [Functional Programming](https://docs.python.org/3/howto/functional.html)

## ✅ Checklist for Day 4

- [ ] Completed Lesson 1: Generators & Decorators
- [ ] Completed Lesson 2: File I/O & JSON
- [ ] Practiced list comprehensions
- [ ] Created and used at least one decorator
- [ ] Learned file handling with context managers
- [ ] Worked with JSON data
- [ ] Solved 5+ exercises

---

**Next:** Day 5 focuses on debugging, professional development practices, and putting it all together
