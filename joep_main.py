import streamlit as st
import requests
import pandas as pd

#import json
#from bs4 import BeautifulSoup

#commit from windows test
#commit from linux test
#new linux installation

response2 = requests.get("http://api.open-notify.org/iss-now.json")
print(response2.json())


response = requests.get("https://catfact.ninja/fact")
print(response.json())

st.title("🎈 App Test")
st.write("For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

#st.write(response2)

if st.button("**Fetch API Data**"):
    data = response.json()
    st.write(data)
    st.table(data, border=True)

    # st.write(pd.DataFrame(data))
    # st.dataframe(data)
    
# Simple button
if st.button("Test"):
    st.write("Test Button pressed")
    st.write(st.session_state.keys)


if st.button("Clear Form"):
    st.session_state.clear()
    


# # Button with a key and different type
# if st.button("Reset Counter", key="reset_button", type="primary"):
#     st.session_state.counter = 0
#     st.write("Counter reset!")
   