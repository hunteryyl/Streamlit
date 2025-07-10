import streamlit as st

st.title("st.secrets")

st.write(st.secrets['message'])

### before running this code, make sure to 
### create a file nmaed 'secrets.toml' 
### in the .streamlit folder in the root directory
