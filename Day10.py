import streamlit as st
st.header("st.selectbox")

option = st.selectbox(
    "What is your favorite color?",
    ("Blue", "Red", "Green", "Yellow", "Purple", "Orange", "Pink", "Black", "White")
)
st.write("Your favorite color is ", option)
