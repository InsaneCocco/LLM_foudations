from pathlib import Path
import yaml
import os

from openai import OpenAI
import streamlit as st


config_file = Path(__file__).resolve().parent / 'config.yml'
with open(config_file, 'r') as file:
    CONFIG = yaml.safe_load(file)

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = CONFIG['openai']['api_key']
client = OpenAI(api_key="KEY")


st.title("AI Assistant")
st.write("Improve your language skills with AI.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are a helpful language tutor. Help the user practice a target language with conversation, vocabulary, grammar, and pronunciation exercises."}
    ]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "system",
            "content": "You are a helpful language tutor. Help the user practice a target language with conversation, vocabulary, grammar, and pronunciation exercises."
        }
    ]

name = st.text_input('What is your name?')


user_input = st.text_input(f"{name}:", "")

if st.button("Send") and user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Llamada a la API OpenAI (nuevo SDK)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=st.session_state.chat_history,
        temperature=0.7
    )
    reply = response.choices[0].message.content

    st.session_state.chat_history.append({"role": "assistant", "content": reply})

# Mostrar conversación
for msg in st.session_state.chat_history[1:]:
    st.markdown(f"**{msg['role'].capitalize()}**: {msg['content']}")
