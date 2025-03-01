from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["registration_db"]
collection = db["users"]

# Register API
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    collection.insert_one(data)
    return jsonify({"message": "User registered successfully"}), 201

# Fetch Users API
@app.route("/users", methods=["GET"])
def get_users():
    users = list(collection.find({}, {"_id": 0}))  # Hide MongoDB _id field
    return jsonify(users), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
