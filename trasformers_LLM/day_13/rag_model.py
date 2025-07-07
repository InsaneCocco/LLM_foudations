# Convert PDF to vectors
# - Extract heddings
# - Convert to vector
# - store into database

# Similarity search
import os
from pathlib import Path
import yaml

from pypdf import PdfReader
import chromadb
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

current_script = os.path.basename(__file__)

config_file = Path(__file__).resolve().parent.parent / 'config.yml'
with open(config_file, 'r') as file:
    CONFIG = yaml.safe_load(file)

client = chromadb.Client()
collection = client.get_or_create_collection(name='pdf_data')

embedder = SentenceTransformer("all-MiniLM-L6-v2")

files_list = [file for file in os.listdir('.') if file != current_script]
print(files_list)

text_in_docs = []

for file in files_list:
    try:
        reader = PdfReader(file)
        number_of_pages = len(reader.pages)
        print(f'Number of pages in file {file}: {number_of_pages}')
        # This is hardcoded for PDF that has only one page.
        page = reader.pages[0]
        text = page.extract_text()
        text_in_docs.append(text)
        print('End of page')

    except FileNotFoundError:
        print("Error: The file 'your_document.pdf' was not found.")


doc_embeddings = embedder.encode(text_in_docs)

collection.add(
    documents=text_in_docs,
    embeddings=doc_embeddings.tolist(),
    ids=[f'doc{i}' for i in range(len(text_in_docs))]
)

question = "Users face compatibility issues with their operating system."
query_embedding = embedder.encode([question])[0]

results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=2
)

retrieved_docs = results['documents'][0]
context = " ".join(retrieved_docs)

genai.configure(api_key=CONFIG['google']['api_key'])

model = genai.GenerativeModel("gemini-2.0-flash")
prompt = f"""You are a helpful assistant that will return the name of the file where the solution
information asked is in. 
example 1:
User prompt: Users report a lack of internet access despite a working connection
response: The searched issues are in: Troubleshooting Connectivity Issues

example 2:
user prompt: Users face compatibility issues with their operating system or other
installed software
response: The searched issues are in: Resolving Software Installation Failures

example 3:
user prompt: Users complain of not receiving expected emails
response: The searched issues are in: Fixing Email Delivery Issues

Context:
{context}

Question: {question}
Answer:"""

response = model.generate_content(prompt)

print(" Retrieved Docs:\n", retrieved_docs)
print("\n Answer:\n", response.text.strip())