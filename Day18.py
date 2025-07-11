import streamlit as st
import pandas as pd

st.title("st.file_uploader")

st.subheader("Input csv file")
uploaded_file = st.file_uploader("Choose a csv file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('DataFrame')
    st.write(df)
    st.subheader('Descriptive Statistics')
    st.write(df.describe())
else:
    st.info("Upload a csv file")
        
