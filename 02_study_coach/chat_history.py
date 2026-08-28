import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()
MODEL = os.environ["GEMINI_MODEL"]

#SDK's chat object used to store memory
chat = client.chats.create(model=MODEL)

chat.send_message("My name is Fudo.")
chat.send_message("Im learning the Gemini API")

for message in chat.get_history():
    print(f"{message.role}: {message.parts[0].text}")

# on this output we see the entire conversation, the users entries and the models entries
# the entire chat gets sent to the model every time a new message is sent for conversation history 

