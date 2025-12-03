from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "The C Programming Language", "author": "Brian Kernighan & Dennis Ritchie"},
    {"id": 2, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 3, "title": "The Pragmatic Programmer", "author": "Andrew Hunt & David Thomas"},
    {"id": 4, "title": "Design Patterns", "author": "Erich Gamma et al."}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
