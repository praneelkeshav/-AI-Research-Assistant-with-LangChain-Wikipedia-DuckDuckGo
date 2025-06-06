# -AI-Research-Assistant-with-LangChain-Wikipedia-DuckDuckGo_Using_OpenAI
An intelligent research assistant built using LangChain, OpenAI, and external tools like DuckDuckGo and Wikipedia. It automates the process of collecting, summarizing, and saving research on any topic using agent-based decision-making. Ideal for students, analysts, and knowledge worker
# 🧠 AI Research Assistant

An intelligent, agent-driven research assistant built with **LangChain**, **OpenAI**, **DuckDuckGo**, and **WikipediaAPI**. It processes a user query, gathers reliable information from Wikipedia and DuckDuckGo, summarizes it, and optionally saves the output to a local text file.

## 🚀 Features

- 🌐 Web Search via DuckDuckGo
- 📚 Wikipedia summaries using the `wikipediaapi`
- ✍️ Saves results to a `.txt` file with a timestamp
- 🤖 Powered by LangChain’s tool-calling agent framework
- ✅ Outputs structured results using `Pydantic`

## 🛠️ Tech Stack

- Python 3.10+
- LangChain
- OpenAI GPT (e.g. `gpt-4-turbo`)
- DuckDuckGo Search
- Wikipedia API
- dotenv for API keys

## 📦 Installation

```bash
git clone https://github.com/yourusername/ai-research-agent.git
cd ai-research-agent
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
