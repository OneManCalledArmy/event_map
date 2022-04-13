import requests

BASE = 'http://127.0.0.1:5000'
EVENT = '/events/'
response = requests.get(BASE + EVENT + 'warsaw')
print(response.json())