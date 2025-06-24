from transformers import pipeline

generator = pipeline('text-generation')

generator('Hello, i am a language model', max_length=30, num_return_sequences=5)