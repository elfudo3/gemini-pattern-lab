import os
from dotenv import load_dotenv
from google import genai 

load_dotenv()

client = genai.Client()
MODEL = os.environ["GEMINI_MODEL"]

#SDK's chats object handles memory bookkeeping 
chat = client.chats.create(model=MODEL)

response = chat.send_message("Mu name is Fudo and I'm studying the Gemini API for the Google AI Hackathon")
print(response.text)
#print(response.usage_metadata)

#when asked for my name, due to the `chats` object, the LLM should have stored the info about me 
response = chat.send_message("What's my name?")
print(response.text)
#print(response.usage_metadata)