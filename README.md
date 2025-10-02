# LangLawer

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
   pip install -r requirements.txt
   ```

```

```

1. **Configure environment** (optional):
   * Add API keys or secrets to a [.env](vscode-file://vscode-app/Applications/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) file if required.
2. **Run the application** :

* Use LangGraph CLI or integrate with LangGraph Studio for visual debugging.

## Customization

* **Add/Modify Agents** : Edit files in [agents](vscode-file://vscode-app/Applications/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) to change agent behavior.
* **Change Workflow Logic** : Update [workflow.py](vscode-file://vscode-app/Applications/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html) to adjust orchestration, add new nodes, or change synthesis logic.
* **Prompts** : Customize agent prompts in [prompts](vscode-file://vscode-app/Applications/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html).

## License

This project is licensed under the terms of the LICENSE file in the repository.
