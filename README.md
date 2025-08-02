# EzSCM
Python Software Engineer Assignment: LLM + Agentic Thinking
Level-1 : LLM-Only Smart Assistant
This is a simple command-line chatbot built in Python that uses **Google Gemini 2.0 Flash API** to answer user questions in a structured, step-by-step format. The focus is on **prompt engineering** to ensure clarity, reasoning, and refusals for restricted tasks (like calculations).

---

##  Features

-  Uses `gemini-2.0-flash` from Google Generative AI
-  Step-by-step answers using prompt engineering
-  Refuses to perform math and redirects to calculator
-  Clean CLI interface
-  Logs interactions (included in `interactions_Level1.txt`)

---

##  Requirements

Install dependencies:
Your `requirements.txt` should contain:
python-dotenv
google-generativeai

1. Create a `.env` file in the root directory:
GEMINI_API_KEY=your_gemini_api_key_here

2. [Get your API key here](https://aistudio.google.com/app/apikey)

---

##  How to Run

python chatbot.py


Then type your questions, e.g.:

- What are the colors in a rainbow?
- Tell me why the sky is blue?
- What is 15 + 23? (will be refused)

---

## 🔒 Note

> Do not share your `.env` file or expose your API key in public repositories. Add `.env` to `.gitignore`.
