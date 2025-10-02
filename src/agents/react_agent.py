from typing import Annotated, Sequence
from langchain_core.messages import BaseMessage, ToolMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph.message import add_messages
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from ..tools.weather_tools import tools
import dotenv

dotenv.load_dotenv()

from typing import TypedDict

class AgentState(TypedDict):
    """The state of the agent."""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    number_of_steps: int

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
temp = os.getenv("MODEL_TEMP", 0.5)
max_retry = os.getenv("MAX_RETRIES", 3)

print(f"Using model: {model} with temperature: {temp} and max_retries: {max_retry}")

# Model
llm = ChatGoogleGenerativeAI(
    model=model,
    temperature=float(temp),
    max_retries=int(max_retry),
    google_api_key=api_key,
)
model = llm.bind_tools(tools)

# Nodes
tools_by_name = {tool.name: tool for tool in tools}

def call_tool(state: AgentState):
    outputs = []
    for tool_call in state["messages"][-1].tool_calls:
        tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=tool_result,
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return {"messages": outputs}

def call_model(state: AgentState, config: RunnableConfig):
    response = model.invoke(state["messages"], config)
    return {"messages": [response]}

def should_continue(state: AgentState):
    messages = state["messages"]
    if not messages[-1].tool_calls:
        return "end"
    return "continue"