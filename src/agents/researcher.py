from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage  
from langchain_core.messages import HumanMessage, ToolMessage
from ..tools.legal_tools import tools
from typing import Dict


from ..utils.model_utils import get_or_create_llm

model = get_or_create_llm()

tools_by_name = {tool.name: tool for tool in tools}

def call_tool(last_message: AIMessage) -> list:
    """Helper: Execute tools from last message."""
    outputs = []
    for tool_call in last_message.tool_calls:
        try:
            tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
            outputs.append(
                ToolMessage(
                    content=str(tool_result),  # Convert to str for messages
                    name=tool_call["name"],
                    tool_call_id=tool_call["id"],
                )
            )
            print(f"Tool {tool_call['name']} executed: {tool_result}")  # Debug print
        except Exception as e:
            outputs.append(ToolMessage(content=f"Tool error: {str(e)}", name=tool_call["name"], tool_call_id=tool_call["id"]))
    return outputs

def researcher(state: Dict):
    """Researcher node: Reasons, calls tools if needed, summarizes."""
    messages = state["messages"]
    query = messages[0].content
    contributions = state.get("contributions", {})
    
    # Initial prompt for research
    prompt = f"""
    You are a Legal Researcher. User's query: {query}
    Previous contributions: {contributions}
    
    Find reliable sources (statutes, cases, official sites) using tools like legal_web_search.
    ALWAYS use tools for fresh info. Then, summarize key findings with citations.
    """
    
    # Start with system-like message for context
    full_messages = [HumanMessage(content=prompt)] + messages[-3:]  # Last 3 for context
    
    response = model.invoke(full_messages)
    state["messages"].append(response)
    
    # Mini-loop: If tool calls, execute and re-invoke model for summary
    if response.tool_calls:
        tool_outputs = call_tool(response)
        state["messages"].extend(tool_outputs)
        
        # Re-prompt model with tool results for summary
        summary_prompt = f"""
        Summarize the tool results for query '{query}':
        {tool_outputs[-1].content}
        Provide: 1. Key laws/cases. 2. Sources. Keep concise (under 300 words).
        """
        summary_response = model.invoke(full_messages + tool_outputs + [HumanMessage(content=summary_prompt)])
        state["messages"].append(summary_response)
        
        # Extract summary for contributions
        summary = summary_response.content[:200] + "..." if len(summary_response.content) > 200 else summary_response.content
        state["contributions"]["researcher"] = summary
    else:
        # Fallback summary if no tools (rare)
        state["contributions"]["researcher"] = "No tools called; basic research needed."
    
    print(f"Researcher done: {state['contributions']['researcher'][:100]}...")  # Debug
    return state