from flask import Flask, jsonify, request, json
from prometheus_flask_exporter import PrometheusMetrics
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
metrics = PrometheusMetrics(app)
client = MongoClient('mongo-2', 27017, username="root", password="example")

db = client.allUsers
query = db.users


@app.route('/')
def hello_world():
    return "Success", 200, {"Access-Control-Allow-Origin": "*"}


@app.route('/api/users', methods=['GET'])
def get_all_users():
    data = []
    todos = query.find()
    for doc in todos:
        doc['_id'] = str(doc['_id'])  # This does the trick! to what sais everyone else. 
        data.append(doc)
    return jsonify(data)


@app.route('/api/user/<user_id>', methods=['GET'])
def get_single_user(user_id):
    data = []
    todos = query.find({"id": int(user_id)})
    for doc in todos:
        doc['_id'] = str(doc['_id'])  # This does the trick! YUP YUP
        data.append(doc)
    return jsonify(data)


@app.route('/api/user', methods=['POST'])
def post_users():
    data = json.loads(request.data)
    data["id"] = increment_post()
    query.insert_one(data)
    return f"a new post has been added"


@app.route('/api/user/<user_id>', methods=['DELETE'])
def delete_users(user_id):
    query.delete_one({"id": int(user_id)})
    return f"delete the post from the database"

@app.route('/api/user/<user_id>', methods=['PUT'])
def update_users(user_id):
    data = json.loads(request.data)
    data["id"] = user_id
    query.find_one_and_update({'id': int(user_id)} , {'$set': data})
    return f"update the post from the database"


def increment_post():
    return str(query.count_documents({}))



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4006, debug=False)
