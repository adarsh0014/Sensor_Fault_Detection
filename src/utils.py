import pandas as pd
import numpy as np
import json
from src.logger import logging
from src.config import mongo_client


def dump_csvfile_to_mongodb_collection(filepath:str,database_name:str,collection_name:str)->None:
    try:
        df = pd.read_csv(filepath)
        df.reset_index(drop=True,inplace=True)
        json_records = list(json.loads(df.T.to_json()).values())
        mongo_client[database_name][collection_name].insert_many(json_records)
    except:
        pass