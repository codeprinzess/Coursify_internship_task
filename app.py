# app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow Cross-Origin Resource Sharing


sample_jobs = [
    {"id": 1, "title": "Software Engineer", "location": "Bangalore"},
    {"id": 2, "title": "Product Manager", "location": "Mumbai"}
]


@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    return jsonify(sample_jobs)


if __name__ == '__main__':
    app.run(debug=True)
