from langchain_core.tools import tool
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
from pydantic import BaseModel, Field
import requests  # For browsing if needed

search = DuckDuckGoSearchRun()  # Instantiates DuckDuckGo search

class LegalSearchInput(BaseModel):
    query: str = Field(description="Legal query, e.g., 'California tenant eviction laws 2025'")
    num_results: int = Field(default=5, description="Max results to fetch")

@tool("legal_web_search", args_schema=LegalSearchInput)
def legal_web_search(query: str, num_results: int = 5):
    """Searches the web for legal information on statutes, cases, or advice. Returns top results with snippets."""
    results = search.run(query)  # DuckDuckGo returns formatted text
    return f"Top {num_results} results for '{query}':\n{results[:1000]}"  # Truncate for brevity

@tool("summarize_doc")
def summarize_doc(url: str, instructions: str = "Summarize key legal points, citations, and implications."):
    """Browses and summarizes a legal document URL (e.g., statute page)."""
    # Simple fetch + placeholder; in prod, use langchain's WebBaseLoader or browser tool
    try:
        response = requests.get(url)
        text = response.text[:2000]  # Truncate
        return f"Summary of {url}: {instructions} - {text[:500]}"  # LLM would expand this
    except Exception as e:
        return f"Error fetching {url}: {str(e)}"

tools = [legal_web_search, summarize_doc]