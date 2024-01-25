import openai

openai.api_key = "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"



content = input("Hi. How Can I help you?\n")

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=content,
    max_tokens=150  
)

print(response.choices[0].text.strip())
