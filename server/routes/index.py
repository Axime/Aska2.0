from .auth.login import login
from flask import Flask, request_started
from .client import client

def init(app: Flask):
    client(app)
    # auth
    login(app)

    # other handlers
