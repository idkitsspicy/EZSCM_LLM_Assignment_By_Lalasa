# calculator_tool.py

import re

number_map = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19,
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
}

def word_to_number(word):
    word = word.lower().strip()
    if word in number_map:
        return number_map[word]
    if '-' in word:
        parts = word.split('-')
        return sum(number_map.get(p, 0) for p in parts)
    return None

def extract_numbers(text):
    words = text.lower().split()
    numbers = []
    for word in words:
        if word.isdigit():
            numbers.append(int(word))
        elif word_to_number(word) is not None:
            numbers.append(word_to_number(word))
    return numbers

def calculate(prompt):
    prompt = prompt.lower()
    numbers = extract_numbers(prompt)

    if len(numbers) < 2:
        return "Sorry, I couldn't find enough numbers to calculate."

    if any(op in prompt for op in ["add", "plus", "+"]):
        result = sum(numbers)
        return f"{' + '.join(map(str, numbers))} = {result}"

    elif any(op in prompt for op in ["multiply", "times", "*"]):
        result = 1
        for n in numbers:
            result *= n
        return f"{' × '.join(map(str, numbers))} = {result}"

    elif any(op in prompt for op in ["subtract", "minus", "-"]):
        result = numbers[0]
        for n in numbers[1:]:
            result -= n
        return f"{' - '.join(map(str, numbers))} = {result}"

    elif any(op in prompt for op in ["divide", "divided by", "/"]):
        result = numbers[0]
        try:
            for n in numbers[1:]:
                result /= n
            return f"{' ÷ '.join(map(str, numbers))} = {result:.2f}"
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

    return "Sorry, I can only handle addition, subtraction, multiplication, and division for now."
