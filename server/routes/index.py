from .auth.login import login
from .auth.registration import registration
from flask import Flask
from .client import client

def init(app: Flask):
    client(app)
    # auth
    login(app)
    registration(app)

    # other handlers
