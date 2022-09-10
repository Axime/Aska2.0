from flask import Flask, request
import json
from .datausers import add_user


def registration(app: Flask):
    @app.post("/api/auth/registration")
    def user_reg():
        request_data = request.get_json()
        try:
            first_name = request_data["first_name"]
            last_name = request_data["last_name"]
            email = request_data["email"]
            password = request_data["password"]
            password_repeat = request_data["password_repeat"]
            secure_key = request_data["__secure_key"]

            req = first_name, last_name, email, password, password_repeat, secure_key
            add_user("".join(req))
            return json.dumps({
                'access_token': '123',
                'user_id': 1,
                'logout_hash': '1234656'
            }), 201, {
                'Content-Type': 'application/json'
            }

        # В случае ошибки выбрасываем это
        except KeyError as e:
            return json.dumps({
                "error": str(e),
                "error_code": 0
            }), 400, {
                'Content-Type': 'application/json'
            }

    return user_reg
