import os

#class Config(object):
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", 'postgresql://localhost/salad')


WTF_CRSF_ENABLED = True
SECRET_KEY = 'sldfkasldj'

