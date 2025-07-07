from sentence_transformers import SentenceTransformer
import numpy as np

# Latter connect the pdf to sentence here.
sentences = ['This is a sentence example', 'Street tacos are the best' ]

# Look in hugging face for the options.
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

embeddings = model.encode(sentences=sentences)

for sentence, embedding in zip(sentences, embeddings):
    embedding_array_string = '['+','.join(map(str, embedding)) + ']'
    print(embedding_array_string)