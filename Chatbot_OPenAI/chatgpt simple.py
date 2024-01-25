import openai

openai.api_key = "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"



content = input("Hi. How Can I help you?\n")

completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = [{"role":"user", "content":content}])

print(completion.choices[0].text.strip())
