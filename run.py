# the purpose of this file is to give my terminal and flask shell access to components of my app 
# so that I can test them through my CLI (not worrying about templates or routes)

#when you want to do testing thru the flask shell with this context processor
#change your FLASK_APP variable in .env to run.py instead of the original app

# import the things I need
from app import app
from app.models import db, User, Animal, Movies

#shell context processor-gives my flask shell ( a little terminal that has access to my flask app) 
# access to database models, etc.

@app.shell_context_processor
def shell_context():
    return {'db': db, 'User': User, 'Animal': Animal, 'Movies': Movies}
#type flask shell in terminal