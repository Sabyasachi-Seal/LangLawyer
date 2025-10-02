from langchain_core.messages import HumanMessage

from ..utils.model_utils import get_or_create_llm

llm = get_or_create_llm()

def drafter(state):
    messages = state["messages"]
    contributions = state.get("contributions", {})
    prompt = f"""
    You are a Legal Drafter. Query: {messages[0].content}
    Research: {contributions.get('researcher', '')}
    Analysis: {contributions.get('analyzer', '')}
    Draft clear, concise advice. Include disclaimers.
    """
    response = llm.invoke([HumanMessage(content=prompt)])
    state["messages"].append(response)
    state["contributions"]["drafter"] = "Draft: [advice summary]"
    return state