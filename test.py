import requests

BASE = 'http://127.0.0.1:5000'
EVENT = '/events/'
WARSZAWA = 'warszawa'
POZNAN = 'poznan'
KEY = 'xxxx'
GGL_MAPS = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='

response_warszawa = requests.get(BASE + EVENT + WARSZAWA)
response_poznan = requests.get(BASE + EVENT + POZNAN)
response_google = requests.get(GGL_MAPS + '52.12,52.33' + KEY)

print(response_warszawa.json())
print(response_poznan.text)
print(response_google.json())