import requests

BASE = 'http://127.0.0.1:5000'
EVENT = '/events/'
WARSZAWA = 'warszawa'
POZNAN = 'poznan'

response_warszawa = requests.get(BASE + EVENT + WARSZAWA)
response_poznan = requests.get(BASE + EVENT + POZNAN)

print(response_warszawa.json())
print(response_poznan.json())