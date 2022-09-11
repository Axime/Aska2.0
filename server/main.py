import os
from flask import Flask, request
from peewee import *
from .routes.index import init


def start():
    app = Flask(__name__)

    init(app)

    # if __name__ == "__main__":
    app.run(debug=(lambda: True if '_DEBUG' in os.environ else False)())
