

---

````markdown
# 🧠 Smart Assistant Project

A multi-level intelligent assistant powered by LLMs, tools, and reasoning capabilities. This assistant evolves across three levels:

- ✅ Level 1: LLM-only basic responses  
- ✅ Level 2: LLM + Calculator Tool integration  
- ✅ Level 3: Agentic AI with memory + tool usage + multi-step reasoning  

---

## 📁 Levels Overview

### 🔹 Level 1: Easy (LLM-Only)
- Direct answers using LLM (Gemini or OpenAI)
- No tools or memory  
- **Example:**  
  **Input:** "What is the capital of France?"  
  **Output:** "Paris"  

  **Input:** "What is 42 times 2?"  
  **Output:** "I'm just a language model. You might have to use a calculator for that problem."  

---

### 🔹 Level 2: Medium (LLM + Calculator Tool)
- Arithmetic from natural language prompts  
- Uses `calculator_tool.py` for operations  
- Cannot handle multiple tasks and politely declines  
- **Example:**  
  **Input:** "Add twenty-three and 9"  
  **Output:** `23 + 9 = 32`  

  **Input:** "Add twenty-three and 9 then tell me capital of Japan"  
  **Output:** "Assistant: Sorry, I can only handle one task at a time."

---

### 🔹 Level 3: Hard (Agentic AI with Memory + Tools)
- Multi-step reasoning  
- Memory and tools like calculator and translator  
- Agent breaks down and executes tasks with history tracking  
- Handles multiple tasks  
- **Example:**  
  **Input:** "Translate twenty-three plus forty to German and calculate it"  
  **Output:**  
  1. Translation: `"dreiundzwanzig plus vierzig"`  
  2. Calculation: `23 + 40 = 63`

---

## ⚙️ How to Run the Project

### 1. 🧩 Install Dependencies

```bash
pip install -r requirements.txt
````

### 2. 🔑 Set up Environment Variables

Create a `.env` file and add your own API key before running the files:

```bash
GEMINI_API_KEY=your_api_key_here
```

### 3. ▶️ Run a Level

#### Level 1 (LLM-only):

```bash
python chatbot.py
```

#### Level 2 (LLM + Calculator Tool):

```bash
python chatbot_with_tool.py
```

#### Level 3 (Agent with Tools + Memory):

```bash
python full_agent.py
```

---

## 🔧 Files & Modules

| File                   | Description                                                    |
| ---------------------- | -------------------------------------------------------------- |
| `calculator_tool.py`   | Natural language calculator (supports digits and word-numbers) |
| `translator_tool.py`   | Language translator (for Level 3)                              |
| `full_agent.py`        | Core agent logic for Level 3                                   |
| `chatbot.py`           | LLM-only execution script (Level 1)                            |
| `chatbot_with_tool.py` | Integration of LLM with calculator (Level 2)                   |
| `.env`                 | Gemini API key                                                 |

## Built-in modules to be installed(requirements.txt) :
``` bash
pip install python-dotenv google-generativeai
```
## Folder Structure 
```bash
smart-assistant/
│
├── level1/
│   ├── chatbot.py                   # Level 1 assistant (LLM-only)
│   └── interactions_Level1.txt      # Sample prompts for Level 1
│
├── level2/
│   ├── chatbot_with_tool.py         # Level 2 assistant (LLM + calculator)
│   ├── calculator_tool.py           # Natural language arithmetic parser
│   └── interactions_Level2.txt      # Sample prompts for Level 2
│
├── level3/
│   ├── full_agent.py                # Level 3 agent (tools + memory)
│   ├── calculator_tool.py           # Shared calculator tool
│   ├── translator_tool.py           # Translator tool for multilingual input
│   └── interactions_Level3.txt      # Sample prompts for Level 3
│
├── .gitignore                       # Contains `.env` exclusion
├── .env                             # Your API key (not pushed to GitHub)
├── requirements.txt                 # Python dependencies
└── README.md                        # Project overview and instructions
```

---

## 🔢 Example Calculator Inputs

```
"Add forty and 60"         → 40 + 60 = 100  
"Multiply seven and nine"  → 7 × 9 = 63  
"Divide 100 by five"       → 100 ÷ 5 = 20.00  
"Subtract 10 from twenty"  → 20 - 10 = 10  
```

---

## 📝 Notes

* Tested with Python 3.8+
* LLM used: Gemini 2.0 Flash (via API)
* For Level 3, ensure both calculator and translator tools are imported properly in `full_agent.py`.

---

## 👩‍💻 Author

Smart Assistant by Lalasa Vattipalli


