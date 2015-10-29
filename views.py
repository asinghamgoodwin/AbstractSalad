from flask import render_template
from app import app, manager

import json


@app.route('/')
def index():
    return render_template('index.html')

