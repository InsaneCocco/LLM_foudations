from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import uuid

from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)
import os
import yaml
from pathlib import Path


config_file = Path(__file__).resolve().parent.parent / 'config.yml'
with open(config_file, 'r') as file:
    CONFIG = yaml.safe_load(file)



# STEP 1: Set API Key
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = CONFIG['google']['api_key']
# Replace with your actual API key

# STEP 2: Load website content using WebBaseLoader
url = "https://docs.langchain.com/docs"  # You can change this to any public URL
loader = WebBaseLoader(url)
documents = loader.load()

# STEP 3: Split into chunks
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

# STEP 4: Initialize Google Gemini Embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# STEP 5: Create FAISS vector store
vectorstore = FAISS.from_documents(docs, embeddings)

# STEP 6: Initialize Gemini LLM
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
# Define the function that calls the model
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    # We return a list, because this will get added to the existing list
    return {"messages": response}


# Define the two nodes we will cycle between
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)


# Adding memory is straight forward in langgraph!
memory = MemorySaver()

app = workflow.compile(
    checkpointer=memory
)

# This enables a single application to manage conversations among multiple users.
thread_id = uuid.uuid4()
config = {"configurable": {"thread_id": thread_id}}


input_message = HumanMessage(content="Hi i am muderfkr")
for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
    event["messages"][-1].pretty_print()

# Here, let's confirm that the AI remembers our name!
input_message = HumanMessage(content="what am i?")
for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
    event["messages"][-1].pretty_print()