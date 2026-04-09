import requests
import os

def search_google(query):
    api_key = os.getenv("SERPAPI_KEY")

    url = f"https://serpapi.com/search.json?q={query}&api_key={api_key}"

    res = requests.get(url).json()

    results = res.get("organic_results", [])

    if results:
        return results[0]["snippet"]

    return "No results found"