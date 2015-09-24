"""this will render html templates depending on what url we go to"""
from flask import Flask, render_template, g
import sqlite3
from flask.ext.wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Optional
from models import *

app = Flask(__name__)
app.config.from_object("config")

class SaladForm(Form):
    # with app.app_context():
    #     db = get_db()
    #     with db:
    #         cur = db.cursor()
    #         cur.execute('SELECT category from category')
    #         categoryList = cur.fetchall()
    
    name = StringField('name', validators=[DataRequired()])
    category = SelectField('category', validators=[Optional()])
    ingredient = StringField('ingredient', validators=[DataRequired()])

    def add_category_choices(self, category_tuples):
        self.category.choices = category_tuples

@app.route('/')
@app.route('/index', methods = ["GET", "POST"])
def index():
    db = get_db()
    with db:
        cur = db.cursor()
        form = SaladForm()
        pretend_ingredients = ["cats", "spinace", "avodabo", "carobs"]
        pretend_categories = ["greebs", "vebebbggeez", "FROOBs"]

        cur.execute('SELECT category from category')
        categoryList = cur.fetchall()
        category_tuples = [(x,x) for x in categoryList]
        form.add_category_choices(category_tuples)

        if form.validate_on_submit():
            print "I validated on submit"
            cur.execute('insert into Ingredient (person, category, ingredient) values (?, ?, ?)', 
                        [form.name.data, form.category.data, form.ingredient.data])
            
            print categoryList
            print form.name.data
            print form.category.data
        else:
            print "I didn't validate"
    db.close()
    return render_template('index.html',
            form=form,
            ingredient_list=pretend_ingredients,
            categories=pretend_categories)


def get_categories():
    pass

if __name__ == '__main__':
    app.run(debug=True)
