import pymongo
from pymongo import errors

from common_types import Config


class DB:

    def __init__(self, config: Config):
        self.client = None
        self.db = None
        self.collection = None
        self.connect(config)

    def connect(self, config: Config):
        try:
            self.client = pymongo.MongoClient(config.db_ip, config.db_port)
            self.client.server_info()
            self.db = self.client[config.db_name]
            self.collection = self.db[config.db_collection]
        except errors.ServerSelectionTimeoutError as e:
            print(f"Can not connection to {config.db_ip}:{config.db_port}")
            print(e)
        except errors.InvalidName as e:
            print(f"database name is used.")

        self.collection.create_index("currentTimestamp", unique=True)

    def insert_document(self, data: dict) -> int:
        try:
            element_id = self.collection.insert_one(data).inserted_id
        except errors.DuplicateKeyError:
            return None
        return element_id

