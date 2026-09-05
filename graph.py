from langgraph.graph import StateGraph, START,END
from model import State
from orchestrator import orchestrator
from worker import fanout, worker
from reducer import reducer
from router import router, route_next
from tavily_search import research_node
from reducer_with_image import merge_content, decide_images, generate_and_place_images

# Subgraph for reducer with image generation
reducer_graph = StateGraph(State)
reducer_graph.add_node("merge_content", merge_content)
reducer_graph.add_node("decide_images", decide_images)
reducer_graph.add_node("generate_and_place_images", generate_and_place_images)
reducer_graph.add_edge(START, "merge_content")
reducer_graph.add_edge("merge_content", "decide_images")
reducer_graph.add_edge("decide_images", "generate_and_place_images")
reducer_graph.add_edge("generate_and_place_images", END)
reducer_subgraph = reducer_graph.compile()


# main graph
graph = StateGraph(State)
graph.add_node("router", router)
graph.add_node("research", research_node)
graph.add_node("orchestrator", orchestrator)
graph.add_node("worker", worker)
graph.add_node("reducer", reducer_subgraph)

graph.add_edge(START, "router")
graph.add_conditional_edges("router", route_next, {"research": "research", "orchestrator": "orchestrator"})
graph.add_edge("research", "orchestrator")

graph.add_conditional_edges("orchestrator", fanout, ["worker"])
graph.add_edge("worker", "reducer")
graph.add_edge("reducer", END)

app = graph.compile()


# graph without image generation
# graph = StateGraph(State)
# graph.add_node("router", router)
# graph.add_node("research", research_node)
# graph.add_node("orchestrator", orchestrator)
# graph.add_node("worker", worker)
# graph.add_node("reducer", reducer)

# graph.add_edge(START, "router")
# graph.add_conditional_edges("router", route_next, {"research": "research", "orchestrator": "orchestrator"})
# graph.add_edge("research", "orchestrator")

# graph.add_conditional_edges("orchestrator", fanout, {"worker": "worker"})
# graph.add_edge("worker", "reducer")
# graph.add_edge("reducer", END)