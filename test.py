import requests
import json
import pprint
import random

<<<<<<< HEAD
print("another derp here")

=======
print("first derp here")
#another derp
>>>>>>> af640c6b66f53268351b0975e76e0bfde55412cc

BASE = 'http://127.0.0.1:5000'
EVENT = '/events/'
WARSZAWA = 'warszawa'
POZNAN = 'poznan'
KEY = 'xxxx'

with open('poznan.json', 'r') as poznan:
    result = random.choice(json.load(poznan))
    pprint.pprint(result)
