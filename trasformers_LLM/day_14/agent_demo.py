from pathlib import Path
import yaml
import os

from langchain.agents import initialize_agent, load_tools
from langchain.agents.agent_types import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI

config_file = Path(__file__).resolve().parent.parent / 'config.yml'
with open(config_file, 'r') as file:
    CONFIG = yaml.safe_load(file)

if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = CONFIG['google']['api_key']

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

tools = load_tools(['llm-math'], llm=model)

agent = initialize_agent(
    tools=tools,
    llm=model,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

response = agent.run(' what is 65 divided by 780')
print(response)