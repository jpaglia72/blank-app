
import requests
import streamlit as st
import numpy as np
import pandas as pd

response = requests.get("https://catfact.ninja/fact")

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.write(chart_data)

#st.cache_data
if st.button("Test"):
    #st.session_state.get
   # response = requests.get("https://catfact.ninja/fact")
    print(response.json())

    cat_api = response.json()
    st.write(cat_api)
