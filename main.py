from langchain_core.messages import HumanMessage
from src.graph.workflow import create_workflow
import traceback

graph = create_workflow()


if __name__ == "__main__":
    inputs = {
        "messages": [HumanMessage(content="What are my rights as a tenant facing eviction in California?")],
        "contributions": {},
        "next": "",
        "iterations": 0
    }

    try:
        for chunk in graph.stream(inputs, stream_mode="values"):
            if "messages" in chunk:
                chunk["messages"][-1].pretty_print()
            print(f"--- State snapshot: next={chunk.get('next', 'N/A')}, iterations={chunk.get('iterations', 0)} ---")  # Debug
    except Exception as e:
        print(f"Workflow error: {e}")
        traceback.print_exc()