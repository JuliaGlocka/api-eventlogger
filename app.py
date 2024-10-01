from flask import Flask, request, jsonify
from flask_expects_json import expects_json
from pymongo import MongoClient, errors

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['log_database']
logs_collection = db['logs']

log_schema = {
    'type': 'object',
    'properties': {
        'message': {'type': 'string'},
        'level': {'type': 'string', 'enum': ['INFO', 'WARNING', 'ERROR']},
        'timestamp': {'type': 'string'}
    },
    'required': ['message', 'level', 'timestamp']
}

@app.route('/log', methods=['POST'])
@expects_json(log_schema)
def create_log():

    data = request.get_json()


    logs_collection.insert_one(data)

    return jsonify({'status': 'Log created', 'data': data}), 201

@app.route('/status', methods=['GET'])
def status():
    try:

        client.admin.command('ping')
        return jsonify({'message': 'Connected to MongoDB: ', 'status': True}), 200
    except errors.PyMongoError:

        return jsonify({'message': 'Connected to MongoDB: ', 'status': False}), 500

if __name__ == '__main__':
    app.run(debug=True)
