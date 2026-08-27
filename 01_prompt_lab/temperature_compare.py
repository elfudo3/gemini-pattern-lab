import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client()
MODEL = os.environ["GEMINI_MODEL"] #reads the model from the .env 

for temp in [0.0, 0.5, 1.0, 1.5]:
    response = client.models.generate_content(
        model=MODEL,
        contents="Give me a name for a study app",
        config=types.GenerateContentConfig(
            system_instruction="You are terse. Reply with the name only",
            temperature=temp,
            max_output_tokens=800,
        ),
    )
    print(f"temp={temp}: {response.text}")

