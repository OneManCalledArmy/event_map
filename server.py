from flask import Flask, jsonify
from flask_restful import Api, Resource
from db import events

app = Flask(__name__)
api = Api(app)

class Events(Resource):
    def get(self, city):
        return jsonify(events[city])

api.add_resource(Events, '/events/<string:city>')

if __name__ == '__main__':
    app.run(debug=True)