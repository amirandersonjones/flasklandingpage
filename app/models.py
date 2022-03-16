# This models.py is responsible for everything database
# Primarily The instantiation of our ORM and the creation of our database models(aka tables/entities)

#import our ORM 
from flask_sqlalchemy import SQLAlchemy

#create the instance of our ORM(object relational mapper aka translater between python and SQL)
db = SQLAlchemy()

#import our LoginManager + tools
from flask_login import LoginManager, UserMixin
#create the instance of our login manager
login = LoginManager()
#create our database model-essentially the python code for a SQL create table

#necesssary function for our login manager
#show login how to query database for users
@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# tools for our models
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash
from uuid import uuid4 #the standard normal id a fuction is generated here so we have to string it in our init method

#the name of the table
class User(db.Model, UserMixin):
#this section defines our columns
    #lay out our columns just like we would in a SQL create table query
    #column_name = db.Column(db.Datatype(<options>), constraignts)
    id = db.Column(db.String(50), primary_key=True) #primary key makes this automatically not nullable as well as unique
    username = db.Column(db.String(15), nullable=False, unique=True)
    email= db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50)) #will be nullable and they don't have to be unique so we can leave this blank
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(250), nullable= False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc)) #have to import from datetime import datetime, timezone

#The plan for this model is:
#User model plan:
#id(uuid)(have to from uuid import uuid4)(uuid is a 36 alphanumerical character that makes our rows or columns unique to anything else) 
#username(string)
#first_name(string)
#last_name(string)
#email(string)
#password(string)*
    #-salted and hashed (from werkzeug.security import generate_password_hash)(salted and hashed is a security measure to make password unintelligle)
#date_created(timestamp)

#This section tells use what we are going to do with the data before we put it in our database. Our table variables are global(locally scoped to the entire user class) and the init handles individual instances
#User is an object/class we can use the init method to create a user that can transform/prep the information before we put it in our database
    def __init__(self, username, email, password, first_name='', last_name=''): #so in the parameters we put what it needs to accept first and then optional info it will accept last. This information is coming from what the use will type in
        self.username = username
        self.email = email.lower()
        self.first_name = first_name
        self.last_name = last_name
        self.password = generate_password_hash(password) #call it in from the password put in the form.before the password ever hits the database it will already be salted and hashed
        self.id = str(uuid4())

#Login Manager:
#installing flask-login(import the stances as well)(go to init.py import login manager and initialize)
#incorporating flask-login with our app
#incorporating flask-login with our user model

#Routing and templating to actually use or login and user system

