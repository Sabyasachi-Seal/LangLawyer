from langgraph.graph import StateGraph, END
from ..agents.react_agent import AgentState, call_model, call_tool, should_continue

def create_workflow():
    workflow = StateGraph(AgentState)
    workflow.add_node("llm", call_model)
    workflow.add_node("tools", call_tool)
    workflow.set_entry_point("llm")
    workflow.add_conditional_edges(
        "llm",
        should_continue,
        {
            "continue": "tools",
            "end": END,
        },
    )
    workflow.add_edge("tools", "llm")
    return workflow.compile()