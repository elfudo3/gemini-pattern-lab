import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()
MODEL = os.environ["GEMINI_MODEL"]

stream = client.models.generate_content_stream(
    model=MODEL,
    contents="Explain what a REST API, & FAST API is in three short paragraphs",
)

for chunk in stream:
    if chunk.text: 
        print(chunk.text, end="", flush=True)

print()

# This is genuinely really boring though so Im skipping to project 4