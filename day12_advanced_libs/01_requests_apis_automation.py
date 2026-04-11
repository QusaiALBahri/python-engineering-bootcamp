# Day 12: Advanced Libraries & Tools

## Learning Outcomes

- Use powerful Python libraries
- Automate tasks (PyAutoGUI)
- Call AI APIs (OpenAI, DeepSeek)
- Work with requests and APIs

---

## Part 1: HTTP Requests

```python
import requests

# GET request
response = requests.get("https://api.github.com/users/github")
print(response.status_code)  # 200 = success
print(response.json())  # Parse as JSON

# POST request
data = {"name": "Alice", "age": 25}
response = requests.post("https://api.example.com/users", json=data)

# Headers
headers = {"Authorization": "Bearer TOKEN"}
response = requests.get("https://api.example.com/data", headers=headers)
```

---

## Part 2: Task Automation with PyAutoGUI

```python
import pyautogui

# Mouse
pyautogui.moveTo(100, 100)  # Move to coordinates
pyautogui.click()  # Click

# Keyboard
pyautogui.typewrite("Hello")  # Type text
pyautogui.press("enter")  # Press key

# Screenshot
img = pyautogui.screenshot()
img.save("screenshot.png")

# OCR (requires pytesseract)
text = pyautogui.locateOnScreen("image.png")  # Find image on screen
```

---

## Part 3: AI APIs

### OpenAI
```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{
        "role": "user",
        "content": "Write a haiku about Python"
    }]
)

print(response.choices[0].message.content)
```

### DeepSeek
```python
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{
        "role": "user",
        "content": "Explain Python OOP"
    }]
)

print(response.choices[0].message.content)
```

---

## Part 4: Working with Environment Variables

Create `.env`:
```
OPENAI_API_KEY=sk-...
DEEPSEEK_API_KEY=...
DATABASE_URL=postgresql://...
```

Load in Python:
```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
db_url = os.getenv("DATABASE_URL")
```

---

## Part 5: Data Formats

### CSV
```python
import csv

# Read
with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"])

# Write
with open("output.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 25})
```

### JSON
```python
import json

# Read
with open("data.json") as f:
    data = json.load(f)

# Write
with open("output.json", "w") as f:
    json.dump({"name": "Alice", "age": 25}, f, indent=2)
```

### XML
```python
import xml.etree.ElementTree as ET

# Read
tree = ET.parse("data.xml")
root = tree.getroot()

# Write
root = ET.Element("data")
child = ET.SubElement(root, "person")
child.text = "Alice"
tree = ET.ElementTree(root)
tree.write("output.xml")
```

---

## Key Libraries

| Library | Use |
|---------|-----|
| **requests** | HTTP requests |
| **openai** | OpenAI API |
| **python-dotenv** | Environment config |
| **pyautogui** | Desktop automation |
| **faker** | Generate fake data |

---

## Next Steps

- [ ] Make an API request to GitHub
- [ ] Call an AI API (OpenAI or DeepSeek)
- [ ] Read and process a CSV file
- [ ] See EXERCISES.md
