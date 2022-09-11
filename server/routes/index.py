from .auth.login import login
from .auth.registration import registration_user
from flask import Flask
from .client import client
import os

def init(app: Flask):
    if (not os.environ.get('_API_ONLY')):
        client(app)
    # auth
    login(app)
    registration_user(app)

    # other handlers
