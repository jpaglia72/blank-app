
import requests
import streamlit as st
import numpy as np
import pandas as pd

response = requests.get("https://catfact.ninja/fact")
cat_api = response.json()

def clear_form():
    #if st.form_submit_button("Clear"):
        st.session_state.clear()
#st.form_submit_button("Clear", on_click=clear_form)

#clear_form()

#st.cache_data
with st.form(key="test form1"):
    st.form_submit_button("Submit")
    st.button("Clear")
    st.write(cat_api)


with st.form(key="dataframe"):
    st.checkbox('Show dataframe')
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.write(chart_data)

