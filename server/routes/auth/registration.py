from flask import Flask, request
import json
import sqlite3

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


            #Registration body
            con = sqlite3.connect("users.db")
            c = con.cursor()
            try:
                c.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)",
                          (first_name, last_name, email, password, password_repeat, secure_key))
                print(f"Данные добавлены {first_name} {last_name} {email} {password} {password_repeat} {secure_key}")
                con.commit()
                c.execute(f"SELECT rowid, * from users WHERE rowid >= 1")
                items = c.fetchall()
                print("Список пользователей")
                for item in items:
                    id, first_name, last_name, email, password, password_repeat, secure_key = item
                    print(f'{id} {first_name} {last_name} {email} {password} {password_repeat} {secure_key}')

                con.close()
            except KeyError as s:
                print(s)

            except Exception as e:
                print(e)



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