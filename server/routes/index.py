from .auth.login import init as login_init
from flask import Flask

def init(app: Flask):
    # auth
    login_init(app)

    # other handlers
