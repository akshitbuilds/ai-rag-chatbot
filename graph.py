def decide_route(query):
    query = query.lower()

    if "who" in query or "latest" in query or "news" in query:
        return "search"
    
    return "rag"