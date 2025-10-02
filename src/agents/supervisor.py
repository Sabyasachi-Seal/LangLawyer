from langchain_core.messages import HumanMessage, AIMessage
from ..utils.model_utils import get_or_create_llm
from ..utils.json_utils import clean_markdown_json, get_next_state_and_reason
from typing import Dict
import re
import json

llm = get_or_create_llm()

def supervisor(state: Dict):
    """Routes via LLM with structured output for reliable parsing."""
    if "contributions" not in state:
        state["contributions"] = {}
    
    messages = state["messages"]
    query = messages[0].content
    contributions = state["contributions"]
    
    prompt = f"""
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

    response = llm.invoke([HumanMessage(content=prompt)])
    content = response.content.strip()
    
    # Debug: Print raw LLM output
    print(f"Supervisor raw LLM output: {content}")
    
    cleaned_content = clean_markdown_json(content)

    next_agent, reason = get_next_state_and_reason(cleaned_content)
    
    if next_agent not in ["researcher", "analyzer", "drafter", "end"]:
        print(next_agent)

    state["next"] = next_agent
    state["iterations"] = state.get("iterations", 0) + 1
    state["messages"].append(AIMessage(content=f"Supervisor routes to: {next_agent}. {reason}"))
    
    print(f"Supervisor Debug: Contributions={list(contributions.keys())}, Next={next_agent}, Iterations={state['iterations']}")
    
    return state