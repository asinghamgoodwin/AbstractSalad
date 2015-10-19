from app import app, manager

import json


@app.route('/')
def index():
    return "Hello, World"

