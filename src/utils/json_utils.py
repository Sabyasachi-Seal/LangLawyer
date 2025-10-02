import re
import json

def clean_markdown_json(content: str) -> str:
    """Strips Markdown code blocks (```json
    # Remove leading/trailing whitespace and common wrappers"""
    content = content.strip()

    lines = content.split('\n')
    cleaned_lines = []
    in_block = False
    for line in lines:
        line = line.strip()
        if line.startswith('```json') or line.startswith('```'):
            in_block = True
            continue  # Skip opener
        if in_block and line == '```':
            in_block = False
            break  # Stop at closer
        if in_block and line:  # Only add non-empty lines inside block
            cleaned_lines.append(line)
    
    cleaned = '\n'.join(cleaned_lines).strip()
    if not cleaned:
        # Fallback: Simple replace if no lines
        cleaned = re.sub(r'```json\s*|\s*```', '', content).strip()
    
    # print(f"Cleaned JSON: {cleaned}")  # Debug to verify
    return cleaned
  

def get_next_state_and_reason(content: str):
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

    return next_agent, reason
  