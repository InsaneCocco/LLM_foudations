import getpass
import os
from pathlib import Path
import yaml
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


config_file = Path(__file__).resolve().parent.parent / 'config.yml'
with open(config_file, 'r') as file:
    CONFIG = yaml.safe_load(file)

if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = CONFIG['google']['api_key']

model = init_chat_model('gemini-2.0-flash', model_provider='google_genai')
prompt = ChatPromptTemplate.from_template('give me a cheap idea oh {date}')

chain = prompt | model | StrOutputParser()

print(chain.invoke({'date' : 'romantic date'}))



