from transformers import pipeline

temperature = 0.5
top_p = 0.9
max_length = 100

generation = pipeline('text-generation')

prompt = ('''You are a translator
''')

output = generation(
    prompt,
    max_length=max_length,
    temperature=temperature,
    top_p=top_p
)

print(output[0]['generated_text'])