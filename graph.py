def decide_route(query):
    if "debales" in query.lower():
        return "rag"
    else:
        return "search"