from __future__ import annotations

import operator
from typing import Literal, TypedDict, List, Annotated

from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, START,END
from langgraph.types import Send

from langchain_core.messages import SystemMessage, HumanMessage

class Task(BaseModel):
    task_id: str
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

class Plan(BaseModel):
    blog_title: str
    audience: str = Field(..., description="Who is the target audience for the blog")
    tone: str = Field(..., description="The tone of the blog (e.g., formal, casual, humorous)")
    tasks: List[Task]

class State(TypedDict):
    topic: str
    plan: Plan
    sections: Annotated[List[str], operator.add]
