import yaml
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import google.generativeai as genai

current_script = Path(__file__).resolve()
config_file = current_script.parent.parent / 'config.yml'

with open(config_file, 'r') as file:
    CONFIG = yaml.safe_load(file)

# Step 1: Initialize ChromaDB in-memory (or persist to disk with Settings)
client = chromadb.Client()

# Step 2: Create or get collection
collection = client.get_or_create_collection(name="rag_docs")

# Step 3: Documents to store
documents = [
    'Football is the most viewed an played sport in the world',
    'CR7 is the best football player all time',
    'Messi es una chivita loca mimada'
]

# Step 4: Generate and add embeddings
embedder = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = embedder.encode(documents)

collection.add(
    documents=documents,
    embeddings=doc_embeddings.tolist(),
    ids=[f"doc{i}" for i in range(len(documents))]
)

# Step 5: User query
question = "Write about messi and cristiano ronaldo"
query_embedding = embedder.encode([question])[0]

# Step 6: Retrieve top-k documents
results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=2
)

retrieved_docs = results['documents'][0]

# Step 7: Generate answer with retrieved context
context = " ".join(retrieved_docs)
# prompt = f"Context: {context}\n\nQuestion: {question}\nAnswer:"

# qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
# response = qa_pipeline(question=question, context=context)


# Set up API key
genai.configure(api_key=CONFIG['google']['api_key'])

# Load Gemini model (free version = gemini-2.0-flash)
model = genai.GenerativeModel("gemini-2.0-flash")
prompt = f"""You are a helpful assistant.

Context:
{context}

Question: {question}
Answer:"""
# Run one-shot prompt
response = model.generate_content(prompt)

# Step 8: Display result
print(" Retrieved Docs:\n", retrieved_docs)
print("\n Answer:\n", response.text.strip())

