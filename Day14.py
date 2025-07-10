import streamlit as st
import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport ### upgrade pip
from streamlit_pandas_profiling import st_profile_report

st.header("'streamlit_pandas_profiling'")

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = df.profile_report()
st_profile_report(pr)