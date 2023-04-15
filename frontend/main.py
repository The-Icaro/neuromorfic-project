import streamlit as st

from page.page import page

from services.data import store_new_external_data
from cache.session_state import init_session_state

init_session_state()
store_new_external_data()

st.title('Neuromorfic Project')

page()