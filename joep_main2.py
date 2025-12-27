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

# Create a form within the sidebar
with st.sidebar.form(key='sidebar_form'):
    # Input widgets inside the form
    st.title("Welcome to Optionator!")

    # selected = st.selectbox("Main Menu", ["Dashboard", "Reports", "Settings", "About"])
    # match selected:
    #     case "Dashboard":
    #         selected == "Dashboard"
    #         st.write("Dashboard")
    #     case "Reports":
    #         st.write("Reports")
    
# if selected == "Dashboard":
#     st.title("Welcome to Optionator")
# elif selected == "Reports":
#     st.write("View Reports")
# elif selected == "Settings":
#     st.write("View Settings")
# elif selected == "About":
#     st.write("About Optionator")
#     st.text("Optionator assists traders with reccomending profitable calls & puts." \
#     "It uses AI technolgy to assit option traders to pick potentially profitiable startegies")


    #selected = st.selectbox("Main Menu", ["Dashboard", "Reports", "Settings", "About"])
    # 
    st.sidebar.divider()
    stock_symbol = st.text_input("Enter Stock Symbol to pull options chain and click Enter:")
   
    # The submit button for the form
    submit_button = st.form_submit_button('Submit')
    get_api_data = st.form_submit_button("Get API data")
    clear_main_form = st.form_submit_button("Clear Main")

    #get_options_data = st.form_submit_button("Get Options Data")

# Main content area

st.write("Enter details in the sidebar and click submit.")

# Check if the form was submitted
if submit_button:
    st.success(f"Symbol Submitted!  {stock_symbol}")
    # You can now use 'name' and 'age' to update your main app logic
else:
    st.info("Waiting for form submission...")

iss_now_api = requests.get("http://api.open-notify.org/iss-now.json")
#print(iss_now_api.json())    write data to console for testing

cat_api = requests.get("https://catfact.ninja/fact")
#print(cat_api.json())  write data to console for testing

textbox = st.text_input("Enter stock symbol:")
st.write(textbox)


if get_api_data:    
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

# if st.form_submit_button("Test"):
#         pressed =  ("Test Button pressed")
#         st.write(pressed)
#     # st.session_state.get(pressed)   


# if st.button("Clear Form"):
#     st.session_state.clear()

if clear_main_form:
    st.session_state.clear()
    
# # Button with a key and different type
# if st.button("Reset Counter", key="reset_button", type="primary"):
#     st.session_state.counter = 0
#     st.write("Counter reset!")