import json
import streamlit as st
from pathlib import Path
import nivo_chart as nc

## The streamlit_elements library only works in Python 3.11.9 kernel.
## import streamlit_elements
from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

st.set_page_config(layout="wide")

st.title("This code partly from original streamlit code Day27 (Day2700.py), but was revised")
st.subheader("Before this code, json data was created by Day2701_jsondata.py")

with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
    st.write("---")

    # Define URL for media player.
    media_url = st.text_input("Media URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")

# json data created by Day2701_jsondata.py and save in the same folder
if "data" not in st.session_state:
    st.session_state.data = Path("data.json").read_text()

# load json data into a dictionary
bump_chart = json.loads(st.session_state.data)

# create a nivo bump chart
# This code is from Day2702_OK.py
# code from Day2702_OK.py was copied from 
# in GitHub repo: https://github.com/aswan-heart-centre/streamlit_nivo
nc.nivo_chart(data=bump_chart["data"], layout=bump_chart["layout"], key="bump_chart")

