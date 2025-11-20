import streamlit as st
import pandas as pd

st.title("🎈 My new app")
st.write("For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

x = st.slider('Slider')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
