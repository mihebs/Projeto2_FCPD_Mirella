from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders')
def get_orders():
    return jsonify([
        {"id": 101, "user_id": 1, "total": 1200.50, "status": "shipped"},
        {"id": 102, "user_id": 2, "total": 45.00, "status": "pending"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
