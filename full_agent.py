# ✅ full_agent.py (Updated for better parsing and integration)

import os
import json
import string
from dotenv import load_dotenv
import google.generativeai as genai
from calculator_tool import calculate, word_to_number
from translator_tool import translate_text

# Load API key and setup model
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

number_map = {
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
}

def is_number_word(token):
    token = token.lower().strip()
    if token in number_map:
        return True
    if '-' in token:
        parts = token.split('-')
        return all(p in number_map for p in parts)
    return False

def is_number(word):
    return word.isdigit() or is_number_word(word)

def ask_llm(prompt):
    response = model.generate_content(prompt)
    return response.text.strip()

def parse_task(prompt):
    prompt = prompt.lower().strip()
    prompt = prompt.replace(", then", " then")

    parts = []
    current = ""
    in_quotes = False

    for char in prompt:
        if char == "'":
            in_quotes = not in_quotes
        if not in_quotes and char in string.punctuation and char not in ["'", "+", "*", "-", "/"]:
            continue
        current += char

    words = current.split()
    subtasks = []
    current = []

    i = 0
    while i < len(words):
        word = words[i]

        if word == "then":
            if current:
                subtasks.append(" ".join(current))
                current = []
        elif word == "and":
            prev = words[i - 1] if i > 0 else ""
            next = words[i + 1] if i + 1 < len(words) else ""
            if is_number(prev) and is_number(next):
                current.append(word)
            else:
                if current:
                    subtasks.append(" ".join(current))
                    current = []
        else:
            current.append(word)
        i += 1

    if current:
        subtasks.append(" ".join(current))

    # Recombine if sentence likely broken mid-LLM query
    if len(subtasks) > 1 and not any(tool in subtasks[-1] for tool in ["translate", "add", "multiply", "divide", "subtract"]):
        subtasks[-2] += " " + subtasks[-1]
        subtasks.pop()

    return subtasks

def handle_subtask(task):
    if "translate" in task and "into" in task:
        import re
        match = re.search(r"'(.*?)'", task)
        lang = re.search(r"into (\w+)", task)

        if match and lang:
            phrase = match.group(1)
            target = lang.group(1)
            translated = translate_text(phrase, target)
            return f"(Translator) {translated}"
        else:
            return "(Translator) Format should be: Translate 'text' into language"

    elif any(op in task for op in ["add", "plus", "multiply", "times", "+", "*", "subtract", "minus", "-", "divide", "divided by", "/"]):
        return f"(Calculator) {calculate(task)}"

    else:
        return f"(LLM) {ask_llm(task)}"

def chat():
    print("\n🤖 Agent is ready. Type 'exit' to quit.\n")
    history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("\n👋 Agent shutting down.")
            break

        subtasks = parse_task(user_input)
        responses = []

        for subtask in subtasks:
            result = handle_subtask(subtask)
            responses.append(f"> {subtask}\n{result}")

        combined = "\n\n".join(responses)
        print(f"\n{combined}\n")

        history.append({
            "user": user_input,
            "agent_response": combined
        })

    

if __name__ == "__main__":
    chat()
