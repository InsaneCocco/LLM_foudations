from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain.tools import Tool
import requests
import yaml
from pathlib import Path

config_file = Path(__file__).resolve().parent.parent / 'config.yml'
with open(config_file, 'r') as file:
    CONFIG = yaml.safe_load(file)

if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = CONFIG['google']['api_key']
os.environ["WEATHER_API_KEY"] = CONFIG['weather']['api_key']

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)


# Tool to fetch current weather using WeatherAPI
def get_weather(city: str) -> str:
    """Fetch current weather for a given city using WeatherAPI."""
    api_key = os.environ["WEATHER_API_KEY"]
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        condition = data["current"]["condition"]["text"]
        temp_c = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        return f"The current weather in {city} is {condition}, temperature: {temp_c}°C, humidity: {humidity}%."
    else:
        return f"Could not fetch weather for {city}. Please check the city name."


weather_tool = Tool(
    name="WeatherTool",
    func=get_weather,
    description="Useful for getting current weather. Input should be a city name like 'London' or 'New York'."
)

# Initialize the agent with the weather tool
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType

tools = [weather_tool]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run the agent with a weather query
response = agent.invoke("What is the weather like in Argentina today?")
print(response)
