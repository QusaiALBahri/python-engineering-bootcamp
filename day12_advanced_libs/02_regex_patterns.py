"""Day 12, Lessons 2-4: Regex, PyAutoGUI, DuckDB"""
import re
import duckdb

print("=== Regular Expressions ===\n")

text = "Contact: john@example.com (555-1234) or visit www.example.com. #hashtag"

emails = re.findall(r'[\w.-]+@[\w.-]+', text)
phones = re.findall(r'\d{3}-\d{4}', text)
urls = re.findall(r'www\.\w+\.\w+', text)
hashtags = re.findall(r'#\w+', text)

print(f"Emails: {emails}")
print(f"Phones: {phones}")
print(f"URLs: {urls}")
print(f"Hashtags: {hashtags}")

print("\n=== DuckDB SQL ===\n")

conn = duckdb.connect(':memory:')

# Create and populate table
data = [
    (1, 'Alice', 90, 'A'),
    (2, 'Bob', 85, 'B'),
    (3, 'Charlie', 95, 'A'),
    (4, 'Diana', 78, 'C'),
]

conn.execute("""
    CREATE TABLE students (
        id INTEGER,
        name VARCHAR,
        score INTEGER,
        grade VARCHAR
    )
""")

conn.execute("INSERT INTO students VALUES (?, ?, ?, ?)", data)

# Queries
print("All students:")
print(conn.execute("SELECT * FROM students").fetchall())

print("\nStudents with A grade:")
print(conn.execute("SELECT name, score FROM students WHERE grade = 'A'").fetchall())

print("\nAverage score:")
print(conn.execute("SELECT AVG(score) FROM students").fetchone())

print("\nGrouped by grade:")
print(conn.execute("SELECT grade, COUNT(*) as count FROM students GROUP BY grade").fetchall())

conn.close()

print("\n✅ Day 12 lessons complete!")
