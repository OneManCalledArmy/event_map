from flask import Flask, jsonify
from flask_restful import Api, Resource
import random
import json

print("test1")
print("test2")

app = Flask(__name__)
api = Api(app)

class Events(Resource):
    def get(self, city):
        with open(city + '.json', 'r') as f:
            result = random.choice(json.load(f))
        return result

api.add_resource(Events, '/events/<string:city>')

if __name__ == '__main__':
    app.run(debug=True)
