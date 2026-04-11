# Day 11: Web Development with Flask

## Learning Outcomes

- Build web applications with Flask
- Create routes and templates
- Handle HTTP requests and responses
- Connect frontend and backend

---

## Part 1: Hello World

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/user/<name>")
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)  # http://localhost:5000
```

---

## Part 2: Templates (HTML)

Create `templates/index.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ message }}</p>
</body>
</html>
```

Flask code:
```python
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html", 
                          title="Welcome",
                          message="Hello!")
```

---

## Part 3: Forms and Requests

```python
from flask import request, render_template

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == "admin" and password == "secret":
            return "Login successful!"
        else:
            return "Login failed!"
    
    return render_template("login.html")
```

---

## Part 4: JSON API

```python
from flask import jsonify

@app.route("/api/data")
def get_data():
    data = {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }
    return jsonify(data)

@app.route("/api/users/<int:user_id>")
def get_user(user_id):
    return jsonify({"user_id": user_id, "name": "Unknown"})
```

---

## Part 5: Complete Example

```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory database
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@app.route("/")
def home():
    return render_template("index.html", users=users)

@app.route("/api/users", methods=["GET"])
def list_users():
    return jsonify(users)

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json
    new_user = {
        "id": max(u["id"] for u in users) + 1,
        "name": data.get("name"),
        "email": data.get("email")
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
```

---

## Key Concepts

| Concept | Purpose |
|---------|---------|
| **Route** | URL path and handler |
| **Template** | HTML with variables |
| **Request** | Get data from user |
| **Response** | Send data to user |
| **JSON** | Data in web format |

---

## Next Steps

- [ ] Create a todo app with Flask
- [ ] Build a simple blog
- [ ] See EXERCISES.md for challenges
