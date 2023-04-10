import openai

openai.api_key ="your api token"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human","AI"]
    )

    return response.choices[0].text

while True:
    prompt = input("You: ")
    #prompt = "\nAI:"
    response = generate_response(prompt)
    print("AI: " + response)