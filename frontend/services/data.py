import requests
from os import getenv as env

BACKEND_ROUTE = env("BACKEND_ROUTE")

def get_data_by_external_id(external_id='1511300'):
    return requests.get(f'{BACKEND_ROUTE}?id={external_id}').json()

def store_new_external_data(external_id='1511300', max_size=8000):
  return requests.post(f'{BACKEND_ROUTE}', 
                            { "dataId": external_id
                            , "maxSize": max_size})