from llm_initialization import llm
from model import Plan, State
from langchain_core.messages import SystemMessage, HumanMessage

def orchestrator(state: State) -> Plan:
    plan = llm.with_structured_output(Plan).invoke(
        [
            SystemMessage(
                content = (
                    "Create a blog plan with 5-7 sections on the following topic."
                )
            ),
            HumanMessage(
                content = (
                    f"Topic: {state['topic']}"
                )
            )
        ]

    )
    return {"plan": plan}