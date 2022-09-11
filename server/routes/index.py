from .auth.login import login
from .auth.registration import registration_user
from flask import Flask
from .client import client

def init(app: Flask):
    client(app)
    # auth
    login(app)
    registration_user(app)

    # other handlers
