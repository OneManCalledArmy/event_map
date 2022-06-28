import requests
import json
import pprint
import random

print("another derp here")


BASE = 'http://127.0.0.1:5000'
EVENT = '/events/'
WARSZAWA = 'warszawa'
POZNAN = 'poznan'
KEY = 'xxxx'

with open('poznan.json', 'r') as poznan:
    result = random.choice(json.load(poznan))
    pprint.pprint(result)
