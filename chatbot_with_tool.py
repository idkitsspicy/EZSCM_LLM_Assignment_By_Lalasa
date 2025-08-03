# chatbot_with_tool.py

import os
from dotenv import load_dotenv
import google.generativeai as genai
from calculator_tool import calculate

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

# Keywords to check for math intent
math_keywords = [
    "add", "plus", "+", "sum",
    "subtract", "minus", "-",
    "multiply", "times", "*",
    "divide", "divided", "/"
]

def detect_math_task(prompt):
    """Detect if the prompt is a math operation."""
    prompt = prompt.lower()
    return any(word in prompt for word in math_keywords)

def ask_gemini(prompt):
    """Send a general prompt to Gemini."""
    response = model.generate_content(prompt)
    return response.text.strip()

def chat():
    print("Assistant is ready. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.strip().lower() == "exit":
            print("👋 Goodbye!")
            break

        if detect_math_task(user_input):
            if "and also" in user_input or "," in user_input or "then" in user_input:
                print("Assistant: Sorry, I can only handle one task at a time.")
            else:
                result = calculate(user_input)
                print(f"Assistant (via calculator): {result}")
        else:
            response = ask_gemini(user_input)
            print(f"Assistant (via LLM): {response}")

if __name__ == "__main__":
    chat()
