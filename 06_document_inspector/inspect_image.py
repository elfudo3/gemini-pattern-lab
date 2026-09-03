import os
from pathlib import Path 

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()
MODEL = os.environ["GEMINI_MODEL"]

# Path(__file__).parent = the folder this script lives in
# so the script works regardles of which directory we run it from
HERE = Path(__file__).parent 

#read the images in raw binary mode
image_bytes = (HERE / "samples" / "photo.jpg").read_bytes()

response = client.models.generate_content(
    model=MODEL,
    #contents is a list here: one file part, one text part
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
        "Describe what you see in this image in two sentences.",
    ],
)

print(response.text)
print("tokens in:", response.usage_metadata.prompt_token_count)