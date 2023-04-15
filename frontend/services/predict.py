import requests
from os import getenv as env

BACKEND_ROUTE = env("BACKEND_ROUTE")

def get_all_predicts():
    return requests.get(f'{BACKEND_ROUTE}/predict').json()

def store_new_predict(predict: str, ypred):
    return requests.post(f'{BACKEND_ROUTE}/predict', 
                               { "dataFeature": ypred
                                , "predict": predict }).json()