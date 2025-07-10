import getpass
import os
from pathlib import Path
import yaml
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter


config_file = Path(__file__).resolve().parent.parent / 'config.yml'
with open(config_file, 'r') as file:
    CONFIG = yaml.safe_load(file)

if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = CONFIG['google']['api_key']

embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

loader = TextLoader('/Users/cocco/Desktop/projects/LLMs/trasformers_LLM/day_14/langc_prompt.txt')

documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
vectorstore = FAISS.from_documents(texts, embeddings)

query = 'what is a promt template?'

docs = vectorstore.similarity_search(query)
print(docs[0].page_content)