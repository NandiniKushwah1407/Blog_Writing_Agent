from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()
tool = TavilySearchResults(max_results=2)
results = tool.invoke({"query": "What is the capital of France?"})

print(results)