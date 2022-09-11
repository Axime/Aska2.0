import os
from .auth.login import login
from .auth.registration import registration_user as registration
from flask import Flask
from .client import client


def init(app: Flask):

    if (not ('_API_ONLY' in os.environ)):
        client(app)
    # auth
    login(app)
    registration(app)

    # other handlers
