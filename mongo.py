from pymongo import MongoClient
from pymongo.errors import PyMongoError

class Mongo:
    def __init__(self, host="localhost", port="27017"):
        self.host = host
        self.port = port

        #connect to database
        self._connect()

    def list_databases(self):
        if self.client is not None:
            names = self.client.list_database_names()
            return names
        else:
            return None

    def _connect(self):
        try:
            self.client = MongoClient(f"mongodb://{self.host}:{self.port}/")
            print(self.client)
            print("Connection is successful")
        except PyMongoError as e:
            print(f"Connection failed:{e}")
