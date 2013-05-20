import os
from pymongo import Connection, MongoClient
client = MongoClient()
con = Connection()

print "URL = " + str(os.environ.get('MONGOHQ_URL'))
print "con type = " + str(type(Connection(os.environ.get('MONGOHQ_URL'))))