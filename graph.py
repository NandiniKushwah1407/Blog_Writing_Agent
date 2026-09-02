from langgraph.graph import StateGraph, START,END
from blog_writing_agent.model import State
from blog_writing_agent.orchestrator import orchestrator
from blog_writing_agent.worker import fanout, worker
from blog_writing_agent.reducer import reducer

graph = StateGraph(State)
graph.add_node("orchestrator", orchestrator)
graph.add_node("worker", worker)
graph.add_node("reducer", reducer)

graph.add_edge(START, "orchestrator")
graph.add_conditional_edges("orchestrator",fanout, ["worker"])
graph.add_edge("worker", "reducer")
graph.add_edge("reducer", END)


app = graph.compile()