import os
from pycaret.classification import *

MODEL_PKL_PATH='model/model' if os.getenv('ENV') == 'development' else 'frontend/model/model'
MODEL = load_model(os.path.realpath(MODEL_PKL_PATH))

def predict(data):
    return predict_model(MODEL, data = data, raw_score = True)