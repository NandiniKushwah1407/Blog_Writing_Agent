from __future__ import annotations

import operator
from typing import TypedDict, List, Annotated

from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, START,END
from langgraph.types import Send

from langchain_core.messages import SystemMessage, HumanMessage

class Task(BaseModel):
    task_id: str
    title: str
    brief: str = Field(..., description="A brief description of the task")

class Plan(BaseModel):
    blog_title: str
    tasks: List[Task]

class State(TypedDict):
    topic: str
    plan: Plan
    sections: Annotated[List[str], operator.add]
