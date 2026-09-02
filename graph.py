from langgraph.graph import StateGraph, START,END
from model import State
from orchestrator import orchestrator
from worker import fanout, worker
from reducer import reducer

graph = StateGraph(State)
graph.add_node("orchestrator", orchestrator)
graph.add_node("worker", worker)
graph.add_node("reducer", reducer)

graph.add_edge(START, "orchestrator")
graph.add_conditional_edges("orchestrator",fanout, ["worker"])
graph.add_edge("worker", "reducer")
graph.add_edge("reducer", END)


app = graph.compile()