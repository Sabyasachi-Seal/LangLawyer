from langchain_core.messages import HumanMessage, AIMessage
from ..utils.model_utils import get_or_create_llm
from ..utils.json_utils import clean_markdown_json, get_next_state_and_reason
from ..prompts.supervisor_prompt import get_supervisor_prompt
from typing import Dict

llm = get_or_create_llm()

def supervisor(state: Dict):
    """Routes via LLM with structured output for reliable parsing."""
    if "contributions" not in state:
        state["contributions"] = {}


    prompt = get_supervisor_prompt(state)

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
    
    print(f"Supervisor Debug: Contributions={list(state['contributions'].keys())}, Next={next_agent}, Iterations={state['iterations']}")
    
    return state