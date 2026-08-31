import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

#Our own data shape, defined in models.py in the same folder
from models import Idea

load_dotenv()

client = genai.Client()
MODEL = os.environ["GEMINI_MODEL"]

#reads from the file 'with' makes sure the file is closed again even if something goes wrong inside the block
#f.read() pulls the whole file in as one string
with open("04_idea_extractor/sample_input.txt") as f:
    notes = f.read()

response = client.models.generate_content(
    model=MODEL,
    contents=f"Extract the action items from these notes:\n\n{notes}",
    config=types.GenerateContentConfig(
        # 1. return JSON rather than prose.
        response_mime_type="application/json",
        # 2. and specifically JSON matching this shape. 
        response_schema=list[Idea],
        # extraction should be repeatable, so we want the least random settings available
        temperature=0.0,
        #room for the model to think before it answers
        max_output_tokens=2000,
    )
)

# .parsed: the SDK takes the JSON, checks it against our Idea class, and hands back a real Python Object
# response.text still holds the raw JSON string if necessary
ideas = response.parsed

for idea in ideas:
    print(f"[{idea.priority}] {idea.title} - {idea.owner or 'unassigned'}")
    print(f"    {idea.description}\n")

# Useful when something goes wrong: STOP means the model finished
# normally, MAX_TOKENS means it was cut off (which usually shows up as a
# JSON parsing error above).
print("finish_reason:", response.candidates[0].finish_reason)
print("tokens in:", response.usage_metadata.prompt_token_count)
print("tokens out:", response.usage_metadata.candidates_token_count)