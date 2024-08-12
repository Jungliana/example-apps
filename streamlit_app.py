import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime


st.header("Streamlit example app")
st.subheader("Button")
st.write("This is a button:")
button_clicks = 0

if st.button("Button"):
    button_clicks += 1
st.write("Clicks: ", button_clicks)

st.divider()
st.subheader("Slider")
st.write("This is a slider:")
slider_value = st.slider("Slider", 0, 100)
st.write("Slider value: ", slider_value)

start_time = st.slider(
    "Date slider:", value=datetime(2020, 1, 1), format="DD-MM-YY"
)
st.write("Slider value:", start_time)

st.divider()
st.subheader("Chart")
chart_data = pd.DataFrame(
     np.random.randn(30, 3),
     columns=['Column 1', 'Column 2', 'Column 3'])

st.line_chart(chart_data)
