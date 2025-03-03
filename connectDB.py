import pymongo
import os

CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")
DATABASE = os.getenv("DATABASE")
COLLECTION=os.getenv("COLLECTION")

def initialize_db():
    try:
        client = pymongo.MongoClient(CONNECTION_STRING)
        db = client[DATABASE]
        return db[COLLECTION]
    except ConnectionRefusedError:
        print("Connection with MongoDB server has been refused, try again.")
        
    
def get_db():
    collection = initialize_db()
    return collection