"""this will render html templates depending on what url we go to"""
from flask import Flask, render_template, g
import sqlite3
from flask.ext.wtf import Form
from wtforms import StringField
from wtforms import DataRequired

app = Flask(__name__)

class SaladForm(Form):
    name = StringField('name', validators=[DataRequired()])
    ingredient = StringField('ingredient', validators=[DataRequired()])

@app.route('/')
@app.route('/index')
def index():
    form = SaladForm()
    pretend_ingredients = ["cats", "spinace", "avodabo", "carobs"]
    pretend_categories = ["greebs", "vebebbggeez", "FROOBs"]

    if form.validate_on_submit():
        return render_template('index.html',
                form=form,
                ingredient_list=pretend_ingredients,
                categories=pretend_categories)
    else:
        return render_template('index.html',
                form=form,
                ingredient_list=pretend_ingredients,
                categories=pretend_categories)


def get_categories():
    pass

if __name__ == '__main__':
    app.run(debug=True)
