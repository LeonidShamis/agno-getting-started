# https://docs.agno.com/examples/concepts/embedders/ollama-embedder

# Use Ollama and Ollama Embedder

from agno.vectordb.lancedb import LanceDb, SearchType

from agno.embedder.ollama import OllamaEmbedder
import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_MODEL_NAME = os.getenv("OLLAMA_MODEL_NAME", "llama3.2:3b-instruct-q8_0")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "localhost")

embedder=OllamaEmbedder(id="mxbai-embed-large", host=OLLAMA_HOST)
embeddings = embedder.get_embedding("chicken and galangal in coconut milk soup")

# Print the embeddings and their dimensions
print(f"Embeddings: {embeddings[:5]}")
print(f"Dimensions: {len(embeddings)}")
