from tavily import TavilyClient

client = TavilyClient(api_key="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")

def search_web(query):

    results = client.search(
        query=query,
        max_results=5
    )

    urls = []

    for r in results["results"]:
        urls.append(r["url"])

    return urls