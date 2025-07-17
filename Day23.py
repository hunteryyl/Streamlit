##### This code has been modified by deepseek
##### The original code from the Streamlit 30 Days is not working. 

import streamlit as st

st.title('st.experimental_get_query_params')

with st.expander('About this app'):
    st.write("`st.experimental_get_query_params()` 可直接從瀏覽器網址列獲取查詢參數")

# 1. 教學說明 (修正URL拼寫錯誤)
st.header('1. Instructions')
st.markdown('''
在瀏覽器網址列後方追加參數：
`?firstname=Jack&surname=Beanstalk`
至基礎網址後方
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
            
最終完整網址應為：
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')

# 2. 顯示查詢參數
st.header('2. Contents of st.experimental_get_query_params')
query_params = st.experimental_get_query_params()
st.write(query_params)

# 3. 安全獲取參數值 (新增錯誤處理)
st.header('3. Retrieving and displaying information from the URL')

# 安全獲取參數值
firstname = query_params.get('firstname', [''])[0]  # 若無參數則返回空字串
surname = query_params.get('surname', [''])[0]

# 檢查參數是否存在
if firstname and surname:
    st.write(f'Hello **{firstname} {surname}**, how are you!')
else:
    st.warning("請在網址列追加參數：`?firstname=Jack&surname=Beanstalk`")