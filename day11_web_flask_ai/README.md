# 🎯 Day 11: Web Development & AI Integration (3 hours)

## 📚 Topics Covered

| Topic | File | Duration | What You'll Learn |
|-------|------|----------|-------------------|
| **Flask Basics** | `01_flask_intro.py` | 30min | Routes, templates, serving web pages |
| **Building an API** | `02_flask_api.py` | 45min | JSON endpoints, request handling |
| **AI Integration** | `03_ai_integration.py` | 45min | Groq, OpenAI, local LLMs |
| **Complete Web App** | `04_flask_ai_app.py` | 30min | Full-stack application |
| **Exercises & Solutions** | `EXERCISES.md`, `SOLUTIONS.md` | 45min | Hands-on projects |

---

## 🎓 Learning Outcomes

✅ Create Flask routes and serve HTML  
✅ Handle HTTP requests and JSON responses  
✅ Integrate AI models (OpenAI, Groq, LM Studio)  
✅ Build a web API with error handling  
✅ Deploy and test a simple web application  

---

## 🚀 Quick Start

```bash
pip install flask requests python-dotenv groq
python 01_flask_intro.py
```

---

## 🧠 Key Concepts

### **Flask Route**
```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.json
    return jsonify({"result": data})

if __name__ == '__main__':
    app.run(debug=True)
```

### **AI API Integration**
```python
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="mixtral-8x7b-32768",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

---

## 📊 Mini Project: AI Chatbot Web App

Build a web interface for an AI chatbot with:
- Input field for user questions
- Display AI responses
- Message history
- Clean, responsive UI
