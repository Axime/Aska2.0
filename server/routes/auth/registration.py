import jwt
import random
from flask import Flask, request
import json
import sqlite3

def registration_user(app: Flask):
    @app.route("/api/auth/registration", methods=["POST"])
    def user_reg():
        request_data = request.get_json()

        #Парсинг JSON на переменные
        first_name= request_data["first_name"]
        last_name = request_data["last_name"]
        email = request_data["email"]
        password = request_data["password"]
        password_repeat = request_data["password_repeat"]
        secure_key = request_data["__secure_key"]


        #Заглушки
        user_token = "test_token"
        user_id = 0
        log_hash =  "test_hash"

        algorithm = "HS256"
        information_for_encode = {"test" : "test"}

        information_for_decript = jwt.encode(information_for_encode, "key", algorithm=algorithm)
        print(jwt.decode(information_for_decript, "key", algorithms=["HS256"]))

        #Ретурн функции user_reg
        return information_for_decript

    return user_reg