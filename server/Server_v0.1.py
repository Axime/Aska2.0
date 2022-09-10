from flask import Flask, request
from peewee import *
import json


app = Flask(__name__)

@app.route("/")
def index():
    return "home page"

@app.route("/api/auth/login", methods=["POST"])
def test():
    reqest_data = request.get_json()
    try:
        login = reqest_data["login"]
        password = reqest_data["password"]
        secure_key = reqest_data["__secure_key"]

        return json.dumps({"access_token":"None",
                           "logout_hash": "None",
                           "user_id": 0})

    except KeyError as e:
        return json.dumps({"error":str(e), "error_code": 0})


if __name__ == "__main__":
    app.run(debug=True)