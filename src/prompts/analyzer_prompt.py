def get_analyzer_prompt(state):
    messages = state["messages"]
    contributions = state.get("contributions", {})
    v1 = f"""
    You are a Legal Analyzer. Query: {messages[0].content}
    Research: {contributions.get('researcher', 'None')}
    Analyze relevance, risks, and applicability to user.
    """
    return v1