"""Day 11, Lesson 3: AI Integration with Flask"""
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ============================================
# 1. Using Groq API
# ============================================

def query_groq(message):
    """Query Groq API (Free, no charges)"""
    try:
        from groq import Groq
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "user", "content": message}],
            max_tokens=500
        )
        return response.choices[0].message.content
    except ImportError:
        return "Groq library not installed. Install with: pip install groq"
    except Exception as e:
        return f"Error: {str(e)}"

# ============================================
# 2. Using OpenAI (Requires API key)
# ============================================

def query_openai(message):
    """Query OpenAI API"""
    try:
        import openai
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
            max_tokens=500
        )
        return response['choices'][0]['message']['content']
    except ImportError:
        return "OpenAI library not installed"
    except Exception as e:
        return f"Error: {str(e)}"

# ============================================
# 3. Flask Routes
# ============================================

@app.route('/chat', methods=['POST'])
def chat():
    """Chat endpoint"""
    data = request.json
    message = data.get('message', '')
    
    if not message:
        return jsonify({"error": "No message provided"}), 400
    
    # Use Groq by default (free)
    response = query_groq(message)
    
    return jsonify({
        "user_message": message,
        "ai_response": response
    })

@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze text"""
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    prompt = f"Analyze this text (sentiment, key points, summary):\n{text}"
    response = query_groq(prompt)
    
    return jsonify({
        "original_text": text,
        "analysis": response
    })

@app.route('/summarize', methods=['POST'])
def summarize():
    """Summarize text"""
    data = request.json
    text = data.get('text', '')
    
    prompt = f"Summarize this in 2-3 sentences:\n{text}"
    response = query_groq(prompt)
    
    return jsonify({"summary": response})

if __name__ == '__main__':
    print("AI Integration App running on http://localhost:5000")
    print("\nCreatea .env file with:")
    print('GROQ_API_KEY="your-key"')
    print('OPENAI_API_KEY="your-key" (optional)')
    app.run(debug=True)
