#additional classes and functions put my function definition in here.
# We don't need the function call here.

#we must install the requests package in our venv to use it

import requests as r

def parse_json(response):
    charlist = []
    for item in response['results']:
        char = {
            'name': item['name'], 
            'no_ep': len(item['episode']),
               }
        
        charlist.append(char)
    return charlist