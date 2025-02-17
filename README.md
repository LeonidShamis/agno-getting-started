
# Getting started examples of using Agno library

## Installation

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ollama setup

Visit https://ollama.com/download and download and install Ollama

Pull Ollama models that you want to use, for example:

```
ollama pull llama3.2:3b-instruct-q8_0
ollama pull llama3.1:8b
```

Embeddings models:

```
ollama pull mxbai-embed-large
ollama pull nomic-embed-text
ollama pull snowflake-arctic-embed2
ollama pull bge-m3
```

## Configuration

```
cp example.env .env
```

Configure your environment variables in the `.env` file

**SUGGESTION**: set OLLAMA_HOST=YOUR-OLLAMA-HOST-IP-ADDRESS to be a real IP address of your Ollama host - this works better when eventually running with Docker

## Examples of using Ollama with local LLMs

```
python ollama_examples/basic_agent.py
python ollama_examples/agent_with_tools.py
python ollama_examples/agent_with_knowledge.py
python ollama_examples/agent_with_knowledge_ollama_embedder.py
```

**NOTE**: the following examples currently fail due to Pydantic validation

```
python ollama_examples/agent_with_storage.py
python ollama_examples/agent_team.py
python ollama_examples/agent_team_news_agency.py
```

## Examples of using inference with GROQ Cloud Free Tier

Set GROQ_API_KEY in the terminal or in the .env file:

```
export GROQ_API_KEY=YOUR-GROQ-CLOUD-API-KEY
```

```
python groq_examples/agent_team.py
```
