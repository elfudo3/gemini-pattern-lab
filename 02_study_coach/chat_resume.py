import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

MODEL = os.environ["GEMINI_MODEL"]

history = [
    types.Content(
        role="user",
        parts=[types.Part.from_text(text="My name is Fudo.")],
    ),
    types.Content(
        role="model",
        parts=[types.Part.from_text(text="Nice to meet you Fudo.")],
    ),
]

#storing the history  
chat = client.chats.create(model=MODEL, history=history)

response = chat.send_message("What's my name?")
print(response.text)
