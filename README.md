# Agentic AI with Tool Skills

## Description

This project implements a simple tool-using AI agent in Python. The agent analyzes a user question, selects an appropriate tool, executes it, and generates a final answer based on the obtained result.

Implemented tools:

* Web search using DuckDuckGo Search
* Currency conversion using the Frankfurter API
* Arithmetic and symbolic calculations using SymPy

The system also records an execution trace containing the selected tool, tool output, execution status, and final answer.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

Open the Jupyter Notebook and run all cells.

Example:

```python
agent = ToolUseAgent(max_steps=4)

result = agent.run(
    "What is the capital of Austria and its current population?"
)

print(result["answer"])
display(result["trace"])
```

## Output

For each query, the agent produces:

* Selected tool
* Tool output
* Execution trace
* Final answer
