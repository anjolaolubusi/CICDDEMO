from flask import Flask, jsonify, request
from flask_restx import Api
import os

app = Flask(__name__, )
api = Api(app)

@app.route("/health", methods=['GET'])
def health():
    return "Alive"

@app.route("/desc", methods=['GET'])
def desc():
    return "This is an api page"


@app.route("/about", methods=['GET'])
def about():
    return "This is built by Anjola"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))