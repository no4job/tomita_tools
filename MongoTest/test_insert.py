__author__ = 'mdu'
from pymongo import MongoClient
import datetime
class person(object):
    def __init__(self,name):
        self.name = name

client = MongoClient()
db=client.modelDB
model = db.model
# result=coll.insert_one({"x":"y"})
# #print(client.server_info())
# print(client.database_names())
# client.close()
#alternate = {person("Andrew") : "Cambridge", person("Barabara") : "Bloomsbury", person("Andrew"): "Corsica"}
#print (alternate)
alternate = {"Andrew" : "Cambridge", "Barabara" : "Bloomsbury"}
model.insert(alternate)
alternate = { "Andrew": "Corsica"}
model.insert(alternate)
exit(0)


