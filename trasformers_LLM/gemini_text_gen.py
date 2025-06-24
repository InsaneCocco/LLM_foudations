import google.generativeai as genai
import streamlit as st

st.title('Gemini example')
genai.configure(api_key='AIzaSyDyTcIv1gmxZ9Vu2ptJia1Fm-W7vQpIZXI')

model = genai.GenerativeModel('gemini-2.0-flash')

prompt = st.text_input('Enter your prompt')

if st.button('Generate content'):
    with st.spinner('Generation response'):
        response = model.generate_content(prompt)


    st.write(response['candidates'][0]['content']['parts'][0]['text'])