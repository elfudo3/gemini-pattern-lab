# gemini-pattern-lab
Six bite sized Python projects for learning Gemini API patterns.
Specifically made in preparation Google AI Hackathon 2026 Dublin!! 

<img width="346" height="218" alt="image" src="https://github.com/user-attachments/assets/24e07700-79f1-4ba1-a118-34979a8501cb" />


---

## Projects

**Project 1: Prompt Lab** — The anatomy of a single Gemini request — authentication, the model call, and the configuration that shapes what comes back.

**Project 2: Study Coach** — Multi-turn conversations and chat history.

**Project 3: Streaming Demo** — Streaming responses — printing the reply token by token as it arrives instead of waiting for the whole thing.

**Project 4: Idea Extractor** — Structured output — getting validated Python objects back instead of a blob of text.

**Project 5: Tool Assistant** — Function calling — letting the model request that my Python functions be run.

**Project 6: Document Inspector** — Multimodal input — sending images and PDFs alongside a text prompt.

---

## How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/elfudo3/gemini-pattern-lab.git
   cd gemini-pattern-lab
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   - Copy `.env.example` to `.env`
   - Add your Gemini API key and model name:
     ```
     GEMINI_API_KEY=your_api_key_here
     GEMINI_MODEL=gemini-2.0-flash
     ```

5. **Run a project**
   ```bash
   cd 01_prompt_lab
   python hello.py
   ```

Each time you return to work, activate the virtual environment with `source .venv/bin/activate`
