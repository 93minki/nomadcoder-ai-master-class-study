import os
import re

import requests
from crewai.tools import tool


@tool
def web_search_tool(query: str):
    """
    Web Search Tool.
    Args:
        query: str
            The query to search the web for.
    Returns:
        A list of search results with the website content in markdown format.
    """
    url = "https://api.firecrawl.dev/v2/search"
    api_key = os.getenv("FIRECRAWL_API_KEY")

    payload = {
        "query": query,
        "sources": ["web"],
        "limit": 3,
        "scrapeOptions": {"formats": ["markdown"]},
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)
    response = response.json()

    if not response["success"]:
        return "Error Using tool."

    cleaned_chunks = []

    for result in response.get("data", {}).get("web", []):
        title = result.get("title", "")
        url = result.get("url", "")
        markdown = result.get("markdown", "")

        cleaned = re.sub(r"\\+|\n+", "", markdown).strip()
        cleaned = re.sub(r"\[[^\]]+\]\([^\)]+\)|https?://[^\s]+", "", cleaned)

        cleaned_result = {
            "title": title,
            "url": url,
            "markdown": cleaned,
        }
        cleaned_chunks.append(cleaned_result)

    return cleaned_chunks
