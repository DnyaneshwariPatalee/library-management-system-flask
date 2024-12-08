from flask import Flask, request, jsonify
import uuid
from functools import wraps

app = Flask(__name__)

# In-memory data storage
books = []
members = []
tokens = {}

# Token-based authentication decorator
def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Extract token from the "Authorization" header (format: "Bearer <token>")
        token = request.headers.get("Authorization")
        if token:
            token = token.split(" ")[1]  # To get the token after "Bearer"
        if not token or token not in tokens:
            return jsonify({"message": "Unauthorized"}), 401
        return func(*args, **kwargs)
    return wrapper

# Root route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Library Management System!"})

# Routes for Books
@app.route('/books', methods=['GET', 'POST'])
@token_required
def books_list():
    if request.method == 'POST':
        data = request.json
        book = {
            "id": str(uuid.uuid4()),
            "title": data.get("title"),
            "author": data.get("author"),
            "year": data.get("year")
        }
        books.append(book)
        return jsonify({"message": "Book added successfully", "book": book}), 201
    
    # GET with optional search and pagination
    query = request.args.get('q', '').lower()
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))

    filtered_books = [b for b in books if query in b["title"].lower() or query in b["author"].lower()]
    start = (page - 1) * per_page
    end = start + per_page
    return jsonify(filtered_books[start:end])

@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
@token_required
def book_detail(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return jsonify({"message": "Book not found"}), 404

    if request.method == 'GET':
        return jsonify(book)
    
    if request.method == 'PUT':
        data = request.json
        book.update({k: v for k, v in data.items() if k in book})
        return jsonify({"message": "Book updated successfully", "book": book})
    
    if request.method == 'DELETE':
        books.remove(book)
        return jsonify({"message": "Book deleted successfully"})

# Routes for Members
@app.route('/members', methods=['GET', 'POST'])
@token_required
def members_list():
    if request.method == 'POST':
        data = request.json
        member = {
            "id": str(uuid.uuid4()),
            "name": data.get("name"),
            "email": data.get("email")
        }
        members.append(member)
        return jsonify({"message": "Member added successfully", "member": member}), 201

    return jsonify(members)

@app.route('/members/<member_id>', methods=['GET', 'PUT', 'DELETE'])
@token_required
def member_detail(member_id):
    member = next((m for m in members if m["id"] == member_id), None)
    if not member:
        return jsonify({"message": "Member not found"}), 404

    if request.method == 'GET':
        return jsonify(member)
    
    if request.method == 'PUT':
        data = request.json
        member.update({k: v for k, v in data.items() if k in member})
        return jsonify({"message": "Member updated successfully", "member": member})
    
    if request.method == 'DELETE':
        members.remove(member)
        return jsonify({"message": "Member deleted successfully"})

# Authentication
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or data.get("username") != "admin" or data.get("password") != "admin":
        return jsonify({"message": "Invalid credentials"}), 401

    token = str(uuid.uuid4())
    tokens[token] = "admin"
    return jsonify({"message": "Login successful", "token": token})

@app.route('/logout', methods=['POST'])
@token_required
def logout():
    token = request.headers.get("Authorization").split(" ")[1]
    tokens.pop(token, None)
    return jsonify({"message": "Logged out successfully"})

if __name__ == '__main__':
    app.run(debug=True)
