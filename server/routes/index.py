from .auth.login import login
from .auth.registration import registration_user
from flask import Flask

def init(app: Flask):
    # auth
    login(app)
    registration_user(app)

    # other handlers
