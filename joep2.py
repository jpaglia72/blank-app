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

#try to add this sidebar
selected = st.selectbox("Main Menu", ["Dashboard", "Reports", "Settings", "About"])
match selected:
    case "Dashboard":
        #selected == "Dashboard"
        st.write("Dashboard")
    case "Reports":
        st.write("Reports, test")

       
# Function to clear the form fields via session state
# def clear_form():
#     # List of keys for the form widgets
#     form_keys = ["text_input_key", "number_input_key", "checkbox_key"]
#     for key in form_keys:
#         if key in st.session_state:
#             del st.session_state[key]
#     # st.rerun() # Use this if you need an immediate rerun after clearing



# Create a form within the sidebar
with st.sidebar.form(key='sidebar_form'):
    # Input widgets inside the form
    st.title("Welcome to Optionator!")

   # st.sidebar.divider()
    #widgets & submit buttons for sidebar menu:
    stock_symbol_input = st.text_input("Enter Stock Symbol to pull options chain and click Enter:")
    get_api_data = st.form_submit_button("Get API data")
    clear_main_form = st.form_submit_button("Clear Form")
    
    iss_now_api = requests.get("http://api.open-notify.org/iss-now.json")
    iss_api = iss_now_api.json()

# Main content area

# Check if the symbol was submitted:
# def stock_input():
#     if stock_symbol_input:
#         st.success(f"Symbol Submitted!  {stock_symbol_input}")
#     else:
#         st.info("Waiting for form submission...")

# @st.cache_data
# @st.cache_resource

def clear_form_button():
    st.session_state.clear()
clear_form_button()

def stock_input():
    if stock_symbol_input:
        st.success(f"Symbol Submitted!  {stock_symbol_input}")
    else:
        st.info("Waiting for form submission...")
stock_input()
#st.session_state.clear()

# Check if the form was submitted
# if submit_button:
#     st.success(f"Symbol Submitted!  {stock_symbol}")
#     # You can now use 'name' and 'age' to update your main app logic
# else:
#     st.info("Waiting for form submission...")

#iss_now_api = requests.get("http://api.open-notify.org/iss-now.json")
# # #print(iss_now_api.json())    write data to console for testing

# cat_api = requests.get("https://catfact.ninja/fact")
#print(cat_api.json())  write data to console for testing

# textbox = st.text_input("Enter stock symbol:")
# st.write(textbox)

#@st.cache_data
#@st.cache_resource
def get_data():
    #iss_now_api = requests.get("http://api.open-notify.org/iss-now.json")
    #cat_api = requests.get("https://catfact.ninja/fact")
#    iss_api = iss_now_api.json()
  #  cat_data = cat_api.json()
    if get_api_data:    
        #iss data returned:
        #iss_api = iss_now_api.json()
        st.write(iss_api)
        st.table(iss_api)
        #cat api returned
        # st.write(cat_data)
        # st.table(cat_data)
        #st.dataframe(iss_api)
#st.session_state.clear()
get_data()

    #cat api returned
    # cat_data = cat_api.json()
    # st.write(cat_data)
    # st.table(cat_data)
    #st.dataframe(cat_data)

# if st.form_submit_button("Test"):
#         pressed =  ("Test Button pressed")
#         st.write(pressed)
#     # st.session_state.get(pressed)   


# if st.button("Clear Form"):
#     st.session_state.clear()



# # Button with a key and different type
# if st.button("Reset Counter", key="reset_button", type="primary"):
#     st.session_state.counter = 0
#     st.write("Counter reset!")