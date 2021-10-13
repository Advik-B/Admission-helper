import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:8080/', connect=False)

db = mongo_client['student-data']
print(mongo_client.list_database_names())
