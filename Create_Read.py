'''
Created on Feb 1, 2021

@author: Michael Bauer
'''
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:53120/?authSource=test' % (username, password))
        self.database = self.client['AAC']

    def create(self, data):
        # Takes in a dictionary parameter to insert into animals collection
        # checks if parameter is empty and if it is a dictionary
        if data is not None and isinstance(data, dict):
            self.database.animals.insert_one(data)  # data should be dictionary
            return True    
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

    def read(self, params):
        # Takes in a dictionary parameter to query the animals collection
        # checks if parameter is empty and if it is a dictionary
        if params is not None and isinstance(params, dict):
            return self.database.animals.find(params, {"_id":False})
        else:
            raise Exception ("Nothing to search, because data parameter is empty")

    def update(self, searchParams, update):
        # Takes in two dictionary parameters to query the animals collection
        # Then update the found document with the update parameter
        # checks if parameters are empty and if they are a dictionary
        if searchParams is not None and update is not None and isinstance(searchParams, dict) and isinstance(update, dict):
            result = self.database.animals.update_one(searchParams, {'$set': update})
            
            if result.modified_count > 0:
                return list(self.database.animals.find(update))
            
            else:
                raise Exception ("Nothing to update")

        else:
            raise Exception ("Nothing to update")
    
    
    def delete(self, delete):
        # Takes in a dictionary parameter to query the animals collection and delete the found document
        # checks if parameter is empty and if it is a dictionary
        if delete is not None and isinstance(delete, dict):
            returnResult = list(self.database.animals.find(delete))
            result = self.database.animals.delete_one(delete)
            
            if result.deleted_count > 0:
                return (returnResult)
            
            else:
                raise Exception ("Nothing to delete")

        else:
            raise Exception ("Nothing to delete")

