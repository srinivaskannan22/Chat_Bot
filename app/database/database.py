from pymongo import MongoClient
import os

mongodb_connection_uri=os.getenv('MONOGODB_CONNECTION_URI')

Mongo=MongoClient(mongodb_connection_uri)


###conneciton to the databbase
db =Mongo['chatbot_collection']
