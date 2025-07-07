import numpy as np
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk
import numpy

# Download te punkt tokenizer data
nltk.download('punkt_tab')

sentences_list = ['Football', 'soccer', 'apple', 'water']
print(sentences_list)

# tokenize sentences into words
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences_list]

print(tokenized_sentences)

# Train Word2vec model.
model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)
print(' model done')
# Get the word embedding for a specific word.
word_embedding = model.wv['soccer']
print('Word embedding done')
# Convert the numpy array to a string representation within an array.
embedding_string = np.array2string(word_embedding, separator=',', precision=6, suppress_small=True)

print(f"Word embedding: {embedding_string}")

