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

### Troubleshooting local models

If you are under a proxy and `ollama pull <model_name>` times out follow these steps:

1. Download the model `gguf` file. Example: `Qwen3-1.7B-Q8_0.gguf`
2. Create a `models` folder: `mkdir C:\models`
3. Place the gguf file inside the models directory: `move C:\Qwen3-1.7B-Q8_0.gguf C:\models\`
4. Rename the model to something simpler, for example: `qwen3.gguf`
5. Create a `Modelfile`: `notepad C:\models\Modelfile` and place this exact text inside this file: `FROM ./qwen3.gguf`
6. Create the model from the Modelfile: `ollama create qwen-local -f Modelfile`
7. Run the model: `ollama run qwen-local`
8. Serve the model so you can use it in your application: `ollama serve`

## Notes

If you encounter SSL errors during the project install `pip-system-certs`: `uv add pip-system-certs`

