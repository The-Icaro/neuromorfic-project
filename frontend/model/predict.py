import streamlit as st
import pandas as pd
from pycaret.classification import *

MODEL_PKL_PATH='./model/model'
MODEL = load_model(MODEL_PKL_PATH)

def predict(data):
    return predict_model(MODEL, data = data, raw_score = True)