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

#new DB model for our app animals
class Animal(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    sci_name = db.Column(db.String(100), unique=True, nullable=False)
    size = db.Column(db.String(50))
    weight = db.Column(db.Integer)
    diet = db.Column(db.String(250))
    habitat = db.Column(db.String(250))
    lifespan = db.Column(db.Integer)
    description = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(150), nullable=True)#not a good idea to store this image in here unless you use no sql.
    price = db.Column(db.Float(2), nullable=False)

#the init for this is going to be different than the other table for the user because we
#are going to let some users create new data in our database and create a new animal(the user will be sending
# the 'POST' request in Json formatt to our system which translates into a python dictionary). Therefore,
#our init method for creating a new animal has to accept a single dictionary.

    #when a user submits a POST request to create a new animal 
        #they'll be sending us a python dictionary
        #we'll then use that to make our object
    #so our init method here will just be getting a single dictionary with only the items we made not nullable
    def __init__(self, dict):
        """
        expected dict struture:
        {
            'name': <str>,
            'sci_name: <str>,
            'description': <str>,
            'price': <float>,
            'image': <str>
            ###rest of k:v pairs optional
            'size': <str>,
            'weight': <int>,
            'diet': <str>,
            'habitat': <str>,
            'lifespan': <int>

        }
        """
        self.id = str(uuid4())
        self.name = dict['name'].title()
        self.sci_name = dict['sci_name'].title()
        self.description = dict['description']
        self.image = dict['image'] #storing an image in a sql database is not a good idea. no sql or a free image hosting site is a better idea.
        self.price = dict['price']
        self.size = dict.get('size') #w/this if the key does't exist it will return none. if we used the normal bracket notation we would get an error
        self.weight = dict.get('weight')
        self.diet = dict.get('diet')
        self.habitat = dict.get('habitat')
        self.lifespan = dict.get('lifespan')

        #write a function to translate this object into a dictionary
        #the role of this is to take the object/self and return a dictionary containing 
        # key value pairs for each attribute 
    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'sci_name': self.sci_name,
            'image': self.image,
            'price': self.price,
            'size': self.size,
            'weight': self.weight,
            'diet': self.diet,
            'habitat': self.habitat,
            'lifespan': self.lifespan
            }
#update my database to have this model
    #1activate my virtual environment
    #2update database flask db migrate
    #3 flask db upgrade
#test init method by adding some data by giving flask shell access to my database model,over to run.py
#import the Animal model next to the user model and in the context processor
#in terminal type flask shell (enter), then db(enter): to access my db, then the name of the model:i.e user, animal, whatever your table name is (enter) 
# to create a test of animals and the scenario of required info and unrequired info need to create a dictionary since that is the format of my init
# type in terminal ad = {}, then add key value pairs to it by saying ad['name']='Fennec Fox'(enter), ad['sci_name']='Vulpes zerda'
#now type ad to print the dict.(enter), then type fox = Animal(ad)"ad is the name of the dictionary (enter), then type fox(enter), then fox__.dict__(enter)
#check everything is right then type db.session.add(fox), db.session.commit(), then check if it worked by querying the database. type Animal.query.all() or go check elephant database

#now that we have created our database we can go about creating our API




#new DB model for my app movies
class Movies(db.Model):
     id = db.Column(db.String(50), primary_key=True)
     name= db.Column(db.String(250), unique=True, nullable=False)
     category = db.Column(db.String(50), nullable=False)
     image = db.Column(db.String(150), nullable=True)
     rating = db.Column(db.String(25))
     box_office = db.Column(db.Integer)
     director = db.Column(db.String(100))
     price = db.Column(db.Float(2), nullable=False)
     
     def __init__(self, dict):
         
        self.id = str(uuid4())
        self.name = dict['name'].title()
        self.category = dict['category']
        self.price = dict['price']
        self.image = dict['image']
        self.rating = dict.get('rating')
        self.box_office = dict.get('box_office')
        self.director = dict.get('director').title()
        
     def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'image': self.image,
            'rating': self.rating,
            'box_office': self.box_office,
            'director': self.director
            }
    
        
      
        
