# LangLawyer

LangLawer is an AI-powered legal assistant application built using LangGraph and LangChain. It orchestrates a multi-agent workflow to analyze legal queries, conduct research, and draft comprehensive responses. The system is modular, extensible, and designed for legal professionals, researchers, and anyone needing structured legal insights.

## Features

* **Multi-Agent Workflow** : The application uses four specialized agents:
* **Supervisor** : Manages the workflow, delegates tasks, and controls the flow between agents.
* **Researcher** : Gathers relevant legal information and resources.
* **Analyzer** : Interprets and analyzes the research findings.
* **Drafter** : Prepares draft responses based on analysis.
* **Stateful Orchestration** : The workflow tracks messages, agent contributions, and iterations, ensuring a controlled and repeatable process.
* **Automated Synthesis** : After agent contributions, the system synthesizes a final legal response, structured as:

1. Overview
2. Key Rights
3. Steps
4. Disclaimer

* **Extensible Design** : Easily add new agents or modify workflow logic for custom legal tasks.
* **LangChain & LangGraph Integration** : Leverages powerful language models and graph-based orchestration for robust AI reasoning.

## How It Works

* The workflow starts with the Supervisor agent.
* Based on the query and workflow state, tasks are routed to Researcher, Analyzer, or Drafter.
* Each agent contributes to the solution, looping back to the Supervisor for further coordination.
* After sufficient iterations or upon completion, the Synthesizer compiles all contributions into a final, structured legal response.

## Project Structure

```
src/
  agents/
    supervisor.py
    researcher.py
    analyzer.py
    drafter.py
  graph/
    workflow.py      # Main workflow logic
  prompts/
    ...              # Agent prompt templates
  tools/
    legal_tools.py   # Utility functions
  utils/
    model_utils.py   # LLM management
    json_utils.py
main.py 
requirements.txt
README.md
```

## Getting Started

1. **Install dependencies** :

   ```
   pip-compile -r -v requirements.in -o 
   requirements.txt --max-rounds 10
   ```

   pip install -r requirements.txt

   ```

   ```
2. **Configure environment** (optional):

   * Add API keys or secrets to a [.env](vscode-file://vscode-app/Applications/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) file if required.
3. **Run the application** :

* Use LangGraph CLI or integrate with LangGraph Studio for visual debugging.

## Customization

* **Add/Modify Agents** : Edit files in [agents](vscode-file://vscode-app/Applications/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) to change agent behavior.
* **Change Workflow Logic** : Update [workflow.py](vscode-file://vscode-app/Applications/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) to adjust orchestration, add new nodes, or change synthesis logic.
* **Prompts** : Customize agent prompts in [prompts](vscode-file://vscode-app/Applications/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html).

## Contributing

We welcome contributions! Here's how you can help:

### Documentation Improvements

We have comprehensive documentation needs tracked in issue templates. See [DOCUMENTATION_ISSUES.md](DOCUMENTATION_ISSUES.md) for a complete overview or visit our [issue templates](.github/ISSUE_TEMPLATE/) to contribute:

- **Workflow Documentation** - Help document the multi-agent workflow system
- **Setup Documentation** - Improve installation and configuration guides
- **Agent Documentation** - Document individual agent implementations
- **API Documentation** - Document integrations and extensibility
- **Testing Documentation** - Add testing guides and examples
- **Error Handling** - Improve troubleshooting and debugging docs

### How to Contribute

1. Check existing [issues](https://github.com/Sabyasachi-Seal/LangLawyer/issues)
2. Choose an issue template from `.github/ISSUE_TEMPLATE/`
3. Create an issue or comment on existing ones
4. Submit a pull request with your improvements

## Changelog

### 2025-01-03

- **Generate documentation issues and templates** (GitHub Copilot)
  - Added comprehensive issue templates for workflow and setup documentation
  - Created DOCUMENTATION_ISSUES.md guide
  - Added 7 detailed issue templates covering all documentation needs

### 2025-30-02

- **Update .env.example with correct API keys and add README.md for project documentation** (Sabyasachi-Seal)
  - Added comprehensive README documentation
  - Updated .env.example with proper API key placeholders

## License

This project is licensed under the terms of the LICENSE file in the repository.
