import streamlit as st

st.header("st.checkbox")

st.write("What wuold you like to do?")

icecream = st.checkbox("Ice Cream")
coffee = st.checkbox("Coffee")
cola = st.checkbox("Cola")

if icecream:
    st.write("Great! Here's some more ice cream 🍦")

if coffee:
    st.write("Great! Here's some more coffer ☕")

if cola:
    st.write("Great! Here's we go 🥤")