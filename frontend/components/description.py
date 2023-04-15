import os
import pandas as pd
import streamlit as st

from services.data import get_data_by_external_id

DATASET_PATH = 'model/dataset.csv' if os.getenv('ENV') == 'development' else 'frontend/model/dataset.csv'
DATASET_ABSOLUT_PATH = os.path.realpath(DATASET_PATH)

def description():
    
    data = pd.read_csv(DATASET_PATH)

    external_data = get_data_by_external_id()
    description = external_data['channel']

    st.header(description['name'])
    st.subheader(description['description'])
    st.text(f"creation Date: {description['created_at']}")
    st.text(f"Last Modified: {description['updated_at']}")

    st.dataframe(data)

