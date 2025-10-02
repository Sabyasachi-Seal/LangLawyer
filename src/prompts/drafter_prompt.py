def get_drafter_prompt(state):
    messages = state["messages"]
    contributions = state.get("contributions", {})
    v1 = f"""
    You are a Legal Drafter. Query: {messages[0].content}
    Research: {contributions.get('researcher', '')}
    Analysis: {contributions.get('analyzer', '')}
    Draft clear, concise advice. Include disclaimers.
    """
    return v1