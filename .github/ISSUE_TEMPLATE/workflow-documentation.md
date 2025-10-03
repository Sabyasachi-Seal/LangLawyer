---
name: Workflow Documentation Enhancement
about: Improve documentation for the multi-agent workflow system
title: '[WORKFLOW DOC] '
labels: 'documentation, workflow'
assignees: ''
---

## Overview
This issue tracks improvements needed for the LangLawyer multi-agent workflow documentation.

## Current State
The workflow currently consists of:
- **Supervisor Agent**: Routes tasks between agents based on state
- **Researcher Agent**: Gathers legal information using tools
- **Analyzer Agent**: Interprets research findings
- **Drafter Agent**: Prepares draft responses
- **Synthesizer Node**: Compiles final response

## Documentation Gaps

### 1. Workflow State Machine Documentation
- [ ] Add detailed state transition diagram
- [ ] Document the `LegalState` TypedDict structure
- [ ] Explain how `contributions` dict is populated and used
- [ ] Document iteration limits and end conditions

### 2. Agent Interaction Documentation
- [ ] Document supervisor routing logic in detail
- [ ] Explain how agents loop back to supervisor
- [ ] Document message passing between agents
- [ ] Add sequence diagrams for common workflows

### 3. Supervisor Decision Logic
- [ ] Document how supervisor decides next agent
- [ ] Explain JSON parsing and fallback mechanisms
- [ ] Document the conditions for ending workflow (state["next"] == "end" or iterations >= 10)
- [ ] Add examples of supervisor routing decisions

### 4. Tool Execution Flow
- [ ] Document how researcher uses legal_web_search tool
- [ ] Explain tool call execution and result handling
- [ ] Document error handling for tool failures
- [ ] Add examples of tool call sequences

### 5. Synthesis Process
- [ ] Document how final response is structured
- [ ] Explain how contributions are compiled
- [ ] Document output format (Overview, Key Rights, Steps, Disclaimer)
- [ ] Add examples of synthesized responses

## Proposed Improvements

### Documentation Files to Create
1. `docs/WORKFLOW.md` - Comprehensive workflow guide
2. `docs/AGENTS.md` - Detailed agent documentation
3. `docs/STATE_MANAGEMENT.md` - State machine and transitions
4. `docs/DIAGRAMS/` - Visual workflow diagrams

### Diagrams Needed
1. High-level workflow flowchart
2. State transition diagram
3. Agent interaction sequence diagram
4. Tool execution flow diagram

### Code Examples Needed
1. Custom workflow configuration example
2. Adding new agents to workflow
3. Modifying routing logic
4. Custom tool integration

## Acceptance Criteria
- [ ] All workflow components are documented
- [ ] Visual diagrams are included
- [ ] Code examples are provided
- [ ] README.md links to detailed docs
- [ ] Examples demonstrate common use cases

## Additional Context
Reference files:
- `src/graph/workflow.py` - Main workflow implementation
- `src/agents/supervisor.py` - Supervisor routing logic
- `src/agents/researcher.py` - Tool execution example
- `README.md` - Current high-level documentation
