import googlemaps
import pprint

API_KEY = 'xxxxxxx'
WARSAW = '52.232146,21.016407'
RADIUS = 5000

gmaps = googlemaps.Client(key=API_KEY)
result = gmaps.places_nearby(location=WARSAW, radius=RADIUS, open_now=False, type='stadium')

for item in result['results']:
    # place_name = item['name']
    # status = item['business_status']
    place_id = item['place_id']
    # location = str(item['geometry']['location']['lat']) + ',' + str(item['geometry']['location']['lng'])
    # vicinity = item['vicinity']
    _fields = ['adr_address',
               'vicinity',
               'geometry/location/lat',
               'geometry/location/lng',
               'formatted_address',
               ]
    place = gmaps.place(place_id=place_id, fields=_fields)
    print(place)