import streamlit as st

def results(data, result):
    
    st.subheader(f'O resultado é:')
    st.header(f'A quantidade de chuva, em milimetros, seria de: {result}')

    st.subheader('Este resultado está relacinado com esses dados: ')
    st.dataframe(data)