from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

while True:

    prompt = input("\nIntroduce una pregunta: ")

    if prompt == "exit":
        break

    completion = openai.Completion.create(engine="text-davinci-003",
                                        prompt=prompt,
                                        n=1,
                                        max_tokens=4000  #Numero máximo de palabras de la respuesta
                                        )

    print(completion.choices[0].text)