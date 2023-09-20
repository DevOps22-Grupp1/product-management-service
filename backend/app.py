from flask import Flask, jsonify, request, json
from prometheus_flask_exporter import PrometheusMetrics
from pymongo import MongoClient
app = Flask(__name__)
metrics = PrometheusMetrics(app)

client = MongoClient('mongo', 27017, username='root', password='example')

db = client.allUsers
query = db.users

# Endpoint for user creation. Works.
@app.route('/users', methods=['POST'])
def create_user():
    try:

        data_list = request.json

        if not isinstance(data_list, list):
            return jsonify({'message': 'JSON data should be a list of user objects'}), 400
        
        created_users = []

        for data in data_list:
            id = data.get('id')
            name = data.get('name')
            email = data.get('email')

            if not 'name' or not 'email':
                return jsonify({'message': 'Username and password are required'}), 400

            #Check if the username already exists
            if query.find_one({'name': name}):
                return jsonify({'message': 'Username already exists'}), 400
    
            #Create a new user document
            new_user = {
                'id': id,
                'name': name,
                'email': email
            }

            #Insert the new user document into the 'users' collection
            query.insert_one(new_user)

            created_users.append(new_user)

        return jsonify({'message': 'User created successfully'}), 201  # 201 indicates resource created

    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500


#Endpoint for updating user information. Works.
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Check if the request contains a valid JSON object
        if not data or not isinstance(data, dict):
            return jsonify({'message': 'Invalid JSON data in the request'}), 400  # 400 indicates a bad request

        # Get the updated name and email fields from the JSON data
        updated_name = data.get('name')
        updated_email = data.get('email')

        # Check if the user with the provided user_id exists
        user = query.find_one({"id": user_id})

        if not user:
            return jsonify({'message': 'User not found'}), 404  # 404 indicates resource not found

        # Update the user's name and email if provided in the JSON data
        if updated_name is not None:
            user['name'] = updated_name
        if updated_email is not None:
            user['email'] = updated_email

        # Update the user document in the MongoDB collection
        query.update_one({"id": user_id}, {"$set": user})

        return jsonify({'message': 'User updated successfully'}), 200  # 200 indicates success

    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500  # 500 indicates an internal server error




#Endpoint for reading a user. Works.
@app.route('/users/<user_id>', methods=['GET'])
def get_single_user(user_id):
    data = []
    todos = query.find({"id": int(user_id)})
    for doc in todos:
        doc['_id'] = str(doc['_id'])  # This does the trick!
        data.append(doc)
    return jsonify(data)
     

#Endpoint for user deletion. Works.
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_single_user(user_id):
    try:
        # Ensure user_id is an integer
        user_id = int(user_id)

        # Check if the user with the provided user_id exists
        user = query.find_one({"id": user_id})
        if not user:
            return jsonify({'message': 'User not found'}), 404  # 404 indicates resource not found

        # Delete the user document with the provided user_id
        query.delete_one({"id": user_id})

        return jsonify({'message': 'User deleted successfully'}), 200  # 200 indicates success

    except ValueError:
        return jsonify({'message': 'Invalid user ID'}), 400  # 400 indicates a bad request

    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500  # 500 indicates an internal server error


@app.route('/')
def hello_world():
    return 'Hello, this is user management service'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
