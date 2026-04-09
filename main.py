from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"   # ✅ FINAL WORKING MODEL
)

from scraper import scrape_website
from rag import create_vector_db
from tools import search_google
from graph import decide_route

# load data
text = scrape_website("https://debales.ai")
db = create_vector_db(text)

def chatbot():
    while True:
        query = input("You: ")

        route = decide_route(query)

        if route == "rag":
            docs = db.similarity_search(query)

            context = docs[0].page_content

            prompt = f"""
            Answer the question based on this context:

            Context:
            {context}

            Question:
            {query}
            """

            response = llm.invoke(prompt)
            print("AI:", response.content)

        else:
            result = search_google(query)
            print("AI:", result)

chatbot()