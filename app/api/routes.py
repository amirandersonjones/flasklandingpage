#intial blueprint setup
from flask import Blueprint, jsonify, request

#instantiate blueprint api and then create a connection between the blueprint api and my flask app.
api = Blueprint('api', __name__, url_prefix='/api')
#Head over to init.py

#imports for api routes
from app.models import db, Animal
from app.models import db, Movies


#the decorator belonging to a blueprint starts with @<blueprint_name> rather than @app
#below is a test route
@api.route('/test')
def test():
    #jsonify? transorms python dictionary (or list) into json data, must import jsonify next to blueprints to use
    return jsonify({'database': 'whoa this is some cool data'}), 200

#make sure you run code often so do a flask run and go to website to see if it is working

#API ROUTES FOR MY ANIMALS MODEL

#route for getting all animals-start with this 1st (easier)-
@api.route('/animals', methods=['GET'])
def getAnimals():
    """
    [Get] return json data on all of the animals in our database
    """
    #query the animals
    #I want to jsonify the result of .to_dict() for each animal in our animals query
    animals = {'Animals': [a.to_dict() for a in Animal.query.all()]}
    #jsonify and send
    return jsonify(animals), 200

#route for creating new animal-we are expecting to get some information
@api.route('/create/animal', methods=['POST'])
def createAnimal():
    """
    [POST] creates a new animal in our database with data provided in the request body
    expected data format JSON
    """
    #how do we accept request in the body of a post request 
    # depending on how specific we want our data to be - we may want to build out some checks 
    # on the data coming in, does it actually make sense? is it something we want in our database?
    #otherwise, create the new animal in the database
    try:
        data = request.get_json() #grab any json data from the body of the request made to this route
        new_animal = Animal(data)
        db.session.add(new_animal)
        db.session.commit()
        return jsonify({'Created New Animal': new_animal.to_dict()}), 201
    except:
        return jsonify({'Create Animal Rejected': 'Animal already exists or improper request.'}), 400
    
#we cant test this create animals route because ['GET'] method doesnt exist for the url
#create animal only the ['POST']. to test we would have to write the request in python or use an API
#testing tool

#route for getting one animal-this is going to be a dynamic route/
# we don't want to create a route for every single animal we want to get.that would be too many routes!
# this route will expect input coming from through the url
@api.route('/animal/name/<string:name>', methods=['GET'])
def getAnimal(name):
    """
    [GET] That accepts an animal name through the url and either gets 
    the appropriate animal from our database or returns that we dont have that animal
    """
    a = Animal.query.filter_by(name=name.title()).first()# we use the .title so when the user types in the search by name it will capaitalize and return whether they use lowercase name or uppercase name
    if a:
        return jsonify(a.to_dict()), 200
    else:
        return jsonify({'Request failed': 'No animal with that name.'}), 404



#route for updating an animal

#route for deleting an animal





#API ROUTES FOR MY MOVIES MODEL

#route for getting all movies
@api.route('/movies', methods=['GET'])
def getMovies():
    """
    [Get] return json data on all of the animals in our database
    """
    #query the movies
    #I want to jsonify the result of .to_dict() for each movie in our movies query
    movies = {'Movies': [m.to_dict() for m in Movies.query.all()]} #we can take the dictionary off and just return a list.up to u how u want to structure the results
    #jsonify and send
    return jsonify(movies), 200

#route for creating a new movie-we are expecting to get some information
@api.route('/create/movie', methods=['POST'])
def createMovie():
    #how do we accept request in the body of a post request 
    # depending on how specific we want our data to be - we may want to build out some checks 
    # on the data coming in, does it actually make sense? is it something we want in our database?
    #otherwise, create the new movie in the database
    try:
        data = request.get_json() #grab any json data from the body of the request made to this route
        new_movie = Movies(data)
        db.session.add(new_movie)
        db.session.commit()
        return jsonify({'Created New Movie': new_movie.to_dict()}), 201
    except:
        return jsonify({'Create Movie Rejected': 'Movie already exists or improper request.'}), 400

#route for getting one movie
#route for getting one animal-this is going to be a dynamic route/
# we don't want to create a route for every single animal we want to get.that would be too many routes!
# this route will expect input coming from through the url
@api.route('/movie/name/<string:name>', methods=['GET'])
def Movie(name):
    """
    [GET] That accepts an animal name through the url and either gets 
    the appropriate animal from our database or returns that we dont have that animal
    """
    m = Movies.query.filter_by(name=name.title()).first()# we use the .title so when the user types in the search by name it will capaitalize and return whether they use lowercase name or uppercase name
    if m:
        return jsonify(m.to_dict()), 200
    else:
        return jsonify({'Request failed': 'No movies with that name.'}), 404


#route for updating a movie

#route for deleting a movie

#route for getting a subset of data on movies

#route for creating a new movie

  