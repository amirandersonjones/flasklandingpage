#intial blueprint setup
from flask import Blueprint, jsonify, request

#instantiate blueprint api and then create a connection between the blueprint api and my flask app.
api = Blueprint('api', __name__, url_prefix='/api')
#Head over to init.py

#imports for api routes
from app.models import db, Animal
from app.models import db, Movies
from .services import token_required

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
@token_required
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


#route for deleting an animal
@api.route('/animal/remove/<string:id>', methods=['DELETE'])
@token_required
def removeAnimal(id):
    """
    [DELETE] accepts an animal ID- if that ID exists in the database, remove that animal from the database
    """
    #if the animal is present in the database say so, and remove
    animal = Animal.query.get(id)
    if not animal: #if no animal with that id is in the database
        #tell the user remove failed
        return jsonify({'Remove failed':'No animal of that ID exists in the database'}), 404
    db.session.delete(animal)
    db.session.commit()
    return jsonify({'Removed animal': animal.to_dict()}), 200

#route for updating an animal
@api.route('/animal/update/<string:id>', methods=['PUT'])#put is used for updating existing data-just like POST, PUT requests can include data being sent to the web server
@token_required
def updateAnimal(id):
    """
    [PUT] accepts an animal ID in the URL and JSON data in the PUT request body in the following format(all values optional)
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
    try:
        #grab the request body and query the database for an animal with that ID
        animal = Animal.query.get(id)
        data = request.get_json()
        #then update animal object.The dictionary coming in will only have coming in what we 
        # want to change. Have to make a change to our model. We need to make a reverse of our
        #to_dict model called a from_dict method
        animal.from_dict(data)#rewrite yourself from this dictionary function we created
        #and recommit it to the database aka it already exists in the database so in this case it is just saveing the changes
        db.session.commit()
        return jsonify({'Updated animal': animal.to_dict()}), 200
    except:
        return jsonify({'Request failed': 'invalid body or animal ID'}), 400







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
@token_required
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

#route for getting one movie#route for getting a subset of data on movies
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

#route for deleting a movie
@api.route('/movie/remove/<string:id>', methods=['DELETE'])
@token_required
def removeMovie(id):
    """
    [DELETE] accepts a movie ID-if that ID esists in the database, remove that movie from the database
    """
    #if the movie is present in the database say so, and remove
    movie = Movies.query.get(id)
    if not movie: #if no movie with that id is in the database
        #tell the user remove failed
        return jsonify({'Remove failed':'No movie of that ID exists in the database'}), 404
    db.session.delete(movie)
    db.session.commit()
    return jsonify({'Removed movie': movie.to_dict()}), 200

#route for updating a movie

@api.route('/movie/update/<string:id>', methods=['PUT'])#put is used for updating existing data-just like POST, PUT requests can include data being sent to the web server
def updateMovie(id):
    """
    [PUT] accepts a movie ID in the URL and JSON data in the PUT request body in the following format(all values optional)
        {
            'name': <str>,
            'category': <str>,
            'price': <float>,
            'image': <str>
            ###rest of k:v pairs optional
            'rating': <str>,
            'box_office': <int>,
            'director': <str>,
            
        }
    """
    try:
        #grab the request body and query the database for a movie with that ID
        movie = Movies.query.get(id)
        data = request.get_json()
        #then update movie object.The dictionary coming in will only have coming in what we 
        # want to change. Have to make a change to our model. We need to make a reverse of our
        #to_dict model called a from_dict method
        movie.from_dict(data)#rewrite yourself from this dictionary function we created
        #and recommit it to the database aka it already exists in the database so in this case it is just saveing the changes
        db.session.commit()
        return jsonify({'Updated animal': movie.to_dict()}), 200
    except:
        return jsonify({'Request failed': 'invalid body or movie ID'}), 400



