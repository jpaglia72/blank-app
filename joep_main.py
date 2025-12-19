import streamlit as st
import requests
#import pandas as pd
#import json
#from bs4 import BeautifulSoup
from datetime import datetime
# from streamlit_option_menu import option_menu

# selected = option_menu(
#     menu_title="Main Menu", 
#     options=["Home", "Settings"], 
#     icons=["house", "gear"], 
#     orientation="horizontal" # or "vertical"
# )

current_time = datetime.now()
st.write(current_time)
print(current_time)

with st.sidebar:
    selected = st.selectbox("Main Menu", ["Dashboard", "Reports", "Settings", "About"])

if selected == "Dashboard":
    st.title("Welcome to Optionator")
elif selected == "Reports":
    st.write("View Reports")
elif selected == "Settings":
    st.write("View Settings")
elif selected == "About":
    st.write("About Optionator")
    st.text("Optionator assists traders with reccomending profitable calls & puts." \
    "It uses AI technolgy to assit option traders to pick potentially profitiable startegies")
iss_now_api = requests.get("http://api.open-notify.org/iss-now.json")
print(iss_now_api.json())

cat_api = requests.get("https://catfact.ninja/fact")
print(cat_api.json())

#st.title("Welcome to Optionator", text_alignment="left")

# st.write("For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
#st.write(response2)

textbox = st.text_input("Enter stock symbol:")
st.write(textbox)

if st.button("**Fetch API Data**"):
    
    #iss data returned:
    iss_api = iss_now_api.json()
    st.write(iss_api)
    st.table(iss_api)
    #st.dataframe(iss_api)


    #cat api returned
    cat_data = cat_api.json()
    st.write(cat_data)
    st.table(cat_data)
    #st.dataframe(cat_data)

    ##write 
    # st.write(pd.DataFrame(data))

    # st.write(pd.DataFrame(data))
    # st.dataframe(data)
    
# Simple button
if st.button("Test"):
   pressed =  st.write("Test Button pressed")
   st.write(pressed)
   st.session_state.get(pressed)



if st.button("Clear Form"):
    st.session_state.clear()
    
# # Button with a key and different type
# if st.button("Reset Counter", key="reset_button", type="primary"):
#     st.session_state.counter = 0
#     st.write("Counter reset!")