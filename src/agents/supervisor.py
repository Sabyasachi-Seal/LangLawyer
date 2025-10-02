from langchain_core.messages import HumanMessage, AIMessage
from ..utils.model_utils import get_or_create_llm
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
    
    Available next steps: researcher (if no sources found), analyzer (after researcher), drafter (after analyzer), end (if ready for final synthesis).
    
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
    
    content.replace('```', '')
    content.replace('json', '')

    # Robust JSON parsing
    try:
        parsed = json.loads(content)
        next_agent = parsed.get("next", "").lower().strip()
        reason = parsed.get("reason", "LLM routing applied.")
    except json.JSONDecodeError:
        print("Warning: JSON parse failed; using regex fallback.")
        match = re.search(r'"next"\s*:\s*"(\w+)"', content, re.IGNORECASE)
        next_agent = match.group(1).lower() if match else "researcher"
        reason_match = re.search(r'"reason"\s*:\s*"([^"]*)"', content, re.IGNORECASE)
        reason = reason_match.group(1) if reason_match else "Fallback reason."# Default fallback

    
    if next_agent not in ["researcher", "analyzer", "drafter", "end"]:
        print(next_agent)

    state["next"] = next_agent
    state["iterations"] = state.get("iterations", 0) + 1
    
    # Your debug prints
    print(f"Supervisor decision: {next_agent}")
    print(next_agent in ["researcher", "analyzer", "drafter"])
    
    state["messages"].append(AIMessage(content=f"Supervisor routes to: {next_agent}. {reason}"))
    
    print(f"Supervisor Debug: Contributions={list(contributions.keys())}, Next={next_agent}, Iterations={state['iterations']}")
    
    return state