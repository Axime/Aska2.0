from flask import Flask, request
from peewee import *

app = Flask(__name__)

@app.route("/")
def index():
    return "home page"

@app.route("/test", methods=["POST"])
def test():
    reqest_data = request.get_json()
    try:
        lang = reqest_data["language"]
        frame = reqest_data["framework"]

        py_vers = reqest_data["version_info"]["python"]

        example = reqest_data['examples'][0]

        bool_test = reqest_data["boolean_test"]
        return """
                The language value is: {}
                The framework value is: {}
                The Python version is: {}
                The item at index 0 in the example list is: {}
                The boolean value is: {}""".format(lang, frame, py_vers, example, bool_test)
    except KeyError as e:
        return f"Блять этого нет{e}"


if __name__ == "__main__":
    app.run(debug=True)