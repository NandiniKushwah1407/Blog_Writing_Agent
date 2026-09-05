from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
from model import State, EvidenceItem
from typing import List
from llm_initialization import llm
from model import EvidencePack
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv() # load environment variables from .env file
# tool = TavilySearchResults(max_results=2)
# results = tool.invoke({"query": "What is the capital of France?"})

# print(results)


def _tavily_search(query: str, max_results: int = 5) -> list[dict]:
    tool = TavilySearchResults(max_results=max_results)
    results = tool.invoke({"query": query})

    normalized: List[dict] = []
    for r in results:
        normalized.append(
            {
                "title": r.get("title") or "",
                "url": r.get("url") or "",
                "snippet": r.get("snippet") or "",
                "published_at": r.get("published_at") or r.get("published_at"),
                "source": r.get("source"),
            }
        )

    return normalized

RESEARCH_SYSTEM = """You are a research synthesizer for technical writing.

Given raw web search results, produce a deduplicated list of EvidenceItem objects.

Rules:
- Only include items with a non-empty url.
- Prefer relevant + authoritative sources (company blogs, docs, reputable outlets).
- If a published date is explicitly present in the result payload, keep it as YYYY-MM-DD.
  If missing or unclear, set published_at=null. Do NOT guess.
- Keep snippets short.
- Deduplicate by URL.
"""


def research_node(state: State) -> dict:
    quires = (state.get("queries", [] or []))
    max_results = 5

    raw_results: list[dict] = []

    for q in quires:
        raw_results.extend(_tavily_search(query=q, max_results=max_results))

    if not raw_results:
        return {"evidence": []}

    extractor = llm.with_structured_output(EvidencePack)
    pack = extractor.invoke(
        [
            SystemMessage(content=RESEARCH_SYSTEM),
            HumanMessage(
                content=f"Raw search results: {raw_results}"
            )
        ]
    )

    dedup = {}
    for e in pack.evidence:
        if e.url:
            dedup[e.url] = e

    return {"evidence": list(dedup.values())}