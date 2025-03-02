import pymongo


client = pymongo.MongoClient("mongodb+srv://mafaaz:test123@sensiecluster.sbiuc.mongodb.net/chatbot?retryWrites=true&w=majority")
db = client["chatbot"]
collection = db["web"]

def get_db():
    return collection