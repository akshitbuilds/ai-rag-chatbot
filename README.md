# 🚀 AI Agent with RAG + Web Search (LangChain + Groq)

## 📌 Overview

This project is an AI chatbot that combines:

* RAG (Retrieval-Augmented Generation)
* Real-time Web Search (SerpAPI)

It intelligently decides whether to:

1. Answer from a knowledge base (Debales AI website)
2. Fetch real-time data from Google

---

## 🎯 Features

* Smart query routing (RAG vs Search)
* Vector database using FAISS
* HuggingFace embeddings
* Fast LLM responses using Groq (LLaMA 3.1)
* Clean, accurate, and contextual answers

---

## 🛠️ Tech Stack

* Python
* LangChain
* Groq API
* HuggingFace (sentence-transformers)
* FAISS
* SerpAPI

---

## 🎥 Demo

Example:

You: What is Debales AI?
AI: Debales AI is an Autonomous Logistics Automation Platform that provides AI agents for supply chain automation.

You: Who is Elon Musk?
AI: Elon Musk is a businessman and entrepreneur known for Tesla, SpaceX, X, and xAI.

---

## ⚙️ Setup

### 1. Clone the repository

```
git clone https://github.com/akshitbuilds/ai-rag-chatbot.git
cd ai-rag-chatbot
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Create `.env` file

Create a file named `.env` in the root directory and add:

```
GROQ_API_KEY=your_groq_api_key
SERPAPI_KEY=your_serpapi_key
```

### 4. Run the project

```
python main.py
```

---

## 📂 Project Structure

```
ai-rag-chatbot/
│
├── main.py          # Main chatbot logic
├── rag.py           # Vector database creation (RAG)
├── scraper.py       # Website scraping
├── tools.py         # Google search using SerpAPI
├── graph.py         # Query routing logic
├── requirements.txt # Dependencies
├── README.md        # Project documentation
```

---

## 🧠 How It Works

1. User enters a query
2. System decides:

   * Use **RAG** → if query is about known data
   * Use **Search** → if query needs real-time info
3. Retrieves relevant data
4. Sends context to LLM (Groq)
5. Returns a clean response

---

## 📌 Author

Akshit Agrawal
