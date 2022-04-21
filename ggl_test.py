import googlemaps
import pprint
import json

API_KEY = 'xxx'
WARSAW = '52.232146,21.016407'
POZNAN = '52.401082,16.927954'
SZCZECIN = '53.432721, 14.548077'
KRAKOW = '50.062236,19.940295'
WROCLAW = '51.109021,17.037548'
RADIUS = 5000

gmaps = googlemaps.Client(key=API_KEY)
result = gmaps.places_nearby(location=WROCLAW, radius=RADIUS, open_now=False, type='stadium')

with open('warsaw.json', 'a') as f:
    json.dump(result['results'], f)

# for item in result['results']:
#     # place_name = item['name']
#     # status = item['business_status']
#     place_id = item['place_id']
#     # location = str(item['geometry']['location']['lat']) + ',' + str(item['geometry']['location']['lng'])
#     # vicinity = item['vicinity']
#     _fields = ['adr_address',
#                'vicinity',
#                'geometry/location/lat',
#                'geometry/location/lng',
#                'formatted_address',
#                ]
#     place = gmaps.place(place_id=place_id, fields=_fields)
#     print(place)