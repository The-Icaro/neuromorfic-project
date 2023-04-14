import streamlit as st

def results(data, result):
    
    st.subheader(f'The Result is:')
    st.header(result)

    st.text('This is a result for the current data')
    st.dataframe(data)