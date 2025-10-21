from src.exception import CustomException
from src.logger import logging
import sys
from src.utils import dump_csvfile_to_mongodb_collection


# def test_except():
#     try:
#         logging.info("here ZeroDivisonError is occuring")
#         a = 1/0
#     except Exception as e:
#         raise CustomException(e,sys)


if __name__ =="__main__":
    file_path = "D:\Programs\Data Science Projects\Sensor Fault Detection\\notebook\data\\aps_failure.csv"
    database_name = 'ineuron'
    collection_name = 'sensor'
    dump_csvfile_to_mongodb_collection(filepath=file_path,database_name=database_name,collection_name=collection_name)

    # try:
    #     test_except()
    # except Exception as e:
    #     print(e)