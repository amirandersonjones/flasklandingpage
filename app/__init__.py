from flask import Flask

app = Flask(__name__)

#from our config file import the Config class that we created
from config import Config

#import blueprints
from .auth.routes import auth

#imports for database stuff
from .models import db
from flask_migrate import Migrate


#define/instantiate our Flask object... aka tell the computer that this is a flask app
app = Flask(__name__,) #instantiating Flask object. Everything we do will be tied to this

#tell This app how it should be configured -over to the config.py fil to set up for this
app.config.from_object(Config)
# aka configure our flask app from the Config object we just wrote


#create a link of communication between blueprints and app
#aka register the blueprints
app.register_blueprint(auth)

# set up our ORM and Migrate connections
db.init_app(app)
migrate = Migrate(app, db)


#we need to tell the app about any routes or models that exist!
#import the routes after funciton definition

from . import routes # from the app folder we are in import the routes
from . import models # from the app folder importer routes must come after the orm and migration setups


#may only need these based on older versions of python/unique to your computer.
# requirements.txt may look different than Sams
# pip install importlib-resources
# pip install importlib-metadata
