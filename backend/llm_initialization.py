import os

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model=os.getenv("OLLAMA_MODEL", os.getenv("LM_STUDIO_MODEL", "qwen2.5:3b-instruct")),
    base_url=os.getenv("OLLAMA_BASE_URL", os.getenv("LM_STUDIO_BASE_URL", "http://localhost:11434")),
    temperature=0.7,
)