from transformers import pipeline

temperature = 0.5
top_p = 0.9
max_length = 100

generation = pipeline('text-generation')

prompt = ('''I want to analize the sentiment of phrases, for each phrase tag it as negative or positive. 
Rewrite the sentence you are analizing and add the sentiment: 
example prompts and responses:
This new technology is groundbreaking and will revolutionize the industry.
Sentiment: Positive
Finding a solution to the problem was more difficult than I anticipated.
Sentiment: Negative

Do not add any other phrase. Just use what i give you.
phrases to analize:
I love spending time with my family and friends.
Sentiment:
The weather is terrible today, and everything went wrong
Sentiment:
The concert last night was amazing! The performers were outstanding
Sentiment:
''')

output = generation(
    prompt,
    max_length=max_length,
    temperature=temperature,
    top_p=top_p
)

print(output[0]['generated_text'])