"""Day 11, Lesson 4: Complete Flask + AI Web App"""
from flask import Flask, render_template_string, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Store conversations
conversations = {}

@app.route('/')
def index():
    return render_template_string('''
    <html>
    <head>
        <title>AI Chat App</title>
        <style>
            body { font-family: Arial; max-width: 800px; margin: 50px auto; background: #f0f0f0; }
            #chat { border: 1px solid #ccc; height: 400px; overflow-y: auto; background: white; padding: 10px; margin: 10px 0; }
            .user-msg { background: blue; color: white; margin: 5px 0; padding: 10px; border-radius: 5px; }
            .ai-msg { background: green; color: white; margin: 5px 0; padding: 10px; border-radius: 5px; }
            input { width: 80%; padding: 10px; }
            button { width: 18%; padding: 10px; }
        </style>
    </head>
    <body>
        <h1>🤖 AI Chatbot</h1>
        <div id="chat"></div>
        <input type="text" id="input" placeholder="Ask me anything...">
        <button onclick="send()">Send</button>
        
        <script>
        async function send() {
            const msg = document.getElementById('input').value;
            if (!msg) return;
            
            document.getElementById('chat').innerHTML += '<div class="user-msg">You: ' + msg + '</div>';
            document.getElementById('input').value = '';
            
            const res = await fetch('/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: msg})
            });
            const data = await res.json();
            document.getElementById('chat').innerHTML += '<div class="ai-msg">AI: ' + data.response + '</div>';
            document.getElementById('chat').scrollTop = document.getElementById('chat').scrollHeight;
        }
        document.getElementById('input').onkeypress = (e) => e.key === 'Enter' && send();
        </script>
    </body>
    </html>
    ''')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    
    try:
        from groq import Groq
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "user", "content": message}],
            max_tokens=500
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Error: {str(e)}. Please set GROQ_API_KEY."
    
    return jsonify({"response": reply})

if __name__ == '__main__':
    print("Flask AI Chat App running on http://localhost:5000")
    print("Make sure .env has GROQ_API_KEY set")
    app.run(debug=True)
