import streamlit as st

from components.form import form
from components.predicts import predicts
from components.description import description

def page():
  description()
  form()
  predicts()