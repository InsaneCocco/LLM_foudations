from langchain_text_splitters import RecursiveCharacterTextSplitter

with open('/Users/cocco/Desktop/projects/LLMs/trasformers_LLM/day_14/langc_prompt.txt') as f:
    state_of_the_union = f.read()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)

texts = text_splitter.create_documents([state_of_the_union])

for i, text in enumerate(texts):
    print(f'Chunk {i}\n')
    print(text.page_content)
    print('-'*40)
    print(f'Metadata: {text.metadata}\n')