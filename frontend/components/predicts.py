import streamlit as st

from services.predict import get_all_predicts

def predicts():
    with st.expander('Visualizar Predição:', expanded = False):
        
      col1, col2, col3 = st.columns(3)

      with col1: pass

      with col3: pass

      with col2:
         submitted = st.button("Search for all predicts")

         if submitted:
            all_predicts = get_all_predicts()
            print(all_predicts)

         