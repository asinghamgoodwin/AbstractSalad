from app import app

import json


@app.route('/')
def index():
    return "Hello, World"



if __name__ == '__main__':
    app.run(debug=True)
