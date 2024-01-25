import openai

openai.api_key = "OPENAI API KEY"

def main():
    prompt = input("Hey There!! How may I help you?")
    while True:
        print(get_api_response(prompt))
        prompt = input()
        

def get_api_response(prompt, temp = 1.0):
    if not prompt:
        return None
    
    try:
        response : dict =  openai.Completion.create(
            model = 'gpt-3.5-turbo-16k-0613',
            prompt = prompt,
            temperature = temp,
            max_tokens = 500,
            top_p = 1,
            frequency_penealty = 0,
            presence_penalty = 0.6,
            stop = [' Human:', ' AI:'])

        return response
    except Exception as e:
        print("ERROR", e)


if __name__ == "__main__":
    main()