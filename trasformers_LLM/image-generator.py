# import google.generativeai as genai
#
# openAI apikey
# genai.configure(api_key=)
#
# model = genai.GenerativeModel('gemini-2.0-flash')
#
# response = model.generate_content('Hey, how are you?')
#
# print(response)

import requests
import streamlit as st

# Streamlit app to generate images using Azure OpenAI DALL-E 3
st.title("Azure OpenAI DALL-E 3 Image Generation")
st.write("This app allows you to generate images using the Azure OpenAI DALL-E 3 model. Enter a prompt to create an image.")
# Set up Azure OpenAI API details

# openAI apikey
# Replace with your actual details
ENDPOINT_URL = "https://.openai.azure.com"
API_KEY = ""
DEPLOYMENT_NAME = "dalle-3"
API_VERSION = "2024-02-01"

# ADD PROPMT INPUT
prompt = st.text_input("Enter a prompt to generate an image:", key="prompt_input")
# Prompt input
#  = input("Enter a prompt to generate an image: ")

# Compose request
url = f"{ENDPOINT_URL}/openai/deployments/{DEPLOYMENT_NAME}/images/generations?api-version={API_VERSION}"
headers = {
    "api-key": API_KEY,
    "Content-Type": "application/json"
}
body = {
    "prompt": prompt,
    "n": 1,
    "size": "1024x1024"
}

# add button to generate image
if st.button("Generate Image"):
    # Make the request
    response = requests.post(url, headers=headers, json=body)
    # Handle response
    if response.status_code == 200:
        data = response.json()
        st.image(data["data"][0]["url"], caption="Generated Image")

# # Make the request
# response = requests.post(url, headers=headers, json=body)

# # Handle response
# if response.status_code == 200:
#     data = response.json()
#     print("\nRevised Prompt:", data["data"][0]["revised_prompt"])
#     print("Image URL:", data["data"][0]["url"])
# else:
#     print("\nError:", response.status_code)
#     print(response.text)

