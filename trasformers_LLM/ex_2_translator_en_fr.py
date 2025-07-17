# Translator from English to French using transformers pipeline
from transformers import pipeline

translator = pipeline(task='translation_en_to_fr')

prompt = input('What do you want to say in french: ')

result = translator(prompt)
translation = result[0].get('translation_text')
print(f'Here is the translation to french {translation}')
