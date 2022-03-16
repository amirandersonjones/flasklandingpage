import os

basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    """set configuaration variables for our entire flask app
        """
    FLASK_APP = os.environ.get('FLASK_APP')#GO GET THE FLASK APP VALUE FROM .ENV
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') #INTERNAL PASSWORD SO TO KEEP AWAY MALICIOUS BEHAVIOR
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False