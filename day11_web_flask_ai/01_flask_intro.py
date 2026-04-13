"""Day 11, Lesson 1: Flask Basics and Routing"""
from flask import Flask, render_template_string, request

app = Flask(__name__)

# ============================================
# 1. Basic Route
# ============================================

@app.route('/')
def home():
    return """
    <h1>Welcome to Flask!</h1>
    <p>This is a simple Flask application.</p>
    <a href="/about">Go to About</a>
    """

# ============================================
# 2. Route with Variable
# ============================================

@app.route('/user/<name>')
def greet_user(name):
    return f"<h1>Hello, {name}!</h1><p>Welcome to Flask.</p>"

@app.route('/age/<int:age>')
def show_age(age):
    return f"<h1>You are {age} years old</h1>"

# ============================================
# 3. Multiple Methods
# ============================================

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        return f"<h1>Data received</h1>"
    return """
    <form method="POST">
        <input type="text" name="data" placeholder="Enter data">
        <button type="submit">Submit</button>
    </form>
    """

# ============================================
# 4. About Page
# ============================================

@app.route('/about')
def about():
    return """
    <h1>About This App</h1>
    <p>This is a Flask demo application showing routing concepts.</p>
    <a href="/">Back to Home</a>
    """

# ============================================
# 5. 404 Error Handler
# ============================================

@app.errorhandler(404)
def not_found(error):
    return "<h1>Page not found (404)</h1>", 404

if __name__ == '__main__':
    print("Flask app running on http://localhost:5000")
    print("Routes:")
    print("  http://localhost:5000/")
    print("  http://localhost:5000/user/Ali")
    print("  http://localhost:5000/age/25")
    print("  http://localhost:5000/about")
    print("  http://localhost:5000/data")
    app.run(debug=True)
