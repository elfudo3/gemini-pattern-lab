import os
from dotenv import load_dotenv
from google import genai 
from google.genai import types

load_dotenv()

client = genai.Client()
MODEL = os.environ["GEMINI_MODEL"]

#we are seeding the conversation by passing the existing history to create
chat = client.chats.create(
    model=MODEL,
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are a study coach for a CS student. Ask one question at a "
            "time. Keep replies under three sentences."
        ),
    ),
)

while True:
    user_input = input("You: ")
    if user_input.lower() in ("quit", "exit"):
        break
    response = chat.send_message(user_input)
    print(f"Coach: {response.text} \n")


