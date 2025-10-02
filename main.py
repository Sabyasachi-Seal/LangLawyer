from langchain_core.messages import HumanMessage
from src.graph.workflow import create_workflow
from dotenv import load_dotenv

load_dotenv()

graph = create_workflow()

# Example query
inputs = {
    "messages": [HumanMessage(content="What are my rights as a tenant facing eviction in California?")],
    "contributions": {},
    "next": "",
    "iterations": 0
}

for chunk in graph.stream(inputs, stream_mode="values"):
    if "messages" in chunk:
        chunk["messages"][-1].pretty_print()