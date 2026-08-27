# Project 1 
Project 1 covers the anatomy of a single Gemini request -authentication, the model call, and the configuration that shapes what comes back

`hello.py` — Makes the smallest possible Gemini API call: load the key from .env, create a client, send one prompt, print the reply.

`configured.py` — Adds GenerateContentConfig to control how the model responds, using system_instruction to set standing behaviour, temperature to control randomness, and max_output_tokens to cap generation length.

`temperature_compare.py` — Runs the same prompt across temperatures 0.0 to 1.5 to show the difference between deterministic and varied output.

---

Basically any .py file that calls Gemini API needs

```python
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client()
MODEL = os.environ["GEMINI_MODEL"] #reads the model from the .env

```

---

## Inside the call:
**system_instruction** - It's separate from contents for a reason: it sets standing behaviour, while contents is the actual request.

**temperature**- is a number,  usually 0.0 to 2.0, that reshapes the probability distribution before choices are made
higher temperature (1.0-2.0) means unlikely tokens get a real chance of being selected
lower temperature (0.0-0.3) sharpens the distribution. high-probability tokens get pushed even higher

**max_output_tokens** - a hard limit on tokens, one token is approx 0.75 words

Example: 
```python
response = client.models.generate_content(
    model=MODEL,
    contents="Give me a name for a study app.",
    config=types.GenerateContentConfig(
        system_instruction="You are terse. Reply with the name only",
        temperature=0.0,
        max_output_tokens=200, #was originally 50 but 50 returned None
    ),
)
```

If you get a return of `None` when you run an API call file, try increasing `max_output_tokens`

