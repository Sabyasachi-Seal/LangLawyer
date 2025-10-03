import os
import sys
import json

# Check if OpenAI API key is available
api_key = os.environ.get('OPENAI_API_KEY', '')

if not api_key:
    print("OpenAI API key not configured, will use fallback")
    sys.exit(1)

# Get commit information from environment
commit_message = os.environ.get('COMMIT_MESSAGE', '')
commit_author = os.environ.get('COMMIT_AUTHOR', '')
changed_files = os.environ.get('CHANGED_FILES', '').split(',')
diff_stat = os.environ.get('DIFF_STAT', '')
commit_body = os.environ.get('COMMIT_BODY', '')

# Filter relevant files
relevant_files = [f for f in changed_files if f and 
                  '.github/workflows' not in f and 
                  'node_modules' not in f and 
                  '.git' not in f]

# Prepare prompt for AI
prompt = f"""You are a changelog generator. Based on the following git commit information, generate a concise, user-friendly changelog entry.

Commit Message: {commit_message}
Author: {commit_author}
Files Changed: {', '.join(relevant_files) if relevant_files else 'None'}

Commit Details:
{commit_body if commit_body else 'No additional details'}

Change Statistics:
{diff_stat if diff_stat else 'Not available'}

Generate a changelog entry in this format:
- **[Brief user-facing description]** ({commit_author})
  - [Key change 1]
  - [Key change 2]

Rules:
1. Focus on WHAT changed from a user/developer perspective, not implementation details
2. Be concise (2-4 bullet points maximum)
3. Use clear, non-technical language where possible
4. Don't mention file names unless critical
5. Start the description with an action verb

Return ONLY the formatted changelog entry, nothing else."""

try:
    import urllib.request
    import urllib.error
    
    # Prepare request to OpenAI API
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that generates concise, user-friendly changelog entries from git commits."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 200
    }
    
    request = urllib.request.Request(
        'https://api.openai.com/v1/chat/completions',
        data=json.dumps(data).encode('utf-8'),
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
    )
    
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.loads(response.read().decode('utf-8'))
        changelog_entry = result['choices'][0]['message']['content'].strip()
        print(changelog_entry)
        
except Exception as e:
    print(f"Error calling OpenAI API: {e}", file=sys.stderr)
    sys.exit(1)
