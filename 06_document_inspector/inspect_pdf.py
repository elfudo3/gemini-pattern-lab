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

pdf_bytes = (HERE / "samples" / "doc.pdf").read_bytes()

response = client.models.generate_content(
    model=MODEL,
    contents=[
        types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf"),
        "Summarise the key points of this document as a bulleted list"
    ],
)

print(response.text)
print("tokens in:", response.usage_metadata.prompt_token_count)
