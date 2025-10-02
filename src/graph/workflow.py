from typing import Annotated, Sequence, TypedDict, Dict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from ..agents.supervisor import supervisor
from ..agents.researcher import researcher
from ..agents.analyzer import analyzer
from ..agents.drafter import drafter
from langchain_core.messages import AIMessage, HumanMessage
from ..utils.model_utils import get_or_create_llm

llm = get_or_create_llm()

class LegalState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    contributions: Dict[str, str]  # agent_name: summary
    next: str  # Next agent or 'end'
    iterations: int  # Track loops

def create_workflow():
    workflow = StateGraph(LegalState)
    
    # Add nodes
    workflow.add_node("supervisor", supervisor)
    workflow.add_node("researcher", researcher)
    workflow.add_node("analyzer", analyzer)
    workflow.add_node("drafter", drafter)
    
    # Edges: Supervisor -> workers -> back to supervisor
    def route_to_agent(state):
        if state["next"] == "end" or state["iterations"] >= 10:
            return "synthesize"
        return state["next"]
    
    workflow.set_entry_point("supervisor")
    workflow.add_conditional_edges(
        "supervisor",
        route_to_agent,
        {
            "researcher": "researcher",
            "analyzer": "analyzer",
            "drafter": "drafter",
            "synthesize": END,
        },
    )
    # Loop back from workers
    for agent in ["researcher", "analyzer", "drafter"]:
        workflow.add_edge(agent, "supervisor")
    
    def synthesize(state):
        contributions = state.get("contributions", {})
        query = state["messages"][0].content
        prompt = f"""
        You are a Legal Synthesizer. Compile comprehensive response.
        Query: {query}
        Contributions:
        - Researcher: {contributions.get('researcher', 'N/A')}
        - Analyzer: {contributions.get('analyzer', 'N/A')}
        - Drafter: {contributions.get('drafter', 'N/A')}
        
        Final structure: 1. Overview. 2. Key Rights. 3. Steps. 4. Disclaimer.
        """
        response = llm.invoke([HumanMessage(content=prompt)])
        state["messages"].append(AIMessage(content=response.content))
        print("Synthesized final response!")  # Debug
        return state
    
    workflow.add_node("synthesize", synthesize)
    
    return workflow.compile()