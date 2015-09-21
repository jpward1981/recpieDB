from flask import Flask
from flask_restful import reqparse, abort, Resource, Api
from flask.ext.pymongo import PyMongo
from pymongo import MongoClient
from bson import json_util
from pymongo.errors import AutoReconnect, ConnectionFailure
import sys

app = Flask('recpieDB')
api = Api(app)
try: 
    mongo = PyMongo(app)
except errors.ConnectionFailure:
    print "Connection To Database Failed"
    sys.exit(1)

#parser = reqparse.RequestParser()
#parser.add_argument('name')

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Ingredients(Resource):
    def get(self, ingredient):
        try:
            result = mongo.db.ingredients.find_one_or_404( { 'name': ingredient } )
        except AutoReconnect as e:
            return "Connection to DB Failed, {}".format(e.message), 500
        # Convert ObjectID class to string _id
        result['_id'] = str(result['_id'])
        return result  

class AddIngredient(Resource):
    ''' This functions will either update or add an ingredient to the database. I am using the update one 
    function at this time to allow the same function to update or create a new ingredient '''
    def __init__(self):
        self.response = {}
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name')
        self.parser.add_argument('on_hand', default=True)
        self.parser.add_argument('qty')
        self.parser.add_argument('measurement')
    def post(self):
        args = self.parser.parse_args()
        try:
            id = mongo.db.ingredients.update( { 'name': args.name }, { 'name': args.name }, upsert=True )
        except AutoReconnect as e: 
            return "Insert/Update Failed, {}".format(e.message), 500
        if 'cupserted' in id:
            id['_id'] = str(id.pop('upserted'))       
        return id

api.add_resource(HelloWorld, '/')
api.add_resource(Ingredients, '/api/v1.0/ingredient/<ingredient>')
api.add_resource(AddIngredient, '/api/v1.0/ingredient/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
