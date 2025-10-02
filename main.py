from langchain_core.messages import HumanMessage
from datetime import datetime
from src.graph.workflow import create_workflow


# Create graph
graph = create_workflow()

# Run
today = datetime.now().strftime('%Y-%m-%d')
inputs = {"messages": [HumanMessage(content=f"What is the weather in Berlin on {today}?")]}
for chunk in graph.stream(inputs, stream_mode="values"):
    chunk["messages"][-1].pretty_print()

# Follow-up
state = {"messages": inputs["messages"], "number_of_steps": 0}
state["messages"].append(HumanMessage(content="Would it be warmer in Munich?"))
for chunk in graph.stream(state, stream_mode="values"):
    chunk["messages"][-1].pretty_print()