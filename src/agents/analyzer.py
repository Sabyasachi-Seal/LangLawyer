from langchain_core.messages import HumanMessage

from ..utils.model_utils import get_or_create_llm
from ..prompts.analyzer_prompt import get_analyzer_prompt

llm = get_or_create_llm()

def analyzer(state):
    prompt = get_analyzer_prompt(state)
    response = llm.invoke([HumanMessage(content=prompt)])
    state["messages"].append(response)
    state["contributions"]["analyzer"] = "Analysis: [key insights]"
    return state