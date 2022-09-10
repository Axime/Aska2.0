from .auth.login import login
from flask import Flask

def init(app: Flask):
    # auth
    login(app)

    # other handlers
