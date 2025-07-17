# Use the Transformer pipeline for Sentiment Analysis using the default model

from transformers import pipeline

analyzer = pipeline(task='sentiment-analysis')
prompt = input('Tell me the phrase to analyze: ')

result = analyzer(prompt)
sentiment = result[0].get('label')
print(f'The sentiment is: {sentiment}')

