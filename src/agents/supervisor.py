from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from ..utils.model_utils import get_or_create_llm

llm = get_or_create_llm()

def supervisor(state):
    """Routes to next agent based on task progress."""
    messages = state["messages"]
    query = messages[0].content  # User's query
    contributions = state.get("contributions", {})  # Dict of agent: summary

    prompt = f"""
    You are a Legal Supervisor. User's query: {query}
    Current contributions:
    {contributions}

    Decide next step: researcher (find sources), analyzer (interpret), drafter (draft advice), or end (synthesize final response).
    Respond with ONLY: 'researcher', 'analyzer', 'drafter', or 'end'. Reason briefly.
    """
    response = llm.invoke([HumanMessage(content=prompt)])
    next_agent = response.content.strip().lower()
    state["next"] = next_agent if next_agent in ["researcher", "analyzer", "drafter"] else "end"
    state["messages"].append(AIMessage(content=f"Supervisor routes to: {next_agent}"))
    return state