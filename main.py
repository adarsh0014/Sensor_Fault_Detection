from src.exception import CustomException
from src.logger import logging
import sys
# from src.utils import dump_csvfile_to_mongodb_collection
from src.pipeline.training_pipeline import TrainPipeline
from fastapi import FastAPI
from src.constant.training_pipeline import SAVED_MODEL_DIR
from src.constant.application import APP_HOST,APP_PORT
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from fastapi.responses import Response
from src.ml.model.estimator import ModelResolver,TargetValueMapping
from src.utils.main_utils import load_object
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi import File, UploadFile, Response
import pandas as pd

# def test_except():
#     try:
#         logging.info("here ZeroDivisonError is occuring")
#         a = 1/0
#     except Exception as e:
#         raise CustomException(e,sys)




# app = FastAPI(openapi_url=None, docs_url=None)
app = FastAPI()


origins = ["*"]
#Cross-Origin Resource Sharing (CORS) 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train",response_class=Response)
async def train_route()-> Response:
    try:

        train_pipeline = TrainPipeline()
        if train_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")
        train_pipeline.run_pipeline()
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")



@app.get("/predict",response_class=Response)
async def predict_route()-> Response:
    try:
        #get data from user csv file
        #conver csv file to dataframe

        df=None

        model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not model_resolver.is_model_exists():
            return Response("Model is not available")
        
        best_model_path = model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)
        
        y_pred = model.predict(df)
        df['predicted_column'] = y_pred
        df['predicted_column'].replace(TargetValueMapping().reverse_mapping(),inplace=True)
        
        #decide how to return file to user.
        
    except Exception as e:
        return Response(f"Error Occured! {e}")







def main():
    try:
      
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)


if __name__ =="__main__":
    # file_path = "D:\Programs\Data Science Projects\Sensor Fault Detection\\notebook\data\\aps_failure.csv"
    # database_name = 'ineuron'
    # collection_name = 'sensor'
    # dump_csvfile_to_mongodb_collection(filepath=file_path,database_name=database_name,collection_name=collection_name)

    app_run(app,host=APP_HOST,port=APP_PORT)
    

    # try:
    #     test_except()
    # except Exception as e:
    #     print(e)