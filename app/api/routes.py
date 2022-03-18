#intial blueprint setup
from flask import Blueprint, jsonify

#instantiate blueprint api and then create a connection between the blueprint api and my flask app.
api = Blueprint('api', __name__, url_prefix='/api')
#Head over to init.py

#imports for api routes
from app.models import Animal
from app.models import Movies

#the decorator belonging to a blueprint starts with @<blueprint_name> rather than @app
#below is a test route
@api.route('/test')
def test():
    #jsonify? transorms python dictionary (or list) into json data, must import jsonify next to blueprints to use
    return jsonify({'database': 'whoa this is some cool data'})

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
    animals = [a.to_dict() for a in Animal.query.all()]
    #jsonify and send
    return jsonify(animals)

#route for creating new animal-we are expecting to get some information

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
    movies = [m.to_dict() for m in Movies.query.all()]
    #jsonify and send
    return jsonify(movies)

#route for getting one movie

#route for updating an animal

#route for deleting a movie

#route for getting a subset of data on movies

#route for creating a new movie

  