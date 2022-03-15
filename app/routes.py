#the route/controller
#flask routes control what content is shown on what url depending on how the user is accessing the 
# url, what button they've pressed. etc.

#the general structure of a flask route is a function with a decorator 
#the decorator adds lines of code that run before and after the decorated function

#our first route:
#goal display the index.html file when user navigates to the base url aka http://127.0.0.1:5000/ 
    # 1.)we need access to our app
from app import app # import the app variable defined in __init__.py
    # 2.) we need the ability to show an html file at a specified url
    #if your route's job is to display an html page -> it's return value should be a call to render_template

from flask import render_template, request
import requests
from lib2to3.pgen2.driver import Driver

from .forms import DriverForm


#from .forms import DriverForm

#non-flask import for route functionality
from .services import getCharacterImages #need to put .services so it wont be looking for a python module. This is a services file and not a python module.
#.services says "from the services file" rather than "from the services module"

from random import choice

import requests as r



@app.route('/') # this decorator says: this is a rounte of the flask app 'app with the url endpoint '/'
def home():
    headline= 'WELCOME TO THE SHOP OF HORRORS'
    x = choice(['TODAY IS FOR MURDER', ' TODAY IS FOR MAYHEIM', ' TODAY IS FOR MADNESS', 'TODAY WILL BE BLOODY', 'NOT YOUR LUCKY DAY'])
    return render_template('index.html', headline=headline, change_heading = x )
# line 17 associates a python function with a url, the decorator makes the funtion on 18 a
# flask route and ties it to 
#the url. when the accesses the url. the python function runs.It returns a call to render template
#and the html is shown because of the python function which is 
# running(python) because it is set up as a route through flask

#create another route--> decorater@app.route('url endpoint), define a python function
@app.route('/shopofhorrors')
def movies():
    headline= 'WELCOME TO THE SHOP OF HORRORS'
    return render_template('horror.html',headline=headline)

@app.route('/shopofhorrorsactors')
def actors():
    headline = 'WELCOME TO THE SHOP OF HORRORS'
    return render_template('actors.html', headline=headline)

#gallary route/made this new route from the original templates
@app.route('/gallary')
def gallary():
    characters= getCharacterImages()
    #print(len(characters))
    return render_template('gallary.html', characters=characters)

# f1 driver info route
#HTTP-METHODS SPECIFY THE ACCEPTABLE METHODS OF CONNECTION TO THIS ENDPOINT ON OUR SERVER
    #METHODS DEFAULTS TO JUST GET BUT WE  HAVE GET-USER JUST GETS INFO FROM OUR SITE, POST-SENDING INFO
    # TO THE USER, PUT-UPDATING INFO ON A SERVER, DELETE-DELETING INFO 
@app.route('/f1', methods=['GET', 'POST'])
def f1drivers():
    form = DriverForm() # this form will be used in both the GET and POST sides of this route
#     forms = DriverForm()
#     #Two scenarios here:
#         #1. user is just accessing this page 
#             #http method-GET-GETTING DATA FROM THE WEB SERVER
#         #2. user has submitted the form requesting certain driver information
#             #http method-POST-SENDING DATA TO THE WEB SERVER
    if request.method == 'POST':
        #this means the user has submitted the form
        #two possible behaviors
            # 1. user provided value form info (aka a real driver name)
                #make api request and display relevant info
            # 2. user provided bad form info
                #redirect them and tell them bad info
        data = r.get('http://ergast.com/api/f1/drivers/{form.drivername.data}.json').json()
        if data['MRData']['total'] !='0':
            # make an api request and display relevant info
            driver = data['MRData']['DriverTable']['Drivers'][0]
        else:
            #user provided bad form info
            driver = form.drivername.data
        # retrn a render_template with the relevant or lack of relevant driver data
        return render_template('f1drivers.html', form=form, driver=driver) #works for post request
    return render_template('f1drivers.html', form=form, driver=None) #works for our GET requests
     
