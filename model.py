from __future__ import annotations

import operator
from typing import Literal, TypedDict, List, Annotated,Optional

from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, START,END
from langgraph.types import Send

from langchain_core.messages import SystemMessage, HumanMessage

class Task(BaseModel):
    id: str
    title: str
    goal: str = Field(..., description="One sentence describing what the reader should be able to do/understand after this section.")
    
    bullets: List[str] = Field(...,
        min_length=3,
        max_length=5,
        description="3-5 concrete, non-overlapping subpoints to cover in this section.")
    
    target_words: int = Field(..., 
            description="Target word count for this section (128-450).")
    
    Section_type: Literal[
        "intro", "core", "examples", "checklist", "common_mistakes", "conclusion"
        ] = Field(...,
                description="Use 'common_mistakes' exactly once in the plan.")
    tags: List[str] = Field(default_factory=list)
    requires_research: bool = False
    requires_citation: bool = False
    requires_code: bool = False

class Plan(BaseModel):
    blog_title: str
    audience: str = Field(..., description="Who is the target audience for the blog")
    tone: str = Field(..., description="The tone of the blog (e.g., formal, casual, humorous)")
    blog_kind: Literal["explainer", "tutorial", "news_roundup", "comparison", "system_design"] = "explainer"
    constraints: List[str] = Field(default_factory=list)
    tasks: List[Task]

class EvidenceItem(BaseModel):
    title: str
    url: str
    published_at: Optional[str] = None # keep it if tavly provides it, otherwise None
    snippet: Optional[str] = None
    source: Optional[str] = None 

class RouterDecision(BaseModel):
    needs_research: bool
    mode: Literal["closed_book", "open_book", "hybrid"]
    queries: List[str] = Field(default_factory=list)

class EvidencePack(BaseModel):
    evidence: List[EvidenceItem] = Field(default_factory=list)


class ImageSpec(BaseModel):
    placeholder: str = Field(..., description="e.g. [[IMAGE_1]]")
    filename: str = Field(..., description="Save under images/, e.g. qkv_flow.png")
    alt: str
    caption: str
    prompt: str = Field(..., description="Prompt to send to the image model.")
    size: Literal["1024x1024", "1024x1536", "1536x1024"] = "1024x1024"
    quality: Literal["low", "medium", "high"] = "medium"


class GlobalImagePlan(BaseModel):
    md_with_placeholders: str
    images: List[ImageSpec] = Field(default_factory=list)
    

class State(TypedDict):
    topic: str

    # routing / research
    mode: str
    needs_research: bool
    queries: List[str]
    evidence: List[EvidenceItem]
    plan: Optional[Plan]

    # workers
    sections: Annotated[List[tuple[int, str]], operator.add]  # (task_id, section_md)

    # reducer/image
    merged_md: str
    md_with_placeholders: str
    image_specs: List[dict]

    final: str