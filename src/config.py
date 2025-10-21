from dataclasses import dataclass
import os
from pymongo import MongoClient
import pymongo

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")


env_var = EnvironmentVariable()

mongo_client = MongoClient(env_var.mongo_db_url)
