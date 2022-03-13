#additional classes and functions put my function definition in here.
# We don't need the function call here.

#we must install the requests package in our venv to use it

from unicodedata import name
import requests as r

def getCharacterImages():
    response = r.get('https://rickandmortyapi.com/api/character')
    if response.status_code == 200:
        data = response.json()
    else: 
        return response.status_code 
    characters = []
    for data in data['results']:
        if data['image']:
            characters.append((data['name'], data['image']))
            #print(data['name'], data['image'])
    
    return characters
   