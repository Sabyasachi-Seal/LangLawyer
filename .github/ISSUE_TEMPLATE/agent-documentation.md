---
name: Agent Documentation Enhancement
about: Improve documentation for individual agents
title: '[AGENT DOC] '
labels: 'documentation, agents'
assignees: ''
---

## Overview
This issue tracks documentation improvements for individual agent implementations.

## Current State
Four agents are implemented:
- Supervisor: Routes workflow
- Researcher: Uses tools to gather information
- Analyzer: Interprets findings
- Drafter: Creates responses

## Documentation Needed

### 1. Supervisor Agent
- [ ] Document routing algorithm
- [ ] Explain JSON parsing and cleaning logic (`clean_markdown_json`)
- [ ] Document fallback mechanisms for invalid LLM responses
- [ ] Explain state management (contributions, iterations)
- [ ] Add examples of routing decisions
- [ ] Document the supervisor prompt structure

### 2. Researcher Agent
- [ ] Document tool binding process
- [ ] Explain tool call execution flow
- [ ] Document mini-loop for tool execution and summarization
- [ ] Explain how contributions are extracted
- [ ] Add examples of research queries and responses
- [ ] Document tool error handling

### 3. Analyzer Agent
- [ ] Document analysis process
- [ ] Explain how analyzer uses researcher contributions
- [ ] Add examples of analysis output
- [ ] Document the analyzer prompt structure

### 4. Drafter Agent
- [ ] Document drafting process
- [ ] Explain how drafter uses analyzer and researcher contributions
- [ ] Add examples of draft responses
- [ ] Document the drafter prompt structure
- [ ] Explain disclaimer generation

## Prompt Documentation
- [ ] Document prompt engineering strategy
- [ ] Explain how prompts use state and contributions
- [ ] Add examples of effective prompts
- [ ] Document prompt customization guidelines

## Tool Documentation
- [ ] Document `legal_web_search` tool
  - [ ] Explain DuckDuckGo integration
  - [ ] Document query formatting best practices
  - [ ] Add result parsing examples
- [ ] Document `summarize_doc` tool
  - [ ] Explain URL fetching mechanism
  - [ ] Document limitations and error handling
  - [ ] Add usage examples

## Proposed Documentation Structure
```
docs/agents/
├── README.md           # Agent overview
├── SUPERVISOR.md       # Supervisor details
├── RESEARCHER.md       # Researcher details
├── ANALYZER.md         # Analyzer details
├── DRAFTER.md          # Drafter details
├── PROMPTS.md          # Prompt engineering guide
└── TOOLS.md            # Tool usage guide
```

## Code Examples Needed
1. Custom agent creation
2. Modifying agent behavior
3. Adding new tools
4. Custom prompt templates

## Acceptance Criteria
- [ ] Each agent has detailed documentation
- [ ] Tool usage is fully documented
- [ ] Prompt engineering is explained
- [ ] Code examples are provided
- [ ] Agent interaction patterns are documented

## Reference Files
- `src/agents/supervisor.py`
- `src/agents/researcher.py`
- `src/agents/analyzer.py`
- `src/agents/drafter.py`
- `src/prompts/*.py`
- `src/tools/legal_tools.py`
