# Agentic AI with Tool Skills

## Description

This project implements a simple AI agent that can automatically select and use external tools to answer user questions.

The agent supports:

* Web search using DuckDuckGo Search
* Currency conversion using the Frankfurter API
* Arithmetic and symbolic calculations

The system records an execution trace containing the selected tool, tool output, execution status, and final answer.

## Requirements

* Python 3.10+
* pandas
* requests
* duckduckgo-search
* sympy
* transformers
* torch

## Installation

Install the required packages:

```bash
pip install pandas requests duckduckgo-search sympy transformers torch
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

## Example Tools

* `search_web()` – retrieves information from the web.
* `convert_currency()` – converts currencies using live exchange rates.
* `calculate()` – performs arithmetic and symbolic calculations.

## Output

For each query the system produces:

1. Selected tool
2. Tool result
3. Execution trace
4. Final answer
