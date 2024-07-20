from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client.mqtt
collection = db.messages

@app.route('/status_count', methods=['GET'])
def get_status_count():
    start = request.args.get('start')
    end = request.args.get('end')

    if not start or not end:
        return jsonify({"error": "Please provide both 'start' and 'end' query parameters"}), 400

    try:
        start_time = float(start)
        end_time = float(end)
    except ValueError:
        return jsonify({"error": "Invalid 'start' or 'end' time format. They should be valid Unix timestamps."}), 400

    pipeline = [
        {'$match': {'timestamp': {'$gte': start_time, '$lte': end_time}}},
        {'$group': {'_id': '$status', 'count': {'$sum': 1}}}
    ]

    results = collection.aggregate(pipeline)
    response = {str(result['_id']): result['count'] for result in results}

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5003, debug=True)
