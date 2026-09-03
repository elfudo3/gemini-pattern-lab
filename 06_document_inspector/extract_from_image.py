import os
from pathlib import Path 

from dotenv import load_dotenv
from google import genai
from google.genai import types


from pydantic import BaseModel, Field

load_dotenv()
client = genai.Client()
MODEL = os.environ["GEMINI_MODEL"]


class Animal(BaseModel):
    type: str
    breed: str
    colour: float
    background: str

HERE = Path(__file__).parent

image_bytes = (HERE / "samples" / "photo.jpg").read_bytes()

response = client.models.generate_content(
    model=MODEL,
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
        "Extract the receipt details.",
    ],
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Animal,
        temperature=0.0,
    ),
)

receipt = response.parsed
print(receipt.total)