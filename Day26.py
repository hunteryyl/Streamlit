import streamlit as st
import requests

st.title(" 🏀 Bored API app")

st.sidebar.header("Input")
selected_type = st.sidebar.selectbox("Select an activity type", 
                                     ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

## This is the original URL, but it is not working anymore
## suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'

## This is the corrected URL
suggested_activity_url = f'https://bored-api.appbrewery.com/filter?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
    with st.expander('About this app'):
        st.write('Are you bored? The **Bored API app** provides suggestions on activities taht you can do when you are bored. This app is powered by the Bored API.')
with c2:
    with st.expander('Json data'):
        st.write(suggested_activity) 

### These three lines of code were revised by myself to display the suggested activity in the app
length = len(suggested_activity)
selected_no = st.sidebar.selectbox("Select a number of activities to display", list(range(1,length)))
json_no = selected_no - 1 # This is the index of the activity in the json data

st.header('Suggested activity')
st.info(len(suggested_activity))
st.info(suggested_activity[json_no]['activity'])

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label='Number of participants', value = suggested_activity[json_no]['participants'], delta='')
with col2:
    st.metric(label='Type of activity', value=suggested_activity[json_no]['type'].capitalize(), delta='')
with col3:
    st.metric(label='Price', value=suggested_activity[json_no]['price'], delta='')
       