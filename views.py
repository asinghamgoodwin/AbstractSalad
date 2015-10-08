"""this will render html templates depending on what url we go to"""
from flask import Flask, render_template, g, redirect
import sqlite3
from flask.ext.wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Optional
from models import *
import saladMath as sm
from contextlib import closing
#for the css compiler
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
# this is referencing our config.py file, and weirdly lets us get away with not using a secret key
app.config.from_object("config")

#This is a sass compiler for styling
assets = Environment(app)
scss = Bundle('sass/main.scss', filters='pyscss', output='css/all.css')
assets.register('scss_all', scss)


class SaladForm(Form):
    ### for some reason this didn't work up here so we did the work down in index() where we'd
    ### already opened a database connection. Maybe we can't open two at once?
    # with app.app_context():
    #     db = get_db()
    #     with db:
    #         cur = db.cursor()
    #         cur.execute('SELECT category from category')
    #         categoryList = cur.fetchall()
    
    name = StringField('name', validators=[DataRequired()])
    # doing validators=[DataRequired()] did not work for the SelectField
    # category = SelectField('category', validators=[Optional()])
    ingredient = StringField('ingredient', validators=[DataRequired()])

    # this is helpful because we want to get our category choices from the database
    # if your choices were static, you could do: SelectFeild('category', choices=[(0,'greens'),(1,'veggies')], validators=...)
    # def add_category_choices(self, category_tuples):
    #     self.category.choices = category_tuples



@app.route('/')
# the GET is important to display the form and stuff, and the POST lets us grab the form input
@app.route('/index')
def index():
    # opening a connection to our database (get_db comes from models)
    db = get_db()
    # with db:
    with closing(db.cursor()) as cur:
        # cur = db.cursor()
        greens_form = SaladForm()
        veggies_form = SaladForm()
        protein_form = SaladForm()
        dressing_form = SaladForm()
        other_form = SaladForm()

        formList = [greens_form, veggies_form, protein_form,dressing_form, other_form]

        category_keys = ["Greens", "Veggies", "Protein", "Dressing", "Other"]

        form_cat_zip = [(formList[i], category_keys[i]) for i in range(5)]
        # [(greens_form, "Greens"), (veggies_form, "Veggies")]

        ### this section is to get the categories from our category table to use as drop-down choices
        cur.execute('SELECT category from category')
        categoryList = cur.fetchall()
        # the categories come as tuples, but we only want the first part, x[0]
        # these come as unicode strings, and we can .encode('utf8') to make them pretty, normal strings
        category_tuples = [(x[0].encode('utf8'),x[0].encode('utf8')) for x in categoryList]
        # for form in formList:
        #     form.add_category_choices(category_tuples)
    # db.close()

    ### this section is for pretty printing
    # db = get_db()
    # with db:
    # with closing(db.cursor()) as cur:
        # cur = db.cursor()

    #     for (form, cat) in form_cat_zip:
    #         if form.validate_on_submit():
    #             print cat+"I validated on submit"
    #             cur.execute('insert into Ingredient (person, category, ingredient) values (?, ?, ?)', 
    #                         [form.name.data, cat, form.ingredient.data])
    #         # print categoryList
    #         # print form.name.data
    #         #print form.category.data
    #         else:
    #             print "I didn't validate"
    # # could we also use close_connection() ?


        cur.execute('SELECT person, category, ingredient FROM Ingredient')            
        IngredientTableTuples = cur.fetchall()
        categories = [x[0] for x in category_tuples]
        categories_for_printing = {}
        for cat in categories:
            categories_for_printing[cat] = [(x[2].encode('utf8'), x[0].encode('utf8')) for x in IngredientTableTuples if x[1] == cat]
            
        #print categories_for_printing
    db.close()

    ourRatios = sm.calculateRatios(categories_for_printing)
    warningsList = sm.warnAboutRatios(sm.perfectSaladRatios, ourRatios)
    warningsString = ", ".join(warningsList)
    print warningsString
    # # pretend_ingredients = ["cats", "spinace", "avodabo", "carobs"]
    # pretend_categories = ["greebs", "vebebbggeez", "FROOBs"]
    return render_template('index.html',
                            form_cat_zip=form_cat_zip,
                            categoryDict=categories_for_printing,
                            # warnings=warningsString
                            )
            # ingredient_list=pretend_ingredients,
            # categories=pretend_categories)

@app.route('/Veggies', methods=["POST"])
def veggies():

    veggies_form = SaladForm()

    db = get_db()

    with closing(db.cursor()) as cur:

        if veggies_form.validate_on_submit():
            print "Veggies validated on submit"
            cur.execute('insert into Ingredient (person, category, ingredient) values (?, ?, ?)',
                    [veggies_form.name.data, 'Veggies', veggies_form.ingredient.data])
        else:
            print "Veggies didn't validate"

    db.commit()
    db.close()
    
    return redirect('/index')

@app.route('/Protein', methods=["POST"])
def protein():

    protein_form = SaladForm()

    db = get_db()

    with closing(db.cursor()) as cur:

        if protein_form.validate_on_submit():
            print "Protein validated on submit"
            cur.execute('insert into Ingredient (person, category, ingredient) values (?, ?, ?)',
                    [protein_form.name.data, 'Protein', protein_form.ingredient.data])
        else:
            print "Protein didn't validate"

    db.commit()
    db.close()
    
    return redirect('/index')

@app.route('/Greens', methods=["POST"])
def greens():

    greens_form = SaladForm()

    db = get_db()

    with closing(db.cursor()) as cur:

        if greens_form.validate_on_submit():
            print "Greens validated on submit"
            cur.execute('insert into Ingredient (person, category, ingredient) values (?, ?, ?)',
                    [greens_form.name.data, 'Greens', greens_form.ingredient.data])
        else:
            print "Greens didn't validate"

    db.commit()
    db.close()
    
    return redirect('/index')

@app.route('/Dressing', methods=["POST"])
def dressing():

    dressing_form = SaladForm()

    db = get_db()

    with closing(db.cursor()) as cur:

        if dressing_form.validate_on_submit():
            print "Dressing validated on submit"
            cur.execute('insert into Ingredient (person, category, ingredient) values (?, ?, ?)',
                    [dressing_form.name.data, 'Dressing', dressing_form.ingredient.data])
        else:
            print "Dressing didn't validate"

    db.commit()
    db.close()
    
    return redirect('/index')

@app.route('/Other', methods=["POST"])
def other():

    other_form = SaladForm()

    db = get_db()

    with closing(db.cursor()) as cur:

        if other_form.validate_on_submit():
            print "Other validated on submit"
            cur.execute('insert into Ingredient (person, category, ingredient) values (?, ?, ?)',
                    [other_form.name.data, 'Other', other_form.ingredient.data])
        else:
            print "Other didn't validate"

    db.commit()
    db.close()
    
    return redirect('/index')


# def get_categories():
#     pass


# this is what makes our app start up when we run python views.py
# I'm pretty sure that the debug=True option makes it so that we don't need to
# restart the server each time we make a change to one of these files
if __name__ == '__main__':
    app.run(debug=True)
