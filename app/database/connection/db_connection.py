import os
from pymongo import MongoClient

class DBConnection:
    def __init__(self):
        self._database = MongoClient(
            host=os.getenv("MONGO_HOST")
        )
        self._connection = self._database[os.getenv("DATABASE_NAME")]
