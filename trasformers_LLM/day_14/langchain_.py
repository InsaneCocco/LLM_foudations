import getpass
import os
from pathlib import Path
import yaml
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate


config_file = Path(__file__).resolve().parent.parent / 'config.yml'
with open(config_file, 'r') as file:
    CONFIG = yaml.safe_load(file)

if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = CONFIG['google']['api_key']

model = init_chat_model('gemini-2.0-flash', model_provider='google_genai')
example_prompt = PromptTemplate.from_template('Generate a energetic name for company {company_name}')

response = example_prompt.invoke({'company_name': 'sonora dinamita'})
print(response)

