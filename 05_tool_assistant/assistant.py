import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

from tools import get_weather, calculate

load_dotenv()
client = genai.Client()
MODEL = os.environ["GEMINI_MODEL"]

#passing the actual Python functions turns on automatic function calling
chat = client.chats.create(
    model=MODEL,
    config=types.GenerateContentConfig(
        tools=[get_weather, calculate],
    ),
)

response = chat.send_message("Whats the weather in Dublin? also whats 23 * 47")
print(response.text)