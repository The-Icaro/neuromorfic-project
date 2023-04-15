import pandas as pd
import streamlit as st

from model.predict import predict
from components.results import results
from services.predict import store_new_predict

def form():
    with st.form("Predict New Data"):

        form_data = {}
        
        form_data['Temperatura - Celsius'] = st.number_input("Temperatura - Celsius", step=0.01, min_value=-50.0, max_value=100.0)
        form_data['Humidade - %'] = st.slider("Humidade - %", 0, 100)
        
        col_1, col_2 = st.columns(2)

        with col_1:
            form_data['Velocidade Vento - Km/h'] = st.number_input("Velocidade Vento - Km/h", step=0.01, min_value=0.0, max_value=300.0)
        with col_2:
            form_data['Direção Vento - Graus'] = st.number_input("Direção Vento - Graus", step=0.01, min_value=0.0, max_value=360.0)
        
        col__1, col__2 =  st.columns(2)

        with col__1:
            form_data['Chuva Acumulada - mm'] = st.number_input("Chuva Acumulada - mm", step=0.01, min_value=0.0, max_value=100.0)
        with col__2:
            form_data['Sensação Térmica'] = st.number_input("Sensação Térmica", step=0.01, min_value=-50.0, max_value=100.0)

        col___1, col___2, col___3, col___4, col___5 = st.columns(5)

        with col___1: pass
        with col___2: pass
        with col___4: pass
        with col___5: pass

        predicted = False

        with col___3:
          if st.form_submit_button('Make Prediction'):
              test_data = pd.DataFrame(form_data, index=[0])
              predict_response = predict(test_data)
              store_new_predict(predict_response['prediction_label'], form_data)
              predicted = True

        if predicted:
          results(test_data, predict_response['prediction_label'].item())