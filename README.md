# LangChain-Langraph-Playground

A playground repo for some LLM projects built with LangChain and LangGraph.

## Prerequisites

uv: 
Python3.12 >= higher: 
Ollama (Optional):

## Setup the environment

Create `.env` file in the root project and populate it with the following environment variables:

```
OPENAI_API_KEY=<your-openai-api-key>
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=<your_langsmith_api_key>
LANGSMITH_PROJECT=<your_project_name>
```

## Using local models with Ollama

### List downloaded models

`ollama list`

### Download a local model

To download a local model using Ollama run: `ollama pull <model_name>` example: `ollama pull gemma3:270m`

### Run the local model

To run the local model: `ollama run <model_name>` example: `ollama run gemma3:270m`.

## Notes

If you encounter SSL errors during the project install `pip-system-certs`: `uv add pip-system-certs`

