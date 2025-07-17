import google.generativeai as genai
import streamlit as st


# add gemini api key
genai.configure()

model = genai.GenerativeModel('gemini-2.0-flash')

prompt = st.text_input('Enter your prompt')

if st.button('Generate content'):
    with st.spinner('Generation response'):
        response = model.generate_content(prompt)


    st.write(response['candidates'][0]['content']['parts'][0]['text'])