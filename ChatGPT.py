import openai  


def inputLines(prompt:str):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    return text


# Set up the OpenAI API client
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"
command = "Rephrase the following paragraph in the same paragraph's language,"
paragraph = inputLines('Write the text:\n')

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=command+paragraph,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
