from flask import Flask, request
import json
from jwt.exceptions import JWTException
from jwt.jwt import JWT
from jwt.jwk import OctetJWK


def login(app: Flask):
    @app.post("/api/auth/login")
    def test():
        reqest_data = request.get_json()
        try:
            jwt = JWT()
            login = reqest_data["login"]
            password = reqest_data["password"]
            secure_key = reqest_data["__secure_key"]
            jwt.decode(secure_key, key=OctetJWK(b'123'))
            return json.dumps({
                "access_token": "None",
                "logout_hash": "None",
                "user_id": 0
            }), 200, {
                'Content-Type': 'application/json'
            }
        except KeyError as e:
            return json.dumps({
                "error": str(e),
                "error_code": 0
            }), 400, {
                'Content-Type': 'application/json'
            }
        except JWTException:
            return '{"error":"secure_key is invalid", "error_code": 0}', 400, {
                'Content-Type': 'applicaiton/json'
            }
    return test
