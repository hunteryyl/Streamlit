import streamlit as st
from datetime import time, datetime

st.header("st.slider")

### Example 1
st.subheader("Slider")
age = st.slider("How old are you?", 0, 90, (18, 30))
st.write("I am ", age, "years old.")

### Example 2
st.subheader("Range Slider")

values = st.slider("Select a range of values", 
                   0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)

### Example 3
st.subheader("Range Time Slider")

appointment = st.slider(
    "Schedule your appointment:",
    value = (time(11,30), time(12,45)))
st.write("You're scheduled for:", appointment)

### Example 4
st.subheader("Datetime Slider")

start_time = st.slider(
    "When do you start?",
    value = datetime(2025, 7, 9, 16, 12), 
    format = "MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

### Example 5
start_color, end_color = st.select_slider(
    "Select a range of color wavelength",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
    value=("blue", "green"),
)
st.write("You selected wavelengths between", start_color, "and", end_color)

