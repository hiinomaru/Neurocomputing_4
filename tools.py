from duckduckgo_search import DDGS

def search_web(query):
    try:
        results = DDGS().text(query, max_results=5)

        if not results:
            return "No results found"

        return results[0]["body"]

    except Exception as e:
        return f"Search error: {e}"