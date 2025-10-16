from src.exception import CustomException
from src.logger import logging
import sys


def test_except():
    try:
        logging.info("here ZeroDivisonError is occuring")
        a = 1/0
    except Exception as e:
        raise CustomException(e,sys)


if __name__ =="__main__":
    try:
        test_except()
    except Exception as e:
        print(e)