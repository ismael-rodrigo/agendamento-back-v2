import pymongo
from src.settings import settings



client = pymongo.MongoClient(settings.DATABASE_URL)



#database 'fastapi_mongo'
db = client['schedule']