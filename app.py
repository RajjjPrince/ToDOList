
# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)
todos = []

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    todos.append(data)
    return jsonify({"message": "Todo added successfully"}), 201

@app.route("/todos/<int:index>", methods=["DELETE"])
def delete_todo(index):
    if 0 <= index < len(todos):
        todos.pop(index)
        return jsonify({"message": "Todo deleted"}), 200
    return jsonify({"error": "Todo not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
