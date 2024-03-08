from flask import Flask, jsonify, request
from flask_restx import Api

app = Flask(__name__, )
api = Api(app)

@app.route("/health", methods=['GET'])
def health():
    return "Alive"

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True, port=8081)