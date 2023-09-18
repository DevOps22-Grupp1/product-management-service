from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
 

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['testdb']
users_collection = db['users']

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    # Check if the username already exists
    if users_collection.find_one({'username': username}):
        return jsonify({'message': 'Username already exists'}), 400

    # Create a new user document in MongoDB
    user = {'username': username, 'password': password}
    result = users_collection.insert_one(user)

    return jsonify({'message': 'User registered successfully', 'user_id': str(result.inserted_id)}), 201

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = users_collection.find_one({'username': username, 'password': password})

    if not user:
        return jsonify({'message': 'Invalid username or password'}), 401

    return jsonify({'message': 'Login successful', 'user_id': str(user['_id'])}), 200



def logout_user(user_id):
    # Here, you can implement the logic for logging the user out.
    # This might involve revoking authentication tokens or performing
    # any other necessary actions.

    # For this example, we'll simply return a message indicating successful logout.
    return jsonify({'message': 'User logged out successfully'}), 200

# Endpoint for updating user information
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json

    # Ensure that the user exists
    existing_user = users_collection.find_one({'_id': ObjectId(user_id)})
    if not existing_user:
        return jsonify({'message': 'User not found'}), 404

    # Update user information (for example, allow updating the password)
    # You can customize this part to update other user information as needed
    if 'password' in data:
        users_collection.update_one({'_id': ObjectId(user_id)}, {'$set': {'password': data['password']}})

    return jsonify({'message': 'User updated successfully'}), 200

@app.route('/users/<user_id>', methods=['GET'])
def get_single_user(user_id):
    data = {}

    # Use find_one to retrieve a single document based on the provided user_id
    user = users_collection.find_one({"_id": int(user_id)})
    
    if user:
        # Convert the ObjectId to a string (if needed)
        if '_id' in user:
            user['_id'] = str(user['_id'])
        
        data = user

    return jsonify(data)



@app.route('/users/<user_id>', methods=['DELETE'])
def delete_single_user(user_id):
    users_collection.delete_one({"id": int(user_id)})
    return f"delete the post from the database"



@app.route('/users', methods=['DELETE'])
def delete_all_users(user_id):
    pass
    


@app.route('/')
def hello_world():
    return 'Hello, this is user management service'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
