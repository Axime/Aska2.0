from flask import Flask, request
import json
import datausers

def registration_user(app: Flask):
    @app.route("/api/auth/registration", methods=["POST"])
    def user_reg():
        request_data = request.get_json()
        try:
            first_name = request_data["first_name"]
            last_name = request_data["last_name"]
            email = request_data["email"]
            password = request_data["password"]
            password_repeat = request_data["password_repeat"]
            secure_key = request_data["__secure_key"]

            req = first_name,last_name,email,password,password_repeat,secure_key
            datausers.add_user("".join(req))
            return "yes!"

#В случае ошибки выбрасываем это
        except KeyError as e:
            return json.dumps({
                "error": str(e),
                "error_code": 0
            }), 400, {
                       'Content-Type': 'application/json'
                   }

    return user_reg