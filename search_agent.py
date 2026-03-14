from tavily import TavilyClient

client = TavilyClient(api_key="TAVILY_API_KEY")

def search_web(query):

    results = client.search(
        query=query,
        max_results=5
    )

    urls = []

    for r in results["results"]:
        urls.append(r["url"])

    return urls