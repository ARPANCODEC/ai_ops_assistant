import os
import requests # type: ignore

def github_search(query, limit=3):
    """
    Fetches popular GitHub repositories based on query.
    """
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}"} if token else {}

    url = f"https://api.github.com/search/repositories?q={query}&sort=stars"
    response = requests.get(url, headers=headers, timeout=10)
    data = response.json()

    results = []
    for repo in data.get("items", [])[:limit]:
        results.append({
            "name": repo["full_name"],
            "stars": repo["stargazers_count"],
            "description": repo["description"]
        })

    return results
