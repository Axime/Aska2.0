from flask import Flask, request
import json


def login(app: Flask):
    @app.route("/api/auth/login", methods=["POST"])
    def test():
        reqest_data = request.get_json()
        try:
            login = reqest_data["login"]
            password = reqest_data["password"]
            secure_key = reqest_data["__secure_key"]
            return json.dumps({
                "access_token": "None",
                "logout_hash": "None",
                "user_id": 0}
            ), 200, {
                'Content-Type': 'application/json'
            }
        except KeyError as e:
            return json.dumps({
                "error": str(e),
                "error_code": 0
            }), 400, {
                'Content-Type': 'application/json'
            }
    return test
