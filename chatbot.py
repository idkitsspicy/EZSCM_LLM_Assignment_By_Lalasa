import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model (v0.8.5+ supports this)
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

def ask_llm(question):
    prompt = f"""
You are a helpful assistant. Always answer by reasoning step-by-step.
If the question is a math problem like addition, subtraction, multiplication or division, say:
"I'm just a language model. You might have to use a calculator for that problem."

Question: {question}
Answer:
"""
    response = model.generate_content(prompt)
    return response.text.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        try:
            reply = ask_llm(user_input)
            print("Assistant:", reply)
        except Exception as e:
            print("❌ Error:", e)
