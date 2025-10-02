def get_supervisor_prompt(state):

    messages = state["messages"]
    query = messages[0].content
    contributions = state["contributions"]

    v1 = f"""
    You are a Legal Supervisor. User's query: {query}
    Current contributions: {contributions}
    
    Route based on progress:
    - researcher: If no 'researcher' key yet (start sources).
    - analyzer: If 'researcher' exists but no 'analyzer' (interpret next).
    - drafter: If 'analyzer' exists but no 'drafter' (draft advice).
    - end: Only if all three keys exist (researcher, analyzer, drafter).

    STRICT FORMAT - Respond EXACTLY with valid JSON (no extra text):
    {{
        "next": "one word: researcher OR analyzer OR drafter OR end",
        "reason": "1-2 sentences explaining why"
    }}

    Example:
    {{
        "next": "researcher",
        "reason": "No prior research; need sources first."
    }}


    """

    return v1