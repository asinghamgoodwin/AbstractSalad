from app import db

class salad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(64), unique=False)
    location = db.Column(db.String(64), unique=False)
    commitments = db.relationship('commitment', backref='salad', lazy='dynamic')

    def __init__(self, date, location):
        self.date = date
        self.location = location

class category(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    commitments = db.relationship('commitment', backref='category', lazy='dynamic')

    def __init__(self, category, commitments):
        self.id = id

class commitment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    salad_id = db.Column(db.Integer, db.ForeignKey('salad.id'))
    person = db.Column(db.String(64), unique=False)
    category = db.Column(db.String(10), db.ForeignKey('category.id'))
    ingredient = db.Column(db.String(64), unique=False)

    def __init__(self, salad_id, person, category, ingredient):
        salad_id = salad_id
        person = person
        category = category
        ingredient = ingredient


