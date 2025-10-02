from langchain_core.messages import HumanMessage

from ..utils.model_utils import get_or_create_llm

llm = get_or_create_llm()

def analyzer(state):
    messages = state["messages"]
    contributions = state.get("contributions", {})
    prompt = f"""
    You are a Legal Analyzer. Query: {messages[0].content}
    Research: {contributions.get('researcher', 'None')}
    Analyze relevance, risks, and applicability to user.
    """
    response = llm.invoke([HumanMessage(content=prompt)])
    state["messages"].append(response)
    state["contributions"]["analyzer"] = "Analysis: [key insights]"
    return state