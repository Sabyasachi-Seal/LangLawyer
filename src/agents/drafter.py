from langchain_core.messages import HumanMessage

from ..utils.model_utils import get_or_create_llm
from ..prompts.drafter_prompt import get_drafter_prompt

llm = get_or_create_llm()

def drafter(state):
    prompt = get_drafter_prompt(state)
    response = llm.invoke([HumanMessage(content=prompt)])
    state["messages"].append(response)
    state["contributions"]["drafter"] = "Draft: [advice summary]"
    return state