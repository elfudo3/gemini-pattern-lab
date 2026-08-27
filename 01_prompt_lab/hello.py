import os
from dotenv import load_dotenv
from google import genai

load_dotenv() #reads .env and puts GEMINI_API_KEY into the environment
#genai.Client() WAS MADE BY GOOGLE TO READ GEMINI_API_KEY 
client = genai.Client()  #SDK (software development kit) picks the key up from there automatically
MODEL = os.environ["GEMINI_MODEL"] #reads the model from the .env

response = client.models.generate_content(
    model=MODEL,
    contents="Explain what a virtual environment is in two sentences.", #prompt
)

print(response.text)