
import requests
import streamlit as st
import numpy as np
import pandas as pd

response = requests.get("https://catfact.ninja/fact")
cat_api = response.json()


#st.cache_data
with st.form(key="test form1"):
    st.form_submit_button("Submit")
       # st.session_state.__getstate__
    st.write(cat_api)
    st.form_submit_button("Clear")
    st.session_state.clear()

with st.form(key="dataframe"):
    st.checkbox('Show dataframe')
    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.write(chart_data)

