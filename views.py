"""this will render html templates depending on what url we go to"""
from flask import Flask, render_template, g, request
import sqlite3
from flask.ext.wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Optional
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import saladMath as sm
from contextlib import closing
import json

app = Flask(__name__)
# this is referencing our config.py file, and weirdly lets us get away with not using a secret key
app.config.from_object("config")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/salad'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models import *

## class SaladForm(Form):
##     name = StringField('name', validators=[DataRequired()])
##     category = SelectField('category', validators=[Optional()])
##     ingredient = StringField('ingredient', validators=[DataRequired()])
## 
##     def add_category_choices(self, category_tuples):
##         self.category.choices = category_tuples

# the GET is important to display the form and stuff, and the POST lets us grab the form input
@app.route('/', methods = ["GET", "POST"])
@app.route('/index', methods = ["GET", "POST"])
def index():
    ## if form.validate_on_submit():
    ##     print "I validated on submit"
    ##     newIng = Ingredient(ingredient=form.ingredient.data,
    ##                         person=form.name.data,
    ##                         category=form.category.data)
    ##     db.session.add(newIng)
    ##     db.session.commit()

    ## else:
    ##     print "I didn't validate"

    ## ingredients = Ingredient.query.all()
    ## categories_for_printing = {}
    ## categories = Category.query.all()
    ## for cat_string in [cat.category for cat in categories]:
    ##     categories_for_printing[cat_string] = []
    ## for ing in ingredients:
    ##     categories_for_printing[ing.category].append((ing.ingredient, ing.person))


    ## ourRatios = sm.calculateRatios(categories_for_printing)
    ## warningsList = sm.warnAboutRatios(sm.perfectSaladRatios, ourRatios)
    ## warningsString = ", ".join(warningsList)
    return render_template('index.html')
##             form=form,
##             categoryDict = categories_for_printing,
##             warnings = warningsString)
## 
@app.route("/add", methods=['POST'])
def add():
    testCategory = db.session.query(Category).get(request.form['category'])

    #category = Category.query.get(int(request.form['category']))
    newIng = Ingredient(request.form['ingredient'],
                        request.form['name'], 
                        testCategory)
                        #request.form['category'])
    #newIng = Ingredient('test ingredient',
    #                    'test alicia',
    #                    category)
    db.session.add(newIng)
    db.session.commit()

##     db = get_db()
##     with closing(db.cursor()) as cur:
##         cur.execute('insert into Ingredient (person, category, ingredient) values (?, ?, ?)', 
##                     [request.form['name'], request.form['category'], request.form['ingredient']])
##         db.commit()
##     db.close()
    return "" 

@app.route("/getCategories")
def getCategories():
    categories = Category.query.all()
    categoryList = [{"name":cat.category, "id":cat.id} for cat in categories]
    return json.dumps(categoryList)

@app.route("/salad")
def salad():
    ingredients = Ingredient.query.all()
    ingredientDict = {"Ingredients": []}
    for ing in ingredients:
        name = ing.person
        category = ing.category.category
        ingredient = ing.ingredient
        ingredientDict["Ingredients"].append({"name": name, "category": category, "ingredient": ingredient})
    return json.dumps(ingredientDict)

##     db = get_db()
##     with closing(db.cursor()) as cur:
##         cur.execute('SELECT person, category, ingredient FROM Ingredient')            
##         IngredientTableTuples = cur.fetchall()
##         ingredientDict = {"Ingredients": []}
##         for name, category, ingredient in IngredientTableTuples:
##             ingredientDict["Ingredients"].append({"name": name, "category": category, "ingredient": ingredient})
##     db.close()
##     return json.dumps(ingredientDict)

# fetch('/salad').then(function(resp) { resp.json().then(function() {console.log(arguments); }); })

@manager.command
def run():
    app.run(debug=True)

if __name__ == '__main__':
    manager.run()
