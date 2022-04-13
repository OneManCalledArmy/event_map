from random import uniform

WARSZAWA = {'LAT': (52.12, 52.33),
            'LON': (20.83, 21.12)
            }

POZNAN = {'LAT': (52.33, 52.47),
          'LON': (16.83, 17.00)
          }

def rand_coord(city):
    lat = uniform(*city['LAT'])
    long = uniform(*city['LON'])
    return lat, long

events = {'warszawa': {'event': 'modlitwa',
                     'lat': rand_coord(WARSZAWA)[0],
                     'long': rand_coord(WARSZAWA)[1]},
          'poznan': {'event': 'chlanie',
                     'lat': rand_coord(POZNAN)[0],
                     'long': rand_coord(POZNAN)[1]}
          }