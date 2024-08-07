import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# While loop to start and stop chatbot

while True:
    userInput = input("I am a terminator")
    # check for exit
    if userInput == "exit":
        break
    # further checks

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{userInput}",
            }
        ],
        model="gpt-3.5-turbo",
    )
    print(chat_completion)
