from blog_writing_agent.model import State
from langgraph.types import Send
from langchain_core.messages import SystemMessage, HumanMessage
from blog_writing_agent.llm_initialization import llm



# intermidieate funtion to send the task to the worker one by one
def fanout(state: State):
    return [
        Send(
            "worker", {"task": task, "topic": state["topic"], "plan": state["plan"]}
        ) for task in state["plan"].tasks
    ]

def worker(payload: dict):
    task = payload["task"]
    topic = payload["topic"]
    plan = payload["plan"]

    blog_title = plan.blog_title

    section_md = llm.invoke(
        [
            SystemMessage(
                content=" Write one clean Markdown Section."
            ),
            HumanMessage(
                content=(
                    f"Blog: {blog_title}\n"
                    f"Topic: {topic}\n"
                    f"Section: {task.title}\n"
                    f"Brief: {task.brief}\n\n"
                    "Return only section conetnt in Markdown."
                )
            )

        ]
    ).content.strip()

    return {"sections": section_md}