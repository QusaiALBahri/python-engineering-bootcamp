"""
Day 4, Lesson 2: File I/O & Data Persistence
Covers:
  - Opening/closing files
  - Reading text files
  - Writing to files
  - JSON serialization
  - Working with paths
  - Context managers
  - CSV basics
"""

import json
import os
from pathlib import Path

# ============================================
# 1. Basic File Reading
# ============================================

print("=" * 50)
print("Reading Files")
print("=" * 50)

# Create a sample file first
sample_content = """Line 1: Hello World
Line 2: Python is awesome
Line 3: File I/O is important
Line 4: Context managers are helpful"""

with open("sample.txt", "w") as f:
    f.write(sample_content)

# Read entire file
print("Method 1: Read entire file")
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# Read lines
print("\n\nMethod 2: Read as lines")
with open("sample.txt", "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines, 1):
        print(f"  Line {i}: {line.rstrip()}")

# Read line by line (memory efficient)
print("\n\nMethod 3: Iterate lines (memory efficient)")
with open("sample.txt", "r") as f:
    for line in f:
        print(f"  {line.rstrip()}")

# ============================================
# 2. Writing to Files
# ============================================

print("\n" + "=" * 50)
print("Writing to Files")
print("=" * 50)

# Write mode (overwrites)
with open("output.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")

print("✓ Created output.txt")

# Append mode (adds to end)
with open("output.txt", "a") as f:
    f.write("Fourth line (appended)\n")

print("✓ Appended to output.txt")

# Read result
with open("output.txt", "r") as f:
    print("\nFile content:")
    print(f.read())

# ============================================
# 3. JSON Serialization
# ============================================

print("\n" + "=" * 50)
print("Working with JSON")
print("=" * 50)

# Create data
student_data = {
    "name": "Ali",
    "age": 25,
    "grades": [85, 90, 88],
    "courses": ["Python", "Web Dev", "AI"]
}

# Write to JSON
json_file = "student.json"
with open(json_file, "w") as f:
    json.dump(student_data, f, indent=2)

print(f"✓ Wrote JSON to {json_file}")

# Read from JSON
with open(json_file, "r") as f:
    loaded_data = json.load(f)

print("\nLoaded data:")
print(f"  Name: {loaded_data['name']}")
print(f"  Age: {loaded_data['age']}")
print(f"  Grades: {loaded_data['grades']}")

# Convert to JSON string
json_string = json.dumps(student_data, indent=2)
print("\nJSON String:")
print(json_string)

# ============================================
# 4. Working with Multiple Records (JSON Array)
# ============================================

print("\n" + "=" * 50)
print("JSON Files with Multiple Records")
print("=" * 50)

# Multiple students
students = [
    {"id": 1, "name": "Ali", "score": 85},
    {"id": 2, "name": "Sara", "score": 92},
    {"id": 3, "name": "Mona", "score": 78}
]

# Save
with open("students.json", "w") as f:
    json.dump(students, f, indent=2)

# Load and display
with open("students.json", "r") as f:
    loaded_students = json.load(f)

print("Students:")
for student in loaded_students:
    print(f"  {student['id']}. {student['name']}: {student['score']}")

# ============================================
# 5. CSV Basics
# ============================================

print("\n" + "=" * 50)
print("CSV Files")
print("=" * 50)

import csv

# Write CSV
csv_data = [
    ["Name", "Age", "City"],
    ["Ali", "25", "Baghdad"],
    ["Sara", "22", "Basra"],
    ["Mona", "28", "Mosul"]
]

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)

print("✓ Created data.csv")

# Read CSV
print("\nCSV Content:")
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"  {row}")

# Read as dictionaries
print("\nAs dictionaries:")
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['Name']}: {row['Age']} years old in {row['City']}")

# ============================================
# 6. File Paths & Operations
# ============================================

print("\n" + "=" * 50)
print("File Paths & Operations")
print("=" * 50)

# Using pathlib (modern approach)
current = Path(".")
print(f"Current directory: {current.absolute()}")

# Create path
file_path = Path("data.json")
print(f"\nFile exists: {file_path.exists()}")
print(f"Is file: {file_path.is_file()}")
print(f"File size: {file_path.stat().st_size} bytes")
print(f"File name: {file_path.name}")
print(f"File stem: {file_path.stem}")
print(f"File suffix: {file_path.suffix}")

# List files
print("\nJSON files in current directory:")
for json_file in current.glob("*.json"):
    print(f"  - {json_file.name}")

# ============================================
# 7. Error Handling with Files
# ============================================

print("\n" + "=" * 50)
print("Error Handling with Files")
print("=" * 50)

def safe_read_file(filename):
    """Read file with error handling"""
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        return None
    except IOError as e:
        print(f"❌ Error reading file: {e}")
        return None

# Try to read non-existent file
content = safe_read_file("nonexistent.txt")

# Read existing file
content = safe_read_file("sample.txt")
if content:
    print(f"✓ Read {len(content)} characters")

# ============================================
# 8. Config File Manager (Practical Example)
# ============================================

print("\n" + "=" * 50)
print("Practical: Config Manager")
print("=" * 50)

class ConfigManager:
    """Manage application configuration"""
    
    def __init__(self, filename="config.json"):
        self.filename = filename
        self.config = self.load()
    
    def load(self):
        """Load config from file"""
        if Path(self.filename).exists():
            with open(self.filename, "r") as f:
                return json.load(f)
        return {}
    
    def save(self):
        """Save config to file"""
        with open(self.filename, "w") as f:
            json.dump(self.config, f, indent=2)
    
    def get(self, key, default=None):
        """Get config value"""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """Set and save config value"""
        self.config[key] = value
        self.save()

# Use config manager
config = ConfigManager("app_config.json")
config.set("theme", "dark")
config.set("language", "en")
config.set("autoSave", True)

print(f"Theme: {config.get('theme')}")
print(f"Language: {config.get('language')}")
print(f"AutoSave: {config.get('autoSave')}")

# ============================================
# 9. Context Managers Explained
# ============================================

print("\n" + "=" * 50)
print("Context Managers (with statement)")
print("=" * 50)

print("""
✓ GOOD - Using context manager with "with":
  with open("file.txt", "r") as f:
      data = f.read()
  # File automatically closes

✗ BAD - Manual file handling:
  f = open("file.txt", "r")
  data = f.read()
  f.close()  # Might be forgotten!
  
Benefits:
  - Automatic resource cleanup
  - Exception-safe file handling
  - Cleaner, more readable code
  - Guaranteed file closure
""")

# ============================================
# 10. Best Practices
# ============================================

print("\n" + "=" * 50)
print("File I/O Best Practices")
print("=" * 50)

print("""
✓ DO:
  - Always use 'with' statement
  - Specify encoding: open("file.txt", encoding="utf-8")
  - Use Path for cross-platform paths
  - Check file exists before reading
  - Use JSON for structured data
  - Close files automatically (with statement)
  - Handle exceptions gracefully

✗ DON'T:
  - Forget to close files
  - Assume files are in specific location
  - Ignore encoding issues
  - Read huge files all at once
  - Use string concatenation for paths
  - Ignore exceptions
""")

# Clean up test files
for file in ["sample.txt", "output.txt", "student.json", "students.json", "data.csv", "app_config.json"]:
    if Path(file).exists():
        os.remove(file)

print("\n✅ Lesson 2 Complete!")
