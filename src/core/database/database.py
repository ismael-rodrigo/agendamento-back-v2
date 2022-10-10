import pymongo
from src.core.settings import settings



client = pymongo.MongoClient(settings.DATABASE_URL)



#database 'fastapi_mongo'
db = client['fastapi_mongo']