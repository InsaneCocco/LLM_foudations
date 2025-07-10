import json

from langchain_community.document_loaders import PyPDFLoader

file_path = ('/Users/cocco/Desktop/projects/LLMs/trasformers_LLM/day_14/JARDINES.pdf')
loader = PyPDFLoader(file_path)

pages = []

for page in loader.lazy_load():
    pages.append(page)

print(f'{json.dumps(pages[0].metadata, indent=4)}\n')
print(pages[0].page_content)