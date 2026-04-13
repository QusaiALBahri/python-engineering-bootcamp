# ✅ Day 11: Web Development & AI - SOLUTIONS

## Solution 1: Simple Flask App

```python
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome!</h1>"

@app.route('/greet/<name>')
def greet(name):
    return f"<h1>Hello, {name}!</h1>"

@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.json
    return jsonify({"received": data, "status": "success"})

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

## Solution 2: TODO API

```python
from flask import Flask, request, jsonify

app = Flask(__name__)
todos = []
next_id = 1

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    global next_id
    todo = request.json
    todo['id'] = next_id
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo:
        todo.update(request.json)
        return jsonify(todo)
    return jsonify({"error": "Not found"}), 404

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({"message": "Deleted"})

if __name__ == '__main__':
    app.run(debug=True)
```

## Solution 3: AI Chatbot

```python
from flask import Flask, request, jsonify, render_template_string
from groq import Groq
import os

app = Flask(__name__)
history = []
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route('/')
def index():
    return render_template_string('''
        <h1>AI Chatbot</h1>
        <div id="chat"></div>
        <input type="text" id="msg" placeholder="Ask something...">
        <button onclick="sendMessage()">Send</button>
        <script>
            async function sendMessage() {
                const msg = document.getElementById('msg').value;
                const res = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: msg})
                });
                const data = await res.json();
                document.getElementById('chat').innerHTML += `<p>You: ${msg}</p><p>AI: ${data.response}</p>`;
            }
        </script>
    ''')

@app.route('/api/chat', methods=['POST'])
def chat():
    msg = request.json['message']
    history.append({"role": "user", "content": msg})
    
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=history,
        max_tokens=500
    )
    
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Key Patterns

- Always return `jsonify()` from API endpoints
- Use `request.json` for POST/PUT data
- Use proper HTTP status codes (201=created, 404=notfound)
- Keep conversational data in memory or database
- Use decorators for route definition
