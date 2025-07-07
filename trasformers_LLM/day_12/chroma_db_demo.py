import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name='rag_db')

collection.add(
    ids=["id_f", "id_s"],
    documents=[
        "Football",
        "soccer"
    ]
)

results = collection.query(
    query_texts=["This is a query document about hawaii"], # Chroma will embed this for you
    n_results=2 # how many results to return
)
print(results)
