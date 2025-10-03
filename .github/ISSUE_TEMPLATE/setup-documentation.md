---
name: Setup Documentation Enhancement
about: Improve installation and configuration documentation
title: '[SETUP DOC] '
labels: 'documentation, setup'
assignees: ''
---

## Overview
This issue tracks improvements needed for LangLawyer setup and configuration documentation.

## Current State
Current setup documentation includes:
- Basic installation command: `pip install -r requirements.txt`
- Environment variable example in `.env.example`
- Minimal run instructions in README.md

## Documentation Gaps

### 1. Installation Prerequisites
- [ ] Document Python version requirements (currently .python-version shows specific version)
- [ ] List system dependencies for duckduckgo-search
- [ ] Document pip version requirements
- [ ] Add virtual environment setup instructions
- [ ] Document platform-specific installation notes (Windows, macOS, Linux)

### 2. Environment Configuration
- [ ] Detailed explanation of each environment variable
  - [ ] `GEMINI_API_KEY` - How to obtain and set
  - [ ] `LANGSMITH_API_KEY` - Optional/required status
  - [ ] `GEMINI_MODEL` - Valid model names and selection guide
  - [ ] `MODEL_TEMP` - Temperature parameter explanation
  - [ ] `MAX_RETRIES` - Retry logic documentation
  - [ ] `MAX_ITERATIONS` - Workflow iteration limit
- [ ] Document how to get API keys (with links)
- [ ] Add examples of valid configuration values
- [ ] Explain optional vs required variables

### 3. LangGraph Configuration
- [ ] Document `langgraph.json` structure
- [ ] Explain the `legal_consultant` graph configuration
- [ ] Document how to modify graph settings
- [ ] Add troubleshooting for LangGraph Studio integration

### 4. Running the Application
- [ ] Document different execution methods:
  - [ ] Direct Python execution: `python main.py`
  - [ ] LangGraph CLI usage
  - [ ] LangGraph Studio integration
- [ ] Add command-line argument documentation (if applicable)
- [ ] Document expected output and behavior
- [ ] Add troubleshooting section for common runtime errors

### 5. Development Setup
- [ ] Document development dependencies
- [ ] Add linting/formatting setup (if applicable)
- [ ] Document testing setup (if tests exist)
- [ ] Add contribution guidelines

### 6. Dependencies Documentation
- [ ] Explain each requirement in requirements.txt:
  - [ ] `langgraph` - Core orchestration
  - [ ] `langchain-google-genai` - LLM provider
  - [ ] `langchain-community` - Tools and utilities
  - [ ] `requests` - HTTP client
  - [ ] `python-dotenv` - Environment management
  - [ ] `pydantic` - Data validation
  - [ ] `duckduckgo-search` / `ddgs` - Search tool
  - [ ] `langgraph-studio` - Visual debugging
  - [ ] `langgraph-cli[inmem]` - CLI tools
- [ ] Document version compatibility
- [ ] Add dependency update guidelines

## Proposed Improvements

### Documentation Files to Create
1. `docs/INSTALLATION.md` - Comprehensive installation guide
2. `docs/CONFIGURATION.md` - Environment and settings guide
3. `docs/RUNNING.md` - Execution and usage guide
4. `docs/TROUBLESHOOTING.md` - Common issues and solutions
5. `docs/DEVELOPMENT.md` - Development setup guide

### Sections to Add to README
1. Detailed prerequisites section
2. Step-by-step installation walkthrough
3. Configuration examples
4. First-run guide
5. Troubleshooting quick reference

### Examples to Provide
1. Complete `.env` file example with real values
2. Virtual environment setup commands for different platforms
3. Installation verification script
4. Example queries and expected outputs

## Acceptance Criteria
- [ ] Installation process is documented step-by-step
- [ ] All environment variables are explained
- [ ] Multiple platform instructions provided
- [ ] Troubleshooting section included
- [ ] Example configurations provided
- [ ] First-run experience is documented

## Additional Context
Reference files:
- `.env.example` - Environment template
- `requirements.txt` - Dependencies
- `langgraph.json` - LangGraph configuration
- `main.py` - Entry point
- `.python-version` - Python version specification
