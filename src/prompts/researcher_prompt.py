def get_researcher_prompt(state):

    messages = state["messages"]
    query = messages[0].content
    contributions = state.get("contributions", {})    

    v1 = f"""
        You are a Legal Researcher. User's query: {query}
        Previous contributions: {contributions}
        
        Find reliable sources (statutes, cases, official sites) using tools like legal_web_search.
        ALWAYS use tools for fresh info. Then, summarize key findings with citations.
        """
    
    return v1