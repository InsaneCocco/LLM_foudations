from transformers import pipeline

temperature = 0.5
top_p = 0.9
max_length = 100

generation = pipeline('text-generation')

user = input('Hey! I am your tutor. What do you want to talk about today?: ')

prompt = (f'''You are a tutor, you should engage in
conversations with users, ask probing questions, and guide them towards a deeper understanding
of a specific topic or problem. should not provide direct answers; instead, it should
encourage critical thinking and self-discovery.
User input: {user}
''')

output = generation(
    prompt,
    max_length=max_length,
    temperature=temperature,
    top_p=top_p
)

print(output[0]['generated_text'])