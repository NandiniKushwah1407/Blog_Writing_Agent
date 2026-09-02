import os

from langchain_openai import ChatOpenAI

# LM Studio exposes an OpenAI-compatible REST API once you start its local
# server: open LM Studio -> Developer (left sidebar) -> load a model ->
# Start Server. It listens on http://localhost:1234/v1 by default.
# LM Studio doesn't check the API key, but the client requires a non-empty
# string, so any placeholder value works.
llm = ChatOpenAI(
    model=os.getenv("LM_STUDIO_MODEL", "REPLACE_WITH_MODEL_ID_FROM_LM_STUDIO"),
    base_url=os.getenv("LM_STUDIO_BASE_URL", "http://localhost:1234/v1"),
    api_key=os.getenv("LM_STUDIO_API_KEY", "lm-studio"),
    temperature=0.7,
)