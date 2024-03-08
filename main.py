from flask import Flask, jsonify, request
from flask_restx import Api
import os

app = Flask(__name__, )
api = Api(app)

@app.route("/health", methods=['GET'])
def health():
    return "Alive"

@app.route("/", methods=['GET'])
def home():
    return "This is an api page"

@app.route("/sshTest", methods=['GET'])
def sshTest():
    return "Deployment is working"



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))