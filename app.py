# app.py

from flask import Flask, request, jsonify
from bot import get_response

app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file("./index.html")

@app.route("/get_response", methods=["POST"])
def get_bot_response():
    user_input = request.form["user_input"]
    response = get_response(user_input)
    return jsonify(response)

if __name__ == "__main__":
    app.run()
