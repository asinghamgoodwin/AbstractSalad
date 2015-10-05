#import sqlite3
#from flask import g
#from views import app
#from flask.ext.sqlalchemy import SQLAlchemy
from views import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(120))

    def __init__(self, category):
        self.category = category


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.String(120))
    person = db.Column(db.String(120))
    category_id = db.Column(db.Integer, db.ForeignKey(Category.id))
    category = db.relationship('Category',
                                backref=db.backref('Ingredient', lazy='joined'))
    salad_id = db.Column(db.Integer)

    def __init__(self, ingredient, person, category):
        self.salad_id = 1
        self.ingredient = ingredient
        self.person = person
        self.category = category

## 
## 
## 
## DATABASE = 'salad.db'
## 
## # just a helper function for get_db()
## def connect_to_database():
##     return sqlite3.connect(DATABASE)
## 
## def get_db():
##     db = getattr(g, '_database', None)
##     if db is None:
##         db = g._database = connect_to_database()
##     return db
## 
## # this function is only to be used once to initialize a database from our schema
## # Step 1: delete any existing .db file
## # Step 2: run python
## # Step 3: import models (this file)
## # Step 4: type in models.init_db()
## # Step 5: check to make sure that you now have a salad.db file! you can play with in in sqlite3
## def init_db():
##     with app.app_context():
##         db = get_db()
##         with app.open_resource('schema.sql', mode='r') as f:
##             db.cursor().executescript(f.read())
##         db.commit()
## 
## @app.teardown_appcontext
## def close_connection(exception):
##     db = getattr(g, '_database', None)
##     if db is not None:
##         db.close()
## 
## # HOW TO play with a sqlite3 database in the terminal:
## # Step 1: type in sqlite3 salad.db
## # .tables will give you a list of all of the tables
## # SELECT * FROM Table; will give you a visual of whats in that table
