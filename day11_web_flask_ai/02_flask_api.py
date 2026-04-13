"""Day 11, Lesson 2: Flask API and JSON Responses"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample database
users_db = [
    {"id": 1, "name": "Ali", "score": 95},
    {"id": 2, "name": "Hana", "score": 87},
    {"id": 3, "name": "Omar", "score": 92}
]

# ============================================
# 1. JSON Response
# ============================================

@app.route('/api/users', methods=['GET'])
def get_users():
    """Retrieve all users"""
    return jsonify(users_db)

# ============================================
# 2. Get Single Item
# ============================================

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a specific user"""
    user = next((u for u in users_db if u['id'] == user_id), None)
    return jsonify(user) if user else ("Not found", 404)

# ============================================
# 3. POST - Create Item
# ============================================

@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Missing data"}), 400
    
    new_id = max([u['id'] for u in users_db]) + 1
    new_user = {"id": new_id, "name": data['name'], "score": data.get('score', 0)}
    users_db.append(new_user)
    
    return jsonify(new_user), 201

# ============================================
# 4. DELETE - Remove Item
# ============================================

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user"""
    global users_db
    users_db = [u for u in users_db if u['id'] != user_id]
    return jsonify({"message": f"User {user_id} deleted"})

# ============================================
# 5. PUT - Update Item
# ============================================

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update a user"""
    user = next((u for u in users_db if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    if 'name' in data:
        user['name'] = data['name']
    if 'score' in data:
        user['score'] = data['score']
    
    return jsonify(user)

# ============================================
# 6. Search
# ============================================

@app.route('/api/search', methods=['GET'])
def search():
    """Search users by name"""
    query = request.args.get('q', '').lower()
    results = [u for u in users_db if query in u['name'].lower()]
    return jsonify(results)

# ============================================
# 7. Statistics
# ============================================

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get statistics"""
    if not users_db:
        return jsonify({"error": "No users"}), 200
    
    scores = [u['score'] for u in users_db]
    return jsonify({
        "count": len(users_db),
        "average_score": sum(scores) / len(scores),
        "max_score": max(scores),
        "min_score": min(scores)
    })

if __name__ == '__main__':
    print("Testing API endpoints:")
    print("GET    /api/users")
    print("GET    /api/users/<id>")
    print("POST   /api/users (with JSON body)")
    print("PUT    /api/users/<id>")
    print("DELETE /api/users/<id>")
    print("GET    /api/search?q=name")
    print("GET    /api/stats")
    app.run(debug=True)
